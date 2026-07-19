#!/usr/bin/env python3
"""
proximity_sweep.py — Exhaustive co-occurrence sweep of "seeing" and "taking"
verbs in the Hebrew Bible.

Data source: OpenScriptures Hebrew Bible (MorphHB), Westminster Leningrad Codex,
per-word Strong's + morphology, at
    https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/<OSIS>.xml
WLC text is Public Domain; the lemma/morphology layer is CC BY 4.0
("Open Scriptures Hebrew Bible Project", https://hb.openscriptures.org/).

What it does:
  1. Fetches/caches all 39 OT book XML files.
  2. Parses every <w> element: the `lemma` attribute IS the Strong's number
     (prefixes glued with '/', homograph suffix as " a"/" b"). Aligns the `morph`
     segments so each matched lemma keeps its part-of-speech / stem.
  3. Flags each word as SEEING, TAKING, or DESIRE if any of its Strong's numbers
     is in the corresponding lemma set (below).
  4. Emits every verse-pair (seeing-verse, taking-verse) within a proximity
     window, tiered by verse distance, with the desire-terms found in the span.

Output: research/data/cooccurrences.csv, research/data/cooccurrences.json,
        research/data/summary.json
"""

import csv
import json
import os
import re
import sys
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict

# --------------------------------------------------------------------------- #
# Lemma sets (Strong's numbers). Numbers are the base integers; the MorphHB
# "augmented" homograph suffix (e.g. "7200", "2530 a") is normalised to the int.
# --------------------------------------------------------------------------- #
SEEING = {
    7200: ("ra'ah", "רָאָה", "see, look, perceive"),
    2372: ("chazah", "חָזָה", "see, behold (esp. in vision)"),
    5027: ("nabat", "נָבַט", "look, regard, gaze (usu. Hiphil)"),
    8259: ("shaqaph", "שָׁקַף", "look down / out"),
    7789: ("shur", "שׁוּר", "behold, regard, look"),
    6822: ("tsaphah", "צָפָה", "look out, keep watch"),
    8159: ("sha'ah", "שָׁעָה", "gaze at, look toward"),
}
TAKING = {
    3947: ("laqach", "לָקַח", "take, seize, fetch, marry"),
    270:  ("achaz", "אָחַז", "grasp, take hold, seize"),
    8610: ("taphas", "תָּפַשׂ", "seize, grasp, catch, wield"),
    3920: ("lakad", "לָכַד", "capture, seize, catch"),
    1497: ("gazal", "גָּזַל", "seize, tear away, rob"),
    5375: ("nasa", "נָשָׂא", "lift, carry, take up  [flagged: 'lift eyes' idiom]"),
}
DESIRE = {  # the "middle term" of the see -> desire -> take sequence
    2530: ("chamad", "חָמַד", "desire, covet, take pleasure in"),
    183:  ("avah", "אָוָה", "desire, long for, crave"),
    8378: ("ta'avah", "תַּאֲוָה", "desire, longing (noun)"),
    2836: ("chashaq", "חָשַׁק", "be attached to, long for, desire"),
}

BOOKS = [
    "Gen", "Exod", "Lev", "Num", "Deut", "Josh", "Judg", "Ruth", "1Sam", "2Sam",
    "1Kgs", "2Kgs", "1Chr", "2Chr", "Ezra", "Neh", "Esth", "Job", "Ps", "Prov",
    "Eccl", "Song", "Isa", "Jer", "Lam", "Ezek", "Dan", "Hos", "Joel", "Amos",
    "Obad", "Jonah", "Mic", "Nah", "Hab", "Zeph", "Hag", "Zech", "Mal",
]

# Human-readable book names for output.
BOOK_NAMES = {
    "Gen": "Genesis", "Exod": "Exodus", "Lev": "Leviticus", "Num": "Numbers",
    "Deut": "Deuteronomy", "Josh": "Joshua", "Judg": "Judges", "Ruth": "Ruth",
    "1Sam": "1 Samuel", "2Sam": "2 Samuel", "1Kgs": "1 Kings", "2Kgs": "2 Kings",
    "1Chr": "1 Chronicles", "2Chr": "2 Chronicles", "Ezra": "Ezra",
    "Neh": "Nehemiah", "Esth": "Esther", "Job": "Job", "Ps": "Psalms",
    "Prov": "Proverbs", "Eccl": "Ecclesiastes", "Song": "Song of Songs",
    "Isa": "Isaiah", "Jer": "Jeremiah", "Lam": "Lamentations", "Ezek": "Ezekiel",
    "Dan": "Daniel", "Hos": "Hosea", "Joel": "Joel", "Amos": "Amos",
    "Obad": "Obadiah", "Jonah": "Jonah", "Mic": "Micah", "Nah": "Nahum",
    "Hab": "Habakkuk", "Zeph": "Zephaniah", "Hag": "Haggai", "Zech": "Zechariah",
    "Mal": "Malachi",
}

WINDOW = 5          # max verse distance to count as "proximity"
RAW_URL = "https://raw.githubusercontent.com/openscriptures/morphhb/master/wlc/{}.xml"
OSIS_NS = "http://www.bibletechnologies.net/2003/OSIS/namespace"

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
DATA_DIR = os.path.join(REPO, "research", "data")
# Cache WLC XML outside the repo (it is the upstream source, not our artifact).
CACHE_DIR = os.environ.get("WLC_CACHE", os.path.join(HERE, ".wlc_cache"))


def fetch_book(osis):
    os.makedirs(CACHE_DIR, exist_ok=True)
    path = os.path.join(CACHE_DIR, osis + ".xml")
    if not os.path.exists(path) or os.path.getsize(path) < 1000:
        url = RAW_URL.format(osis)
        with urllib.request.urlopen(url, timeout=60) as r:
            data = r.read()
        with open(path, "wb") as f:
            f.write(data)
    return path


def strongs_from_lemma(lemma):
    """Return list of (int_strongs, augmented_lemma_str) for numeric segments."""
    out = []
    for seg in lemma.split("/"):
        seg = seg.strip()
        if not seg:
            continue
        m = re.match(r"^(\d+)", seg)
        if m:
            out.append((int(m.group(1)), seg))
    return out


def morph_segments(morph):
    """Split morph into per-segment codes, dropping the leading language char."""
    if not morph:
        return []
    parts = morph.split("/")
    if parts and parts[0] and parts[0][0] in ("H", "A"):
        parts[0] = parts[0][1:]
    return parts


def parse_book(osis, path):
    """Return list of verse dicts in document order for one book."""
    tree = ET.parse(path)
    root = tree.getroot()
    verse_tag = f"{{{OSIS_NS}}}verse"
    w_tag = f"{{{OSIS_NS}}}w"
    verses = []
    for verse in root.iter(verse_tag):
        osis_id = verse.get("osisID")
        if not osis_id:
            continue
        # osisID like "Gen.3.6"; some verses carry multiple ids "Gen.3.6 Gen.3.7"
        first_id = osis_id.split()[0]
        _, chap, vs = first_id.split(".")
        words = []
        for w in verse.iter(w_tag):
            lemma = w.get("lemma", "")
            morph = w.get("morph", "")
            form = "".join(w.itertext())
            nums = strongs_from_lemma(lemma)
            msegs = morph_segments(morph)
            lsegs = [s.strip() for s in lemma.split("/") if s.strip()]
            # Map each numeric lemma segment to its aligned morph code.
            pos_by_num = {}
            for i, seg in enumerate(lsegs):
                mm = re.match(r"^(\d+)", seg)
                if mm:
                    code = msegs[i] if i < len(msegs) else ""
                    pos_by_num[int(mm.group(1))] = code
            words.append({
                "form": form,
                "lemma": lemma,
                "morph": morph,
                "nums": [n for n, _ in nums],
                "pos_by_num": pos_by_num,
            })
        verses.append({
            "book": osis, "chap": int(chap), "verse": int(vs),
            "ref": f"{BOOK_NAMES[osis]} {chap}:{vs}",
            "osis": first_id, "words": words,
        })
    return verses


def category_hits(verse, lemma_set):
    """Return list of (num, name, hebrew, form, morph_code) for set matches."""
    hits = []
    for w in verse["words"]:
        for num in w["nums"]:
            if num in lemma_set:
                name, heb, _gloss = lemma_set[num]
                hits.append({
                    "num": num, "name": name, "hebrew": heb,
                    "form": w["form"], "pos": w["pos_by_num"].get(num, ""),
                })
    return hits


def is_nasa_eyes(verse):
    """True if this verse's nasa (5375) is the 'lift eyes' seeing idiom
    (nasa + 'ayin/'enayim, Strong's 5869)."""
    has_nasa = any(5375 in w["nums"] for w in verse["words"])
    has_eyes = any(5869 in w["nums"] for w in verse["words"])
    return has_nasa and has_eyes


def main():
    os.makedirs(DATA_DIR, exist_ok=True)
    all_verses = {}      # book -> ordered verse list
    for osis in BOOKS:
        path = fetch_book(osis)
        all_verses[osis] = parse_book(osis, path)
        sys.stderr.write(f"parsed {osis}: {len(all_verses[osis])} verses\n")

    rows = []
    seen_pairs = set()
    for osis in BOOKS:
        verses = all_verses[osis]
        # index verses that carry seeing / taking / desire terms
        seeing_idx, taking_idx, desire_idx = {}, {}, {}
        for i, v in enumerate(verses):
            s = category_hits(v, SEEING)
            t = category_hits(v, TAKING)
            d = category_hits(v, DESIRE)
            if s:
                seeing_idx[i] = s
            if t:
                taking_idx[i] = t
            if d:
                desire_idx[i] = d

        for ti, thits in taking_idx.items():
            for si, shits in seeing_idx.items():
                dist = abs(ti - si)
                if dist > WINDOW:
                    continue
                key = (osis, si, ti)
                if key in seen_pairs:
                    continue
                seen_pairs.add(key)
                lo, hi = min(si, ti), max(si, ti)
                # desire terms anywhere in the spanned verses
                span_desire = []
                for di, dhits in desire_idx.items():
                    if lo <= di <= hi:
                        for h in dhits:
                            span_desire.append(f"{h['name']} {h['hebrew']} ({verses[di]['ref']})")
                tier = 1 if dist == 0 else (2 if dist <= 2 else 3)
                # Does the taking term include only nasa, and is it the 'lift eyes' idiom?
                taking_nums = {h["num"] for h in thits}
                nasa_eyes_flag = (taking_nums == {5375} and is_nasa_eyes(verses[ti]))
                rows.append({
                    "book": BOOK_NAMES[osis],
                    "osis_book": osis,
                    "seeing_ref": verses[si]["ref"],
                    "seeing_osis": verses[si]["osis"],
                    "seeing_terms": "; ".join(
                        f"{h['name']} {h['hebrew']} [{h['form']}]" for h in shits),
                    "seeing_lemmas": ",".join(str(h["num"]) for h in shits),
                    "taking_ref": verses[ti]["ref"],
                    "taking_osis": verses[ti]["osis"],
                    "taking_terms": "; ".join(
                        f"{h['name']} {h['hebrew']} [{h['form']}]" for h in thits),
                    "taking_lemmas": ",".join(str(h["num"]) for h in thits),
                    "verse_distance": dist,
                    "tier": tier,
                    "desire_in_span": " | ".join(span_desire),
                    "has_desire": bool(span_desire),
                    "nasa_lift_eyes_idiom": nasa_eyes_flag,
                    "category": "",  # filled during manual/agent adjudication
                })

    # sort by canonical book order, then chapter/verse of the earlier ref
    order = {b: i for i, b in enumerate(BOOKS)}

    def sort_key(r):
        so = r["seeing_osis"].split(".")
        to = r["taking_osis"].split(".")
        anchor = min((int(so[1]), int(so[2])), (int(to[1]), int(to[2])))
        return (order[r["osis_book"]], anchor[0], anchor[1])

    rows.sort(key=sort_key)

    # ---- write CSV ----
    csv_path = os.path.join(DATA_DIR, "cooccurrences.csv")
    fields = ["book", "seeing_ref", "seeing_terms", "seeing_lemmas",
              "taking_ref", "taking_terms", "taking_lemmas", "verse_distance",
              "tier", "has_desire", "desire_in_span", "nasa_lift_eyes_idiom",
              "category"]
    with open(csv_path, "w", newline="", encoding="utf-8") as f:
        wtr = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        wtr.writeheader()
        for r in rows:
            wtr.writerow(r)

    # ---- write JSON ----
    with open(os.path.join(DATA_DIR, "cooccurrences.json"), "w",
              encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)

    # ---- summary ----
    by_tier = defaultdict(int)
    by_book = defaultdict(lambda: defaultdict(int))
    with_desire = 0
    nasa_eyes = 0
    excl_nasa_eyes_by_tier = defaultdict(int)
    for r in rows:
        by_tier[r["tier"]] += 1
        by_book[r["book"]][r["tier"]] += 1
        if r["has_desire"]:
            with_desire += 1
        if r["nasa_lift_eyes_idiom"]:
            nasa_eyes += 1
        else:
            excl_nasa_eyes_by_tier[r["tier"]] += 1

    summary = {
        "window_verses": WINDOW,
        "total_pairs": len(rows),
        "by_tier": dict(sorted(by_tier.items())),
        "by_tier_excluding_nasa_lift_eyes_idiom":
            dict(sorted(excl_nasa_eyes_by_tier.items())),
        "pairs_with_desire_term_in_span": with_desire,
        "nasa_lift_eyes_idiom_pairs": nasa_eyes,
        "seeing_lemmas": {str(k): v[0] for k, v in SEEING.items()},
        "taking_lemmas": {str(k): v[0] for k, v in TAKING.items()},
        "desire_lemmas": {str(k): v[0] for k, v in DESIRE.items()},
        "by_book": {b: dict(sorted(t.items())) for b, t in by_book.items()},
    }
    with open(os.path.join(DATA_DIR, "summary.json"), "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    # ---- console report ----
    print(f"TOTAL verse-pairs (window <= {WINDOW}): {len(rows)}")
    print(f"  Tier 1 (same verse):      {by_tier[1]}")
    print(f"  Tier 2 (1-2 verses):      {by_tier[2]}")
    print(f"  Tier 3 (3-5 verses):      {by_tier[3]}")
    print(f"  with a desire-term in span: {with_desire}")
    print(f"  nasa 'lift eyes' idiom pairs (flagged): {nasa_eyes}")

    # sanity checks on the anchor passages
    anchors = ["Genesis 3:6", "Genesis 6:2", "Genesis 12:14", "Genesis 12:15",
               "Genesis 34:2", "Genesis 38:2", "Exodus 2:5", "Exodus 2:6",
               "Joshua 7:21", "2 Samuel 11:2", "2 Samuel 11:4"]
    print("\nAnchor check (does each appear as a seeing or taking ref?):")
    refs_seen = {r["seeing_ref"] for r in rows} | {r["taking_ref"] for r in rows}
    for a in anchors:
        print(f"  {a:16s} {'OK' if a in refs_seen else 'MISSING'}")


if __name__ == "__main__":
    main()

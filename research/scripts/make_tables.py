#!/usr/bin/env python3
"""Generate Markdown catalog tables + a per-book summary from cooccurrences.json.

Writes partials into research/data/ for inclusion/reference while assembling
the report. Deterministic: the tables contain EVERY row in the catalog, so the
"every single instance" claim is auditable against these files and the CSV.
"""
import json
import os
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))
rows = json.load(open(os.path.join(DATA, "cooccurrences.json"), encoding="utf-8"))

BOOKS = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua","Judges",
    "Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles","2 Chronicles",
    "Ezra","Nehemiah","Esther","Job","Psalms","Proverbs","Ecclesiastes",
    "Song of Songs","Isaiah","Jeremiah","Lamentations","Ezekiel","Daniel","Hosea",
    "Joel","Amos","Obadiah","Jonah","Micah","Nahum","Habakkuk","Zephaniah",
    "Haggai","Zechariah","Malachi"]
order = {b: i for i, b in enumerate(BOOKS)}


def strip_prefix(form):
    return form  # keep vocalised form with maqqef-split prefixes as-is


def terms_short(cell):
    # cell like "ra'ah רָאָה [וַ/יַּ֨רְא]; ..." -> keep name + form
    return cell.replace(" [", " ").replace("]", "")


def row_refs(r):
    if r["seeing_ref"] == r["taking_ref"]:
        return r["seeing_ref"]
    return f"{r['seeing_ref']} → {r['taking_ref']}"


def table(rows_subset, header_note=""):
    out = []
    out.append("| # | Reference(s) | Seeing | Taking | Δ | Desire term in span |")
    out.append("|---|---|---|---|---|---|")
    for i, r in enumerate(rows_subset, 1):
        des = r["desire_in_span"] if r["has_desire"] else ""
        idiom = " _(nasa 'lift-eyes' idiom)_" if r["nasa_lift_eyes_idiom"] else ""
        out.append("| {} | {} | {} | {}{} | {} | {} |".format(
            i, row_refs(r), terms_short(r["seeing_terms"]),
            terms_short(r["taking_terms"]), idiom, r["verse_distance"], des))
    return "\n".join(out)


def sort_rows(rs):
    def k(r):
        so = r["seeing_osis"].split("."); to = r["taking_osis"].split(".")
        anchor = min((int(so[1]), int(so[2])), (int(to[1]), int(to[2])))
        return (order.get(r["book"], 99), anchor[0], anchor[1])
    return sorted(rs, key=k)


for tier, fname in [(1, "_tier1_table.md"), (2, "_tier2_table.md"),
                    (3, "_tier3_table.md")]:
    sub = sort_rows([r for r in rows if r["tier"] == tier])
    with open(os.path.join(DATA, fname), "w", encoding="utf-8") as f:
        f.write(table(sub))
    print(f"{fname}: {len(sub)} rows")

# per-book summary
by_book = defaultdict(lambda: {1: 0, 2: 0, 3: 0, "desire": 0, "idiom": 0})
for r in rows:
    by_book[r["book"]][r["tier"]] += 1
    if r["has_desire"]:
        by_book[r["book"]]["desire"] += 1
    if r["nasa_lift_eyes_idiom"]:
        by_book[r["book"]]["idiom"] += 1

lines = ["| Book | Tier 1 | Tier 2 | Tier 3 | Total | w/ desire | idiom-flagged |",
         "|---|---|---|---|---|---|---|"]
tot = {1: 0, 2: 0, 3: 0, "desire": 0, "idiom": 0, "all": 0}
for b in BOOKS:
    if b not in by_book:
        continue
    d = by_book[b]
    allc = d[1] + d[2] + d[3]
    lines.append(f"| {b} | {d[1]} | {d[2]} | {d[3]} | {allc} | {d['desire']} | {d['idiom']} |")
    for k in (1, 2, 3, "desire", "idiom"):
        tot[k] += d[k]
    tot["all"] += allc
lines.append(f"| **Total** | **{tot[1]}** | **{tot[2]}** | **{tot[3]}** | **{tot['all']}** | **{tot['desire']}** | **{tot['idiom']}** |")
with open(os.path.join(DATA, "_bybook_table.md"), "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print("_bybook_table.md written")

# dump Tier-1 for classification (plain text)
t1 = sort_rows([r for r in rows if r["tier"] == 1])
with open(os.path.join(DATA, "_tier1_for_classification.txt"), "w", encoding="utf-8") as f:
    for r in t1:
        f.write(f"{row_refs(r)} | see={terms_short(r['seeing_terms'])} | "
                f"take={terms_short(r['taking_terms'])} | "
                f"desire={r['desire_in_span'] if r['has_desire'] else '-'} | "
                f"idiom={r['nasa_lift_eyes_idiom']}\n")
print(f"_tier1_for_classification.txt: {len(t1)} rows")

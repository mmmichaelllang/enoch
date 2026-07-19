# research/ — Seeing & Taking word-study

A corpus-driven study of every place in the Hebrew Bible where a verb of **seeing**
and a verb of **taking** occur in close proximity — the *"saw … and took"* motif
(Gen 3:6; 6:2; Josh 7:21; 2 Sam 11:2–4; …) — with a survey of theological
interpretation.

The report itself is **[`seeing-and-taking.md`](seeing-and-taking.md)**.

## What's here

```
research/
├── seeing-and-taking.md      # the report (start here)
├── data/
│   ├── cooccurrences.csv      # canonical catalogue: every co-occurring verse-pair
│   ├── cooccurrences.json     # same, as JSON
│   ├── summary.json           # aggregate counts
│   └── tier1_categories.json  # hand-adjudicated Tier-1 categories
└── scripts/
    ├── proximity_sweep.py     # fetch MorphHB → parse lemmas → tiered co-occurrence sweep
    ├── make_tables.py         # render the catalogue tables
    └── classify_tier1.py      # attach category + gloss to each same-verse hit
```

## Reproducing the catalogue

```bash
python3 research/scripts/proximity_sweep.py   # writes data/cooccurrences.{csv,json}, summary.json
python3 research/scripts/make_tables.py        # writes the tier / per-book tables
python3 research/scripts/classify_tier1.py     # writes data/_tier1_classified.md, tier1_categories.json
```

The sweep fetches the tagged Hebrew text over the network on first run and caches
it outside the repo (set `WLC_CACHE` to choose the cache directory). No third-party
Python packages are required (standard library only).

## Method in brief

- **Text:** Westminster Leningrad Codex via the **Open Scriptures Hebrew Bible
  (MorphHB)** project — every word tagged with its Strong's-number lemma and
  morphology. WLC text is public domain; the morphology layer is **CC BY 4.0**
  (© Open Scriptures Hebrew Bible Project, <https://hb.openscriptures.org/>).
- **Seeing (7 verbs):** רָאָה, חָזָה, נָבַט, שָׁקַף, שׁוּר, צָפָה, שָׁעָה.
- **Taking (6 verbs):** לָקַח, אָחַז, תָּפַשׂ, לָכַד, גָּזַל, נָשָׂא *(flagged — see the report §2.5)*.
- **Desire (middle term):** חָמַד, אָוָה, תַּאֲוָה, חָשַׁק.
- **Proximity:** Tier 1 = same verse; Tier 2 = 1–2 verses; Tier 3 = 3–5 verses.

See the report's Method section for the full rationale, the *nāśāʾ* "lift-eyes"
caveat, and the citation-integrity policy.

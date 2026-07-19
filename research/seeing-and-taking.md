# Seeing and Taking: A Complete Catalogue of the רָאָה / לָקַח Motif in the Hebrew Scriptures

*A corpus-driven word-study with a survey of theological interpretation*

> **Scope.** This report documents **every instance** in the Hebrew Bible (Tanakh) where a verb of *seeing* and a verb of *taking* occur within close proximity of one another, classifies each occurrence, and surveys how interpreters — ancient, rabbinic, patristic, and modern — have read the pattern. The catalogue was produced not from memory but by a reproducible sweep of a morphologically tagged Hebrew text, so that the claim "every instance" is auditable against the data files and scripts that accompany it.

> **A note on method and provenance.** This study was requested as a "deepest-dive" research report. The bespoke citation pipeline of that name (an OpenAlex resolver over a persistent source database, built to *refuse to fabricate* references) was not available in the environment where the report was assembled; its discipline was preserved by hand. Every scholarly attribution below is tagged **[confirmed]** (a real, located source, verified while preparing this report) or **[general-knowledge]** (a standard attribution to a real work that was not re-opened here and should be checked against the text before it is quoted). No quotations, page numbers, or DOIs have been invented. Scripture is cited in the ESV unless noted.

---

## Abstract

Across the Hebrew Bible the sequence *"he saw … and he took"* recurs at moments of consequence: Eve and the tree (Gen 3:6), the sons of God and the daughters of men (Gen 6:2), Achan and the spoil of Jericho (Josh 7:21), David and Bathsheba (2 Sam 11:2–4). A complete morphological sweep of the Westminster Leningrad Codex for seven verbs of seeing and six of taking, within a five-verse window, yields **1,298 co-occurring verse-pairs**. Filtering reveals that the raw total is inflated by a single idiom — *nāśāʾ ʿênayim*, "to lift the eyes (and see)" — which accounts for a large share of apparent "takings" but denotes vision, not acquisition. Once that idiom and the non-acquisitive senses of *nāśāʾ* are set aside, the genuinely acquisitive *"saw … took"* collocation is carried almost entirely by one verb, **לָקַח (lāqaḥ)**, and clusters at a small number of theologically weighted scenes. In exactly **three verses** the full triad *see → desire → take* appears together lexically — Genesis 3:6, Joshua 7:21, and Deuteronomy 21:11 — precisely the texts (the Fall, Achan's theft, the captive-bride law) around which the interpretive tradition has concentrated. The report presents the complete catalogue, a passage-by-passage analysis of the significant nodes, and a survey of the theological literature from *1 Enoch* to modern narrative criticism.

---

## 1. The question

The Hebrew narrator is sparing with interior life. Motive is most often conveyed not by comment but by a chain of verbs, and one chain in particular has long drawn the attention of readers: a person **sees** something desirable and then **takes** it. The pattern is compact enough to be missed and frequent enough to be a signature. Its most famous occurrence stands at the head of the canon — "the woman **saw** that the tree was good … she **took** of its fruit and ate" (Gen 3:6) — and its verbal shape recurs when "the sons of God **saw** … and **took**" (Gen 6:2), when Achan confesses "I **saw** … I **coveted** … and **took**" (Josh 7:21), and when David "**saw** … sent messengers and **took**" (2 Sam 11:2–4).

Two questions follow. First, the empirical one: *where, exactly, and how often* do the Hebrew verbs of seeing and taking fall together — not only in these celebrated verses but everywhere? Second, the interpretive one: *what has the pattern been taken to mean* — is it a deliberate literary device, a moral diagnosis of sin, a piece of narrative artistry, or an over-read coincidence of two very common verbs?

This report answers the first question exhaustively and the second by survey. It is offered as a companion to the site on which it is published — an edition of *1 Enoch*, whose *Book of the Watchers* (chs. 6–8) is the earliest sustained meditation on one node of this very pattern, Genesis 6:2, where the watching angels "saw … and took."

---

## 2. Method

### 2.1 Corpus and data source

The base text is the **Westminster Leningrad Codex** as encoded by the **Open Scriptures Hebrew Bible (MorphHB)** project, which tags every word with its lemma (a Strong's number) and full morphology. Each word is an XML element of the form:

```xml
<w lemma="c/7200" morph="HC/Vqw3fs">וַ/תֵּ֣רֶא</w>
```

where the numeric lemma `7200` is the verb רָאָה (*rāʾāh*, "see"), the `c/` prefix is the conjunction *wa-*, and `Vqw3fs` marks a Qal *wayyiqtol* third-feminine-singular. Because the tag is the Strong's number itself, homographs are disambiguated at the source: רָאָה "see" (H7200) is never confused with the graphically similar יָרֵא "fear" (H3372). The WLC text is in the public domain; the morphology layer is used under **CC BY 4.0** (© Open Scriptures Hebrew Bible Project, <https://hb.openscriptures.org/>).

### 2.2 The lexical sets

Following the request for a *full synonym sweep*, the study does not restrict itself to the single pair רָאָה / לָקַח but gathers the principal verbs in each semantic field. Nominal derivatives (e.g. מַרְאֶה "appearance," רֹאֶה "seer") were tracked separately and are not included in the verb counts.

**Seeing (7 lemmas)**

| Strong's | Lemma | Translit. | Gloss |
|---|---|---|---|
| H7200 | רָאָה | *rāʾāh* | see, look, perceive |
| H2372 | חָזָה | *ḥāzāh* | see, behold (esp. in vision) |
| H5027 | נָבַט | *nābaṭ* | look, regard, gaze (usu. Hiphil) |
| H8259 | שָׁקַף | *šāqap* | look down / out |
| H7789 | שׁוּר | *šûr* | behold, regard |
| H6822 | צָפָה | *ṣāpāh* | look out, keep watch |
| H8159 | שָׁעָה | *šāʿāh* | gaze at, look toward |

**Taking (6 lemmas)**

| Strong's | Lemma | Translit. | Gloss |
|---|---|---|---|
| H3947 | לָקַח | *lāqaḥ* | take, seize, fetch, marry |
| H270 | אָחַז | *ʾāḥaz* | grasp, take hold, seize |
| H8610 | תָּפַשׂ | *tāpaś* | seize, grasp, catch, wield |
| H3920 | לָכַד | *lākad* | capture, seize, catch |
| H1497 | גָּזַל | *gāzal* | seize, tear away, rob |
| H5375 | נָשָׂא | *nāśāʾ* | lift, carry, take up **(see §2.5)** |

**Desire — the "middle term" (4 lemmas).** Because the classical form of the motif is *see → desire → take*, the verbs and nouns of desire were tracked in parallel, so that the presence of an explicit middle term could be flagged:

| Strong's | Lemma | Translit. | Gloss |
|---|---|---|---|
| H2530 | חָמַד | *ḥāmad* | desire, covet, take pleasure in |
| H183 | אָוָה | *ʾāwāh* | desire, long for, crave |
| H8378 | תַּאֲוָה | *taʾăwāh* | desire, longing (noun) |
| H2836 | חָשַׁק | *ḥāšaq* | be attached to, long for |

### 2.3 Proximity tiers

Every seeing-verse was paired with every taking-verse of the same book that fell within **five verses** of it. Each pair is tagged by distance:

- **Tier 1** — the two verbs stand in the **same verse** (e.g. Gen 3:6).
- **Tier 2** — they stand **one or two verses apart** (e.g. David *sees* in 2 Sam 11:2 and *takes* in 11:4).
- **Tier 3** — they stand **three to five verses apart** (a proxy for "the same immediate scene").

The five-verse ceiling is a deliberate, reproducible operationalisation of "close proximity"; it is not a claim about pericope boundaries, which the source text does not mark. Distance is measured in running verse-numbers within a book, so that adjacency across a chapter break is counted naturally.

### 2.4 Adjudication and categories

Each **Tier-1** pair — the tightest and most defensible collocations — was hand-classified into one of five categories:

- **A — Transgressive:** an illicit *see → (desire) → take* (sexual seizure or theft).
- **B — Narrative:** an ordinary "saw … took" (a report, a battle manoeuvre, a procedure).
- **C — Righteous inversion:** the pattern turned toward good (covering, sacrifice, rescue, holy zeal).
- **D — Juridical / cultic:** law, ritual, covenant, or the watchman's charge.
- **I — Idiom / non-take:** cases where the "taking" verb — almost always *nāśāʾ* — does not denote acquisition (see §2.5).

Tier-2 and Tier-3 pairs are presented in full but carry only the objective flags (distance, idiom, presence of a desire term); their semantic classification would require case-by-case judgement beyond what a proximity sweep can certify, and the notable members are treated individually in §5.

### 2.5 The *nāśāʾ* caveat — and a finding

Including נָשָׂא (*nāśāʾ*, "lift/carry/take up") in the taking set was necessary for a genuine *full* sweep, but it introduces the study's largest source of noise, and dealing with it produces one of its clearest results. In Biblical Hebrew *nāśāʾ ʿênayim*, "to **lift the eyes**," is the standard idiom for *looking*; the phrase "he lifted his eyes **and saw**" (וַיִּשָּׂא … וַיַּרְא) therefore couples a "taking" verb with a "seeing" verb in a way that has nothing to do with acquisition. The sweep flags every such case; 133 of the 1,298 pairs are so marked, and of the 131 same-verse hits, **65 turn out to be *nāśāʾ* in a non-acquisitive sense** — lifting the eyes, lifting the voice in weeping, bearing guilt, carrying a burden, or "lifting the face" (i.e. showing favour). Setting these aside is not data-trimming but lexical honesty, and it sharpens the picture: the acquisitive *"saw … took"* is overwhelmingly the work of **לָקַח**.

### 2.6 Reproducibility

Three scripts accompany this report and regenerate every number and table in it:

- `research/scripts/proximity_sweep.py` — fetches the MorphHB books, parses the lemmas, and writes the raw catalogue (`research/data/cooccurrences.csv` and `.json`, plus `summary.json`).
- `research/scripts/make_tables.py` — renders the tier and per-book tables.
- `research/scripts/classify_tier1.py` — attaches the hand-adjudicated category and gloss to each Tier-1 pair.

### 2.7 Citation-integrity policy

As noted above, the theological survey (§6) attributes positions only to real, locatable works, each tagged **[confirmed]** or **[general-knowledge]**, and every attribution used in the drafting was put through an independent adversarial verification pass; anything that could not be corroborated was down-graded to [general-knowledge] or removed. Where the survey advances a synthetic claim that no single scholar makes — for instance, that Genesis 3, Genesis 6, Joshua 7, and 2 Samuel 11 form one authored "sin-grammar" — it says so explicitly (see §7).

---

## 3. Results

### 3.1 The shape of the data

The sweep returned **1,298** co-occurring verse-pairs within the five-verse window, distributed as follows:

| Tier | Definition | Pairs |
|---|---|---|
| 1 | same verse | 131 |
| 2 | 1–2 verses apart | 454 |
| 3 | 3–5 verses apart | 713 |
| **Total** | | **1,298** |

Their distribution across the canon — with the *nāśāʾ*-idiom cases and desire-bearing spans broken out — is given per book below.

| Book | Tier 1 | Tier 2 | Tier 3 | Total | w/ desire | idiom-flagged |
|---|---|---|---|---|---|---|
| Genesis | 26 | 64 | 102 | 192 | 1 | 29 |
| Exodus | 2 | 26 | 41 | 69 | 0 | 1 |
| Leviticus | 2 | 13 | 17 | 32 | 0 | 0 |
| Numbers | 7 | 28 | 48 | 83 | 0 | 11 |
| Deuteronomy | 4 | 15 | 36 | 55 | 2 | 7 |
| Joshua | 6 | 7 | 17 | 30 | 6 | 2 |
| Judges | 8 | 23 | 26 | 57 | 0 | 1 |
| Ruth | 1 | 0 | 1 | 2 | 0 | 0 |
| 1 Samuel | 8 | 27 | 59 | 94 | 0 | 3 |
| 2 Samuel | 3 | 16 | 28 | 47 | 0 | 7 |
| 1 Kings | 2 | 12 | 21 | 35 | 0 | 0 |
| 2 Kings | 12 | 49 | 60 | 121 | 0 | 0 |
| 1 Chronicles | 3 | 9 | 13 | 25 | 0 | 5 |
| 2 Chronicles | 1 | 10 | 12 | 23 | 0 | 0 |
| Nehemiah | 0 | 2 | 1 | 3 | 0 | 0 |
| Esther | 3 | 7 | 3 | 13 | 0 | 2 |
| Job | 0 | 13 | 19 | 32 | 0 | 1 |
| Psalms | 2 | 13 | 10 | 25 | 1 | 0 |
| Proverbs | 1 | 2 | 3 | 6 | 0 | 0 |
| Ecclesiastes | 1 | 7 | 7 | 15 | 0 | 0 |
| Song of Songs | 0 | 2 | 6 | 8 | 0 | 0 |
| Isaiah | 9 | 33 | 52 | 94 | 4 | 10 |
| Jeremiah | 7 | 15 | 22 | 44 | 0 | 4 |
| Lamentations | 1 | 2 | 7 | 10 | 0 | 0 |
| Ezekiel | 11 | 34 | 61 | 106 | 0 | 20 |
| Daniel | 2 | 5 | 4 | 11 | 0 | 9 |
| Hosea | 0 | 1 | 1 | 2 | 0 | 0 |
| Amos | 0 | 3 | 8 | 11 | 0 | 0 |
| Jonah | 0 | 1 | 1 | 2 | 0 | 0 |
| Micah | 1 | 3 | 3 | 7 | 1 | 0 |
| Habakkuk | 2 | 2 | 6 | 10 | 0 | 0 |
| Zechariah | 6 | 10 | 16 | 32 | 0 | 21 |
| Malachi | 0 | 0 | 2 | 2 | 0 | 0 |
| **Total** | **131** | **454** | **713** | **1298** | **15** | **133** |


Genesis dominates the Tier-1 count (26), as one would expect of the book that establishes the pattern; the visionary books (Ezekiel, Zechariah, Daniel, Isaiah) contribute heavily but almost entirely through the *"I lifted my eyes and saw"* idiom, and the historical books (2 Kings, 1–2 Samuel) supply the bulk of the ordinary, narrative *"saw … took."*

### 3.2 The category profile of the same-verse hits

Hand-classification of all 131 Tier-1 pairs:

| Category | Meaning | Count |
|---|---|---|
| A | Transgressive (see → [desire] → take) | 8 |
| B | Ordinary narrative | 48 |
| C | Righteous inversion | 5 |
| D | Juridical / cultic | 5 |
| I | *nāśāʾ* idiom / non-take | 65 |
| **Total** | | **131** |

The eight **transgressive** same-verse cases are Genesis 3:6, 6:2, 12:15, 34:2, 38:2; Judges 14:2; Joshua 7:21; and Jeremiah 5:26. The paradigmatic case, David and Bathsheba, does **not** appear here: its *seeing* (11:2) and *taking* (11:4) are two verses apart, and it surfaces only at **Tier 2** — a reminder that the motif works across a narrative gap as well as within a verse, and that a same-verse-only search would have missed the very episode the tradition treats as its clearest example.

### 3.3 The three verses that carry the whole triad

Only **three** verses contain a seeing verb, a taking verb, **and** an explicit verb or noun of desire in the same breath:

| Reference | Seeing | Desire | Taking | Scene |
|---|---|---|---|---|
| **Genesis 3:6** | *rāʾāh* | *taʾăwāh* / *neḥmād* (*ḥāmad*) | *lāqaḥ* | Eve and the tree |
| **Joshua 7:21** | *rāʾāh* | *ḥāmad* ("I coveted") | *lāqaḥ* | Achan and the spoil |
| **Deuteronomy 21:11** | *rāʾāh* | *ḥāšaq* ("you desire") | *lāqaḥ* | the beautiful captive |

That the two *narrative* members of this trio are the Fall and Achan — the canon's two great case-studies of a coveting that brings death on a community — is the single most suggestive result of the sweep, and it is exactly where the interpreters converge (§§5–6). The third, Deuteronomy 21, is the same sequence transposed into *law*, where the pattern is not condemned but regulated and hedged with protections for the captive woman.

A further, poignant datum: the only occurrences of the desire-root *ḥāmad* near a seeing verb outside these scenes fall in **Isaiah 53:2** — "he had no form or majesty that we should look at him, and no beauty that we should **desire** him." The Servant is the deliberate *anti-type*: the one who, by the logic of the whole motif, ought to have been *seen-and-desired-and-taken* is instead the one whom no eye covets.

---

## 4. The complete catalogue

The tables below list **every** co-occurrence returned by the sweep. Tier 1 is given here with its adjudicated categories; the complete Tier-2 and Tier-3 tables follow in the appendices, and the canonical machine-readable record is `research/data/cooccurrences.csv`.

### 4.1 Tier 1 — same-verse co-occurrences (all 131, classified)

| # | Reference | Category | Seeing verb | Taking verb | Sense |
|---|---|---|---|---|---|
| 1 | Genesis 3:6 | A — Transgressive | ra'ah רָאָה וַ/תֵּ֣רֶא | laqach לָקַח וַ/תִּקַּ֥ח | Eve saw the tree, desired (ta'avah/nechmad), and took — the archetypal see→desire→take |
| 2 | Genesis 6:2 | A — Transgressive | ra'ah רָאָה וַ/יִּרְא֤וּ | laqach לָקַח וַ/יִּקְח֤וּ | The sons of God saw the daughters of men were fair and took wives — echo of 3:6 |
| 3 | Genesis 9:23 | C — Righteous inversion | ra'ah רָאָה רָאֽוּ | laqach לָקַח וַ/יִּקַּח֩ | Shem and Japheth took a garment to cover Noah, refusing to see his nakedness (inversion) |
| 4 | Genesis 12:15 | A — Transgressive | ra'ah רָאָה וַ/יִּרְא֤וּ | laqach לָקַח וַ/תֻּקַּ֥ח | Pharaoh's princes saw Sarai's beauty; the woman was taken into his house |
| 5 | Genesis 13:10 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂא | Lot lifted his eyes and saw the plain of the Jordan (nasa-enayim idiom) |
| 6 | Genesis 13:14 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא שָׂ֣א | 'Lift your eyes and see' — God to Abram (nasa-enayim idiom) |
| 7 | Genesis 18:2 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֔רְא; ra'ah רָאָה וַ/יַּ֗רְא | nasa נָשָׂא וַ/יִּשָּׂ֤א | Abraham lifted his eyes and saw the three visitors (nasa-enayim idiom) |
| 8 | Genesis 21:16 | I — Idiom / non-take | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא וַ/תִּשָּׂ֥א | Hagar lifted her voice and wept, not wishing to see the child die (nasa-qol, non-take) |
| 9 | Genesis 22:4 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א | Abraham lifted his eyes and saw the place afar off (nasa-enayim idiom) |
| 10 | Genesis 22:13 | C — Righteous inversion | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֨א; achaz אָחַז נֶאֱחַ֥ז; laqach לָקַח וַ/יִּקַּ֣ח | Abraham saw the ram caught (achaz) and took (laqach) it as a substitute — redemptive |
| 11 | Genesis 24:63 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֔רְא | nasa נָשָׂא וַ/יִּשָּׂ֤א | Isaac lifted his eyes and saw the camels coming (nasa-enayim idiom) |
| 12 | Genesis 24:64 | I — Idiom / non-take | ra'ah רָאָה וַ/תֵּ֖רֶא | nasa נָשָׂא וַ/תִּשָּׂ֤א | Rebekah lifted her eyes and saw Isaac (nasa-enayim idiom) |
| 13 | Genesis 28:6 | B — Narrative | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח לָ/קַֽחַת; laqach לָקַח תִקַּ֥ח | Esau saw that Isaac blessed Jacob and charged him to take a wife (marriage narrative) |
| 14 | Genesis 30:9 | B — Narrative | ra'ah רָאָה וַ/תֵּ֣רֶא | laqach לָקַח וַ/תִּקַּח֙ | Leah saw she had stopped bearing and took Zilpah to give to Jacob |
| 15 | Genesis 31:10 | I — Idiom / non-take | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא וָ/אֶשָּׂ֥א | Jacob in a dream lifted his eyes and saw the flock (nasa-enayim idiom) |
| 16 | Genesis 31:12 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאֵה֙; ra'ah רָאָה רָאִ֔יתִי | nasa נָשָׂא שָׂא | 'Lift your eyes and see' — the angel to Jacob (nasa-enayim idiom) |
| 17 | Genesis 31:50 | B — Narrative | ra'ah רָאָה רְאֵ֕ה | laqach לָקַח תִּקַּ֤ח | Laban: God will see between us if you take other wives (covenant witness) |
| 18 | Genesis 32:21 | I — Idiom / non-take | ra'ah רָאָה אֶרְאֶ֣ה | nasa נָשָׂא יִשָּׂ֥א | Jacob hopes Esau will 'lift his face' (accept him) when he sees him (nasa-panim, non-take) |
| 19 | Genesis 33:1 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֨א | Jacob lifted his eyes and saw Esau approaching (nasa-enayim idiom) |
| 20 | Genesis 33:5 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא וַ/יִּשָּׂ֣א | Esau lifted his eyes and saw the women and children (nasa-enayim idiom) |
| 21 | Genesis 33:10 | B — Narrative | ra'ah רָאָה רָאִ֣יתִי; ra'ah רָאָה כִּ/רְאֹ֛ת | laqach לָקַח וְ/לָקַחְתָּ֥ | Jacob: if I have found favor, take my present — 'I have seen your face' (reconciliation gift) |
| 22 | Genesis 34:2 | A — Transgressive | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח וַ/יִּקַּ֥ח | Shechem saw Dinah, took her, and violated her — see→take as sexual violence |
| 23 | Genesis 37:25 | I — Idiom / non-take | ra'ah רָאָה וַ/יִּרְא֔וּ | nasa נָשָׂא וַ/יִּשְׂא֤וּ; nasa נָשָׂא נֹֽשְׂאִ֗ים | Joseph's brothers lifted their eyes and saw the caravan (nasa-enayim idiom) |
| 24 | Genesis 38:2 | A — Transgressive | ra'ah רָאָה וַ/יַּרְא | laqach לָקַח וַ/יִּקָּחֶ֖/הָ | Judah saw the daughter of Shua and took her (Kline links this to David/Bathsheba) |
| 25 | Genesis 43:29 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֞רְא | nasa נָשָׂא וַ/יִּשָּׂ֣א | Joseph lifted his eyes and saw Benjamin (nasa-enayim idiom) |
| 26 | Genesis 45:27 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא לָ/שֵׂ֣את | Jacob saw the wagons sent to carry (nasa) him and revived (non-take) |
| 27 | Exodus 2:5 | C — Righteous inversion | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּקָּחֶֽ/הָ | Pharaoh's daughter saw the ark and took it — the taking preserves Moses' life |
| 28 | Exodus 19:4 | I — Idiom / non-take | ra'ah רָאָה רְאִיתֶ֔ם | nasa נָשָׂא וָ/אֶשָּׂ֤א | 'You have seen... how I bore (nasa) you on eagles' wings' (non-take) |
| 29 | Leviticus 5:1 | D — Juridical/cultic | ra'ah רָאָה רָאָ֖ה | nasa נָשָׂא וְ/נָשָׂ֥א | If a witness saw and does not testify, he bears (nasa) his iniquity (law) |
| 30 | Leviticus 20:17 | D — Juridical/cultic | ra'ah רָאָה וְ/רָאָ֨ה; ra'ah רָאָה תִרְאֶ֤ה | laqach לָקַח יִקַּ֣ח; nasa נָשָׂא יִשָּֽׂא | If a man takes his sister and sees her nakedness, he bears (nasa) iniquity (incest law) |
| 31 | Numbers 17:24 | B — Narrative | ra'ah רָאָה וַ/יִּרְא֥וּ | laqach לָקַח וַ/יִּקְח֖וּ | The chiefs saw and each took his rod (Aaron's budding staff, procedural) |
| 32 | Numbers 22:41 | B — Narrative | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֤ח | Balak took Balaam up to a height to see the people of Israel |
| 33 | Numbers 23:28 | B — Narrative | shaqaph שָׁקַף הַ/נִּשְׁקָ֖ף | laqach לָקַח וַ/יִּקַּ֥ח | Balak took Balaam to Peor, overlooking (nishqaf) the wasteland |
| 34 | Numbers 24:2 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֨א | Balaam lifted his eyes and saw Israel encamped (nasa-enayim idiom) |
| 35 | Numbers 24:20 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | Balaam saw Amalek and took up (nasa) his oracle (nasa-mashal, non-take) |
| 36 | Numbers 24:21 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | Balaam saw the Kenite and took up (nasa) his oracle (nasa-mashal, non-take) |
| 37 | Numbers 25:7 | C — Righteous inversion | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּ֥ח | Phinehas saw the sin and took a spear to stay the plague — righteous zeal |
| 38 | Deuteronomy 1:31 | I — Idiom / non-take | ra'ah רָאָה רָאִ֔יתָ | nasa נָשָׂא נְשָׂאֲ/ךָ֙; nasa נָשָׂא יִשָּׂא | 'You saw how the LORD bore (nasa) you as a man carries his son' (non-take) |
| 39 | Deuteronomy 3:27 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאֵ֣ה | nasa נָשָׂא וְ/שָׂ֥א | 'Lift your eyes and see' — Moses on Pisgah (nasa-enayim idiom) |
| 40 | Deuteronomy 4:19 | I — Idiom / non-take | ra'ah רָאָה וְֽ֠/רָאִיתָ | nasa נָשָׂא תִּשָּׂ֨א | Lest you lift your eyes and see the host of heaven and worship it (nasa-enayim) |
| 41 | Deuteronomy 21:11 | D — Juridical/cultic | ra'ah רָאָה וְ/רָאִיתָ֙ | laqach לָקַח וְ/לָקַחְתָּ֥ | If you see a beautiful captive and desire (chashaq) her, you may take her — the pattern in law |
| 42 | Joshua 3:3 | I — Idiom / non-take | ra'ah רָאָה כִּ/רְאֽוֹתְ/כֶ֗ם | nasa נָשָׂא נֹשְׂאִ֖ים | When you see the ark, which the priests bear (nasa), you shall follow (non-take) |
| 43 | Joshua 5:13 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֔רְא | nasa נָשָׂא וַ/יִּשָּׂ֤א | Joshua lifted his eyes and saw the captain of the LORD's host (nasa-enayim idiom) |
| 44 | Joshua 7:21 | A — Transgressive | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | laqach לָקַח וָֽ/אֶקָּחֵ֑/ם | Achan: 'I saw... I coveted (chamad)... and took' — the explicit see→covet→take triad |
| 45 | Joshua 8:1 | B — Narrative | ra'ah רָאָה רְאֵ֣ה | laqach לָקַח קַ֣ח | 'See, I have given Ai into your hand; take all the people of war' (battle command) |
| 46 | Joshua 8:8 | B — Narrative | ra'ah רָאָה רְא֖וּ | taphas תָּפַשׂ כְּ/תָפְשְׂ/כֶ֣ם | 'When you have seized (taphas) the city... see, I have commanded you' (ambush) |
| 47 | Joshua 8:21 | B — Narrative | ra'ah רָאָה רָא֗וּ | lakad לָכַד לָכַ֤ד | Joshua saw that the ambush had captured (lakad) the city and turned to fight |
| 48 | Judges 9:43 | B — Narrative | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּ֣ח | Abimelech saw the people come out and took his men in ambush (battle) |
| 49 | Judges 9:48 | B — Narrative | ra'ah רָאָה רְאִיתֶם֙ | laqach לָקַח וַ/יִּקַּח֩; nasa נָשָׂא וַ/יִּ֨שָּׂאֶ֔/הָ | Abimelech took an axe and cut a branch; 'what you have seen me do, do quickly' |
| 50 | Judges 13:19 | B — Narrative | ra'ah רָאָה רֹאִֽים | laqach לָקַח וַ/יִּקַּ֨ח | Manoah took the kid for offering while he and his wife looked on (theophany) |
| 51 | Judges 13:23 | B — Narrative | ra'ah רָאָה הֶרְאָ֖/נוּ | laqach לָקַח לָקַ֤ח | 'The LORD would not have shown us all this, nor taken a burnt offering from us' |
| 52 | Judges 14:2 | A — Transgressive | ra'ah רָאָה רָאִ֥יתִי | laqach לָקַח קְחוּ | Samson saw a woman at Timnah: 'take her for me' — see→take driven by the eyes |
| 53 | Judges 14:8 | B — Narrative | ra'ah רָאָה לִ/רְא֔וֹת | laqach לָקַח לְ/קַחְתָּ֔/הּ | Samson returned to take the woman and turned aside to see the lion's carcass |
| 54 | Judges 14:11 | B — Narrative | ra'ah רָאָה כִּ/רְאוֹתָ֣/ם | laqach לָקַח וַ/יִּקְחוּ֙ | When they saw Samson they took thirty companions to be with him |
| 55 | Judges 19:17 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֛רְא | nasa נָשָׂא וַ/יִּשָּׂ֣א | The old man lifted his eyes and saw the wayfarer in the square (nasa-enayim idiom) |
| 56 | Ruth 2:18 | I — Idiom / non-take | ra'ah רָאָה וַ/תֵּ֥רֶא | nasa נָשָׂא וַ/תִּשָּׂא֙ | Ruth took up (nasa) her gleanings and carried them home; her mother-in-law saw (non-take) |
| 57 | 1 Samuel 6:13 | I — Idiom / non-take | ra'ah רָאָה וַ/יִּרְאוּ֙; ra'ah רָאָה לִ/רְאֽוֹת | nasa נָשָׂא וַ/יִּשְׂא֣וּ | The reapers lifted their eyes and saw the returning ark (nasa-enayim idiom) |
| 58 | 1 Samuel 14:17 | I — Idiom / non-take | ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא וְ/נֹשֵׂ֥א | 'See who has gone from us'; Jonathan and his armor-bearer (nose keli, non-take) |
| 59 | 1 Samuel 17:51 | B — Narrative | ra'ah רָאָה וַ/יִּרְא֧וּ | laqach לָקַח וַ/יִּקַּ֣ח | David... took Goliath's sword; the Philistines saw their champion was dead (battle) |
| 60 | 1 Samuel 19:20 | B — Narrative | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח לָ/קַ֣חַת | Saul's messengers saw the band of prophets; they were sent to take David |
| 61 | 1 Samuel 24:12 | B — Narrative | ra'ah רָאָה רְאֵ֔ה; ra'ah רָאָה רְאֵ֛ה; ra'ah רָאָה וּ/רְאֵה֙ | laqach לָקַח לְ/קַחְתָּֽ/הּ | David: 'See the skirt of your robe in my hand... I took it and did not kill you' |
| 62 | 1 Samuel 25:35 | B — Narrative | ra'ah רָאָה רְאִי֙ | laqach לָקַח וַ/יִּקַּ֤ח; nasa נָשָׂא וָ/אֶשָּׂ֖א | David took from Abigail's hand what she brought: 'see, I have heeded your voice' |
| 63 | 1 Samuel 26:12 | B — Narrative | ra'ah רָאָה רֹאֶה֩ | laqach לָקַח וַ/יִּקַּח֩ | David took Saul's spear and jug while all slept; no one saw (sparing Saul) |
| 64 | 1 Samuel 31:5 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא נֹשֵֽׂא | Saul's armor-bearer (nose keli) saw that Saul was dead and fell on his sword (non-take) |
| 65 | 2 Samuel 13:34 | I — Idiom / non-take | tsaphah צָפָה הַ/צֹּפֶה֙; ra'ah רָאָה וַ/יַּ֗רְא | nasa נָשָׂא וַ/יִּשָּׂ֞א | The watchman lifted his eyes and saw a crowd coming (nasa-enayim idiom) |
| 66 | 2 Samuel 18:24 | I — Idiom / non-take | tsaphah צָפָה הַ/צֹּפֶ֜ה; ra'ah רָאָה וַ/יַּ֔רְא | nasa נָשָׂא וַ/יִּשָּׂ֤א | The watchman lifted his eyes and saw a man running (nasa-enayim idiom) |
| 67 | 2 Samuel 24:22 | B — Narrative | ra'ah רָאָה רְאֵה֙ | laqach לָקַח יִקַּ֥ח | Araunah: 'let my lord take what is good; see, here are the oxen' (threshing floor) |
| 68 | 1 Kings 16:18 | B — Narrative | ra'ah רָאָה כִּ/רְא֤וֹת | lakad לָכַד נִלְכְּדָ֣ה | Zimri saw the city was taken (nilkedah) and burned the palace over himself |
| 69 | 1 Kings 17:23 | C — Righteous inversion | ra'ah רָאָה רְאִ֖י | laqach לָקַח וַ/יִּקַּ֨ח | Elijah took the revived child down: 'See, your son lives' (rescue) |
| 70 | 2 Kings 2:10 | B — Narrative | ra'ah רָאָה תִּרְאֶ֨ה | laqach לָקַח לֻקָּ֤ח | Elijah: 'if you see me taken (luqach) from you, it shall be so' (ascension) |
| 71 | 2 Kings 3:14 | I — Idiom / non-take | nabat נָבַט אַבִּ֥יט; ra'ah רָאָה אֶרְאֶֽ/ךָּ | nasa נָשָׂא נֹשֵׂ֑א | Elisha: were it not that I regard (nasa-panim) Jehoshaphat, I would not look at you (non-take) |
| 72 | 2 Kings 3:26 | B — Narrative | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּ֣ח | The king of Moab saw the battle was too hard and took 700 swordsmen (siege) |
| 73 | 2 Kings 6:13 | B — Narrative | ra'ah רָאָה וּ/רְאוּ֙ | laqach לָקַח וְ/אֶקָּחֵ֑/הוּ | 'Go and see where he is, that I may send and take him' (hunt for Elisha) |
| 74 | 2 Kings 7:13 | B — Narrative | ra'ah רָאָה וְ/נִרְאֶֽה | laqach לָקַח וְ/יִקְחוּ | 'Let men take five horses and see' — reconnaissance in besieged Samaria |
| 75 | 2 Kings 7:14 | B — Narrative | ra'ah רָאָה וּ/רְאֽוּ | laqach לָקַח וַ/יִּקְח֕וּ | They took two chariots and horses and went to see (after the Arameans fled) |
| 76 | 2 Kings 9:17 | B — Narrative | tsaphah צָפָה וְ/הַ/צֹּפֶה֩; ra'ah רָאָה וַ/יַּ֞רְא; ra'ah רָאָה רֹאֶ֑ה | laqach לָקַח קַ֥ח | The watchman saw Jehu's company: 'take a horseman and send to meet them' |
| 77 | 2 Kings 9:26 | B — Narrative | ra'ah רָאָה רָאִ֤יתִי | nasa נָשָׂא שָׂ֧א | 'I saw the blood of Naboth... take him up and cast him on the plot' (Jehu's vengeance) |
| 78 | 2 Kings 9:32 | I — Idiom / non-take | shaqaph שָׁקַף וַ/יַּשְׁקִ֣יפוּ | nasa נָשָׂא וַ/יִּשָּׂ֤א | Jehu lifted his face; the eunuchs looked out (shaqaph) at the window (nasa-panim, non-take) |
| 79 | 2 Kings 11:4 | B — Narrative | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֣ח | Jehoiada took the captains and showed them the king's son (coup for Joash) |
| 80 | 2 Kings 23:16 | B — Narrative | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח וַ/יִּקַּ֤ח | Josiah turned, saw the tombs, and took the bones to defile the altar (reform) |
| 81 | 2 Kings 25:19 | B — Narrative | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח לָקַח֩ | Nebuzaradan took an officer and men who saw the king's face (deportation) |
| 82 | 1 Chronicles 10:5 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא נֹשֵֽׂא | Saul's armor-bearer (nose keli) saw he was dead and died with him (non-take) |
| 83 | 1 Chronicles 21:16 | I — Idiom / non-take | ra'ah רָאָה וַ/יַּ֞רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א | David lifted his eyes and saw the angel of the LORD (nasa-enayim idiom) |
| 84 | 1 Chronicles 21:23 | B — Narrative | ra'ah רָאָה רְאֵה֩ | laqach לָקַח קַֽח | Ornan: 'take it... see, I give the oxen for burnt offerings' (David's altar) |
| 85 | 2 Chronicles 24:11 | I — Idiom / non-take | ra'ah רָאָה וְ/כִ/רְאוֹתָ֞/ם | nasa נָשָׂא וְ/יִשָּׂאֻ֖/הוּ | When they saw the chest held much money they carried (nasa) it out (non-take) |
| 86 | Esther 2:9 | B — Narrative | ra'ah רָאָה הָ/רְאֻי֥וֹת | nasa נָשָׂא וַ/תִּשָּׂ֣א | Hegai saw Esther pleased him and advanced her in the harem |
| 87 | Esther 2:15 | B — Narrative | ra'ah רָאָה רֹאֶֽי/הָ | laqach לָקַח לָקַֽח; nasa נָשָׂא נֹשֵׂ֣את | Esther required only what Hegai appointed; she won favor with all who saw her |
| 88 | Esther 5:2 | I — Idiom / non-take | ra'ah רָאָה כִ/רְא֨וֹת | nasa נָשָׂא נָשְׂאָ֥ה | The king saw Esther and she won favor (nasa-chen) in his sight (non-take) |
| 89 | Psalms 4:7 | I — Idiom / non-take | ra'ah רָאָה יַרְאֵ֪/נ֫וּ | nasa נָשָׂא נְֽסָ/ה | 'Who will show us good? Lift (nasa) the light of your face upon us' (non-take) |
| 90 | Psalms 25:18 | I — Idiom / non-take | ra'ah רָאָה רְאֵ֣ה | nasa נָשָׂא וְ֝/שָׂ֗א | 'See my affliction... and forgive (nasa) all my sins' (non-take) |
| 91 | Proverbs 24:32 | B — Narrative | chazah חָזָה וָֽ/אֶחֱזֶ֣ה; ra'ah רָאָה רָ֝אִ֗יתִי | laqach לָקַח לָקַ֥חְתִּי | 'I saw and took it to heart; I looked and received instruction' (wisdom reflection) |
| 92 | Ecclesiastes 2:3 | B — Narrative | ra'ah רָאָה אֶרְאֶ֗ה | achaz אָחַז וְ/לֶ/אֱחֹ֣ז | Qoheleth sought to see good while laying hold (achaz) of folly (experiment) |
| 93 | Isaiah 6:1 | I — Idiom / non-take | ra'ah רָאָה וָ/אֶרְאֶ֧ה | nasa נָשָׂא וְ/נִשָּׂ֑א | 'I saw the Lord... high and lifted up (nissa)' (non-take) |
| 94 | Isaiah 18:3 | I — Idiom / non-take | ra'ah רָאָה תִּרְא֔וּ | nasa נָשָׂא כִּ/נְשֹׂא | 'When a signal is lifted (nasa) on the mountains, you shall see it' (non-take) |
| 95 | Isaiah 21:3 | B — Narrative | ra'ah רָאָה מֵ/רְאֽוֹת | achaz אָחַז אֲחָז֔וּ/נִי | Pangs seized (achaz) the prophet at what he was made to see (metaphorical seizure) |
| 96 | Isaiah 40:26 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאוּ֙ | nasa נָשָׂא שְׂאוּ | 'Lift your eyes on high and see who created these' (nasa-enayim idiom) |
| 97 | Isaiah 47:3 | B — Narrative | ra'ah רָאָה תֵּרָאֶ֖ה | laqach לָקַח אֶקָּ֔ח | 'Your nakedness shall be seen... I will take vengeance' (laqach-naqam, judgment on Babylon) |
| 98 | Isaiah 49:18 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאִ֔י | nasa נָשָׂא שְׂאִֽי | 'Lift your eyes and see; they all gather' (nasa-enayim idiom) |
| 99 | Isaiah 51:6 | I — Idiom / non-take | nabat נָבַט וְֽ/הַבִּ֧יטוּ | nasa נָשָׂא שְׂאוּ֩ | 'Lift your eyes to the heavens and look' (nasa-enayim idiom) |
| 100 | Isaiah 52:8 | I — Idiom / non-take | tsaphah צָפָה צֹפַ֛יִ/ךְ; ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא נָ֥שְׂאוּ | The watchmen lift their voice (nasa-qol) and see eye to eye (non-take) |
| 101 | Isaiah 60:4 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאִ֔י | nasa נָשָׂא שְׂאִֽי | 'Lift your eyes and see; they all gather to you' (nasa-enayim idiom) |
| 102 | Jeremiah 3:2 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאִ֗י | nasa נָשָׂא שְׂאִֽי | 'Lift your eyes to the bare heights and see' (nasa-enayim idiom) |
| 103 | Jeremiah 5:26 | A — Transgressive | shur שׁוּר יָשׁוּר֙ | lakad לָכַד יִלְכֹּֽדוּ | The wicked watch (shur) like fowlers and catch (lakad) men — predatory seizure |
| 104 | Jeremiah 6:1 | I — Idiom / non-take | shaqaph שָׁקַף נִשְׁקְפָ֥ה | nasa נָשָׂא שְׂא֣וּ | 'Raise (nasa) a signal... for disaster looms (nishqefah)' (non-take) |
| 105 | Jeremiah 13:20 | I — Idiom / non-take | ra'ah רָאָה ו/ראי; ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא שאי; nasa נָשָׂא שְׂא֤וּ | 'Lift your eyes and see those coming from the north' (nasa-enayim idiom) |
| 106 | Jeremiah 32:24 | B — Narrative | ra'ah רָאָה רֹאֶֽה | lakad לָכַד לְ/לָכְדָ/הּ֒ | The city is given over and taken (lakad) by the besiegers, as you see (siege) |
| 107 | Jeremiah 34:3 | B — Narrative | ra'ah רָאָה תִּרְאֶ֗ינָה | taphas תָּפַשׂ תָּפֹ֣שׂ; taphas תָּפַשׂ תִּתָּפֵ֔שׂ | Zedekiah: you shall be caught (taphas) and taken; your eyes shall see the king's eyes |
| 108 | Jeremiah 52:25 | B — Narrative | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח לָקַח֩ | Nebuzaradan took an officer and men who saw the king's face (deportation) |
| 109 | Lamentations 4:16 | I — Idiom / non-take | nabat נָבַט לְ/הַבִּיטָ֑/ם | nasa נָשָׂא נָשָׂ֔אוּ | The LORD no longer regards them (nasa-panim); priests were shown no favor (non-take) |
| 110 | Ezekiel 1:4 | B — Narrative | ra'ah רָאָה וָ/אֵ֡רֶא | laqach לָקַח מִתְלַקַּ֔חַת | 'I looked, and behold... fire enfolding (mitlaqqachat) itself' (inaugural vision) |
| 111 | Ezekiel 11:1 | I — Idiom / non-take | ra'ah רָאָה וָ/אֶרְאֶ֨ה | nasa נָשָׂא וַ/תִּשָּׂ֨א | 'The Spirit lifted (nasa) me and I saw' (non-take, prophetic rapture) |
| 112 | Ezekiel 11:24 | I — Idiom / non-take | ra'ah רָאָה רָאִֽיתִי | nasa נָשָׂא נְשָׂאַ֗תְ/נִי | 'The Spirit lifted me... in the vision I had seen' (non-take, prophetic rapture) |
| 113 | Ezekiel 12:6 | I — Idiom / non-take | ra'ah רָאָה תִרְאֶ֖ה | nasa נָשָׂא תִּשָּׂא֙ | 'Lift (nasa) your baggage on your shoulder... you shall not see the ground' (non-take) |
| 114 | Ezekiel 12:12 | I — Idiom / non-take | ra'ah רָאָה יִרְאֶ֥ה | nasa נָשָׂא יִשָּׂא֙ | 'The prince shall lift (nasa) his baggage on his shoulder... he shall not see' (non-take) |
| 115 | Ezekiel 12:13 | B — Narrative | ra'ah רָאָה יִרְאֶ֖ה | taphas תָּפַשׂ וְ/נִתְפַּ֖שׂ | 'He shall be caught (taphas) in my snare... yet he shall not see the land' (judgment) |
| 116 | Ezekiel 19:5 | B — Narrative | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח וַ/תִּקַּ֛ח | 'When the lioness saw... she took another of her cubs and made him a lion' (allegory) |
| 117 | Ezekiel 20:28 | B — Narrative | ra'ah רָאָה וַ/יִּרְאוּ֩ | nasa נָשָׂא נָשָׂ֨אתִי֙ | They saw every high hill and there presented their offerings (idolatry indictment) |
| 118 | Ezekiel 21:29 | B — Narrative | ra'ah רָאָה לְ/הֵֽרָאוֹת֙ | taphas תָּפַשׂ תִּתָּפֵֽשׂוּ | 'While they see false visions for you... you shall be seized (taphas)' (judgment) |
| 119 | Ezekiel 33:2 | D — Juridical/cultic | tsaphah צָפָה לְ/צֹפֶֽה | laqach לָקַח וְ/לָקְח֨וּ | The people take a man and set him as watchman (tsofeh) when they see the sword (law) |
| 120 | Ezekiel 33:6 | D — Juridical/cultic | tsaphah צָפָה וְ֠/הַ/צֹּפֶה; ra'ah רָאָה יִרְאֶ֨ה; tsaphah צָפָה הַ/צֹּפֶ֥ה | laqach לָקַח וַ/תִּקַּ֥ח; laqach לָקַח נִלְקָ֔ח | If the watchman sees the sword but does not warn, the sword takes (laqach) a life (responsibility) |
| 121 | Daniel 8:3 | I — Idiom / non-take | ra'ah רָאָה וָ/אֶרְאֶ֔ה | nasa נָשָׂא וָ/אֶשָּׂ֤א | 'I lifted my eyes and saw a ram' (nasa-enayim, apocalyptic vision) |
| 122 | Daniel 10:5 | I — Idiom / non-take | ra'ah רָאָה וָ/אֵ֔רֶא | nasa נָשָׂא וָ/אֶשָּׂ֤א | 'I lifted my eyes and looked, and behold a man' (nasa-enayim, vision) |
| 123 | Micah 7:9 | I — Idiom / non-take | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא אֶשָּׂ֔א | 'I will bear (nasa) the LORD's indignation... until I behold his vindication' (non-take) |
| 124 | Habakkuk 1:3 | I — Idiom / non-take | ra'ah רָאָה תַרְאֵ֤/נִי; nabat נָבַט תַּבִּ֔יט | nasa נָשָׂא יִשָּֽׂא | 'Why do you make me see wrong... strife lifts up (nasa)?' (non-take) |
| 125 | Habakkuk 3:10 | I — Idiom / non-take | ra'ah רָאָה רָא֤וּ/ךָ | nasa נָשָׂא נָשָֽׂא | 'The mountains saw you... the deep lifted (nasa) its voice' (non-take theophany) |
| 126 | Zechariah 2:1 | I — Idiom / non-take | ra'ah רָאָה וָ/אֵ֑רֶא | nasa נָשָׂא וָ/אֶשָּׂ֥א | 'I lifted my eyes and saw, and behold four horns' (nasa-enayim, vision) |
| 127 | Zechariah 2:5 | I — Idiom / non-take | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא וָ/אֶשָּׂ֥א | 'I lifted my eyes and saw a man with a measuring line' (nasa-enayim, vision) |
| 128 | Zechariah 5:1 | I — Idiom / non-take | ra'ah רָאָה וָֽ/אֶרְאֶ֑ה | nasa נָשָׂא וָ/אֶשָּׂ֥א | 'I lifted my eyes and saw a flying scroll' (nasa-enayim, vision) |
| 129 | Zechariah 5:5 | I — Idiom / non-take | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא שָׂ֣א | 'Lift your eyes and see what this is that goes forth' (nasa-enayim, vision) |
| 130 | Zechariah 5:9 | I — Idiom / non-take | ra'ah רָאָה וָ/אֵ֗רֶא | nasa נָשָׂא וָ/אֶשָּׂ֨א; nasa נָשָׂא וַ/תִּשֶּׂ֨אנָה֙ | 'I lifted my eyes and saw two women with wind in their wings' (nasa-enayim, vision) |
| 131 | Zechariah 6:1 | I — Idiom / non-take | ra'ah רָאָה וָֽ/אֶרְאֶ֔ה | nasa נָשָׂא וָ/אֶשָּׂ֤א | 'I lifted my eyes and saw four chariots' (nasa-enayim, vision) |


---

## 5. The significant passages

### Genesis 3:6 — Eve and the tree (the archetype)

The Masoretic text (Sefaria, *Miqra according to the Masorah*) reads:

> וַתֵּ֣רֶא הָֽאִשָּׁ֡ה כִּ֣י טוֹב֩ הָעֵ֨ץ לְמַאֲכָ֜ל וְכִ֧י תַֽאֲוָה־ה֣וּא לָעֵינַ֗יִם וְנֶחְמָ֤ד הָעֵץ֙ לְהַשְׂכִּ֔יל וַתִּקַּ֥ח מִפִּרְי֖וֹ וַתֹּאכַ֑ל וַתִּתֵּ֧ן גַּם־לְאִישָׁ֛הּ עִמָּ֖הּ וַיֹּאכַֽל׃

Revised JPS (2023): "When the woman saw that the tree was good for eating and a delight to the eyes, and that the tree was desirable as a source of wisdom, she took of its fruit and ate. She also gave some to her husband, and he ate."

This single verse holds the whole motif in compressed form. The narrative is carried by a chain of *wayyiqtol* verbs, of which the two poles are perception and seizure: *wattēreʾ* ("and she saw," qal of **ra'ah**, H7200) and *wattiqqaḥ* ("and she took," qal of **laqach**, H3947), resolving into *wattōʾkal* ("and she ate"). Between seeing and taking the verse inserts a doubled note of desire — the exact psychological hinge the later episodes will reuse. The tree is *taʾăwāh la-ʿênayim*, "a delight/craving **to the eyes**" (**ta'avah**, H8378, a nominal of appetite), and *neḥmād*, "desirable" (niphal participle of **chamad**, H2530). *Chamad* is the operative verb of the Tenth Commandment's prohibition of coveting (Exod 20:17; Deut 5:21), a link foregrounded by TheTorah.com's treatment of whether *chamad* names a feeling or an act [confirmed]; here it names the desire that issues directly in the act of taking.

Three grounds are enumerated in strict parallel — good for food, a delight to the eyes, desirable for wisdom — a tripartite appraisal widely mapped onto 1 John 2:16's "desire of the flesh, desire of the eyes, and pride of life" [confirmed], the reading Augustine systematizes as *concupiscentia carnis / oculorum / ambitio saeculi* (*Confessions* X.35) [confirmed]. James 1:14–15 supplies the same syntax of consequence — desire conceives, births sin, and ends in death [confirmed]. Ibn Ezra already ties the tree to desire at 3:6 [confirmed, in dossier via Sefaria].

That 3:6 functions as the *archetype* of a see→desire→take sequence is best supported indirectly: Wenham (*Genesis 1–15*, WBC, 1987) reads Genesis 6:2's "saw…good/fair…took" as a deliberate echo of *this* verse [confirmed, in dossier], which presupposes 3:6 as the template. (Cassuto, by contrast, reads 6:2 as ordinary lawful marriage and rejects the illicit-desire echo — the disagreement is discussed in the survey below.) The device itself — a repeated key-word binding episodes into thematic argument — is Buber and Rosenzweig's *Leitwort* / *milah manḥah* [confirmed], elaborated by Alter [confirmed] and grounded methodologically in Fishbane's principle that shared distinctive vocabulary signals intentional allusion [confirmed].

*Caveats.* The verse names *ra'ah*, *ta'avah/chamad*, and *laqach*, but its status as the fountainhead of a cross-corpus "sin pattern" is a modern synthesis, not a claim any ancient source makes; it is assembled from Fishbane's method plus Wenham's 3→6 echo, and should be labelled as such. Note too that "delight to the eyes" renders a noun (*taʾăwāh*), not a verb, and that *neḥmād* is passive-stative ("desirable"), so the "coveting" is predicated of the object's appeal as much as of Eve's volition — the grammar leaves the agency of desire productively ambiguous.

### Genesis 6:1-4 — the sons of God, and the Watchers of 1 Enoch

Genesis 6:1-4 compresses a whole drama into two narrative verbs. When humanity multiplies, "the sons of God" (*bnei ha-ʾelohim*) act:

> וַיִּרְאוּ֙ בְנֵי־הָ֣אֱלֹהִ֔ים אֶת־בְּנוֹת֖ הָאָדָ֑ם כִּ֥י טֹבֹ֖ת הֵ֥נָּה וַיִּקְח֛וּ לָהֶ֥ם נָשִׁ֖ים מִכֹּ֥ל אֲשֶׁר־בָּחָֽרוּ׃
>
> "the sons of God *saw* the daughters of men that they were *fair*; and they *took* them wives of all which they chose" (Gen 6:2, KJV).

The operative chain is *wayyirʾu* (*raʾah*, "see," H7200) → *ki tovot* ("that [they were] good/fair," from *tov*, H2896) → *wayyiqḥu* (*laqach*, "take," H3947), sealed by *baḥaru* (*bachar*, "choose," H977). Both verbs are qal *wayyiqtol* preterites: sight issues directly in seizure, with no intervening speech, permission, or negotiation.

This is the same syntagm as the first transgression. In Gen 3:6 the woman *saw* (*wa-tereʾ*, *raʾah*) that the tree was *good* (*tov*) and *desirable* (*neḥmad*, from *chamad*, H2530), and she *took* (*wa-tiqqaḥ*, *laqach*). Wenham (*Genesis 1-15*, WBC, 1987) reads 6:2 as a deliberate verbal echo of 3:6 — *saw…good/fair…took* — recasting the antediluvian sin in the grammar of Eden [confirmed]. (Cassuto pointedly dissents: in his comment on 6:2 he takes "took … wives" as the ordinary idiom for lawful marriage and glosses "good/fair" via Exod 2:2, not Gen 3, denying any note of illicit desire here [confirmed] — a reminder that the echo is an argued reading, not a datum.) Ramban (Nachmanides) on 6:2 presses the coercion latent in *laqach*: the "sons of God" are powerful men/rulers who *took* wives by force, even married women [confirmed, via dossier/Sefaria].

Second Temple interpreters seized precisely on this "saw…took." *1 Enoch* 6-8 (the Book of the Watchers) and *Jubilees* 5 expand v.2 into a myth of angelic rebellion: the Watchers under Shemihazah/Semjaza *see* and desire the women, descend on Mount Hermon, bind themselves by oath ("two hundred"), *take* wives, and beget the giants (the *nephilim*/*gibborim* of v.4), while Asael/Azazel teaches forbidden arts. Kugel (*How to Read the Bible*, 2007), Stuckenbruck (DSD 7.3, 2000), and Reed (*Fallen Angels*, 2005) trace how this reading made Gen 6 the very etiology of evil [confirmed]. The terse *raʾah*/*laqach* of the Hebrew becomes, in the Enochic edition this site presents, the primal cosmic crime.

**Caveats.** The identity of *bnei ha-ʾelohim* is contested (angelic, Sethite, or dynastic-royal); the angelic reading behind *1 Enoch* is the earliest *attested*, not demonstrably the "original" sense. The 3→6 echo is a literary observation (Wenham; explicitly contested by Cassuto), not proof of single authorship. Per the honesty rule, no monograph welds Gen 3:6, 6:2, Achan (Josh 7), and David (2 Sam 11) into one authored "sin pattern"; that larger synthesis is assembled here from Fishbane's allusion method plus these commentators, and is labeled as such.

### Genesis 9:20-23 — Ham sees, Shem and Japheth take (the first inversion)

After Noah plants a vineyard, drinks, and lies uncovered (*wayyitgal*, v.21), the scene turns on the two verbs that elsewhere drive transgression. Ham **saw**: וַיַּ֗רְא חָ֚ם אֲבִ֣י כְנַ֔עַן אֵ֖ת עֶרְוַ֣ת אָבִ֑יו — "Ham, the father of Canaan, *saw* his father's nakedness" (v.22; *wayyar'*, root *ra'ah*, H7200). The brothers **took**: וַיִּקַּח֩ שֵׁ֨ם וָיֶ֜פֶת אֶת־הַשִּׂמְלָ֗ה — "But Shem and Japheth *took* a cloth" (v.23; *wayyiqqach*, root *laqach*, H3947), laid it on both their shoulders, walked backward (*aḥorannit*), and covered (*wayekhassu*, root *kasah*, H3680) their father — the verse closing on the key-word now negated: וְעֶרְוַ֥ת אֲבִיהֶ֖ם לֹ֥א רָאֽוּ, "and their father's nakedness they did *not see*" (*lo ra'u*).

The pericope is bracketed by *ra'ah*: transgressive seeing opens it, refused seeing closes it. This is the Category-C inversion. In Gen 3:6 and 6:2 the chain *ra'ah → ṭov/ḥamad → laqach* runs downhill into sin; here *ra'ah* is itself the offense, and *laqach* — the very verb of the illicit "taking" of the tree and of the women — becomes the instrument of repair. The righteous act is a refusal to complete the pattern: they *take* precisely in order not to *see*.

The object, *ervah* ("nakedness," H6172), reaches back to Eden, where the eyes opened by the forbidden eating first discovered nakedness (Gen 3:7); Shem and Japheth reverse that exposure by re-covering. Reading the shared *ra'ah / laqach* diction as deliberate echo rather than coincidence rests on Fishbane's criterion that distinctive shared vocabulary signals intentional allusion [confirmed] and on Alter's *Leitwort* device [confirmed]. Wenham frames the primeval narratives as the "logical development of sin" [confirmed] — the template Gen 9 momentarily reverses; Sarna reads the Noah-drunkenness scene within that same primeval arc [general-knowledge].

**Caveats.** (1) No dossier source explicitly labels Gen 9:20-23 a "redemptive inversion" of the see→take motif; that framing is my synthesis, assembled from Fishbane's method plus Wenham's reading of the 3→6 template. (2) *ervat aviv* ("nakedness of his father") is a sexual euphemism in Lev 18/20, which fed early readings (paternal castration, maternal incest; e.g. b. Sanhedrin 70a [general-knowledge]) that Ham did more than look. On those readings "seeing" is itself a euphemism, and the tidy verbal inversion is partly a surface effect of the narrator's discretion.

### Genesis 12:10-20 — Sarai seen in Egypt and taken

The Egyptian episode supplies the pattern's first royal-scale instance: a wife *seen* and *taken*. The frame is set before entry — Abram tells Sarai *hinneh na yada'ti ki ishah yefat mar'eh att*, "I know that thou art a fair woman to look upon" (12:11 KJV), where **mar'eh** ("appearance") is a nominal of *ra'ah*, so beauty is already defined as an object of sight. The verbs then arrive doubled and unmistakable.

**12:14** — וַיִּרְא֤וּ הַמִּצְרִים֙ אֶת־הָאִשָּׁ֔ה כִּֽי־יָפָ֥ה הִ֖וא מְאֹֽד — "the Egyptians beheld (*wayyir'u*, **ra'ah**, H7200) the woman that she was very fair (*yafah*)."
**12:15** — וַיִּרְא֤וּ אֹתָהּ֙ שָׂרֵ֣י פַרְעֹ֔ה … וַתֻּקַּ֥ח הָאִשָּׁ֖ה בֵּ֥ית פַּרְעֹֽה — "the princes of Pharaoh saw (*wayyir'u*) her … and the woman was taken (*wattuqqach*, **laqach**, H3947) into Pharaoh's house."

Seeing repeats (populace, then court) and issues directly in taking. Notably, *wattuqqach* is the **passive** of *laqach* (the anomalous Qal-passive/Hophal pattern): Sarai is grammatical patient, an object moved into the royal house, her agency erased. The root then resurfaces actively at the resolution — Pharaoh's *va'eqqach otah li le'ishah*, "I took her to me to wife," and the imperative *qach*, "take her, and go" (12:19) — so *laqach* brackets the whole scene.

Methodologically, Fishbane's criterion of distinctive shared vocabulary licenses reading this *ra'ah → laqach* sequence as continuous with Eve's "saw…took" (Gen 3:6) and the Watchers' "saw…fair…took" (Gen 6:2), the chain Wenham documents [confirmed]. Alter groups 12, 20, 26 as wife-sister **type-scene** variants [confirmed]; Sarna treats the "she is my sister" ruse similarly [confirmed]. Forward, the pairing anticipates the royal *saw/sent/took* of David and Bathsheba (2 Sam 11:2,4), the see-and-take that Sternberg and Kline analyze [confirmed] — though the ethical vector inverts: here the endangered husband, not the king, is culpable.

The comparison the guidance flags holds philologically. **Gen 20:2** has *laqach* (*wayyiqqach*, Abimelech "took Sarah") but no report of seeing her beauty — taking without the pointed *ra'ah*. **Gen 26** has the sight vocabulary — Rebekah is *tovat mar'eh* (26:7), and Abimelech *wayyar*, "looked… and saw" (26:8) — yet no taking; there seeing *exposes* the truth and averts seizure. Only Gen 12 fuses the two verbs tightly.

### Genesis 22:13 — Abraham sees the ram and takes it (redemptive substitution)

**Text (Sefaria, fetched this session).** MT (Miqra according to the Masorah): וַיִּשָּׂ֨א אַבְרָהָ֜ם אֶת־עֵינָ֗יו וַיַּרְא֙ וְהִנֵּה־אַ֔יִל אַחַ֕ר נֶאֱחַ֥ז בַּסְּבַ֖ךְ בְּקַרְנָ֑יו וַיֵּ֤לֶךְ אַבְרָהָם֙ וַיִּקַּ֣ח אֶת־הָאַ֔יִל וַיַּעֲלֵ֥הוּ לְעֹלָ֖ה תַּ֥חַת בְּנֽוֹ׃ — RJPS (2023): "When Abraham looked up, his eye fell upon a ram, caught in the thicket by its horns. So Abraham went and took the ram and offered it up as a burnt offering in place of his son."

The verse chains the study's two signature verbs in their fullest idiomatic form. Abraham "lifted his eyes and saw" — *wayyissaʼ … et-ʻenav* (*nasaʼ*, H5375) *wayyarʼ* (*raʼah*, H7200) — the formulaic perception-pair that launches episodes of appraisal and choice across Genesis (13:10; 18:2; 24:63), and that here frames an inclusio within the chapter itself: Abraham "lifts his eyes and sees" the place from afar (22:4) and now the ram. What the eye lights on is then "taken": *wayyiqqach* (*laqach*, H3947). Seeing issues in taking, exactly as in Gen 3:6 and 6:2.

But the sequence is morally inverted. Between the seeing and the taking stands the third verb the guidance flags: the ram is *neʼechaz* (Niphal of *achaz*, H270), "caught, held fast," in the thicket. *achaz* is a near-synonym of *laqach* within the semantic field of grasping/seizing; the animal is passively "seized" by the bramble precisely so that it may be actively "taken" by Abraham — the lexical texture doubles the taking motif while relocating its agency. And the taking terminates not in acquisition but in surrender: the ram is offered *le-ʻolah tachat beno*, "as a burnt offering **in place of** his son," *tachat* (H8478) being the preposition of substitution/exchange.

The see→take pattern is thus turned toward sacrifice. Where Eve saw the fruit was good and took (Gen 3:6) and the sons of God saw the daughters were fair and took (Gen 6:2), Abraham sees a divinely provided victim and takes it in order to give it up: the verbs are identical, the vector reversed — from grasping-for-self to offering-instead-of. Read against v. 8 ("God will *see/provide*," *yirʼeh*, same root *raʼah*) and the naming YHWH-*yirʼeh* (22:14), the "seeing" motif is redoubled and rehabilitated — sight bound to provision rather than covetous appraisal.

Methodologically this applies the Leitwort principle — Buber's *milah manḥah* and Alter's "thematic key-word" [confirmed] — and Fishbane's criterion that shared distinctive vocabulary signals intentional linkage [confirmed]. Sarna's *JPS Genesis* notes the formulaic "lifted his eyes" idiom and the substitutionary force of *tachat* [general-knowledge].

**Caveats.** (1) No dossier source argues that 22:13 belongs to a single authored "see→take" pattern alongside 3:6/6:2; the redemptive *inversion* proposed here is my synthesis, built on the Leitwort / inner-biblical-allusion method, and should be labelled as such. (2) *achaz* and *laqach* are distinct roots — their pairing is thematic, not etymological. (3) The consonantal crux *achar* ("behind," MT) vs. *echad* ("one ram," read by the Samaritan Pentateuch, LXX, and Syriac and adopted by RJPS) is text-critical and does not touch the *raʼah*/*laqach* verbs [confirmed from the fetched RJPS note].

### Genesis 34:1–2 — Shechem sees Dinah and takes her

> **34:1** וַתֵּצֵ֤א דִינָה֙ בַּת־לֵאָ֔ה אֲשֶׁ֥ר יָלְדָ֖ה לְיַעֲקֹ֑ב לִרְא֖וֹת בִּבְנ֥וֹת הָאָֽרֶץ׃
> "Now Dinah, the daughter whom Leah had borne to Jacob, went out to visit the daughters of the land."
> **34:2** וַיַּ֨רְא אֹתָ֜הּ שְׁכֶ֧ם בֶּן־חֲמ֛וֹר הַֽחִוִּ֖י נְשִׂ֣יא הָאָ֑רֶץ וַיִּקַּ֥ח אֹתָ֛הּ וַיִּשְׁכַּ֥ב אֹתָ֖הּ וַיְעַנֶּֽהָ׃
> "Shechem son of Hamor the Hivite, chief of the country, saw her, and took her and lay with her and disgraced her." (RJPS 2023, which footnotes *disgraced* as literally "violated"; MAM Hebrew — both fetched from Sefaria) [confirmed]

**The verb chain.** Verse 2 strings four consecutive *wayyiqtol* forms with no intervening dialogue or deliberation: *wayyar'* ("and he saw," *ra'ah*, H7200) — *wayyiqqach* ("and he took," *laqach*, H3947) — *wayyishkav* ("and he lay," *shakav*, H7901) — *wayĕ'anneha* ("and he violated her," piel of *'anah* II, H6031). The syntax itself performs the aggression: perception collapses immediately into seizure and assault, the subject (Shechem) governing every verb and Dinah reduced to the suffixed object *'otah* ("her") on each.

**A framing irony in v. 1.** Dinah "goes out" (*wattetse'*, *yatsa'*, H3318) *lir'ot* — the infinitive of the same root *ra'ah*, "to see" (RJPS softens it to "visit"). Her seeing is social and open; his seeing, in the next clause, is predatory. The narrator sets one *ra'ah* against another so that the identical verb marks the pivot from a daughter's outing to a man's appropriation.

**Two philological notes.** First, *wayyishkav 'otah* takes the direct-object marker '*et* rather than the usual *shakav 'im* ("lie *with*") or *shakav 'el*; the accusative construction is grammatically harsh and is widely read as connoting force and objectification rather than mutuality (Sternberg's reading of the Dinah episode, *Poetics*, develops exactly this brutality of grammar) [general-knowledge]. Second, *'innah* is the legal-narrative term for sexual degradation, recurring in Deuteronomy's rape laws (Deut 22:24, 29) and, tellingly, in Amnon's rape of Tamar (2 Sam 13:14), which likewise pairs *wayĕ'anneha* with *shakav*.

**Motif placement.** The bare *ra'ah* → *laqach* sequence is the recurrent grammar of illicit appropriation traced through Eve's *saw…took* (Gen 3:6), the Watchers/sons of God who *saw…took* (Gen 6:2), and David who *saw…sent…took* (2 Sam 11). Fishbane's criterion — shared distinctive vocabulary as the signal of intentional linkage — and the Buber–Rosenzweig *Leitwort* principle license reading these as one keyword pattern [confirmed]; Alter names *see/take* as a syntax of transgressive desire [confirmed], and Wenham documents the 3:6 → 6:2 echo directly [confirmed]. Gen 34 supplies the pattern's most explicitly violent instance, where "taking" is unambiguously rape.

**Caveats.** No source in the dossier argues that Gen 3:6 → 6:2 → 2 Sam 11 → Gen 34 constitute a single authored "sin sequence"; that synthesis is assembled here from Fishbane's method plus the individual echo-studies, and should be read as an interpretive construct rather than a claim any one monograph makes. The *shakav-'et*-as-violence reading, while common, rests on a rare construction and is an inference, not a lexical certainty. Wenham's commentary covers Gen 1–15, so its authority is invoked for the 3→6 backbone, not for Gen 34 itself.

### Genesis 38:2 — Judah sees Bath-shua and takes her

**Text (WLC / KJV).** וַיַּרְא־שָׁ֧ם יְהוּדָ֛ה בַּת־אִ֥ישׁ כְּנַעֲנִ֖י וּשְׁמ֣וֹ שׁ֑וּעַ וַיִּקָּחֶ֖הָ וַיָּבֹ֥א אֵלֶֽיהָ׃ — "And Judah *saw* there a daughter of a certain Canaanite, whose name was Shua[h]; and he *took* her, and went in unto her" (KJV; the MT vocalizes the name שׁוּעַ, *Shua*).

**Operative verbs.** The clause chains three *wayyiqtol* forms. (1) וַיַּרְא *wayyarʾ*, Qal imperfect-consecutive 3ms of רָאָה *raʾah* (H7200), "and he saw" — WLC morphology `Vqw3ms`. (2) וַיִּקָּחֶהָ *wayyiqqacheha*, Qal of לָקַח *laqach* (H3947) with 3fs suffix, "and he took her" (`Vqw3ms/Sp3fs`). (3) וַיָּבֹא...אֵלֶיהָ *wayyavoʾ...ʾeleha*, בּוֹא *boʾ* (H935), the standard euphemism for consummation. Crucially, *laqach* + a woman is the ordinary Hebrew idiom for contracting marriage; here the "taking" is lawful wedlock, not the illicit seizure of Gen 6:2 — a Category-B ("take as wife") rather than Category-A ("seize") instance, even as the bare *saw...took* skeleton reproduces the motif.

**Analogy to David.** Kline (2024; bibleinterp 2025) [confirmed] makes this verse a linchpin: Judah's "seeing and taking" of Bath-shua is read as an intentional narrative analogy to David's *saw...sent...took* of Bathsheba (2 Sam 11:2,4), reinforced by the onomastic overlap — Bathsheba appears as *Bath-shua* (בַּת־שׁוּעַ) in the Chronicler's genealogy [general-knowledge, not fetched this run]. Kline situates the pairing within a lineage of Judah-narratives and cites Sternberg (1985:365), Garsiel (1985:18–23), and Alter for the analogical method [confirmed as dossier references]. Methodologically this rests on Fishbane's principle that shared distinctive diction signals deliberate allusion [confirmed], and on Alter's *Leitwort* poetics [confirmed]. The same *raʾah...laqach* verb-pair anchors Eve's transgression (Gen 3:6, *saw...good...took*) and the Watchers' (Gen 6:2, *saw...fair...took*), per Wenham [confirmed], so Gen 38:2 functions as a mid-genealogy echo binding the primeval pattern to the David story.

**Caveats.** The parallel is structural, not lexically airtight: unlike Gen 3:6 and 6:2, Judah's "seeing" carries *no* adjective of desirability (*ṭov*, *ṭovot*), so the desire-laden coloring is supplied by the analogy, not by this verse's own vocabulary. And because *laqach* here denotes legitimate marriage, the transgressive charge attaches less to the act than to its Canaanite exogamy and grim sequel (Er, Onan, Tamar). No monograph argues a single authored Gen 3→6→38→2 Sam 11 "sin pattern"; that synthesis is assembled from Fishbane's method plus Wenham and Kline/Sternberg, and should be presented as such.

### Exodus 2:1-10 — Moses seen to be "good"; drawn and taken

When the Levite mother bears her son the narrator reports (2:2): *wattēreʾ ʾōtô kî-ṭôv hûʾ* — "she saw that he was good/goodly" (Sefaria/Revised JPS: "when she saw how beautiful he was") — followed by *wattiṣpĕnēhû*, "she hid him." The collocation *raʾah* (H7200) + *kî-ṭôv* (H2896) is the exact verbal signature of the Genesis 1 creation refrain, *wayyarʾ… kî-ṭôv* [general-knowledge], and stands one lexeme short of Eve's triad in Gen 3:6 (*saw…good…took*) — the echo Wenham [confirmed] traces forward into the Watchers' "saw…fair…took" at Gen 6:2. Here, though, perceiving the child as "good" issues not in seizure but in concealment: the mother sees and hides. The motif is being deliberately re-tooled.

The full seeing/taking sequence surfaces at 2:5, transposed to Pharaoh's daughter: *wattēreʾ et-hattēvāh* ("she saw the ark"), *wattišlaḥ et-ʾămātāh* ("she sent her maidservant"), *wattiqqāḥehā* ("and took it") — *raʾah / šalaḥ* (H7971) */ laqaḥ* (H3947, wayyiqtol with assimilated nun). This is the identical triad Alter reads in David's crime (2 Sam 11: saw / sent / took) [general-knowledge], the "seeing and taking" that Kline and Sternberg treat as the David narrative's index of predatory desire [confirmed]. Fishbane's criterion — shared distinctive diction as a marker of intentional linkage [confirmed] — applies, but the valence is inverted: the signature verb *laqaḥ*, which "takes" Eve's fruit, the Watchers' wives (1 Enoch 6-7 [confirmed]), and Bathsheba, here "takes" an endangered infant to preserve him. The taking is rescue, and it is subversive — a daughter of the murdering Pharaoh countermanding his own decree.

Two details sharpen the reversal. The basket is a *tēvāh* (H8392), a word used elsewhere only of Noah's ark: both vessels carry life safely through the water of judgment. And where the pattern's engine of transgression is *ḥamad*, "covet" (Gen 3:6; Achan; the tenth commandment [confirmed, TheTorah.com]), 2:6 gives the near-homophone *wattaḥmōl*, "she took pity" (*ḥamal*, H2550) — compassion, not craving. The unit closes with a naming etiology: *mĕšîtihû*, "I drew him out" (*mašah*, H4871).

**Caveats.** No dossier source situates Exodus 2 within a unified "seeing/taking sin pattern"; it functions as the motif's benign counter-instance, and placing it in this study is my analytical move, not a claimed authorial scheme. The sense of *ṭôv* in 2:2 is disputed — a merely "healthy/goodly" child versus an intended allusion to Gen 1 — so the creation echo is a literary inference, not lexically compelled. The *ḥamal*/*ḥamad* resonance is phonetic only; the roots (ח-מ-ל vs. ח-מ-ד) are distinct (my observation). And *wattiqqāḥehā* leaves the taker grammatically ambiguous (the daughter, or the maid she sent).

### Deuteronomy 21:10-14 — the beautiful captive (the pattern codified in law)

Here the see–desire–take sequence is not narrated as transgression but *legislated* as permitted procedure. A soldier who has taken captives, and "*sees* (וְרָאִיתָ, *we-ra'ita*, from *ra'ah*, H7200) among the captives a woman beautiful of form (אֵשֶׁת יְפַת־תֹּאַר), and *desires* her (וְחָשַׁקְתָּ, *we-chashaqta*, from *chashaq*, H2836), and *takes* her (וְלָקַחְתָּ, *we-laqachta*, from *laqach*, H3947) to himself for a wife" (v. 11). The Masoretic text (WLC):

> וְרָאִיתָ֙ בַּשִּׁבְיָ֔ה אֵ֖שֶׁת יְפַת־תֹּ֑אַר וְחָשַׁקְתָּ֣ בָ֔הּ וְלָקַחְתָּ֥ לְךָ֖ לְאִשָּֽׁה׃
>
> "And seest among the captives a beautiful woman, and hast a desire unto her, that thou wouldest have her to thy wife" (v. 11, KJV).

The triad *ra'ah → chashaq → laqach* replays the visual-appetitive-acquisitive arc Genesis attaches to Eve (*ra'ah…laqach*, 3:6) and the sons of God (*ra'ah…laqach*, 6:2). Two of the three verbs match verbatim; the middle term, however, is *chashaq* — not the *chamad* (H2530) of the Decalogue's covetousness clause (Exod 20:17; cf. TheTorah.com on *chamad* [confirmed]). *Chashaq* denotes attachment or setting one's desire upon (the verb used of YHWH's love for Israel, Deut 7:7; 10:15 [general-knowledge]), so the appetite is named without the Decalogue's forbidden coloring.

What marks the juridical instance is the hedging that follows: the captive shaves her head, pares her nails, sheds "the raiment of her captivity," and mourns her parents a full month (vv. 12-13) before consummation; and if the man later "has no delight" (חָפַצְתָּ, *chafetz*, H2654) in her, he must free her — not sell her, not treat her as merchandise — "because thou hast humbled her" (עִנִּיתָהּ, *'innita*, from *'anah*, H6031, v. 14). The law admits the see-desire-take impulse yet legislates delay and a floor of dignity against it. Classical halakhah read the whole grant as concession: "the Torah spoke only in view of the evil inclination" (b. Qiddushin 21b [general-knowledge]).

Reading this beside the narrative "fall" texts rests methodologically on Alter's *Leitwort* device [confirmed] and Fishbane's criterion that shared distinctive vocabulary signals intentional linkage [confirmed]; Kline independently tags the "seeing" and "taking" of Bathsheba as deliberate analogy [confirmed].

**Caveats.** (1) This is casuistic law — prescriptive, not descriptive; the sequence appears as regulated permission, not a paradigm of sin. (2) Only *ra'ah* and *laqach* are lexically shared with Gen 3:6/6:2; the desire-term *chashaq* differs, so the tie is structural and thematic, not a verbatim three-verb chain. (3) The passage arguably *restrains* the very sequence it names, cutting against reading it as another straightforward link in a "sin pattern." (4) No dossier source unites Gen 3 → 6 → Josh 7 → 2 Sam 11 → Deut 21 as one authored template; this juxtaposition is assembled from Alter's method, Fishbane, and the Kline/Sternberg David scholarship.

### Joshua 7:20-21 — Achan saw, coveted, took (the explicit triad)

Achan's confession is the single place in the Hebrew Bible where the seeing–desiring–taking sequence is spelled out in three consecutive first-person verbs, with the loaded root *chamad* occupying the middle slot. Fetched from Sefaria this session (Hebrew: Miqra according to the Masorah; English: Revised JPS, 2023):

> **Josh 7:20** — "Achan answered Joshua, 'It is true, I have sinned (*chata'ti*) against the ETERNAL, the God of Israel. This is what I did:'"
> וַיַּעַן עָכָן ... אָנֹכִי חָטָאתִי לַיהֹוָה אֱלֹהֵי יִשְׂרָאֵל
>
> **Josh 7:21** — "I saw among the spoil a fine Shinar mantle ... and I coveted them and took them. They are buried in the ground in my tent..."
> וָאֵרֶא בַשָּׁלָל אַדֶּרֶת שִׁנְעָר אַחַת טוֹבָה ... וָאֶחְמְדֵם וָאֶקָּחֵם

The triad is a chain of three Qal *wayyiqtol* (waw-consecutive) verbs: *wa'ere'* (*ra'ah*, "I saw," H7200) — *wa'echmedem* (*chamad*, "I coveted them," H2530) — *wa'eqqachem* (*laqach*, "I took them," H3947). The paired objective suffixes ‑*em* ("them") weld coveting to seizure, and the mantle is qualified as *tovah* ("good/fine") — the same evaluative adjective the primeval scene assigns its object. Note too the qere/ketiv on the first verb (ketiv *wa'er'eh*, qere *wa'ere'*), a textual flag sitting on the very act of seeing.

This is the fullest verbal instantiation of the template Wenham (*Genesis 1–15*) locates in Gen 3:6 and 6:2, where "saw...good/fair...took" (*ra'ah...tov...laqach*) marks transgressive desire [confirmed, dossier]. Achan tightens the parallel because Gen 3:6 itself calls the tree *ne'chmad* ("desirable," *chamad* root) [general-knowledge; Gen 3:6 not fetched this run] — so Achan's finite *chamad* makes explicit the desire the Eden verse names only adjectivally. On Fishbane's criterion — shared distinctive vocabulary signalling intentional allusion — the cluster reads as deliberate; but, per the honesty rule, no single monograph threads Gen 3 → 6 → Josh 7 → 2 Sam 11 as one authored pattern. That synthesis is assembled here from Fishbane's method plus Wenham's (3→6) reading and the *chamad* scholarship.

*Chamad* also makes this a narrative enactment of the Tenth Commandment's *lo tachmod* (Exod 20:17; Deut 5:21) [confirmed, dossier via TheTorah.com]. TheTorah.com frames the standing debate over whether *chamad* denotes a feeling or an act; Achan's confession answers it narratively — the coveting issues directly in the taking. And the sequence is lethal, like the Fall: the *cherem* breach kills thirty-six at Ai (7:5) and brings death on Achan's household (7:24-25), the desire→sin→death arc abstracted at James 1:14-15 [confirmed, dossier]. (That the loot is a mantle of *Shinar* — the land of Babel, Gen 11:2 — quietly threads the grasp back to primeval overreach [general-knowledge].)

**Caveats.** The RJPS renders *tovah* as "fine," muting the *tov* link to Gen 3:6 that the Hebrew preserves. "Category A" status rests on the lexical triad itself, not on any explicit intertextual marker inside Joshua. And the Gen 3:6 verbal data here is named from memory, not fetched this session.

### Judges 14:1-3 — Samson saw a woman and said "take her for me"

**Text (MT; NJPS with KJV noted).** v.1: *wayyēred šimšôn timnātâ wayyarʾ ʾiššâ* — "Once Samson went down to Timnah; and while in Timnah, he noticed [KJV *saw*] a certain young Philistine woman." v.2: "*ʾiššâ rāʾîtî* — I have seen a woman… *qĕḥû-ʾôtāh lî lĕʾiššâ* — now therefore get [take] her for me as a wife." v.3, over his parents' objection: "*ʾôtāh qaḥ-lî kî-hîʾ yāšĕrâ bĕʿênāy* — Get me that one, for she is right in my eyes" (KJV "she pleaseth me well").

**Operative verbs.** The template is stripped to its skeleton: *raʾah*, "see" (H7200), at vv.1–2, then *laqach*, "take" (H3947), three times — imperative *qĕḥû* (v.2), infinitive construct *lāqaḥat* in the parents' protest (v.3), imperative *qaḥ* (v.3). Category A (seeing) → Category B (taking), with a distinctive twist: the "take" is **demanded aloud** rather than executed by the seer's own hand.

**The "eyes" Leitwort and its reversal.** Samson supplies no *ṭôb* ("good," Gen 3:6) or *ḥāmad* ("covet," Achan, Josh 7:21); his sole warrant is *yāšĕrâ bĕʿênāy* (root *yashar*, H3474) — "right in my eyes" — echoed at 14:7 (*wattîšar bĕʿênê šimšôn*). The leading word is *ʿayin/ʿênayim* (H5869), a *milah manḥah* in Buber's sense — the Leitwort device defined by Alter [confirmed] and Buber [confirmed]. Samson's private "right in his eyes" is verbally the book's own indictment: *ʾîš hayyāšār bĕʿênāyw yaʿăśeh*, "everyone did what was right in his own eyes" (Judg 17:6; 21:25 [confirmed, fetched]). The payoff is lexically exact — the man who sees and takes *by his eyes* is later seized by the Philistines who *waynaqqĕrû ʾet-ʿênāyw*, "gouged out his eyes" (16:21 [confirmed, fetched]; *naqar*, H5365). Sight opens the cycle; blinding closes it.

**Placement in the catalogue.** By Fishbane's criterion — shared distinctive vocabulary as a marker of design [confirmed] — the *raʾah…laqach* string ranges Samson alongside Eve (Gen 3:6), the sons of God (6:2), Achan (Josh 7:21), and David (2 Sam 11:2–4).

**Caveats.** No dossier monograph treats Samson as a member of a single authored *raʾah→laqach* "sin pattern"; that grouping is assembled here from the Leitwort device plus Fishbane's method. The *ʿayin* wordplay (14:3 → 16:21) and the tie to the "right in his own eyes" refrain are standard literary observations [general-knowledge], not claims sourced to a Samson-specific study in the dossier. Note too that NJPS's "she pleases me" flattens *yāšĕrâ bĕʿênāy*, whose literal "right/straight in my eyes" is precisely what carries the pun.

### 2 Samuel 11:1-4 — David saw, sent, and took Bathsheba

**Fetched text (RJPS, via Sefaria).** 11:2 — *wayyar' ishah rochetzet ... wehā'ishah tovat mar'eh me'od* / וַיַּ֥רְא אִשָּׁ֛ה רֹחֶ֖צֶת ... וְהָ֣אִשָּׁ֔ה טוֹבַ֥ת מַרְאֶ֖ה מְאֹֽד, "he saw a woman bathing ... the woman was very beautiful." 11:4 — *wayyishlach dawid mal'akim wayyiqqacheha* / וַיִּשְׁלַח֩ דָּוִ֨ד מַלְאָכִ֜ים וַיִּקָּחֶ֗הָ, "David sent messengers ... and took her."

The scene runs on the same two-verb spine that governs Gen 3:6 and 6:2: *ra'ah* (H7200, "see") in v.2 and *laqach* (H3947, "take") in v.4. The object of the royal gaze is glossed *tovat mar'eh me'od*, "very good of appearance" — *tovat* ("good," cf. Gen 3:6 *tov*, 6:2 *tovot*) modifying *mar'eh*, itself a noun from the root *ra'ah*. Desirability is thereby lodged inside the act of seeing, the same fusion of sight and value that drives Eve's and the Watchers' "taking." Alter reads the chapter's opening as a terse chain of transitive verbs (saw–sent–took–lay) that reduces Bathsheba to a grammatical object and exposes the king's appetite [general-knowledge].

What marks this as a Tier-2 (spread) instance is the gap between seeing and taking. Where Gen 3:6 and 6:2 juxtapose *saw* and *took*, 2 Samuel interposes v.3, in which David sends to inquire (*shalach*, H7971) after the woman and is told she is Uriah's wife. Sternberg treats precisely this interval as the moral crux: the report of her marriage is information that should abort the sequence, so the narrative "filling" of the see→take gap converts impulse into deliberation and deliberation into guilt [confirmed]. Fokkelman reads the same verb-chain as the structural engine of the chapter [confirmed]. The doubled *shalach* (vv.3, 4) makes "sending" the royal instrument that closes a distance no ordinary man could cross.

Kline lists the "seeing" and "taking" of Bathsheba (11:2, 4) as an intentional narrative analogy — pairing it with Judah's seeing-and-taking of Bath-shua in Gen 38:2 — citing Sternberg (1985:365) and Garsiel (1985:18–23) [confirmed]. On Fishbane's criterion, it is the shared, distinctive lexical pair that licenses reading such links as deliberate rather than coincidental [confirmed].

The verdict seals the motif lexically. Nathan's parable (12:4) twice uses *laqach* — the rich man is "loath to take" (*laqachat*) from his own flock, then "took" (*wayyiqqach*) the poor man's one ewe-lamb — the very verb applied to Bathsheba in 11:4, so that "You are the man" (12:7) retroactively names David's *laqach* as theft.

**Caveats.** Framing this scene as a "royal re-enactment of the Fall" is an assembled synthesis, not a claim any one study makes: it joins Fishbane's allusion method to the Wenham reading of Gen 3→6 and applies it to the David material through Sternberg, Kline, and Garsiel [confirmed as a construction]. Alter's and Sternberg's own analyses foreground narrative artistry and the analogy to Gen 38, not a programmatic replay of Eden. The Hebrew here is *shalach* + *laqach*, not *chamad*; the "coveting" link to the motif is thematic, carried by *tovat mar'eh*, not by a shared desire-verb.

### Numbers 25:6-8 — Phinehas saw and took a spear (righteous zeal)

The Baal-Peor episode furnishes the motif's sharpest reversal. The verb pair that elsewhere drives transgression — *ra'ah* ("see," H7200) followed by *laqach* ("take," H3947) — recurs here intact, but its object is inverted.

Verse 6 first stages the offense in the idiom of sight: an Israelite man brings the Midianite woman near "to his companions, in the sight of (*le'eynei*, לְעֵינֵי) Moses and of the whole Israelite community" (Num 25:6, RJPS) — the transgression is committed before the communal *eyes*. Verse 7 answers with the priest's gaze and grasp: "When Phinehas... saw this (*wayyar'*, וַיַּרְא), he left the assembly and, taking (*wayyiqqach*, וַיִּקַּח) a spear (*romach*, רֹמַח, H7420) in his hand" (Num 25:7). Verse 8: "he... stabbed (*wayyidqor*, וַיִּדְקֹר; *daqar*, H1856) both of them... Then the plague was checked (*wattē'ātsar*, וַתֵּעָצַר; *'atsar*, H6113)" (Num 25:8).

Two features mark the redirection. First, the *wayyiqtol* chain *wayyar'... wayyaqom... wayyiqqach* ("he saw... he rose... he took") reproduces the paratactic rhythm of Gen 3:6 and Gen 6:2 — what Alter classifies as a *Leitwort*, a thematic key-word repeated across contexts to bind them [confirmed: Alter, *The Art of Biblical Narrative*]. Second, the object of *laqach* is not the desirable woman but a *romach*, a weapon: the "taking" that in Eden and in 2 Samuel 11 seizes the forbidden object is here weaponized against it. On Fishbane's criterion — shared distinctive vocabulary as a signal of intentional linkage [confirmed: Fishbane, *Biblical Interpretation in Ancient Israel*] — the lexical overlap invites the reader to hear the transgression-formula and register its violent cancellation.

The narrative rewards the inversion where the earlier scenes punish it: Phinehas receives a covenant of peace (Num 25:12-13), and Ps 106:30-31 credits the act to him as righteousness, echoing the reckoning-language of Gen 15:6 [general-knowledge]. The *see -> take* that begets death (cf. Jas 1:15) becomes, in priestly hands, the *see -> take* that stays it.

**Caveats.** No source in the dossier treats Numbers 25 as a deliberate inversion of the Genesis *see -> take* formula; the antithesis reading is assembled here from Alter's *Leitwort* concept and Fishbane's allusion-criterion, and should be held as a literary observation, not a documented authorial intention. *Ra'ah* and *laqach* are among the commonest verbs in Biblical Hebrew, so their co-occurrence is suggestive rather than probative — the case rests on the syntactic patterning and thematic reversal, not on rare diction. The RJPS "when... saw this" smooths the Hebrew, which reads simply "and he saw."


---

## 6. A survey of theological interpretation

### Method: Leitwort and inner-biblical allusion

The claim that recurring verbs such as *ra'ah* ("to see") and *laqach* ("to take") carry interpretive weight rests on a specific literary-critical premise: that lexical repetition in biblical narrative is deliberate rather than incidental. Martin Buber gave this premise its classic formulation in his account of *Leitwort* ("leading-word") style, rendered in Hebrew as *milah manḥah* [confirmed]. For Buber, a Leitwort is a word or word-root that recurs significantly across a text or a sequence of texts; the reader who follows those repetitions is guided toward a meaning the narrative does not state discursively. Franz Rosenzweig, his collaborator on the German Bible, treated the same phenomenon as intrinsic to the form of biblical storytelling rather than a defect of "primitive" style [confirmed]. Both were reacting in part against source-critical atomization, reading the received text as an artful whole.

Robert Alter naturalized this approach for English readers, glossing the Leitwort as a "thematic key-word" and treating verbal recurrence as a primary technique of biblical art [confirmed]. In his commentary on 2 Samuel 11 he reads David's chain of *saw / sent / took* as purposeful patterning of the transgression [general-knowledge].

Buber and Alter locate the device chiefly *within* a narrative unit. Michael Fishbane extends the logic *across* the canon: in his account of inner-biblical interpretation, shared distinctive vocabulary is the principal signal that one text intentionally alludes to another [confirmed]. This diachronic move — reconstructing an actual history of allusion and scribal exegesis — differs in orientation from Buber's synchronic, whole-text reading, though the two are routinely invoked together.

The method has a genuine limit, and Fishbane's own criterion exposes it. *Ra'ah* and *laqach* are among the most common verbs in Biblical Hebrew; their mere co-occurrence is weak evidence of allusion, since almost any narrative of desire and acquisition will deploy them. What can bear argumentative weight is not the isolated verbs but the distinctive *cluster* and *sequence* — seeing, evaluating ("good"/"fair"), then taking — and the density with which it recurs. Rarer, more marked terms (e.g. *chamad*, "to covet") function as stronger allusive markers than the frequent verbs alone [confirmed]. The honest verdict is that the motif is suggestive as patterned repetition, not demonstrable from raw vocabulary counts.

### The Fall and the Flood: Genesis 3:6 echoed at 6:2

The clearest inner-Genesis instance of the "seeing"→"taking" motif links the garden to the generation of the Flood. In Gen 3:6 "the woman *saw* that the tree was *good* for food ... she *took* of the fruit thereof" (KJV); in Gen 6:2 "the sons of God *saw* the daughters of men that they were *fair*; and they *took* them wives" (KJV). Both verses run the same Hebrew spine: *ra'ah* ("saw," Qal *wayyiqtol* — *wattēreʾ*, 3fs, at 3:6; *wayyirʾû*, 3mp, at 6:2), the evaluative *ṭov* ("good"/"fair" — *ṭov* of the tree, *ṭovot* of the women), and *laqach* ("took," Qal *wayyiqtol* — *wattiqqaḥ* / *wayyiqḥû*).

Gordon Wenham makes this parallel explicit: his Word commentary reads the "saw ... fair ... took" of 6:2 as a deliberate echo of Eve's "saw ... good ... took," so that the transgression of the "sons of God" is narrated in the grammar of the first sin [confirmed]. In his essay "Original Sin in Genesis 1–11" he frames the primeval history as a logical, escalating development of sin, of which 6:1–4 is a further stage [confirmed]. Nahum Sarna reads the episode within the primeval theme of humanity overstepping the bounds God has fixed [confirmed]. Umberto Cassuto, by contrast, resists any transgression reading of 6:2 at all: in his comment on the verse he takes "took … wives" as the ordinary Hebrew idiom for lawful marriage and derives the women's being "good/fair" from the usage at Exod 2:2 rather than from Gen 3 — an important dissent that marks the "saw … took" echo as an argued literary judgment rather than a settled fact [confirmed]. Methodologically this rests on Fishbane's principle that shared distinctive vocabulary signals intentional allusion [confirmed], and on the Buber–Rosenzweig and Alter notion of the *Leitwort* (Heb. *milah manḥah*) — a repeated key-word bearing thematic weight [confirmed].

Two cautions temper the reading. First, the shared triad is narrower than sometimes claimed: the desire vocabulary of 3:6 — *ta'awah* ("a delight") and *neḥmad* (Niphal participle of *chamad*, "desirable") — has no counterpart in 6:2, which instead closes with *bachar* ("chose"). The common chain is *saw–good–took*, not the full lexicon of coveting. Second, the identity of the "sons of God" is disputed — Enochic tradition reads them as angelic Watchers, whereas Ramban takes them as human rulers who *took* wives by force, even married women [confirmed] — yet the verbal echo holds on either construal. Source critics who treat 6:1–4 as an originally independent mythic fragment would locate the echo in the canonical final form rather than in single authorship [general-knowledge].

### David and Bathsheba as re-enactment

Of the biblical "seeing"+"taking" episodes, David and Bathsheba (2 Sam 11) is the one most often read as a deliberate re-enactment of a Genesis prototype. The chain is compact: David "saw" a woman bathing (*ra'ah*, וַיַּרְא, 11:2) — "very beautiful to look upon," *ṭôḇat mar'eh*, whose noun *mar'eh* ("appearance") shares the root r-'-h with the verb of seeing — then "sent" (*shalach*) messengers and "took" her (*laqach*, וַיִּקָּחֶהָ, 11:4). Robert Alter, who established the *Leitwort* ("thematic key-word") as a compositional unit (*The Art of Biblical Narrative*, 1981) [confirmed], reads this saw–sent–took progression as a patterned verbal sequence enacting the king's abuse of power (*The David Story*, 1999) [general-knowledge]. The same frame governs Eve's act, where she "saw" the tree was "good" (*ṭôḇ*), "desirable" (*neḥmad*, niphal participle of *chamad*), and "took" (*wattiqqach*, Gen 3:6).

The strongest *explicit* case for intentional analogy points not to Eden but to Gen 38. Joanna Kline (*Narrative Analogy in the David Story*, 2024; bibleinterp essay, 2025) lists the "seeing" and "taking" of Bathsheba (11:2, 4) beside Judah's "seeing" and "taking" of the Canaanite Bath-shua (Gen 38:2: *wayyar'* … *wayyiqqacheha*), reinforced by the shared name Bath-shua [confirmed]. She builds on Meir Sternberg's extended reading of 2 Sam 11 — his gap-filling and repetition analysis, which she cites at p. 365 for the analogy — and on Moshe Garsiel's catalogue of Samuel's comparative structures (1985:18–23) [confirmed as Kline's citations]. J.P. Fokkelman's close reading (*Narrative Art and Poetry in the Books of Samuel* I, 1981) similarly foregrounds the chapter's verbal artistry [confirmed work].

Methodologically this all rests on Michael Fishbane's criterion (1985): distinctive shared vocabulary, not a generic plot, marks allusion [confirmed] — a needed caution, since "see and take" could be mere narrative convention. The sequel tightens the thread: Nathan's parable turns on the same root — the rich man "took" (*laqach*, וַיִּקַּח) the poor man's ewe-lamb (12:4) — and the verdict "you have taken (*laqachta*) his wife" (12:9) binds deed to indictment. The lexical echo of Eden (*ṭôḇ* plus the root r-'-h) is suggestive, but the honest position is that the Samuel critics argue the analogy primarily with Judah and the patriarchs; the direct Gen 3 → David "sin pattern" is an interpretive synthesis (Fishbane's method layered onto the Gen 3 → Gen 38 verbal chain), not the explicit claim of any one of these monographs.

### Coveting, the eye, and the Tenth Commandment

If the motif's outer frame is "saw... took" (*ra'ah... laqach*), its concealed middle term is the verb of desire. Achan's confession gives the sequence unabbreviated: "I saw (*wa'ere'*) among the spoil a fine Shinar mantle... and I coveted them (*wa'echmedem*) and took them (*wa'eqqachem*)" (Josh 7:21, JPS). Here *ra'ah* → *chamad* → *laqach* (H2530) stand in explicit succession — eye, heart, and hand named as three distinct beats. Narratives such as Gen 3:6 and 2 Sam 11 compress the triad, dropping the middle verb; yet Gen 3:6 retains the desire vocabulary itself, the tree being "a delight to the eyes" (*ta'avah... la-'enayim*, from *avah*) and "desirable" (*nechmad*, the niphal of *chamad*) before the woman "took" (*wattiqqach*). On Fishbane's principle that shared distinctive vocabulary marks an intended connection [confirmed], *chamad* is the lexical hinge between these scenes.

The Tenth Commandment isolates this middle term and legislates it. Exodus uses one verb twice — "You shall not covet (*lo tachmod*) your neighbor's house... you shall not covet (*lo tachmod*) your neighbor's wife" (Exod 20:14 MT = 20:17 in the Christian numbering). Deuteronomy's parallel fronts the wife and splits the lexicon: "You shall not covet (*lo tachmod*) your neighbor's wife. And you shall not crave (*ve-lo tit'avveh*, hitpael of *avah*) your neighbor's house, or field..." (Deut 5:18 MT = 5:21) — pairing *chamad* with the *ta'avah* root that Gen 3:6 had already stacked.

Whether *chamad* names a feeling or an action is the standing dispute, surveyed by TheTorah.com's "Do Not Covet: Is It a Feeling or an Action?" [confirmed]. One camp takes it as inward emotion, so that the commandment uniquely regulates a disposition; another, appealing to Micah 2:2 — "They covet fields (*chamdu*), and seize them; houses, and take them away (*ve-nasa'u*)" — holds that *chamad* names acquisitive desire culminating in seizure, its parallelism with *gazal* ("seize") and *nasa'* ("carry off") pulling the verb toward act, not mere affect. Deuteronomy's substituted *tit'avveh* is then read by some as distinguishing the covetous scheme from the bare wish.

Behind the verb stands the eye as desire's organ. 1 John 2:16 names "the desire of the eyes," which Augustine glosses as *concupiscentia oculorum* (Confessions X.35) [confirmed]; James 1:14–15 traces desire to sin to death [confirmed]. Ibn Ezra, on the Decalogue, famously argues that a disciplined person does not covet what is beyond reach, treating *lo tachmod* as a curable orientation of the seeing self [general-knowledge]. On this reading the wider motif's "seeing" is never neutral perception: the eye is where *ta'avah* kindles, and *chamad* is the hinge that turns sight into theft.

### Second Temple and Enochic reception of Genesis 6

The *Book of the Watchers* (1 Enoch 6–11) is the earliest sustained reading of Genesis 6:1–4, and it builds its whole etiology of evil out of the terse "saw … took." In the host edition of this report — R. H. Charles (1893) set against the Hermeneia translation of Nickelsburg & VanderKam (2013) — 1 Enoch 6:2 reproduces the biblical sequence and amplifies it: the watchers, "the sons of heaven, saw them and desired them" (Hermeneia); Charles renders the same clause "saw and lusted after them." Where Gen 6:2's *laqach* ("took," *wayyiqchu*) governs "wives," both editions have the watchers resolve to "choose for ourselves wives from the daughters of men" — a lexical softening of "take" into deliberate election, followed by the sworn descent on Hermon, the oath of the "two hundred," and their chief Shemihazah/Semjâzâ. The Enochic author thus reads the biblical *ra'ah*-plus-*laqach* not as a passing notice but as a premeditated, oath-bound boundary-crossing between heaven and earth [confirmed, host edition].

For this tradition the angelic transgression is the *origin* of evil. Charles's own note in the host edition observes that "lust is throughout the whole book represented as the great sin of the angels" [confirmed, host edition]. Reed, *Fallen Angels* (2005), argues that the Enochic stream roots the entry of evil in the watchers' rebellion — illicit union plus the forbidden teaching associated with Asael — rather than in Adam [confirmed, in dossier]. Stuckenbruck (DSD 2000) traces how this "angels/giants" exegesis of Gen 6 developed across the third–second centuries BCE [general-knowledge], and Kugel notes that reading "sons of God" as angels was the dominant Second Temple construal [general-knowledge]. Jubilees 5 retells the same descent and judgment within its own chronological frame [general-knowledge]; note that Jubilees is not part of the host edition, which prints 1 Enoch alone.

This yields the standard contrast between an **Enochic (Watchers) etiology**, which locates evil's entry in a heavenly revolt and largely sidelines Eden, and an **Adamic (Eden) etiology**, dominant later in Paul, 4 Ezra/2 Baruch, and much rabbinic and Christian thought [general-knowledge; Reed frames the two as rival origins-of-evil, confirmed in dossier].

One caution should be flagged. The modern literary claim that Gen 6:2's "saw … took" *re-enacts* Eden's "saw … took" (Gen 3:6; so Wenham, *Genesis 1–15*) is an interpretive move by later readers — grounded in the shared verbs *ra'ah*/*laqach* recorded in this project's tagged corpus — not the Enochic authors' own reading [Wenham confirmed in dossier]. (Cassuto, notably, reads 6:2 as ordinary lawful marriage and resists the Eden echo entirely [confirmed].) 1 Enoch does not present the watchers as repeating Adam; it offers an *alternative* etiology in which Adam is essentially absent. Reading 6:2 as an "Eden re-enactment" therefore harmonizes two origin-stories that the Second Temple sources deliberately kept apart, and should be labelled as such rather than assumed.

### Rabbinic and medieval Jewish readings

The classical Jewish exegetes read Genesis 3:6 and 6:2 locally, verse by verse, rather than as one authored cross-textual pattern; yet their comments repeatedly isolate the very verbs the modern literary readers foreground — *ra'ah* ("saw") and *laqach* ("took") — and probe the desire that stands between them.

On Genesis 3:6, *Bereshit Rabbah* 19:5 anatomizes the woman's *seeing* as a compound appetite. R. Yosei bar Zimra notes that "three matters were stated regarding that tree… and the three of them were stated in one verse": good for eating, a "delight to the eyes" (*ta'avah la-einayim*), and "desirable [*neḥmad*, from *ḥamad*] as a source of wisdom [*lehaskil*]" [confirmed, fetched from Sefaria]. Significantly, the midrash reads the *taking* itself concretely and non-violently — on "she took of its fruit" R. Aivu says "she squeezed grapes and gave it to him," and the inclusive particle *gam* ("also") is expanded so that Eve fed the fruit to the beasts and birds as well [confirmed, fetched].

Ibn Ezra (on 3:6) glosses "the woman saw" as "in her heart," an inward perception rather than literal sight, and distinctively holds that the tree "possessed the power to instill sexual desire" (*ta'avat ha-mishgal*), so that eating led directly to Adam's "knowing" (*yada*) his wife [confirmed, fetched]. Here the desire behind the *seeing* is specifically erotic — a reading Genesis Rabbah's more intellectualist triad does not require.

The *taking* turns coercive in the medieval treatment of Genesis 6:2. Rashi glosses "sons of God" as "the sons of princes and rulers" (citing *Bereshit Rabbah* 26), noting that "whomever they chose" includes "even a married woman," and that a bride adorned for her wedding canopy would be seized by a lord "first"; he also records the alternate reading of "princely angels" [confirmed, fetched]. Ramban explicitly endorses Rashi — "this is the language of Rashi, and so it is in *Bereshith Rabbah*" — but sharpens it into a charge of *ḥamas* (violence): "when the daughters of men were fair, they would take them forcibly [*be-ones*] as wives," married women included, so that the Flood's punishment fell "only because of the violence," a wrong so self-evident it "does not require the Torah" to prohibit it [confirmed, fetched].

Two cautions. First, none of these sources builds a *Leitwort* chain from 3:6 to 6:2; the shared *ra'ah*/*laqach* sequence is a modern literary observation (argued by Wenham, resisted by Cassuto; Alter's *Leitwort* principle systematizes such linkage [confirmed, dossier]), not a classical one. Second, the readings disagree — over the desire's nature (intellectual and appetitive in Genesis Rabbah versus sexual in Ibn Ezra) and over the agents of 6:2 (human rulers for Rashi and Ramban; angels in the tradition Rashi merely reports).

### Patristic and Reformation readings: the lust of the eyes

The patristic tradition reads the "seeing"+"taking" sequence through the lens of disordered desire, and Augustine gives it its enduring name. In *Confessions* X.35 he isolates *concupiscentia oculorum*, the "lust of the eyes," as a distinct appetite — a craving to know, test, and possess through the senses, sight above all, which he links to *curiositas* [confirmed, in dossier]. The phrase is not Augustine's coinage but the Vulgate of 1 John 2:16, whose triad (*concupiscentia carnis*, *concupiscentia oculorum*, *superbia vitae*) he treats as a taxonomy of fallen wanting [confirmed, in dossier]. In *City of God* XIV, concupiscence becomes the enduring legacy of Adam's disobedience: the will's self-rupture, transmitted to his posterity as an appetite no longer governed by reason [confirmed, in dossier]. The eye, on this reading, is the gateway through which the world solicits the will.

The Hebrew of Genesis 3:6 gives the reading a genuine anchor. The verse names the organ explicitly: the woman *saw* (*ra'ah*) that the tree was "a delight to the eyes" (*ta'awah … la-'einayim*) and "desirable" (*nechmad*, from *chamad*), and so she "took" (*laqach*) — appetite routed through vision, then seized [confirmed; Sefaria, Gen 3:6]. Yet Augustine's own emphasis complicates a purely ocular account: in *City of God* XIV.13 he locates the *root* of the first sin in pride (*superbia*), the will's prior turning from God, with concupiscence as its penalty and continuing symptom rather than its first cause [confirmed, in dossier]. The eye is the conduit; the taproot lies deeper.

The Reformers inherit and shift the accent. Calvin, on Genesis 3:6, treats the enticing "appearance" as the avenue of the Fall but places its origin in unbelief — distrust of God's word — so that the outward lust of the eyes follows a prior infidelity [general-knowledge]. Luther, in his *Lectures on Genesis*, likewise begins the Fall with doubt of the Word, after which the eyes and appetite are drawn in, and reads concupiscence as the abiding disease left in human nature [general-knowledge]. The strand thus converges on the eye as the passage of desire while disagreeing on the cause behind it — pride (Augustine), unbelief (Calvin, Luther) — a distinction worth preserving against any flattening into a single "lust of the eyes."

### New Testament reception: 1 John 2:16 and James 1:14-15

The Hebrew *see*→*desire*→*take* grammar of Genesis 3:6 receives two influential New Testament reformulations, each of which transposes the narrative motif into ethical abstraction rather than reproducing the Leitwort verbally.

**1 John 2:16.** The triad "the desire of the flesh, the desire of the eyes, and the pride of life" (wording per dossier) has been read since antiquity as a distillation of the three-fold appeal the woman perceives in Gen 3:6: the tree "good for food" (appetite/flesh), "a delight to the eyes" (the eyes), and "desirable to make wise" (the ambition of life). The alignment is most explicit in Augustine, who lifts *concupiscentia oculorum*, "lust of the eyes," directly out of 1 John 2:16 (*Confessions* X.35 [confirmed]) and, in *City of God* XIV, makes concupiscence the abiding legacy of Adam's transgression [confirmed]. On this reading the Johannine list is a doctrinal compression of the Eden temptation: what Genesis narrates through the iterated verbs *ra'ah* ("saw") and *laqach* ("took") [general-knowledge], 1 John states as a taxonomy of disordered desire.

Caution is warranted, and dossier resources do not settle it. No source here demonstrates that the author of 1 John consciously exegetes Gen 3:6; because 1 John is Greek (*epithymia*) and Genesis Hebrew, the overlap is thematic, not the "shared distinctive vocabulary" that Fishbane [confirmed] treats as the signature of deliberate inner-biblical allusion. The neat one-to-one mapping — loosest at "pride of life" ↔ "make wise" — is therefore best labelled a reception-historical, typological reading, strong in Augustine and the later tradition, rather than a demonstrable authorial citation [general-knowledge].

**James 1:14-15.** James abstracts the sequence into a generative chain: a person is "lured and enticed by his own desire (*epithymia*)"; then "desire, when it has conceived, gives birth to sin, and sin, when it is fully grown, brings forth death" (wording per dossier / standard editions). The narrative grammar is here theologized into an *ordo*: enticement → desire → act (sin) → death — the arc of Genesis 2-3, where illicit desire issues in the forbidden act and the sentence of death. James converts what Wenham calls the primeval narratives' "logical development of sin" [confirmed] from story into psychology, personifying desire as mother, sin as offspring, and death as terminus. The two texts together mark the point at which the Hebrew Leitwort (Alter [confirmed]) passes into Christian moral doctrine.


---

## 7. Synthesis

### 7.1 What the pattern is

Read across the whole corpus, the *see → take* sequence is best understood not as a fixed formula but as a **grammar of the will** that Hebrew narrative can deploy in either direction. Its unmarked, everyday form is morally neutral: people constantly see and then take in the ordinary course of battle, worship, and household life (category B, 48 of the same-verse cases). What gives the pattern its charge is the **middle term**. When desire is named — or, as more often, left unnamed but obvious from the object (a wife, a beauty, a forbidden spoil) — the sequence becomes a diagnosis. Eve, the sons of God, Shechem, Achan, David: each *sees* a good, and the seeing kindles a wanting, and the wanting reaches out and *takes* what was not given. The tradition from *1 Enoch* to Augustine to the modern narrative critics reads this as the anatomy of transgression itself: the eye is the frontier across which desire crosses into deed.

### 7.2 The inversions

The same grammar can be turned. In five same-verse cases the pattern is redeemed: Shem and Japheth **take** a garment precisely in order **not to see** their father's nakedness (Gen 9:23); Abraham **sees** the ram and **takes** it as the substitute for his son (Gen 22:13); Pharaoh's daughter **sees** the ark and **takes** it to save a life (Exod 2:5); Phinehas **sees** the outrage and **takes** a spear to halt a plague (Num 25:7); Elijah **takes** the revived child and says, "**See**, your son lives" (1 Kgs 17:23). And the captive-bride law (Deut 21) shows the legislator doing to the pattern what grace does to desire — not abolishing it but disciplining it. The motif, in short, is not sin as such; it is the neutral machinery of desire that sin exploits and that righteousness can reclaim.

### 7.3 What the data does and does not show

The sweep can prove **proximity**; it cannot, by itself, prove **allusion**. That *rāʾāh* and *lāqaḥ* are two of the commonest verbs in the language means their co-occurrence is sometimes only statistical. The case that any given pairing is *intentional* rests on the criteria set out by the literary critics (§6): distinctive shared vocabulary, a matching sequence, and a thematic payoff. Those criteria are strongest exactly where the sweep also concentrates the signal — Genesis 3 and 6, Joshua 7, 2 Samuel 11 — and weakest in the visionary "lifted-my-eyes" idiom, which the data itself quarantines. No single ancient author is on record claiming that these four scenes form one designed sequence; that larger figure is a synthesis assembled by later readers from Fishbane's method of inner-biblical allusion, Wenham's and Cassuto's reading of Genesis 3→6, the David-and-Bathsheba analogists (Sternberg, Fokkelman, Kline), and the *ḥāmad*/Tenth-Commandment scholarship — and it should be held as exactly that: a well-founded synthesis, not a datum.

---

## 8. Limitations

- **Proximity ≠ intention.** See §7.3. The catalogue is a map of where the verbs meet, not a proof that every meeting is meaningful.
- **Lemma choice.** Widening or narrowing the seeing/taking sets would move the totals. The sets used are documented in §2.2 so that the study can be rerun under other definitions; the *nāśāʾ* decision in particular is flagged, not hidden.
- **Window choice.** The five-verse ceiling is a defensible but arbitrary line; broader "same-scene" links exist and are noted where they matter, but were not counted as "proximity."
- **Tier 2/3 classification.** Only the 131 same-verse pairs are individually adjudicated; the 1,167 wider pairs carry objective flags only, with the significant members treated in §5.
- **One text-tradition.** The study reflects the Leningrad Codex / MorphHB tagging; it does not collate the Samaritan Pentateuch, Qumran, or the Septuagint's Vorlage, any of which could add or remove marginal cases.

---

## Appendix A — Tier 2 (1–2 verses apart), complete

| # | Reference(s) | Seeing | Taking | Δ | Desire term in span |
|---|---|---|---|---|---|
| 1 | Genesis 2:19 → Genesis 2:21 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח וַ/יִּקַּ֗ח | 2 |  |
| 2 | Genesis 7:1 → Genesis 6:21 | ra'ah רָאָה רָאִ֛יתִי | laqach לָקַח קַח | 2 |  |
| 3 | Genesis 7:1 → Genesis 7:2 | ra'ah רָאָה רָאִ֛יתִי | laqach לָקַח תִּֽקַּח | 1 |  |
| 4 | Genesis 8:8 → Genesis 8:9 | ra'ah רָאָה לִ/רְאוֹת֙ | laqach לָקַח וַ/יִּקָּחֶ֔/הָ | 1 |  |
| 5 | Genesis 9:22 → Genesis 9:23 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּח֩ | 1 |  |
| 6 | Genesis 12:1 → Genesis 11:31 | ra'ah רָאָה אַרְאֶֽ/ךָּ | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 7 | Genesis 12:7 → Genesis 12:5 | ra'ah רָאָה וַ/יֵּרָ֤א; ra'ah רָאָה הַ/נִּרְאֶ֥ה | laqach לָקַח וַ/יִּקַּ֣ח | 2 |  |
| 8 | Genesis 12:14 → Genesis 12:15 | ra'ah רָאָה וַ/יִּרְא֤וּ | laqach לָקַח וַ/תֻּקַּ֥ח | 1 |  |
| 9 | Genesis 13:15 → Genesis 13:14 | ra'ah רָאָה רֹאֶ֖ה | nasa נָשָׂא שָׂ֣א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 10 | Genesis 16:4 → Genesis 16:3 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח וַ/תִּקַּ֞ח | 1 |  |
| 11 | Genesis 16:5 → Genesis 16:3 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח וַ/תִּקַּ֞ח | 2 |  |
| 12 | Genesis 18:1 → Genesis 18:2 | ra'ah רָאָה וַ/יֵּרָ֤א | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 13 | Genesis 18:2 → Genesis 18:4 | ra'ah רָאָה וַ/יַּ֔רְא; ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח יֻקַּֽח | 2 |  |
| 14 | Genesis 19:17 → Genesis 19:15 | nabat נָבַט תַּבִּ֣יט | laqach לָקַח קַ֨ח | 2 |  |
| 15 | Genesis 21:16 → Genesis 21:14 | ra'ah רָאָה אֶרְאֶ֖ה | laqach לָקַח וַ/יִּֽקַּֽח | 2 |  |
| 16 | Genesis 21:16 → Genesis 21:18 | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא שְׂאִ֣י | 2 |  |
| 17 | Genesis 21:19 → Genesis 21:18 | ra'ah רָאָה וַ/תֵּ֖רֶא | nasa נָשָׂא שְׂאִ֣י | 1 |  |
| 18 | Genesis 21:19 → Genesis 21:21 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/תִּֽקַּֽח | 2 |  |
| 19 | Genesis 22:4 → Genesis 22:2 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח קַח | 2 |  |
| 20 | Genesis 22:4 → Genesis 22:3 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֞ח | 1 |  |
| 21 | Genesis 22:4 → Genesis 22:6 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֨ח; laqach לָקַח וַ/יִּקַּ֣ח | 2 |  |
| 22 | Genesis 22:8 → Genesis 22:6 | ra'ah רָאָה יִרְאֶה | laqach לָקַח וַ/יִּקַּ֨ח; laqach לָקַח וַ/יִּקַּ֣ח | 2 |  |
| 23 | Genesis 22:8 → Genesis 22:10 | ra'ah רָאָה יִרְאֶה | laqach לָקַח וַ/יִּקַּ֖ח | 2 |  |
| 24 | Genesis 22:14 → Genesis 22:13 | ra'ah רָאָה יִרְאֶ֑ה; ra'ah רָאָה יֵרָאֶֽה | nasa נָשָׂא וַ/יִּשָּׂ֨א; achaz אָחַז נֶאֱחַ֥ז; laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 25 | Genesis 24:63 → Genesis 24:61 | ra'ah רָאָה וַ/יַּ֔רְא | laqach לָקַח וַ/יִּקַּ֥ח | 2 |  |
| 26 | Genesis 24:64 → Genesis 24:63 | ra'ah רָאָה וַ/תֵּ֖רֶא | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 27 | Genesis 24:63 → Genesis 24:64 | ra'ah רָאָה וַ/יַּ֔רְא | nasa נָשָׂא וַ/תִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 28 | Genesis 24:63 → Genesis 24:65 | ra'ah רָאָה וַ/יַּ֔רְא | laqach לָקַח וַ/תִּקַּ֥ח | 2 |  |
| 29 | Genesis 24:64 → Genesis 24:65 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/תִּקַּ֥ח | 1 |  |
| 30 | Genesis 27:1 → Genesis 26:34 | ra'ah רָאָה מֵ/רְאֹ֑ת | laqach לָקַח וַ/יִּקַּ֤ח | 2 |  |
| 31 | Genesis 27:1 → Genesis 27:3 | ra'ah רָאָה מֵ/רְאֹ֑ת | nasa נָשָׂא שָׂא | 2 |  |
| 32 | Genesis 28:8 → Genesis 28:6 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח לָ/קַֽחַת; laqach לָקַח תִקַּ֥ח | 2 |  |
| 33 | Genesis 28:8 → Genesis 28:9 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֡ח | 1 |  |
| 34 | Genesis 29:2 → Genesis 29:1 | ra'ah רָאָה וַ/יַּ֞רְא | nasa נָשָׂא וַ/יִּשָּׂ֥א | 1 |  |
| 35 | Genesis 29:10 → Genesis 29:11 | ra'ah רָאָה רָאָ֨ה | nasa נָשָׂא וַ/יִּשָּׂ֥א | 1 |  |
| 36 | Genesis 31:2 → Genesis 31:1 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח לָקַ֣ח | 1 |  |
| 37 | Genesis 31:12 → Genesis 31:10 | ra'ah רָאָה וּ/רְאֵה֙; ra'ah רָאָה רָאִ֔יתִי | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 38 | Genesis 31:10 → Genesis 31:12 | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא שָׂא _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 39 | Genesis 31:43 → Genesis 31:45 | ra'ah רָאָה רֹאֶ֖ה | laqach לָקַח וַ/יִּקַּ֥ח | 2 |  |
| 40 | Genesis 31:49 → Genesis 31:50 | tsaphah צָפָה יִ֥צֶף | laqach לָקַח תִּקַּ֤ח | 1 |  |
| 41 | Genesis 32:21 → Genesis 32:23 | ra'ah רָאָה אֶרְאֶ֣ה | laqach לָקַח וַ/יִּקַּ֞ח | 2 |  |
| 42 | Genesis 32:26 → Genesis 32:24 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקָּחֵ֔/ם | 2 |  |
| 43 | Genesis 33:10 → Genesis 33:11 | ra'ah רָאָה רָאִ֣יתִי; ra'ah רָאָה כִּ/רְאֹ֛ת | laqach לָקַח קַח; laqach לָקַח וַ/יִּקָּֽח | 1 |  |
| 44 | Genesis 34:1 → Genesis 34:2 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח וַ/יִּקַּ֥ח | 1 |  |
| 45 | Genesis 34:2 → Genesis 34:4 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח קַֽח | 2 |  |
| 46 | Genesis 37:25 → Genesis 37:24 | ra'ah רָאָה וַ/יִּרְא֔וּ | laqach לָקַח וַ/יִּ֨קָּחֻ֔/הוּ | 1 |  |
| 47 | Genesis 39:13 → Genesis 39:12 | ra'ah רָאָה כִּ/רְאוֹתָ֔/הּ | taphas תָּפַשׂ וַ/תִּתְפְּשֵׂ֧/הוּ | 1 |  |
| 48 | Genesis 39:14 → Genesis 39:12 | ra'ah רָאָה רְא֗וּ | taphas תָּפַשׂ וַ/תִּתְפְּשֵׂ֧/הוּ | 2 |  |
| 49 | Genesis 42:27 → Genesis 42:26 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 1 |  |
| 50 | Genesis 42:35 → Genesis 42:33 | ra'ah רָאָה וַ/יִּרְא֞וּ | laqach לָקַח קְח֥וּ | 2 |  |
| 51 | Genesis 42:35 → Genesis 42:36 | ra'ah רָאָה וַ/יִּרְא֞וּ | laqach לָקַח תִּקָּ֔חוּ | 1 |  |
| 52 | Genesis 43:16 → Genesis 43:15 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח וַ/יִּקְח֤וּ; laqach לָקַח לָקְח֥וּ | 1 |  |
| 53 | Genesis 43:16 → Genesis 43:18 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח וְ/לָ/קַ֧חַת | 2 |  |
| 54 | Genesis 44:28 → Genesis 44:29 | ra'ah רָאָה רְאִיתִ֖י/ו | laqach לָקַח וּ/לְקַחְתֶּ֧ם | 1 |  |
| 55 | Genesis 44:31 → Genesis 44:29 | ra'ah רָאָה כִּ/רְאוֹת֛/וֹ | laqach לָקַח וּ/לְקַחְתֶּ֧ם | 2 |  |
| 56 | Genesis 45:28 → Genesis 45:27 | ra'ah רָאָה וְ/אֶרְאֶ֖/נּוּ | nasa נָשָׂא לָ/שֵׂ֣את | 1 |  |
| 57 | Genesis 48:3 → Genesis 48:1 | ra'ah רָאָה נִרְאָֽה | laqach לָקַח וַ/יִּקַּ֞ח | 2 |  |
| 58 | Genesis 48:8 → Genesis 48:9 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח קָֽחֶ/ם | 1 |  |
| 59 | Genesis 48:10 → Genesis 48:9 | ra'ah רָאָה לִ/רְא֑וֹת | laqach לָקַח קָֽחֶ/ם | 1 |  |
| 60 | Genesis 48:11 → Genesis 48:9 | ra'ah רָאָה רְאֹ֥ה; ra'ah רָאָה הֶרְאָ֥ה | laqach לָקַח קָֽחֶ/ם | 2 |  |
| 61 | Genesis 48:11 → Genesis 48:13 | ra'ah רָאָה רְאֹ֥ה; ra'ah רָאָה הֶרְאָ֥ה | laqach לָקַח וַ/יִּקַּ֣ח | 2 |  |
| 62 | Genesis 50:11 → Genesis 50:13 | ra'ah רָאָה וַ/יַּ֡רְא | nasa נָשָׂא וַ/יִּשְׂא֨וּ | 2 |  |
| 63 | Genesis 50:15 → Genesis 50:13 | ra'ah רָאָה וַ/יִּרְא֤וּ | nasa נָשָׂא וַ/יִּשְׂא֨וּ | 2 |  |
| 64 | Genesis 50:15 → Genesis 50:17 | ra'ah רָאָה וַ/יִּרְא֤וּ | nasa נָשָׂא שָׂ֣א; nasa נָשָׂא שָׂ֣א | 2 |  |
| 65 | Exodus 2:2 → Exodus 2:1 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/יִּקַּ֖ח | 1 |  |
| 66 | Exodus 2:2 → Exodus 2:3 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּֽקַּֽח | 1 |  |
| 67 | Exodus 2:5 → Exodus 2:3 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּֽקַּֽח | 2 |  |
| 68 | Exodus 2:6 → Exodus 2:5 | ra'ah רָאָה וַ/תִּרְאֵ֣/הוּ | laqach לָקַח וַ/תִּקָּחֶֽ/הָ | 1 |  |
| 69 | Exodus 2:11 → Exodus 2:9 | ra'ah רָאָה וַ/יַּ֖רְא; ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/תִּקַּ֧ח | 2 |  |
| 70 | Exodus 4:5 → Exodus 4:4 | ra'ah רָאָה נִרְאָ֥ה | achaz אָחַז וֶ/אֱחֹ֖ז | 1 |  |
| 71 | Exodus 4:18 → Exodus 4:17 | ra'ah רָאָה וְ/אֶרְאֶ֖ה | laqach לָקַח תִּקַּ֣ח | 1 |  |
| 72 | Exodus 4:18 → Exodus 4:20 | ra'ah רָאָה וְ/אֶרְאֶ֖ה | laqach לָקַח וַ/יִּקַּ֨ח; laqach לָקַח וַ/יִּקַּ֥ח | 2 |  |
| 73 | Exodus 4:21 → Exodus 4:20 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וַ/יִּקַּ֨ח; laqach לָקַח וַ/יִּקַּ֥ח | 1 |  |
| 74 | Exodus 5:9 → Exodus 5:11 | sha'ah שָׁעָה יִשְׁע֖וּ | laqach לָקַח קְח֤וּ | 2 |  |
| 75 | Exodus 10:28 → Exodus 10:26 | ra'ah רָאָה רְא֣וֹת; ra'ah רָאָה רְאֹתְ/ךָ֥ | laqach לָקַח נִקַּ֔ח | 2 |  |
| 76 | Exodus 12:23 → Exodus 12:21 | ra'ah רָאָה וְ/רָאָ֤ה | laqach לָקַח וּ/קְח֨וּ | 2 |  |
| 77 | Exodus 12:23 → Exodus 12:22 | ra'ah רָאָה וְ/רָאָ֤ה | laqach לָקַח וּ/לְקַחְתֶּ֞ם | 1 |  |
| 78 | Exodus 13:17 → Exodus 13:19 | ra'ah רָאָה בִּ/רְאֹתָ֥/ם | laqach לָקַח וַ/יִּקַּ֥ח | 2 |  |
| 79 | Exodus 14:13 → Exodus 14:11 | ra'ah רָאָה וּ/רְאוּ֙; ra'ah רָאָה רְאִיתֶ֤ם; ra'ah רָאָה לִ/רְאֹתָ֥/ם | laqach לָקַח לְקַחְתָּ֖/נוּ | 2 |  |
| 80 | Exodus 16:15 → Exodus 16:16 | ra'ah רָאָה וַ/יִּרְא֣וּ | laqach לָקַח תִּקָּֽחוּ | 1 |  |
| 81 | Exodus 16:32 → Exodus 16:33 | ra'ah רָאָה יִרְא֣וּ | laqach לָקַח קַ֚ח | 1 |  |
| 82 | Exodus 18:14 → Exodus 18:12 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּ֞ח | 2 |  |
| 83 | Exodus 18:21 → Exodus 18:22 | chazah חָזָה תֶחֱזֶ֣ה | nasa נָשָׂא וְ/נָשְׂא֖וּ | 1 |  |
| 84 | Exodus 22:9 → Exodus 22:10 | ra'ah רָאָה רֹאֶֽה | laqach לָקַח וְ/לָקַ֥ח | 1 |  |
| 85 | Exodus 24:10 → Exodus 24:8 | ra'ah רָאָה וַ/יִּרְא֕וּ | laqach לָקַח וַ/יִּקַּ֤ח | 2 |  |
| 86 | Exodus 27:8 → Exodus 27:7 | ra'ah רָאָה הֶרְאָ֥ה | nasa נָשָׂא בִּ/שְׂאֵ֥ת | 1 |  |
| 87 | Exodus 32:5 → Exodus 32:4 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 88 | Exodus 32:19 → Exodus 32:20 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֞ח | 1 |  |
| 89 | Exodus 33:8 → Exodus 33:7 | nabat נָבַט וְ/הִבִּ֨יטוּ֙ | laqach לָקַח יִקַּ֨ח | 1 |  |
| 90 | Exodus 34:3 → Exodus 34:4 | ra'ah רָאָה יֵרָ֖א | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 91 | Leviticus 5:1 → Leviticus 4:34 | ra'ah רָאָה רָאָ֖ה | laqach לָקַח וְ/לָקַ֨ח | 2 |  |
| 92 | Leviticus 9:4 → Leviticus 9:2 | ra'ah רָאָה נִרְאָ֥ה | laqach לָקַח קַח | 2 |  |
| 93 | Leviticus 9:4 → Leviticus 9:3 | ra'ah רָאָה נִרְאָ֥ה | laqach לָקַח קְח֤וּ | 1 |  |
| 94 | Leviticus 9:4 → Leviticus 9:5 | ra'ah רָאָה נִרְאָ֥ה | laqach לָקַח וַ/יִּקְח֗וּ | 1 |  |
| 95 | Leviticus 9:6 → Leviticus 9:5 | ra'ah רָאָה וְ/יֵרָ֥א | laqach לָקַח וַ/יִּקְח֗וּ | 1 |  |
| 96 | Leviticus 9:23 → Leviticus 9:22 | ra'ah רָאָה וַ/יֵּרָ֥א | nasa נָשָׂא וַ/יִּשָּׂ֨א | 1 |  |
| 97 | Leviticus 9:24 → Leviticus 9:22 | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א | 2 |  |
| 98 | Leviticus 9:23 → Leviticus 10:1 | ra'ah רָאָה וַ/יֵּרָ֥א | laqach לָקַח וַ/יִּקְח֣וּ | 2 |  |
| 99 | Leviticus 9:24 → Leviticus 10:1 | ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח וַ/יִּקְח֣וּ | 1 |  |
| 100 | Leviticus 14:3 → Leviticus 14:4 | ra'ah רָאָה וְ/רָאָה֙ | laqach לָקַח וְ/לָקַ֧ח | 1 |  |
| 101 | Leviticus 14:44 → Leviticus 14:42 | ra'ah רָאָה וְ/רָאָ֕ה | laqach לָקַח וְ/לָקְחוּ֙; laqach לָקַח יִקַּ֖ח | 2 |  |
| 102 | Leviticus 14:48 → Leviticus 14:49 | ra'ah רָאָה וְ/רָאָה֙ | laqach לָקַח וְ/לָקַ֛ח | 1 |  |
| 103 | Leviticus 20:17 → Leviticus 20:19 | ra'ah רָאָה וְ/רָאָ֨ה; ra'ah רָאָה תִרְאֶ֤ה | nasa נָשָׂא יִשָּֽׂאוּ | 2 |  |
| 104 | Numbers 4:20 → Numbers 4:22 | ra'ah רָאָה לִ/רְא֛וֹת | nasa נָשָׂא נָשֹׂ֗א | 2 |  |
| 105 | Numbers 8:4 → Numbers 8:6 | ra'ah רָאָה הֶרְאָ֤ה | laqach לָקַח קַ֚ח | 2 |  |
| 106 | Numbers 11:15 → Numbers 11:14 | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא לָ/שֵׂ֖את | 1 |  |
| 107 | Numbers 11:15 → Numbers 11:16 | ra'ah רָאָה אֶרְאֶ֖ה | laqach לָקַח וְ/לָקַחְתָּ֤ | 1 |  |
| 108 | Numbers 11:15 → Numbers 11:17 | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא וְ/נָשְׂא֤וּ; nasa נָשָׂא תִשָּׂ֥א | 2 |  |
| 109 | Numbers 13:18 → Numbers 13:20 | ra'ah רָאָה וּ/רְאִיתֶ֥ם | laqach לָקַח וּ/לְקַחְתֶּ֖ם | 2 |  |
| 110 | Numbers 13:32 → Numbers 14:1 | ra'ah רָאָה רָאִ֥ינוּ | nasa נָשָׂא וַ/תִּשָּׂא֙ | 2 |  |
| 111 | Numbers 13:33 → Numbers 14:1 | ra'ah רָאָה רָאִ֗ינוּ | nasa נָשָׂא וַ/תִּשָּׂא֙ | 1 |  |
| 112 | Numbers 16:19 → Numbers 16:17 | ra'ah רָאָה וַ/יֵּרָ֥א | laqach לָקַח וּ/קְח֣וּ | 2 |  |
| 113 | Numbers 16:19 → Numbers 16:18 | ra'ah רָאָה וַ/יֵּרָ֥א | laqach לָקַח וַ/יִּקְח֞וּ | 1 |  |
| 114 | Numbers 20:6 → Numbers 20:8 | ra'ah רָאָה וַ/יֵּרָ֥א | laqach לָקַח קַ֣ח | 2 |  |
| 115 | Numbers 23:9 → Numbers 23:7 | ra'ah רָאָה אֶרְאֶ֔/נּוּ; shur שׁוּר אֲשׁוּרֶ֑/נּוּ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 2 |  |
| 116 | Numbers 23:9 → Numbers 23:11 | ra'ah רָאָה אֶרְאֶ֔/נּוּ; shur שׁוּר אֲשׁוּרֶ֑/נּוּ | laqach לָקַח לְקַחְתִּ֔י/ךָ | 2 |  |
| 117 | Numbers 23:13 → Numbers 23:11 | ra'ah רָאָה תִּרְאֶ֣/נּוּ; ra'ah רָאָה תִרְאֶ֔ה; ra'ah רָאָה תִרְאֶ֑ה | laqach לָקַח לְקַחְתִּ֔י/ךָ | 2 |  |
| 118 | Numbers 23:13 → Numbers 23:14 | ra'ah רָאָה תִּרְאֶ֣/נּוּ; ra'ah רָאָה תִרְאֶ֔ה; ra'ah רָאָה תִרְאֶ֑ה | laqach לָקַח וַ/יִּקָּחֵ֨/הוּ֙ | 1 |  |
| 119 | Numbers 23:21 → Numbers 23:20 | nabat נָבַט הִבִּ֥יט; ra'ah רָאָה רָאָ֥ה | laqach לָקַח לָקָ֑חְתִּי | 1 |  |
| 120 | Numbers 23:28 → Numbers 23:27 | shaqaph שָׁקַף הַ/נִּשְׁקָ֖ף | laqach לָקַח אֶקָּ֣חֲ/ךָ֔ | 1 |  |
| 121 | Numbers 24:1 → Numbers 24:2 | ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 122 | Numbers 24:1 → Numbers 24:3 | ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 123 | Numbers 24:4 → Numbers 24:2 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 124 | Numbers 24:2 → Numbers 24:3 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 125 | Numbers 24:4 → Numbers 24:3 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 126 | Numbers 24:16 → Numbers 24:15 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 127 | Numbers 24:17 → Numbers 24:15 | ra'ah רָאָה אֶרְאֶ֨/נּוּ֙; shur שׁוּר אֲשׁוּרֶ֖/נּוּ | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 128 | Numbers 24:21 → Numbers 24:20 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 1 |  |
| 129 | Numbers 24:20 → Numbers 24:21 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 1 |  |
| 130 | Numbers 24:21 → Numbers 24:23 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 2 |  |
| 131 | Numbers 32:1 → Numbers 31:54 | ra'ah רָאָה וַ/יִּרְא֞וּ | laqach לָקַח וַ/יִּקַּ֨ח | 1 |  |
| 132 | Deuteronomy 1:8 → Deuteronomy 1:9 | ra'ah רָאָה רְאֵ֛ה | nasa נָשָׂא שְׂאֵ֥ת | 1 |  |
| 133 | Deuteronomy 1:21 → Deuteronomy 1:23 | ra'ah רָאָה רְ֠אֵה | laqach לָקַח וָ/אֶקַּ֤ח | 2 |  |
| 134 | Deuteronomy 1:33 → Deuteronomy 1:31 | ra'ah רָאָה לַ/רְאֹֽתְ/כֶם֙ | nasa נָשָׂא נְשָׂאֲ/ךָ֙; nasa נָשָׂא יִשָּׂא | 2 |  |
| 135 | Deuteronomy 3:25 → Deuteronomy 3:27 | ra'ah רָאָה וְ/אֶרְאֶה֙ | nasa נָשָׂא וְ/שָׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 136 | Deuteronomy 3:28 → Deuteronomy 3:27 | ra'ah רָאָה תִּרְאֶֽה | nasa נָשָׂא וְ/שָׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 137 | Deuteronomy 4:19 → Deuteronomy 4:20 | ra'ah רָאָה וְֽ֠/רָאִיתָ | laqach לָקַח לָקַ֣ח | 1 |  |
| 138 | Deuteronomy 4:35 → Deuteronomy 4:34 | ra'ah רָאָה הָרְאֵ֣תָ | laqach לָקַח לָ/קַ֨חַת | 1 |  |
| 139 | Deuteronomy 4:36 → Deuteronomy 4:34 | ra'ah רָאָה הֶרְאֲ/ךָ֙ | laqach לָקַח לָ/קַ֨חַת | 2 |  |
| 140 | Deuteronomy 9:16 → Deuteronomy 9:17 | ra'ah רָאָה וָ/אֵ֗רֶא | taphas תָּפַשׂ וָ/אֶתְפֹּשׂ֙ | 1 |  |
| 141 | Deuteronomy 22:4 → Deuteronomy 22:6 | ra'ah רָאָה תִרְאֶה֩ | laqach לָקַח תִקַּ֥ח | 2 |  |
| 142 | Deuteronomy 28:32 → Deuteronomy 28:31 | ra'ah רָאָה רֹא֔וֹת | gazal גָּזַל גָּז֣וּל | 1 |  |
| 143 | Deuteronomy 30:15 → Deuteronomy 30:13 | ra'ah רָאָה רְאֵ֨ה | laqach לָקַח וְ/יִקָּחֶ֣/הָ | 2 |  |
| 144 | Deuteronomy 31:11 → Deuteronomy 31:9 | ra'ah רָאָה לֵ/רָאוֹת֙ | nasa נָשָׂא הַ/נֹּ֣שְׂאִ֔ים | 2 |  |
| 145 | Deuteronomy 32:39 → Deuteronomy 32:40 | ra'ah רָאָה רְא֣וּ | nasa נָשָׂא אֶשָּׂ֥א | 1 |  |
| 146 | Deuteronomy 32:39 → Deuteronomy 32:41 | ra'ah רָאָה רְא֣וּ | achaz אָחַז וְ/תֹאחֵ֥ז | 2 |  |
| 147 | Joshua 6:2 → Joshua 6:4 | ra'ah רָאָה רְאֵה֙ | nasa נָשָׂא יִשְׂאוּ֩ | 2 |  |
| 148 | Joshua 7:21 → Joshua 7:23 | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | laqach לָקַח וַ/יִּקָּחוּ/ם֙ | 2 | chamad חָמַד (Joshua 7:21) |
| 149 | Joshua 8:14 → Joshua 8:12 | ra'ah רָאָה כִּ/רְא֣וֹת | laqach לָקַח וַ/יִּקַּ֕ח | 2 |  |
| 150 | Joshua 8:20 → Joshua 8:19 | ra'ah רָאָה וַ/יִּרְא֗וּ | lakad לָכַד וַֽ/יִּלְכְּד֑וּ/הָ | 1 |  |
| 151 | Joshua 8:21 → Joshua 8:19 | ra'ah רָאָה רָא֗וּ | lakad לָכַד וַֽ/יִּלְכְּד֑וּ/הָ | 2 |  |
| 152 | Joshua 8:20 → Joshua 8:21 | ra'ah רָאָה וַ/יִּרְא֗וּ | lakad לָכַד לָכַ֤ד | 1 |  |
| 153 | Joshua 8:21 → Joshua 8:23 | ra'ah רָאָה רָא֗וּ | taphas תָּפַשׂ תָּ֣פְשׂוּ | 2 |  |
| 154 | Judges 3:24 → Judges 3:25 | ra'ah רָאָה וַ/יִּרְא֕וּ | laqach לָקַח וַ/יִּקְח֤וּ | 1 |  |
| 155 | Judges 4:22 → Judges 4:21 | ra'ah רָאָה וְ/אַרְאֶ֔/ךָּ | laqach לָקַח וַ/תִּקַּ֣ח | 1 |  |
| 156 | Judges 6:22 → Judges 6:20 | ra'ah רָאָה וַ/יַּ֣רְא; ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח קַ֣ח | 2 |  |
| 157 | Judges 9:43 → Judges 9:45 | ra'ah רָאָה וַ/יַּ֗רְא | lakad לָכַד וַ/יִּלְכֹּד֙ | 2 |  |
| 158 | Judges 9:48 → Judges 9:50 | ra'ah רָאָה רְאִיתֶם֙ | lakad לָכַד וַֽ/יִּלְכְּדָֽ/הּ | 2 |  |
| 159 | Judges 9:55 → Judges 9:54 | ra'ah רָאָה וַ/יִּרְא֥וּ | nasa נָשָׂא נֹשֵׂ֣א | 1 |  |
| 160 | Judges 12:3 → Judges 12:5 | ra'ah רָאָה וָֽ/אֶרְאֶ֞ה | lakad לָכַד וַ/יִּלְכֹּ֥ד | 2 |  |
| 161 | Judges 13:20 → Judges 13:19 | ra'ah רָאָה רֹאִ֔ים | laqach לָקַח וַ/יִּקַּ֨ח | 1 |  |
| 162 | Judges 13:21 → Judges 13:19 | ra'ah רָאָה לְ/הֵרָאֹ֖ה | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 163 | Judges 13:21 → Judges 13:23 | ra'ah רָאָה לְ/הֵרָאֹ֖ה | laqach לָקַח לָקַ֤ח | 2 |  |
| 164 | Judges 13:22 → Judges 13:23 | ra'ah רָאָה רָאִֽינוּ | laqach לָקַח לָקַ֤ח | 1 |  |
| 165 | Judges 14:1 → Judges 14:2 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח קְחוּ | 1 |  |
| 166 | Judges 14:1 → Judges 14:3 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח לָ/קַ֣חַת; laqach לָקַח קַֽח | 2 |  |
| 167 | Judges 14:2 → Judges 14:3 | ra'ah רָאָה רָאִ֥יתִי | laqach לָקַח לָ/קַ֣חַת; laqach לָקַח קַֽח | 1 |  |
| 168 | Judges 16:1 → Judges 16:3 | ra'ah רָאָה וַ/יַּרְא | achaz אָחַז וַ/יֶּאֱחֹ֞ז | 2 |  |
| 169 | Judges 16:5 → Judges 16:3 | ra'ah רָאָה וּ/רְאִי֙ | achaz אָחַז וַ/יֶּאֱחֹ֞ז | 2 |  |
| 170 | Judges 18:26 → Judges 18:24 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח לְקַחְתֶּ֧ם | 2 |  |
| 171 | Judges 18:26 → Judges 18:27 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח לָקְח֜וּ | 1 |  |
| 172 | Judges 19:3 → Judges 19:1 | ra'ah רָאָה וַ/יִּרְאֵ֨/הוּ֙ | laqach לָקַח וַ/יִּֽקַּֽח | 2 |  |
| 173 | Judges 19:30 → Judges 19:28 | ra'ah רָאָה הָ/רֹאֶ֗ה; ra'ah רָאָה נִרְאֲתָה֙ | laqach לָקַח וַ/יִּקָּחֶ֨/הָ֙ | 2 |  |
| 174 | Judges 19:30 → Judges 19:29 | ra'ah רָאָה הָ/רֹאֶ֗ה; ra'ah רָאָה נִרְאֲתָה֙ | laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 175 | Judges 21:21 → Judges 21:22 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | laqach לָקַח לָקַ֛חְנוּ | 1 |  |
| 176 | Judges 21:21 → Judges 21:23 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | nasa נָשָׂא וַ/יִּשְׂא֤וּ; gazal גָּזַל גָּזָ֑לוּ | 2 |  |
| 177 | 1 Samuel 4:13 → 1 Samuel 4:11 | tsaphah צָפָה מְצַפֶּ֔ה | laqach לָקַח נִלְקָ֑ח | 2 |  |
| 178 | 1 Samuel 4:15 → 1 Samuel 4:17 | ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח נִלְקָֽחָה | 2 |  |
| 179 | 1 Samuel 6:9 → 1 Samuel 6:7 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | laqach לָקַח קְח֨וּ | 2 |  |
| 180 | 1 Samuel 6:9 → 1 Samuel 6:8 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | laqach לָקַח וּ/לְקַחְתֶּ֞ם | 1 |  |
| 181 | 1 Samuel 6:9 → 1 Samuel 6:10 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | laqach לָקַח וַ/יִּקְח֗וּ | 1 |  |
| 182 | 1 Samuel 10:24 → 1 Samuel 10:23 | ra'ah רָאָה הַ/רְּאִיתֶם֙ | laqach לָקַח וַ/יִּקָּחֻ֣/הוּ | 1 |  |
| 183 | 1 Samuel 14:16 → 1 Samuel 14:14 | ra'ah רָאָה וַ/יִּרְא֤וּ; tsaphah צָפָה הַ/צֹּפִים֙ | nasa נָשָׂא וְ/נֹשֵׂ֥א | 2 |  |
| 184 | 1 Samuel 14:16 → 1 Samuel 14:17 | ra'ah רָאָה וַ/יִּרְא֤וּ; tsaphah צָפָה הַ/צֹּפִים֙ | nasa נָשָׂא וְ/נֹשֵׂ֥א | 1 |  |
| 185 | 1 Samuel 15:35 → 1 Samuel 16:2 | ra'ah רָאָה לִ/רְא֤וֹת | laqach לָקַח תִּקַּ֣ח | 2 |  |
| 186 | 1 Samuel 16:1 → 1 Samuel 16:2 | ra'ah רָאָה רָאִ֧יתִי | laqach לָקַח תִּקַּ֣ח | 1 |  |
| 187 | 1 Samuel 16:18 → 1 Samuel 16:20 | ra'ah רָאָה רָאִ֜יתִי | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 188 | 1 Samuel 17:42 → 1 Samuel 17:40 | nabat נָבַט וַ/יַּבֵּ֧ט; ra'ah רָאָה וַ/יִּרְאֶ֥ה | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 189 | 1 Samuel 17:42 → 1 Samuel 17:41 | nabat נָבַט וַ/יַּבֵּ֧ט; ra'ah רָאָה וַ/יִּרְאֶ֥ה | nasa נָשָׂא נֹשֵׂ֥א | 1 |  |
| 190 | 1 Samuel 17:51 → 1 Samuel 17:49 | ra'ah רָאָה וַ/יִּרְא֧וּ | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 191 | 1 Samuel 17:55 → 1 Samuel 17:54 | ra'ah רָאָה וְ/כִ/רְא֨וֹת | laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 192 | 1 Samuel 17:55 → 1 Samuel 17:57 | ra'ah רָאָה וְ/כִ/רְא֨וֹת | laqach לָקַח וַ/יִּקַּ֤ח | 2 |  |
| 193 | 1 Samuel 19:15 → 1 Samuel 19:13 | ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח וַ/תִּקַּ֨ח | 2 |  |
| 194 | 1 Samuel 19:15 → 1 Samuel 19:14 | ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח לָ/קַ֣חַת | 1 |  |
| 195 | 1 Samuel 20:29 → 1 Samuel 20:31 | ra'ah רָאָה וְ/אֶרְאֶ֣ה | laqach לָקַח וְ/קַ֤ח | 2 |  |
| 196 | 1 Samuel 24:11 → 1 Samuel 24:12 | ra'ah רָאָה רָא֣וּ | laqach לָקַח לְ/קַחְתָּֽ/הּ | 1 |  |
| 197 | 1 Samuel 24:16 → 1 Samuel 24:17 | ra'ah רָאָה וְ/יֵ֨רֶא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 1 |  |
| 198 | 1 Samuel 25:17 → 1 Samuel 25:18 | ra'ah רָאָה וּ/רְאִי֙ | laqach לָקַח וַ/תִּקַּח֩ | 1 |  |
| 199 | 1 Samuel 26:12 → 1 Samuel 26:11 | ra'ah רָאָה רֹאֶה֩ | laqach לָקַח קַח | 1 |  |
| 200 | 1 Samuel 31:5 → 1 Samuel 31:4 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא לְ/נֹשֵׂ֨א; nasa נָשָׂא נֹשֵׂ֣א; laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 201 | 1 Samuel 31:7 → 1 Samuel 31:5 | ra'ah רָאָה וַ/יִּרְא֣וּ | nasa נָשָׂא נֹשֵֽׂא | 2 |  |
| 202 | 1 Samuel 31:5 → 1 Samuel 31:6 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא וְ/נֹשֵׂ֨א | 1 |  |
| 203 | 1 Samuel 31:7 → 1 Samuel 31:6 | ra'ah רָאָה וַ/יִּרְא֣וּ | nasa נָשָׂא וְ/נֹשֵׂ֨א | 1 |  |
| 204 | 2 Samuel 1:7 → 2 Samuel 1:9 | ra'ah רָאָה וַ/יִּרְאֵ֑/נִי | achaz אָחַז אֲחָזַ֖/נִי | 2 |  |
| 205 | 2 Samuel 3:13 → 2 Samuel 3:15 | ra'ah רָאָה תִרְאֶ֣ה; ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח וַ/יִּקָּחֶ֖/הָ | 2 |  |
| 206 | 2 Samuel 10:6 → 2 Samuel 10:4 | ra'ah רָאָה וַ/יִּרְאוּ֙ | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 207 | 2 Samuel 11:2 → 2 Samuel 11:4 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקָּחֶ֗/הָ | 2 |  |
| 208 | 2 Samuel 13:6 → 2 Samuel 13:8 | ra'ah רָאָה לִ/רְאֹת֗/וֹ | laqach לָקַח וַ/תִּקַּ֨ח | 2 |  |
| 209 | 2 Samuel 13:34 → 2 Samuel 13:36 | tsaphah צָפָה הַ/צֹּפֶה֙; ra'ah רָאָה וַ/יַּ֗רְא | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 2 |  |
| 210 | 2 Samuel 15:25 → 2 Samuel 15:24 | ra'ah רָאָה וְ/הִרְאַ֥/נִי | nasa נָשָׂא נֹֽשְׂאִים֙ | 1 |  |
| 211 | 2 Samuel 17:17 → 2 Samuel 17:19 | ra'ah רָאָה לְ/הֵרָא֖וֹת | laqach לָקַח וַ/תִּקַּ֣ח | 2 |  |
| 212 | 2 Samuel 17:18 → 2 Samuel 17:19 | ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח וַ/תִּקַּ֣ח | 1 |  |
| 213 | 2 Samuel 18:25 → 2 Samuel 18:24 | tsaphah צָפָה הַ/צֹּפֶה֙ | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 214 | 2 Samuel 18:26 → 2 Samuel 18:24 | ra'ah רָאָה וַ/יַּ֣רְא; tsaphah צָפָה הַ/צֹּפֶה֮; tsaphah צָפָה הַ/צֹּפֶה֙ | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 215 | 2 Samuel 18:26 → 2 Samuel 18:28 | ra'ah רָאָה וַ/יַּ֣רְא; tsaphah צָפָה הַ/צֹּפֶה֮; tsaphah צָפָה הַ/צֹּפֶה֙ | nasa נָשָׂא נָשְׂא֥וּ | 2 |  |
| 216 | 2 Samuel 18:27 → 2 Samuel 18:28 | tsaphah צָפָה הַ/צֹּפֶ֔ה; ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא נָשְׂא֥וּ | 1 |  |
| 217 | 2 Samuel 18:29 → 2 Samuel 18:28 | ra'ah רָאָה רָאִיתִי֩ | nasa נָשָׂא נָשְׂא֥וּ | 1 |  |
| 218 | 2 Samuel 22:16 → 2 Samuel 22:17 | ra'ah רָאָה וַ/יֵּֽרָאוּ֙ | laqach לָקַח יִקָּחֵ֑/נִי | 1 |  |
| 219 | 2 Samuel 24:20 → 2 Samuel 24:22 | shaqaph שָׁקַף וַ/יַּשְׁקֵ֣ף; ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח יִקַּ֥ח | 2 |  |
| 220 | 1 Kings 9:12 → 1 Kings 9:11 | ra'ah רָאָה לִ/רְאוֹת֙ | nasa נָשָׂא נִשָּׂ֨א | 1 |  |
| 221 | 1 Kings 10:4 → 1 Kings 10:2 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | nasa נָשָׂא נֹשְׂאִ֨ים | 2 |  |
| 222 | 1 Kings 10:12 → 1 Kings 10:11 | ra'ah רָאָה נִרְאָ֔ה | nasa נָשָׂא נָשָׂ֥א | 1 |  |
| 223 | 1 Kings 11:28 → 1 Kings 11:30 | ra'ah רָאָה וַ/יַּ֨רְא | taphas תָּפַשׂ וַ/יִּתְפֹּ֣שׂ | 2 |  |
| 224 | 1 Kings 14:4 → 1 Kings 14:3 | ra'ah רָאָה לִ/רְא֔וֹת | laqach לָקַח וְ/לָקַ֣חַתְּ | 1 |  |
| 225 | 1 Kings 18:1 → 1 Kings 17:23 | ra'ah רָאָה הֵרָאֵ֣ה | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 226 | 1 Kings 18:2 → 1 Kings 18:4 | ra'ah רָאָה לְ/הֵרָא֖וֹת | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 227 | 1 Kings 18:39 → 1 Kings 18:40 | ra'ah רָאָה וַ/יַּרְא֙ | taphas תָּפַשׂ תִּפְשׂ֣וּ; taphas תָּפַשׂ וַֽ/יִּתְפְּשׂ֑וּ/ם | 1 |  |
| 228 | 1 Kings 19:3 → 1 Kings 19:4 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח קַ֣ח | 1 |  |
| 229 | 1 Kings 19:6 → 1 Kings 19:4 | nabat נָבַט וַ/יַּבֵּ֕ט | laqach לָקַח קַ֣ח | 2 |  |
| 230 | 1 Kings 20:7 → 1 Kings 20:6 | ra'ah רָאָה וּ/רְא֔וּ | laqach לָקַח וְ/לָקָֽחוּ | 1 |  |
| 231 | 1 Kings 22:25 → 1 Kings 22:26 | ra'ah רָאָה רֹאֶ֖ה | laqach לָקַח קַ֚ח | 1 |  |
| 232 | 2 Kings 2:10 → 2 Kings 2:8 | ra'ah רָאָה תִּרְאֶ֨ה | laqach לָקַח וַ/יִּקַּח֩ | 2 |  |
| 233 | 2 Kings 2:10 → 2 Kings 2:9 | ra'ah רָאָה תִּרְאֶ֨ה | laqach לָקַח אֶלָּקַ֣ח | 1 |  |
| 234 | 2 Kings 2:12 → 2 Kings 2:10 | ra'ah רָאָה רֹאֶ֗ה; ra'ah רָאָה רָאָ֖/הוּ | laqach לָקַח לֻקָּ֤ח | 2 |  |
| 235 | 2 Kings 2:12 → 2 Kings 2:14 | ra'ah רָאָה רֹאֶ֗ה; ra'ah רָאָה רָאָ֖/הוּ | laqach לָקַח וַ/יִּקַּח֩ | 2 |  |
| 236 | 2 Kings 2:15 → 2 Kings 2:14 | ra'ah רָאָה וַ/יִּרְאֻ֨/הוּ | laqach לָקַח וַ/יִּקַּח֩ | 1 |  |
| 237 | 2 Kings 2:15 → 2 Kings 2:16 | ra'ah רָאָה וַ/יִּרְאֻ֨/הוּ | nasa נָשָׂא נְשָׂא/וֹ֙ | 1 |  |
| 238 | 2 Kings 2:19 → 2 Kings 2:20 | ra'ah רָאָה רֹאֶ֑ה | laqach לָקַח קְחוּ; laqach לָקַח וַ/יִּקְח֖וּ | 1 |  |
| 239 | 2 Kings 3:14 → 2 Kings 3:15 | nabat נָבַט אַבִּ֥יט; ra'ah רָאָה אֶרְאֶֽ/ךָּ | laqach לָקַח קְחוּ | 1 |  |
| 240 | 2 Kings 3:17 → 2 Kings 3:15 | ra'ah רָאָה תִרְא֥וּ; ra'ah רָאָה תִרְא֣וּ | laqach לָקַח קְחוּ | 2 |  |
| 241 | 2 Kings 3:26 → 2 Kings 3:27 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּח֩ | 1 |  |
| 242 | 2 Kings 3:26 → 2 Kings 4:1 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח לָ/קַ֜חַת | 2 |  |
| 243 | 2 Kings 5:7 → 2 Kings 5:5 | ra'ah רָאָה וּ/רְא֔וּ | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 244 | 2 Kings 5:21 → 2 Kings 5:20 | ra'ah רָאָה וַ/יִּרְאֶ֤ה | laqach לָקַח מִ/קַּ֥חַת; laqach לָקַח וְ/לָקַחְתִּ֥י | 1 |  |
| 245 | 2 Kings 5:21 → 2 Kings 5:23 | ra'ah רָאָה וַ/יִּרְאֶ֤ה | laqach לָקַח קַ֣ח; nasa נָשָׂא וַ/יִּשְׂא֖וּ | 2 |  |
| 246 | 2 Kings 6:6 → 2 Kings 6:7 | ra'ah רָאָה וַ/יַּרְאֵ֨/הוּ֙ | laqach לָקַח וַ/יִּקָּחֵֽ/הוּ | 1 |  |
| 247 | 2 Kings 7:13 → 2 Kings 7:12 | ra'ah רָאָה וְ/נִרְאֶֽה | taphas תָּפַשׂ וְ/נִתְפְּשֵׂ֣/ם | 1 |  |
| 248 | 2 Kings 7:14 → 2 Kings 7:12 | ra'ah רָאָה וּ/רְאֽוּ | taphas תָּפַשׂ וְ/נִתְפְּשֵׂ֣/ם | 2 |  |
| 249 | 2 Kings 7:14 → 2 Kings 7:13 | ra'ah רָאָה וּ/רְאֽוּ | laqach לָקַח וְ/יִקְחוּ | 1 |  |
| 250 | 2 Kings 7:13 → 2 Kings 7:14 | ra'ah רָאָה וְ/נִרְאֶֽה | laqach לָקַח וַ/יִּקְח֕וּ | 1 |  |
| 251 | 2 Kings 8:10 → 2 Kings 8:8 | ra'ah רָאָה וְ/הִרְאַ֥/נִי | laqach לָקַח קַ֤ח | 2 |  |
| 252 | 2 Kings 8:10 → 2 Kings 8:9 | ra'ah רָאָה וְ/הִרְאַ֥/נִי | laqach לָקַח וַ/יִּקַּ֨ח | 1 |  |
| 253 | 2 Kings 8:13 → 2 Kings 8:15 | ra'ah רָאָה הִרְאַ֧/נִי | laqach לָקַח וַ/יִּקַּ֤ח | 2 |  |
| 254 | 2 Kings 8:29 → 2 Kings 9:1 | ra'ah רָאָה לִ/רְא֞וֹת | laqach לָקַח וְ֠/קַח | 1 |  |
| 255 | 2 Kings 9:2 → 2 Kings 9:1 | ra'ah רָאָה וּ/רְאֵֽה | laqach לָקַח וְ֠/קַח | 1 |  |
| 256 | 2 Kings 9:2 → 2 Kings 9:3 | ra'ah רָאָה וּ/רְאֵֽה | laqach לָקַח וְ/לָקַחְתָּ֤ | 1 |  |
| 257 | 2 Kings 9:16 → 2 Kings 9:17 | ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח קַ֥ח | 1 |  |
| 258 | 2 Kings 9:18 → 2 Kings 9:17 | tsaphah צָפָה הַ/צֹּפֶה֙ | laqach לָקַח קַ֥ח | 1 |  |
| 259 | 2 Kings 9:26 → 2 Kings 9:25 | ra'ah רָאָה רָאִ֤יתִי | nasa נָשָׂא שָׂ֚א; nasa נָשָׂא נָשָׂ֣א | 1 |  |
| 260 | 2 Kings 9:27 → 2 Kings 9:25 | ra'ah רָאָה רָאָ֔ה | nasa נָשָׂא שָׂ֚א; nasa נָשָׂא נָשָׂ֣א | 2 |  |
| 261 | 2 Kings 9:27 → 2 Kings 9:26 | ra'ah רָאָה רָאָ֔ה | nasa נָשָׂא שָׂ֧א | 1 |  |
| 262 | 2 Kings 9:30 → 2 Kings 9:32 | shaqaph שָׁקַף וַ/תַּשְׁקֵ֖ף | nasa נָשָׂא וַ/יִּשָּׂ֤א | 2 |  |
| 263 | 2 Kings 10:16 → 2 Kings 10:14 | ra'ah רָאָה וּ/רְאֵ֖ה | taphas תָּפַשׂ תִּפְשׂ֣וּ/ם; taphas תָּפַשׂ וַֽ/יִּתְפְּשׂ֖וּ/ם | 2 |  |
| 264 | 2 Kings 11:1 → 2 Kings 11:2 | ra'ah רָאָה ו/ראתה; ra'ah רָאָה רָאֲתָ֖ה | laqach לָקַח וַ/תִּקַּ֣ח | 1 |  |
| 265 | 2 Kings 11:4 → 2 Kings 11:2 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/תִּקַּ֣ח | 2 |  |
| 266 | 2 Kings 12:11 → 2 Kings 12:9 | ra'ah רָאָה כִּ/רְאוֹתָ֔/ם | laqach לָקַח קְחַת | 2 |  |
| 267 | 2 Kings 12:11 → 2 Kings 12:10 | ra'ah רָאָה כִּ/רְאוֹתָ֔/ם | laqach לָקַח וַ/יִּקַּ֞ח | 1 |  |
| 268 | 2 Kings 14:8 → 2 Kings 14:7 | ra'ah רָאָה נִתְרָאֶ֥ה | taphas תָּפַשׂ וְ/תָפַ֥שׂ | 1 |  |
| 269 | 2 Kings 14:8 → 2 Kings 14:10 | ra'ah רָאָה נִתְרָאֶ֥ה | nasa נָשָׂא וּֽ/נְשָׂאֲ/ךָ֖ | 2 |  |
| 270 | 2 Kings 14:11 → 2 Kings 14:10 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | nasa נָשָׂא וּֽ/נְשָׂאֲ/ךָ֖ | 1 |  |
| 271 | 2 Kings 14:11 → 2 Kings 14:13 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | taphas תָּפַשׂ תָּפַ֛שׂ | 2 |  |
| 272 | 2 Kings 16:10 → 2 Kings 16:8 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 273 | 2 Kings 16:10 → 2 Kings 16:9 | ra'ah רָאָה וַ/יַּ֥רְא | taphas תָּפַשׂ וַֽ/יִּתְפְּשֶׂ֔/הָ | 1 |  |
| 274 | 2 Kings 19:16 → 2 Kings 19:14 | ra'ah רָאָה וּ/רְאֵ֑ה | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 275 | 2 Kings 20:5 → 2 Kings 20:7 | ra'ah רָאָה רָאִ֖יתִי | laqach לָקַח קְח֖וּ; laqach לָקַח וַ/יִּקְח֛וּ | 2 |  |
| 276 | 2 Kings 20:15 → 2 Kings 20:17 | ra'ah רָאָה רָא֖וּ; ra'ah רָאָה רָא֔וּ; ra'ah רָאָה הִרְאִיתִ֖/ם | nasa נָשָׂא וְ/נִשָּׂ֣א | 2 |  |
| 277 | 2 Kings 23:17 → 2 Kings 23:16 | ra'ah רָאָה רֹאֶ֑ה | laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 278 | 2 Kings 23:29 → 2 Kings 23:30 | ra'ah רָאָה כִּ/רְאֹת֖/וֹ | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 279 | 2 Kings 25:19 → 2 Kings 25:18 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 280 | 2 Kings 25:19 → 2 Kings 25:20 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 281 | 1 Chronicles 10:5 → 1 Chronicles 10:4 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא נֹשֵׂ֨א; nasa נָשָׂא נֹשֵׂ֣א; laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 282 | 1 Chronicles 10:7 → 1 Chronicles 10:5 | ra'ah רָאָה וַ֠/יִּרְאוּ | nasa נָשָׂא נֹשֵֽׂא | 2 |  |
| 283 | 1 Chronicles 10:7 → 1 Chronicles 10:9 | ra'ah רָאָה וַ֠/יִּרְאוּ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 2 |  |
| 284 | 1 Chronicles 15:29 → 1 Chronicles 15:27 | shaqaph שָׁקַף נִשְׁקְפָ֣ה; ra'ah רָאָה וַ/תֵּ֨רֶא | nasa נָשָׂא הַ/נֹּשְׂאִ֣ים | 2 |  |
| 285 | 1 Chronicles 19:6 → 1 Chronicles 19:4 | ra'ah רָאָה וַ/יִּרְאוּ֙ | laqach לָקַח וַ/יִּקַּ֨ח | 2 |  |
| 286 | 1 Chronicles 19:19 → 1 Chronicles 20:2 | ra'ah רָאָה וַ/יִּרְא֞וּ | laqach לָקַח וַ/יִּקַּ֣ח | 2 |  |
| 287 | 1 Chronicles 21:15 → 1 Chronicles 21:16 | ra'ah רָאָה רָאָ֤ה | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 288 | 1 Chronicles 21:21 → 1 Chronicles 21:23 | nabat נָבַט וַ/יַּבֵּ֤ט; ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח קַֽח | 2 |  |
| 289 | 1 Chronicles 21:23 → 1 Chronicles 21:24 | ra'ah רָאָה רְאֵה֩ | nasa נָשָׂא אֶשָּׂ֤א | 1 |  |
| 290 | 2 Chronicles 9:3 → 2 Chronicles 9:1 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | nasa נָשָׂא נֹשְׂאִ֨ים | 2 |  |
| 291 | 2 Chronicles 12:7 → 2 Chronicles 12:9 | ra'ah רָאָה וּ/בִ/רְא֤וֹת | laqach לָקַח וַ/יִּקַּ֞ח; laqach לָקַח לָקָ֑ח; laqach לָקַח וַ/יִּקַּח֙ | 2 |  |
| 292 | 2 Chronicles 15:9 → 2 Chronicles 15:8 | ra'ah רָאָה בִּ/רְאֹתָ֕/ם | lakad לָכַד לָכַ֖ד | 1 |  |
| 293 | 2 Chronicles 16:7 → 2 Chronicles 16:6 | ra'ah רָאָה הָ/רֹאֶ֔ה | laqach לָקַח לָקַח֙; nasa נָשָׂא וַ/יִּשְׂא֞וּ | 1 |  |
| 294 | 2 Chronicles 18:24 → 2 Chronicles 18:25 | ra'ah רָאָה רֹאֶ֖ה | laqach לָקַח קְחוּ֙ | 1 |  |
| 295 | 2 Chronicles 22:10 → 2 Chronicles 22:9 | ra'ah רָאָה רָאֲתָ֖ה | lakad לָכַד וַֽ/יִּלְכְּדֻ֜/הוּ | 1 |  |
| 296 | 2 Chronicles 22:10 → 2 Chronicles 22:11 | ra'ah רָאָה רָאֲתָ֖ה | laqach לָקַח וַ/תִּקַּח֩ | 1 |  |
| 297 | 2 Chronicles 25:17 → 2 Chronicles 25:19 | ra'ah רָאָה נִתְרָאֶ֥ה | nasa נָשָׂא וּ/נְשָׂאֲ/ךָ֥ | 2 |  |
| 298 | 2 Chronicles 25:21 → 2 Chronicles 25:19 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | nasa נָשָׂא וּ/נְשָׂאֲ/ךָ֥ | 2 |  |
| 299 | 2 Chronicles 25:21 → 2 Chronicles 25:23 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | taphas תָּפַשׂ תָּפַ֛שׂ | 2 |  |
| 300 | Nehemiah 6:16 → Nehemiah 6:18 | ra'ah רָאָה וַ/יִּֽרְא֗וּ | laqach לָקַח לָקַ֕ח | 2 |  |
| 301 | Nehemiah 13:23 → Nehemiah 13:25 | ra'ah רָאָה רָאִ֤יתִי | nasa נָשָׂא תִּשְׂאוּ֙ | 2 |  |
| 302 | Esther 1:4 → Esther 1:6 | ra'ah רָאָה בְּ/הַרְאֹת֗/וֹ | achaz אָחַז אָחוּז֙ | 2 |  |
| 303 | Esther 2:9 → Esther 2:7 | ra'ah רָאָה הָ/רְאֻי֥וֹת | laqach לָקַח לְקָחָ֧/הּ | 2 |  |
| 304 | Esther 2:9 → Esther 2:8 | ra'ah רָאָה הָ/רְאֻי֥וֹת | laqach לָקַח וַ/תִּלָּקַ֤ח | 1 |  |
| 305 | Esther 2:15 → Esther 2:16 | ra'ah רָאָה רֹאֶֽי/הָ | laqach לָקַח וַ/תִּלָּקַ֨ח | 1 |  |
| 306 | Esther 2:15 → Esther 2:17 | ra'ah רָאָה רֹאֶֽי/הָ | nasa נָשָׂא וַ/תִּשָּׂא | 2 |  |
| 307 | Esther 5:9 → Esther 5:11 | ra'ah רָאָה וְ/כִ/רְאוֹת֩ | nasa נָשָׂא נִשְּׂא֔/וֹ | 2 |  |
| 308 | Esther 5:13 → Esther 5:11 | ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא נִשְּׂא֔/וֹ | 2 |  |
| 309 | Job 2:13 → Job 2:12 | ra'ah רָאָה רָא֔וּ | nasa נָשָׂא וַ/יִּשְׂא֨וּ; nasa נָשָׂא וַ/יִּשְׂא֥וּ _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 310 | Job 5:3 → Job 5:5 | ra'ah רָאָה רָ֭אִיתִי | laqach לָקַח יִקָּחֵ֑/הוּ | 2 |  |
| 311 | Job 7:19 → Job 7:21 | sha'ah שָׁעָה תִשְׁעֶ֣ה | nasa נָשָׂא תִשָּׂ֣א | 2 |  |
| 312 | Job 20:17 → Job 20:19 | ra'ah רָאָה יֵ֥רֶא | gazal גָּזַל גָּ֝זַ֗ל | 2 |  |
| 313 | Job 23:9 → Job 23:11 | chazah חָזָה אָ֑חַז; ra'ah רָאָה אֶרְאֶֽה | achaz אָחַז אָחֲזָ֣ה | 2 |  |
| 314 | Job 24:1 → Job 24:2 | chazah חָזָה חָ֥זוּ | gazal גָּזַל גָּ֝זְל֗וּ | 1 |  |
| 315 | Job 27:12 → Job 27:13 | chazah חָזָה חֲזִיתֶ֑ם | laqach לָקַח יִקָּֽחוּ | 1 |  |
| 316 | Job 28:27 → Job 29:1 | ra'ah רָאָה רָ֭אָ/הּ | nasa נָשָׂא שְׂאֵ֥ת | 2 |  |
| 317 | Job 34:21 → Job 34:19 | ra'ah רָאָה יִרְאֶֽה | nasa נָשָׂא נָשָׂ֨א | 2 |  |
| 318 | Job 34:29 → Job 34:31 | shur שׁוּר יְשׁוּרֶ֑/נּוּ | nasa נָשָׂא נָשָׂ֗אתִי | 2 |  |
| 319 | Job 34:32 → Job 34:31 | chazah חָזָה אֶ֭חֱזֶה | nasa נָשָׂא נָשָׂ֗אתִי | 1 |  |
| 320 | Job 35:5 → Job 35:7 | nabat נָבַט הַבֵּ֣ט; ra'ah רָאָה וּ/רְאֵ֑ה; shur שׁוּר וְ/שׁ֥וּר | laqach לָקַח יִקָּֽח | 2 |  |
| 321 | Job 38:22 → Job 38:20 | ra'ah רָאָה תִּרְאֶֽה | laqach לָקַח תִ֭קָּחֶ/נּוּ | 2 |  |
| 322 | Psalms 9:14 → Psalms 9:16 | ra'ah רָאָה רְאֵ֣ה | lakad לָכַד נִלְכְּדָ֥ה | 2 |  |
| 323 | Psalms 10:11 → Psalms 10:12 | ra'ah רָאָה רָאָ֥ה | nasa נָשָׂא נְשָׂ֣א | 1 |  |
| 324 | Psalms 10:14 → Psalms 10:12 | ra'ah רָאָה רָאִ֡תָה; nabat נָבַט תַּבִּיט֮ | nasa נָשָׂא נְשָׂ֣א | 2 |  |
| 325 | Psalms 18:16 → Psalms 18:17 | ra'ah רָאָה וַ/יֵּ֤רָא֨וּ | laqach לָקַח יִקָּחֵ֑/נִי | 1 |  |
| 326 | Psalms 25:19 → Psalms 25:18 | ra'ah רָאָה רְאֵֽה | nasa נָשָׂא וְ֝/שָׂ֗א | 1 |  |
| 327 | Psalms 31:12 → Psalms 31:14 | ra'ah רָאָה רֹאַ֥/י | laqach לָקַח לָ/קַ֖חַת | 2 |  |
| 328 | Psalms 48:6 → Psalms 48:7 | ra'ah רָאָה רָ֭אוּ | achaz אָחַז אֲחָזָ֣תַ/ם | 1 |  |
| 329 | Psalms 48:9 → Psalms 48:7 | ra'ah רָאָה רָאִ֗ינוּ | achaz אָחַז אֲחָזָ֣תַ/ם | 2 |  |
| 330 | Psalms 49:20 → Psalms 49:18 | ra'ah רָאָה יִרְאוּ | laqach לָקַח יִקַּ֣ח | 2 |  |
| 331 | Psalms 50:18 → Psalms 50:16 | ra'ah רָאָה רָאִ֣יתָ | nasa נָשָׂא וַ/תִּשָּׂ֖א | 2 |  |
| 332 | Psalms 59:11 → Psalms 59:13 | ra'ah רָאָה יַרְאֵ֥/נִי | lakad לָכַד וְ/יִלָּכְד֥וּ | 2 |  |
| 333 | Psalms 63:3 → Psalms 63:5 | chazah חָזָה חֲזִיתִ֑י/ךָ; ra'ah רָאָה לִ/רְא֥וֹת | nasa נָשָׂא אֶשָּׂ֥א | 2 |  |
| 334 | Psalms 89:49 → Psalms 89:51 | ra'ah רָאָה יִרְאֶה | nasa נָשָׂא שְׂאֵתִ֥/י | 2 |  |
| 335 | Proverbs 22:29 → Proverbs 22:27 | chazah חָזָה חָזִ֡יתָ | laqach לָקַח יִקַּ֥ח | 2 |  |
| 336 | Proverbs 27:12 → Proverbs 27:13 | ra'ah רָאָה רָאָ֣ה | laqach לָקַח קַח | 1 |  |
| 337 | Ecclesiastes 2:1 → Ecclesiastes 2:3 | ra'ah רָאָה וּ/רְאֵ֣ה | achaz אָחַז וְ/לֶ/אֱחֹ֣ז | 2 |  |
| 338 | Ecclesiastes 5:12 → Ecclesiastes 5:14 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא יִשָּׂ֣א | 2 |  |
| 339 | Ecclesiastes 5:17 → Ecclesiastes 5:18 | ra'ah רָאָה רָאִ֣יתִי; ra'ah רָאָה וְ/לִ/רְא֨וֹת | nasa נָשָׂא וְ/לָ/שֵׂ֣את | 1 |  |
| 340 | Ecclesiastes 6:1 → Ecclesiastes 5:18 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא וְ/לָ/שֵׂ֣את | 2 |  |
| 341 | Ecclesiastes 7:27 → Ecclesiastes 7:26 | ra'ah רָאָה רְאֵה֙ | lakad לָכַד יִלָּ֥כֶד | 1 |  |
| 342 | Ecclesiastes 9:11 → Ecclesiastes 9:12 | ra'ah רָאָה וְ/רָאֹ֣ה | achaz אָחַז שֶׁ/נֶּֽאֱחָזִים֙; achaz אָחַז הָ/אֲחֻז֖וֹת | 1 |  |
| 343 | Ecclesiastes 9:13 → Ecclesiastes 9:12 | ra'ah רָאָה רָאִ֥יתִי | achaz אָחַז שֶׁ/נֶּֽאֱחָזִים֙; achaz אָחַז הָ/אֲחֻז֖וֹת | 1 |  |
| 344 | Song of Songs 2:14 → Song of Songs 2:15 | ra'ah רָאָה הַרְאִ֨י/נִי֙ | achaz אָחַז אֶֽחֱזוּ | 1 |  |
| 345 | Song of Songs 3:3 → Song of Songs 3:4 | ra'ah רָאָה רְאִיתֶֽם | achaz אָחַז אֲחַזְתִּי/ו֙ | 1 |  |
| 346 | Isaiah 1:12 → Isaiah 1:14 | ra'ah רָאָה לֵ/רָא֖וֹת | nasa נָשָׂא נְשֹֽׂא | 2 |  |
| 347 | Isaiah 2:1 → Isaiah 2:2 | chazah חָזָה חָזָ֔ה | nasa נָשָׂא וְ/נִשָּׂ֖א | 1 |  |
| 348 | Isaiah 5:30 → Isaiah 5:29 | nabat נָבַט וְ/נִבַּ֤ט | achaz אָחַז וְ/יֹאחֵ֣ז | 1 |  |
| 349 | Isaiah 6:1 → Isaiah 5:29 | ra'ah רָאָה וָ/אֶרְאֶ֧ה | achaz אָחַז וְ/יֹאחֵ֣ז | 2 |  |
| 350 | Isaiah 5:30 → Isaiah 6:1 | nabat נָבַט וְ/נִבַּ֤ט | nasa נָשָׂא וְ/נִשָּׂ֑א | 1 |  |
| 351 | Isaiah 6:5 → Isaiah 6:6 | ra'ah רָאָה רָא֥וּ | laqach לָקַח לָקַ֖ח | 1 |  |
| 352 | Isaiah 13:1 → Isaiah 13:2 | chazah חָזָה חָזָ֔ה | nasa נָשָׂא שְֽׂאוּ | 1 |  |
| 353 | Isaiah 18:4 → Isaiah 18:3 | nabat נָבַט וְ/אַבִּ֣יטָה | nasa נָשָׂא כִּ/נְשֹׂא | 1 |  |
| 354 | Isaiah 22:4 → Isaiah 22:6 | sha'ah שָׁעָה שְׁע֥וּ | nasa נָשָׂא נָשָׂ֣א | 2 |  |
| 355 | Isaiah 22:8 → Isaiah 22:6 | nabat נָבַט וַ/תַּבֵּט֙ | nasa נָשָׂא נָשָׂ֣א | 2 |  |
| 356 | Isaiah 33:15 → Isaiah 33:14 | ra'ah רָאָה מֵ/רְא֥וֹת | achaz אָחַז אָחֲזָ֥ה | 1 |  |
| 357 | Isaiah 39:4 → Isaiah 39:6 | ra'ah רָאָה רָא֖וּ; ra'ah רָאָה רָא֔וּ; ra'ah רָאָה הִרְאִיתִ֖י/ם | nasa נָשָׂא וְ/נִשָּׂ֣א | 2 |  |
| 358 | Isaiah 40:5 → Isaiah 40:4 | ra'ah רָאָה וְ/רָא֤וּ | nasa נָשָׂא יִנָּשֵׂ֔א | 1 |  |
| 359 | Isaiah 40:26 → Isaiah 40:24 | ra'ah רָאָה וּ/רְאוּ֙ | nasa נָשָׂא תִּשָּׂאֵֽ/ם | 2 |  |
| 360 | Isaiah 44:16 → Isaiah 44:14 | ra'ah רָאָה רָאִ֥יתִי | laqach לָקַח וַ/יִּקַּ֤ח | 2 |  |
| 361 | Isaiah 44:16 → Isaiah 44:15 | ra'ah רָאָה רָאִ֥יתִי | laqach לָקַח וַ/יִּקַּ֤ח | 1 |  |
| 362 | Isaiah 47:3 → Isaiah 47:2 | ra'ah רָאָה תֵּרָאֶ֖ה | laqach לָקַח קְחִ֥י | 1 |  |
| 363 | Isaiah 52:10 → Isaiah 52:8 | ra'ah רָאָה וְ/רָאוּ֙ | nasa נָשָׂא נָ֥שְׂאוּ _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 364 | Isaiah 52:10 → Isaiah 52:11 | ra'ah רָאָה וְ/רָאוּ֙ | nasa נָשָׂא נֹשְׂאֵ֖י | 1 |  |
| 365 | Isaiah 52:15 → Isaiah 52:13 | ra'ah רָאָה רָא֔וּ | nasa נָשָׂא וְ/נִשָּׂ֛א | 2 |  |
| 366 | Isaiah 53:2 → Isaiah 53:4 | ra'ah רָאָה וְ/נִרְאֵ֥/הוּ | nasa נָשָׂא נָשָׂ֔א | 2 | chamad חָמַד (Isaiah 53:2) |
| 367 | Isaiah 53:10 → Isaiah 53:8 | ra'ah רָאָה יִרְאֶ֥ה | laqach לָקַח לֻקָּ֔ח | 2 |  |
| 368 | Isaiah 53:10 → Isaiah 53:12 | ra'ah רָאָה יִרְאֶ֥ה | nasa נָשָׂא נָשָׂ֔א | 2 |  |
| 369 | Isaiah 53:11 → Isaiah 53:12 | ra'ah רָאָה יִרְאֶ֣ה | nasa נָשָׂא נָשָׂ֔א | 1 |  |
| 370 | Isaiah 56:10 → Isaiah 56:12 | tsaphah צָפָה צפו; tsaphah צָפָה צֹפָ֞י/ו | laqach לָקַח אֶקְחָה | 2 |  |
| 371 | Isaiah 57:8 → Isaiah 57:7 | chazah חָזָה חָזִֽית | nasa נָשָׂא וְ/נִשָּׂ֔א | 1 |  |
| 372 | Isaiah 60:2 → Isaiah 60:4 | ra'ah רָאָה יֵרָאֶֽה | nasa נָשָׂא שְׂאִֽי _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 373 | Isaiah 60:5 → Isaiah 60:4 | ra'ah רָאָה תִּרְאִי֙ | nasa נָשָׂא שְׂאִֽי _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 374 | Isaiah 60:4 → Isaiah 60:6 | ra'ah רָאָה וּ/רְאִ֔י | nasa נָשָׂא יִשָּׂ֔אוּ | 2 |  |
| 375 | Isaiah 60:5 → Isaiah 60:6 | ra'ah רָאָה תִּרְאִי֙ | nasa נָשָׂא יִשָּׂ֔אוּ | 1 |  |
| 376 | Isaiah 64:3 → Isaiah 64:5 | ra'ah רָאָה רָאָ֗תָה | nasa נָשָׂא יִשָּׂאֻֽ/נוּ | 2 |  |
| 377 | Isaiah 66:14 → Isaiah 66:12 | ra'ah רָאָה וּ/רְאִיתֶם֙ | nasa נָשָׂא תִּנָּשֵׂ֔אוּ | 2 |  |
| 378 | Isaiah 66:19 → Isaiah 66:21 | ra'ah רָאָה רָא֣וּ | laqach לָקַח אֶקַּ֛ח | 2 |  |
| 379 | Jeremiah 2:10 → Jeremiah 2:8 | ra'ah רָאָה וּ/רְא֔וּ; ra'ah רָאָה וּ/רְא֕וּ | taphas תָּפַשׂ וְ/תֹפְשֵׂ֤י | 2 |  |
| 380 | Jeremiah 2:31 → Jeremiah 2:30 | ra'ah רָאָה רְא֣וּ | laqach לָקַח לָקָ֑חוּ | 1 |  |
| 381 | Jeremiah 5:1 → Jeremiah 5:3 | ra'ah רָאָה וּ/רְאוּ | laqach לָקַח קַ֣חַת | 2 |  |
| 382 | Jeremiah 7:17 → Jeremiah 7:16 | ra'ah רָאָה רֹאֶ֔ה | nasa נָשָׂא תִּשָּׂ֧א | 1 |  |
| 383 | Jeremiah 13:20 → Jeremiah 13:21 | ra'ah רָאָה ו/ראי; ra'ah רָאָה וּ/רְא֔וּ | achaz אָחַז יֹאחֱז֔וּ/ךְ | 1 |  |
| 384 | Jeremiah 20:4 → Jeremiah 20:5 | ra'ah רָאָה רֹא֑וֹת | laqach לָקַח וּ/לְקָח֔וּ/ם | 1 |  |
| 385 | Jeremiah 20:12 → Jeremiah 20:10 | ra'ah רָאָה רֹאֶ֥ה; ra'ah רָאָה אֶרְאֶ֤ה | laqach לָקַח וְ/נִקְחָ֥ה | 2 |  |
| 386 | Jeremiah 32:4 → Jeremiah 32:3 | ra'ah רָאָה תִּרְאֶֽינָה | lakad לָכַד וּ/לְכָדָֽ/הּ | 1 |  |
| 387 | Jeremiah 33:24 → Jeremiah 33:26 | ra'ah רָאָה רָאִ֗יתָ | laqach לָקַח מִ/קַּ֤חַת | 2 |  |
| 388 | Jeremiah 38:21 → Jeremiah 38:23 | ra'ah רָאָה הִרְאַ֖/נִי | taphas תָּפַשׂ תִּתָּפֵ֔שׂ | 2 |  |
| 389 | Jeremiah 39:4 → Jeremiah 39:5 | ra'ah רָאָה רָ֠אָ/ם | laqach לָקַח וַ/יִּקְח֣וּ | 1 |  |
| 390 | Jeremiah 40:4 → Jeremiah 40:2 | ra'ah רָאָה רְאֵה֙ | laqach לָקַח וַ/יִּקַּ֥ח | 2 |  |
| 391 | Jeremiah 41:13 → Jeremiah 41:12 | ra'ah רָאָה כִּ/רְא֤וֹת | laqach לָקַח וַ/יִּקְחוּ֙ | 1 |  |
| 392 | Jeremiah 52:25 → Jeremiah 52:24 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 393 | Jeremiah 52:25 → Jeremiah 52:26 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח וַ/יִּקַּ֣ח | 1 |  |
| 394 | Lamentations 2:20 → Lamentations 2:19 | ra'ah רָאָה רְאֵ֤ה; nabat נָבַט וְֽ/הַבִּ֔יטָ/ה | nasa נָשָׂא שְׂאִ֧י | 1 |  |
| 395 | Lamentations 4:17 → Lamentations 4:16 | tsaphah צָפָה צִפִּ֔ינוּ | nasa נָשָׂא נָשָׂ֔אוּ | 1 |  |
| 396 | Ezekiel 8:2 → Ezekiel 8:3 | ra'ah רָאָה וָ/אֶרְאֶ֗ה | laqach לָקַח וַ/יִּקָּחֵ֖/נִי; nasa נָשָׂא וַ/תִּשָּׂ֣א | 1 |  |
| 397 | Ezekiel 8:4 → Ezekiel 8:3 | ra'ah רָאָה רָאִ֖יתִי | laqach לָקַח וַ/יִּקָּחֵ֖/נִי; nasa נָשָׂא וַ/תִּשָּׂ֣א | 1 |  |
| 398 | Ezekiel 8:4 → Ezekiel 8:5 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 399 | Ezekiel 8:6 → Ezekiel 8:5 | ra'ah רָאָה הֲ/רֹאֶ֥ה; ra'ah רָאָה תִּרְאֶ֔ה | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 400 | Ezekiel 8:7 → Ezekiel 8:5 | ra'ah רָאָה וָ/אֶרְאֶ֕ה | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 401 | Ezekiel 10:8 → Ezekiel 10:6 | ra'ah רָאָה וַ/יֵּרָ֖א | laqach לָקַח קַ֥ח | 2 |  |
| 402 | Ezekiel 10:8 → Ezekiel 10:7 | ra'ah רָאָה וַ/יֵּרָ֖א | nasa נָשָׂא וַ/יִּשָּׂא֙; laqach לָקַח וַ/יִּקַּ֖ח | 1 |  |
| 403 | Ezekiel 10:9 → Ezekiel 10:7 | ra'ah רָאָה וָ/אֶרְאֶ֗ה | nasa נָשָׂא וַ/יִּשָּׂא֙; laqach לָקַח וַ/יִּקַּ֖ח | 2 |  |
| 404 | Ezekiel 10:15 → Ezekiel 10:16 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא וּ/בִ/שְׂאֵ֨ת | 1 |  |
| 405 | Ezekiel 10:20 → Ezekiel 10:19 | ra'ah רָאָה רָאִ֛יתִי | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 406 | Ezekiel 10:22 → Ezekiel 11:1 | ra'ah רָאָה רָאִ֨יתִי֙ | nasa נָשָׂא וַ/תִּשָּׂ֨א | 1 |  |
| 407 | Ezekiel 11:24 → Ezekiel 11:22 | ra'ah רָאָה רָאִֽיתִי | nasa נָשָׂא וַ/יִּשְׂא֤וּ | 2 |  |
| 408 | Ezekiel 11:25 → Ezekiel 11:24 | ra'ah רָאָה הֶרְאָֽ/נִי | nasa נָשָׂא נְשָׂאַ֗תְ/נִי | 1 |  |
| 409 | Ezekiel 12:6 → Ezekiel 12:7 | ra'ah רָאָה תִרְאֶ֖ה | nasa נָשָׂא נָשָׂ֖אתִי _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 410 | Ezekiel 12:13 → Ezekiel 12:12 | ra'ah רָאָה יִרְאֶ֖ה | nasa נָשָׂא יִשָּׂא֙ _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 411 | Ezekiel 12:12 → Ezekiel 12:13 | ra'ah רָאָה יִרְאֶ֥ה | taphas תָּפַשׂ וְ/נִתְפַּ֖שׂ | 1 |  |
| 412 | Ezekiel 16:37 → Ezekiel 16:39 | ra'ah רָאָה וְ/רָא֖וּ | laqach לָקַח וְ/לָקְח֖וּ | 2 |  |
| 413 | Ezekiel 16:50 → Ezekiel 16:52 | ra'ah רָאָה רָאִֽיתִי | nasa נָשָׂא שְׂאִ֣י; nasa נָשָׂא וּ/שְׂאִ֣י | 2 |  |
| 414 | Ezekiel 18:14 → Ezekiel 18:12 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | gazal גָּזַל גָּזָ֔ל; nasa נָשָׂא נָשָׂ֣א | 2 |  |
| 415 | Ezekiel 18:14 → Ezekiel 18:13 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | laqach לָקַח לָקַ֖ח | 1 |  |
| 416 | Ezekiel 18:14 → Ezekiel 18:15 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | nasa נָשָׂא נָשָׂ֔א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 417 | Ezekiel 18:14 → Ezekiel 18:16 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | gazal גָּזַל גָזָ֑ל | 2 |  |
| 418 | Ezekiel 19:5 → Ezekiel 19:4 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | taphas תָּפַשׂ נִתְפָּ֑שׂ | 1 |  |
| 419 | Ezekiel 21:26 → Ezekiel 21:28 | ra'ah רָאָה רָאָ֖ה | taphas תָּפַשׂ לְ/הִתָּפֵֽשׂ | 2 |  |
| 420 | Ezekiel 21:29 → Ezekiel 21:28 | ra'ah רָאָה לְ/הֵֽרָאוֹת֙ | taphas תָּפַשׂ לְ/הִתָּפֵֽשׂ | 1 |  |
| 421 | Ezekiel 23:11 → Ezekiel 23:10 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח לָקָ֔חוּ | 1 |  |
| 422 | Ezekiel 32:31 → Ezekiel 32:30 | ra'ah רָאָה יִרְאֶ֣ה | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 1 |  |
| 423 | Ezekiel 33:3 → Ezekiel 33:2 | ra'ah רָאָה וְ/רָאָ֥ה | laqach לָקַח וְ/לָקְח֨וּ | 1 |  |
| 424 | Ezekiel 33:2 → Ezekiel 33:4 | tsaphah צָפָה לְ/צֹפֶֽה | laqach לָקַח וַ/תִּקָּחֵ֑/הוּ | 2 |  |
| 425 | Ezekiel 33:3 → Ezekiel 33:4 | ra'ah רָאָה וְ/רָאָ֥ה | laqach לָקַח וַ/תִּקָּחֵ֑/הוּ | 1 |  |
| 426 | Ezekiel 33:6 → Ezekiel 33:4 | tsaphah צָפָה וְ֠/הַ/צֹּפֶה; ra'ah רָאָה יִרְאֶ֨ה; tsaphah צָפָה הַ/צֹּפֶ֥ה | laqach לָקַח וַ/תִּקָּחֵ֑/הוּ | 2 |  |
| 427 | Ezekiel 33:7 → Ezekiel 33:6 | tsaphah צָפָה צֹפֶ֥ה | laqach לָקַח וַ/תִּקַּ֥ח; laqach לָקַח נִלְקָ֔ח | 1 |  |
| 428 | Ezekiel 41:8 → Ezekiel 41:6 | ra'ah רָאָה וְ/רָאִ֧יתִי | achaz אָחַז אֲחוּזִ֑ים; achaz אָחַז אֲחוּזִ֖ים | 2 |  |
| 429 | Ezekiel 43:3 → Ezekiel 43:5 | ra'ah רָאָה רָאִ֗יתִי; ra'ah רָאָה רָאִ֨יתִי֙; ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא וַ/תִּשָּׂאֵ֣/נִי | 2 |  |
| 430 | Daniel 1:15 → Daniel 1:16 | ra'ah רָאָה נִרְאָ֤ה | nasa נָשָׂא נֹשֵׂא֙ | 1 |  |
| 431 | Daniel 8:1 → Daniel 8:3 | ra'ah רָאָה נִרְאָ֤ה; ra'ah רָאָה הַ/נִּרְאָ֥ה | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 432 | Daniel 8:2 → Daniel 8:3 | ra'ah רָאָה וָֽ/אֶרְאֶה֮; ra'ah רָאָה בִּ/רְאֹתִ֔/י; ra'ah רָאָה וָ/אֶרְאֶה֙ | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 433 | Daniel 8:4 → Daniel 8:3 | ra'ah רָאָה רָאִ֣יתִי | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 434 | Daniel 10:7 → Daniel 10:5 | ra'ah רָאָה וְ/רָאִיתִי֩; ra'ah רָאָה רָא֖וּ | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 435 | Hosea 5:13 → Hosea 5:14 | ra'ah רָאָה וַ/יַּ֨רְא | nasa נָשָׂא אֶשָּׂ֖א | 1 |  |
| 436 | Amos 7:1 → Amos 6:13 | ra'ah רָאָה הִרְאַ֨/נִי֙ | laqach לָקַח לָקַ֥חְנוּ | 2 |  |
| 437 | Amos 9:1 → Amos 9:2 | ra'ah רָאָה רָאִ֨יתִי | laqach לָקַח תִקָּחֵ֑/ם | 1 |  |
| 438 | Amos 9:1 → Amos 9:3 | ra'ah רָאָה רָאִ֨יתִי | laqach לָקַח וּ/לְקַחְתִּ֑י/ם | 2 |  |
| 439 | Jonah 4:5 → Jonah 4:3 | ra'ah רָאָה יִרְאֶ֔ה | laqach לָקַח קַח | 2 |  |
| 440 | Micah 7:7 → Micah 7:9 | tsaphah צָפָה אֲצַפֶּ֔ה | nasa נָשָׂא אֶשָּׂ֔א | 2 |  |
| 441 | Micah 7:10 → Micah 7:9 | ra'ah רָאָה וְ/תֵרֶ֤א; ra'ah רָאָה תִּרְאֶ֣ינָּה | nasa נָשָׂא אֶשָּׂ֔א | 1 |  |
| 442 | Micah 7:16 → Micah 7:18 | ra'ah רָאָה יִרְא֤וּ | nasa נָשָׂא נֹשֵׂ֤א | 2 |  |
| 443 | Habakkuk 1:1 → Habakkuk 1:3 | chazah חָזָה חָזָ֔ה | nasa נָשָׂא יִשָּֽׂא | 2 |  |
| 444 | Habakkuk 1:5 → Habakkuk 1:3 | ra'ah רָאָה רְא֤וּ; nabat נָבַט וְֽ/הַבִּ֔יטוּ | nasa נָשָׂא יִשָּֽׂא | 2 |  |
| 445 | Zechariah 2:3 → Zechariah 2:1 | ra'ah רָאָה וַ/יַּרְאֵ֣/נִי | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 446 | Zechariah 2:3 → Zechariah 2:4 | ra'ah רָאָה וַ/יַּרְאֵ֣/נִי | nasa נָשָׂא נָשָׂ֣א; nasa נָשָׂא הַ/נֹּשְׂאִ֥ים | 1 |  |
| 447 | Zechariah 2:3 → Zechariah 2:5 | ra'ah רָאָה וַ/יַּרְאֵ֣/נִי | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 2 |  |
| 448 | Zechariah 2:5 → Zechariah 2:4 | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא נָשָׂ֣א; nasa נָשָׂא הַ/נֹּשְׂאִ֥ים | 1 |  |
| 449 | Zechariah 2:6 → Zechariah 2:4 | ra'ah רָאָה לִ/רְא֥וֹת | nasa נָשָׂא נָשָׂ֣א; nasa נָשָׂא הַ/נֹּשְׂאִ֥ים | 2 |  |
| 450 | Zechariah 2:6 → Zechariah 2:5 | ra'ah רָאָה לִ/רְא֥וֹת | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 451 | Zechariah 5:2 → Zechariah 5:1 | ra'ah רָאָה רֹאֶ֑ה; ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 1 |  |
| 452 | Zechariah 5:5 → Zechariah 5:7 | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא נִשֵּׂ֑את | 2 |  |
| 453 | Zechariah 5:9 → Zechariah 5:7 | ra'ah רָאָה וָ/אֵ֗רֶא | nasa נָשָׂא נִשֵּׂ֑את | 2 |  |
| 454 | Zechariah 6:8 → Zechariah 6:10 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח לָק֨וֹחַ֙ | 2 |  |


---

## Appendix B — Tier 3 (3–5 verses apart), complete

| # | Reference(s) | Seeing | Taking | Δ | Desire term in span |
|---|---|---|---|---|---|
| 1 | Genesis 2:19 → Genesis 2:15 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח וַ/יִּקַּ֛ח | 4 |  |
| 2 | Genesis 2:19 → Genesis 2:22 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח לָקַ֥ח | 3 |  |
| 3 | Genesis 2:19 → Genesis 2:23 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח לֻֽקֳחָה | 4 |  |
| 4 | Genesis 4:4 → Genesis 3:23 | sha'ah שָׁעָה וַ/יִּ֣שַׁע | laqach לָקַח לֻקַּ֖ח | 5 |  |
| 5 | Genesis 6:5 → Genesis 6:2 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקְח֤וּ | 3 |  |
| 6 | Genesis 8:5 → Genesis 8:9 | ra'ah רָאָה נִרְא֖וּ | laqach לָקַח וַ/יִּקָּחֶ֔/הָ | 4 |  |
| 7 | Genesis 8:13 → Genesis 8:9 | ra'ah רָאָה וַ/יַּ֕רְא | laqach לָקַח וַ/יִּקָּחֶ֔/הָ | 4 |  |
| 8 | Genesis 12:1 → Genesis 11:29 | ra'ah רָאָה אַרְאֶֽ/ךָּ | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 9 | Genesis 12:1 → Genesis 12:5 | ra'ah רָאָה אַרְאֶֽ/ךָּ | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 10 | Genesis 12:12 → Genesis 12:15 | ra'ah רָאָה יִרְא֤וּ | laqach לָקַח וַ/תֻּקַּ֥ח | 3 |  |
| 11 | Genesis 12:14 → Genesis 12:19 | ra'ah רָאָה וַ/יִּרְא֤וּ | laqach לָקַח וָ/אֶקַּ֥ח; laqach לָקַח קַ֥ח | 5 |  |
| 12 | Genesis 12:15 → Genesis 12:19 | ra'ah רָאָה וַ/יִּרְא֤וּ | laqach לָקַח וָ/אֶקַּ֥ח; laqach לָקַח קַ֥ח | 4 |  |
| 13 | Genesis 13:10 → Genesis 13:6 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא נָשָׂ֥א | 4 |  |
| 14 | Genesis 13:14 → Genesis 13:10 | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא וַ/יִּשָּׂא _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 15 | Genesis 13:15 → Genesis 13:10 | ra'ah רָאָה רֹאֶ֖ה | nasa נָשָׂא וַ/יִּשָּׂא _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 16 | Genesis 13:10 → Genesis 13:14 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא שָׂ֣א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 17 | Genesis 15:5 → Genesis 14:24 | nabat נָבַט הַבֶּט | laqach לָקַח יִקְח֥וּ | 5 |  |
| 18 | Genesis 15:5 → Genesis 15:9 | nabat נָבַט הַבֶּט | laqach לָקַח קְחָ֥/ה | 4 |  |
| 19 | Genesis 15:5 → Genesis 15:10 | nabat נָבַט הַבֶּט | laqach לָקַח וַ/יִּֽקַּֽח | 5 |  |
| 20 | Genesis 18:1 → Genesis 17:23 | ra'ah רָאָה וַ/יֵּרָ֤א | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 21 | Genesis 18:1 → Genesis 18:4 | ra'ah רָאָה וַ/יֵּרָ֤א | laqach לָקַח יֻקַּֽח | 3 |  |
| 22 | Genesis 18:1 → Genesis 18:5 | ra'ah רָאָה וַ/יֵּרָ֤א | laqach לָקַח וְ/אֶקְחָ֨ה | 4 |  |
| 23 | Genesis 18:2 → Genesis 18:5 | ra'ah רָאָה וַ/יַּ֔רְא; ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וְ/אֶקְחָ֨ה | 3 |  |
| 24 | Genesis 18:2 → Genesis 18:7 | ra'ah רָאָה וַ/יַּ֔רְא; ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 25 | Genesis 18:21 → Genesis 18:24 | ra'ah רָאָה וְ/אֶרְאֶ֔ה | nasa נָשָׂא תִשָּׂ֣א | 3 |  |
| 26 | Genesis 18:21 → Genesis 18:26 | ra'ah רָאָה וְ/אֶרְאֶ֔ה | nasa נָשָׂא וְ/נָשָׂ֥אתִי | 5 |  |
| 27 | Genesis 19:17 → Genesis 19:14 | nabat נָבַט תַּבִּ֣יט | laqach לָקַח לֹקְחֵ֣י | 3 |  |
| 28 | Genesis 19:17 → Genesis 19:21 | nabat נָבַט תַּבִּ֣יט | nasa נָשָׂא נָשָׂ֣אתִי | 4 |  |
| 29 | Genesis 19:26 → Genesis 19:21 | nabat נָבַט וַ/תַּבֵּ֥ט | nasa נָשָׂא נָשָׂ֣אתִי | 5 |  |
| 30 | Genesis 20:10 → Genesis 20:14 | ra'ah רָאָה רָאִ֔יתָ | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 31 | Genesis 21:9 → Genesis 21:14 | ra'ah רָאָה וַ/תֵּ֨רֶא | laqach לָקַח וַ/יִּֽקַּֽח | 5 |  |
| 32 | Genesis 21:19 → Genesis 21:14 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/יִּֽקַּֽח | 5 |  |
| 33 | Genesis 21:19 → Genesis 21:16 | ra'ah רָאָה וַ/תֵּ֖רֶא | nasa נָשָׂא וַ/תִּשָּׂ֥א | 3 |  |
| 34 | Genesis 21:16 → Genesis 21:21 | ra'ah רָאָה אֶרְאֶ֖ה | laqach לָקַח וַ/תִּֽקַּֽח | 5 |  |
| 35 | Genesis 22:8 → Genesis 22:3 | ra'ah רָאָה יִרְאֶה | laqach לָקַח וַ/יִּקַּ֞ח | 5 |  |
| 36 | Genesis 22:8 → Genesis 22:4 | ra'ah רָאָה יִרְאֶה | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 37 | Genesis 22:8 → Genesis 22:13 | ra'ah רָאָה יִרְאֶה | nasa נָשָׂא וַ/יִּשָּׂ֨א; achaz אָחַז נֶאֱחַ֥ז; laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 38 | Genesis 22:13 → Genesis 22:10 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּ֖ח | 3 |  |
| 39 | Genesis 22:14 → Genesis 22:10 | ra'ah רָאָה יִרְאֶ֑ה; ra'ah רָאָה יֵרָאֶֽה | laqach לָקַח וַ/יִּקַּ֖ח | 4 |  |
| 40 | Genesis 24:64 → Genesis 24:61 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/יִּקַּ֥ח | 3 |  |
| 41 | Genesis 24:63 → Genesis 24:67 | ra'ah רָאָה וַ/יַּ֔רְא | laqach לָקַח וַ/יִּקַּ֧ח | 4 |  |
| 42 | Genesis 24:63 → Genesis 25:1 | ra'ah רָאָה וַ/יַּ֔רְא | laqach לָקַח וַ/יִּקַּ֥ח | 5 |  |
| 43 | Genesis 24:64 → Genesis 24:67 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/יִּקַּ֧ח | 3 |  |
| 44 | Genesis 24:64 → Genesis 25:1 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/יִּקַּ֥ח | 4 |  |
| 45 | Genesis 28:6 → Genesis 28:1 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח תִקַּ֥ח | 5 |  |
| 46 | Genesis 28:6 → Genesis 28:2 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וְ/קַח | 4 |  |
| 47 | Genesis 28:6 → Genesis 28:9 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֡ח | 3 |  |
| 48 | Genesis 28:6 → Genesis 28:11 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּח֙ | 5 |  |
| 49 | Genesis 28:8 → Genesis 28:11 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּח֙ | 3 |  |
| 50 | Genesis 31:5 → Genesis 31:1 | ra'ah רָאָה רֹאֶ֤ה | laqach לָקַח לָקַ֣ח | 4 |  |
| 51 | Genesis 31:5 → Genesis 31:10 | ra'ah רָאָה רֹאֶ֤ה | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 52 | Genesis 31:12 → Genesis 31:17 | ra'ah רָאָה וּ/רְאֵה֙; ra'ah רָאָה רָאִ֔יתִי | nasa נָשָׂא וַ/יִּשָּׂ֛א | 5 |  |
| 53 | Genesis 31:42 → Genesis 31:45 | ra'ah רָאָה רָאָ֥ה | laqach לָקַח וַ/יִּקַּ֥ח | 3 |  |
| 54 | Genesis 31:42 → Genesis 31:46 | ra'ah רָאָה רָאָ֥ה | laqach לָקַח וַ/יִּקְח֥וּ | 4 |  |
| 55 | Genesis 31:43 → Genesis 31:46 | ra'ah רָאָה רֹאֶ֖ה | laqach לָקַח וַ/יִּקְח֥וּ | 3 |  |
| 56 | Genesis 31:49 → Genesis 31:45 | tsaphah צָפָה יִ֥צֶף | laqach לָקַח וַ/יִּקַּ֥ח | 4 |  |
| 57 | Genesis 31:50 → Genesis 31:45 | ra'ah רָאָה רְאֵ֕ה | laqach לָקַח וַ/יִּקַּ֥ח | 5 |  |
| 58 | Genesis 31:49 → Genesis 31:46 | tsaphah צָפָה יִ֥צֶף | laqach לָקַח וַ/יִּקְח֥וּ | 3 |  |
| 59 | Genesis 31:50 → Genesis 31:46 | ra'ah רָאָה רְאֵ֕ה | laqach לָקַח וַ/יִּקְח֥וּ | 4 |  |
| 60 | Genesis 32:26 → Genesis 32:21 | ra'ah רָאָה וַ/יַּ֗רְא | nasa נָשָׂא יִשָּׂ֥א | 5 |  |
| 61 | Genesis 32:21 → Genesis 32:24 | ra'ah רָאָה אֶרְאֶ֣ה | laqach לָקַח וַ/יִּקָּחֵ֔/ם | 3 |  |
| 62 | Genesis 32:26 → Genesis 32:23 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּ֞ח | 3 |  |
| 63 | Genesis 32:31 → Genesis 33:1 | ra'ah רָאָה רָאִ֤יתִי | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 64 | Genesis 33:5 → Genesis 33:1 | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 65 | Genesis 33:1 → Genesis 33:5 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֣א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 66 | Genesis 33:10 → Genesis 33:5 | ra'ah רָאָה רָאִ֣יתִי; ra'ah רָאָה כִּ/רְאֹ֛ת | nasa נָשָׂא וַ/יִּשָּׂ֣א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 67 | Genesis 33:5 → Genesis 33:10 | ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח וְ/לָקַחְתָּ֥ | 5 |  |
| 68 | Genesis 34:1 → Genesis 34:4 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח קַֽח | 3 |  |
| 69 | Genesis 35:1 → Genesis 34:28 | ra'ah רָאָה הַ/נִּרְאֶ֣ה | laqach לָקַח לָקָֽחוּ | 4 |  |
| 70 | Genesis 37:20 → Genesis 37:24 | ra'ah רָאָה וְ/נִרְאֶ֕ה | laqach לָקַח וַ/יִּ֨קָּחֻ֔/הוּ | 4 |  |
| 71 | Genesis 37:20 → Genesis 37:25 | ra'ah רָאָה וְ/נִרְאֶ֕ה | nasa נָשָׂא וַ/יִּשְׂא֤וּ; nasa נָשָׂא נֹֽשְׂאִ֗ים _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 72 | Genesis 38:2 → Genesis 38:6 | ra'ah רָאָה וַ/יַּרְא | laqach לָקַח וַ/יִּקַּ֧ח | 4 |  |
| 73 | Genesis 38:15 → Genesis 38:20 | ra'ah רָאָה וַ/יִּרְאֶ֣/הָ | laqach לָקַח לָ/קַ֥חַת | 5 |  |
| 74 | Genesis 39:3 → Genesis 38:28 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/תִּקַּ֣ח | 5 |  |
| 75 | Genesis 39:3 → Genesis 39:7 | ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא וַ/תִּשָּׂ֧א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 76 | Genesis 39:23 → Genesis 39:20 | ra'ah רָאָה רֹאֶ֤ה | laqach לָקַח וַ/יִּקַּח֩ | 3 |  |
| 77 | Genesis 40:6 → Genesis 40:11 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וָ/אֶקַּ֣ח | 5 |  |
| 78 | Genesis 40:16 → Genesis 40:11 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וָ/אֶקַּ֣ח | 5 |  |
| 79 | Genesis 40:16 → Genesis 40:13 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא יִשָּׂ֤א | 3 |  |
| 80 | Genesis 40:16 → Genesis 40:19 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא יִשָּׂ֨א | 3 |  |
| 81 | Genesis 40:16 → Genesis 40:20 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא וַ/יִּשָּׂ֞א | 4 |  |
| 82 | Genesis 42:12 → Genesis 42:16 | ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח וְ/יִקַּ֣ח | 4 |  |
| 83 | Genesis 42:21 → Genesis 42:16 | ra'ah רָאָה רָאִ֜ינוּ | laqach לָקַח וְ/יִקַּ֣ח | 5 |  |
| 84 | Genesis 42:21 → Genesis 42:24 | ra'ah רָאָה רָאִ֜ינוּ | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 85 | Genesis 42:21 → Genesis 42:26 | ra'ah רָאָה רָאִ֜ינוּ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 5 |  |
| 86 | Genesis 42:27 → Genesis 42:24 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 87 | Genesis 43:3 → Genesis 42:36 | ra'ah רָאָה תִרְא֣וּ | laqach לָקַח תִּקָּ֔חוּ | 5 |  |
| 88 | Genesis 43:16 → Genesis 43:11 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח קְח֞וּ | 5 |  |
| 89 | Genesis 43:16 → Genesis 43:12 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח קְח֣וּ | 4 |  |
| 90 | Genesis 43:16 → Genesis 43:13 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח קָ֑חוּ | 3 |  |
| 91 | Genesis 43:29 → Genesis 43:34 | ra'ah רָאָה וַ/יַּ֞רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א | 5 |  |
| 92 | Genesis 44:26 → Genesis 44:29 | ra'ah רָאָה לִ/רְאוֹת֙ | laqach לָקַח וּ/לְקַחְתֶּ֧ם | 3 |  |
| 93 | Genesis 44:34 → Genesis 44:29 | ra'ah רָאָה אֶרְאֶ֣ה | laqach לָקַח וּ/לְקַחְתֶּ֧ם | 5 |  |
| 94 | Genesis 45:13 → Genesis 45:18 | ra'ah רָאָה רְאִיתֶ֑ם | laqach לָקַח וּ/קְח֧וּ | 5 |  |
| 95 | Genesis 45:27 → Genesis 45:23 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא נֹשְׂאִ֖ים; nasa נָשָׂא נֹֽ֠שְׂאֹת | 4 |  |
| 96 | Genesis 45:28 → Genesis 45:23 | ra'ah רָאָה וְ/אֶרְאֶ֖/נּוּ | nasa נָשָׂא נֹשְׂאִ֖ים; nasa נָשָׂא נֹֽ֠שְׂאֹת | 5 |  |
| 97 | Genesis 45:28 → Genesis 46:5 | ra'ah רָאָה וְ/אֶרְאֶ֖/נּוּ | nasa נָשָׂא וַ/יִּשְׂא֨וּ; nasa נָשָׂא לָ/שֵׂ֥את | 5 |  |
| 98 | Genesis 48:3 → Genesis 47:30 | ra'ah רָאָה נִרְאָֽה | nasa נָשָׂא וּ/נְשָׂאתַ֨/נִי֙ | 4 |  |
| 99 | Genesis 48:8 → Genesis 48:13 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 100 | Genesis 48:10 → Genesis 48:13 | ra'ah רָאָה לִ/רְא֑וֹת | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 101 | Genesis 48:17 → Genesis 48:13 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 102 | Genesis 48:17 → Genesis 48:22 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח לָקַ֨חְתִּי֙ | 5 |  |
| 103 | Exodus 2:5 → Exodus 2:1 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/יִּקַּ֖ח | 4 |  |
| 104 | Exodus 2:6 → Exodus 2:1 | ra'ah רָאָה וַ/תִּרְאֵ֣/הוּ | laqach לָקַח וַ/יִּקַּ֖ח | 5 |  |
| 105 | Exodus 2:2 → Exodus 2:5 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּקָּחֶֽ/הָ | 3 |  |
| 106 | Exodus 2:6 → Exodus 2:3 | ra'ah רָאָה וַ/תִּרְאֵ֣/הוּ | laqach לָקַח וַ/תִּֽקַּֽח | 3 |  |
| 107 | Exodus 2:5 → Exodus 2:9 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּקַּ֧ח | 4 |  |
| 108 | Exodus 2:6 → Exodus 2:9 | ra'ah רָאָה וַ/תִּרְאֵ֣/הוּ | laqach לָקַח וַ/תִּקַּ֧ח | 3 |  |
| 109 | Exodus 2:12 → Exodus 2:9 | ra'ah רָאָה וַ/יַּ֖רְא | laqach לָקַח וַ/תִּקַּ֧ח | 3 |  |
| 110 | Exodus 4:1 → Exodus 4:4 | ra'ah רָאָה נִרְאָ֥ה | achaz אָחַז וֶ/אֱחֹ֖ז | 3 |  |
| 111 | Exodus 4:5 → Exodus 4:9 | ra'ah רָאָה נִרְאָ֥ה | laqach לָקַח וְ/לָקַחְתָּ֙; laqach לָקַח תִּקַּ֣ח | 4 |  |
| 112 | Exodus 4:14 → Exodus 4:9 | ra'ah רָאָה וְ/רָאֲ/ךָ֖ | laqach לָקַח וְ/לָקַחְתָּ֙; laqach לָקַח תִּקַּ֣ח | 5 |  |
| 113 | Exodus 4:14 → Exodus 4:17 | ra'ah רָאָה וְ/רָאֲ/ךָ֖ | laqach לָקַח תִּקַּ֣ח | 3 |  |
| 114 | Exodus 4:21 → Exodus 4:17 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח תִּקַּ֣ח | 4 |  |
| 115 | Exodus 4:21 → Exodus 4:25 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וַ/תִּקַּ֨ח | 4 |  |
| 116 | Exodus 6:3 → Exodus 6:7 | ra'ah רָאָה וָ/אֵרָ֗א | laqach לָקַח וְ/לָקַחְתִּ֨י | 4 |  |
| 117 | Exodus 6:3 → Exodus 6:8 | ra'ah רָאָה וָ/אֵרָ֗א | nasa נָשָׂא נָשָׂ֨אתִי֙ | 5 |  |
| 118 | Exodus 10:10 → Exodus 10:13 | ra'ah רָאָה רְא֕וּ | nasa נָשָׂא נָשָׂ֖א | 3 |  |
| 119 | Exodus 10:23 → Exodus 10:19 | ra'ah רָאָה רָא֞וּ | nasa נָשָׂא וַ/יִּשָּׂא֙ | 4 |  |
| 120 | Exodus 10:23 → Exodus 10:26 | ra'ah רָאָה רָא֞וּ | laqach לָקַח נִקַּ֔ח | 3 |  |
| 121 | Exodus 10:29 → Exodus 10:26 | ra'ah רָאָה רְא֥וֹת | laqach לָקַח נִקַּ֔ח | 3 |  |
| 122 | Exodus 14:13 → Exodus 14:10 | ra'ah רָאָה וּ/רְאוּ֙; ra'ah רָאָה רְאִיתֶ֤ם; ra'ah רָאָה לִ/רְאֹתָ֥/ם | nasa נָשָׂא וַ/יִּשְׂאוּ֩ _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 123 | Exodus 16:29 → Exodus 16:33 | ra'ah רָאָה רְא֗וּ | laqach לָקַח קַ֚ח | 4 |  |
| 124 | Exodus 23:5 → Exodus 23:1 | ra'ah רָאָה תִרְאֶ֞ה | nasa נָשָׂא תִשָּׂ֖א | 4 |  |
| 125 | Exodus 23:5 → Exodus 23:8 | ra'ah רָאָה תִרְאֶ֞ה | laqach לָקַח תִקָּ֑ח | 3 |  |
| 126 | Exodus 23:17 → Exodus 23:21 | ra'ah רָאָה יֵרָאֶה֙ | nasa נָשָׂא יִשָּׂא֙ | 4 |  |
| 127 | Exodus 24:10 → Exodus 24:6 | ra'ah רָאָה וַ/יִּרְא֕וּ | laqach לָקַח וַ/יִּקַּ֤ח | 4 |  |
| 128 | Exodus 24:11 → Exodus 24:6 | chazah חָזָה וַֽ/יֶּחֱזוּ֙ | laqach לָקַח וַ/יִּקַּ֤ח | 5 |  |
| 129 | Exodus 24:10 → Exodus 24:7 | ra'ah רָאָה וַ/יִּרְא֕וּ | laqach לָקַח וַ/יִּקַּח֙ | 3 |  |
| 130 | Exodus 24:11 → Exodus 24:7 | chazah חָזָה וַֽ/יֶּחֱזוּ֙ | laqach לָקַח וַ/יִּקַּח֙ | 4 |  |
| 131 | Exodus 24:11 → Exodus 24:8 | chazah חָזָה וַֽ/יֶּחֱזוּ֙ | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 132 | Exodus 25:9 → Exodus 25:14 | ra'ah רָאָה מַרְאֶ֣ה | nasa נָשָׂא לָ/שֵׂ֥את | 5 |  |
| 133 | Exodus 32:1 → Exodus 32:4 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 134 | Exodus 32:9 → Exodus 32:4 | ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 135 | Exodus 32:25 → Exodus 32:20 | ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח וַ/יִּקַּ֞ח | 5 |  |
| 136 | Exodus 33:10 → Exodus 33:7 | ra'ah רָאָה וְ/רָאָ֤ה | laqach לָקַח יִקַּ֨ח | 3 |  |
| 137 | Exodus 33:12 → Exodus 33:7 | ra'ah רָאָה רְ֠אֵה | laqach לָקַח יִקַּ֨ח | 5 |  |
| 138 | Exodus 33:23 → Exodus 34:4 | ra'ah רָאָה וְ/רָאִ֖יתָ; ra'ah רָאָה יֵרָאֽוּ | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 139 | Exodus 34:3 → Exodus 34:7 | ra'ah רָאָה יֵרָ֖א | nasa נָשָׂא נֹשֵׂ֥א | 4 |  |
| 140 | Exodus 34:10 → Exodus 34:7 | ra'ah רָאָה וְ/רָאָ֣ה | nasa נָשָׂא נֹשֵׂ֥א | 3 |  |
| 141 | Exodus 34:20 → Exodus 34:16 | ra'ah רָאָה יֵרָא֥וּ | laqach לָקַח וְ/לָקַחְתָּ֥ | 4 |  |
| 142 | Exodus 34:35 → Exodus 35:5 | ra'ah רָאָה וְ/רָא֤וּ | laqach לָקַח קְח֨וּ | 5 |  |
| 143 | Exodus 35:30 → Exodus 35:26 | ra'ah רָאָה רְא֛וּ | nasa נָשָׂא נָשָׂ֥א | 4 |  |
| 144 | Leviticus 9:6 → Leviticus 9:2 | ra'ah רָאָה וְ/יֵרָ֥א | laqach לָקַח קַח | 4 |  |
| 145 | Leviticus 9:6 → Leviticus 9:3 | ra'ah רָאָה וְ/יֵרָ֥א | laqach לָקַח קְח֤וּ | 3 |  |
| 146 | Leviticus 9:23 → Leviticus 10:4 | ra'ah רָאָה וַ/יֵּרָ֥א | nasa נָשָׂא שְׂא֤וּ | 5 |  |
| 147 | Leviticus 9:24 → Leviticus 10:4 | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא שְׂא֤וּ | 4 |  |
| 148 | Leviticus 9:24 → Leviticus 10:5 | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא וַ/יִּשָּׂאֻ/ם֙ | 5 |  |
| 149 | Leviticus 13:3 → Leviticus 12:8 | ra'ah רָאָה וְ/רָאָ֣ה; ra'ah רָאָה וְ/רָאָ֥/הוּ | laqach לָקַח וְ/לָקְחָ֣ה | 3 |  |
| 150 | Leviticus 13:5 → Leviticus 12:8 | ra'ah רָאָה וְ/רָאָ֣/הוּ | laqach לָקַח וְ/לָקְחָ֣ה | 5 |  |
| 151 | Leviticus 14:3 → Leviticus 14:6 | ra'ah רָאָה וְ/רָאָה֙ | laqach לָקַח יִקַּ֣ח | 3 |  |
| 152 | Leviticus 14:37 → Leviticus 14:42 | ra'ah רָאָה וְ/רָאָ֣ה | laqach לָקַח וְ/לָקְחוּ֙; laqach לָקַח יִקַּ֖ח | 5 |  |
| 153 | Leviticus 14:39 → Leviticus 14:42 | ra'ah רָאָה וְ/רָאָ֕ה | laqach לָקַח וְ/לָקְחוּ֙; laqach לָקַח יִקַּ֖ח | 3 |  |
| 154 | Leviticus 14:44 → Leviticus 14:49 | ra'ah רָאָה וְ/רָאָ֕ה | laqach לָקַח וְ/לָקַ֛ח | 5 |  |
| 155 | Leviticus 14:48 → Leviticus 14:51 | ra'ah רָאָה וְ/רָאָה֙ | laqach לָקַח וְ/לָקַ֣ח | 3 |  |
| 156 | Leviticus 16:2 → Leviticus 16:5 | ra'ah רָאָה אֵרָאֶ֖ה | laqach לָקַח יִקַּ֛ח | 3 |  |
| 157 | Leviticus 16:2 → Leviticus 16:7 | ra'ah רָאָה אֵרָאֶ֖ה | laqach לָקַח וְ/לָקַ֖ח | 5 |  |
| 158 | Leviticus 20:17 → Leviticus 20:14 | ra'ah רָאָה וְ/רָאָ֨ה; ra'ah רָאָה תִרְאֶ֤ה | laqach לָקַח יִקַּ֧ח | 3 |  |
| 159 | Leviticus 20:17 → Leviticus 20:20 | ra'ah רָאָה וְ/רָאָ֨ה; ra'ah רָאָה תִרְאֶ֤ה | nasa נָשָׂא יִשָּׂ֖אוּ | 3 |  |
| 160 | Leviticus 20:17 → Leviticus 20:21 | ra'ah רָאָה וְ/רָאָ֨ה; ra'ah רָאָה תִרְאֶ֤ה | laqach לָקַח יִקַּ֛ח | 4 |  |
| 161 | Numbers 4:20 → Numbers 4:15 | ra'ah רָאָה לִ/רְא֛וֹת | nasa נָשָׂא לָ/שֵׂ֔את | 5 |  |
| 162 | Numbers 4:20 → Numbers 4:25 | ra'ah רָאָה לִ/רְא֛וֹת | nasa נָשָׂא וְ/נָ֨שְׂא֜וּ | 5 |  |
| 163 | Numbers 8:4 → Numbers 8:8 | ra'ah רָאָה הֶרְאָ֤ה | laqach לָקַח וְ/לָֽקְחוּ֙; laqach לָקַח תִּקַּ֥ח | 4 |  |
| 164 | Numbers 11:15 → Numbers 11:12 | ra'ah רָאָה אֶרְאֶ֖ה | nasa נָשָׂא שָׂאֵ֣/הוּ; nasa נָשָׂא יִשָּׂ֤א | 3 |  |
| 165 | Numbers 13:18 → Numbers 13:23 | ra'ah רָאָה וּ/רְאִיתֶ֥ם | nasa נָשָׂא וַ/יִּשָּׂאֻ֥/הוּ | 5 |  |
| 166 | Numbers 13:26 → Numbers 13:23 | ra'ah רָאָה וַ/יַּרְא֖וּ/ם | nasa נָשָׂא וַ/יִּשָּׂאֻ֥/הוּ | 3 |  |
| 167 | Numbers 13:28 → Numbers 13:23 | ra'ah רָאָה רָאִ֥ינוּ | nasa נָשָׂא וַ/יִּשָּׂאֻ֥/הוּ | 5 |  |
| 168 | Numbers 14:14 → Numbers 14:18 | ra'ah רָאָה נִרְאָ֣ה | nasa נָשָׂא נֹשֵׂ֥א | 4 |  |
| 169 | Numbers 14:14 → Numbers 14:19 | ra'ah רָאָה נִרְאָ֣ה | nasa נָשָׂא נָשָׂ֨אתָה֙ | 5 |  |
| 170 | Numbers 14:22 → Numbers 14:18 | ra'ah רָאָה הָ/רֹאִ֤ים | nasa נָשָׂא נֹשֵׂ֥א | 4 |  |
| 171 | Numbers 14:23 → Numbers 14:18 | ra'ah רָאָה יִרְאוּ֙; ra'ah רָאָה יִרְאֽוּ/הָ | nasa נָשָׂא נֹשֵׂ֥א | 5 |  |
| 172 | Numbers 14:22 → Numbers 14:19 | ra'ah רָאָה הָ/רֹאִ֤ים | nasa נָשָׂא נָשָׂ֨אתָה֙ | 3 |  |
| 173 | Numbers 14:23 → Numbers 14:19 | ra'ah רָאָה יִרְאוּ֙; ra'ah רָאָה יִרְאֽוּ/הָ | nasa נָשָׂא נָשָׂ֨אתָה֙ | 4 |  |
| 174 | Numbers 15:39 → Numbers 16:1 | ra'ah רָאָה וּ/רְאִיתֶ֣ם | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 175 | Numbers 15:39 → Numbers 16:3 | ra'ah רָאָה וּ/רְאִיתֶ֣ם | nasa נָשָׂא תִּֽתְנַשְּׂא֖וּ | 5 |  |
| 176 | Numbers 16:19 → Numbers 16:15 | ra'ah רָאָה וַ/יֵּרָ֥א | nasa נָשָׂא נָשָׂ֔אתִי | 4 |  |
| 177 | Numbers 17:7 → Numbers 17:4 | ra'ah רָאָה וַ/יֵּרָ֖א | laqach לָקַח וַ/יִּקַּ֞ח | 3 |  |
| 178 | Numbers 17:7 → Numbers 17:11 | ra'ah רָאָה וַ/יֵּרָ֖א | laqach לָקַח קַ֣ח | 4 |  |
| 179 | Numbers 17:7 → Numbers 17:12 | ra'ah רָאָה וַ/יֵּרָ֖א | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 180 | Numbers 17:24 → Numbers 18:1 | ra'ah רָאָה וַ/יִּרְא֥וּ | nasa נָשָׂא תִּשְׂא֖וּ; nasa נָשָׂא תִּשְׂא֖וּ | 5 |  |
| 181 | Numbers 20:6 → Numbers 20:9 | ra'ah רָאָה וַ/יֵּרָ֥א | laqach לָקַח וַ/יִּקַּ֥ח | 3 |  |
| 182 | Numbers 20:29 → Numbers 20:25 | ra'ah רָאָה וַ/יִּרְאוּ֙ | laqach לָקַח קַ֚ח | 4 |  |
| 183 | Numbers 21:20 → Numbers 21:25 | shaqaph שָׁקַף וְ/נִשְׁקָ֖פָה | laqach לָקַח וַ/יִּקַּח֙ | 5 |  |
| 184 | Numbers 22:2 → Numbers 21:32 | ra'ah רָאָה וַ/יַּ֥רְא | lakad לָכַד וַֽ/יִּלְכְּד֖וּ | 5 |  |
| 185 | Numbers 23:3 → Numbers 22:41 | ra'ah רָאָה יַּרְאֵ֖/נִי | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 186 | Numbers 23:3 → Numbers 23:7 | ra'ah רָאָה יַּרְאֵ֖/נִי | nasa נָשָׂא וַ/יִּשָּׂ֥א | 4 |  |
| 187 | Numbers 23:9 → Numbers 23:14 | ra'ah רָאָה אֶרְאֶ֔/נּוּ; shur שׁוּר אֲשׁוּרֶ֑/נּוּ | laqach לָקַח וַ/יִּקָּחֵ֨/הוּ֙ | 5 |  |
| 188 | Numbers 23:13 → Numbers 23:18 | ra'ah רָאָה תִּרְאֶ֣/נּוּ; ra'ah רָאָה תִרְאֶ֔ה; ra'ah רָאָה תִרְאֶ֑ה | nasa נָשָׂא וַ/יִּשָּׂ֥א | 5 |  |
| 189 | Numbers 23:21 → Numbers 23:18 | nabat נָבַט הִבִּ֥יט; ra'ah רָאָה רָאָ֥ה | nasa נָשָׂא וַ/יִּשָּׂ֥א | 3 |  |
| 190 | Numbers 23:21 → Numbers 23:24 | nabat נָבַט הִבִּ֥יט; ra'ah רָאָה רָאָ֥ה | nasa נָשָׂא יִתְנַשָּׂ֑א | 3 |  |
| 191 | Numbers 23:28 → Numbers 23:24 | shaqaph שָׁקַף הַ/נִּשְׁקָ֖ף | nasa נָשָׂא יִתְנַשָּׂ֑א | 4 |  |
| 192 | Numbers 24:1 → Numbers 23:27 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח אֶקָּ֣חֲ/ךָ֔ | 4 |  |
| 193 | Numbers 24:2 → Numbers 23:27 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח אֶקָּ֣חֲ/ךָ֔ | 5 |  |
| 194 | Numbers 24:1 → Numbers 23:28 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֥ח | 3 |  |
| 195 | Numbers 24:2 → Numbers 23:28 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח וַ/יִּקַּ֥ח | 4 |  |
| 196 | Numbers 23:28 → Numbers 24:2 | shaqaph שָׁקַף הַ/נִּשְׁקָ֖ף | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 197 | Numbers 23:28 → Numbers 24:3 | shaqaph שָׁקַף הַ/נִּשְׁקָ֖ף | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 198 | Numbers 24:2 → Numbers 24:7 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וְ/תִנַּשֵּׂ֖א | 5 |  |
| 199 | Numbers 24:4 → Numbers 24:7 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וְ/תִנַּשֵּׂ֖א | 3 |  |
| 200 | Numbers 24:20 → Numbers 24:15 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 201 | Numbers 24:16 → Numbers 24:20 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֥א | 4 |  |
| 202 | Numbers 24:16 → Numbers 24:21 | chazah חָזָה יֶֽחֱזֶ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֥א | 5 |  |
| 203 | Numbers 24:17 → Numbers 24:20 | ra'ah רָאָה אֶרְאֶ֨/נּוּ֙; shur שׁוּר אֲשׁוּרֶ֖/נּוּ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 3 |  |
| 204 | Numbers 24:17 → Numbers 24:21 | ra'ah רָאָה אֶרְאֶ֨/נּוּ֙; shur שׁוּר אֲשׁוּרֶ֖/נּוּ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 4 |  |
| 205 | Numbers 24:20 → Numbers 24:23 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 3 |  |
| 206 | Numbers 25:7 → Numbers 25:4 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח קַ֚ח | 3 |  |
| 207 | Numbers 27:13 → Numbers 27:18 | ra'ah רָאָה וְ/רָאִ֣יתָה | laqach לָקַח קַח | 5 |  |
| 208 | Numbers 32:1 → Numbers 31:51 | ra'ah רָאָה וַ/יִּרְא֞וּ | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 209 | Deuteronomy 1:8 → Deuteronomy 1:12 | ra'ah רָאָה רְאֵ֛ה | nasa נָשָׂא אֶשָּׂ֖א | 4 |  |
| 210 | Deuteronomy 1:19 → Deuteronomy 1:15 | ra'ah רָאָה רְאִיתֶ֗ם | laqach לָקַח וָ/אֶקַּ֞ח | 4 |  |
| 211 | Deuteronomy 1:19 → Deuteronomy 1:23 | ra'ah רָאָה רְאִיתֶ֗ם | laqach לָקַח וָ/אֶקַּ֤ח | 4 |  |
| 212 | Deuteronomy 1:21 → Deuteronomy 1:25 | ra'ah רָאָה רְ֠אֵה | laqach לָקַח וַ/יִּקְח֤וּ | 4 |  |
| 213 | Deuteronomy 1:28 → Deuteronomy 1:23 | ra'ah רָאָה רָאִ֥ינוּ | laqach לָקַח וָ/אֶקַּ֤ח | 5 |  |
| 214 | Deuteronomy 1:28 → Deuteronomy 1:25 | ra'ah רָאָה רָאִ֥ינוּ | laqach לָקַח וַ/יִּקְח֤וּ | 3 |  |
| 215 | Deuteronomy 1:28 → Deuteronomy 1:31 | ra'ah רָאָה רָאִ֥ינוּ | nasa נָשָׂא נְשָׂאֲ/ךָ֙; nasa נָשָׂא יִשָּׂא | 3 |  |
| 216 | Deuteronomy 1:35 → Deuteronomy 1:31 | ra'ah רָאָה יִרְאֶ֥ה | nasa נָשָׂא נְשָׂאֲ/ךָ֙; nasa נָשָׂא יִשָּׂא | 4 |  |
| 217 | Deuteronomy 1:36 → Deuteronomy 1:31 | ra'ah רָאָה יִרְאֶ֔/נָּה | nasa נָשָׂא נְשָׂאֲ/ךָ֙; nasa נָשָׂא יִשָּׂא | 5 |  |
| 218 | Deuteronomy 2:31 → Deuteronomy 2:34 | ra'ah רָאָה רְאֵ֗ה | lakad לָכַד וַ/נִּלְכֹּ֤ד | 3 |  |
| 219 | Deuteronomy 2:31 → Deuteronomy 2:35 | ra'ah רָאָה רְאֵ֗ה | lakad לָכַד לָכָֽדְנוּ | 4 |  |
| 220 | Deuteronomy 3:24 → Deuteronomy 3:27 | ra'ah רָאָה לְ/הַרְא֣וֹת | nasa נָשָׂא וְ/שָׂ֥א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 221 | Deuteronomy 4:3 → Deuteronomy 3:27 | ra'ah רָאָה הָֽ/רֹאֹ֔ת | nasa נָשָׂא וְ/שָׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 222 | Deuteronomy 4:15 → Deuteronomy 4:19 | ra'ah רָאָה רְאִיתֶם֙ | nasa נָשָׂא תִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 223 | Deuteronomy 4:15 → Deuteronomy 4:20 | ra'ah רָאָה רְאִיתֶם֙ | laqach לָקַח לָקַ֣ח | 5 |  |
| 224 | Deuteronomy 9:13 → Deuteronomy 9:9 | ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח לָ/קַ֜חַת | 4 |  |
| 225 | Deuteronomy 9:13 → Deuteronomy 9:17 | ra'ah רָאָה רָאִ֨יתִי֙ | taphas תָּפַשׂ וָ/אֶתְפֹּשׂ֙ | 4 |  |
| 226 | Deuteronomy 9:16 → Deuteronomy 9:21 | ra'ah רָאָה וָ/אֵ֗רֶא | laqach לָקַח לָקַחְתִּי֮ | 5 |  |
| 227 | Deuteronomy 10:21 → Deuteronomy 10:17 | ra'ah רָאָה רָא֖וּ | nasa נָשָׂא יִשָּׂ֣א; laqach לָקַח יִקַּ֖ח | 4 |  |
| 228 | Deuteronomy 16:16 → Deuteronomy 16:19 | ra'ah רָאָה יֵרָאֶ֨ה; ra'ah רָאָה יֵרָאֶ֛ה | laqach לָקַח תִקַּ֣ח | 3 |  |
| 229 | Deuteronomy 21:7 → Deuteronomy 21:3 | ra'ah רָאָה רָאֽוּ | laqach לָקַח וְ/לָֽקְח֡וּ | 4 |  |
| 230 | Deuteronomy 21:7 → Deuteronomy 21:11 | ra'ah רָאָה רָאֽוּ | laqach לָקַח וְ/לָקַחְתָּ֥ | 4 | chashaq חָשַׁק (Deuteronomy 21:11) |
| 231 | Deuteronomy 22:1 → Deuteronomy 21:19 | ra'ah רָאָה תִרְאֶה֩ | taphas תָּפַשׂ וְ/תָ֥פְשׂוּ | 5 |  |
| 232 | Deuteronomy 22:1 → Deuteronomy 22:6 | ra'ah רָאָה תִרְאֶה֩ | laqach לָקַח תִקַּ֥ח | 5 |  |
| 233 | Deuteronomy 22:4 → Deuteronomy 22:7 | ra'ah רָאָה תִרְאֶה֩ | laqach לָקַח תִּֽקַּֽח | 3 |  |
| 234 | Deuteronomy 26:7 → Deuteronomy 26:2 | ra'ah רָאָה וַ/יַּ֧רְא | laqach לָקַח וְ/לָקַחְתָּ֞ | 5 |  |
| 235 | Deuteronomy 26:7 → Deuteronomy 26:4 | ra'ah רָאָה וַ/יַּ֧רְא | laqach לָקַח וְ/לָקַ֧ח | 3 |  |
| 236 | Deuteronomy 28:32 → Deuteronomy 28:29 | ra'ah רָאָה רֹא֔וֹת | gazal גָּזַל וְ/גָז֛וּל | 3 |  |
| 237 | Deuteronomy 28:34 → Deuteronomy 28:29 | ra'ah רָאָה תִּרְאֶֽה | gazal גָּזַל וְ/גָז֛וּל | 5 |  |
| 238 | Deuteronomy 28:34 → Deuteronomy 28:31 | ra'ah רָאָה תִּרְאֶֽה | gazal גָּזַל גָּז֣וּל | 3 |  |
| 239 | Deuteronomy 29:2 → Deuteronomy 29:7 | ra'ah רָאָה רָא֖וּ | laqach לָקַח וַ/נִּקַּח֙ | 5 |  |
| 240 | Deuteronomy 29:3 → Deuteronomy 29:7 | ra'ah רָאָה לִ/רְא֖וֹת | laqach לָקַח וַ/נִּקַּח֙ | 4 |  |
| 241 | Deuteronomy 30:15 → Deuteronomy 30:12 | ra'ah רָאָה רְאֵ֨ה | laqach לָקַח וְ/יִקָּחֶ֣/הָ | 3 |  |
| 242 | Deuteronomy 32:36 → Deuteronomy 32:40 | ra'ah רָאָה יִרְאֶה֙ | nasa נָשָׂא אֶשָּׂ֥א | 4 |  |
| 243 | Deuteronomy 32:36 → Deuteronomy 32:41 | ra'ah רָאָה יִרְאֶה֙ | achaz אָחַז וְ/תֹאחֵ֥ז | 5 |  |
| 244 | Deuteronomy 32:52 → Deuteronomy 33:3 | ra'ah רָאָה תִּרְאֶ֣ה | nasa נָשָׂא יִשָּׂ֖א | 3 |  |
| 245 | Joshua 2:1 → Joshua 2:4 | ra'ah רָאָה רְא֥וּ | laqach לָקַח וַ/תִּקַּ֧ח | 3 |  |
| 246 | Joshua 3:3 → Joshua 3:6 | ra'ah רָאָה כִּ/רְאֽוֹתְ/כֶ֗ם | nasa נָשָׂא שְׂאוּ֙; nasa נָשָׂא וַ/יִּשְׂאוּ֙ | 3 |  |
| 247 | Joshua 3:3 → Joshua 3:8 | ra'ah רָאָה כִּ/רְאֽוֹתְ/כֶ֗ם | nasa נָשָׂא נֹשְׂאֵ֥י | 5 |  |
| 248 | Joshua 6:2 → Joshua 5:13 | ra'ah רָאָה רְאֵה֙ | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 249 | Joshua 6:2 → Joshua 6:6 | ra'ah רָאָה רְאֵה֙ | nasa נָשָׂא שְׂא֖וּ; nasa נָשָׂא יִשְׂאוּ֙ | 4 |  |
| 250 | Joshua 7:21 → Joshua 7:16 | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | lakad לָכַד וַ/יִּלָּכֵ֖ד | 5 | chamad חָמַד (Joshua 7:21) |
| 251 | Joshua 7:21 → Joshua 7:17 | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | lakad לָכַד וַ/יִּלְכֹּ֕ד; lakad לָכַד וַ/יִּלָּכֵ֖ד | 4 | chamad חָמַד (Joshua 7:21) |
| 252 | Joshua 7:21 → Joshua 7:18 | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | lakad לָכַד וַ/יִּלָּכֵ֗ד | 3 | chamad חָמַד (Joshua 7:21) |
| 253 | Joshua 7:21 → Joshua 7:24 | ra'ah רָאָה ו/אראה; ra'ah רָאָה וָ/אֵ֣רֶא | laqach לָקַח וַ/יִּקַּ֣ח | 3 | chamad חָמַד (Joshua 7:21) |
| 254 | Joshua 8:1 → Joshua 7:23 | ra'ah רָאָה רְאֵ֣ה | laqach לָקַח וַ/יִּקָּחוּ/ם֙ | 4 |  |
| 255 | Joshua 8:1 → Joshua 7:24 | ra'ah רָאָה רְאֵ֣ה | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 256 | Joshua 8:4 → Joshua 8:1 | ra'ah רָאָה רְ֠אוּ | laqach לָקַח קַ֣ח | 3 |  |
| 257 | Joshua 8:4 → Joshua 8:8 | ra'ah רָאָה רְ֠אוּ | taphas תָּפַשׂ כְּ/תָפְשְׂ/כֶ֣ם | 4 |  |
| 258 | Joshua 8:8 → Joshua 8:12 | ra'ah רָאָה רְא֖וּ | laqach לָקַח וַ/יִּקַּ֕ח | 4 |  |
| 259 | Joshua 8:14 → Joshua 8:19 | ra'ah רָאָה כִּ/רְא֣וֹת | lakad לָכַד וַֽ/יִּלְכְּד֑וּ/הָ | 5 |  |
| 260 | Joshua 8:20 → Joshua 8:23 | ra'ah רָאָה וַ/יִּרְא֗וּ | taphas תָּפַשׂ תָּ֣פְשׂוּ | 3 |  |
| 261 | Joshua 24:7 → Joshua 24:3 | ra'ah רָאָה וַ/תִּרְאֶ֨ינָה֙ | laqach לָקַח וָ֠/אֶקַּח | 4 |  |
| 262 | Judges 2:7 → Judges 2:4 | ra'ah רָאָה רָא֗וּ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 3 |  |
| 263 | Judges 3:24 → Judges 3:21 | ra'ah רָאָה וַ/יִּרְא֕וּ | laqach לָקַח וַ/יִּקַּח֙ | 3 |  |
| 264 | Judges 3:24 → Judges 3:28 | ra'ah רָאָה וַ/יִּרְא֕וּ | lakad לָכַד וַֽ/יִּלְכְּד֞וּ | 4 |  |
| 265 | Judges 6:22 → Judges 6:25 | ra'ah רָאָה וַ/יַּ֣רְא; ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח קַ֤ח | 3 |  |
| 266 | Judges 6:22 → Judges 6:26 | ra'ah רָאָה וַ/יַּ֣רְא; ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח וְ/לָֽקַחְתָּ֙ | 4 |  |
| 267 | Judges 6:22 → Judges 6:27 | ra'ah רָאָה וַ/יַּ֣רְא; ra'ah רָאָה רָאִ֨יתִי֙ | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 268 | Judges 9:48 → Judges 9:43 | ra'ah רָאָה רְאִיתֶם֙ | laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 269 | Judges 9:43 → Judges 9:48 | ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וַ/יִּקַּח֩; nasa נָשָׂא וַ/יִּ֨שָּׂאֶ֔/הָ | 5 |  |
| 270 | Judges 9:48 → Judges 9:45 | ra'ah רָאָה רְאִיתֶם֙ | lakad לָכַד וַ/יִּלְכֹּד֙ | 3 |  |
| 271 | Judges 9:55 → Judges 9:50 | ra'ah רָאָה וַ/יִּרְא֥וּ | lakad לָכַד וַֽ/יִּלְכְּדָֽ/הּ | 5 |  |
| 272 | Judges 12:3 → Judges 12:6 | ra'ah רָאָה וָֽ/אֶרְאֶ֞ה | achaz אָחַז וַ/יֹּאחֲז֣וּ | 3 |  |
| 273 | Judges 13:22 → Judges 13:19 | ra'ah רָאָה רָאִֽינוּ | laqach לָקַח וַ/יִּקַּ֨ח | 3 |  |
| 274 | Judges 13:23 → Judges 13:19 | ra'ah רָאָה הֶרְאָ֖/נוּ | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 275 | Judges 13:19 → Judges 13:23 | ra'ah רָאָה רֹאִֽים | laqach לָקַח לָקַ֤ח | 4 |  |
| 276 | Judges 13:20 → Judges 13:23 | ra'ah רָאָה רֹאִ֔ים | laqach לָקַח לָקַ֤ח | 3 |  |
| 277 | Judges 13:22 → Judges 14:2 | ra'ah רָאָה רָאִֽינוּ | laqach לָקַח קְחוּ | 5 |  |
| 278 | Judges 14:1 → Judges 13:23 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח לָקַ֤ח | 3 |  |
| 279 | Judges 14:2 → Judges 13:23 | ra'ah רָאָה רָאִ֥יתִי | laqach לָקַח לָקַ֤ח | 4 |  |
| 280 | Judges 13:23 → Judges 14:2 | ra'ah רָאָה הֶרְאָ֖/נוּ | laqach לָקַח קְחוּ | 4 |  |
| 281 | Judges 13:23 → Judges 14:3 | ra'ah רָאָה הֶרְאָ֖/נוּ | laqach לָקַח לָ/קַ֣חַת; laqach לָקַח קַֽח | 5 |  |
| 282 | Judges 14:8 → Judges 14:3 | ra'ah רָאָה לִ/רְא֔וֹת | laqach לָקַח לָ/קַ֣חַת; laqach לָקַח קַֽח | 5 |  |
| 283 | Judges 14:11 → Judges 14:8 | ra'ah רָאָה כִּ/רְאוֹתָ֣/ם | laqach לָקַח לְ/קַחְתָּ֔/הּ | 3 |  |
| 284 | Judges 14:8 → Judges 14:11 | ra'ah רָאָה לִ/רְא֔וֹת | laqach לָקַח וַ/יִּקְחוּ֙ | 3 |  |
| 285 | Judges 16:18 → Judges 16:21 | ra'ah רָאָה וַ/תֵּ֣רֶא | achaz אָחַז וַ/יֹּאחֲז֣וּ/הוּ | 3 |  |
| 286 | Judges 16:24 → Judges 16:21 | ra'ah רָאָה וַ/יִּרְא֤וּ | achaz אָחַז וַ/יֹּאחֲז֣וּ/הוּ | 3 |  |
| 287 | Judges 16:27 → Judges 16:31 | ra'ah רָאָה הָ/רֹאִ֖ים | nasa נָשָׂא וַ/יִּשְׂא֣וּ | 4 |  |
| 288 | Ruth 1:18 → Ruth 1:14 | ra'ah רָאָה וַ/תֵּ֕רֶא | nasa נָשָׂא וַ/תִּשֶּׂ֣נָה | 4 |  |
| 289 | 1 Samuel 2:32 → 1 Samuel 2:28 | nabat נָבַט וְ/הִבַּטְתָּ֙ | nasa נָשָׂא לָ/שֵׂ֥את | 4 |  |
| 290 | 1 Samuel 3:21 → 1 Samuel 4:3 | ra'ah רָאָה לְ/הֵרָאֹ֣ה | laqach לָקַח נִקְחָ֧ה | 3 |  |
| 291 | 1 Samuel 3:21 → 1 Samuel 4:4 | ra'ah רָאָה לְ/הֵרָאֹ֣ה | nasa נָשָׂא וַ/יִּשְׂא֣וּ | 4 |  |
| 292 | 1 Samuel 4:15 → 1 Samuel 4:11 | ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח נִלְקָ֑ח | 4 |  |
| 293 | 1 Samuel 4:13 → 1 Samuel 4:17 | tsaphah צָפָה מְצַפֶּ֔ה | laqach לָקַח נִלְקָֽחָה | 4 |  |
| 294 | 1 Samuel 4:15 → 1 Samuel 4:19 | ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח הִלָּקַח֙ | 4 |  |
| 295 | 1 Samuel 5:7 → 1 Samuel 5:2 | ra'ah רָאָה וַ/יִּרְא֥וּ | laqach לָקַח וַ/יִּקְח֤וּ | 5 |  |
| 296 | 1 Samuel 5:7 → 1 Samuel 5:3 | ra'ah רָאָה וַ/יִּרְא֥וּ | laqach לָקַח וַ/יִּקְחוּ֙ | 4 |  |
| 297 | 1 Samuel 6:13 → 1 Samuel 6:8 | ra'ah רָאָה וַ/יִּרְאוּ֙; ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח וּ/לְקַחְתֶּ֞ם | 5 |  |
| 298 | 1 Samuel 6:9 → 1 Samuel 6:13 | ra'ah רָאָה וּ/רְאִיתֶ֗ם | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 299 | 1 Samuel 6:13 → 1 Samuel 6:10 | ra'ah רָאָה וַ/יִּרְאוּ֙; ra'ah רָאָה לִ/רְאֽוֹת | laqach לָקַח וַ/יִּקְח֗וּ | 3 |  |
| 300 | 1 Samuel 6:16 → 1 Samuel 6:13 | ra'ah רָאָה רָא֑וּ | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 301 | 1 Samuel 9:17 → 1 Samuel 9:22 | ra'ah רָאָה רָאָ֣ה | laqach לָקַח וַ/יִּקַּ֤ח | 5 |  |
| 302 | 1 Samuel 10:24 → 1 Samuel 10:20 | ra'ah רָאָה הַ/רְּאִיתֶם֙ | lakad לָכַד וַ/יִּלָּכֵ֖ד | 4 |  |
| 303 | 1 Samuel 10:24 → 1 Samuel 10:21 | ra'ah רָאָה הַ/רְּאִיתֶם֙ | lakad לָכַד וַ/תִּלָּכֵ֖ד; lakad לָכַד וַ/יִּלָּכֵד֙ | 3 |  |
| 304 | 1 Samuel 14:16 → 1 Samuel 14:12 | ra'ah רָאָה וַ/יִּרְא֤וּ; tsaphah צָפָה הַ/צֹּפִים֙ | nasa נָשָׂא נֹשֵׂ֣א; nasa נָשָׂא נֹשֵׂ֤א | 4 |  |
| 305 | 1 Samuel 14:17 → 1 Samuel 14:12 | ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא נֹשֵׂ֣א; nasa נָשָׂא נֹשֵׂ֤א | 5 |  |
| 306 | 1 Samuel 14:16 → 1 Samuel 14:13 | ra'ah רָאָה וַ/יִּרְא֤וּ; tsaphah צָפָה הַ/צֹּפִים֙ | nasa נָשָׂא וְ/נֹשֵׂ֥א; nasa נָשָׂא וְ/נֹשֵׂ֥א | 3 |  |
| 307 | 1 Samuel 14:17 → 1 Samuel 14:13 | ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא וְ/נֹשֵׂ֥א; nasa נָשָׂא וְ/נֹשֵׂ֥א | 4 |  |
| 308 | 1 Samuel 14:17 → 1 Samuel 14:14 | ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא וְ/נֹשֵׂ֥א | 3 |  |
| 309 | 1 Samuel 14:27 → 1 Samuel 14:32 | ra'ah רָאָה ו/תראנה | laqach לָקַח וַ/יִּקְח֨וּ | 5 |  |
| 310 | 1 Samuel 14:29 → 1 Samuel 14:32 | ra'ah רָאָה רְאוּ | laqach לָקַח וַ/יִּקְח֨וּ | 3 |  |
| 311 | 1 Samuel 14:38 → 1 Samuel 14:41 | ra'ah רָאָה וּ/רְא֔וּ | lakad לָכַד וַ/יִּלָּכֵ֧ד | 3 |  |
| 312 | 1 Samuel 14:38 → 1 Samuel 14:42 | ra'ah רָאָה וּ/רְא֔וּ | lakad לָכַד וַ/יִּלָּכֵ֖ד | 4 |  |
| 313 | 1 Samuel 14:52 → 1 Samuel 14:47 | ra'ah רָאָה וְ/רָאָ֨ה | lakad לָכַד לָכַ֥ד | 5 |  |
| 314 | 1 Samuel 16:6 → 1 Samuel 16:2 | ra'ah רָאָה וַ/יַּ֖רְא | laqach לָקַח תִּקַּ֣ח | 4 |  |
| 315 | 1 Samuel 16:7 → 1 Samuel 16:2 | nabat נָבַט תַּבֵּ֧ט; ra'ah רָאָה יִרְאֶה֙; ra'ah רָאָה יִרְאֶ֣ה; ra'ah רָאָה יִרְאֶ֥ה | laqach לָקַח תִּקַּ֣ח | 5 |  |
| 316 | 1 Samuel 16:6 → 1 Samuel 16:11 | ra'ah רָאָה וַ/יַּ֖רְא | laqach לָקַח וְ/קָחֶ֔/נּוּ | 5 |  |
| 317 | 1 Samuel 16:7 → 1 Samuel 16:11 | nabat נָבַט תַּבֵּ֧ט; ra'ah רָאָה יִרְאֶה֙; ra'ah רָאָה יִרְאֶ֣ה; ra'ah רָאָה יִרְאֶ֥ה | laqach לָקַח וְ/קָחֶ֔/נּוּ | 4 |  |
| 318 | 1 Samuel 16:17 → 1 Samuel 16:13 | ra'ah רָאָה רְאוּ | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 319 | 1 Samuel 16:18 → 1 Samuel 16:13 | ra'ah רָאָה רָאִ֜יתִי | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 320 | 1 Samuel 16:17 → 1 Samuel 16:20 | ra'ah רָאָה רְאוּ | laqach לָקַח וַ/יִּקַּ֨ח | 3 |  |
| 321 | 1 Samuel 16:17 → 1 Samuel 16:21 | ra'ah רָאָה רְאוּ | nasa נָשָׂא נֹשֵׂ֥א | 4 |  |
| 322 | 1 Samuel 16:18 → 1 Samuel 16:21 | ra'ah רָאָה רָאִ֜יתִי | nasa נָשָׂא נֹשֵׂ֥א | 3 |  |
| 323 | 1 Samuel 16:18 → 1 Samuel 16:23 | ra'ah רָאָה רָאִ֜יתִי | laqach לָקַח וְ/לָקַ֥ח | 5 |  |
| 324 | 1 Samuel 17:24 → 1 Samuel 17:20 | ra'ah רָאָה בִּ/רְאוֹתָ֖/ם | nasa נָשָׂא וַ/יִּשָּׂ֣א | 4 |  |
| 325 | 1 Samuel 17:25 → 1 Samuel 17:20 | ra'ah רָאָה הַ/רְּאִיתֶם֙ | nasa נָשָׂא וַ/יִּשָּׂ֣א | 5 |  |
| 326 | 1 Samuel 17:28 → 1 Samuel 17:31 | ra'ah רָאָה רְא֥וֹת | laqach לָקַח וַ/יִּקָּחֵֽ/הוּ | 3 |  |
| 327 | 1 Samuel 17:55 → 1 Samuel 17:51 | ra'ah רָאָה וְ/כִ/רְא֨וֹת | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 328 | 1 Samuel 17:51 → 1 Samuel 17:54 | ra'ah רָאָה וַ/יִּרְא֧וּ | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 329 | 1 Samuel 17:55 → 1 Samuel 18:2 | ra'ah רָאָה וְ/כִ/רְא֨וֹת | laqach לָקַח וַ/יִּקָּחֵ֥/הוּ | 5 |  |
| 330 | 1 Samuel 19:15 → 1 Samuel 19:20 | ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח לָ/קַ֣חַת | 5 |  |
| 331 | 1 Samuel 21:15 → 1 Samuel 21:10 | ra'ah רָאָה תִרְאוּ֙ | laqach לָקַח תִּֽקַּח; laqach לָקַח קָ֔ח | 5 |  |
| 332 | 1 Samuel 23:22 → 1 Samuel 23:26 | ra'ah רָאָה וּ/רְאוּ֙; ra'ah רָאָה רָאָ֖/הוּ | taphas תָּפַשׂ לְ/תָפְשָֽׂ/ם | 4 |  |
| 333 | 1 Samuel 23:23 → 1 Samuel 23:26 | ra'ah רָאָה וּ/רְא֣וּ | taphas תָּפַשׂ לְ/תָפְשָֽׂ/ם | 3 |  |
| 334 | 1 Samuel 24:9 → 1 Samuel 24:12 | nabat נָבַט וַ/יַּבֵּ֤ט | laqach לָקַח לְ/קַחְתָּֽ/הּ | 3 |  |
| 335 | 1 Samuel 24:16 → 1 Samuel 24:12 | ra'ah רָאָה וְ/יֵ֨רֶא֙ | laqach לָקַח לְ/קַחְתָּֽ/הּ | 4 |  |
| 336 | 1 Samuel 24:12 → 1 Samuel 24:17 | ra'ah רָאָה רְאֵ֔ה; ra'ah רָאָה רְאֵ֛ה; ra'ah רָאָה וּ/רְאֵה֙ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 5 |  |
| 337 | 1 Samuel 25:23 → 1 Samuel 25:18 | ra'ah רָאָה וַ/תֵּ֤רֶא | laqach לָקַח וַ/תִּקַּח֩ | 5 |  |
| 338 | 1 Samuel 25:23 → 1 Samuel 25:28 | ra'ah רָאָה וַ/תֵּ֤רֶא | nasa נָשָׂא שָׂ֥א | 5 |  |
| 339 | 1 Samuel 25:25 → 1 Samuel 25:28 | ra'ah רָאָה רָאִ֛יתִי | nasa נָשָׂא שָׂ֥א | 3 |  |
| 340 | 1 Samuel 25:35 → 1 Samuel 25:39 | ra'ah רָאָה רְאִי֙ | laqach לָקַח לְ/קַחְתָּ֥/הּ | 4 |  |
| 341 | 1 Samuel 25:35 → 1 Samuel 25:40 | ra'ah רָאָה רְאִי֙ | laqach לָקַח לְ/קַחְתֵּ֥/ךְ | 5 |  |
| 342 | 1 Samuel 26:3 → 1 Samuel 25:43 | ra'ah רָאָה וַ/יַּ֕רְא | laqach לָקַח לָקַ֥ח | 4 |  |
| 343 | 1 Samuel 26:16 → 1 Samuel 26:11 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח קַח | 5 |  |
| 344 | 1 Samuel 26:16 → 1 Samuel 26:12 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וַ/יִּקַּח֩ | 4 |  |
| 345 | 1 Samuel 28:21 → 1 Samuel 28:24 | ra'ah רָאָה וַ/תֵּ֖רֶא | laqach לָקַח וַ/תִּקַּח | 3 |  |
| 346 | 1 Samuel 31:7 → 1 Samuel 31:4 | ra'ah רָאָה וַ/יִּרְא֣וּ | nasa נָשָׂא לְ/נֹשֵׂ֨א; nasa נָשָׂא נֹשֵׂ֣א; laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 347 | 1 Samuel 31:7 → 1 Samuel 31:12 | ra'ah רָאָה וַ/יִּרְא֣וּ | laqach לָקַח וַ/יִּקְח֞וּ | 5 |  |
| 348 | 2 Samuel 1:7 → 2 Samuel 1:10 | ra'ah רָאָה וַ/יִּרְאֵ֑/נִי | laqach לָקַח וָ/אֶקַּ֞ח | 3 |  |
| 349 | 2 Samuel 6:16 → 2 Samuel 6:13 | shaqaph שָׁקַף נִשְׁקְפָ֣ה; ra'ah רָאָה וַ/תֵּ֨רֶא | nasa נָשָׂא נֹשְׂאֵ֥י | 3 |  |
| 350 | 2 Samuel 10:9 → 2 Samuel 10:4 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 351 | 2 Samuel 10:19 → 2 Samuel 11:4 | ra'ah רָאָה וַ/יִּרְא֨וּ | laqach לָקַח וַ/יִּקָּחֶ֗/הָ | 4 |  |
| 352 | 2 Samuel 13:5 → 2 Samuel 13:8 | ra'ah רָאָה לִ/רְאוֹתֶ֗/ךָ; ra'ah רָאָה אֶרְאֶ֔ה | laqach לָקַח וַ/תִּקַּ֨ח | 3 |  |
| 353 | 2 Samuel 13:5 → 2 Samuel 13:9 | ra'ah רָאָה לִ/רְאוֹתֶ֗/ךָ; ra'ah רָאָה אֶרְאֶ֔ה | laqach לָקַח וַ/תִּקַּ֤ח | 4 |  |
| 354 | 2 Samuel 13:5 → 2 Samuel 13:10 | ra'ah רָאָה לִ/רְאוֹתֶ֗/ךָ; ra'ah רָאָה אֶרְאֶ֔ה | laqach לָקַח וַ/תִּקַּ֣ח | 5 |  |
| 355 | 2 Samuel 13:6 → 2 Samuel 13:9 | ra'ah רָאָה לִ/רְאֹת֗/וֹ | laqach לָקַח וַ/תִּקַּ֤ח | 3 |  |
| 356 | 2 Samuel 13:6 → 2 Samuel 13:10 | ra'ah רָאָה לִ/רְאֹת֗/וֹ | laqach לָקַח וַ/תִּקַּ֣ח | 4 |  |
| 357 | 2 Samuel 15:27 → 2 Samuel 15:24 | ra'ah רָאָה הֲ/רוֹאֶ֣ה | nasa נָשָׂא נֹֽשְׂאִים֙ | 3 |  |
| 358 | 2 Samuel 15:28 → 2 Samuel 15:24 | ra'ah רָאָה רְאוּ֙ | nasa נָשָׂא נֹֽשְׂאִים֙ | 4 |  |
| 359 | 2 Samuel 17:17 → 2 Samuel 17:13 | ra'ah רָאָה לְ/הֵרָא֖וֹת | nasa נָשָׂא וְ/הִשִּׂ֧יאוּ | 4 |  |
| 360 | 2 Samuel 17:18 → 2 Samuel 17:13 | ra'ah רָאָה וַ/יַּ֤רְא | nasa נָשָׂא וְ/הִשִּׂ֧יאוּ | 5 |  |
| 361 | 2 Samuel 17:23 → 2 Samuel 17:19 | ra'ah רָאָה רָאָ֗ה | laqach לָקַח וַ/תִּקַּ֣ח | 4 |  |
| 362 | 2 Samuel 18:10 → 2 Samuel 18:14 | ra'ah רָאָה וַ/יַּרְא֙; ra'ah רָאָה רָאִ֣יתִי | laqach לָקַח וַ/יִּקַּח֩ | 4 |  |
| 363 | 2 Samuel 18:10 → 2 Samuel 18:15 | ra'ah רָאָה וַ/יַּרְא֙; ra'ah רָאָה רָאִ֣יתִי | nasa נָשָׂא נֹשְׂאֵ֖י | 5 |  |
| 364 | 2 Samuel 18:11 → 2 Samuel 18:14 | ra'ah רָאָה רָאִ֔יתָ | laqach לָקַח וַ/יִּקַּח֩ | 3 |  |
| 365 | 2 Samuel 18:11 → 2 Samuel 18:15 | ra'ah רָאָה רָאִ֔יתָ | nasa נָשָׂא נֹשְׂאֵ֖י | 4 |  |
| 366 | 2 Samuel 18:21 → 2 Samuel 18:17 | ra'ah רָאָה רָאִ֑יתָה | laqach לָקַח וַ/יִּקְח֣וּ | 4 |  |
| 367 | 2 Samuel 18:21 → 2 Samuel 18:18 | ra'ah רָאָה רָאִ֑יתָה | laqach לָקַח לָקַ֗ח | 3 |  |
| 368 | 2 Samuel 18:21 → 2 Samuel 18:24 | ra'ah רָאָה רָאִ֑יתָה | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 369 | 2 Samuel 18:27 → 2 Samuel 18:24 | tsaphah צָפָה הַ/צֹּפֶ֔ה; ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 370 | 2 Samuel 18:29 → 2 Samuel 18:24 | ra'ah רָאָה רָאִיתִי֩ | nasa נָשָׂא וַ/יִּשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 371 | 2 Samuel 18:24 → 2 Samuel 18:28 | tsaphah צָפָה הַ/צֹּפֶ֜ה; ra'ah רָאָה וַ/יַּ֔רְא | nasa נָשָׂא נָשְׂא֥וּ | 4 |  |
| 372 | 2 Samuel 18:25 → 2 Samuel 18:28 | tsaphah צָפָה הַ/צֹּפֶה֙ | nasa נָשָׂא נָשְׂא֥וּ | 3 |  |
| 373 | 2 Samuel 20:12 → 2 Samuel 20:9 | ra'ah רָאָה וַ/יַּ֨רְא; ra'ah רָאָה רָאָ֔ה | achaz אָחַז וַ/תֹּ֜חֶז | 3 |  |
| 374 | 2 Samuel 24:3 → 2 Samuel 23:37 | ra'ah רָאָה רֹא֑וֹת | nasa נָשָׂא נשאי; nasa נָשָׂא נֹשֵׂ֕א | 5 |  |
| 375 | 2 Samuel 24:17 → 2 Samuel 24:22 | ra'ah רָאָה בִּ/רְאֹת֣/וֹ | laqach לָקַח יִקַּ֥ח | 5 |  |
| 376 | 1 Kings 1:48 → 1 Kings 1:51 | ra'ah רָאָה רֹאֽוֹת | achaz אָחַז אָחַ֞ז | 3 |  |
| 377 | 1 Kings 3:5 → 1 Kings 3:1 | ra'ah רָאָה נִרְאָ֧ה | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 378 | 1 Kings 3:28 → 1 Kings 3:24 | ra'ah רָאָה רָא֔וּ | laqach לָקַח קְח֣וּ | 4 |  |
| 379 | 1 Kings 8:8 → 1 Kings 8:3 | ra'ah רָאָה וַ/יֵּרָאוּ֩; ra'ah רָאָה יֵרָא֖וּ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 5 |  |
| 380 | 1 Kings 9:12 → 1 Kings 9:16 | ra'ah רָאָה לִ/רְאוֹת֙ | lakad לָכַד וַ/יִּלְכֹּ֤ד | 4 |  |
| 381 | 1 Kings 10:4 → 1 Kings 9:28 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח וַ/יִּקְח֤וּ | 4 |  |
| 382 | 1 Kings 10:7 → 1 Kings 10:2 | ra'ah רָאָה וַ/תִּרְאֶ֣ינָה | nasa נָשָׂא נֹשְׂאִ֨ים | 5 |  |
| 383 | 1 Kings 10:7 → 1 Kings 10:11 | ra'ah רָאָה וַ/תִּרְאֶ֣ינָה | nasa נָשָׂא נָשָׂ֥א | 4 |  |
| 384 | 1 Kings 11:28 → 1 Kings 11:31 | ra'ah רָאָה וַ/יַּ֨רְא | laqach לָקַח קַח | 3 |  |
| 385 | 1 Kings 13:25 → 1 Kings 13:29 | ra'ah רָאָה וַ/יִּרְא֤וּ | nasa נָשָׂא וַ/יִּשָּׂ֨א | 4 |  |
| 386 | 1 Kings 17:23 → 1 Kings 17:19 | ra'ah רָאָה רְאִ֖י | laqach לָקַח וַ/יִּקָּחֵ֣/הוּ | 4 |  |
| 387 | 1 Kings 18:2 → 1 Kings 17:23 | ra'ah רָאָה לְ/הֵרָא֖וֹת | laqach לָקַח וַ/יִּקַּ֨ח | 3 |  |
| 388 | 1 Kings 17:23 → 1 Kings 18:4 | ra'ah רָאָה רְאִ֖י | laqach לָקַח וַ/יִּקַּ֨ח | 5 |  |
| 389 | 1 Kings 18:1 → 1 Kings 18:4 | ra'ah רָאָה הֵרָאֵ֣ה | laqach לָקַח וַ/יִּקַּ֨ח | 3 |  |
| 390 | 1 Kings 18:15 → 1 Kings 18:12 | ra'ah רָאָה אֵרָאֶ֥ה | nasa נָשָׂא יִֽשָּׂאֲ/ךָ֙ | 3 |  |
| 391 | 1 Kings 18:17 → 1 Kings 18:12 | ra'ah רָאָה כִּ/רְא֥וֹת | nasa נָשָׂא יִֽשָּׂאֲ/ךָ֙ | 5 |  |
| 392 | 1 Kings 18:43 → 1 Kings 18:40 | nabat נָבַט הַבֵּ֣ט; nabat נָבַט וַ/יַּבֵּ֔ט | taphas תָּפַשׂ תִּפְשׂ֣וּ; taphas תָּפַשׂ וַֽ/יִּתְפְּשׂ֑וּ/ם | 3 |  |
| 393 | 1 Kings 19:6 → 1 Kings 19:10 | nabat נָבַט וַ/יַּבֵּ֕ט | laqach לָקַח לְ/קַחְתָּֽ/הּ | 4 |  |
| 394 | 1 Kings 20:13 → 1 Kings 20:18 | ra'ah רָאָה הְֽ/רָאִ֔יתָ | taphas תָּפַשׂ תִּפְשׂ֣וּ/ם; taphas תָּפַשׂ תִּפְשֽׂוּ/ם | 5 |  |
| 395 | 1 Kings 20:22 → 1 Kings 20:18 | ra'ah רָאָה וּ/רְאֵ֖ה | taphas תָּפַשׂ תִּפְשׂ֣וּ/ם; taphas תָּפַשׂ תִּפְשֽׂוּ/ם | 4 |  |
| 396 | 1 Kings 21:29 → 1 Kings 22:3 | ra'ah רָאָה הֲֽ/רָאִ֔יתָ | laqach לָקַח מִ/קַּ֣חַת | 3 |  |
| 397 | 2 Kings 2:10 → 2 Kings 2:5 | ra'ah רָאָה תִּרְאֶ֨ה | laqach לָקַח לֹקֵ֥חַ | 5 |  |
| 398 | 2 Kings 2:12 → 2 Kings 2:8 | ra'ah רָאָה רֹאֶ֗ה; ra'ah רָאָה רָאָ֖/הוּ | laqach לָקַח וַ/יִּקַּח֩ | 4 |  |
| 399 | 2 Kings 2:12 → 2 Kings 2:9 | ra'ah רָאָה רֹאֶ֗ה; ra'ah רָאָה רָאָ֖/הוּ | laqach לָקַח אֶלָּקַ֣ח | 3 |  |
| 400 | 2 Kings 2:15 → 2 Kings 2:10 | ra'ah רָאָה וַ/יִּרְאֻ֨/הוּ | laqach לָקַח לֻקָּ֤ח | 5 |  |
| 401 | 2 Kings 2:10 → 2 Kings 2:14 | ra'ah רָאָה תִּרְאֶ֨ה | laqach לָקַח וַ/יִּקַּח֩ | 4 |  |
| 402 | 2 Kings 2:12 → 2 Kings 2:16 | ra'ah רָאָה רֹאֶ֗ה; ra'ah רָאָה רָאָ֖/הוּ | nasa נָשָׂא נְשָׂא/וֹ֙ | 4 |  |
| 403 | 2 Kings 2:19 → 2 Kings 2:14 | ra'ah רָאָה רֹאֶ֑ה | laqach לָקַח וַ/יִּקַּח֩ | 5 |  |
| 404 | 2 Kings 2:15 → 2 Kings 2:20 | ra'ah רָאָה וַ/יִּרְאֻ֨/הוּ | laqach לָקַח קְחוּ; laqach לָקַח וַ/יִּקְח֖וּ | 5 |  |
| 405 | 2 Kings 2:19 → 2 Kings 2:16 | ra'ah רָאָה רֹאֶ֑ה | nasa נָשָׂא נְשָׂא/וֹ֙ | 3 |  |
| 406 | 2 Kings 2:24 → 2 Kings 2:20 | ra'ah רָאָה וַ/יִּרְאֵ֔/ם | laqach לָקַח קְחוּ; laqach לָקַח וַ/יִּקְח֖וּ | 4 |  |
| 407 | 2 Kings 3:17 → 2 Kings 3:14 | ra'ah רָאָה תִרְא֥וּ; ra'ah רָאָה תִרְא֣וּ | nasa נָשָׂא נֹשֵׂ֑א | 3 |  |
| 408 | 2 Kings 3:22 → 2 Kings 3:26 | ra'ah רָאָה וַ/יִּרְא֨וּ | laqach לָקַח וַ/יִּקַּ֣ח | 4 |  |
| 409 | 2 Kings 3:22 → 2 Kings 3:27 | ra'ah רָאָה וַ/יִּרְא֨וּ | laqach לָקַח וַ/יִּקַּח֩ | 5 |  |
| 410 | 2 Kings 4:25 → 2 Kings 4:20 | ra'ah רָאָה כִּ/רְא֨וֹת | nasa נָשָׂא וַ/יִּשָּׂאֵ֔/הוּ | 5 |  |
| 411 | 2 Kings 4:25 → 2 Kings 4:29 | ra'ah רָאָה כִּ/רְא֨וֹת | laqach לָקַח וְ/קַ֨ח | 4 |  |
| 412 | 2 Kings 5:21 → 2 Kings 5:16 | ra'ah רָאָה וַ/יִּרְאֶ֤ה | laqach לָקַח אֶקָּ֑ח; laqach לָקַח לָ/קַ֖חַת | 5 |  |
| 413 | 2 Kings 5:21 → 2 Kings 5:24 | ra'ah רָאָה וַ/יִּרְאֶ֤ה | laqach לָקַח וַ/יִּקַּ֥ח | 3 |  |
| 414 | 2 Kings 5:21 → 2 Kings 5:26 | ra'ah רָאָה וַ/יִּרְאֶ֤ה | laqach לָקַח לָ/קַ֤חַת; laqach לָקַח וְ/לָ/קַ֣חַת | 5 |  |
| 415 | 2 Kings 6:6 → 2 Kings 6:2 | ra'ah רָאָה וַ/יַּרְאֵ֨/הוּ֙ | laqach לָקַח וְ/נִקְחָ֤ה | 4 |  |
| 416 | 2 Kings 6:17 → 2 Kings 6:13 | ra'ah רָאָה וְ/יִרְאֶ֑ה; ra'ah רָאָה וַ/יַּ֗רְא | laqach לָקַח וְ/אֶקָּחֵ֑/הוּ | 4 |  |
| 417 | 2 Kings 7:13 → 2 Kings 7:8 | ra'ah רָאָה וְ/נִרְאֶֽה | nasa נָשָׂא וַ/יִּשְׂא֣וּ; nasa נָשָׂא וַ/יִּשְׂא֣וּ | 5 |  |
| 418 | 2 Kings 7:19 → 2 Kings 7:14 | ra'ah רָאָה רֹאֶה֙ | laqach לָקַח וַ/יִּקְח֕וּ | 5 |  |
| 419 | 2 Kings 8:13 → 2 Kings 8:8 | ra'ah רָאָה הִרְאַ֧/נִי | laqach לָקַח קַ֤ח | 5 |  |
| 420 | 2 Kings 8:13 → 2 Kings 8:9 | ra'ah רָאָה הִרְאַ֧/נִי | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 421 | 2 Kings 8:10 → 2 Kings 8:15 | ra'ah רָאָה וְ/הִרְאַ֥/נִי | laqach לָקַח וַ/יִּקַּ֤ח | 5 |  |
| 422 | 2 Kings 8:29 → 2 Kings 9:3 | ra'ah רָאָה לִ/רְא֞וֹת | laqach לָקַח וְ/לָקַחְתָּ֤ | 3 |  |
| 423 | 2 Kings 9:16 → 2 Kings 9:13 | ra'ah רָאָה לִ/רְא֥וֹת | laqach לָקַח וַ/יִּקְחוּ֙ | 3 |  |
| 424 | 2 Kings 9:17 → 2 Kings 9:13 | tsaphah צָפָה וְ/הַ/צֹּפֶה֩; ra'ah רָאָה וַ/יַּ֞רְא; ra'ah רָאָה רֹאֶ֑ה | laqach לָקַח וַ/יִּקְחוּ֙ | 4 |  |
| 425 | 2 Kings 9:18 → 2 Kings 9:13 | tsaphah צָפָה הַ/צֹּפֶה֙ | laqach לָקַח וַ/יִּקְחוּ֙ | 5 |  |
| 426 | 2 Kings 9:20 → 2 Kings 9:17 | tsaphah צָפָה הַ/צֹּפֶה֙ | laqach לָקַח קַ֥ח | 3 |  |
| 427 | 2 Kings 9:22 → 2 Kings 9:17 | ra'ah רָאָה כִּ/רְא֤וֹת | laqach לָקַח קַ֥ח | 5 |  |
| 428 | 2 Kings 9:20 → 2 Kings 9:25 | tsaphah צָפָה הַ/צֹּפֶה֙ | nasa נָשָׂא שָׂ֚א; nasa נָשָׂא נָשָׂ֣א | 5 |  |
| 429 | 2 Kings 9:22 → 2 Kings 9:25 | ra'ah רָאָה כִּ/רְא֤וֹת | nasa נָשָׂא שָׂ֚א; nasa נָשָׂא נָשָׂ֣א | 3 |  |
| 430 | 2 Kings 9:22 → 2 Kings 9:26 | ra'ah רָאָה כִּ/רְא֤וֹת | nasa נָשָׂא שָׂ֧א | 4 |  |
| 431 | 2 Kings 9:30 → 2 Kings 9:25 | shaqaph שָׁקַף וַ/תַּשְׁקֵ֖ף | nasa נָשָׂא שָׂ֚א; nasa נָשָׂא נָשָׂ֣א | 5 |  |
| 432 | 2 Kings 9:30 → 2 Kings 9:26 | shaqaph שָׁקַף וַ/תַּשְׁקֵ֖ף | nasa נָשָׂא שָׂ֧א | 4 |  |
| 433 | 2 Kings 9:27 → 2 Kings 9:32 | ra'ah רָאָה רָאָ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֤א | 5 |  |
| 434 | 2 Kings 10:3 → 2 Kings 10:6 | ra'ah רָאָה וּ/רְאִיתֶ֞ם | laqach לָקַח קְחוּ֙ | 3 |  |
| 435 | 2 Kings 10:3 → 2 Kings 10:7 | ra'ah רָאָה וּ/רְאִיתֶ֞ם | laqach לָקַח וַ/יִּקְחוּ֙ | 4 |  |
| 436 | 2 Kings 11:1 → 2 Kings 11:4 | ra'ah רָאָה ו/ראתה; ra'ah רָאָה רָאֲתָ֖ה | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 437 | 2 Kings 11:4 → 2 Kings 11:9 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקְחוּ֙ | 5 |  |
| 438 | 2 Kings 11:14 → 2 Kings 11:9 | ra'ah רָאָה וַ/תֵּ֡רֶא | laqach לָקַח וַ/יִּקְחוּ֙ | 5 |  |
| 439 | 2 Kings 11:14 → 2 Kings 11:19 | ra'ah רָאָה וַ/תֵּ֡רֶא | laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 440 | 2 Kings 12:11 → 2 Kings 12:6 | ra'ah רָאָה כִּ/רְאוֹתָ֔/ם | laqach לָקַח יִקְח֤וּ | 5 |  |
| 441 | 2 Kings 12:11 → 2 Kings 12:8 | ra'ah רָאָה כִּ/רְאוֹתָ֔/ם | laqach לָקַח תִּקְחוּ | 3 |  |
| 442 | 2 Kings 13:21 → 2 Kings 13:18 | ra'ah רָאָה רָא֣וּ | laqach לָקַח קַ֥ח; laqach לָקַח וַ/יִּקָּ֑ח | 3 |  |
| 443 | 2 Kings 13:21 → 2 Kings 13:25 | ra'ah רָאָה רָא֣וּ | laqach לָקַח וַ/יִּקַּ֤ח; laqach לָקַח לָקַ֗ח | 4 |  |
| 444 | 2 Kings 14:11 → 2 Kings 14:7 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | taphas תָּפַשׂ וְ/תָפַ֥שׂ | 4 |  |
| 445 | 2 Kings 14:8 → 2 Kings 14:13 | ra'ah רָאָה נִתְרָאֶ֥ה | taphas תָּפַשׂ תָּפַ֛שׂ | 5 |  |
| 446 | 2 Kings 14:11 → 2 Kings 14:14 | ra'ah רָאָה וַ/יִּתְרָא֣וּ | laqach לָקַח וְ/לָקַ֣ח | 3 |  |
| 447 | 2 Kings 14:26 → 2 Kings 14:21 | ra'ah רָאָה רָאָ֧ה | laqach לָקַח וַ/יִּקְח֞וּ | 5 |  |
| 448 | 2 Kings 16:12 → 2 Kings 16:8 | ra'ah רָאָה וַ/יַּ֥רְא | laqach לָקַח וַ/יִּקַּ֨ח | 4 |  |
| 449 | 2 Kings 16:12 → 2 Kings 16:9 | ra'ah רָאָה וַ/יַּ֥רְא | taphas תָּפַשׂ וַֽ/יִּתְפְּשֶׂ֔/הָ | 3 |  |
| 450 | 2 Kings 20:13 → 2 Kings 20:17 | ra'ah רָאָה וַ/יַּרְאֵ֣/ם; ra'ah רָאָה הֶרְאָ֧/ם | nasa נָשָׂא וְ/נִשָּׂ֣א | 4 |  |
| 451 | 2 Kings 20:13 → 2 Kings 20:18 | ra'ah רָאָה וַ/יַּרְאֵ֣/ם; ra'ah רָאָה הֶרְאָ֧/ם | laqach לָקַח יקח; laqach לָקַח יִקָּ֑חוּ | 5 |  |
| 452 | 2 Kings 20:15 → 2 Kings 20:18 | ra'ah רָאָה רָא֖וּ; ra'ah רָאָה רָא֔וּ; ra'ah רָאָה הִרְאִיתִ֖/ם | laqach לָקַח יקח; laqach לָקַח יִקָּ֑חוּ | 3 |  |
| 453 | 2 Kings 22:20 → 2 Kings 23:4 | ra'ah רָאָה תִרְאֶ֣ינָה | nasa נָשָׂא וְ/נָשָׂ֥א | 4 |  |
| 454 | 2 Kings 23:29 → 2 Kings 23:34 | ra'ah רָאָה כִּ/רְאֹת֖/וֹ | laqach לָקַח לָקָ֔ח | 5 |  |
| 455 | 2 Kings 25:19 → 2 Kings 25:14 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח לָקָֽחוּ | 5 |  |
| 456 | 2 Kings 25:19 → 2 Kings 25:15 | ra'ah רָאָה מֵ/רֹאֵ֤י | laqach לָקַח לָקַ֖ח | 4 |  |
| 457 | 1 Chronicles 10:7 → 1 Chronicles 10:4 | ra'ah רָאָה וַ֠/יִּרְאוּ | nasa נָשָׂא נֹשֵׂ֨א; nasa נָשָׂא נֹשֵׂ֣א; laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 458 | 1 Chronicles 10:5 → 1 Chronicles 10:9 | ra'ah רָאָה וַ/יַּ֥רְא | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 4 |  |
| 459 | 1 Chronicles 10:7 → 1 Chronicles 10:12 | ra'ah רָאָה וַ֠/יִּרְאוּ | nasa נָשָׂא וַ/יִּשְׂא֞וּ | 5 |  |
| 460 | 1 Chronicles 15:29 → 1 Chronicles 15:26 | shaqaph שָׁקַף נִשְׁקְפָ֣ה; ra'ah רָאָה וַ/תֵּ֨רֶא | nasa נָשָׂא נֹשְׂאֵ֖י | 3 |  |
| 461 | 1 Chronicles 19:16 → 1 Chronicles 20:2 | ra'ah רָאָה וַ/יַּ֣רְא | laqach לָקַח וַ/יִּקַּ֣ח | 5 |  |
| 462 | 1 Chronicles 21:12 → 1 Chronicles 21:16 | ra'ah רָאָה רְאֵ֔ה | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 463 | 1 Chronicles 21:20 → 1 Chronicles 21:16 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 464 | 1 Chronicles 21:21 → 1 Chronicles 21:16 | nabat נָבַט וַ/יַּבֵּ֤ט; ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא וַ/יִּשָּׂ֨א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 465 | 1 Chronicles 21:20 → 1 Chronicles 21:23 | ra'ah רָאָה וַ/יַּרְא֙ | laqach לָקַח קַֽח | 3 |  |
| 466 | 1 Chronicles 21:20 → 1 Chronicles 21:24 | ra'ah רָאָה וַ/יַּרְא֙ | nasa נָשָׂא אֶשָּׂ֤א | 4 |  |
| 467 | 1 Chronicles 21:21 → 1 Chronicles 21:24 | nabat נָבַט וַ/יַּבֵּ֤ט; ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא אֶשָּׂ֤א | 3 |  |
| 468 | 1 Chronicles 21:28 → 1 Chronicles 21:23 | ra'ah רָאָה בִּ/רְא֤וֹת | laqach לָקַח קַֽח | 5 |  |
| 469 | 1 Chronicles 21:28 → 1 Chronicles 21:24 | ra'ah רָאָה בִּ/רְא֤וֹת | nasa נָשָׂא אֶשָּׂ֤א | 4 |  |
| 470 | 2 Chronicles 5:9 → 2 Chronicles 5:4 | ra'ah רָאָה וַ/יֵּרָאוּ֩; ra'ah רָאָה יֵרָא֖וּ | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 5 |  |
| 471 | 2 Chronicles 9:3 → 2 Chronicles 8:18 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | laqach לָקַח וַ/יִּקְח֣וּ | 3 |  |
| 472 | 2 Chronicles 9:6 → 2 Chronicles 9:1 | ra'ah רָאָה וַ/תִּרְאֶ֣ינָה | nasa נָשָׂא נֹשְׂאִ֨ים | 5 |  |
| 473 | 2 Chronicles 12:7 → 2 Chronicles 12:4 | ra'ah רָאָה וּ/בִ/רְא֤וֹת | lakad לָכַד וַ/יִּלְכֹּ֛ד | 3 |  |
| 474 | 2 Chronicles 12:7 → 2 Chronicles 12:11 | ra'ah רָאָה וּ/בִ/רְא֤וֹת | nasa נָשָׂא וּ/נְשָׂא֔וּ/ם | 4 |  |
| 475 | 2 Chronicles 16:10 → 2 Chronicles 16:6 | ra'ah רָאָה הָ/רֹאֶ֗ה | laqach לָקַח לָקַח֙; nasa נָשָׂא וַ/יִּשְׂא֞וּ | 4 |  |
| 476 | 2 Chronicles 22:6 → 2 Chronicles 22:9 | ra'ah רָאָה לִ/רְא֞וֹת | lakad לָכַד וַֽ/יִּלְכְּדֻ֜/הוּ | 3 |  |
| 477 | 2 Chronicles 22:6 → 2 Chronicles 22:11 | ra'ah רָאָה לִ/רְא֞וֹת | laqach לָקַח וַ/תִּקַּח֩ | 5 |  |
| 478 | 2 Chronicles 22:10 → 2 Chronicles 23:1 | ra'ah רָאָה רָאֲתָ֖ה | laqach לָקַח וַ/יִּקַּ֣ח | 3 |  |
| 479 | 2 Chronicles 23:13 → 2 Chronicles 23:8 | ra'ah רָאָה וַ/תֵּ֡רֶא | laqach לָקַח וַ/יִּקְחוּ֙ | 5 |  |
| 480 | 2 Chronicles 26:5 → 2 Chronicles 25:28 | ra'ah רָאָה בִּ/רְאֹ֣ת | nasa נָשָׂא וַ/יִּשָּׂאֻ֖/הוּ | 5 |  |
| 481 | 2 Chronicles 26:5 → 2 Chronicles 26:1 | ra'ah רָאָה בִּ/רְאֹ֣ת | laqach לָקַח וַ/יִּקְח֞וּ | 4 |  |
| 482 | Nehemiah 4:8 → Nehemiah 4:11 | ra'ah רָאָה וָ/אֵ֣רֶא | nasa נָשָׂא וְ/הַ/נֹּשְׂאִ֥ים | 3 |  |
| 483 | Esther 1:11 → Esther 1:6 | ra'ah רָאָה לְ/הַרְא֨וֹת | achaz אָחַז אָחוּז֙ | 5 |  |
| 484 | Esther 3:4 → Esther 3:1 | ra'ah רָאָה לִ/רְאוֹת֙ | nasa נָשָׂא וַֽ/יְנַשְּׂאֵ֑/הוּ | 3 |  |
| 485 | Esther 3:5 → Esther 3:1 | ra'ah רָאָה וַ/יַּ֣רְא | nasa נָשָׂא וַֽ/יְנַשְּׂאֵ֑/הוּ | 4 |  |
| 486 | Job 2:13 → Job 2:8 | ra'ah רָאָה רָא֔וּ | laqach לָקַח וַ/יִּֽקַּֽח | 5 |  |
| 487 | Job 3:9 → Job 3:6 | ra'ah רָאָה יִ֝רְאֶ֗ה | laqach לָקַח יִקָּחֵ֪/ה֫וּ | 3 |  |
| 488 | Job 4:8 → Job 4:12 | ra'ah רָאָה רָ֭אִיתִי | laqach לָקַח וַ/תִּקַּ֥ח | 4 |  |
| 489 | Job 7:8 → Job 7:13 | shur שׁוּר תְ֭שׁוּרֵ/נִי | nasa נָשָׂא יִשָּׂ֥א | 5 |  |
| 490 | Job 10:18 → Job 10:15 | ra'ah רָאָה תִרְאֵֽ/נִי | nasa נָשָׂא אֶשָּׂ֣א | 3 |  |
| 491 | Job 11:11 → Job 11:15 | ra'ah רָאָה וַ/יַּרְא | nasa נָשָׂא תִּשָּׂ֣א | 4 |  |
| 492 | Job 15:17 → Job 15:12 | chazah חָזָה חָ֝זִ֗יתִי | laqach לָקַח יִּקָּחֲ/ךָ֥ | 5 |  |
| 493 | Job 22:11 → Job 22:8 | ra'ah רָאָה תִרְאֶ֑ה | nasa נָשָׂא וּ/נְשׂ֥וּא | 3 |  |
| 494 | Job 22:12 → Job 22:8 | ra'ah רָאָה וּ/רְאֵ֤ה | nasa נָשָׂא וּ/נְשׂ֥וּא | 4 |  |
| 495 | Job 22:19 → Job 22:22 | ra'ah רָאָה יִרְא֣וּ | laqach לָקַח קַח | 3 |  |
| 496 | Job 24:15 → Job 24:10 | shur שׁוּר תְשׁוּרֵ֣/נִי | nasa נָשָׂא נָ֣שְׂאוּ | 5 |  |
| 497 | Job 24:15 → Job 24:19 | shur שׁוּר תְשׁוּרֵ֣/נִי | gazal גָּזַל יִגְזְל֥וּ | 4 |  |
| 498 | Job 28:24 → Job 29:1 | nabat נָבַט יַבִּ֑יט; ra'ah רָאָה יִרְאֶֽה | nasa נָשָׂא שְׂאֵ֥ת | 5 |  |
| 499 | Job 34:26 → Job 34:31 | ra'ah רָאָה רֹאִֽים | nasa נָשָׂא נָשָׂ֗אתִי | 5 |  |
| 500 | Job 35:14 → Job 36:3 | shur שׁוּר תְשׁוּרֶ֑/נּוּ | nasa נָשָׂא אֶשָּׂ֣א | 5 |  |
| 501 | Job 38:17 → Job 38:13 | ra'ah רָאָה תִּרְאֶֽה | achaz אָחַז לֶ֭/אֱחֹז | 4 |  |
| 502 | Job 38:17 → Job 38:20 | ra'ah רָאָה תִּרְאֶֽה | laqach לָקַח תִ֭קָּחֶ/נּוּ | 3 |  |
| 503 | Job 42:5 → Job 42:8 | ra'ah רָאָה רָאָֽתְ/ךָ | laqach לָקַח קְחֽוּ; nasa נָשָׂא אֶשָּׂ֗א | 3 |  |
| 504 | Job 42:5 → Job 42:9 | ra'ah רָאָה רָאָֽתְ/ךָ | nasa נָשָׂא וַ/יִּשָּׂ֥א | 4 |  |
| 505 | Psalms 27:13 → Psalms 28:2 | ra'ah רָאָה לִ/רְא֥וֹת | nasa נָשָׂא בְּ/נָשְׂאִ֥/י | 3 |  |
| 506 | Psalms 49:11 → Psalms 49:16 | ra'ah רָאָה יִרְאֶ֨ה | laqach לָקַח יִקָּחֵ֣/נִי | 5 |  |
| 507 | Psalms 49:20 → Psalms 49:16 | ra'ah רָאָה יִרְאוּ | laqach לָקַח יִקָּחֵ֣/נִי | 4 |  |
| 508 | Psalms 55:10 → Psalms 55:13 | ra'ah רָאָה רָאִ֨יתִי | nasa נָשָׂא וְ/אֶ֫שָּׂ֥א | 3 |  |
| 509 | Psalms 85:8 → Psalms 85:3 | ra'ah רָאָה הַרְאֵ֣/נוּ | nasa נָשָׂא נָ֭שָׂאתָ | 5 |  |
| 510 | Psalms 91:8 → Psalms 91:12 | nabat נָבַט תַבִּ֑יט; ra'ah רָאָה תִּרְאֶֽה | nasa נָשָׂא יִשָּׂא֑וּ/נְ/ךָ | 4 |  |
| 511 | Psalms 91:16 → Psalms 91:12 | ra'ah רָאָה וְ֝/אַרְאֵ֗/הוּ | nasa נָשָׂא יִשָּׂא֑וּ/נְ/ךָ | 4 | chashaq חָשַׁק (Psalms 91:14) |
| 512 | Psalms 94:7 → Psalms 94:2 | ra'ah רָאָה יִרְאֶה | nasa נָשָׂא הִ֭נָּשֵׂא | 5 |  |
| 513 | Psalms 139:16 → Psalms 139:20 | ra'ah רָאָה רָ֘א֤וּ | nasa נָשָׂא נָשֻׂ֖א | 4 |  |
| 514 | Psalms 139:24 → Psalms 139:20 | ra'ah רָאָה וּ/רְאֵ֗ה | nasa נָשָׂא נָשֻׂ֖א | 4 |  |
| 515 | Proverbs 6:6 → Proverbs 6:2 | ra'ah רָאָה רְאֵ֖ה | lakad לָכַד נִ֝לְכַּ֗דְתָּ | 4 |  |
| 516 | Proverbs 20:12 → Proverbs 20:16 | ra'ah רָאָה רֹאָ֑ה | laqach לָקַח לְֽקַח | 4 |  |
| 517 | Proverbs 22:29 → Proverbs 22:25 | chazah חָזָה חָזִ֡יתָ | laqach לָקַח וְ/לָקַחְתָּ֖ | 4 |  |
| 518 | Ecclesiastes 1:16 → Ecclesiastes 2:3 | ra'ah רָאָה רָאָ֥ה | achaz אָחַז וְ/לֶ/אֱחֹ֣ז | 5 |  |
| 519 | Ecclesiastes 5:17 → Ecclesiastes 5:14 | ra'ah רָאָה רָאִ֣יתִי; ra'ah רָאָה וְ/לִ/רְא֨וֹת | nasa נָשָׂא יִשָּׂ֣א | 3 |  |
| 520 | Ecclesiastes 7:13 → Ecclesiastes 7:18 | ra'ah רָאָה רְאֵ֖ה | achaz אָחַז תֶּאֱחֹ֣ז | 5 |  |
| 521 | Ecclesiastes 7:14 → Ecclesiastes 7:18 | ra'ah רָאָה רְאֵ֑ה | achaz אָחַז תֶּאֱחֹ֣ז | 4 |  |
| 522 | Ecclesiastes 7:15 → Ecclesiastes 7:18 | ra'ah רָאָה רָאִ֖יתִי | achaz אָחַז תֶּאֱחֹ֣ז | 3 |  |
| 523 | Ecclesiastes 7:29 → Ecclesiastes 7:26 | ra'ah רָאָה רְאֵה | lakad לָכַד יִלָּ֥כֶד | 3 |  |
| 524 | Ecclesiastes 9:9 → Ecclesiastes 9:12 | ra'ah רָאָה רְאֵ֨ה | achaz אָחַז שֶׁ/נֶּֽאֱחָזִים֙; achaz אָחַז הָ/אֲחֻז֖וֹת | 3 |  |
| 525 | Song of Songs 2:12 → Song of Songs 2:15 | ra'ah רָאָה נִרְא֣וּ | achaz אָחַז אֶֽחֱזוּ | 3 |  |
| 526 | Song of Songs 3:3 → Song of Songs 2:15 | ra'ah רָאָה רְאִיתֶֽם | achaz אָחַז אֶֽחֱזוּ | 5 |  |
| 527 | Song of Songs 3:3 → Song of Songs 3:8 | ra'ah רָאָה רְאִיתֶֽם | achaz אָחַז אֲחֻ֣זֵי | 5 |  |
| 528 | Song of Songs 3:11 → Song of Songs 3:8 | ra'ah רָאָה וּֽ/רְאֶ֛ינָה | achaz אָחַז אֲחֻ֣זֵי | 3 |  |
| 529 | Song of Songs 7:5 → Song of Songs 7:9 | tsaphah צָפָה צוֹפֶ֖ה | achaz אָחַז אֹֽחֲזָ֖ה | 4 |  |
| 530 | Song of Songs 7:13 → Song of Songs 7:9 | ra'ah רָאָה נִרְאֶ֞ה | achaz אָחַז אֹֽחֲזָ֖ה | 4 |  |
| 531 | Isaiah 2:1 → Isaiah 2:4 | chazah חָזָה חָזָ֔ה | nasa נָשָׂא יִשָּׂ֨א | 3 |  |
| 532 | Isaiah 5:30 → Isaiah 5:26 | nabat נָבַט וְ/נִבַּ֤ט | nasa נָשָׂא וְ/נָֽשָׂא | 4 |  |
| 533 | Isaiah 6:1 → Isaiah 5:26 | ra'ah רָאָה וָ/אֶרְאֶ֧ה | nasa נָשָׂא וְ/נָֽשָׂא | 5 |  |
| 534 | Isaiah 6:5 → Isaiah 6:1 | ra'ah רָאָה רָא֥וּ | nasa נָשָׂא וְ/נִשָּׂ֑א | 4 |  |
| 535 | Isaiah 6:1 → Isaiah 6:6 | ra'ah רָאָה וָ/אֶרְאֶ֧ה | laqach לָקַח לָקַ֖ח | 5 |  |
| 536 | Isaiah 6:9 → Isaiah 6:6 | ra'ah רָאָה וּ/רְא֥וּ; ra'ah רָאָה רָא֖וֹ | laqach לָקַח לָקַ֖ח | 3 |  |
| 537 | Isaiah 6:10 → Isaiah 6:6 | ra'ah רָאָה יִרְאֶ֨ה | laqach לָקַח לָקַ֖ח | 4 |  |
| 538 | Isaiah 21:6 → Isaiah 21:3 | tsaphah צָפָה הַֽ/מְצַפֶּ֔ה; ra'ah רָאָה יִרְאֶ֖ה | achaz אָחַז אֲחָז֔וּ/נִי | 3 |  |
| 539 | Isaiah 21:7 → Isaiah 21:3 | ra'ah רָאָה וְ/רָ֣אָה | achaz אָחַז אֲחָז֔וּ/נִי | 4 |  |
| 540 | Isaiah 22:9 → Isaiah 22:6 | ra'ah רָאָה רְאִיתֶ֖ם | nasa נָשָׂא נָשָׂ֣א | 3 |  |
| 541 | Isaiah 22:11 → Isaiah 22:6 | nabat נָבַט הִבַּטְתֶּם֙; ra'ah רָאָה רְאִיתֶֽם | nasa נָשָׂא נָשָׂ֣א | 5 |  |
| 542 | Isaiah 30:10 → Isaiah 30:6 | ra'ah רָאָה לָֽ/רֹאִים֙; ra'ah רָאָה תִרְא֔וּ; chazah חָזָה תֶחֱזוּ; chazah חָזָה חֲז֖וּ | nasa נָשָׂא יִשְׂאוּ֩ | 4 |  |
| 543 | Isaiah 30:20 → Isaiah 30:25 | ra'ah רָאָה רֹא֥וֹת | nasa נָשָׂא נִשָּׂאָ֔ה | 5 |  |
| 544 | Isaiah 30:30 → Isaiah 30:25 | ra'ah רָאָה יַרְאֶ֔ה | nasa נָשָׂא נִשָּׂאָ֔ה | 5 |  |
| 545 | Isaiah 33:15 → Isaiah 33:10 | ra'ah רָאָה מֵ/רְא֥וֹת | nasa נָשָׂא אֶנָּשֵֽׂא | 5 |  |
| 546 | Isaiah 33:17 → Isaiah 33:14 | chazah חָזָה תֶּחֱזֶ֣ינָה; ra'ah רָאָה תִּרְאֶ֖ינָה | achaz אָחַז אָחֲזָ֥ה | 3 |  |
| 547 | Isaiah 33:19 → Isaiah 33:14 | ra'ah רָאָה תִרְאֶ֑ה | achaz אָחַז אָחֲזָ֥ה | 5 |  |
| 548 | Isaiah 33:19 → Isaiah 33:24 | ra'ah רָאָה תִרְאֶ֑ה | nasa נָשָׂא נְשֻׂ֥א | 5 |  |
| 549 | Isaiah 33:20 → Isaiah 33:24 | chazah חָזָה חֲזֵ֣ה; ra'ah רָאָה תִרְאֶ֨ינָה | nasa נָשָׂא נְשֻׂ֥א | 4 |  |
| 550 | Isaiah 37:17 → Isaiah 37:14 | ra'ah רָאָה וּ/רְאֵ֑ה | laqach לָקַח וַ/יִּקַּ֨ח | 3 |  |
| 551 | Isaiah 39:2 → Isaiah 38:21 | ra'ah רָאָה וַ/יַּרְאֵ֣/ם; ra'ah רָאָה הֶרְאָ֧/ם | nasa נָשָׂא יִשְׂא֖וּ | 3 |  |
| 552 | Isaiah 39:4 → Isaiah 38:21 | ra'ah רָאָה רָא֖וּ; ra'ah רָאָה רָא֔וּ; ra'ah רָאָה הִרְאִיתִ֖י/ם | nasa נָשָׂא יִשְׂא֖וּ | 5 |  |
| 553 | Isaiah 39:2 → Isaiah 39:6 | ra'ah רָאָה וַ/יַּרְאֵ֣/ם; ra'ah רָאָה הֶרְאָ֧/ם | nasa נָשָׂא וְ/נִשָּׂ֣א | 4 |  |
| 554 | Isaiah 39:2 → Isaiah 39:7 | ra'ah רָאָה וַ/יַּרְאֵ֣/ם; ra'ah רָאָה הֶרְאָ֧/ם | laqach לָקַח יִקָּ֑חוּ | 5 |  |
| 555 | Isaiah 39:4 → Isaiah 39:7 | ra'ah רָאָה רָא֖וּ; ra'ah רָאָה רָא֔וּ; ra'ah רָאָה הִרְאִיתִ֖י/ם | laqach לָקַח יִקָּ֑חוּ | 3 |  |
| 556 | Isaiah 40:5 → Isaiah 40:2 | ra'ah רָאָה וְ/רָא֤וּ | laqach לָקַח לָקְחָה֙ | 3 |  |
| 557 | Isaiah 41:20 → Isaiah 41:16 | ra'ah רָאָה יִרְא֣וּ | nasa נָשָׂא תִּשָּׂאֵ֔/ם | 4 |  |
| 558 | Isaiah 41:28 → Isaiah 42:2 | ra'ah רָאָה וְ/אֵ֨רֶא֙ | nasa נָשָׂא יִשָּׂ֑א | 3 |  |
| 559 | Isaiah 44:9 → Isaiah 44:14 | ra'ah רָאָה יִרְא֛וּ | laqach לָקַח וַ/יִּקַּ֤ח | 5 | chamad חָמַד (Isaiah 44:9) |
| 560 | Isaiah 44:18 → Isaiah 44:14 | ra'ah רָאָה מֵֽ/רְאוֹת֙ | laqach לָקַח וַ/יִּקַּ֤ח | 4 |  |
| 561 | Isaiah 44:18 → Isaiah 44:15 | ra'ah רָאָה מֵֽ/רְאוֹת֙ | laqach לָקַח וַ/יִּקַּ֤ח | 3 |  |
| 562 | Isaiah 49:18 → Isaiah 49:22 | ra'ah רָאָה וּ/רְאִ֔י | nasa נָשָׂא אֶשָּׂ֤א; nasa נָשָׂא תִּנָּשֶֽׂאנָה | 4 |  |
| 563 | Isaiah 51:1 → Isaiah 51:6 | nabat נָבַט הַבִּ֨יטוּ֙ | nasa נָשָׂא שְׂאוּ֩ _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 564 | Isaiah 51:2 → Isaiah 51:6 | nabat נָבַט הַבִּ֨יטוּ֙ | nasa נָשָׂא שְׂאוּ֩ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 565 | Isaiah 52:8 → Isaiah 52:5 | tsaphah צָפָה צֹפַ֛יִ/ךְ; ra'ah רָאָה יִרְא֔וּ | laqach לָקַח לֻקַּ֥ח | 3 |  |
| 566 | Isaiah 52:10 → Isaiah 52:5 | ra'ah רָאָה וְ/רָאוּ֙ | laqach לָקַח לֻקַּ֥ח | 5 |  |
| 567 | Isaiah 52:8 → Isaiah 52:11 | tsaphah צָפָה צֹפַ֛יִ/ךְ; ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא נֹשְׂאֵ֖י | 3 |  |
| 568 | Isaiah 52:8 → Isaiah 52:13 | tsaphah צָפָה צֹפַ֛יִ/ךְ; ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא וְ/נִשָּׂ֛א | 5 |  |
| 569 | Isaiah 52:10 → Isaiah 52:13 | ra'ah רָאָה וְ/רָאוּ֙ | nasa נָשָׂא וְ/נִשָּׂ֛א | 3 |  |
| 570 | Isaiah 52:15 → Isaiah 52:11 | ra'ah רָאָה רָא֔וּ | nasa נָשָׂא נֹשְׂאֵ֖י | 4 |  |
| 571 | Isaiah 53:2 → Isaiah 52:13 | ra'ah רָאָה וְ/נִרְאֵ֥/הוּ | nasa נָשָׂא וְ/נִשָּׂ֛א | 4 | chamad חָמַד (Isaiah 53:2) |
| 572 | Isaiah 52:15 → Isaiah 53:4 | ra'ah רָאָה רָא֔וּ | nasa נָשָׂא נָשָׂ֔א | 4 | chamad חָמַד (Isaiah 53:2) |
| 573 | Isaiah 53:11 → Isaiah 53:8 | ra'ah רָאָה יִרְאֶ֣ה | laqach לָקַח לֻקָּ֔ח | 3 |  |
| 574 | Isaiah 57:8 → Isaiah 57:13 | chazah חָזָה חָזִֽית | nasa נָשָׂא יִשָּׂא; laqach לָקַח יִקַּח | 5 |  |
| 575 | Isaiah 57:18 → Isaiah 57:13 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא יִשָּׂא; laqach לָקַח יִקַּח | 5 |  |
| 576 | Isaiah 57:18 → Isaiah 57:15 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא וְ/נִשָּׂ֗א | 3 |  |
| 577 | Isaiah 60:2 → Isaiah 60:6 | ra'ah רָאָה יֵרָאֶֽה | nasa נָשָׂא יִשָּׂ֔אוּ | 4 |  |
| 578 | Isaiah 63:5 → Isaiah 63:9 | nabat נָבַט וְ/אַבִּיט֙ | nasa נָשָׂא וַֽ/יְנַשְּׂאֵ֖/ם | 4 |  |
| 579 | Isaiah 64:8 → Isaiah 64:5 | nabat נָבַט הַבֶּט | nasa נָשָׂא יִשָּׂאֻֽ/נוּ | 3 |  |
| 580 | Isaiah 66:8 → Isaiah 66:12 | ra'ah רָאָה רָאָה֙ | nasa נָשָׂא תִּנָּשֵׂ֔אוּ | 4 |  |
| 581 | Isaiah 66:18 → Isaiah 66:21 | ra'ah רָאָה וְ/רָא֥וּ | laqach לָקַח אֶקַּ֛ח | 3 |  |
| 582 | Isaiah 66:24 → Isaiah 66:21 | ra'ah רָאָה וְ/רָא֔וּ | laqach לָקַח אֶקַּ֛ח | 3 |  |
| 583 | Jeremiah 3:6 → Jeremiah 3:2 | ra'ah רָאָה הֲֽ/רָאִ֔יתָ | nasa נָשָׂא שְׂאִֽי _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 584 | Jeremiah 3:7 → Jeremiah 3:2 | ra'ah רָאָה ו/תראה; ra'ah רָאָה וַ/תֵּ֛רֶא | nasa נָשָׂא שְׂאִֽי _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 585 | Jeremiah 5:21 → Jeremiah 5:26 | ra'ah רָאָה יִרְא֔וּ | lakad לָכַד יִלְכֹּֽדוּ | 5 |  |
| 586 | Jeremiah 6:16 → Jeremiah 6:11 | ra'ah רָאָה וּ/רְא֜וּ | lakad לָכַד יִלָּכֵ֔דוּ | 5 |  |
| 587 | Jeremiah 7:11 → Jeremiah 7:16 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא תִּשָּׂ֧א | 5 |  |
| 588 | Jeremiah 7:12 → Jeremiah 7:16 | ra'ah רָאָה וּ/רְאוּ֙ | nasa נָשָׂא תִּשָּׂ֧א | 4 |  |
| 589 | Jeremiah 11:18 → Jeremiah 11:14 | ra'ah רָאָה הִרְאִיתַ֥/נִי | nasa נָשָׂא תִּשָּׂ֥א | 4 |  |
| 590 | Jeremiah 13:26 → Jeremiah 13:21 | ra'ah רָאָה וְ/נִרְאָ֖ה | achaz אָחַז יֹאחֱז֔וּ/ךְ | 5 |  |
| 591 | Jeremiah 18:17 → Jeremiah 18:22 | ra'ah רָאָה אֶרְאֵ֖/ם | lakad לָכַד לְ/לָכְדֵ֔/נִי | 5 |  |
| 592 | Jeremiah 32:24 → Jeremiah 32:28 | ra'ah רָאָה רֹאֶֽה | lakad לָכַד וּ/לְכָדָֽ/הּ | 4 |  |
| 593 | Jeremiah 33:24 → Jeremiah 34:3 | ra'ah רָאָה רָאִ֗יתָ | taphas תָּפַשׂ תָּפֹ֣שׂ; taphas תָּפַשׂ תִּתָּפֵ֔שׂ | 5 |  |
| 594 | Jeremiah 34:3 → Jeremiah 33:26 | ra'ah רָאָה תִּרְאֶ֗ינָה | laqach לָקַח מִ/קַּ֤חַת | 3 |  |
| 595 | Jeremiah 39:4 → Jeremiah 38:28 | ra'ah רָאָה רָ֠אָ/ם | lakad לָכַד נִלְכְּדָ֣ה; lakad לָכַד נִלְכְּדָ֖ה | 4 |  |
| 596 | Jeremiah 40:4 → Jeremiah 40:1 | ra'ah רָאָה רְאֵה֙ | laqach לָקַח בְּ/קַחְתּ֣/וֹ | 3 |  |
| 597 | Jeremiah 41:13 → Jeremiah 41:16 | ra'ah רָאָה כִּ/רְא֤וֹת | laqach לָקַח וַ/יִּקַּח֩ | 3 |  |
| 598 | Jeremiah 42:2 → Jeremiah 41:16 | ra'ah רָאָה רֹא֥וֹת | laqach לָקַח וַ/יִּקַּח֩ | 4 |  |
| 599 | Jeremiah 44:2 → Jeremiah 43:10 | ra'ah רָאָה רְאִיתֶ֗ם | laqach לָקַח וְ֠/לָקַחְתִּי | 5 |  |
| 600 | Jeremiah 44:17 → Jeremiah 44:12 | ra'ah רָאָה רָאִֽינוּ | laqach לָקַח וְ/לָקַחְתִּ֞י | 5 |  |
| 601 | Jeremiah 44:17 → Jeremiah 44:14 | ra'ah רָאָה רָאִֽינוּ | nasa נָשָׂא מְנַשְּׂאִ֤ים | 3 |  |
| 602 | Jeremiah 44:17 → Jeremiah 44:22 | ra'ah רָאָה רָאִֽינוּ | nasa נָשָׂא לָ/שֵׂ֗את | 5 |  |
| 603 | Jeremiah 46:5 → Jeremiah 46:9 | ra'ah רָאָה רָאִ֗יתִי | taphas תָּפַשׂ תֹּפְשֵׂ֣י; taphas תָּפַשׂ תֹּפְשֵׂ֖י | 4 |  |
| 604 | Jeremiah 51:61 → Jeremiah 51:56 | ra'ah רָאָה וְֽ/רָאִ֔יתָ | lakad לָכַד וְ/נִלְכְּדוּ֙ | 5 |  |
| 605 | Lamentations 2:14 → Lamentations 2:19 | chazah חָזָה חָ֤זוּ; chazah חָזָה וַ/יֶּ֣חֱזוּ | nasa נָשָׂא שְׂאִ֧י | 5 |  |
| 606 | Lamentations 2:16 → Lamentations 2:19 | ra'ah רָאָה רָאִֽינוּ | nasa נָשָׂא שְׂאִ֧י | 3 |  |
| 607 | Lamentations 3:1 → Lamentations 2:19 | ra'ah רָאָה רָאָ֣ה | nasa נָשָׂא שְׂאִ֧י | 4 |  |
| 608 | Lamentations 3:36 → Lamentations 3:41 | ra'ah רָאָה רָאָֽה | nasa נָשָׂא נִשָּׂ֤א | 5 |  |
| 609 | Lamentations 4:16 → Lamentations 4:20 | nabat נָבַט לְ/הַבִּיטָ֑/ם | lakad לָכַד נִלְכַּ֖ד | 4 |  |
| 610 | Lamentations 4:17 → Lamentations 4:20 | tsaphah צָפָה צִפִּ֔ינוּ | lakad לָכַד נִלְכַּ֖ד | 3 |  |
| 611 | Lamentations 5:1 → Lamentations 4:20 | nabat נָבַט הביט; nabat נָבַט הַבִּ֖יטָ/ה; ra'ah רָאָה וּ/רְאֵ֥ה | lakad לָכַד נִלְכַּ֖ד | 3 |  |
| 612 | Ezekiel 1:1 → Ezekiel 1:4 | ra'ah רָאָה וָ/אֶרְאֶ֖ה | laqach לָקַח מִתְלַקַּ֔חַת | 3 |  |
| 613 | Ezekiel 1:15 → Ezekiel 1:19 | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא וּ/בְ/הִנָּשֵׂ֤א; nasa נָשָׂא יִנָּשְׂא֖וּ | 4 |  |
| 614 | Ezekiel 1:15 → Ezekiel 1:20 | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא יִנָּשְׂאוּ֙ | 5 |  |
| 615 | Ezekiel 3:17 → Ezekiel 3:12 | tsaphah צָפָה צֹפֶ֥ה | nasa נָשָׂא וַ/תִּשָּׂאֵ֣/נִי | 5 |  |
| 616 | Ezekiel 3:17 → Ezekiel 3:14 | tsaphah צָפָה צֹפֶ֥ה | nasa נָשָׂא נְשָׂאַ֖תְ/נִי; laqach לָקַח וַ/תִּקָּחֵ֑/נִי | 3 |  |
| 617 | Ezekiel 3:23 → Ezekiel 4:1 | ra'ah רָאָה רָאִ֖יתִי | laqach לָקַח קַח | 5 |  |
| 618 | Ezekiel 4:15 → Ezekiel 5:1 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח קַח; laqach לָקַח תִּקָּחֶ֣/נָּה; laqach לָקַח וְ/לָקַחְתָּ֥ | 3 |  |
| 619 | Ezekiel 4:15 → Ezekiel 5:2 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וְ/לָֽקַחְתָּ֣ | 4 |  |
| 620 | Ezekiel 4:15 → Ezekiel 5:3 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וְ/לָקַחְתָּ֥ | 5 |  |
| 621 | Ezekiel 8:2 → Ezekiel 8:5 | ra'ah רָאָה וָ/אֶרְאֶ֗ה | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 622 | Ezekiel 8:6 → Ezekiel 8:3 | ra'ah רָאָה הֲ/רֹאֶ֥ה; ra'ah רָאָה תִּרְאֶ֔ה | laqach לָקַח וַ/יִּקָּחֵ֖/נִי; nasa נָשָׂא וַ/תִּשָּׂ֣א | 3 |  |
| 623 | Ezekiel 8:7 → Ezekiel 8:3 | ra'ah רָאָה וָ/אֶרְאֶ֕ה | laqach לָקַח וַ/יִּקָּחֵ֖/נִי; nasa נָשָׂא וַ/תִּשָּׂ֣א | 4 |  |
| 624 | Ezekiel 8:9 → Ezekiel 8:5 | ra'ah רָאָה וּ/רְאֵה֙ | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 625 | Ezekiel 8:10 → Ezekiel 8:5 | ra'ah רָאָה וָֽ/אֶרְאֶה֒ | nasa נָשָׂא שָׂא; nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 626 | Ezekiel 10:1 → Ezekiel 10:6 | ra'ah רָאָה וָ/אֶרְאֶ֗ה; ra'ah רָאָה נִרְאָ֖ה | laqach לָקַח קַ֥ח | 5 |  |
| 627 | Ezekiel 10:9 → Ezekiel 10:6 | ra'ah רָאָה וָ/אֶרְאֶ֗ה | laqach לָקַח קַ֥ח | 3 |  |
| 628 | Ezekiel 10:15 → Ezekiel 10:19 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 629 | Ezekiel 10:20 → Ezekiel 10:16 | ra'ah רָאָה רָאִ֛יתִי | nasa נָשָׂא וּ/בִ/שְׂאֵ֨ת | 4 |  |
| 630 | Ezekiel 10:22 → Ezekiel 10:19 | ra'ah רָאָה רָאִ֨יתִי֙ | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 631 | Ezekiel 11:1 → Ezekiel 10:19 | ra'ah רָאָה וָ/אֶרְאֶ֨ה | nasa נָשָׂא וַ/יִּשְׂא֣וּ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 632 | Ezekiel 10:20 → Ezekiel 11:1 | ra'ah רָאָה רָאִ֛יתִי | nasa נָשָׂא וַ/תִּשָּׂ֨א | 3 |  |
| 633 | Ezekiel 11:25 → Ezekiel 11:22 | ra'ah רָאָה הֶרְאָֽ/נִי | nasa נָשָׂא וַ/יִּשְׂא֤וּ | 3 |  |
| 634 | Ezekiel 12:2 → Ezekiel 11:22 | ra'ah רָאָה לִ/רְא֜וֹת; ra'ah רָאָה רָא֗וּ | nasa נָשָׂא וַ/יִּשְׂא֤וּ | 5 |  |
| 635 | Ezekiel 12:2 → Ezekiel 11:24 | ra'ah רָאָה לִ/רְא֜וֹת; ra'ah רָאָה רָא֗וּ | nasa נָשָׂא נְשָׂאַ֗תְ/נִי | 3 |  |
| 636 | Ezekiel 12:3 → Ezekiel 11:24 | ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא נְשָׂאַ֗תְ/נִי | 4 |  |
| 637 | Ezekiel 12:2 → Ezekiel 12:6 | ra'ah רָאָה לִ/רְא֜וֹת; ra'ah רָאָה רָא֗וּ | nasa נָשָׂא תִּשָּׂא֙ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 638 | Ezekiel 12:2 → Ezekiel 12:7 | ra'ah רָאָה לִ/רְא֜וֹת; ra'ah רָאָה רָא֗וּ | nasa נָשָׂא נָשָׂ֖אתִי _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 639 | Ezekiel 12:3 → Ezekiel 12:6 | ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא תִּשָּׂא֙ _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 640 | Ezekiel 12:3 → Ezekiel 12:7 | ra'ah רָאָה יִרְא֔וּ | nasa נָשָׂא נָשָׂ֖אתִי _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 641 | Ezekiel 12:12 → Ezekiel 12:7 | ra'ah רָאָה יִרְאֶ֥ה | nasa נָשָׂא נָשָׂ֖אתִי _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 642 | Ezekiel 13:23 → Ezekiel 14:5 | chazah חָזָה תֶחֱזֶ֔ינָה | taphas תָּפַשׂ תְּפֹ֥שׂ | 5 |  |
| 643 | Ezekiel 14:22 → Ezekiel 15:3 | ra'ah רָאָה וּ/רְאִיתֶ֥ם | laqach לָקַח הֲ/יֻקַּ֤ח; laqach לָקַח יִקְח֤וּ | 4 |  |
| 644 | Ezekiel 14:23 → Ezekiel 15:3 | ra'ah רָאָה תִרְא֥וּ | laqach לָקַח הֲ/יֻקַּ֤ח; laqach לָקַח יִקְח֤וּ | 3 |  |
| 645 | Ezekiel 16:37 → Ezekiel 16:32 | ra'ah רָאָה וְ/רָא֖וּ | laqach לָקַח תִּקַּ֖ח | 5 |  |
| 646 | Ezekiel 16:50 → Ezekiel 16:54 | ra'ah רָאָה רָאִֽיתִי | nasa נָשָׂא תִּשְׂאִ֣י | 4 |  |
| 647 | Ezekiel 18:14 → Ezekiel 18:17 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | laqach לָקַח לָקָ֔ח | 3 |  |
| 648 | Ezekiel 18:14 → Ezekiel 18:18 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | gazal גָּזַל גָּזַל֙ | 4 |  |
| 649 | Ezekiel 18:14 → Ezekiel 18:19 | ra'ah רָאָה וַ/יַּ֕רְא; ra'ah רָאָה וַ/יִּרְאֶ֕ה | nasa נָשָׂא נָשָׂ֥א | 5 |  |
| 650 | Ezekiel 18:28 → Ezekiel 19:1 | ra'ah רָאָה וַ/יִּרְאֶ֣ה | nasa נָשָׂא שָׂ֣א | 5 |  |
| 651 | Ezekiel 19:5 → Ezekiel 19:1 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | nasa נָשָׂא שָׂ֣א | 4 |  |
| 652 | Ezekiel 19:5 → Ezekiel 19:8 | ra'ah רָאָה וַ/תֵּ֨רֶא֙ | taphas תָּפַשׂ נִתְפָּֽשׂ | 3 |  |
| 653 | Ezekiel 19:11 → Ezekiel 19:8 | ra'ah רָאָה וַ/יֵּרָ֣א | taphas תָּפַשׂ נִתְפָּֽשׂ | 3 |  |
| 654 | Ezekiel 20:28 → Ezekiel 20:23 | ra'ah רָאָה וַ/יִּרְאוּ֩ | nasa נָשָׂא נָשָׂ֧אתִי | 5 |  |
| 655 | Ezekiel 20:28 → Ezekiel 20:31 | ra'ah רָאָה וַ/יִּרְאוּ֩ | nasa נָשָׂא וּ/בִ/שְׂאֵ֣ת | 3 |  |
| 656 | Ezekiel 21:26 → Ezekiel 21:29 | ra'ah רָאָה רָאָ֖ה | taphas תָּפַשׂ תִּתָּפֵֽשׂוּ | 3 |  |
| 657 | Ezekiel 21:34 → Ezekiel 21:29 | chazah חָזָה בַּ/חֲז֥וֹת | taphas תָּפַשׂ תִּתָּפֵֽשׂוּ | 5 |  |
| 658 | Ezekiel 23:13 → Ezekiel 23:10 | ra'ah רָאָה וָ/אֵ֖רֶא | laqach לָקַח לָקָ֔חוּ | 3 |  |
| 659 | Ezekiel 23:14 → Ezekiel 23:10 | ra'ah רָאָה וַ/תֵּ֗רֶא | laqach לָקַח לָקָ֔חוּ | 4 |  |
| 660 | Ezekiel 28:17 → Ezekiel 28:12 | ra'ah רָאָה לְ/רַ֥אֲוָה | nasa נָשָׂא שָׂ֥א | 5 |  |
| 661 | Ezekiel 33:2 → Ezekiel 32:30 | tsaphah צָפָה לְ/צֹפֶֽה | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 4 |  |
| 662 | Ezekiel 33:3 → Ezekiel 32:30 | ra'ah רָאָה וְ/רָאָ֥ה | nasa נָשָׂא וַ/יִּשְׂא֥וּ | 5 |  |
| 663 | Ezekiel 32:31 → Ezekiel 33:2 | ra'ah רָאָה יִרְאֶ֣ה | laqach לָקַח וְ/לָקְח֨וּ | 3 |  |
| 664 | Ezekiel 32:31 → Ezekiel 33:4 | ra'ah רָאָה יִרְאֶ֣ה | laqach לָקַח וַ/תִּקָּחֵ֑/הוּ | 5 |  |
| 665 | Ezekiel 33:6 → Ezekiel 33:2 | tsaphah צָפָה וְ֠/הַ/צֹּפֶה; ra'ah רָאָה יִרְאֶ֨ה; tsaphah צָפָה הַ/צֹּפֶ֥ה | laqach לָקַח וְ/לָקְח֨וּ | 4 |  |
| 666 | Ezekiel 33:7 → Ezekiel 33:2 | tsaphah צָפָה צֹפֶ֥ה | laqach לָקַח וְ/לָקְח֨וּ | 5 |  |
| 667 | Ezekiel 33:2 → Ezekiel 33:6 | tsaphah צָפָה לְ/צֹפֶֽה | laqach לָקַח וַ/תִּקַּ֥ח; laqach לָקַח נִלְקָ֔ח | 4 |  |
| 668 | Ezekiel 33:3 → Ezekiel 33:6 | ra'ah רָאָה וְ/רָאָ֥ה | laqach לָקַח וַ/תִּקַּ֥ח; laqach לָקַח נִלְקָ֔ח | 3 |  |
| 669 | Ezekiel 33:7 → Ezekiel 33:4 | tsaphah צָפָה צֹפֶ֥ה | laqach לָקַח וַ/תִּקָּחֵ֑/הוּ | 3 |  |
| 670 | Ezekiel 39:15 → Ezekiel 39:10 | ra'ah רָאָה וְ/רָאָה֙ | nasa נָשָׂא יִשְׂא֨וּ | 5 |  |
| 671 | Ezekiel 39:21 → Ezekiel 39:26 | ra'ah רָאָה וְ/רָא֣וּ | nasa נָשָׂא וְ/נָשׂוּ֙ | 5 |  |
| 672 | Ezekiel 44:5 → Ezekiel 44:10 | ra'ah רָאָה וּ/רְאֵ֨ה | nasa נָשָׂא וְ/נָשְׂא֖וּ | 5 |  |
| 673 | Daniel 1:13 → Daniel 1:16 | ra'ah רָאָה וְ/יֵרָא֤וּ; ra'ah רָאָה תִּרְאֵ֔ה | nasa נָשָׂא נֹשֵׂא֙ | 3 |  |
| 674 | Daniel 8:6 → Daniel 8:3 | ra'ah רָאָה רָאִ֔יתִי | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 675 | Daniel 8:7 → Daniel 8:3 | ra'ah רָאָה וּ/רְאִיתִ֞י/ו | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 676 | Daniel 10:8 → Daniel 10:5 | ra'ah רָאָה וָֽ/אֶרְאֶ֗ה | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 677 | Hosea 13:7 → Hosea 13:11 | shur שׁוּר אָשֽׁוּר | laqach לָקַח וְ/אֶקַּ֖ח | 4 |  |
| 678 | Amos 3:9 → Amos 3:4 | ra'ah רָאָה וּ/רְא֞וּ | lakad לָכַד לָכָֽד | 5 |  |
| 679 | Amos 3:9 → Amos 3:5 | ra'ah רָאָה וּ/רְא֞וּ | lakad לָכַד וְ/לָכ֖וֹד; lakad לָכַד יִלְכּֽוֹד | 4 |  |
| 680 | Amos 5:22 → Amos 5:26 | nabat נָבַט אַבִּֽיט | nasa נָשָׂא וּ/נְשָׂאתֶ֗ם | 4 |  |
| 681 | Amos 6:2 → Amos 5:26 | ra'ah רָאָה וּ/רְא֔וּ | nasa נָשָׂא וּ/נְשָׂאתֶ֗ם | 3 |  |
| 682 | Amos 7:1 → Amos 6:10 | ra'ah רָאָה הִרְאַ֨/נִי֙ | nasa נָשָׂא וּ/נְשָׂא֞/וֹ | 5 |  |
| 683 | Amos 7:4 → Amos 6:13 | ra'ah רָאָה הִרְאַ֨/נִי֙ | laqach לָקַח לָקַ֥חְנוּ | 5 |  |
| 684 | Amos 8:1 → Amos 7:15 | ra'ah רָאָה הִרְאַ֖/נִי | laqach לָקַח וַ/יִּקָּחֵ֣/נִי | 3 |  |
| 685 | Amos 8:2 → Amos 7:15 | ra'ah רָאָה רֹאֶה֙ | laqach לָקַח וַ/יִּקָּחֵ֣/נִי | 4 |  |
| 686 | Jonah 3:10 → Jonah 4:3 | ra'ah רָאָה וַ/יַּ֤רְא | laqach לָקַח קַח | 3 |  |
| 687 | Micah 7:4 → Micah 6:16 | tsaphah צָפָה מְצַפֶּ֨י/ךָ֙ | nasa נָשָׂא תִּשָּֽׂאוּ | 4 | avah אָוָה (Micah 7:1) |
| 688 | Micah 7:4 → Micah 7:9 | tsaphah צָפָה מְצַפֶּ֨י/ךָ֙ | nasa נָשָׂא אֶשָּׂ֔א | 5 |  |
| 689 | Micah 7:15 → Micah 7:18 | ra'ah רָאָה אַרְאֶ֖/נּוּ | nasa נָשָׂא נֹשֵׂ֤א | 3 |  |
| 690 | Habakkuk 1:5 → Habakkuk 1:10 | ra'ah רָאָה רְא֤וּ; nabat נָבַט וְֽ/הַבִּ֔יטוּ | lakad לָכַד וַֽ/יִּלְכְּדָֽ/הּ | 5 |  |
| 691 | Habakkuk 1:13 → Habakkuk 1:10 | ra'ah רָאָה מֵ/רְא֣וֹת; nabat נָבַט וְ/הַבִּ֥יט; nabat נָבַט תַבִּיט֙ | lakad לָכַד וַֽ/יִּלְכְּדָֽ/הּ | 3 |  |
| 692 | Habakkuk 2:1 → Habakkuk 2:6 | tsaphah צָפָה וַ/אֲצַפֶּ֗ה; ra'ah רָאָה לִ/רְאוֹת֙ | nasa נָשָׂא יִשָּׂ֔אוּ | 5 |  |
| 693 | Habakkuk 2:15 → Habakkuk 2:19 | nabat נָבַט הַבִּ֖יט | taphas תָּפַשׂ תָּפוּשׂ֙ | 4 |  |
| 694 | Habakkuk 3:6 → Habakkuk 3:10 | ra'ah רָאָה רָאָה֙ | nasa נָשָׂא נָשָֽׂא | 4 |  |
| 695 | Habakkuk 3:7 → Habakkuk 3:10 | ra'ah רָאָה רָאִ֖יתִי | nasa נָשָׂא נָשָֽׂא | 3 |  |
| 696 | Zechariah 2:5 → Zechariah 2:1 | ra'ah רָאָה וָ/אֵ֖רֶא | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 697 | Zechariah 2:6 → Zechariah 2:1 | ra'ah רָאָה לִ/רְא֥וֹת | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 698 | Zechariah 2:1 → Zechariah 2:4 | ra'ah רָאָה וָ/אֵ֑רֶא | nasa נָשָׂא נָשָׂ֣א; nasa נָשָׂא הַ/נֹּשְׂאִ֥ים | 3 |  |
| 699 | Zechariah 2:1 → Zechariah 2:5 | ra'ah רָאָה וָ/אֵ֑רֶא | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 700 | Zechariah 4:10 → Zechariah 5:1 | ra'ah רָאָה וְ/רָא֞וּ | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 5 |  |
| 701 | Zechariah 5:5 → Zechariah 5:1 | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא וָ/אֶשָּׂ֥א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 702 | Zechariah 5:1 → Zechariah 5:5 | ra'ah רָאָה וָֽ/אֶרְאֶ֑ה | nasa נָשָׂא שָׂ֣א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 703 | Zechariah 5:2 → Zechariah 5:5 | ra'ah רָאָה רֹאֶ֑ה; ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא שָׂ֣א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 704 | Zechariah 5:2 → Zechariah 5:7 | ra'ah רָאָה רֹאֶ֑ה; ra'ah רָאָה רֹאֶה֙ | nasa נָשָׂא נִשֵּׂ֑את | 5 |  |
| 705 | Zechariah 5:9 → Zechariah 5:5 | ra'ah רָאָה וָ/אֵ֗רֶא | nasa נָשָׂא שָׂ֣א _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 706 | Zechariah 5:5 → Zechariah 5:9 | ra'ah רָאָה וּ/רְאֵ֔ה | nasa נָשָׂא וָ/אֶשָּׂ֨א; nasa נָשָׂא וַ/תִּשֶּׂ֨אנָה֙ _(nasa 'lift-eyes' idiom)_ | 4 |  |
| 707 | Zechariah 6:1 → Zechariah 5:7 | ra'ah רָאָה וָֽ/אֶרְאֶ֔ה | nasa נָשָׂא נִשֵּׂ֑את | 5 |  |
| 708 | Zechariah 6:1 → Zechariah 5:9 | ra'ah רָאָה וָֽ/אֶרְאֶ֔ה | nasa נָשָׂא וָ/אֶשָּׂ֨א; nasa נָשָׂא וַ/תִּשֶּׂ֨אנָה֙ _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 709 | Zechariah 5:9 → Zechariah 6:1 | ra'ah רָאָה וָ/אֵ֗רֶא | nasa נָשָׂא וָ/אֶשָּׂ֤א _(nasa 'lift-eyes' idiom)_ | 3 |  |
| 710 | Zechariah 6:8 → Zechariah 6:11 | ra'ah רָאָה רְאֵ֗ה | laqach לָקַח וְ/לָקַחְתָּ֥ | 3 |  |
| 711 | Zechariah 6:8 → Zechariah 6:13 | ra'ah רָאָה רְאֵ֗ה | nasa נָשָׂא יִשָּׂ֣א | 5 |  |
| 712 | Malachi 1:5 → Malachi 1:8 | ra'ah רָאָה תִּרְאֶ֑ינָה | nasa נָשָׂא הֲ/יִשָּׂ֣א | 3 |  |
| 713 | Malachi 1:5 → Malachi 1:9 | ra'ah רָאָה תִּרְאֶ֑ינָה | nasa נָשָׂא הֲ/יִשָּׂ֤א | 4 |  |


---

## Appendix C — Data and code

| File | Contents |
|---|---|
| `research/data/cooccurrences.csv` / `.json` | the canonical catalogue: every pair, with references, Hebrew forms, tier, desire-flag, and idiom-flag |
| `research/data/summary.json` | aggregate counts |
| `research/data/tier1_categories.json` | the hand-adjudicated Tier-1 categories |
| `research/scripts/*.py` | the sweep, table-builder, and classifier |

---

## Bibliography

The works below are cited in §§5–6. Each carries the confidence tag used throughout; **[confirmed]** items were located while preparing this report, **[general-knowledge]** items are standard attributions to real works that should be checked against the text before quotation.

Every attribution in §§5–6 was put through an independent adversarial verification pass. Two corrections from that pass are recorded here: **Cassuto** is *not* a witness for the Genesis 3→6 "saw…took" echo — in his comment on 6:2 he reads "took … wives" as ordinary lawful marriage and derives "good/fair" from Exodus 2:2, explicitly resisting a transgression reading; the report therefore cites Wenham for the echo and cites Cassuto for his dissent. And the **Sternberg, p. 365** locator is *Kline's* citation of Sternberg, not an independently confirmed page (Sternberg's principal David-and-Bathsheba analysis sits earlier in the volume).

**Primary texts and data**

- *Biblia Hebraica* — Westminster Leningrad Codex, tagged edition: **Open Scriptures Hebrew Bible (MorphHB)**, <https://hb.openscriptures.org/>. Morphology layer CC BY 4.0. `[confirmed — the study's data source]`
- *1 Enoch*, **Book of the Watchers** (chs. 6–11), esp. 6:1–8:4 — in the host edition (R. H. Charles, 1893; Nickelsburg & VanderKam, Hermeneia, 2013). `[confirmed — the host edition]`
- *Jubilees* 5. `[general-knowledge — real text; not in the host edition]`
- Scripture in English: ESV; verse-level quotations in §5 from **Revised JPS (2023)** and the **Miqra according to the Masorah** Hebrew, retrieved via Sefaria. `[confirmed — fetched]`

**Modern commentary and literary criticism**

- Robert Alter, *The Art of Biblical Narrative* (Basic Books, 1981; rev. 2011). `[confirmed]`
- Robert Alter, *The David Story: A Translation with Commentary of 1 and 2 Samuel* (Norton, 1999). `[general-knowledge]`
- Martin Buber, "Leitwort Style in Pentateuch Narrative" (1927) & Franz Rosenzweig, "The Secret of the Form of the Biblical Narratives" (1928), in *Scripture and Translation*, trans. L. Rosenwald & E. Fox (Indiana Univ. Press, 1994). `[confirmed]`
- Umberto Cassuto, *A Commentary on the Book of Genesis, Part I: From Adam to Noah*, trans. I. Abrahams (Magnes, ET 1961). *Cited for his dissent on Gen 6:2 (lawful marriage; "good" via Exod 2:2), not for the 3→6 echo.* `[confirmed]`
- Michael Fishbane, *Biblical Interpretation in Ancient Israel* (Clarendon/Oxford, 1985). `[confirmed]`
- J. P. Fokkelman, *Narrative Art and Poetry in the Books of Samuel*, vol. 1: *King David* (Van Gorcum, 1981). `[confirmed]`
- Moshe Garsiel, *The First Book of Samuel: A Literary Study of Comparative Structures, Analogies and Parallels* (Rubin Mass, 1985). `[confirmed — as cited by Kline]`
- Joanna Kline, *Narrative Analogy in the David Story: Parallels between Genesis 25–50 and 1 Samuel 16–1 Kings 2* (Mohr Siebeck, 2024); and "Narrative Analogy in the David Story," *Bible Interp* (2025). `[confirmed]`
- Meir Sternberg, *The Poetics of Biblical Narrative* (Indiana Univ. Press, 1985). `[confirmed — work; the "p. 365" locator is Kline's citation]`
- Gordon J. Wenham, *Genesis 1–15* (Word Biblical Commentary 1; Word, 1987). `[confirmed — verify exact page for the 6:2 comment]`
- Gordon J. Wenham, "Original Sin in Genesis 1–11," *Churchman* 104/4 (1990). `[confirmed — PDF]`
- Nahum Sarna, *The JPS Torah Commentary: Genesis* (JPS, 1989); *Understanding Genesis* (Schocken, 1966). `[confirmed — work]`

**Second Temple and its scholarship**

- Loren T. Stuckenbruck, "The 'Angels' and 'Giants' of Genesis 6:1–4 in Second and Third Century BCE Jewish Interpretation," *Dead Sea Discoveries* 7.3 (2000). `[confirmed — real]`
- Annette Yoshiko Reed, *Fallen Angels and the History of Judaism and Christianity* (Cambridge Univ. Press, 2005). `[confirmed — real]`
- James L. Kugel, *How to Read the Bible* (Free Press, 2007); *Traditions of the Bible* (Harvard, 1998). `[confirmed — titles]`

**Rabbinic and medieval Jewish**

- *Bereshit (Genesis) Rabbah* 19:5 (on Gen 3:6); 26 (on Gen 6:2). `[confirmed — Sefaria]`
- Rashi; Ramban (Nachmanides); Ibn Ezra, on Genesis 3:6 and 6:2. `[confirmed — Sefaria]`

**Patristic and Reformation**

- Augustine, *Confessions* X.35 (*concupiscentia oculorum*); *City of God* XIV.13. `[confirmed]`
- John Calvin, *Commentary on Genesis* (on 3:6, 6:2). `[general-knowledge — real work]`
- Martin Luther, *Lectures on Genesis* (*Luther's Works* 1–2). `[general-knowledge — real work]`

**New Testament and reception**

- 1 John 2:16; James 1:14–15. `[confirmed]`
- Leonard Greenspoon, "Do Not Covet: Is It a Feeling or an Action?" *TheTorah.com* (2018). *On* חמד *ḥamad; the article contrasts* ḥamad *with* אוה *ʾawah (Deut 5:21), not with* ḥašaq. `[confirmed]`


---

*Hebrew text and morphology: Open Scriptures Hebrew Bible (MorphHB), Westminster Leningrad Codex, CC BY 4.0. Prepared as a companion to the 1 Enoch edition at mrla.ng.*

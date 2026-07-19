#!/usr/bin/env python3
"""Attach a hand-adjudicated category + gloss to each Tier-1 (same-verse)
co-occurrence, and regenerate the Tier-1 catalog table with those columns.

Categories:
  A  transgressive        illicit see -> (desire) -> take (sexual/property seizure)
  B  neutral / narrative  ordinary "saw ... took" (report, battle, procedure)
  C  righteous inversion  the pattern turned to good (cover, sacrifice, rescue, zeal)
  D  juridical / cultic    law, ritual, covenant, watchman-responsibility
  I  idiom / non-take      nasa in a non-acquisitive sense (lift eyes/voice/face,
                           bear guilt, carry) -- not a genuine "take"

The seeing verb is genuine in every row; category I marks rows where the
"taking" verb (almost always nasa H5375) does not denote acquisitive taking.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.abspath(os.path.join(HERE, "..", "data"))

# ref -> (category, gloss)
CLASS = {
    "Genesis 3:6":   ("A", "Eve saw the tree, desired (ta'avah/nechmad), and took — the archetypal see→desire→take"),
    "Genesis 6:2":   ("A", "The sons of God saw the daughters of men were fair and took wives — echo of 3:6"),
    "Genesis 9:23":  ("C", "Shem and Japheth took a garment to cover Noah, refusing to see his nakedness (inversion)"),
    "Genesis 12:15": ("A", "Pharaoh's princes saw Sarai's beauty; the woman was taken into his house"),
    "Genesis 13:10": ("I", "Lot lifted his eyes and saw the plain of the Jordan (nasa-enayim idiom)"),
    "Genesis 13:14": ("I", "'Lift your eyes and see' — God to Abram (nasa-enayim idiom)"),
    "Genesis 18:2":  ("I", "Abraham lifted his eyes and saw the three visitors (nasa-enayim idiom)"),
    "Genesis 21:16": ("I", "Hagar lifted her voice and wept, not wishing to see the child die (nasa-qol, non-take)"),
    "Genesis 22:4":  ("I", "Abraham lifted his eyes and saw the place afar off (nasa-enayim idiom)"),
    "Genesis 22:13": ("C", "Abraham saw the ram caught (achaz) and took (laqach) it as a substitute — redemptive"),
    "Genesis 24:63": ("I", "Isaac lifted his eyes and saw the camels coming (nasa-enayim idiom)"),
    "Genesis 24:64": ("I", "Rebekah lifted her eyes and saw Isaac (nasa-enayim idiom)"),
    "Genesis 28:6":  ("B", "Esau saw that Isaac blessed Jacob and charged him to take a wife (marriage narrative)"),
    "Genesis 30:9":  ("B", "Leah saw she had stopped bearing and took Zilpah to give to Jacob"),
    "Genesis 31:10": ("I", "Jacob in a dream lifted his eyes and saw the flock (nasa-enayim idiom)"),
    "Genesis 31:12": ("I", "'Lift your eyes and see' — the angel to Jacob (nasa-enayim idiom)"),
    "Genesis 31:50": ("B", "Laban: God will see between us if you take other wives (covenant witness)"),
    "Genesis 32:21": ("I", "Jacob hopes Esau will 'lift his face' (accept him) when he sees him (nasa-panim, non-take)"),
    "Genesis 33:1":  ("I", "Jacob lifted his eyes and saw Esau approaching (nasa-enayim idiom)"),
    "Genesis 33:5":  ("I", "Esau lifted his eyes and saw the women and children (nasa-enayim idiom)"),
    "Genesis 33:10": ("B", "Jacob: if I have found favor, take my present — 'I have seen your face' (reconciliation gift)"),
    "Genesis 34:2":  ("A", "Shechem saw Dinah, took her, and violated her — see→take as sexual violence"),
    "Genesis 37:25": ("I", "Joseph's brothers lifted their eyes and saw the caravan (nasa-enayim idiom)"),
    "Genesis 38:2":  ("A", "Judah saw the daughter of Shua and took her (Kline links this to David/Bathsheba)"),
    "Genesis 43:29": ("I", "Joseph lifted his eyes and saw Benjamin (nasa-enayim idiom)"),
    "Genesis 45:27": ("I", "Jacob saw the wagons sent to carry (nasa) him and revived (non-take)"),
    "Exodus 2:5":    ("C", "Pharaoh's daughter saw the ark and took it — the taking preserves Moses' life"),
    "Exodus 19:4":   ("I", "'You have seen... how I bore (nasa) you on eagles' wings' (non-take)"),
    "Leviticus 5:1": ("D", "If a witness saw and does not testify, he bears (nasa) his iniquity (law)"),
    "Leviticus 20:17":("D", "If a man takes his sister and sees her nakedness, he bears (nasa) iniquity (incest law)"),
    "Numbers 17:24": ("B", "The chiefs saw and each took his rod (Aaron's budding staff, procedural)"),
    "Numbers 22:41": ("B", "Balak took Balaam up to a height to see the people of Israel"),
    "Numbers 23:28": ("B", "Balak took Balaam to Peor, overlooking (nishqaf) the wasteland"),
    "Numbers 24:2":  ("I", "Balaam lifted his eyes and saw Israel encamped (nasa-enayim idiom)"),
    "Numbers 24:20": ("I", "Balaam saw Amalek and took up (nasa) his oracle (nasa-mashal, non-take)"),
    "Numbers 24:21": ("I", "Balaam saw the Kenite and took up (nasa) his oracle (nasa-mashal, non-take)"),
    "Numbers 25:7":  ("C", "Phinehas saw the sin and took a spear to stay the plague — righteous zeal"),
    "Deuteronomy 1:31":("I", "'You saw how the LORD bore (nasa) you as a man carries his son' (non-take)"),
    "Deuteronomy 3:27":("I", "'Lift your eyes and see' — Moses on Pisgah (nasa-enayim idiom)"),
    "Deuteronomy 4:19":("I", "Lest you lift your eyes and see the host of heaven and worship it (nasa-enayim)"),
    "Deuteronomy 21:11":("D", "If you see a beautiful captive and desire (chashaq) her, you may take her — the pattern in law"),
    "Joshua 3:3":    ("I", "When you see the ark, which the priests bear (nasa), you shall follow (non-take)"),
    "Joshua 5:13":   ("I", "Joshua lifted his eyes and saw the captain of the LORD's host (nasa-enayim idiom)"),
    "Joshua 7:21":   ("A", "Achan: 'I saw... I coveted (chamad)... and took' — the explicit see→covet→take triad"),
    "Joshua 8:1":    ("B", "'See, I have given Ai into your hand; take all the people of war' (battle command)"),
    "Joshua 8:8":    ("B", "'When you have seized (taphas) the city... see, I have commanded you' (ambush)"),
    "Joshua 8:21":   ("B", "Joshua saw that the ambush had captured (lakad) the city and turned to fight"),
    "Judges 9:43":   ("B", "Abimelech saw the people come out and took his men in ambush (battle)"),
    "Judges 9:48":   ("B", "Abimelech took an axe and cut a branch; 'what you have seen me do, do quickly'"),
    "Judges 13:19":  ("B", "Manoah took the kid for offering while he and his wife looked on (theophany)"),
    "Judges 13:23":  ("B", "'The LORD would not have shown us all this, nor taken a burnt offering from us'"),
    "Judges 14:2":   ("A", "Samson saw a woman at Timnah: 'take her for me' — see→take driven by the eyes"),
    "Judges 14:8":   ("B", "Samson returned to take the woman and turned aside to see the lion's carcass"),
    "Judges 14:11":  ("B", "When they saw Samson they took thirty companions to be with him"),
    "Judges 19:17":  ("I", "The old man lifted his eyes and saw the wayfarer in the square (nasa-enayim idiom)"),
    "Ruth 2:18":     ("I", "Ruth took up (nasa) her gleanings and carried them home; her mother-in-law saw (non-take)"),
    "1 Samuel 6:13": ("I", "The reapers lifted their eyes and saw the returning ark (nasa-enayim idiom)"),
    "1 Samuel 14:17":("I", "'See who has gone from us'; Jonathan and his armor-bearer (nose keli, non-take)"),
    "1 Samuel 17:51":("B", "David... took Goliath's sword; the Philistines saw their champion was dead (battle)"),
    "1 Samuel 19:20":("B", "Saul's messengers saw the band of prophets; they were sent to take David"),
    "1 Samuel 24:12":("B", "David: 'See the skirt of your robe in my hand... I took it and did not kill you'"),
    "1 Samuel 25:35":("B", "David took from Abigail's hand what she brought: 'see, I have heeded your voice'"),
    "1 Samuel 26:12":("B", "David took Saul's spear and jug while all slept; no one saw (sparing Saul)"),
    "1 Samuel 31:5": ("I", "Saul's armor-bearer (nose keli) saw that Saul was dead and fell on his sword (non-take)"),
    "2 Samuel 13:34":("I", "The watchman lifted his eyes and saw a crowd coming (nasa-enayim idiom)"),
    "2 Samuel 18:24":("I", "The watchman lifted his eyes and saw a man running (nasa-enayim idiom)"),
    "2 Samuel 24:22":("B", "Araunah: 'let my lord take what is good; see, here are the oxen' (threshing floor)"),
    "1 Kings 16:18": ("B", "Zimri saw the city was taken (nilkedah) and burned the palace over himself"),
    "1 Kings 17:23": ("C", "Elijah took the revived child down: 'See, your son lives' (rescue)"),
    "2 Kings 2:10":  ("B", "Elijah: 'if you see me taken (luqach) from you, it shall be so' (ascension)"),
    "2 Kings 3:14":  ("I", "Elisha: were it not that I regard (nasa-panim) Jehoshaphat, I would not look at you (non-take)"),
    "2 Kings 3:26":  ("B", "The king of Moab saw the battle was too hard and took 700 swordsmen (siege)"),
    "2 Kings 6:13":  ("B", "'Go and see where he is, that I may send and take him' (hunt for Elisha)"),
    "2 Kings 7:13":  ("B", "'Let men take five horses and see' — reconnaissance in besieged Samaria"),
    "2 Kings 7:14":  ("B", "They took two chariots and horses and went to see (after the Arameans fled)"),
    "2 Kings 9:17":  ("B", "The watchman saw Jehu's company: 'take a horseman and send to meet them'"),
    "2 Kings 9:26":  ("B", "'I saw the blood of Naboth... take him up and cast him on the plot' (Jehu's vengeance)"),
    "2 Kings 9:32":  ("I", "Jehu lifted his face; the eunuchs looked out (shaqaph) at the window (nasa-panim, non-take)"),
    "2 Kings 11:4":  ("B", "Jehoiada took the captains and showed them the king's son (coup for Joash)"),
    "2 Kings 23:16": ("B", "Josiah turned, saw the tombs, and took the bones to defile the altar (reform)"),
    "2 Kings 25:19": ("B", "Nebuzaradan took an officer and men who saw the king's face (deportation)"),
    "1 Chronicles 10:5":("I", "Saul's armor-bearer (nose keli) saw he was dead and died with him (non-take)"),
    "1 Chronicles 21:16":("I", "David lifted his eyes and saw the angel of the LORD (nasa-enayim idiom)"),
    "1 Chronicles 21:23":("B", "Ornan: 'take it... see, I give the oxen for burnt offerings' (David's altar)"),
    "2 Chronicles 24:11":("I", "When they saw the chest held much money they carried (nasa) it out (non-take)"),
    "Esther 2:9":    ("B", "Hegai saw Esther pleased him and advanced her in the harem"),
    "Esther 2:15":   ("B", "Esther required only what Hegai appointed; she won favor with all who saw her"),
    "Esther 5:2":    ("I", "The king saw Esther and she won favor (nasa-chen) in his sight (non-take)"),
    "Psalms 4:7":    ("I", "'Who will show us good? Lift (nasa) the light of your face upon us' (non-take)"),
    "Psalms 25:18":  ("I", "'See my affliction... and forgive (nasa) all my sins' (non-take)"),
    "Proverbs 24:32":("B", "'I saw and took it to heart; I looked and received instruction' (wisdom reflection)"),
    "Ecclesiastes 2:3":("B", "Qoheleth sought to see good while laying hold (achaz) of folly (experiment)"),
    "Isaiah 6:1":    ("I", "'I saw the Lord... high and lifted up (nissa)' (non-take)"),
    "Isaiah 18:3":   ("I", "'When a signal is lifted (nasa) on the mountains, you shall see it' (non-take)"),
    "Isaiah 21:3":   ("B", "Pangs seized (achaz) the prophet at what he was made to see (metaphorical seizure)"),
    "Isaiah 40:26":  ("I", "'Lift your eyes on high and see who created these' (nasa-enayim idiom)"),
    "Isaiah 47:3":   ("B", "'Your nakedness shall be seen... I will take vengeance' (laqach-naqam, judgment on Babylon)"),
    "Isaiah 49:18":  ("I", "'Lift your eyes and see; they all gather' (nasa-enayim idiom)"),
    "Isaiah 51:6":   ("I", "'Lift your eyes to the heavens and look' (nasa-enayim idiom)"),
    "Isaiah 52:8":   ("I", "The watchmen lift their voice (nasa-qol) and see eye to eye (non-take)"),
    "Isaiah 60:4":   ("I", "'Lift your eyes and see; they all gather to you' (nasa-enayim idiom)"),
    "Jeremiah 3:2":  ("I", "'Lift your eyes to the bare heights and see' (nasa-enayim idiom)"),
    "Jeremiah 5:26": ("A", "The wicked watch (shur) like fowlers and catch (lakad) men — predatory seizure"),
    "Jeremiah 6:1":  ("I", "'Raise (nasa) a signal... for disaster looms (nishqefah)' (non-take)"),
    "Jeremiah 13:20":("I", "'Lift your eyes and see those coming from the north' (nasa-enayim idiom)"),
    "Jeremiah 32:24":("B", "The city is given over and taken (lakad) by the besiegers, as you see (siege)"),
    "Jeremiah 34:3": ("B", "Zedekiah: you shall be caught (taphas) and taken; your eyes shall see the king's eyes"),
    "Jeremiah 52:25":("B", "Nebuzaradan took an officer and men who saw the king's face (deportation)"),
    "Lamentations 4:16":("I", "The LORD no longer regards them (nasa-panim); priests were shown no favor (non-take)"),
    "Ezekiel 1:4":   ("B", "'I looked, and behold... fire enfolding (mitlaqqachat) itself' (inaugural vision)"),
    "Ezekiel 11:1":  ("I", "'The Spirit lifted (nasa) me and I saw' (non-take, prophetic rapture)"),
    "Ezekiel 11:24": ("I", "'The Spirit lifted me... in the vision I had seen' (non-take, prophetic rapture)"),
    "Ezekiel 12:6":  ("I", "'Lift (nasa) your baggage on your shoulder... you shall not see the ground' (non-take)"),
    "Ezekiel 12:12": ("I", "'The prince shall lift (nasa) his baggage on his shoulder... he shall not see' (non-take)"),
    "Ezekiel 12:13": ("B", "'He shall be caught (taphas) in my snare... yet he shall not see the land' (judgment)"),
    "Ezekiel 19:5":  ("B", "'When the lioness saw... she took another of her cubs and made him a lion' (allegory)"),
    "Ezekiel 20:28": ("B", "They saw every high hill and there presented their offerings (idolatry indictment)"),
    "Ezekiel 21:29": ("B", "'While they see false visions for you... you shall be seized (taphas)' (judgment)"),
    "Ezekiel 33:2":  ("D", "The people take a man and set him as watchman (tsofeh) when they see the sword (law)"),
    "Ezekiel 33:6":  ("D", "If the watchman sees the sword but does not warn, the sword takes (laqach) a life (responsibility)"),
    "Daniel 8:3":    ("I", "'I lifted my eyes and saw a ram' (nasa-enayim, apocalyptic vision)"),
    "Daniel 10:5":   ("I", "'I lifted my eyes and looked, and behold a man' (nasa-enayim, vision)"),
    "Micah 7:9":     ("I", "'I will bear (nasa) the LORD's indignation... until I behold his vindication' (non-take)"),
    "Habakkuk 1:3":  ("I", "'Why do you make me see wrong... strife lifts up (nasa)?' (non-take)"),
    "Habakkuk 3:10": ("I", "'The mountains saw you... the deep lifted (nasa) its voice' (non-take theophany)"),
    "Zechariah 2:1": ("I", "'I lifted my eyes and saw, and behold four horns' (nasa-enayim, vision)"),
    "Zechariah 2:5": ("I", "'I lifted my eyes and saw a man with a measuring line' (nasa-enayim, vision)"),
    "Zechariah 5:1": ("I", "'I lifted my eyes and saw a flying scroll' (nasa-enayim, vision)"),
    "Zechariah 5:5": ("I", "'Lift your eyes and see what this is that goes forth' (nasa-enayim, vision)"),
    "Zechariah 5:9": ("I", "'I lifted my eyes and saw two women with wind in their wings' (nasa-enayim, vision)"),
    "Zechariah 6:1": ("I", "'I lifted my eyes and saw four chariots' (nasa-enayim, vision)"),
}

CAT_NAME = {
    "A": "Transgressive", "B": "Narrative", "C": "Righteous inversion",
    "D": "Juridical/cultic", "I": "Idiom / non-take",
}


def main():
    rows = json.load(open(os.path.join(DATA, "cooccurrences.json"), encoding="utf-8"))
    t1 = [r for r in rows if r["tier"] == 1]
    missing = [r["seeing_ref"] for r in t1 if r["seeing_ref"] not in CLASS]
    if missing:
        raise SystemExit(f"UNCLASSIFIED Tier-1 refs: {missing}")

    BOOKS = ["Genesis","Exodus","Leviticus","Numbers","Deuteronomy","Joshua",
        "Judges","Ruth","1 Samuel","2 Samuel","1 Kings","2 Kings","1 Chronicles",
        "2 Chronicles","Ezra","Nehemiah","Esther","Job","Psalms","Proverbs",
        "Ecclesiastes","Song of Songs","Isaiah","Jeremiah","Lamentations",
        "Ezekiel","Daniel","Hosea","Joel","Amos","Obadiah","Jonah","Micah",
        "Nahum","Habakkuk","Zephaniah","Haggai","Zechariah","Malachi"]
    order = {b: i for i, b in enumerate(BOOKS)}

    def sort_key(r):
        c = int(r["seeing_osis"].split(".")[1]); v = int(r["seeing_osis"].split(".")[2])
        return (order[r["book"]], c, v)
    t1.sort(key=sort_key)

    # counts
    counts = {k: 0 for k in CAT_NAME}
    for r in t1:
        counts[CLASS[r["seeing_ref"]][0]] += 1

    lines = ["| # | Reference | Category | Seeing verb | Taking verb | Sense |",
             "|---|---|---|---|---|---|"]
    for i, r in enumerate(t1, 1):
        cat, gloss = CLASS[r["seeing_ref"]]
        see = r["seeing_terms"].replace(" [", " ").replace("]", "")
        take = r["taking_terms"].replace(" [", " ").replace("]", "")
        lines.append(f"| {i} | {r['seeing_ref']} | {cat} — {CAT_NAME[cat]} | {see} | {take} | {gloss} |")
    with open(os.path.join(DATA, "_tier1_classified.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    print("Tier-1 classification counts:")
    for k in ["A", "B", "C", "D", "I"]:
        print(f"  {k} {CAT_NAME[k]:20s}: {counts[k]}")
    print(f"  TOTAL: {sum(counts.values())}")

    # also write a compact category summary json
    with open(os.path.join(DATA, "tier1_categories.json"), "w", encoding="utf-8") as f:
        json.dump({"counts": counts, "category_names": CAT_NAME,
                   "classified": {r["seeing_ref"]: CLASS[r["seeing_ref"]][0] for r in t1}},
                  f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()

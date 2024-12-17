#!/usr/bin/python3
"""

python3 core8/pwb.py people/add_qids

SELECT ?item ?dem WHERE {
  ?item wdt:P31 wd:Q3624078;
    wdt:P1549 ?dem.
  filter (lang(?dem) = "en")
}


SELECT
(concat('"',str(?dem),'":"', strafter(str(?item),"/entity/"),'",') as ?333)

WHERE {
  ?item wdt:P31 wd:Q12737077;
    wdt:P3321 ?dem.
  filter (lang(?dem) = "en")
}

"""

from people.people_get_topic import job_to_qid, nat_to_qid

uux = {
    "actress": "Q21169216",
    "actor": "Q33999",
    "businessman": "Q43845",
    "costume designer": "Q1323191",
    "disc golf course designer": "Q120884973",
    "draughtsman": "Q15296811",
    "figure skating coach": "Q57199189",
    "fireman": "Q107711",
    "fisherman": "Q331432",
    "flaneur": "Q1427113",
    "frontiersman": "Q18289562",
    "handyman": "Q1552579",
    "houseboy": "Q10526633",
    "launderer": "Q16624872",
    "locker room attendant": "Q109906114",
    "lumberjack": "Q1124183",
    "man-midwife": "Q185196",
    "melographer": "Q121157760",
    "newspaperman": "Q96050759",
    "Occidentalist": "Q110635489",
    "penman": "Q108762424",
    "poisoner": "Q42763889",
    "pornographic actor": "Q488111",
    "professional actor": "Q131308697",
    "radiosportsman": "Q56164819",
    "skyrunner": "Q83169285",
    "social educator": "Q5819949",
    "sportsman": "Q2066131",
    "statesman": "Q372436",
    "streamer": "Q57414145",
    "Sugar daddy": "Q15975810",
    "tradesman": "Q2588761",
    "trombonist": "Q544972",
    "vice chairman": "Q1127270",
    "victualler": "Q1165514",
    "volunteer fireman": "Q11559510",
    "warlock": "Q47429760",
    "washermen": "Q16624872",
    "welder": "Q836328",
    "yogi": "Q2901587",
}


for x, q in job_to_qid.items():
    x2 = x.replace("~", "").strip().lower()
    qid = uux.get(x, q)
    print(f"    '{x}': '{qid}',")

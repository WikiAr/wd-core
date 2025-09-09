#!/usr/bin/python3
"""
#!/usr/bin/env python3

python3 core8/pwb.py des/desc limit:1000 optional
python3 core8/pwb.py des/desc limit:1000 optional place:Q173387 save #قبر
python3 core8/pwb.py des/desc limit:1000 optional place:Q918230 save #فيلا رومانية
python3 core8/pwb.py des/desc limit:1000 optional place:Q641226 #صالة
python3 core8/pwb.py des/desc limit:1000 optional place:Q483110 #ملعب
python3 core8/pwb.py des/desc limit:1000 optional place:Q1329623 #مركز ثقافي
python3 core8/pwb.py des/desc limit:1000 optional place:Q1154710 #استاد كرة قدم
python3 core8/pwb.py des/desc limit:1000 optional place:Q12518 #برج
python3 core8/pwb.py des/desc limit:1000 optional place:Q2225692 #منطقة سكنية في أندونوسيا
python3 core8/pwb.py des/desc limit:1000 optional place:Q185113

أوصاف مناطق جغرافية

python3 core8/pwb.py des/desc  limit:2000 offplace:85
python3 core8/pwb.py des/desc limit:2000 offplace:100 qslimit:5000
python3 core8/pwb.py des/desc limit:2000 qslimit:2000 alllimit:10000

python3 core8/pwb.py des/desc limit:2000 qslimit:5000 alllimit:10000

SELECT DISTINCT
(GROUP_CONCAT(DISTINCT(STRAFTER(STR(?item), "/entity/")); separator="@@") as ?q) #(CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
(GROUP_CONCAT(DISTINCT(STR(?placeare)); separator="@@") as ?placear) #?placear
(GROUP_CONCAT(DISTINCT(STRAFTER(STR(?p17), "/entity/")); separator="@@") as ?pp17) #(CONCAT(STRAFTER(STR(?p17), "/entity/")) AS ?pp17)
(GROUP_CONCAT(DISTINCT(STR(?p17labe)); separator="@@") as ?p17lab) #?p17lab
WHERE {
  ?item wdt:P31 wd:Q160091.
  {?item (wdt:P131|wdt:P276) ?place. ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar")
   ?place wdt:P17 ?p17.
  }  union {?item wdt:P17 ?p17.}
  #{?place wdt:P17 ?p17. } union {?item wdt:P17 ?p17.}
  ?p17 rdfs:label ?p17labe.FILTER((LANG(?p17labe)) = "ar")
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})FILTER (?statementcount > 50 ) .
  #FILTER (count(?p17) = 1 ) .
  #FILTER (count(?place) = 1 ) .
}
GROUP BY ?item
limit 100
"""

#
# (C) Ibrahem Qasim, 2022
#
#

import re
import sys

# ---
from wd_api import wd_sparql_bot
from newapi import printe
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="bot", www="www")
# ---
from wd_api import qs_bot
from wd_api import wd_bot

from des.contries2 import ContriesTable2
from des.places import placesTable
from wd_api import get_property_for_list

# placesTable = {"Q29701762": {"ar": "مستوطنة"}}
placesTable2 = {fg: placesTable[fg] for fg in placesTable}
# ---
q_list_done = []
New_QS = {1: []}
offset = {1: 0}
offset_place = {1: 0}
# ---
limit = {1: 0}
QSlimit = {1: 3000}
alllimit = {1: 50000}
# ---

Quase = {
    "Q8054": """SELECT DISTINCT
(CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
?placear
(CONCAT(STRAFTER(STR(?p17), "/entity/")) AS ?pp17)
?p17lab
WHERE {
  ?item wdt:P31 wd:%s.
  {?item wdt:P702 ?p17. }  union {?item wdt:P703 ?p17.}
  #{?place wdt:P17 ?p17. } union {?item wdt:P17 ?p17.}

  ?p17 rdfs:label ?p17lab.FILTER((LANG(?p17lab)) = "ar")

  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
""",
    2020: """SELECT #DISTINCT
(GROUP_CONCAT(DISTINCT(STRAFTER(STR(?item), "/entity/")); separator="@@") as ?q) #(CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
(GROUP_CONCAT(DISTINCT(STR(?placeare)); separator="@@") as ?placear) #?placear
(GROUP_CONCAT(DISTINCT(STRAFTER(STR(?p17), "/entity/")); separator="@@") as ?pp17) #(CONCAT(STRAFTER(STR(?p17), "/entity/")) AS ?pp17)
(GROUP_CONCAT(DISTINCT(STR(?p17labe)); separator="@@") as ?p17lab) #?p17lab
(COUNT(?p17) AS ?p17count)
(COUNT(?place) AS ?placecount)
WHERE {
  ?item wdt:P31 wd:%s.
  ?item (wdt:P131|wdt:P276) ?place. ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar")
  #?place wdt:P17 ?p17.
  {?place wdt:P17 ?p17. } union {?item wdt:P17 ?p17.}
  ?p17 rdfs:label ?p17labe.FILTER((LANG(?p17labe)) = "ar")
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item# HAVING ( ?p17count = 1 )
""",
}
# ---
if "optional" in sys.argv:
    # Quase[2020] = Quase[2020].replace('?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar")', 'optional { ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar") }' )
    # Quase[2020] = Quase[2020].replace('?item (wdt:P131|wdt:P276) ?place. ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar")', 'optional { ?item (wdt:P131|wdt:P276) ?place. ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar") }' )
    Quase[2020] = Quase[2020].replace(
        '?item (wdt:P131|wdt:P276) ?place. ?place rdfs:label ?placeare.FILTER((LANG(?placeare)) = "ar")',
        """
optional { ?item (wdt:P131|wdt:P276) ?place. }
SERVICE wikibase:label {
    bd:serviceParam wikibase:language "ar" .
    ?place rdfs:label ?placeare
  }""",
    )


for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg == "off":
        offset[1] = int(value)
    elif arg == "offplace":
        offset_place[1] = int(value)
    # ---
    # python3 core8/pwb.py des/desc descqs limit:4000 optional place:Q185113
    # python3 core8/pwb.py des/desc descqs limit:1000 place:Q8054
    if arg == "place" and value in placesTable:
        placesTable2 = {value: placesTable[value]}
    # ---
    if arg == "alllimit":
        alllimit[1] = int(value)
    elif arg == "limit":
        limit[1] = int(value)
    elif arg == "qslimit":
        QSlimit[1] = int(value)
    # ---


def descqs(q, value, lang):
    if len(New_QS[1]) < QSlimit[1]:
        qsline = f'{q}|D{lang}|"{value}"'
        New_QS[1].append(qsline)
        printe.output("<<lightyellow>>a %d\t%d:add %s to qlline " % (len(New_QS[1]), QSlimit[1], qsline))
    else:
        printe.output(f"<<lightgreen>> Add {len(New_QS[1])} line to quickstatements")
        qs_bot.QS_line("||".join(New_QS[1]), user="Mr.Ibrahembot")
        New_QS[1] = []


def Add_desc(q, value, lang):
    # ---
    if q in q_list_done:
        printe.output("q in q_list_done")
        return ""
    # ---
    q_list_done.append(q)
    # ---
    if "descqs" in sys.argv:
        descqs(q, value, lang)
    else:
        WD_API_Bot.Des_API(q, value, lang, ask="")


def work_one_item(start, lang, tab, c, total, findlab=False):
    # ---
    """work_one_item used in np/si3.py"""
    # ---
    if not start.strip():
        return ""
    # ---
    arlabel = start + " في {}"
    # ---
    q = tab["q"]
    p17lab = tab.get("p17lab", "").split("@@")[0]
    p17 = tab.get("pp17", "")
    placear = tab.get("placear", "").split("@@")[0]
    # ---
    if not p17lab:
        p17lab = ContriesTable2.get(p17, {}).get(lang, "")
    # ---
    if findlab:
        if p17lab == "" or placear == "":
            df = get_property_for_list.get_property_label_for_qids(["P17", "P131", "P276"], [q]) or {}
            printe.output("get_property_for_list")
            printe.output(df)
            # ---
        # ---
        if not p17lab:
            p17lab = df.get(q, {}).get("P17", "").split("@@")[0]
        # ---
        if not placear:
            placear = df.get(q, {}).get("P131", "").split("@@")[0]
        if not placear:
            placear = df.get(q, {}).get("P276", "").split("@@")[0]
    # ---
    placeartest = re.sub(r"[abcdefghijklmnopqrstuvwxyz@]", "", placear.lower())
    # ---
    if placeartest.lower() != placear.lower():
        printe.output(f"placeartest:[{placeartest}] != placear[{placear}]")
        placear = ""
    # ---
    placecount = int(tab.get("placecount", 1))
    if placecount != 1:
        printe.output(f"<<lightred>> placecount :{placecount},placear:{placear}")
        # placear = ''
    # ---
    p17count = int(tab.get("p17count", 1))
    if p17count != 1:
        printe.output(f"<<lightred>> p17count :{p17count},p17lab:{p17lab}")
    # ---
    arlabel2 = ""
    # ---
    if placear == p17lab or placear.find(p17lab) != -1:
        p17lab = ""
    # ---
    if placear and p17lab:
        asd = f"{placear}، {p17lab}"
        arlabel2 = arlabel.format(asd)
    elif placear not in ["", p17lab]:
        arlabel2 = arlabel.format(placear)
    elif p17lab:
        arlabel2 = arlabel.format(p17lab)
    # ---
    printe.output(f'  * action {c}/{total} "{q}:{arlabel2}"')
    # ---
    if not arlabel2:
        return ""
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz@]", "", arlabel2.lower())
    if test.lower() != arlabel2.lower():
        printe.output("test:[%s] != arlabel2[%s]")
        return ""
    # ---
    item = wd_bot.Get_Item_API_From_Qid(q, sites="", titles="", props="")
    # ---
    descriptions = item["descriptions"]
    # NewDesc = {}
    # addedlangs = []
    # ---
    if lang in descriptions:
        printe.output(f"lang:ar in descriptions({descriptions[lang]})")
        if descriptions[lang] != start:
            return ""
    # ---
    # NewDesc[lang] = { "language":lang,"value": arlabel2 }
    # addedlangs.append(lang)
    # ---
    # WD_API_Bot.Des_API( q, arlabel2 ,lang)
    # ---
    Add_desc(q, arlabel2, lang)


def work_one_place(place):
    lang = "ar"
    # ---
    start = placesTable2[place].get(lang, "")
    if not start.strip():
        printe.output('start.strip() == ""')
        return ""
    # ---
    if New_QS[1] != [] and "cleanlist" in sys.argv:
        qs_bot.QS_line("||".join(New_QS[1]), user="Mr.Ibrahembot")
        New_QS[1] = []
    quarry = Quase[place] if place in Quase else Quase[2020]
    # ---
    quarry = quarry % place
    # ---
    json1 = wd_sparql_bot.sparql_generator_big_results(quarry, offset=offset[1], limit=limit[1], alllimit=alllimit[1])
    total = len(json1)
    c = 1
    # ---
    for tab in json1:
        # ---
        c += 1
        q = tab["q"]
        # ---
        if q in q_list_done:
            printe.output("q in q_list_done")
            continue
        # ---
        work_one_item(start, lang, tab, c, total)


def mainoo():
    # ---
    kee = sorted(placesTable2.keys())
    # ---
    lenth_place = len(placesTable2)
    for placenum, place in enumerate(kee, start=1):
        # ---
        ara = placesTable2[place].get("ar", "")
        # ---
        printe.output(f'<<lightred>> {placenum}/{lenth_place}, place:"{place}", arlabel:"{ara}". ')
        # ---
        if placenum >= offset_place[1]:
            # ---
            work_one_place(place)
    # ---
    if New_QS[1] != []:
        qs_bot.QS_line("||".join(New_QS[1]), user="Mr.Ibrahembot")
        New_QS[1] = []


if __name__ == "__main__":
    mainoo()

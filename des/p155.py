#!/usr/bin/python3
"""

إضافة تسميات عناصر ويكي بيانات

بناءاً على خاصية سبقه أو تبعه

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import re
import sys
import pywikibot
from wd_api import wd_bot

# ---
from himo_api import New_Himo_API
import logging
logger = logging.getLogger(__name__)

WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="mr", www="www")
# ---
from des.p155tables import cccccups, Mako_keys_4, Mako_keys2, Mako_keys, International_Federation, olympics
from des.p155tables import keys_1, Sports_Keys_Lab

# ---
Usema = {1: True}
Ask = {1: True}
Limit = {1: "100"}
yes_answer = ["y", "a", "", "Y", "A", "all"]
# ---

# ---
log_done = []
# ---
years = r"(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)"
tests_en = r"[abcdefghijklmnopqrstuvwxyz]"
tests_ar = r"[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإىءئؤة1234567890\–\-\.]"

def make_newlabel(label, ar, en):
    # ---
    logger.info(f'<<lightblue>>make_newlabel label:"{label}",ar:"{ar}",en:"{en}" ')
    newlabel = ""
    # ---
    label = f"{label.lower()} "
    label = label.replace("' ", " ")
    label = label.replace(" double ", " doubles ")
    label = label.replace(" single ", " singles ")
    label = label.replace(" kilometre ", " kilometres ")
    label = label.replace(" metre ", " metres ")
    label = label.replace(" championship ", " championships ")
    # ---
    en = f"{en.lower()} "
    en = en.replace("' ", " ")
    en = en.replace(" double ", " doubles ")
    en = en.replace(" single ", " singles ")
    en = en.replace(" kilometre ", " kilometres ")
    en = en.replace(" metre ", " metres ")
    en = en.replace(" championship ", " championships ")
    # ---
    en2 = en
    if en.find("(") != -1:
        en2 = en.lower().split("(")[0]
    # ---
    # if re.sub( tests_en , "" , newlabel , flags = re.IGNORECASE ).strip() != newlabel :
    # if re.sub( tests_ar , "" , newlabel , flags = re.IGNORECASE ).strip() != "" :
    if en.lower().strip() == "" or ar.lower().strip() == "":
        newlabel = label
    elif label.lower().strip() == en.lower().strip():
        newlabel = ar
    elif label.find(en.lower()) != -1:
        newlabel = f"{ar} " + label.replace(en.lower(), "")
    elif en2 != en and label.find(en2) != -1:
        newlabel = f"{ar} " + label.replace(en2.lower(), "")
    else:
        newlabel = label
    # ---
    logger.info(f'<<lightblue>>olympics newlabel:"{newlabel}" ')
    # ---
    for oll in olympics:
        newlabel = re.sub(oll, olympics[oll], newlabel, flags=re.IGNORECASE)
    # ---
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) time trial", r" سباق \g<1> ضد الساعة للرجال ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) road race", r" سباق الطريق \g<1> للرجال ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase", r" رجال \g<1> متر حواجز خيول ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase", r" رجال \g<1> متر حواجز خيول ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) hurdles", r" رجال \g<1> متر حواجز ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m) walk", r" رجال \g<1> متر مشي ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+)\s*(?:metres|m)", r" رجال \g<1> متر ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+) metre", r" رجال \g<1> متر ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+) kg", r" رجال \g<1> كجم ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" men\'s (\d+|\d+\.\d+) kilometres", r" رجال \g<1> كيلوجرام ", newlabel, flags=re.IGNORECASE)
    # ---
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m) time trial", r" سباق \g<1> ضد الساعة للسيدات ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m) road race", r" سباق الطريق \g<1> للسيدات ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase", r" سيدات \g<1> متر حواجز خيول ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m) hurdles", r" سيدات \g<1> متر حواجز ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m) walk", r" سيدات \g<1> متر مشي ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+)\s*(?:metres|m)", r" سيدات \g<1> متر ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+) metre", r" سيدات \g<1> متر ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+) kg", r" سيدات \g<1> كجم ", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r" women\'s (\d+|\d+\.\d+) kilometres", r" سيدات \g<1> كيلوجرام ", newlabel, flags=re.IGNORECASE)
    # ---
    newlabel = re.sub(r" (\d|\d+|\d+\.\d+) to (\d|\d+|\d+\.\d+) ton", r" \g<1> إلى \g<2> طن", newlabel, flags=re.IGNORECASE)
    # ---
    # newlabel2 = newlabel
    # ---
    for aeo in cccccups:
        newlabel = re.sub(aeo, cccccups[aeo], newlabel, flags=re.IGNORECASE)
    # ---
    for x in Mako_keys:
        newlabel = re.sub(x, Mako_keys[x], newlabel, flags=re.IGNORECASE)
    # ---
    for xx in Mako_keys2:
        newlabel = re.sub(xx, Mako_keys2[xx], newlabel, flags=re.IGNORECASE)
    # ---
    newlabel = re.sub(r"at the summer olympics", "في الألعاب الأولمبية الصيفية", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r"at the summer youth olympics", "في الألعاب الأولمبية الشبابية الصيفية", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r"at the winter youth olympics", "في الألعاب الأولمبية الشبابية الشتوية", newlabel, flags=re.IGNORECASE)
    newlabel = re.sub(r"at the winter olympics", "في الألعاب الأولمبية الشتوية", newlabel, flags=re.IGNORECASE)
    # ---
    for aeo in Mako_keys_4:
        newlabel = re.sub(f" {aeo}", f" {Mako_keys_4[aeo]}", newlabel, flags=re.IGNORECASE)
    # ---
    for rrr in International_Federation:
        newlabel = re.sub(
            f" {rrr}",
            f" {International_Federation[rrr]}",
            newlabel,
            flags=re.IGNORECASE,
        )
    # ---
    for ccc in Sports_Keys_Lab:
        newlabel = re.sub(
            f" {ccc}",
            f" {Sports_Keys_Lab[ccc]}",
            newlabel,
            flags=re.IGNORECASE,
        )
    # ---
    for hgh in keys_1:
        newlabel = re.sub(f" {hgh}", f" {keys_1[hgh]}", newlabel, flags=re.IGNORECASE)
    # ---
    newlabel = newlabel.replace("  ", " ")
    # ---
    # if newlabel2 != newlabel:
    # logger.info( '<<lightblue>> newlabel2:%s, newlabel:"%s" ' % ( newlabel2 , newlabel ) )
    # ---
    logger.info(f'<<lightblue>> label:{label}, newlabel:"{newlabel}" ')
    # ---
    if not newlabel.strip():
        logger.info('<<lightblue>> newlabel = "" ')
        return ""
    # ---
    newlabel = newlabel.strip()
    mat = re.match(f"^{years}" + r"\sفي\s.*", newlabel)
    if not mat:
        newlabel = re.sub(
            f"^{years}" + r"\s*(.*)\-(.*)",
            r"\g<2> \g<1> - \g<3>",
            newlabel,
            flags=re.IGNORECASE,
        ).strip()
        newlabel = re.sub(
            f"^{years}" + r"\s*(.*)\–(.*)",
            r"\g<2> \g<1> - \g<3>",
            newlabel,
            flags=re.IGNORECASE,
        ).strip()
        newlabel = re.sub(
            f"^{years}" + r"\s*(.*)",
            r"\g<2> \g<1>",
            newlabel,
            flags=re.IGNORECASE,
        ).strip()
    # ---
    leb_test = re.sub(tests_ar, "", newlabel, flags=re.IGNORECASE)
    if leb_test.strip():
        logger.info(f"<<lightblue>> leb_test({leb_test.strip()}) ==  ")
        newlabel = ""
    # ---
    newlabel = newlabel.replace("ألعاب أولمبية شتوية", "الألعاب الأولمبية الشتوية")
    newlabel = newlabel.replace("ألعاب أولمبية صيفية", "الألعاب الأولمبية الصيفية")
    newlabel = newlabel.replace("  ", " ")
    # ---
    return newlabel.strip()

def Item(item):
    # ---
    q = item["item"]
    # ---#
    # item[''] = re.sub(r"shooting at the 2016 summer olympics"  , "" , item['dden'], flags = re.IGNORECASE  )
    item["dden"] = re.sub(r"(.*) at the (\d+) (Winter|summer) olympics", r"\g<2> \g<1> at the \g<3> olympics", item["dden"], flags=re.IGNORECASE)
    item["label"] = re.sub(r"(.*) at the (\d+) (Winter|summer) olympics", r"\g<2> \g<1> at the \g<3> olympics", item["label"], flags=re.IGNORECASE)
    item["dden"] = re.sub(r"(.*) at the (\d+) (Winter|summer) youth olympics", r"\g<2> \g<1> at the \g<3> youth olympics", item["dden"], flags=re.IGNORECASE)
    item["label"] = re.sub(r"(.*) at the (\d+) (Winter|summer) youth olympics", r"\g<2> \g<1> at the \g<3> youth olympics", item["label"], flags=re.IGNORECASE)
    # ---
    lline = ",".join([f"{x}:{item[x]}" for x in item])
    logger.info(lline)
    # ---
    en = re.sub(r"^(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d) ", "", item["dden"], flags=re.IGNORECASE)
    if en == item["dden"]:
        en = re.sub(r" (\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)$", "", item["dden"], flags=re.IGNORECASE)
    en = en.strip()
    # ---
    ar = re.sub(r"^(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d) ", "", item["ddar"], flags=re.IGNORECASE)
    if ar == item["ddar"]:
        ar = re.sub(r" (\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)$", "", ar, flags=re.IGNORECASE)
    ar = ar.strip()
    if Usema[1]:
        if (ar == item["ddar"].strip() and ar.lower().strip() != "") or (en == item["dden"].strip() and en.lower().strip() != ""):
            logger.info("<<lightred>> ar == item['ddar'] or en == item['dden'] ")
            logger.info(f"<<lightred>> en:{en},dden:{item['dden']} ")
            logger.info(f"<<lightred>> ar:{ar},ddar:{item['ddar']} ")
            # return ''
            ar = ""
            en = ""
    # ---
    label = item["label"].lower()
    # ---
    newlabel = make_newlabel(label, ar, en)
    year = mat.group(1) if (mat := re.match(f".*{years}.*", item["label"])) else ""
    # ---
    if newlabel.strip() and year.strip() and newlabel.find(year.strip()) == -1:
        logger.info(f"<<lightred>> cant find year:{year}, at newlabel ({newlabel}) ")
        return ""
    if Ask[1]:
        if newlabel.strip():
            sa = pywikibot.input(f'<<lightyellow>>bot: Labels_API Add "{newlabel}" as label to "{q}"? ([y]es, [N]o):')
            if sa in yes_answer:
                WD_API_Bot.Labels_API(q, newlabel, "ar", False, Or_Alii=True)
            if sa == "a":
                Ask[1] = False
    elif newlabel.strip():
        WD_API_Bot.Labels_API(q, newlabel, "ar", False, Or_Alii=True)

    # ---

Quarry = {
    "use":
        "",
    0:
        """
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
  ?item wdt:P31/wdt:P279* wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item wdt:P3450 ?dd.
  #?dd wdt:P31/wdt:P279* wd:Q8463186.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
}
LIMIT """,
    1:
        """
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 # ?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item (wdt:P3450|wdt:P361) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
}
LIMIT """,
    2:
        """
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
 #  ?dd wdt:P527 ?item.
  #?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  {
  ?item wdt:P155 ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    } union {
  ?item wdt:P156 ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    }
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr

}
LIMIT  """,
    3:
        """
SELECT DISTINCT ?item ?label
?dden ?ddar
WHERE {
   # ?item2 wdt:P31 wd:Q27020041.
    ?item2 rdfs:label ?ddar filter (lang(?ddar) = "ar") .
    ?item2 rdfs:label ?dden filter (lang(?dden) = "en") .
    { ?item2 wdt:P155 ?item. } union {?item2 wdt:P156 ?item. }
    ?item rdfs:label ?label filter (lang(?label) = "en") .
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr

}
LIMIT  """,
    4:
        """
SELECT DISTINCT ?item ?label
?dden ?ddar
WHERE {
    #?item2 wdt:P31 wd:Q27020041.
    ?item2 rdfs:label ?ddar filter (lang(?ddar) = "ar") .
    ?item2 rdfs:label ?dden filter (lang(?dden) = "en") .
    { ?item2 wdt:P155 ?item. } union {?item2 wdt:P156 ?item. }
    ?item rdfs:label ?label filter (lang(?label) = "en") .
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
    #sr
}
LIMIT  """,
    5:
        """
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
 #  ?dd wdt:P527 ?item.
  #?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  optional {
  ?item (wdt:P155|wdt:P156) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    }
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr

}
LIMIT  """,
    6:
        """
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
  ?item wdt:P641 ?p641.
  #?item wdt:P31 wd:Q27020041.
  ?item (wdt:P31|wdt:P361) ?tt.
  #?tt wdt:P31/wdt:P279* wd:Q1344963.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item (wdt:P156|wdt:P155) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
#sr

}
LIMIT
""",
    7:
        """
SELECT DISTINCT ?item ?label ?dden ?ddar
WHERE {
    ?item rdfs:label ?label filter (lang(?label) = "en") .
	?item wdt:P31 ?dd.?dd wdt:P279 wd:Q13219666.
  #?item (wdt:P361|wdt:P3450|wdt:P31) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    #sr
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
}
LIMIT  """,
    8:
        """
SELECT ?item ?ddar ?dden ?label
WHERE {
  ?io wdt:P31 wd:Q27020041.
  ?io p:P3450 ?statement .
  ?statement pq:P155 ?item.
  ?statement pq:P156 ?after.
  ?io rdfs:label ?dden filter (lang(?dden) = "en")
  ?io rdfs:label ?ddar filter (lang(?ddar) = "ar")
  FILTER NOT EXISTS {?item rdfs:label ?ara filter (lang(?ara) = "ar")} .
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  #sr

}
LIMIT
""",
}
# ---
Quarry["use"] = Quarry[2]

def main():
    # ---
    # python pwb.py des/p155 qua0 P17:Q145
    # python pwb.py des/p155 qua0
    # python pwb.py des/p155 qua1
    # python pwb.py des/p155 qua1 sky
    #
    # python pwb.py des/p155 qua8 -limit:400
    # python pwb.py des/p155 qua2 -limit:400
    # python pwb.py des/p155 qua3 -limit:400
    # python pwb.py des/p155 qua4 -limit:400
    # python pwb.py des/p155 -limit:400
    # ---
    logger.info(sys.argv)
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "qua0":
            Quarry["use"] = Quarry[0]
            Usema[1] = False
        # ---
        if arg == "qua7":
            Quarry["use"] = Quarry[7]
            Usema[1] = False
        # ---
        if arg == "qua1":
            Quarry["use"] = Quarry[1]
            Usema[1] = False
        # ---
        if arg == "qua2":
            Quarry["use"] = Quarry[2]
        # ---
        if arg == "qua3":
            Quarry["use"] = Quarry[3]
        # ---
        if arg == "qua4":
            Quarry["use"] = Quarry[4]
        # ---
        if arg == "qua5":
            Quarry["use"] = Quarry[5]
        # ---
        if arg == "qua6":
            Quarry["use"] = Quarry[6]
        # ---
        if arg == "qua8":
            Quarry["use"] = Quarry[8]
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "sky":
            # Quarry['use']  = Quarry['use'].replace("#sr" , "?item (wdt:P3450|wdt:P361) ?P361. ?P361 (wdt:P3450|wdt:P361) wd:Q285389. \n#sr\n" )
            Quarry["use"] = Quarry["use"].replace("#sr", "?item (wdt:P31|wdt:P361) ?P361. ?P361 (wdt:P31/wdt:P279*|wdt:P361) wd:Q18536594. \n#sr\n")
        # ---
        if arg == "save":
            Ask[1] = False
            logger.info("<<lightred>> Ask = False.")
        # ---
        if arg in ["-limit", "limit"]:
            Limit[1] = value
            logger.info(f"<<lightred>> Limit = {value}.")
        # ---#
        # python pwb.py des/p155 qua0 P279:Q1079023
        if arg == "-P279":
            tart = f"?item wdt:P31/wdt:P279* wd:{value}."
            logger.info(f'tart: "{tart}"')
            Quarry["use"] = Quarry["use"].replace("#sr", tart + "\n#sr")
        # ---#
        # python pwb.py des/p155 qua2 P31:Q18536594
        elif arg.startswith("P") and value.startswith("Q"):
            tart = f"?item wdt:{arg} wd:{value}."
            logger.info(f'tart: "{tart}"')
            Quarry["use"] = Quarry["use"].replace("#sr", tart + "\n#sr")
            # ---#
    Quaa = Quarry["use"] + Limit[1]
    logger.info(Quaa)
    sparql = wd_bot.sparql_generator_url(Quaa)
    # ---
    Table = {}
    for item in sparql:
        q = item["item"].split("/entity/")[1]
        item["item"] = q
        Table[q] = item
    for num, (item, tabj) in enumerate(Table.items(), start=1):
        logger.info('<<lightblue>> %d/%d item:"%s" ' % (num, len(Table.keys()), item))
        Item(tabj)

def test():
    # cc = "2010 World Figure Skating Championships - ladies' singles free skating"
    # ar = make_newlabel( cc , '' , '' )
    # ar = make_newlabel( "2020 Volleyball at the Summer olympics" , 'الألعاب الأولمبية الصيفية 2020' , '2020 Summer Olympics' )
    # ar = make_newlabel( "1988 Ski jumping at the Winter olympics – Large hill individual" , '' , '' )
    # ar = make_newlabel( "1998 cross-country skiing at the winter olympics – women's 10 kilometre freestyle pursuit" , '' , '' )
    # ar = make_newlabel( "1964 weightlifting at the summer olympics – men's 82.5 kg" , '' , '' )
    ar = make_newlabel("2014 world team table tennis championships", "", "")
    # logger.info( cc )
    logger.info(ar)

# ---
if __name__ == "__main__":
    if sys.argv and "test" in sys.argv:
        test()
    else:
        main()
    # Item({'ddar': 'بطولة العالم لتنس الطاولة 1932', 'dden': '1932 World Table Tennis Championships', 'item': 'Q203962', 'label': '1933 World Table Tennis Championships (January)'})
    # Item({'ddar': 'بطولة العالم للشطرنج 1975', 'dden': 'World Chess Championship 1975', 'item': 'Q1999918', 'label': 'World Chess Championship 1978'})
# ---

# python pwb.py des/p155 qua7 -P279:Q13219666 limit:200
# python pwb.py des/p155 qua4 -P279:Q1344963 limit:200
# python pwb.py des/p155 qua4 -P279:Q1079023 limit:200

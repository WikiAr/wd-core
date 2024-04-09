#!/usr/bin/python3
"""

اضافة تسميات بناءاً على الاسم الأول واسم العائلة

"""
#
# (C) Ibrahem Qasim, 2022
#
from wd_api import wd_bot
from api_sql import sql

import pywikibot

# import pywikibot.data.wikidataquery as wdquery
# used in logfiles, unicoded strings
# ---
import sys

# ---
File_name_to_check = {1: "name/LOG/name_to_check.log.csv"}
# ---
# ---

# ---
try:
    from wd_api import himoAPI_test as himoAPI
except ImportError:
    pywikibot.output('<<lightred>> Can\'t import himoAPI_test as himoAPI')
# ---
# from wd_api import himoAPI
# ---
ask = {1: True}
OFFSET = {1: '   '}
Limit = {1: ' limit 100 '}
# ---
names = [
    "Q307288",  # عبد الملك
    "Q307378",  # عبد الرحمن
    "Q307578",  # عبد الله
    "Q317333",  # عبد اللطيف
    "Q317304",  # عبد الكريم
    "Q317520",  # عبد القادر
    "Q479670",  # عبد المجيد
    "Q2820910",  # عبد اللطيف
    "Q4664595",  # عبد العزى
    "Q4664544",  # عبد ربه
    "Q4665310",  # عبد البصير
    "Q4664745",  # عبد الفتاح
    "Q4665099",  # عبد الرضا
    "Q4665376",  # عبد الحكيم
    "Q4666246",  # عبد الرؤوف
    "Q4665347",  # عبد الهادي
    "Q4665579",  # عبد الناصر
    "Q4665610",  # عبد القيوم
    "Q4666228",  # عبد الرب
    "Q4665382",  # عبد الحليم
    "Q4665325",  # عبد الغفور
    "Q4665739",  # عبد الودود
    "Q4665445",  # عبد الجميل
    "Q4665616",  # عبد القدوس
    "Q4665752",  # عبد الواحد
    "Q4665356",  # عبد الحفيظ
    "Q4665487",  # عبد الخالق
    "Q4665566",  # عبد المنعم
    "Q4665365",  # عبد الحي
    "Q2511172",  # عبد العظيم
    "Q4666328",  # عبد الشكور
    "Q4666312",  # عبد السلام
    "Q11723828",  # عبد الوهاب
    "Q13057047",  # عبد الصمد
    "Q16001377",  # عبد الرشيد
    "Q12222876",  # عبد الستار
    "Q3710734",  # عبد الرحمن
    "Q17280253",  # عبد المنان
    "Q13479668",  # عبد العليم
    "Q13422873",  # عبد الحميد
    "Q20995570",  # عبد الرحيم
    "Q22977313",  # عبد الرزاق
    "Q28051190",  # عبد المطلب
    "Q28053523",  # عبد الستار
    "Q28053508",  # عبد الحق
    "Q28053534",  # عبد الغفار
    "Q28053543",  # عبد المتين
    "Q28053386",  # عبد الرقيب
    "Q28053499",  # عبد الجليل
    "Q28053538",  # عبد الغني
    "Q28053535",  # عبد الغفور
    "Q28053511",  # عبد الحافظ
    "Q28053555",  # عبد الباقي
    "Q28053562",  # عبد الجبار
    "Q28053554",  # عبد الباسط
    "Q46371927",  # عبد العزيز
    "Q56597708",  # عبد النور
    "Q56870624",  # عبد القوي
]
# ---
fafafa = """عبد الملك
عبد الرحمن
عبد الله
عبد اللطيف
عبد الكريم
عبد القادر
عبد المجيد
عبد اللطيف
عبد العزى
عبد ربه
عبد البصير
عبد الفتاح
عبد الرضا
عبد الحكيم
عبد الرؤوف
عبد الهادي
عبد الناصر
عبد القيوم
عبد الرب
عبد الحليم
عبد الغفور
عبد الودود
عبد الجميل
عبد القدوس
عبد الواحد
عبد الحفيظ
عبد الخالق
عبد المنعم
عبد الحي
عبد العظيم
عبد الشكور
عبد السلام
عبد الوهاب
عبد الصمد
عبد الرشيد
عبد الستار
عبد الرحمن
عبد المنان
عبد العليم
عبد الحميد
عبد الرحيم
عبد الرزاق
عبد المطلب
عبد الستار
عبد الحق
عبد الغفار
عبد المتين
عبد الرقيب
عبد الجليل
عبد الغني
عبد الغفور
عبد الحافظ
عبد الباقي
عبد الجبار
عبد الباسط
عبد العزيز
عبد النور
عبد القوي"""
# ---
Quarry = {
    1: '''

SELECT ?item ?label
WHERE {
    ?item wdt:P31 wd:Q5.
    ?item rdfs:label ?label.
    FILTER((LANG(?label)) = "ar")
    #sr
    #FILTER (CONTAINS(?label, 'عبد الله')) .


    }
'''
}


def action_one_item(q, ar):
    pywikibot.output(f'<<lightblue>>> {q}:{ar} ')
    ar2 = ar
    if ar.find("عبد ") != -1:
        ar2 = ar.replace("عبد ", "عبد")
    if ar != ar2:
        himoAPI.Alias_API(q, [ar2], "ar", False)


def workqua(qua):
    qua = qua + OFFSET[1]
    # ---
    qua = qua + Limit[1]
    pywikibot.output(qua)
    # ---
    sparql = wd_bot.sparql_generator_url(qua)
    total = len(sparql)
    for pa in sparql:
        # pa = pigenerator[page]
        pa['item'] = pa['item'].split('/entity/')[1]
        action_one_item(pa['item'], pa['label'])


# ---
queries = '''use wikidatawiki_p;
SELECT term_full_entity_id , term_text
from wb_terms
WHERE term_entity_type = 'item'
AND term_language = 'ar'#en#ar#
AND term_type = 'label' #description#label#
AND term_text like "%عبد_%"
LIMIT 500
;'''


def mains():
    pywikibot.output('start with query')
    # ---
    FFF = True
    # ---
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(':')
        # ---
        if arg.startswith("names"):
            # ---
            # python3 core8/pwb.py wd/ali names
            # python3 core8/pwb.py wd/ali fafafa
            lala = ""
            lala = [x.strip() for x in names if x.strip() != ""]
            pywikibot.output(f'lala: "{lala}"')
            acd = "  wd:".join(lala)
            tart = f"?item (wdt:P734|wdt:P735) ?name. VALUES ?name { wd:{acd} } ."
            pywikibot.output(f'acd: "{tart}"')
            Quarry[1] = Quarry[1].replace("#sr", f"{tart}\n#sr")
        elif arg.startswith("c"):
            tart = "FILTER (CONTAINS(?label, 'عبد الله')) ."
            pywikibot.output(f'acd: "{tart}"')
            Quarry[1] = Quarry[1].replace("#sr", f"{tart}\n#sr")
        elif arg.startswith("fafafa"):
            for uu in fafafa.split("\n"):
                if uu:
                    tart = f"FILTER (CONTAINS(?label, '{uu}')) ."
                    pywikibot.output(f'acd: "{tart}"')
                    qsa = Quarry[1].replace("#sr", f"{tart}\n#sr")
                    workqua(qsa)
        elif arg.startswith("sql"):
            for uu in fafafa.split("\n"):
                if uu:
                    fff = queries.replace("عبد_", uu)
                    tart3 = sql.Make_sql_2_rows(fff, wiki="wikidata")
                    pywikibot.output(f'tart3: "{tart3}"')
                    for te in tart3:
                        action_one_item(te[1], te[2])
        # ---
        # python pwb.py wd/ali ss:340662
        elif arg == "ss":
            fff = queries
            tart3 = wd_bot.get_quarry_results(value, get_rows=2)
            FFF = False
            # pywikibot.output( 'tart3: "%s"' % tart3 )
            for te in tart3:
                action_one_item(te, tart3[te])
        # ---
        if arg == 'limit':
            Limit[1] = f" limit {value}"
    # ---
    '''fff = queries
    tart3 = wd_bot.get_quarry_results("340662", get_rows=2)
    FFF = False
    #pywikibot.output( 'tart3: "%s"' % tart3 )
    for te in tart3 :
        action_one_item( te , tart3[ te ] )
    # ---'''
    if FFF:
        workqua(Quarry[1])


# ---
if __name__ == "__main__":
    mains()
# ---

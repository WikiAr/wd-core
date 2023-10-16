#!/usr/bin/python
"""
python pwb.py cy/cy5 -page:باتريك_كونراد
python pwb.py cy/cy5 -page:جويل_سوتير
python pwb.py cy/cy5 -page:كريس_فروم

python pwb.py cy/cy5 workibrahem test2 -title:خوان_سباستيان_مولانو
python pwb.py cy/cy5 workibrahem test2 -title:إليسا_ونغو_بورغيني ask
python pwb.py cy/cy5 workibrahem test2 -title:كوين_سيمونز

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import sys
import urllib
import urllib.request
import urllib.parse
# ---
import requests
import datetime
# ---
AskToSave = True
from datetime import datetime
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
# ---
# from API.useraccount import *
from . import useraccount
api_url = 'https://' + 'ar.wikipedia.org/w/api.php'
username = useraccount.username
password = useraccount.password
# ---
workibrahem = False
if 'workibrahem' in sys.argv:
    from API import useraccount
    username = useraccount.hiacc
    password = useraccount.hipass
    workibrahem = True
    print('workibrahem active')
# ---
session = {}
session[1] = requests.Session()
session["csrftoken"] = ""
# ---


def login():
    # get login token
    r1 = session[1].get(api_url, params={
        'format': 'json',
        'action': 'query',
        'meta': 'tokens',
        'type': 'login',
    })
    r1.raise_for_status()

    # log in
    r2 = session[1].post(api_url, data={
        'format': 'json',
        'action': 'login',
        'lgname': username,
        'lgpassword': password,
        'lgtoken': r1.json()['query']['tokens']['logintoken'],
    })

    # print( str( r2.json() ) )

    if r2.json()['login']['result'] != 'Success':
        raise RuntimeError(r2.json()['login']['reason'])

    # get edit token
    r3 = session[1].get(api_url, params={
        'format': 'json',
        'action': 'query',
        'meta': 'tokens',
    })
    session["csrftoken"] = r3.json()['query']['tokens']['csrftoken']


# ---
login()
# ---
remove_date = {}
Work_with_Year = {}
Work_with_Stage = {1: False}
Stage = {}
Stage[""] = ""
# ---
TEST = {1: False, 2: False}
# import pywikibot
# ---
# from likeapi import encode
# encode.encode_arabic(label)
# ---
litters = {
    "ا": "%D8%A7",
    "ب": "%D8%A8",
    "ت": "%D8%AA",
    "ث": "%D8%AB",
    "ج": "%D8%AC",
    "ح": "%D8%AD",
    "خ": "%D8%AE",
    "د": "%D8%AF",
    "ذ": "%D8%B0",
    "ر": "%D8%B1",
    "ز": "%D8%B2",
    "س": "%D8%B3",
    "ش": "%D8%B4",
    "ص": "%D8%B5",
    "ض": "%D8%B6",
    "ط": "%D8%B7",
    "ظ": "%D8%B8",
    "ع": "%D8%B9",
    "غ": "%D8%BA",
    "ف": "%D9%81",
    "ق": "%D9%82",
    "ك": "%D9%83",
    "ل": "%D9%84",
    "م": "%D9%85",
    "ن": "%D9%86",
    "ه": "%D9%87",
    "و": "%D9%88",
    "ي": "%D9%8A",
    "أ": "%D8%A3",
    "آ": "%D8%A2",
    "إ": "%D8%A5",
    "ى": "%D9%89",
    "ء": "%D8%A1",
    "ئ": "%D8%A6",
    "ؤ": "%D8%A4",
    " ": "%20",
    "_": "%20",
}
# ---


def encode_arabic(label):
    label2 = label
    for x in litters:
        label2 = label2.replace(x, litters[x])
    return label2
# ---


def ec_de_code(tt, type):
    fao = tt
    if type == 'encode':
        fao = urllib.parse.quote(tt)
    elif type == 'decode':
        fao = urllib.parse.unquote(tt)
    return fao
# ---


def print_test2(s):
    if TEST[2]:
        # pywikibot.output(s)
        print(s)
# ---


def printt(s):
    SS = False
    if SS or 'test' in sys.argv or 'test2' in sys.argv:
        # pywikibot.output(s)
        print(s)
# ---


def printo(s):
    SS = True
    if SS:
        try:
            print(ec_de_code(s, 'encode'))
        except:
            print("")
            if workibrahem:
                print(s)


# ---
HeadVars = ['imagejersey']
JOJOJO = 'نتيجة سباق الدراجات/جيرسي'
# ---


def findflag(race, flag):
    flage = {
        'إيطاليا': '{{رمز علم|إيطاليا}}',
        'جيرو ديل ترينتينو': '{{رمز علم|إيطاليا}}',
        'the Alps': '{{رمز علم|إيطاليا}}',
        'France': '{{رمز علم|فرنسا}}',
        'فرنسا': '{{رمز علم|فرنسا}}',
        'إسبانيا': '{{رمز علم|إسبانيا}}',
        'دونكيرك': '{{رمز علم|بلجيكا}}',
        'غنت-وفلجم': '{{رمز علم|بلجيكا}}',
        'Gent–Wevelgem': '{{رمز علم|بلجيكا}}',
        'Norway': '{{رمز علم|النرويج}}',
        'النرويج': '{{رمز علم|النرويج}}',
        'كريثيديا دو دوفين': '{{رمز علم|سويسرا}}',
        'du Dauphiné': '{{رمز علم|سويسرا}}',
        'سويسرا': '{{رمز علم|سويسرا}}',
        'باريس-نايس': '{{رمز علم|فرنسا}}',
    }
    # ---
    race = str(race)
    # ---
    for ff in flage.keys():
        te = re.sub(str(ff), '', race)
        # ---
        if te != race:
            flag = flage[ff]
    # ---
    return flag


# ---
Skip_items = ["Q4115189"]
# ---


def fix_label(label):
    label = label.strip()

    label = re.sub(r"بطولة العالم لسباق الدراجات على الطريق (\d+) – سباق الطريق الفردي للرجال",
                   r"سباق الطريق في بطولة العالم \g<1>", label)

    label = re.sub(r"ركوب الدراجات في الألعاب الأولمبية الصيفية (\d+) – سيدات فردي سباق الطريق",
                   r"سباق الطريق للسيدات في ركوب الدراجات الأولمبية الصيفية \g<1>", label)

    label = re.sub(r"ركوب الدراجات في الألعاب الأولمبية الصيفية (\d+) – فريق رجال سباق الطريق", r"سباق الطريق لفرق الرجال في ركوب الدراجات الأولمبية الصيفية \g<1>", label)

    # بطولة العالم لسباق الدراجات على الطريق 1966 – سباق الطريق الفردي للرجال
    label = re.sub(r"بطولة العالم لسباق الدراجات على الطريق (\d+) – سباق الطريق الفردي للرجال",
                   r"سباق الطريق للرجال في بطولة العالم \g<1>", label)

    label = re.sub(r"سباق الطريق المداري ", "سباق الطريق ", label)
    label = re.sub(r"(بطولة [\s\w]+) الوطنية ", r"\g<1> ", label)
    label = re.sub(r"^(سباق\s*.*? في بطولة العالم)\s*(لسباق الدراجات على الطريق|للدراجات) (.*?)$", r"\g<1> \g<3>", label)
    label = re.sub(r"^(سباق\s*.*? في بطولة [\s\w]+)\s*(لسباق الدراجات على الطريق|للدراجات) (.*?)$", r"\g<1> \g<3>", label)

    # سباق الطريق للسيدات في ركوب الدراجات في الألعاب الأولمبية الصيفية 2016
    label = re.sub(r"في ركوب الدراجات في الألعاب الأولمبية ", "في ركوب الدراجات الأولمبية ", label)

    # في ركوب الدراجات في دورة ألعاب الكومنولث
    label = re.sub(r"ركوب الدراجات في دورة ألعاب الكومنولث", "ركوب الدراجات في دورة الكومنولث", label)
    label = re.sub(r"\s+", " ", label)
    return label
# ---


def make_temp_lines(table, title):
    # ---
    table2 = {"qid": "", "race": "", "p17": "", "poss": ""}
    # ---
    for rr in HeadVars:
        if not rr in table:
            table[rr] = ''
    # ---
    image = table['imagejersey']
    image = re.sub(r'JOJOJO', JOJOJO, image)
    image = image.replace('%20', "_")
    # ---
    date = table['Date']
    flag = table['p17lab']
    # ---
    qid = table['item']
    table2["qid"] = qid
    # ---
    if qid in Skip_items:
        return "", table2
    # ---
    link = table.get('title', '')
    label = table.get('itemlab', '')
    if link != '':
        race = '[[' + link + ']]'
        label = link.split(" (")[0]
    # ---
    label = fix_label(label)
    # ---
    if link != "":
        if label != link:
            race = '[[' + link + '|' + label + ']]'
        else:
            race = '[[' + link + ']]'
    else:
        race = label
    # ---
    sss = table['p642label']
    # الفائز وفقاً لترتيب النقاط للشباب
    sss = re.sub(r'الفائز وفقاً لترتيب', 'الفائز في ترتيب', sss)
    sss = re.sub(r'الفائز حسب التصنيف العام', 'الفائز في التصنيف العام', sss)
    # ---
    ranke = table.get('rank', "")
    # ---
    ranke_tab = {
        "المرتبة 1 في": "الأول في",
        "المرتبة 2 في": "الثاني في",
        "المرتبة 3 في": "الثالث في",
        "المرتبة 4 في": "الرابع في",
        "المرتبة 5 في": "الخامس في",
        "المرتبة 6 في": "السادس في",
        "المرتبة 7 في": "السابع في",
        "المرتبة 8 في": "الثامن في",
        "المرتبة 9 في": "التاسع في",
        "المرتبة 10 في": "العاشر في",
        # "المرتبة 11 في" : "الحادي عشر في",
        # "المرتبة 12 في" : "الثاني عشر في",
    }
    for kk in ranke_tab:
        if ranke.find(kk) >= 0:
            ranke = re.sub(kk, ranke_tab[kk], ranke)
    # ---
    newflag = findflag(race, flag)
    # ---
    table2["race"] = race
    table2["p17"] = newflag
    table2["poss"] = sss
    # ---
    so = '{{نتيجة سباق الدراجات/سطر4'
    so = so + '\n|qid = ' + qid
    so = so + '\n|السباق = ' + race
    so = so + '\n|البلد = ' + newflag
    so = so + '\n|التاريخ = ' + date
    so = so + '\n|المركز = ' + sss
    so = so + '\n|المرتبة = ' + ranke
    so = so + '\n|جيرسي = ' + image
    so = so + '\n}}'
    # ---
    if race and race.lower().strip().startswith("q"):
        printt(' *** remove line startswith q.')
        return "", table2
    # ---
    r'''
    fanco = title
    #fanco = qid
    # ---
    if not fanco in remove_date :
        remove_date[fanco] = 0
    # ---
    if fanco in Work_with_Year :
        if date == '' :
            remove_date[fanco] += 1
            print_test2( 'remove_date[fanco] += 1 (%d) date == ""' % remove_date[fanco] )
            return "", table2
        else:
            hhh = re.match(r'(\d\d\d\d)\-\d\d\-\d\dT\d\d\:\d\d\:\d\dZ', date )
            if hhh :
                if int( hhh.group(1) ) < Work_with_Year[fanco] :
                    remove_date[fanco] += 1
                    print_test2( 'remove_date[fanco] += 1 (%d) date == "%s"' % (remove_date[fanco], date) )
                    return "", table2
    # ---'''
    if ranke != "" and sss.strip() == "":
        if Work_with_Stage[1] == False and Len_of_valid_results.get(title, 0) > 10:
            if re.sub(r"المرتبة 1 في", "", ranke) == ranke and re.sub(r"الأول في", "", ranke) == ranke:
                printt(' *** remove line with rank < 1.')
                return "", table2
    # ---
    if flag != newflag:
        printt(f' *** race:"{race}", flag:"{flag}", newflag:"{newflag}"')
    # ---
    if not title in Len_of_valid_results:
        Len_of_valid_results[title] = 0
    Len_of_valid_results[title] += 1
    # ---
    return so, table2


# ---
qu_2018 = """SELECT
?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?jersey_3 ?jersey_4 ?p642label ?p585 ?p582 ?p580 ?title
WHERE {
SELECT ?item  ?itemlab ?jerseylab ?p17lab
           ?jersey1lab ?image1 ?image2  ?image3 ?image4
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_1)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image2), "/Special:FilePath/"), "|", ?jersey2lab, "}}") AS ?jersey_2)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image3), "/Special:FilePath/"), "|", ?jersey3lab, "}}") AS ?jersey_3)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image4), "/Special:FilePath/"), "|", ?jersey4lab, "}}") AS ?jersey_4)
           ?p642label ?p585 ?p582 ?p580 ?title
           WHERE {
             BIND(wd:Q447532 AS ?aa)
             ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.  ?winner pq:P642 ?P642.
             OPTIONAL {  ?item p:P4323 ?statment1.    ?statment1 ps:P4323 ?aa.    ?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
             OPTIONAL {  ?item p:P2321 ?statment2.    ?statment2 ps:P2321 ?aa.    ?statment2 pq:P2912 ?jersey2.    ?jersey2 wdt:P18 ?image2.  }
             OPTIONAL {  ?item p:P4320 ?statment3.    ?statment3 ps:P4320 ?aa.    ?statment3 pq:P2912 ?jersey3.    ?jersey3 wdt:P18 ?image3.  }
             OPTIONAL {  ?item p:P3494 ?statment4.    ?statment4 ps:P3494 ?aa.    ?statment4 pq:P2912 ?jersey4.    ?jersey4 wdt:P18 ?image4.  }

             OPTIONAL { ?item wdt:P17 ?p17.}
             OPTIONAL { ?item wdt:P585 ?p585.}
             OPTIONAL { ?item wdt:P582 ?p582.}
             OPTIONAL { ?item wdt:P580 ?p580.}
    FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
    FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
    FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
             OPTIONAL { ?sitelink schema:about ?item
                       . ?sitelink schema:isPartOf <https://ar.wikipedia.org/>
                                                      . ?sitelink schema:name ?title }
             SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
                                     ?p17 rdfs:label ?p17lab.
                                     ?item rdfs:label ?itemlab.
                                     ?jersey1 rdfs:label ?jersey1lab.
                                     ?jersey2 rdfs:label ?jersey2lab.
                                     ?jersey3 rdfs:label ?jersey3lab.
                                     ?jersey4 rdfs:label ?jersey4lab.
                                     ?P642 rdfs:label ?p642label.
                                    }

} } """
# ---
q22u = """SELECT
    ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?p642label ?p585 ?p582 ?p580
    WHERE {
    SELECT ?item  ?itemlab ?jerseylab ?image  ?p17lab
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image), "/Special:FilePath/"), "|", ?jerseylab, "}}") AS ?jersey_1)
               ?jersey1lab ?image1
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_2)
               ?p642label  ?p585 ?p582 ?p580
               WHERE {
                 BIND(wd:Q518222 AS ?aa)
                 OPTIONAL {    ?item p:P2417 ?statment.    ?statment ps:P2417 ?aa.    ?statment pq:P2912 ?jersey.    ?jersey wdt:P18 ?image.  }
                 OPTIONAL {    ?item p:P2321 ?statment1.    ?statment1 ps:P2321 ?aa.    ?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
                 OPTIONAL { ?item wdt:P17 ?p17.}
                 OPTIONAL { ?item wdt:P585 ?p585.}
                 OPTIONAL { ?item wdt:P582 ?p582.}
                 OPTIONAL { ?item wdt:P580 ?p580.}
                 ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.
                 ?winner pq:P642 ?P642.
        FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
                 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
                                         ?p17 rdfs:label ?p17lab.
                                         ?item rdfs:label ?itemlab.
                                         ?jersey rdfs:label ?jerseylab.
                                         ?jersey1 rdfs:label ?jersey1lab.
                                         ?P642 rdfs:label ?p642label.
                                        }

    }   } """
# ---


def get_query_results(query):
    # ---
    query = re.sub(r'\n\s+', '\n', query)
    # ---
    fao = urllib.parse.quote(query)
    # ---
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query=' + fao
    # ---
    if "printurl" in sys.argv:
        printt(url)
    # ---
    req = False
    # ---
    try:
        req = session[1].get(url)
    except Exception as e:
        print('<<lightred>> Traceback (most recent call last):')
        print("<<lightred>> Exception:%s." % e)
        print('CRITICAL:')
    # ---
    json1 = {}
    if req:
        try:
            json1 = req.json()
        except Exception as e:
            json1 = {}
            # ---
            print('<<lightred>> Traceback (most recent call last):')
            e = str(e)
            if e.find('java.util.concurrent') != -1:
                e = "java.util.concurrent"
            print("<<lightred>> Exception:%s." % e)
            print('CRITICAL:')
    # ---
    return json1
# ---


def GetSparql(qid, title):
    old_qu = """SELECT
    ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?p642label ?p585 ?p582 ?p580 ?title
    WHERE {
    SELECT ?item  ?itemlab ?jerseylab ?image  ?p17lab
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image), "/Special:FilePath/"), "|", ?jerseylab, "}}") AS ?jersey_1)
               ?jersey1lab ?image1
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_2)
               ?p642label  ?p585 ?p582 ?p580 ?title
               WHERE {
                 BIND(wd:Q518222 AS ?aa)
                 OPTIONAL {    ?item p:P2417 ?statment.    ?statment ps:P2417 ?aa.    ?statment pq:P2912 ?jersey.    ?jersey wdt:P18 ?image.  }
                 OPTIONAL {    ?item p:P2321 ?statment1.    ?statment1 ps:P2321 ?aa.    ?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
                 OPTIONAL { ?item wdt:P17 ?p17.}
                 OPTIONAL { ?item wdt:P585 ?p585.}
                 OPTIONAL { ?item wdt:P582 ?p582.}
                 OPTIONAL { ?item wdt:P580 ?p580.}
                 ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.
                 ?winner pq:P642 ?P642.
        FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
                 OPTIONAL { ?sitelink schema:about ?item
                           . ?sitelink schema:isPartOf <https://ar.wikipedia.org/>
                                                          . ?sitelink schema:name ?title }
                 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
                                         ?p17 rdfs:label ?p17lab.
                                         ?item rdfs:label ?itemlab.
                                         ?jersey rdfs:label ?jerseylab.
                                         ?jersey1 rdfs:label ?jersey1lab.
                                         ?P642 rdfs:label ?p642label.
                                        }

    } } """
    # ---
    qu_2019 = """SELECT DISTINCT ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?jersey_3 ?jersey_4 ?p642label ?p585 ?p582 ?p580 ?rankP4323 ?rankP2321 ?rankP4320 ?rankP3494 ?title
    WHERE {     SELECT DISTINCT ?item ?itemlab ?jerseylab ?p17lab ?rankP4323 ?rankP2321 ?rankP4320 ?rankP3494
               ?jersey1lab ?image1 ?image2  ?image3 ?image4
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_1)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image2), "/Special:FilePath/"), "|", ?jersey2lab, "}}") AS ?jersey_2)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image3), "/Special:FilePath/"), "|", ?jersey3lab, "}}") AS ?jersey_3)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image4), "/Special:FilePath/"), "|", ?jersey4lab, "}}") AS ?jersey_4)
               ?p642label ?p585 ?p582 ?p580 ?title
               WHERE {
                 BIND(wd:Q447532 AS ?aa)
                  ?item wdt:P31 ?a1a.
                 OPTIONAL {  ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.  ?winner pq:P642 ?P642.  }
                  ?item (p:P1346|p:P4323|p:P2321|p:P4320|p:P3494) ?statment0.
                 ?statment0 (ps:P1346|ps:P4323|ps:P2321|ps:P4320|ps:P3494) ?aa.
                 OPTIONAL {  ?item p:P4323 ?statment1 .  ?statment1  ps:P4323 ?aa.
                           OPTIONAL {?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
                           OPTIONAL {?statment1 pq:P1352 ?rankP4323. }
                          }
                 OPTIONAL {  ?item p:P2321 ?statment2 .  ?statment2 ps:P2321 ?aa.
                           OPTIONAL {?statment2 pq:P2912 ?jersey2.    ?jersey2 wdt:P18 ?image2.  }
                           OPTIONAL {?statment2 pq:P1352 ?rankP2321. }
                          }
                 OPTIONAL {  ?item p:P4320 ?statment3 .  ?statment3 ps:P4320 ?aa.
                           OPTIONAL {?statment3 pq:P2912 ?jersey3.    ?jersey3 wdt:P18 ?image3.  }
                           OPTIONAL {?statment3 pq:P1352 ?rankP4320. }
                          }
                 OPTIONAL {  ?item p:P3494 ?statment4 .  ?statment4 ps:P3494 ?aa.
                           OPTIONAL {?statment4 pq:P2912 ?jersey4.    ?jersey4 wdt:P18 ?image4.  }
                           OPTIONAL {?statment4 pq:P1352 ?rankP3494. }
                          }
OPTIONAL { ?item wdt:P17 ?p17.} OPTIONAL { ?item wdt:P585 ?p585.}  OPTIONAL { ?item wdt:P582 ?p582.}  OPTIONAL { ?item wdt:P580 ?p580.}
FILTER NOT EXISTS { ?item wdt:P31 wd:Q20646667. } # plain stage
FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
FILTER NOT EXISTS { ?item wdt:P31 ?P31 . ?P31 wdt:P279 wd:Q18131152 }
FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
OPTIONAL { ?sitelink schema:about ?item
                           . ?sitelink schema:isPartOf <https://ar.wikipedia.org/>
                                                          . ?sitelink schema:name ?title }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
    ?p17 rdfs:label ?p17lab.
    ?item rdfs:label ?itemlab.
    ?jersey1 rdfs:label ?jersey1lab.
    ?jersey2 rdfs:label ?jersey2lab.
    ?jersey3 rdfs:label ?jersey3lab.
    ?jersey4 rdfs:label ?jersey4lab.
    ?P642 rdfs:label ?p642label.
    }

    } } """
    # ---
    qu_2019 = qu_2019.replace('Q447532', qid)
    qu2 = qu_2019
    # ---
    if title in Stage:
        qu2 = qu2.replace('FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }', "")
        qu2 = qu2.replace('FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }', "")
    # }Limit 10  } """
    # ---
    json1 = get_query_results(qu2)
    # ---
    for rr in json1.get('head', {}).get('vars', []):
        HeadVars.append(rr)
    # ---
    bindings = json1.get('results', {}).get('bindings', [])
    # ---
    if len(bindings) > 1:
        return json1
    else:
        # one result or no result
        if title in Stage:
            return {}
        # ---
        qua3 = qu_2019
        qua3 = qua3.replace('FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }', "")
        qua3 = qua3.replace('FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }', "")
        qua3 = qua3.replace('FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }', "")
        qua3 = qua3 + "\n#%s" % menet
        # ---
        json2 = get_query_results(qua3)
        # ---
        print("try 2")
        # ---
        return json2


# ---
# import dateutil.parser
# import operator
# ---
NoAppend = ['p585', 'p582', 'p580']
# ---
ranks_label = {
    "P4323": "المرتبة %s في تصنيف أفضل شاب",
    "P2321": "المرتبة %s في التصنيف العام",
    "P4320": "المرتبة %s في تصنيف الجبال",
    "P3494": "المرتبة %s في تصنيف النقاط",
}
# ---
Len_of_results = {}
Len_of_valid_results = {}
# ---


def fix_results(table):
    results2 = {}
    # ---
    tata = {
        "head": {"vars": ["item", "p17lab", "itemlab", "jersey_1", "jersey_2", "jersey_3", "jersey_4", "p642label", "p585", "p582", "p580", "rankP4323", "rankP2321", "rankP4320", "rankP3494", "title"]},
        "results": {
            "bindings": [{
                "item": {"type": "uri", "value": "http://www.wikidata.org/entity/Q53557910"},
                "title": {"xml:lang": "ar", "type": "literal", "value": "طواف أستونيا 2018"},
                "p580": {"datatype": "http://www.w3.org/2001/XMLSchema#dateTime", "type": "literal", "value": "2018-05-25T00:00:00Z"},
                "p582": {"datatype": "http://www.w3.org/2001/XMLSchema#dateTime", "type": "literal", "value": "2018-05-26T00:00:00Z"},
                "p17lab": {"xml:lang": "ar", "type": "literal", "value": "إستونيا"},
                "itemlab": {"xml:lang": "ar", "type": "literal", "value": "طواف أستونيا 2018"},
                "rankP2321": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "2"},
                "rankP4323": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "1"},
                "rankP3494": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "1"},
                "p642label": {"xml:lang": "ar", "type": "literal", "value": "الفائز وفقاً لترتيب النقاط"},
                "jersey_1": {"type": "literal", "value": "{{JOJOJO|Jersey%20white.svg|قميص أبيض، أفضل شاب}}"},
                "jersey_2": {"type": "literal", "value": "{{JOJOJO|Jersey%20white.svg|قميص أبيض، أفضل شاب}}"},
                "jersey_4": {"type": "literal", "value": "{{JOJOJO|Jersey%20red.svg|قميص أحمر، تصنيف النقاط}}"
                             }
            }]}}
    # ---
    printt("* Lenth fix_results: '%d' ." % len(table))
    for params in table:
        # ---
        if params.get('itemlab', {}).get("value", "").lower().strip().startswith("q"):
            printt(' *** remove line startswith q---.')
            continue
        # ---
        q = 'item' in params and params['item']['value'].split('/entity/')[1]
        # ---
        if not q in results2:
            results2[q] = {'Date': [], 'imagejersey': [], 'item': [], "rank": []}
        # ---
        date = params.get('p585') or params.get('p582') or params.get('p585') or {}
        date = date.get('value') or ''
        # ---
        if not date in results2[q]['Date']:
            results2[q]['Date'].append(date)
        # ---
        for param in params:
            # ---
            value = params[param]['value']
            # ---
            param2 = param
            if param.startswith('rank'):
                param2 = 'rank'
                value2 = param.replace('rank', "")
                if value2 in ranks_label:
                    value = ranks_label[value2] % value
            # ---
            if param.startswith('jersey_'):
                param2 = 'imagejersey'
            # ---
            if param == 'p17lab':
                value = '{{رمز علم|' + value + '}}'
            elif param == 'item':
                value = value.split('/entity/')[1]
            # ---
            # if param == "p642label":
                # value = re.sub(r'الفائز وفقاً ', 'الفائز في ', value )
                # value = re.sub(r'الفائز حسب التصنيف العام ', 'الفائز في التصنيف العام', value )
            # ---
            if not param2 in NoAppend:
                if not param2 in results2[q]:
                    results2[q][param2] = []
                # ---
                if not value in results2[q][param2]:
                    results2[q][param2].append(value)
            # ---
    return results2
# ---


def fix_date(data, title):
    data2 = {}
    # ---
    p642label = 0
    # ---
    for ta in data:
        # ---
        datn = data[ta].get('Date', [])
        # ---
        if type(datn) == list and len(datn) > 0:
            ddds = [x.strip() for x in datn if x.strip() != '']
            # ---
            # print(date)
            # ---
            fanco = title
            if not fanco in remove_date:
                remove_date[fanco] = 0
            # ---
            if fanco in Work_with_Year:
                date = ''
                if ddds != []:
                    date = ddds[0]
                if date == '':
                    remove_date[fanco] += 1
                    # return ""
                    continue
                else:
                    hhh = re.match(r'(\d\d\d\d)\-\d\d\-\d\dT\d\d\:\d\d\:\d\dZ', date)
                    if hhh:
                        if int(hhh.group(1)) < Work_with_Year[fanco]:
                            remove_date[fanco] += 1
                            # print_test2( 'remove_date[fanco] += 1 (%d) date == "%s"' % (remove_date[fanco], date) )
                            # return ""
                            continue
        # ---
        data2[ta] = data[ta]
        if data2[ta].get('p642label', False):
            p642label += 1
        # ---
        if remove_date[fanco] != 0:
            print_test2('remove_date[fanco] += 1 (%d)' % remove_date[fanco])
    # ---
    # Len_of_results[title] = len(data2)
    Len_of_results[title] = p642label
    # ---
    return data2
# ---


def make_new_text(qid, title):
    Date_List2 = []
    # new_lines[title] = []
    new_lines[title] = {}
    json1 = GetSparql(qid, title)
    # ---
    if not json1:
        return False
    # ---
    bindings = json1.get('results', {}).get('bindings', [])
    # ---
    if len(bindings) < 1:
        return False
    # ---
    results = fix_results(bindings)
    # ---
    Len_results = len(results)
    printt("* Lenth results: '%d' ." % Len_results)
    # ---
    # Len_of_results[title] = Len_results
    # ---
    qidso = {}
    num = 0
    for qq in results:
        num += 1
        # ---
        if not qq in qidso:
            qidso[qq] = {}
        # ---
        date = results[qq]['Date'][0]
        if date != '':
            if date not in Date_List2:
                Date_List2.append(date)
        else:
            if qq not in Date_List2:
                Date_List2.append(qq)
        # ---
        qidso[qq] = results[qq]
    # ---
    qids_2 = fix_date(qidso, title)
    # ---
    Date_List2.sort()
    printt('**Date_List2: ')
    # ---
    texxt = ''
    for dd in Date_List2:
        for qoo, tao in qids_2.items():
            # ---
            if qoo in Skip_items:
                continue
            # ---
            date = tao['Date'][0]
            # ---
            if dd == date:
                table = {}
                # ---
                for ss in tao:
                    space = '، '
                    if ss == 'imagejersey' or ss == 'p17lab':
                        space = ''
                    # ---
                    faso = tao[ss]
                    faso.sort()
                    # ---
                    if len(faso) > 0:
                        if len(faso) == 1 or ss == 'p17lab':
                            k = faso[0]
                        elif len(faso) > 1:
                            k = space.join(faso)
                        # ---
                        if ss == 'Date':
                            k = faso[0]
                        # ---
                        table[ss] = k
                # ---
                v, tab = make_temp_lines(table, title)
                # ---
                if v != "":
                    vvv = re.sub(r"\n", "", v)
                    new_lines[title][qoo] = tab
                    new_lines[title][qoo]["qid"] = qoo
                    new_lines[title][qoo]["race"] = tab.get("race", "")  # re.sub( regline, "\g<race>", vvv )
                    new_lines[title][qoo]["p17"] = tab.get("p17", "")  # re.sub( regline, "\g<p17>", vvv )
                    new_lines[title][qoo]["poss"] = tab.get("poss", "")  # re.sub( regline, "\g<poss>", vvv )
                    # ---
                    texxt = texxt + v + '\n'
                # ---
    note = '<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->\n'
    texxt = note + texxt
    # ---
    t24 = Len_of_valid_results.get(title, 0)
    t23 = Len_of_results.get(title, 0)
    printt(f"Len_of_valid_results : {t24}, Len_of_results : {t23}")
    printt(f"Len_of_valid_results : {t24}, Len_of_results : {t23}")
    # ---
    # ---
    return texxt
# ---


def GetSectionNew3(text):
    printt('**GetSectionNew3: ')
    text = text
    text2 = text
    FirsPart = ''
    # temp1 = '{{نتيجة سباق الدراجات/بداية|wikidatalist=t}}'
    # temptop = '{{نتيجة سباق الدراجات/بداية}}'
    # ---
    Frist = re.compile(r'\{\{نتيجة سباق الدراجات\/بداية\s*?.*?\}\}')
    Fristsss = Frist.findall(text)
    if Fristsss:
        printt('Section: ')
        FirsPart = Fristsss[0]
        printt(FirsPart)
    # ---
    if FirsPart != '':
        text2 = text2.split(FirsPart)[1]
        text2 = FirsPart + text2
    # ---
    text2 = text2.split('{{نتيجة سباق الدراجات/نهاية}}')[0]
    text2 = text2 + '{{نتيجة سباق الدراجات/نهاية}}'
    # ---
    return text2, FirsPart


# ---
returntext = {1: True}
# ---


def make_dada(NewText, MainTitle):
    url = "https://" + "ar.wikipedia.org/w/index.php?title=" + ec_de_code(MainTitle, 'decode') + '&action=submit'
    t = "<form id='editform' name='editform' method='POST' action='" + url + "'>"
    t += "<textarea id='wikitext-new' class='form-control' name='wpTextbox1'>" + NewText + "</textarea>"
    t += '''
<input type='hidden' name='wpSummary' value='تحديث نتائج اللاعب'/>
<input id='btn-saveandreturn' type='submit' class='btn' name='wpDiff' value='Save &amp; Return' title='Open the edit interface in a new tab/window, then quietly return to the main page.'/>
<input id='wpPreview' type='submit' class='btn-lg' tabindex='5' title='[p]' accesskey='p' name='wpPreview' value='Preview changes'/>
<input id='wpDiff' type='submit' class='btn-lg' tabindex='7' name='wpDiff' value='show changes' accesskey='v' title='show changes.'/>
</form>'''
    return t
# ---


def page_put(NewText, summ, MainTitle):
    printt(' page_put: ' + br)
    # try:
    title = ec_de_code(MainTitle, 'decode')
    # ---
    printt(' page_put %s:' % (MainTitle) + br)
    # print_test2( NewText )
    # ---
    if (not TEST[1] and not TEST[2]) or workibrahem:
        r4 = session[1].post(api_url, data={
            "action": "edit",
            "format": "json",
            "title": title,
            "text": NewText,
            "summary": summ,
            "bot": 1,
            "nocreate": 1,
            "token": session["csrftoken"],
        })
        if workibrahem:
            print(r4.text)
        if 'nochange' in r4.text:
            printo('nodiff')
        elif 'Success' in r4.text:
            # print('** true .. ' + '[[' + title + ']]' )
            # print('* true . ')
            printo('true')
            # printo( r4.text )
        elif 'abusefilter-disallowed' in r4.text and returntext[1]:
            texts = "</br>خطأ عند تعديل الصفحة، قم بنسخ المحتوى أدناه إلى الصفحة:</br>"
            texts += make_dada(NewText, MainTitle)
            printo(texts)
        else:
            printo(r4.text)


# ---
lines = {}
new_lines = {}
states = {}
# ---
# new_lines
# ---
regline = r"\{\{نتيجة سباق الدراجات/سطر4"
regline += r"\|\s*qid\s*\=(?P<qid>Q\d+)"
regline += r"\|\s*السباق\s*\=(?P<race>.*)"
regline += r"\|\s*البلد\s*\=(?P<p17>.*)"
regline += r"\|\s*التاريخ\s*\=(?P<date>.*)"
regline += r"\|\s*المركز\s*\=(?P<poss>.*)"
regline += r"\|\s*(?:rank|المرتبة)\s*\=(?P<rank>.*)"
regline += r"\|\s*جيرسي\s*\=(?P<jersey>.*)"
regline += r"\s*\|\}\}"
# ---


def work_tano(text, MainTitle):
    # ---
    lines[MainTitle] = {}  # []
    # ---
    # reg_line2 = '\{\{نتيجة سباق الدراجات\/سطر4\s*?.*?\}\}'
    reg_line = r'\{\{نتيجة سباق الدراجات\/سطر4([^{]|\{[^{]|\{\{[^{}]+\}\})+\}\}'
    re.compile(reg_line)
    # pas = fff.findall( text )
    # ---
    # vf = re.compile(r'\{\{نتيجة سباق الدراجات\/سطر4([^{]|\{[^{]|\{\{[^{}]+\}\})+\}\}' ).findall( text )
    if text.startswith("{{نتيجة سباق الدراجات/بداية}}\n<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->"):
        text = text.replace("{{نتيجة سباق الدراجات/بداية}}\n<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->", "")
    text = text.replace("{{نتيجة سباق الدراجات/نهاية}}", "")
    text = text.strip()
    vf = text.split("{{نتيجة سباق الدراجات/سطر4")
    # ---
    if vf:
        for pp in vf:
            if pp == "":
                continue
            # ---
            if not pp.startswith("{{نتيجة سباق الدراجات/سطر4"):
                pp = "{{نتيجة سباق الدراجات/سطر4" + pp
            # ---
            q_id = ""
            # q_id = re.sub(r".*(Q\d+).*", "\g<1>", pp )
            ppr = re.sub(r"\n", "", pp)
            q_id = re.sub(r"\{\{نتيجة سباق الدراجات\/سطر4\|qid\s*\=\s*(Q\d+)\|.*\}\}", r"\g<1>", ppr)
            # if TEST[1]:
            # print( ppr )
            # print( ppr )
            hhh = re.match(r'.*(Q\d+).*', ppr)
            if hhh:
                if q_id != hhh.group(1):
                    q_id = hhh.group(1)
            # lines[MainTitle].append( q_id )
            lines[MainTitle][q_id] = {}
            lines[MainTitle][q_id]["qid"] = q_id
            lines[MainTitle][q_id]["poss"] = re.sub(regline, r"\g<poss>", ppr)
            lines[MainTitle][q_id]["rank"] = re.sub(regline, r"\g<rank>", ppr)
            lines[MainTitle][q_id]["race"] = re.sub(regline, r"\g<race>", ppr)
            lines[MainTitle][q_id]["p17"] = re.sub(regline, r"\g<p17>", ppr)
            # ---
            # print( q_id )
            # print( "========================" )
    # ---
    # print( "lenth sections : %d"  % len( lines[MainTitle] ) )
    # ---
    new_line = 0
    same_line = 0
    removed_line = 0
    # ---
    if MainTitle in new_lines:
        for line in new_lines[MainTitle].keys():
            # ---
            if line == "Q49164584" and TEST[1]:
                print(new_lines[MainTitle][line])
            # ---
            # print( "new_lines:%s" % line )
            same = 0
            new = 0
            if line in lines[MainTitle].keys():
                for x in ["poss", "race", "p17"]:
                    if new_lines[MainTitle][line][x] == lines[MainTitle][line][x]:
                        same = 1
                    else:
                        new = 1
            else:
                new = 1
            # ---
            if same == 1:
                same_line += 1
            elif new == 1:
                new_line += 1
            # ---
        # ---
        for liner in lines[MainTitle].keys():
            # print( "lines:%s" % liner )
            if not liner in new_lines[MainTitle].keys():
                removed_line += 1
    # ---
    states[MainTitle] = {"new_line": new_line, "same_line": same_line, "removed_line": removed_line}
    # ---
    liner = "new_line:%d,same_line:%d,removed_line:%d" % (new_line, same_line, removed_line)
    # ---
    if MainTitle in remove_date and remove_date[MainTitle] != 0:
        liner += ',removed_line_date:%d' % remove_date[MainTitle]
        states[MainTitle]['removed_line_date'] = remove_date[MainTitle]
    # ---
    return liner
    # ---


def puttext(text, MainTitle, Newsect):
    printt('**puttext: ' + br)
    sect, Frist = GetSectionNew3(text)
    # ---
    work_tano(sect, MainTitle)
    # ---
    text = text
    Newsect = Frist + '\n' + Newsect + '{{نتيجة سباق الدراجات/نهاية}}'
    Newsect = re.sub(r'\n\n{{نتيجة سباق الدراجات/نهاية}}', '\n{{نتيجة سباق الدراجات/نهاية}}', Newsect)
    NewText = text.replace(sect, Newsect)
    summ = 'بوت:تجربة تحديث بيانات اللاعب'
    if workibrahem:
        summ = ''
    printt('showDiff of page: ' + MainTitle + br)
    if MainTitle in states:
        if states[MainTitle]["new_line"] != 0 or states[MainTitle]["removed_line"] != 0 and text != NewText:
            page_put(NewText, summ, MainTitle)
        else:
            printo('nodiff')
# ---


def template_params(text, title):
    Frist = re.compile(r'\{\{نتيجة سباق الدراجات\/بداية\s*?.*?\}\}')
    pas = Frist.findall(text)
    # ---
    if not pas:
        return False, False
    # ---
    params = str(pas[0])
    params = re.sub(r"\s*\=\s*", "=", params)
    params = re.sub(r"\s*\|\s*", "|", params)
    # ---
    do = re.search(r'.*\|تاريخ\=(\d+)(\}\}|\|)', text)
    if do:
        Work_with_Year[title] = int(do.group(1))
        print_test2("Work_with_Year:%s" % do.group(1))
    # ---
    if re.sub(r"مراحل\s*\=\s*نعم", "", params) != params:
        printt("Work with Stage")
        Work_with_Stage[1] = True
        Stage[title] = ""
    # ---
    if re.sub(r".*id\s*\=\s*(Q\d+).*", r"\g<1>", params) != params:
        printt('** found currect line')
        Qid = re.sub(r".*id\=(Q\d+).*", r"\g<1>", params)
        printt('id: ' + Qid)
        return Qid, True
    # ---
    return False, False
# ---


def CheckTempalteInPageText(text):
    printt('**CheckTempalteInPageText: ' + br)
    # ---
    # \{\{template_tesult(\|id\=Q\d+|)\}\}
    Topname = r'نتيجة سباق الدراجات\/بداية'
    Top = r'\{\{' + Topname + r'\}\}'
    Top2 = r'\{\{' + Topname + r'\s*\|\s*id\s*\=\s*Q\d+\s*\}\}'
    Top3 = r'\{\{' + Topname + r'\s*?.*?\}\}'
    Bottom = r'\{\{نتيجة سباق الدراجات\/نهاية\}\}'
    if text != '':
        # ---
        Check_Top = re.sub(Top, '', text)
        Check_Top2 = re.sub(Top2, '', text)
        Check_Top3 = re.sub(Top3, '', text)
        Check_Bottom = re.sub(Bottom, '', text)
        # ---
        if (text == Check_Top) and (text == Check_Top2) and (text == Check_Top3):
            po = 'لا يمكن إيجاد ' + '{{نتيجة سباق الدراجات/بداية ' + 'في الصفحة. '
            printo(po)
            return False
        elif text == Check_Bottom:
            oo = 'لا يمكن إيجاد ' + '{{نتيجة سباق الدراجات/نهاية}} ' + 'في الصفحة. '
            printo(oo)
            return False
        else:
            printt(' * Tempaltes Already there.' + br)
            return True
    else:
        printt(' * no text.' + br)
# ---


def GetPageText(title):
    text, item = '', False
    printt('**GetPageText: ' + br)
    # ---
    tit = title  # ec_de_code(title, 'encode')
    # ---
    url = 'https://' + 'ar.wikipedia.org/w/api.php?action=parse&prop=wikitext|properties&utf8=1&format=json&page=' + tit
    printt('url:' + url)
    # ---
    json1 = {}
    try:
        json1 = session[1].get(url).json()
    except Exception as e:
        print('<<lightred>> Traceback (most recent call last):')
        print("<<lightred>> Exception:%s." % e)
        print('CRITICAL:')
    # ---
    if not json1:
        return text, item
    # ---
    printt('find json1:' + br)
    # ---
    parse = json1.get('parse', {})
    if parse != {}:
        printt('find parse in json1:' + br)
        # ---
        text = parse.get('wikitext', {}).get('*', '')
        if text != '':
            printt('find wikitext in parse:' + br)
            printt('find * in parse.wikitext :' + br)
        # ---
        properties = parse.get('properties', [])
        # ---
        if properties != []:
            printt('find properties in parse:' + br)
            for prop in properties:
                if 'name' in prop:
                    if prop['name'] == "wikibase_item":
                        item = prop['*']
                        printt('find item in parse.wikitext :' + item + br)
                        break
    # ---
    elif 'error' in json1:
        text = False
        if 'info' in json1['error']:
            printt(json1['error']['info'])
        else:
            printt(json1)
    else:
        printt('no parse in json1:' + br)
        printt(json1)
    # ---
    return text, item
# ---


def StartOnePage(title):
    printt('**StartOnePage: ' + br)
    # ---
    title = title.replace('_', ' ')
    # ---
    if title.find("%") == -1:
        title = ec_de_code(title, 'encode')
        # print( 'title encode: ' + title )
    # ---
    text, item = GetPageText(title)
    # ---
    if not text or text == '':
        printo('الصفحة المطلوبة غير موجودة أو أن محتواها فارغ.')
        return
    # ---
    Check = CheckTempalteInPageText(text)
    # ---
    if not Check:
        printt('no Check: pass....' + br)
        return
    # ---
    printt('**Isre: ')
    # ---
    Qid, QidinTemplate = template_params(text, title)
    if QidinTemplate:
        item = Qid
    # if not Qid:
        # Qid = getwditem(title)
    # ---
    if not item:
        if QidinTemplate:
            NewText = "<!-- Can't find item by item :\"" + item + "\" --> "
            printt("**" + NewText)
        else:
            NewText = "<!-- Can't find item in page :\"" + title + "\" --> "
            printt("**" + NewText)
    # ---
    if not item:
        return
    # ---
    printt('**item: ' + item)
    NewText = make_new_text(item, title)
    # ---
    if NewText:
        printt('**puttext::: ')
        puttext(text, title, NewText)
    else:
        ur = (f'<a href="https://www.wikidata.org/wiki/{item}">{item}</a>.')
        printo('لا توجد نتائج لهذه الصفحة تأكد من صحة معرف ويكي بيانات: %s.' % ur)

        # print(ur)
    # ---
br = '</br>'
# ---


def main():
    # ---
    title = ''
    # ---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        # ---
        if arg == 'test':
            TEST[1] = True
        # ---
        if arg == '-title' or arg == '-page':
            title = value
        # ---
        if arg == 'test2':
            TEST[2] = True
        # ---
        if arg == "text":
            returntext[1] = True
    # ---
    if TEST[1]:
        printt('TestMain:' + br)
        # python pwb.py cy5 test
        # StartOnePage('%D8%B3%D9%8A%D9%84%D9%81%D8%A7%D9%86_%D8%AA%D8%B4%D8%A7%D9%81%D8%A7%D9%86%D9%8A%D9%84')
        # StartOnePage('%D8%AC%D8%A7%D9%8A_%D9%83%D8%B1%D9%88%D9%81%D9%88%D8%B1%D8%AF')
        # StartOnePage('%D8%AF%D9%88%D9%85%D9%8A%D9%86%D9%8A%D9%83%D9%88_%D8%A8%D9%88%D8%B2%D9%88%D9%81%D9%8A%D9%81%D9%88')
        # StartOnePage('%D8%A2%D8%B4%D9%84%D9%8A_%D9%85%D9%88%D9%84%D9%85%D8%A7%D9%86')
        StartOnePage('%D8%B1%D9%8A%D8%AA%D8%B4%D9%8A_%D8%A8%D9%88%D8%B1%D8%AA')
    # make_new_text('Q286183')#
    # ---
    # StartOnePage('%D8%B3%D9%8A%D9%84%D9%81%D8%A7%D9%86_%D8%AA%D8%B4%D8%A7%D9%81%D8%A7%D9%86%D9%8A%D9%84')
    if title != '':
        StartOnePage(title)
    else:
        printo('title==""')


# ---
tty = """
===سباقات أو مراحل فاز بها===
{{نتيجة سباق الدراجات/بداية|مراحل=نعم | id = Q623
}}
<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->
{{نتيجة سباق الدراجات/سطر4
|qid = Q3003022
|السباق = [[كريثيديا دو دوفين 2013]]
|البلد = {{رمز علم|سويسرا}}
|التاريخ = 2013-06-09T00:00:00Z
|المركز = المركز الثاني
|جيرسي =
|}}
{{نتيجة سباق الدراجات/سطر4
|qid = Q28948862
|السباق = [[كريثيديا دو دوفين 2017]]
|البلد = {{رمز علم|سويسرا}}
|التاريخ = 2017-06-11T00:00:00Z
|المركز = المركز الثاني
|جيرسي =
|}}
{{نتيجة سباق الدراجات/نهاية}}

"""
if __name__ == "__main__":
    # GetSparql("Q3266987", "")
    main()
    # s, o = template_params(tty, "dfdfdf")
    # print(s)
# ---

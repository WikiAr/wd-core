#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
'''
#استعلام خنافس

SELECT DISTINCT 
?en  (COUNT(?en) AS ?count) WHERE {
  ?item wdt:P171* wd:Q22671.
  ?item wdt:P105 wd:Q7432.
  #?item schema:description ?en.
  ?item schema:description ?en. FILTER((LANG(?en)) = "en")
}

GROUP BY ?en
ORDER BY DESC(?count)
#LIMIT 3000
'''
# ---
# start of newdesc.py file
# from wd_API import newdesc
#   newdesc.main_from_file(file , topic , translations2)
#   newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
#
import re
import time
import codecs
import pywikibot
import json
# import sys
from pywikibot import pagegenerators as pg
import unicodedata
# import urllib
# import urllib.request
# import urllib.parse
import unicodedata
# ---
import sys
# ---
import urllib
import urllib.request
import urllib.parse
# ---
from wd_API import wd_bot
#---
from wd_API import wd_desc
# wd_desc.wwdesc(NewDesc, qid, i, fixlang, ask="", tage='')
# wd_desc.work_api_desc(NewDesc, qid, addedlangs=[], fixlang=[], ask="")
#---
quuu = {}
quuu['species of beetle'] = """
SELECT DISTINCT 
?item WHERE {
    BIND("species of beetle"@en AS ?en) ?item schema:description ?en.
    
    BIND("espèces de coléoptères"@fr AS ?fr) 
    BIND("specie di coleottero"@it AS ?it) 
    {?item schema:description ?it. } UNION {?item schema:description ?fr.}
    #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 20000"""
quuu['species of insect'] = """
SELECT DISTINCT 
?item WHERE {
    BIND("species of insect"@en AS ?en) ?item schema:description ?en.
    BIND("espèce de coléoptères"@fr AS ?fr)
    BIND("specie di coleottero"@it AS ?it)
    {?item schema:description ?it. } UNION {?item schema:description ?fr.}
    #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 100000"""
# ---
# start of newdesc.py file
# from wd_API import newdesc
# newdesc.work22(q , topic, translations)
# newdesc.main_from_file(file , topic , translations)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
# from API.replacement import replacement
# ---
translations = {
    'species of beetle': {
        'it': 'specie di coleotteri',
        # 'fr': 'espèces de coléoptères',
        'fr': 'espèce de coléoptères',

    },
    'species of insect': {
        'it': 'specie di insetti',
        # 'fr': "espèces d'insectes",
        'fr': "espèce d'insectes",

    },
}
# ---


def work2(item, topic):
    item.get()
    # ---
    ItemDescriptions = item.descriptions
    NewDesc = {}
    fixlang = []
    q = item.title(as_link=False)
    # ---
    if "en" in ItemDescriptions.keys():
        en = ItemDescriptions["en"]  # ['value']
        # ---
        if en in translations.keys():
            replacement = translations[en]
            for lang in replacement.keys():
                if lang in ItemDescriptions.keys():
                    value = ItemDescriptions[lang]  # ['value']
                    if value != replacement[lang]:
                        NewDesc[lang] = {"language": lang,
                                         "value": replacement[lang]}
                        pywikibot.output('<<lightyellow>> {}:replace "{}" by: "{}".'.format(
                            lang, value, replacement[lang]))
                        fixlang.append(lang)
                else:
                    NewDesc[lang] = {"language": lang,
                                     "value": translations[topic][lang]}
                    # addedlangs.append(lang)
            # ---
            # pywikibot.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )
            wd_desc.wwdesc(NewDesc, q, 1, fixlang, ask=False)
# ---


def mam():
    topic = 'species of insect'
    pywikibot.output('*<<lightyellow>> mainfromQuarry:')
    Quarry = quuu[topic]
    if sys.argv and "OFFSET" in sys.argv:
        Quarry = Quarry + " OFFSET 100000"
    json = wd_bot.wd_sparql_generator_url(Quarry)
    lenth = len(json)
    num = 0
    # topic = 'Wikinews article'
    # ---
    for item in json:
        num += 1
        q = item.title(as_link=False)
        pywikibot.output(
            '<<lightyellow>>*mainfromQuarry: %d/%d topic:"%s" , q:"%s".' % (num, lenth, topic, q))
        work2(item, topic)


# ---
if __name__ == "__main__":
    mam()
# ---

#!/usr/bin/env python3
#  fix disambiguation
#

# ---
# start of newdesc.py file

#   newdesc.main_from_file(file , topic , translations2)
#   newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
#
from API import open_url

import pywikibot
import json
# import sys
# import urllib
# import urllib.request
# import urllib.parse
# ---
# ---

# ---
from wd_api import wd_bot
from wd_api import wd_desc
from desc_dicts.descraptions import *
# ---
translations = {}
translations['Wikimedia disambiguation page'] = DescraptionsTable['Wikimedia disambiguation page']
# ---
replacement = {}
replacement["fa"] = {
    "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"],
    "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"],
    "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"],
    "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"]
}
# ---


def work2(item, topic):
    try:
        item.get()
    except BaseException:
        pywikibot.output('<<lightyellow>>  cant item.get()')
        return ''

    # OOutPut( '<<lightyellow>> **newdesc: work2:'  + item.title(as_link=False))
    # ItemDescriptions = {}
    # ---
    keys = [x for x in translations[topic].keys()]
    # ---
    ItemDescriptions = item.descriptions
    NewDesc = {}
    addedlangs = []
    replacelang = []
    q = item.title(as_link=False)
    # ---
    for lang in ItemDescriptions.keys():  # استبدال
        if lang in replacement.keys():
            value = ItemDescriptions[lang]  # ['value']
            if 'value' in ItemDescriptions[lang]:
                value = ItemDescriptions[lang]['value']
            # ---
            if value in replacement[lang]:
                NewDesc[lang] = {
                    "language": lang,
                    "value": replacement[lang][value]
                }
                # pywikibot.output( '<<lightyellow>>  replace "%s" by: "%s".' % ( value , replacement[lang][value]) )
                replacelang.append(lang)
    # ---
    for lang in keys:
        if lang not in ItemDescriptions.keys():
            NewDesc[lang] = {
                "language": lang,
                "value": translations[topic][lang]
            }
            addedlangs.append(lang)
    # ---
    # pywikibot.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )

    wd_desc.work_api_desc(NewDesc, q)


# ---


def mainfromQuarry():
    pywikibot.output('*<<lightyellow>> mainfromQuarry:')
    Quarry = '''SELECT DISTINCT ?item
WHERE {
  ?item schema:description "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا"@fa.
}
limit 10000'''

    Quarry2 = '''SELECT ?item
WHERE {VALUES (?item) {(wd:Q29976539) }
?item ?s ?ss}
limit 1'''
    json1 = wd_bot.wd_sparql_generator_url(Quarry2)
    lenth = len(json1)
    num = 0
    topic = 'Wikimedia disambiguation page'
    # ---
    for item in json1:
        num += 1
        q = item.title(as_link=False)
        pywikibot.output('<<lightyellow>>*mainfromQuarry: %d/%d topic:"%s" , q:"%s".' % (num, lenth, topic, q))
        work2(item, topic)


# ---
wikidatasite = pywikibot.Site('wikidata', 'wikidata')
repo = wikidatasite.data_repository()
# ---
# open_url.getURL( url )
# ---


def mainfromQuarry2():
    pywikibot.output('*<<lightyellow>> mainfromQuarry:')
    # quarrr = '207388'
    quarrr = '207496'
    num = 0
    url = 'https://quarry.wmflabs.org/run/' + quarrr + '/output/1/json'
    sparql = open_url.getURL(url=url)
    jso = json.loads(sparql)
    topic = 'Wikimedia disambiguation page'
    list = ["Q" + str(x[0]) for x in jso['rows'] if x[1] == "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا"]
    for page in list:
        item = pywikibot.ItemPage(repo, page.strip())
        num += 1
        q = item.title(as_link=False)
        pywikibot.output('<<lightyellow>>*mainfromQuarry: %d/%d topic:"%s" , q:"%s".' % (num, len(list), topic, q))
        work2(item, topic)


# ---
if __name__ == "__main__":
    mainfromQuarry2()
# ---

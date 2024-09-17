#!/usr/bin/env python3
#  fix disambiguation
#

# ---


#   newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
#
from API import open_url

from wd_api import wd_bot
import pywikibot
import json

from wd_api import wd_desc
from desc_dicts.descraptions import DescraptionsTable
# from desc_dicts.descraptions import *

# ---
translations = {"Wikimedia disambiguation page": DescraptionsTable["Wikimedia disambiguation page"]}
# ---
replacement = {}
replacement["fa"] = {
    "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا": DescraptionsTable["Wikimedia disambiguation page"]["fa"],
    # "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"],
    # "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا": DescraptionsTable['Wikimedia disambiguation page']["fa"],
    "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا": DescraptionsTable["Wikimedia disambiguation page"]["fa"],
}


def work2(q, topic):
    # ---
    # OOutPut( '<<lightyellow>> **newdesc: work2:'  + q)
    # ItemDescriptions = {}
    # ---
    ItemDescriptions = wd_bot.Get_item_descriptions_or_labels(q, "descriptions")
    # ---
    keys = list(translations[topic].keys())
    # ---
    NewDesc = {}
    addedlangs = []
    replacelang = []
    # ---
    for lang in ItemDescriptions.keys():  # استبدال
        if lang in replacement.keys():
            value = ItemDescriptions[lang]  # ['value']
            if "value" in ItemDescriptions[lang]:
                value = ItemDescriptions[lang]["value"]
            # ---
            if value in replacement[lang]:
                NewDesc[lang] = {"language": lang, "value": replacement[lang][value]}
                # pywikibot.output( '<<lightyellow>>  replace "%s" by: "%s".' % ( value , replacement[lang][value]) )
                replacelang.append(lang)
    # ---
    for lang in keys:
        if lang not in ItemDescriptions.keys():
            NewDesc[lang] = {"language": lang, "value": translations[topic][lang]}
            addedlangs.append(lang)
    # ---
    # pywikibot.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )

    wd_desc.work_api_desc(NewDesc, q)


def mainfromQuarry():
    pywikibot.output("*<<lightyellow>> mainfromQuarry:")
    Quarry = """SELECT DISTINCT ?item
WHERE {
  ?item schema:description "یک صفحهٔ ابهام\\u200cزدایی در ویکی\\u200cپدیا"@fa.
}
limit 10000"""

    Quarry2 = """SELECT ?item
WHERE {VALUES (?item) {(wd:Q29976539) }
?item ?s ?ss}
limit 1"""
    json1 = wd_bot.wd_sparql_generator_url(Quarry2, returnq=True)
    lenth = len(json1)
    topic = "Wikimedia disambiguation page"
    # ---
    for num, q in enumerate(json1, start=1):
        pywikibot.output(f'<<lightyellow>>*mainfromQuarry: {num}/{lenth} topic:"{topic}" , q:"{q}".')
        work2(q, topic)


# ---
wikidatasite = pywikibot.Site("wikidata", "wikidata")
repo = wikidatasite.data_repository()
# ---
# open_url.open_the_url( url )


def mainfromQuarry2():
    pywikibot.output("*<<lightyellow>> mainfromQuarry:")
    # ---
    # quarrr = '207388'
    quarrr = "207496"
    # ---
    url = f"https://quarry.wmcloud.org/run/{quarrr}/output/1/json"
    # ---
    sparql = open_url.open_the_url(url=url)
    # ---
    jso = json.loads(sparql)
    # ---
    topic = "Wikimedia disambiguation page"
    # ---
    lista = [f"Q{str(x[0])}" for x in jso["rows"] if x[1] == "یک صفحهٔ ابهام\u200cزدایی در ویکی\u200cپدیا"]
    # ---
    for num, page in enumerate(lista, start=1):
        q = page.strip()
        pywikibot.output(f'<<lightyellow>>*mainfromQuarry: {num}/{len(lista)} topic:"{topic}" , q:"{q}".')
        work2(q, topic)


if __name__ == "__main__":
    mainfromQuarry2()

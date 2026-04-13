#!/usr/bin/env python3 core8/pwb.py

#  python3 core8/pwb.py wd/wikinews
#

import logging

from . import wd_desc

# from bots_subs.wd_api import newdesc
# newdesc.mainfromQuarry ( topic, Quarry, translations)
# newdesc.mainfromQuarry2( topic, Quarry, translations)


logger = logging.getLogger(__name__)
from . import wd_bot

translations = {
    "Wikimedia module": {  # Q4167836
        "ar": "وحدة ويكيميديا",
        "en": "Wikimedia module",
        "nl": "Wikimedia-module",
        "he": "יחידה של ויקימדיה",
        "bg": "Уикимедия модул",
    }
}

# from bots_subs.wd_api import newdesc
# newdesc.work22(q, topic, translations)
# newdesc.work2_with_replacement(item, topic, translations, replacement_ke)
# newdesc.mainfromQuarry2( topic, Quarry, translations)
# newdesc.Quarry_with_item_langs( p31, Quarry, translations)

# from API.replacement import replacement


def work2_with_replacement(item, topic, translations, replacement_ke):
    item.get()
    # logger.info( '<<lightyellow>> **newdesc: work2:'  + item.title(as_link=False))
    # ItemDescriptions = {}
    # ---
    keys1 = sorted([x for x in translations[topic].keys()])
    # ---
    if "en" in keys1:
        keys1.append("en-gb")
        keys1.append("en-ca")
    # ---
    ItemDescriptions = item.descriptions
    NewDesc = {}
    # ---
    q = item.title(as_link=False)
    # ---
    for lang in replacement_ke.keys():  # استبدال
        if lang in ItemDescriptions.keys() and lang in keys1:
            value = ItemDescriptions[lang]
            if value in replacement_ke[lang]:
                NewDesc[lang] = {"language": lang, "value": translations[topic][lang]}
                logger.info(f'<<lightyellow>> replace "{value}" by: "{translations[topic][lang]}".')
    # ---
    for lang in keys1:
        if lang not in ItemDescriptions.keys():
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            NewDesc[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    # logger.info( '<<lightyellow>>  NewDesc' + str(NewDesc) )
    wd_desc.work_api_desc(NewDesc, q)


def work22(q, topic, translations):
    # ---
    keys = sorted([x for x in translations[topic].keys()])
    if "en" in keys:
        keys.append("en-gb")
        keys.append("en-ca")
    # ---
    ItemDescriptions = wd_bot.Get_item_descriptions_or_labels(q, "descriptions")
    # ---
    if not ItemDescriptions or not isinstance(ItemDescriptions, dict):
        ItemDescriptions = {}
    # ---
    ItemDesc_keys = list(ItemDescriptions.keys())
    # ---
    NewDesc = {}
    # ---
    for lang in keys:
        if lang not in ItemDesc_keys:
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            NewDesc[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    wd_desc.work_api_desc(NewDesc, q)


def mainfromQuarry(topic, Quarry, translations):
    # logger.info( '*<<lightyellow>> mainfromQuarry:' )
    # Quarry = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q17633526.}'
    json = wd_bot.sparql_generator_url_Z(Quarry)
    lenth = len(json)
    num = 0
    # ---
    for item in json:
        num += 1
        q = "item" in item and item["item"].split("/entity/")[1]
        logger.info(f'<<lightyellow>>*mainfromQuarry: {num}/{lenth} topic:"{topic}", q:"{q}".')
        work22(q, topic, translations)


def Quarry_with_item_langs(p31, Quarry, translations):
    json = wd_bot.sparql_generator_url_Z(Quarry)
    lenth = len(json)
    num = 0
    # ---
    p31_langs = list(translations.get(p31, {}).keys())
    # ---
    for item in json:
        num += 1
        q = "item" in item and item["item"].split("/entity/")[1]
        logger.info(f'<<lightyellow>>*mainfromQuarry: {num}/{lenth} p31:"{p31}", q:"{q}".')
        # ---
        q_langs = item.get("langs", "").split(",")
        # ---
        lang_to_add = list(set(p31_langs) - set(q_langs))
        # ---
        if len(lang_to_add) > 0:
            work22(q, p31, translations)


def mainfromQuarry2(topic, Quarry, translations):
    mainfromQuarry(topic, Quarry, translations)


def work2(item, topic, translations):
    # ---
    keys = sorted([x for x in translations[topic].keys()])
    if "en" in keys:
        keys.append("en-gb")
        keys.append("en-ca")
    # ---
    NewDesc = {}
    # ---
    item.get()
    # ---
    q = item.title(as_link=False)
    # ---
    ItemDescriptions = item.descriptions
    # ---
    for lang in keys:
        if lang not in ItemDescriptions.keys():
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            NewDesc[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    wd_desc.work_api_desc(NewDesc, q)

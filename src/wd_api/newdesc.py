#

import logging

from . import wd_bot, wd_desc, wd_sparql_bot

logger = logging.getLogger(__name__)
translations = {
    "Wikimedia module": {  # Q4167836
        "ar": "وحدة ويكيميديا",
        "en": "Wikimedia module",
        "nl": "Wikimedia-module",
        "he": "יחידה של ויקימדיה",
        "bg": "Уикимедия модул",
    }
}


def work2_with_replacement(item, topic, translations, replacement_ke) -> None:
    item.get()
    # logger.info( '<<lightyellow>> **newdesc: work2:'  + item.title(as_link=False))
    # item_descriptions = {}
    # ---
    keys1 = sorted(translations[topic].keys())
    # ---
    if "en" in keys1:
        keys1.append("en-gb")
        keys1.append("en-ca")
    # ---
    item_descriptions = item.descriptions
    new_desc_data = {}
    # ---
    q = item.title(as_link=False)
    # ---
    for lang in replacement_ke.keys():  # استبدال
        if lang in item_descriptions.keys() and lang in keys1:
            value = item_descriptions[lang]
            if value in replacement_ke[lang]:
                new_desc_data[lang] = {"language": lang, "value": translations[topic][lang]}
                logger.info(f'<<lightyellow>> replace "{value}" by: "{translations[topic][lang]}".')
    # ---
    for lang in keys1:
        if lang not in item_descriptions.keys():
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            new_desc_data[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    # logger.info( '<<lightyellow>>  new_desc_data' + str(new_desc_data) )
    wd_desc.work_api_desc(new_desc_data, q)


def work22(q, topic, translations) -> None:
    # ---
    keys = sorted(translations[topic].keys())
    if "en" in keys:
        keys.append("en-gb")
        keys.append("en-ca")
    # ---
    item_descriptions = wd_bot.Get_item_descriptions_or_labels(q, "descriptions")
    # ---
    if not item_descriptions or not isinstance(item_descriptions, dict):
        item_descriptions = {}
    # ---
    itemdesc_keys = list(item_descriptions.keys())
    # ---
    new_desc_data = {}
    # ---
    for lang in keys:
        if lang not in itemdesc_keys:
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            new_desc_data[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    wd_desc.work_api_desc(new_desc_data, q)


def mainfromQuarry(topic, quarry, translations) -> None:
    # logger.info( '*<<lightyellow>> mainfromQuarry:' )
    # quarry = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q17633526.}'
    json = wd_sparql_bot.sparql_generator_url(quarry)
    lenth = len(json)
    num = 0
    # ---
    for item in json:
        num += 1
        q = "item" in item and item["item"].split("/entity/")[1]
        logger.info(f'<<lightyellow>>*mainfromQuarry: {num}/{lenth} topic:"{topic}", q:"{q}".')
        work22(q, topic, translations)


def Quarry_with_item_langs(p31, quarry, translations) -> None:
    json = wd_sparql_bot.sparql_generator_url(quarry)
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


def mainfromQuarry2(topic, quarry, translations) -> None:
    mainfromQuarry(topic, quarry, translations)


def work2(item, topic, translations) -> None:
    # ---
    keys = sorted(translations[topic].keys())
    if "en" in keys:
        keys.append("en-gb")
        keys.append("en-ca")
    # ---
    new_desc_data = {}
    # ---
    item.get()
    # ---
    q = item.title(as_link=False)
    # ---
    item_descriptions = item.descriptions
    # ---
    for lang in keys:
        if lang not in item_descriptions.keys():
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            # ---
            new_desc_data[lang] = {"language": lang, "value": translations[topic][lang2]}
    # ---
    wd_desc.work_api_desc(new_desc_data, q)

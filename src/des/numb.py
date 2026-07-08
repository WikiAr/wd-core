#!/usr/bin/python3
""" """

import logging

from shared.himo_api import HimoAPIBot
from wd_api import wd_bot, wd_sparql_bot

logger = logging.getLogger(__name__)

WdApiBot = HimoAPIBot(mr_or_bot="bot", www="www")


limit = {1: 0}
quarry = """SELECT (CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
 WHERE {
?item wdt:P31 wd:Q49008.
#FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
FILTER NOT EXISTS {?item schema:description ?ar filter (lang(?ar) = "ar")} .
}
"""
json1 = wd_sparql_bot.sparql_generator_url(quarry)
total = len(json1)
for c, q in enumerate(json1, start=1):
    qid_str = q["q"]
    logger.info(f"work {c} from {total} , {qid_str}")
    descriptions = wd_bot.Get_item_descriptions_or_labels(qid_str, "descriptions")
    if "ar" not in descriptions:
        WdApiBot.des_api(qid_str, "عدد أولي", "ar", ask="")

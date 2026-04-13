#!/usr/bin/python3
"""

python3 core8/pwb.py des/numb

"""

import logging

from bots_subs.hi_api import NewHimoAPIBot
from bots_subs.wd_api import wd_bot

logger = logging.getLogger(__name__)

WD_API_Bot = NewHimoAPIBot(mr_or_bot="bot", www="www")


limit = {1: 0}
quarry = """SELECT (CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
 WHERE {
?item wdt:P31 wd:Q49008.
#FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
FILTER NOT EXISTS {?item schema:description ?ar filter (lang(?ar) = "ar")} .
}
"""
json1 = wd_bot.sparql_generator_url_Z(quarry)
total = len(json1)
for c, q in enumerate(json1, start=1):
    Qid = q["q"]
    logger.info(f"work {c} from {total} , {Qid}")
    descriptions = wd_bot.Get_item_descriptions_or_labels(Qid, "descriptions")
    if "ar" not in descriptions:
        WD_API_Bot.Des_API(Qid, "عدد أولي", "ar", ask="")

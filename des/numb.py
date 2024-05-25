#!/usr/bin/python3
"""

python3 core8/pwb.py des/numb

"""

#
# (C) Ibrahem Qasim, 2022
#
#

from API import printe

# ---
from wd_api import wd_bot

from wd_api import himoAPI

# ---
limit = {1: 0}
quarry = """SELECT (CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
 WHERE {
?item wdt:P31 wd:Q49008.
#FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
FILTER NOT EXISTS {?item schema:description ?ar filter (lang(?ar) = "ar")} .
}
"""
json1 = wd_bot.sparql_generator_url(quarry)
total = len(json1)
for c, q in enumerate(json1, start=1):
    Qid = q["q"]
    printe.output(f"work {c} from {total} , {Qid}")
    descriptions = wd_bot.Get_item_descriptions_or_labels(Qid, "descriptions")
    if "ar" not in descriptions:
        himoAPI.Des_API(Qid, "عدد أولي", "ar", ask="")
# ---

# ---

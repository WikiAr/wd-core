#!/usr/bin/env python3
#
#
"""
جميع الأوصاف

"""

import logging
import random
import sys

import tqdm

from wd_core.des.railway import railway_tables, work_railway
from wd_core.desc_dicts.descraptions import (
    DescraptionsTable,
    Qid_Descraptions,
    Space_Descraptions,
)
from wd_core.wd_api import newdesc, wd_sparql_bot

logger = logging.getLogger(__name__)


DESC_TABLE = {
    "Q318": Space_Descraptions.get("Q318", {}),
    "Q523": Space_Descraptions.get("Q523", {}),
    "Q3863": Space_Descraptions.get("Q3863", {}),
    "Q6243": Space_Descraptions.get("Q6243", {}),
    "Q13632": Space_Descraptions.get("Q13632", {}),
    "Q115518": Space_Descraptions.get("Q115518", {}),
    "Q130019": Space_Descraptions.get("Q130019", {}),
    "Q204194": Space_Descraptions.get("Q204194", {}),
    "Q1153690": Space_Descraptions.get("Q1153690", {}),
    "Q1332364": Space_Descraptions.get("Q1332364", {}),
    "Q1457376": Space_Descraptions.get("Q1457376", {}),
    "Q1931185": Space_Descraptions.get("Q1931185", {}),
    "Q15917122": Space_Descraptions.get("Q15917122", {}),
    "Q67206691": Space_Descraptions.get("Q67206691", {}),
    "Q71963409": Space_Descraptions.get("Q71963409", {}),
    "Q7187": Qid_Descraptions.get("Q7187", {}),
    "Q7889": Qid_Descraptions.get("Q7889", {}),
    "Q8054": Qid_Descraptions.get("Q8054", {}),
    "Q11173": Qid_Descraptions.get("Q11173", {}),
    "Q21199": Qid_Descraptions.get("Q21199", {}),
    "Q24856": Qid_Descraptions.get("Q24856", {}),
    # 'Q101352' : Qid_Descraptions.get('Q101352', {}), # family name
    "Q3409032": Qid_Descraptions.get("Q3409032", {}),
    "Q4167410": Qid_Descraptions.get("Q4167410", {}),
    "Q4167836": Qid_Descraptions.get("Q4167836", {}),
    "Q4502142": Qid_Descraptions.get("Q4502142", {}),
    "Q6979593": Qid_Descraptions.get("Q6979593", {}),
    "Q10870555": Qid_Descraptions.get("Q10870555", {}),
    "Q11266439": Qid_Descraptions.get("Q11266439", {}),
    "Q13100073": Qid_Descraptions.get("Q13100073", {}),
    "Q13406463": Qid_Descraptions.get("Q13406463", {}),
    "Q17633526": Qid_Descraptions.get("Q17633526", {}),
    "Q19389637": Qid_Descraptions.get("Q19389637", {}),
    "Q11753321": DescraptionsTable.get("Wikimedia template", {}),
    "Q15145755": DescraptionsTable.get("Wikimedia module", {}),  # Module test cases
    "Q18711811": DescraptionsTable.get("Wikimedia module", {}),  # map data module
    "Q24046192": DescraptionsTable.get("Wikimedia category", {}),
    # 'Q8502' : PLACES_TABLE.get('Q8502', {}),     # جبل
    # 'Q39614' : PLACES_TABLE.get('Q39614', {}),   # مقبرة
    # 'Q79007' : PLACES_TABLE.get('Q79007', {}),   # شارع
}

DESC_TABLE["Q726242"] = {"ar": "نجم"}
DESC_TABLE["Q2247863"] = {"ar": "نجم"}
DESC_TABLE["Q66619666"] = {"ar": "نجم"}
DESC_TABLE["Q72803622"] = {"ar": "نجم"}

for x, dd in railway_tables.items():
    DESC_TABLE[x] = dd

for x in DESC_TABLE:
    if x in sys.argv:
        DESC_TABLE = {x: DESC_TABLE[x]}
        break

temp_table = {}

if len(DESC_TABLE) > 1:
    # chose randomly 5 of the DESC_TABLE
    # ---
    liste = list(DESC_TABLE.keys())
    # ---
    list2 = random.sample(liste, 10)
    # ---
    print(list2)
    # ---
    random.shuffle(list2)
    # ---
    for x in list2:
        temp_table[x] = DESC_TABLE[x]
    # ---
    DESC_TABLE = temp_table

quarry_o = """
    SELECT DISTINCT ?item ?langs
    WITH { SELECT ?item WHERE {
        ?item wdt:P31 wd:Q1457376 } ORDER BY DESC(xsd:integer(SUBSTR(STR(?item),33))) limit 1000
        } AS %a
    WITH { SELECT ?item (COUNT(?l) as ?ls) (GROUP_CONCAT(DISTINCT(lang(?l)); separator=",") as ?langs) WHERE {
        INCLUDE %a.
        ?item schema:description ?l } GROUP BY ?item HAVING( ?ls < 10)
        } as %b
    WHERE {
        INCLUDE %b
    }
    ORDER BY DESC(xsd:integer(SUBSTR(STR(?item),33)))
"""

quarry_list = [
    quarry_o,
    quarry_o.replace("limit 1000", "limit 1000 offset 1000"),
    quarry_o.replace("limit 1000", "limit 1000 offset 2000"),
    quarry_o.replace("limit 1000", "limit 1000 offset 3000"),
    quarry_o.replace("limit 1000", "limit 1000 offset 4000"),
    quarry_o.replace("limit 1000", "limit 1000 offset 5000"),
]

qlist_done = []


def work_one_json(json1, topic_ar, p31, p31_langs) -> None:
    # ---
    json_lenth = len(json1)
    # ---
    for num, item in tqdm.tqdm(enumerate(json1, start=1)):
        num += 1
        q = "item" in item and item["item"].split("/entity/")[1]
        # ---
        q_langs = item.get("langs", "").split(",")
        # ---
        lang_to_add = list(set(p31_langs) - set(q_langs))
        # ---
        tp = f'<<lightyellow>>*mainfromQuarry: {num} from {json_lenth} p31:"{p31}", qid:"{q}":<<lightblue>>{topic_ar}'
        # ---
        if not lang_to_add:
            logger.info(tp)
            continue
        # ---
        if num % 50 == 0:
            logger.info(tp)
        # ---
        if p31 in railway_tables:
            work_railway({}, p31, q=q)
        # elif p31 in PLACES_TABLE:
        # work_railway( {}, p31, q=q )
        else:
            newdesc.work22(q, p31, DESC_TABLE)


def work_one_quarry(quarry, p31, p31_desc):
    json1 = wd_sparql_bot.sparql_generator_url(quarry)
    # ---
    quarry_result_lenth = len(json1)
    # ---
    topic_ar = p31_desc.get("ar") or p31_desc.get("en") or ""
    # ---
    p31_langs = list(p31_desc.keys())
    # ---
    work_one_json(json1, topic_ar, p31, p31_langs)
    # ---
    return quarry_result_lenth


def main() -> None:
    # lenth of DESC_TABLE and quarry_list
    all_lenth = len(quarry_list) * len(DESC_TABLE)
    # ---
    numb = 0
    # ---
    for p31, p31_desc in DESC_TABLE.items():
        # ---
        quarry_result_lenth = 0
        # ---
        random.shuffle(quarry_list)
        # ---
        for qu_numb, quarry in enumerate(quarry_list):
            # ---
            if quarry_result_lenth == 0 and qu_numb > 1:
                logger.info("<<lightred>> len of first quarry == 0 continue")
                continue
            # ---
            numb += 1
            # ---
            logger.info(f"work in {numb} from {all_lenth} querirs")
            # ---
            quarry = quarry.replace("wd:Q1457376", f"wd:{p31}")
            # ---
            if qu_numb == 1:
                logger.info("<<lightred>> first quarry")
                logger.info(quarry)
            # ---
            quarry_result_lenth = work_one_quarry(quarry, p31, p31_desc)


if __name__ == "__main__":
    main()

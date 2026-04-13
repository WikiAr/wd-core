#!/usr/bin/python3
"""

إضافة تسميات عناصر تصنيفات في ويكي بيانات

نسخ تسمية العنصر إلى التصنيف المطابق له في الإسم

python3 core8/pwb.py alabel/labels -limit:20

"""

import logging
import sys

from bots_subs.hi_api import NewHimoAPIBot

from bots_subs import wiki_sql

WD_API_Bot = NewHimoAPIBot(mr_or_bot="mr", www="www")

logger = logging.getLogger(__name__)


Limit = {1: ""}


# result = wiki_sql.sql_new(qua, wiki="")

# TODO: Table 'wikidatawiki_p.wbt_item_terms' doesn't exist

Quaa = """#USE wikidatawiki_p;
SELECT
    CONCAT("Q", ips_item_id) as qid,
    ips_site_page as page
FROM
    wb_items_per_site
WHERE
    ips_site_id = 'arwiki'
AND NOT EXISTS (
    SELECT
        wbit_item_id
    FROM
        wbt_item_terms
        INNER JOIN wbt_term_in_lang ON wbtl_id = wbit_term_in_lang_id
        INNER JOIN wbt_text_in_lang ON wbxl_id = wbtl_text_in_lang_id
    WHERE
        wbit_item_id = ips_item_id
        AND wbxl_language = "ar"
        AND wbtl_type_id = 1
    )
"""

for arg in sys.argv:
    arg, _, value = arg.partition(":")
    # ---
    if arg in ["-limit", "limit"]:
        Limit[1] = value
        logger.info(f"<<lightred>> Limit = {value}.")

if Limit[1]:
    Quaa += f"limit {Limit[1]}"


def main():
    # python3 core8/pwb.py alabel/labels -limit:20
    # ---
    logger.info(Quaa)
    # ---
    try:
        result = wiki_sql.sql_new(Quaa, wiki="wikidata")
    except Exception as e:
        print(f"Exception: {e}")
        return
    # ---
    len_result = len(result)
    # ---
    for num, item in enumerate(result, start=1):
        qid = item["qid"]
        page = item["page"]
        # ---
        if isinstance(qid, bytes):
            logger.info("type(qid) == bytes")
            qid = qid.decode("utf-8")
        if isinstance(page, bytes):
            logger.info("type(page) == bytes")
            page = page.decode("utf-8")
        # ---
        logger.info(f'<<lightgreen>> {num}/{len_result} qid:"{qid}", page:"{page}"')
        # ---
        if page:
            WD_API_Bot.Add_Labels_if_not_there(qid, page, "ar", False)

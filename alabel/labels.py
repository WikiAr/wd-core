#!/usr/bin/python3
"""

إضافة تسميات عناصر تصنيفات في ويكي بيانات

نسخ تسمية العنصر إلى التصنيف المطابق له في الإسم

python3 core8/pwb.py alabel/labels -limit:20

"""

import sys

# ---
from newapi import printe
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="mr", www="www")
# ---
from api_sql import wiki_sql

# ---
Limit = {1: ""}
# ---

# ---
# result = wiki_sql.sql_new(qua, wiki="", printqua=False)
# ---
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
# ---
for arg in sys.argv:
    arg, _, value = arg.partition(":")
    # ---
    if arg in ["-limit", "limit"]:
        Limit[1] = value
        printe.output(f"<<lightred>> Limit = {value}.")
# ---
if Limit[1]:
    Quaa += f"limit {Limit[1]}"


def main():
    # python3 core8/pwb.py alabel/labels -limit:20
    # ---
    result = wiki_sql.sql_new(Quaa, wiki="wikidata", printqua=True)
    # ---
    len_result = len(result)
    # ---
    for num, item in enumerate(result, start=1):
        qid = item["qid"]
        page = item["page"]
        # ---
        if isinstance(qid, bytes):
            printe.output("type(qid) == bytes")
            qid = qid.decode("utf-8")
        if isinstance(page, bytes):
            printe.output("type(page) == bytes")
            page = page.decode("utf-8")
        # ---
        printe.output(f'<<lightgreen>> {num}/{len_result} qid:"{qid}", page:"{page}"')
        # ---
        if page:
            # WD_API_Bot.Labels_API(qid, page, "ar", False, Or_Alii=True)
            WD_API_Bot.Add_Labels_if_not_there(qid, page, "ar", False)


if __name__ == "__main__":
    if "test" in sys.argv:
        WD_API_Bot.Add_Labels_if_not_there("Q109927", "83 Beatrix", "ar", False)
    else:
        main()

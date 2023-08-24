#!/usr/bin/python
"""

إضافة تسميات عناصر تصنيفات في ويكي بيانات

نسخ تسمية العنصر إلى التصنيف المطابق له في الإسم

python3 ./core8/pwb.py alabel/labels -limit:20

"""
#
# (C) Ibrahem Qasim, 2023
#
#
import re
import time
import pywikibot
import sys
# ---
from API import printe
from wd_API import himoAPI_test as himoAPI
# ---
Limit = {1: ''}
# ---
from api_sql import wiki_sql
# ---
# result = wiki_sql.sql_new(qua, wiki="", printqua=False)
# ---
Quaa = '''#USE wikidatawiki_p;
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
'''
# ---
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    # ---
    if arg == '-limit' or arg == 'limit':
        Limit[1] = value
        printe.output(f'<<lightred>> Limit = {value}.')
# ---
if Limit[1] != '':
    Quaa = Quaa + f'limit {Limit[1]}'
# ---


def main():
    # python3 ./core8/pwb.py alabel/labels -limit:20
    # ---
    result = wiki_sql.sql_new(Quaa, wiki="wikidata", printqua=True)
    # ---
    len_result = len(result)
    # ---
    num = 0
    # ---
    for item in result:
        qid = item['qid']
        page = item['page']
        # ---
        if type(qid) == bytes:
            printe.output('type(qid) == bytes')
            qid = qid.decode("utf-8")
        if type(page) == bytes:
            printe.output('type(page) == bytes')
            page = page.decode("utf-8")
        # ---
        num += 1
        # ---
        printe.output(f'<<lightgreen>> {num}/{len_result} qid:"{qid}", page:"{page}"')
        # ---
        if page != "":
            himoAPI.Labels_API(qid, page, "ar", False, Or_Alii=True)


# ---
if __name__ == "__main__":
    main()
# ---

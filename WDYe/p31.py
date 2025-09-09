#!/usr/bin/python3
"""
# لا يعمل
إضافة خاصية P31 للتصنيفات

python pwb.py c30/p31
python pwb.py c30/p31 enwiki

"""
#
# (C) Ibrahem Qasim, 2022
#
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="bot", www="www")
# ---
import pywikibot

# ---
import sys

# ---
from api_sql import sql as c18sql

# ---
# use arwiki_p;
mainquarry = '''
SELECT p.page_title,
       pp_value
FROM page AS p,
     page_props AS pp,
     wikidatawiki_p.page AS wdp
WHERE p.page_namespace = 14
/*and NOT EXISTS
        (SELECT *
         FROM wikidatawiki_p.pagelinks wdpl
         WHERE wdpl.pl_from = wdp.page_id
             AND wdpl.pl_title = 'P31'
             */
    AND p.page_id not in
        (SELECT tl_from
         FROM templatelinks,
              linktarget
         WHERE lt_namespace = 10
             AND tl_target_id = lt_id
             AND lt_title = "تحويل_تصنيف" )
    AND p.page_is_redirect = 0
    AND pp_page = p.page_id
    AND pp_propname = 'wikibase_item'
    AND wdp.page_title = pp_value
    AND wdp.page_namespace = 0
    AND wdp.page_id not in
        (SELECT wdpl.pl_from
         FROM wikidatawiki_p.pagelinks wdpl
         WHERE wdpl.pl_title = 'P31'
             AND wdpl.pl_from = wdp.page_id)
    AND wdp.page_is_redirect = 0
GROUP BY p.page_title #order BY ll_from
#LIMIT 2000;
'''
# ---
# ---
WIKI = {1: "arwiki"}
AutoSave = {1: False}


def treat_page(qid):
    WD_API_Bot.Claim_API2(qid, "P31", "Q4167836")


def main2(*args):
    # ---
    quarry = mainquarry
    result = []
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(':')
        # ---
        if arg == 'limit':
            quarry = f"{quarry}\n LIMIT {value};"
        # ---
        if arg == 'enwiki':
            WIKI[1] = "enwiki"
    # ---
    pywikibot.output(quarry)
    result = c18sql.Make_sql_2_rows(quarry, wiki=WIKI[1])
    pywikibot.output("===============================")
    for counter, title in enumerate(result, start=1):
        pywikibot.output(f" <<lightblue>> page: {counter}/{len(result)} : {title}:{result[title]} ")
        treat_page(result[title])


# ---
if __name__ == '__main__':
    main2()
# ---

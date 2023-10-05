#!/usr/bin/python
"""

إضافة خاصية P31 للتصنيفات

python pwb.py c30/p31
python pwb.py c30/p31 enwiki

"""
#
# (C) Ibrahem Qasim, 2022
#
from wd_API import himoAPI
import pywikibot

# ---
import sys
# ---
from api_sql import sql as c18sql
# ---
# use arwiki_p;
mainquarry = '''
select p.page_title , pp_value
FROM page as p, page_props as pp, wikidatawiki_p.page as wdp
WHERE p.page_namespace = 14
#and not exists (select * from wikidatawiki_p.pagelinks wdpl where wdpl.pl_from = wdp.page_id  AND wdpl.pl_title = 'P31' )
and p.page_id not in (select tl_from from templatelinks, linktarget where lt_namespace = 10 and tl_target_id = lt_id and lt_title = "تحويل_تصنيف" )

and p.page_is_redirect = 0
AND pp_page = p.page_id AND pp_propname = 'wikibase_item' AND wdp.page_title = pp_value AND wdp.page_namespace = 0
and wdp.page_id not in (select wdpl.pl_from from wikidatawiki_p.pagelinks wdpl where wdpl.pl_title = 'P31' and wdpl.pl_from = wdp.page_id)
AND wdp.page_is_redirect = 0
GROUP BY p.page_title
#order by ll_from
#LIMIT 2000;'''
# ---
# ---
WIKI = {1: "arwiki"}
AutoSave = {1: False}
# ---


def treat_page(qid):
    himoAPI.Claim_API2(qid, "P31", "Q4167836")
# ---


def main2(*args):
    # ---
    quarry = mainquarry
    result = []
    # ---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        # ---
        if arg == 'limit':
            quarry = quarry + f"\n LIMIT {value};"
    # ---
        if arg == 'enwiki':
            WIKI[1] = "enwiki"
    # ---
    pywikibot.output(quarry)
    result = c18sql.Make_sql_2_rows(quarry, wiki=WIKI[1])
    pywikibot.output("===============================")
    # ---
    counter = 0
    for title in result:
        counter += 1
        pywikibot.output(" <<lightblue>> page: %d/%d : %s:%s " %
                         (counter, len(result), title, result[title]))
        treat_page(result[title])


# ---
if __name__ == '__main__':
    main2()
# ---

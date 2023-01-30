#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة خاصية P31 للتصنيفات

python pwb.py c30/p31
python pwb.py c30/p31 enwiki

"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
import pywikibot
import codecs
import re
import string
#---
import sys
#---
from API import sql as c18sql
#---
#use arwiki_p;
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
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.page_put(NewText , summary , title)

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, lab , lang , False, Or_Alii = False, change_des = False)
#himoAPI.Alias_API( Qid, [Alias] , lang , False)
#himoAPI.Merge( q1, q2)
#himoAPI.wbcreateredirect( From, To)
#himoAPI.Sitelink_API( Qid, title , wiki )
#himoAPI.Remove_Sitelink( Qid , wiki )
#himoAPI.Add_Labels_if_not_there( Qid, label , lang , ASK = "")
#---
WIKI = { 1 : "arwiki" }
AutoSave = { 1: False}
#---
def treat_page( qid ):
    himoAPI.Claim_API2( qid , "P31" , "Q4167836")
#---
def main2(*args):
    #---
    quarry = mainquarry
    result = []
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg =='limit':
            quarry = quarry + "\n LIMIT %s;" % value
    #---
        if arg == 'enwiki':
            WIKI[1] = "enwiki"
    #---
    pywikibot.output( quarry )
    result = c18sql.Make_sql_2_rows( quarry , wiki = WIKI[1] )
    pywikibot.output( "===============================" )
    #---
    counter = 0
    for title in result:
        counter += 1
        pywikibot.output( " <<lightblue>> page: %d/%d : %s:%s "  %  ( counter , len(result) , title , result[title] ) )
        treat_page( result[title] )
#---
if __name__ == '__main__':
    main2()
#---
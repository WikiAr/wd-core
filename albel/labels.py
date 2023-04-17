#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة تسميات عناصر تصنيفات في ويكي بيانات

نسخ تسمية العنصر إلى التصنيف المطابق له في الإسم


"""
#
# (C) Ibrahem Qasim, 2022
#
#


import re
import time
import pywikibot
#---
import sys
#---
import urllib
import urllib.parse
from api_sql import sql
from wd_API import himoAPI_test as himoAPI
#---
Limit = { 1: '' }
#---
def main():
    #python3 pwb.py wd/labels limit:20
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'always' or arg == 'save':
            SaveR[1] = True
            pywikibot.output('<<lightred>> SaveR = True.')
        #---
        if arg == '-limit' or arg == 'limit':
            Limit[1] = value
            pywikibot.output('<<lightred>> Limit = %s.' % value )
        #---#
    Quaa = '''#USE wikidatawiki_p;
SELECT
  CONCAT("Q", ips_item_id),
  ips_site_page
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
    #---
    if Limit[1] != '' :
        Quaa = Quaa + 'limit %s' % Limit[1]
    #---
    pywikibot.output( Quaa )
    sparql = sql.Make_sql_2_rows( Quaa , wiki = "wikidata" )
    #---
    Table = {}
    for item in sparql:
        Table[item] = sparql[item]
    #---
    num = 0
    for item in Table:
        num += 1
        pywikibot.output( '<<lightgreen>> %d/%d item:"%s" ' % (num ,len(Table.keys() ),item) )
        if Table[item] != "" : 
            himoAPI.Labels_API( item, Table[item] , "ar" , False, Or_Alii = True)
    #---
if __name__ == "__main__":
    main()
#---

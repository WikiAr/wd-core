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
import urllib.request
import urllib.parse

#---
from API import himoBOT2
#---
from wd_API import himoAPI_test as himoAPI
#---
Limit = { 1: "500"}
#---
def main():
    #python pwb.py wd/category
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'always':
            SaveR[1] = True
            pywikibot.output('<<lightred>> SaveR = True.')
        #---
        if arg == '-limit' or arg == 'limit':
            Limit[1] = value
            pywikibot.output('<<lightred>> Limit = %s.' % value )
        #---#
    Quaa = '''
SELECT DISTINCT 
?cat
(concat("" , str(?item_ar) , ''  )  as ?ar_name)
WHERE {
  #?item wdt:P31* wd:Q18608583.
  #?item wdt:P31* wd:Q18608583.
  #?item wdt:P31* wd:Q27020041.
 { ?cat wdt:P301 ?item. } UNION {  ?item wdt:P910 ?cat. }
 # ?item wdt:P31 wd:Q51031626.
 # ?item wdt:P910 ?cat.
   FILTER NOT EXISTS {?cat rdfs:label ?catar filter (lang(?catar) = "ar")} .
   ?item rdfs:label ?item_ar filter (lang(?item_ar) = "ar") .
   ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .
   ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .
   BIND( concat("Category:" , str(?item_en)) as ?change_name)
  
  FILTER ( str(?cat_en) = str(?change_name) )
}
LIMIT '''
    Quaa = Quaa + Limit[1]
    pywikibot.output( Quaa )
    sparql = himoBOT2.sparql_generator_url(Quaa)
    #---
    Table = {}
    for item in sparql:
        q = item['cat'].split("/entity/")[1]
        Table[q] = item["ar_name"]
    #---
    num = 0
    for item in Table:
        num += 1
        #if num < 2:
        pywikibot.output( '<<lightgreen>> %d/%d item:"%s" ' % (num ,len(Table.keys() ),item) )
        #pywikibot.output( Table[item] )
        if Table[item] != "" : 
            lab = 'تصنيف:' + Table[item]
            himoAPI.Labels_API( item, lab , "ar" , False, Or_Alii = True)
    #---
if __name__ == "__main__":
    main()
#---

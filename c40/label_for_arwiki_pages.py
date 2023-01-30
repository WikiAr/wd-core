#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت اضافة التسميات في ويكي بيانات
لصفحات ويكيبيديا العربية

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
from pywikibot import pagegenerators
from pywikibot import pagegenerators as pg
import re
import codecs
import sys
import datetime
from datetime import datetime, date, time

def action_one_item2(wditem):
    if ('ar' in wditem.labels): #وصف انجليزي متوفر في ويكي بيانات
        pywikibot.output( ' تسمية عربية متوفرة: %s ' % wditem.labels['ar'])
        pass
    else:
        if ('arwiki' in wditem.sitelinks):
            ma = wditem.sitelinks['arwiki']
            s = ('Bot: Add Arabic label "%s"' % ma)
            pywikibot.output(s)
            arlab = { 'ar': ma }
            try:
                item.editLabels(labels=arlab, summary=s)
            except:
                pass
    
def wd_sparql_generator(query):     
  wikidatasite=pywikibot.Site('wikidata','wikidata') 
  generator=pg.WikidataSPARQLPageGenerator(query, site=wikidatasite)
  for wd in generator:
    wd.get(get_redirect=True)
    yield wd

def main():
    itemsdone = 0
    pywikibot.output ("- بدء المهمة")
    
    query = """select distinct ?item ?LabelAR ?page_titleAR where {
    ?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ;  schema:name ?page_titleAR .
    FILTER(NOT EXISTS { ?item rdfs:label ?LabelAR filter (lang(?LabelAR) = "ar") .})
    } LIMIT 5"""
	
    pywikibot.output ("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        itemsdone += 1
        action_one_item2(wditem)
        #pywikibot.output('%s pass' % (wditem)
		
    pywikibot.output('Items done: %s' % itemsdone)
    
if __name__ == "__main__":  
    main()

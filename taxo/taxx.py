#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف للكائنات بناءاً على استعلام جديد


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
import pywikibot.data.wikidataquery as wdquery
import codecs #used in logfiles, unicoded strings
import datetime
import json
#---
import sys
#---
import urllib

import urllib
import urllib.request
import urllib.parse
#---
# start of himoBOT.py file
from API import himoBOT
#---
"""
# استعلام عن الكائنات بمرتبة تصنيفية طائفة
SELECT ?item ?itemar ?itemen WHERE {
  ?item wdt:P31 wd:Q16521. ?item wdt:P105 wd:Q37517.
  { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar")  }
  { ?item rdfs:label ?itemen. FILTER((LANG(?itemen)) = "en")  } 
} #LIMIT 100"""
#---
from all_new_taxo import *
from API.descraptions import DescraptionsTable
My_Des = {}
for description in DescraptionsTable.keys():
    My_Des[description.lower()] = DescraptionsTable[description]
#---
# start of newdesc.py file
from API import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
def main(arabic):
    translations  = {}
    num = 0
    for gen in gens.keys():
        for type in arabic.keys():
            num += 1
            topic = gen + ' ' + type
            pywikibot.output( 'topic "%s":' % topic )
            translations[topic] = {}
            #---
            for lang in arabic[type].keys():
            #for lang in arabic[type]:
                if (lang in gens[gen]) and (lang in arabic[type]):
                    translations[topic][lang] = gens[gen][lang] + ' ' + arabic[type][lang].lower()
                else:
                    pywikibot.output( 'lang "%s" not in "%s"' % (  lang , gen ) )
            #---
            topic2 = translations[topic]['en'].lower()
            if topic2 in My_Des:
                for lang in My_Des[topic2]:
                    if not lang in translations[topic]:
                        translations[topic][lang] = My_Des[topic2][lang]
            #---
            tao = topic
            if 'ar' in translations[topic]:
                tao = translations[topic]['ar']
            if 'en' in translations[topic]:
                tao = tao + '|' + translations[topic]['en']
            #---
            lenth =  len(gens) *  len(arabic)
            pywikibot.output( '*<<lightred>> a > : %d/%d %s:' % (  num , lenth , tao ) )
            #---
            for lang in translations[topic].keys():
                #---
                qua ='SELECT ?item WHERE { ?item wdt:P31 wd:Q16521. '
                qua = qua + ( '?item wdt:P171* wd:%s.' %  type )
                qua = qua + ( '?item wdt:P105  wd:%s.' %  gen )
                qua = qua + ('\nFILTER NOT EXISTS  {?item schema:description ?des. FILTER((LANG(?des)) = "%s") .} }' % lang )
                #---
                #pywikibot.output(qua)
                newdesc.mainfromQuarry2( topic , qua, translations)
#---
debugedo=False       
if __name__ == "__main__":  
    if debugedo:
        pywikibot.output("debug is on")
        Q = 'novel'  
        #for lang in language:
        #pywikibot.output( 'lang: "%s" with value: ' % 'fr' )
    else:
        main(arabic)
        #GetQuery('Q49084' , 'fr' )
#---
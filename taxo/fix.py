#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#

#---
# start of newdesc.py file
# from API import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
#
import re
import time
import codecs
import pywikibot
import json
#import sys
from pywikibot import pagegenerators as pg
import unicodedata
#import urllib
#import urllib.request
#import urllib.parse
import unicodedata
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse

#---
from API import himoBOT
#---
wikidatasite = pywikibot.Site('wikidata', 'wikidata')
repo = wikidatasite.data_repository()
#---
translations = {}
translations['Q28319'] = {    #   
        "ar": "نوع من حرشفيات الأجنحة"
        #, "en": "of lepidoptera"
        , "it": "specie di coleotteri"
        }
#---
replacement = {}
replacement["it"] = {"specie di coleottero" : translations['Q28319']["it"] }
replacement["ar"] = {"نوع من الحشرات" : translations['Q28319']["ar"]  }
#---
def work2(item , topic):
    item.get()
    #OOutPut( '<<lightyellow>> **newdesc: work2:'  + item.title(as_link=False))
    #ItemDescriptions = {}
    #---
    keys = [x for x in translations[topic].keys()]
    #---
    ItemDescriptions = item.descriptions
    NewDesc = {}
    addedlangs = []
    replacelang = []
    q = item.title(as_link=False)
    #---
    for lang in ItemDescriptions.keys():        # استبدال 
        if lang in replacement.keys():
            value = ItemDescriptions[lang]#['value']
            if 'value' in ItemDescriptions[lang]:
                value = ItemDescriptions[lang]['value']
            #---
            if value in replacement[lang]:
                NewDesc[lang] = {"language":lang,"value":replacement[lang][value]}
                #pywikibot.output( '<<lightyellow>>  replace "%s" by: "%s".' % ( value , replacement[lang][value]) )
                replacelang.append(lang)
    #---
    for lang in keys:
        if not lang in ItemDescriptions.keys():
            NewDesc[lang] = {"language":lang,"value":translations[topic][lang]}
            addedlangs.append(lang)
    #---
    #OOutPut( '<<lightyellow>>  NewDesc' + str(NewDesc) )

    himoBOT.work_api_desc_with_fix( NewDesc , q)
#---
def mainfromQuarry():
    pywikibot.output( '*<<lightyellow>> mainfromQuarry:' )
    Quarry ='''SELECT ?item
WHERE
{
  ?item schema:description "specie di coleottero"@it.
  ?item wdt:P171* wd:Q28319 .
  ?item wdt:P105 wd:Q7432.
}
#LIMIT 100'''
    json = himoBOT.wd_sparql_generator_url(Quarry)
    lenth = len(json)
    num = 0
    topic = 'Q28319'
    #---
    for item in json:
        num += 1
        q = item.title(as_link=False)
        pywikibot.output( '<<lightyellow>>*mainfromQuarry: %d/%d topic:"%s" , q:"%s".'  % (num , lenth , topic, q))
        work2(item , topic)
#---
if __name__ == "__main__":
    mainfromQuarry()
#---
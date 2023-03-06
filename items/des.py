#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
'''

إزالة أوصاف خاطئة

'''
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
from API import himoAPI
#---
wikidatasite = pywikibot.Site('wikidata', 'wikidata')
repo = wikidatasite.data_repository()
#---
from Contries import ContriesTable
replacementkkr = ['في ' + ContriesTable[x]['ar'] for x in ContriesTable]
replacementkk = ['in ' + ContriesTable[x]['en'] for x in ContriesTable]
#---
def MakeStr(type , NewDesc):
    value = 'value'
    language = 'language'
    #---
    if type == 'sitelinks':
        language = 'site'
        value = 'title'
    #---
    Newline = ''
    for la in NewDesc:
        test = re.sub( '\'' , '' , NewDesc[la][value])
        #sa = "'" + la + "': " + "{'value': '" + NewDesc[la]['value'] + "', 'language': '" + la + "'},"
        #---
        if test != NewDesc[la][value]:
            sa = '"' + la + '": ' + '{"' + value + '": "' + NewDesc[la][value] + '", "' + language + '": "' + la + '"},'
        else:
            sa = "'" + la + "': " + "{'" + value + "': '" + NewDesc[la][value] + "', '" + language + "': '" + la + "'},"
        #---

        Newline = Newline + sa
    data3 = "'" + type + "' :{ " + Newline + "} , "
    return data3
#---
def work2(item , topic):
    item.get()
    #OOutPut( '<<lightyellow>> **newdesc: work2:'  + item.title(as_link=False))
    NewDesc = {}
    NewDesc = {}
    addedlangs = []
    q = item.title(as_link=False)
    pywikibot.output(item.descriptions)
    for lang in item.descriptions.keys():        # استبدال 
        value = item.descriptions[lang]
        if value in replacementkk or value in replacementkkr:
            NewDesc[lang] = {"language":lang,"value":''}
            pywikibot.output( '<<lightyellow>> remove "%s".'  % value)
            addedlangs.append(lang)
    #pywikibot.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )
    
    ds = '{' + MakeStr('descriptions' , NewDesc) + '}'
    himoAPI.New_Mult_Des_2(q, ds, 'Bot: remove wrong descriptions.' , False)
#---

def main():
    loo = [ 'in India', 'in Ivory Coast']
    Quarry = '''SELECT ?item
    WHERE {
      ?item schema:description ?itemDescription .
      ?item schema:description "in India"@en.
      SERVICE wikibase:label { bd:serviceParam wikibase:language "en" } 
      }
    limit 100'''
    for lo in replacementkk:
        Quarry = re.sub( 'in India' , lo , Quarry)
        json = himoBOT.wd_sparql_generator_url(Quarry)
        lenth = len(json)
        num = 0
        #topic = 'Wikinews article'
        #---
        for item in json:
            num += 1
            q = item.title(as_link=False)
            pywikibot.output( '<<lightyellow>>*mainfromQuarry: %d/%d topic:"%s" , q:"%s".'  % (num , lenth , lo, q))
            work2(item , lo)
if __name__ == "__main__":
    main()
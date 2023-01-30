#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إيجاد تسمية عربية من خلال قوالب 
geobox

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import codecs
import re
#---
import string
import pywikibot
#---
import sys
#---
import urllib.request
import urllib.parse

#---
from datetime import datetime, date, time
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")

s = '''SELECT (concat(strafter(str(?ss),"/entity/"))  as ?item)#?item
    ?itemabel ?page
    WHERE {
    SERVICE wikibase:mwapi {
    bd:serviceParam wikibase:api "Generator" .
    bd:serviceParam wikibase:endpoint "ar.wikipedia.org" .
    bd:serviceParam mwapi:gcmtitle "تصنيف:عزل محافظة إب" .
    bd:serviceParam mwapi:generator "categorymembers" .
    bd:serviceParam mwapi:gcmprop "ids|title|type" .
    bd:serviceParam mwapi:gcmlimit "max" .
    ?page wikibase:apiOutput mwapi:title  .
    ?ns wikibase:apiOutput "@ns" .
    ?ss wikibase:apiOutputItem mwapi:item .
    }
    OPTIONAL {?ss rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .
    FILTER NOT EXISTS {?ss wdt:P31 wd:Q6617100.} .
    FILTER (?ns = "0")
    FILTER NOT EXISTS {?article schema:about ?ss ;schema:isPartOf <https://ceb.wikipedia.org/> .} .} #'''
s = s + str(menet)
#---
def path():
    #---
    so = urllib.parse.quote(s) #, safe='')
    pywikibot.output('urllib.parse.quote')
    pywikibot.output(so)
#---
def quotequote():
    #---
    so = urllib.parse.quote(s)
    pywikibot.output('urllib.parse.quote')
    pywikibot.output(so)
#---
def main():
    try:
        path()
    except:
        quotequote()
#---   
if __name__ == '__main__':
     main()
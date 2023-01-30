#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت استعلام سباركل والكتابة على صفحة مستخدم

python pwb.py himos

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import json
import pywikibot
import codecs
import urllib
from pywikibot import pagegenerators as pg

#---
import sys
#---
import urllib.request
import urllib.parse

#--- 
wikidatasite = pywikibot.Site('wikidata','wikidata') 
repo = wikidatasite.data_repository()

def GGG():
    table = []
    query = '''SELECT DISTINCT 
	?item
	WHERE {
	  BIND("species of insect"@en AS ?year)
	  ?item schema:description ?year.
	  OPTIONAL {
		?item schema:description ?itemabel.
		FILTER((LANG(?itemabel)) = "ar")
	  }
	  
	}
	LIMIT 100'''
    generator = pg.WikidataSPARQLPageGenerator(query,site=wikidatasite)
    for wd in generator:
        wd.get(get_redirect=True)
        #table.append(wd)
        yield wd
    #return table
def main():
    generator = GGG()
    for item in generator:
        print( item.title() )
    
#---
     
if __name__ == "__main__":
    main()

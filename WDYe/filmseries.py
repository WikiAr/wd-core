#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#
#site = pywikibot.Site('wikidata', 'wikidata')
#repo = site.data_repository()

#---
# start of newdesc.py file
from API import newdesc
#   newdesc.main_from_file(file , topic , translations2)
#   newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
from API.descraptions import DescraptionsTable

translations = {}
translations['film series'] = DescraptionsTable['film series']

#---
quarry = 'SELECT ?item  WHERE { ?item wdt:P31 wd:Q24856 \nFILTER NOT EXISTS { ?item schema:description ?des. filter (lang(?des) = "ar")} .}'
topic = 'film series'
#---
newdesc.mainfromQuarry2( topic, quarry, translations)
#---
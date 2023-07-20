#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#
# ---
# start of newdesc.py file
import pywikibot
# ---
# start of newdesc.py file
from wd_API import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
# ---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions
# ---
translations = {}
translations["Q11173"] = Qid_Descraptions['Q11173']
# ---
for p31 in translations:
    en_desc = translations[p31]["en"]
    quarry = '''SELECT DISTINCT ?item (GROUP_CONCAT(DISTINCT(?desc); separator=",") as ?langs) 
    WHERE { 
      SELECT ?item ?desc
    WHERE {  
      ?item wdt:P31 wd:%s. 
      ?item schema:description ?itemDes . 
      ?item schema:description "%s"@en 
      BIND(lang(?itemDes) AS ?desc)
          }
    limit 1000000
          }
    GROUP BY ?item
    limit 30000''' % (p31, en_desc)
    # ---
    newdesc.Quarry_with_item_langs(p31, quarry, translations)
    # newdesc.mainfromQuarry2( p31, quarry, translations)
# ---

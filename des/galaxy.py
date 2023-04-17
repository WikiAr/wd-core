#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#
'''


python pwb.py des/galaxy

'''
#---
# start of newdesc.py file
from wd_API import newdesc
from likeapi.descraptions import DescraptionsTable, Qid_Descraptions
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
translations = {
    "Q318" : DescraptionsTable.get('galaxy') or Qid_Descraptions.get('Q318') or {}
    }
#---
for q in translations:
    quarry = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s.} limit 50000' % q
    newdesc.mainfromQuarry2( q, quarry, translations )
#---
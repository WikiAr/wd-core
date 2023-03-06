#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python3 pwb.py des/numb

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
import codecs
import re

from API import printe
import sys
import time
#---
from API import himoBOT
from API import himoBOT2
from API import himoAPI
#---
limit = { 1 : 0 }
quarry = '''SELECT (CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
 WHERE {
?item wdt:P31 wd:Q49008.
#FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
FILTER NOT EXISTS {?item schema:description ?ar filter (lang(?ar) = "ar")} .
}
'''
c = 0
json1 = himoBOT.sparql_generator_url( quarry )
total = len(json1)
for q in json1:
    c += 1
    Qid = q['q']
    printe.output( 'work %d from %d , %s' % ( c , total , Qid ) )
    descriptions = himoBOT2.Get_item_descriptions_or_labels( Qid  , "descriptions" )
    if not "ar" in descriptions:
        himoAPI.Des_API( Qid , 'عدد أولي' , 'ar' , ask = "")
#---

















#---
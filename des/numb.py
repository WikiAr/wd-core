#!/usr/bin/python
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
# ---
from wd_API import wd_bot
from API import himoBOT2
from wd_API import himoAPI
# ---
limit = { 1 : 0 }
quarry = '''SELECT (CONCAT(STRAFTER(STR(?item), "/entity/")) AS ?q)
 WHERE {
?item wdt:P31 wd:Q49008.
#FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
FILTER NOT EXISTS {?item schema:description ?ar filter (lang(?ar) = "ar")} .
}
'''
c = 0
json1 = wd_bot.sparql_generator_url( quarry )
total = len(json1)
for q in json1:
    c += 1
    Qid = q['q']
    printe.output( 'work %d from %d , %s' % ( c , total , Qid ) )
    descriptions = himoBOT2.Get_item_descriptions_or_labels( Qid  , "descriptions" )
    if "ar" not in descriptions:
        himoAPI.Des_API( Qid , 'عدد أولي' , 'ar' , ask = "")
# ---

















# ---
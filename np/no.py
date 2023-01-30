#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.

#Q13005188 mandal 
'''

python3 pwb.py np/nldes3 limit:2000 sparql:Q571 #كتاب
python3 pwb.py np/nldes3 limit:2000 sparql:Q7725634 #رواية
python3 pwb.py np/nldes3 limit:2000 sparql:Q1760610 #كتاب هزلي
python3 pwb.py np/nldes3 limit:2000 sparql:Q1318295 #قصة
python3 pwb.py np/nldes3 limit:2000 sparql:Q49084 #قصة قصيرة
python3 pwb.py np/nldes3 limit:2000 sparql:Q187685 #أطروحة أكاديمية
python3 pwb.py np/nldes3 limit:2000 sparql:Q96739634 #حركة فردية

python3 pwb.py np/nl p50s limit:2000



python3 pwb.py np/nl limit:2000

python3 pwb.py np/no limit:2000

python3 pwb.py np/no songs limit:2000 ask

python3 pwb.py np/nldes3 a3r sparql:Q3231690 #طراز سيارة

python3 pwb.py np/nldes3 a3r sparql:Q7366 #أغنية
python3 pwb.py np/nldes3 a3r sparql:Q482994 #ألبوم
python3 pwb.py np/nldes3 a3r sparql:Q134556 #منفردة
python3 pwb.py np/nldes3 a3r sparql:Q7302866 #مقطع
python3 pwb.py np/nldes3 a3r sparql:Q1573906 #جولة
python3 pwb.py np/nldes3 a3r sparql:Q182832 #حفلة


python3 pwb.py np/nldes3 a3r sparql:Q215380 #طاقم موسيقي
python3 pwb.py np/nldes3 a3r sparql:Q7278 #حزب سياسي
python3 pwb.py np/nldes3 a3r sparql:Q14752149  #نادي كرة قدم للهواة
python3 pwb.py np/nldes3 a3r sparql:Q476028  #نادي كرة قدم 

python3 pwb.py np/nldes3 sparql:Q27020041 #موسم رياضي

python3 pwb.py np/nldes3 a3r sparql:Q43229 #منظمة
python3 pwb.py np/nldes3 a3r sparql:Q728937 #خط سكة حديد
python3 pwb.py np/nldes3 a3r sparql:Q46970 #شركة طيران
python3 pwb.py np/nldes3 a3r sparql:Q4830453 #شركة
python3 pwb.py np/nldes3 a3r sparql:Q783794 #شركة
'''
import sys
import re
import pywikibot
from np.nldes3 import wd_sparql_query, action_one_item, p50s, songs_type
from np.nldes3 import *
#---
taber = { 1 : p50s }
#---
totalreads = 0
#---
if sys.argv and 'songs' in sys.argv:
    taber[1] = {}
    for dd in songs_type :
        taber[1][dd] = { 'ar' : songs_type[dd] , 'P' : 'P175' }
#---
query = '''SELECT DISTINCT 
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P31 wd:%s . 
  #optional { 
  ?item wdt:%s ?p50. ?p50 rdfs:label ?labe .FILTER((LANG(?labe)) = "ar")
  #}
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item'''
#---
if sys.argv and 'optional' in sys.argv:
    query = '''SELECT DISTINCT 
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P31 wd:%s . 
  optional { 
  ?item wdt:%s ?p50. ?p50 rdfs:label ?labe .FILTER((LANG(?labe)) = "ar")
  }
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item'''
#---
def just_get_ar(labe):
    lab = labe.split('@@')
    tab = []
    #---
    claimstr = ''
    #---
    for o in lab:
        test = re.sub( "[abcdefghijklmnopqrstuvwxyz@]" , '' , o.lower() )
        if test.lower() == o.lower() and o != '' :
            tab.append(o)
    #---
    if tab != []:
        claimstr = '، و'.join(tab)
        print( "just_get_ar:%s." % claimstr )
    #---
    return claimstr
    #---
for qq in taber[1] :
    sparql_query = query % ( qq , taber[1][qq]['P'] )
    #---
    pigenerator = wd_sparql_query( sparql_query , ddf = True )
    #---
    for wd in pigenerator:
        pywikibot.output( "<<lightblue>> ============" )
        pywikibot.output( wd )
        q = wd['item'].split("/entity/")[1]
        totalreads+=1
        pywikibot.output( "p%d/%d q:%s" % ( totalreads , len(pigenerator) , q ) )
        #---
        claimstr = just_get_ar(wd.get( 'lab' , '' ))
        #---
        thisfound,thisone = action_one_item( 'ar', q, claimstr=claimstr)
    #---

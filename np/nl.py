#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.

#Q13005188 mandal 
'''

python3 pwb.py np/nl1 a3r p50s save
python3 pwb.py np/nl1 a3r save

python3 pwb.py np/nldes3 sparql:Q96739634


'Q452237':{'ar':'حركة', 'en':'motion' },# 69706
'Q22969563':{'ar':'', 'en':'bodendenkmal' },# 43700
'Q187685':{'ar':'أطروحة أكاديمية', 'en':'doctoral thesis' },# 27516
'Q1505023':{'ar':'استجواب', 'en':'Interpellation' },# 18598
'Q97695005':{'ar':'حركة مجموعة اللجنة', 'en':'committee group motion' },# 11681
'Q55725952':{'ar':'نموذج جرار', 'en':'tractor model' },# 10349
'Q98491862':{'ar':'توجيهات اللجنة', 'en':'committee directives' },# 10076
'Q10429085':{'ar':'تقرير', 'en':'report' },# 9937
'Q2065227':{'ar':'جريدة رسمية', 'en':'official journal' },# 9533
'Q47089':{'ar':'فالق', 'en':'fault' },# 8244
'Q686822':{'ar':'مشروع قانون', 'en':'bill' },# 7919
'Q457843':{'ar':'', 'en':'album amicorum' },# 7635
'Q96482904':{'ar':'', 'en':'decision of the Supreme Court of Sweden' },# 7288
'Q98467717':{'ar':'', 'en':'record of meeting of the Riksdag' },# 7151
'Q13433827':{'ar':'مقالة موسوعية', 'en':'encyclopedic article' },# 4993
'Q41710':{'ar':'مجموعة إثنية', 'en':'ethnic group' },# 4566
'Q21014462':{'ar':'خط خلية', 'en':'cell line' },# 4334
'Q4164871':{'ar':'منصب', 'en':'position' },# 4000

'''
import sys
import pywikibot
from np.nldes3 import wd_sparql_query
from np.nldesc import action_one_item, all_types_list, simple_set_byP131, SPARQLSE, New_QS, p50s
from np.np_lists import bldiat, Space_tab, p50s, nationalities, songs_type, others_list, others_list_2, space_list_and_other, qura, Geo_entity
#---
taber = qura
#---
if sys.argv and 'p50s' in sys.argv:
    taber = p50s
#---
totalreads = 0
#---
for g in taber :
    sparql_query = SPARQLSE.get(g,'')
    #---
    pigenerator = wd_sparql_query( sparql_query , ddf = True )
    #---
    for wd in pigenerator:
        pywikibot.output( "<<lightblue>> ============" )
        pywikibot.output( wd )
        q = wd['item'].split("/entity/")[1]
        totalreads+=1
        pywikibot.output( "p%d/%d q:%s" % ( totalreads , len(pigenerator) , q ) )
        thisfound,thisone = action_one_item( 'ar', q )
    #---
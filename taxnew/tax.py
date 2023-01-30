#!/usr/bin/python
# -*- coding: utf-8  -*-
#
"""

python3 pwb.py taxnew/tax descqs place:Family_of_molluscs limit:400 
python3 pwb.py taxnew/tax descqs limit:600 qslimit:5000
python3 pwb.py taxnew/tax descqs limit:400

"""
#f
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
from pywikibot import pagegenerators as pg
import codecs
from API.maindir import main_dir
#---
import sys
#---
import urllib

import urllib.request
import urllib.parse

#---
# start of himoBOT.py file
from API import himoAPI
from API import himoBOT2
from API import himoBOT
#---
from API.taxones import *#tax_translationsNationalities#taxone_list
#---
Nationalities_list = list( tax_translationsNationalities.keys() )
Nationalities_list.sort()
#---
#site = pywikibot.Site('wikidata', 'wikidata')
#repo = site.data_repository()
#---
offset = { 1 : 0 }
offset_place = { 1 : 0 }
#---
limit = { 1 : 0 }
QSlimit = { 1 : 3000 }
alllimit = { 1 : 50000 }
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(':')
    #---
    # python3 pwb.py taxnew/tax -tax:isopod
    if arg == 'tax' or arg == '-tax' :
        value = "~ " + value.replace("_" , " ")
        if value in taxone_list:
            taxone_list = { value : taxone_list[ value ] }
        else:
            print("tax value:(%s) not in taxone_list" % value )
    #---
    if arg == 'offplace':
        offset_place[1] = int(value)
    #---
    if arg == 'off':
        offset[1] = int(value)
    #---
    if arg == 'limit':
        limit[1] = int(value)
    #---
    if arg == 'alllimit':
        alllimit[1] = int(value)
    #---
    if arg == 'qslimit':
        QSlimit[1] = int(value)
    #---
    # python3 pwb.py des/des descqs limit:4000 place:Q185113
    # python3 pwb.py des/des descqs limit:1000 place:Q8054
    value2 = value.replace('_', " ")
    if arg == 'place' :
        if value2 in tax_translations:
            tax_translations = { value2 : tax_translations[value2] } 
        else:
            print('value2:%s not in tax_translations ' % value2 )
            tax_translations = {}
    #---
tax_translations = {}
tax_translations_lower = {}
#---
for tax_key, tax_lab in taxone_list.items():      # الأصنوفة
    if tax_lab.strip() != '' and tax_key.strip() != '' :
        for natkey in Nationalities_list :            # النوع 
            natar = tax_translationsNationalities[natkey]
            if natkey.strip() != '' and natar.strip() != '' :
                kkey = tax_key.replace('~', natkey)
                tax_translations[kkey] = tax_lab.replace('~',natar )
                tax_translations_lower[kkey.lower()] = tax_lab.replace('~',natar )
#---
def logme( dar ):
   # with codecs.open("o/"+aas+".log.csv", "a", encoding="utf-8") as logfile:
    with codecs.open("taxnew/q.log.csv", "a", encoding="utf-8") as logfile:
        line = '%s%s' % (dar , '\n')
        logfile.write( line )
    logfile.close()
#---
New_QS = { 1 : [] }
#---
def descqs( q , value , lang ):
    qsline = '%s|D%s|"%s"' % ( q, lang , value )
    if "logme" in sys.argv or "log" in sys.argv:
        pywikibot.output( "<<lightyellow>>a %d\t%d:add %s to qlline " % (len(New_QS[1]) , QSlimit[1] , qsline  )  )
        logme( qsline )
    else:
        if len(New_QS[1]) < QSlimit[1]:
            New_QS[1].append( qsline )
            pywikibot.output( "<<lightyellow>>a %d\t%d:add %s to qlline " % (len(New_QS[1]) , QSlimit[1] , qsline  )  )
        else:
            pywikibot.output( "<<lightgreen>> Add %d line to quickstatements" % len(New_QS[1]) )
            himoAPI.QS_line( "||".join( New_QS[1] ) , user = "Mr.Ibrahembot" )
            New_QS[1] = []
#---
q_list_done = []
#---
def Add_desc( q , value , lang ):
    #---
    if q in q_list_done:
        pywikibot.output("q in q_list_done")
        return ''
    #---
    q_list_done.append(q)
    #---
    if "descqs" in sys.argv:
        descqs( q , value , lang )
    else:
        himoAPI.Des_API( q , value , lang , ask = "")
#---
def wd_sparql_query( spq , ddf = False ):
    #---
    qua = spq
    #---
    #if limit[1] != 0 : 
        #spq = spq + " limit " + str( limit[1] )
    #---
    New_List = []
    #---
    #wikidatasite=pywikibot.Site('wikidata','wikidata') 
    #generator=pg.WikidataSPARQLPageGenerator(spq,site=wikidatasite)
    #---
    Keep = True
    off = 0
    #---
    if offset[1] != 0 :
        off = offset[1]
    #---
    while Keep:
        #---
        quarr = qua
        #---
        #if ddf:
        if limit[1] != 0 :
            quarr = quarr + "\n limit " + str( limit[1] ) 
        if off != 0 :
            quarr = quarr + " offset " + str( off )
        #else: offset[1] != 0 :
            #quarr = quarr + " offset " + str( offset[1] )
        #---
        #pywikibot.output(quarr)
        #---
        #pywikibot.output( 'quarr "%s"' % quarr )
        #---
        generator = himoBOT.sparql_generator_url( quarr )
        #---
        for x in generator:
            New_List.append( x )
        #---
        off = int( off + limit[1] )
        #---
        if off == alllimit[1] or off > alllimit[1] :
            print('Keep = False 1 ')
            Keep = False
        #---
        if not generator or generator == [] or "nokeep" in sys.argv :
            print('Keep = False 2 ')
            Keep = False
        #---
        if not ddf or limit[1] == 0 :
            print('Keep = False 3 ')
            Keep = False
    #---
    return New_List
#---
def main():
    pywikibot.output( '<<lightpurple>>------------ main :' )
    #---
    Queries = 1
    #---
    tax_translations_list = list(tax_translations.keys())
    tax_translations_list.sort()
    totalqueries = len(tax_translations_list)
    #---
    lang = "ar"
    #---
    for translation in tax_translations_list:
        #  الاستعلام
        Queries += 1
        pywikibot.output( '<<lightgreen>>a:%d\t%d: Quary:%s, %s. ==' % (Queries , totalqueries , translation , lang ) )
        #---
        if Queries < offset_place[1]:
            continue
        #---
        ta2 = translation#.lower() + ' (fossil)'
        ta_lower = ta2.replace( ta2[0], ta2[0].lower() , 1)
        ta_upper = ta2.replace( ta2[0], ta2[0].upper() , 1)
        pywikibot.output(lang + '\t' + ta2 + '\t' + tax_translations[translation])
        qua = '''SELECT (CONCAT(STRAFTER(STR(?item), "/entity/") ) as ?q)#?item 
WHERE 
    {
    { ?item schema:description "%s"@en.  } union { ?item schema:description "%s"@en.  }
    OPTIONAL { ?item schema:description ?itemDe. FILTER(LANG(?itemDe) = "%s").  }
    FILTER (!BOUND(?itemDe)) 
    }

        ''' % ( ta_lower , ta_upper , lang )
        #---
        #---
        json1 = wd_sparql_query( qua , ddf = True )
        #action(json1 , translation , tax_translations)    #---
        total = len(json1)
        c = 0
        #---
        for q in json1:    # عنصر ويكي بيانات
            c += 1
            q = q["q"]
            pywikibot.output( '<<lightyellow>>  * action %d/%d "%s"' % ( c , total , q) )
            #---
            desc = tax_translations[translation]
            #---

            #descriptions = item["descriptions"]
            #if lang in descriptions:
                #pywikibot.output('lang:%s in descriptions(%s)' % descriptions[lang] )
                #if descriptions[lang] != desc:
                    #return ''
            #---
            Add_desc( q , desc , lang  )
    #---
    if New_QS[1] != []  :
        himoAPI.QS_line( "||".join( New_QS[1] ) , user = "Mr.Ibrahembot" )
        New_QS[1] = []
    #---
    pywikibot.output("انتهت بنجاح")
#---

MainTest = False#False#True
if __name__ == "__main__":
    if MainTest:
        Main_Test()
    else:
        main()
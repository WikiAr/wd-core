#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python pwb.py p131/pp

إضافة خاصية التقسيم الإداري بناءاً على معلومات جيو نيمز.

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json
import re
import time
import pywikibot
#import Nationalities as aa
import codecs
from API.maindir import main_dir
from datetime import datetime
#---
import sys
#---
import urllib
import urllib
import urllib.request
import urllib.parse

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#himoAPI.Merge( q1, q2)
#---
# start of himoBOT.py file
from API import himoBOT
#---
def log(t , page):
    #pywikibot.output( t )
    fo  = str(t) + '\n'
    with codecs.open("p131/log/"+page+".log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(fo)
      except :
            pywikibot.output("Error writing")
#---   
def getjson(geoname , values):
    url = 'http://' + 'api.geonames.org/getJSON?formatted=true&username=ibrahemqasim&geonameId=' + geoname 
    #---
    tables = {}
    for va in values:
        tables[va] = ''
    #---
    sparql = himoBOT.getURL(url=url)
    js = himoBOT.load_SPARQL_New(sparql=sparql)
    if js:
        if 'status' in js and 'message' in js['status']:
            pywikibot.output( '<<lightred>> "%s".' %  js['status']['message'])
            return False
        for va in values:
            if va in js:
                tables[va] = js[va]
    #---
    pywikibot.output(tables)
    return tables
#---
'''def Work_VA(adminId1 , List_pp , item , type):
    table = {'p131' : ''}
    if adminId1 in List_pp[type]:
        pywikibot.output( '<<lightblue>>%s "%s" already there: "%s".' % (type , adminId1 , List_pp[type][adminId1]) )
        table['p131'] = List_pp[type][adminId1]
    else:
        quarry_2 = ( 'SELECT (concat(strafter(str(?itema),"/entity/")) as ?item) WHERE { ?itema wdt:P1566 "%s". ?itema wdt:P17 wd:Q805.} limit 1' % adminId1)
        item_2 = himoBOT.sparql_generator_url(quarry_2)
        #pywikibot.output( "<<lightblue>>quarry_2:----\n%s\n----" % quarry_2 )
        if item_2:
            table['p131'] = item_2[0]['item']
            pywikibot.output( '<<lightblue>>%s: find item "%s" for: "%s".' % (type , table['p131'] , adminId1) )
            tao_2 = '\nList_pp["' + type + '"]["' + adminId1 + '"] = "' + str(item_2[0]['item']) + '"'
            log(tao_2, "List_pp.py")
    #---
    tao_1 = '\nList["' + item + '"] = ' + str(table)
    log(tao_1, "items.py")
    #---
    KA = False#False#True
    if KA:
        if table['p131'] != '' :
            pywikibot.output( '<<lightred>>P131: Add "%s" to: "%s".' % (table['p131'] , item) )
            himoAPI.Claim_API2(item , 'P131' , table['p131'])'''
#---
def Work_VA(adminId1 , List_pp , item , type):
    table = {'p131' : ''}
    if adminId1 in List_pp:
        pywikibot.output( '<<lightblue>>%s "%s" already there: "%s".' % (type , adminId1 , List_pp[adminId1]) )
        table['p131'] = List_pp[adminId1]
    else:
        pywikibot.output( '<<lightblue>> "%s" not in List_pp.' % adminId1)
        quarry_2 = ( 'SELECT (concat(strafter(str(?itema),"/entity/")) as ?item) WHERE { ?itema wdt:P1566 "%s". ?itema wdt:P17 wd:Q805.} ' % adminId1)
        item_2 = himoBOT.sparql_generator_url(quarry_2)
        if item_2:
            pywikibot.output( "<<lightblue>> found len(item_2): %s.." % len(item_2)  )
            pywikibot.output(item_2)
            if len(item_2) < 2:
                table['p131'] = item_2[0]['item']
                pywikibot.output( '<<lightblue>>%s: find item "%s" for: "%s".' % (type , table['p131'] , adminId1) )
                tao_2 = '\nList_pp["' + adminId1 + '"] = "' + str(item_2[0]['item']) + '"'
                log(tao_2, "pplist.py")
                #---
                tao_1 = '\nList["' + item + '"] = ' + str(table)
                log(tao_1, "items.py")
            #---
            else:
                #pywikibot.output( "<<lightblue>> found len(item_2): %s.." % len(item_2)  )
                gg_1 = item + '\tgeoname:\t' + adminId1
                for it in item_2:
                    gg_1 = gg_1 + '\t' + it['item']
                pywikibot.output( '<<lightblue>> ---------\n many value "%s"..' % gg_1 )
                log(gg_1, "dupp.log.csv")
            #---
        else:
            pywikibot.output( '<<lightred>> NO item_2. for "%s"' %  adminId1)
            jsop = getjson(adminId1 , ['wikipediaURL' ,'asciiName' , 'fcodeName'])
            if jsop:
                cdcdc = '%s\t%s' % ( adminId1 , str(jsop) )
                log( cdcdc , "need.log.csv")
    #---
    KA = False#False#True
    if KA:
        if table['p131'] != '' :
            pywikibot.output( 'P131: Add "%s" to: "%s".' % (table['p131'] , item) )
            himoAPI.Claim_API2(item , 'P131' , table['p131'])

#---
Table ={
    'Q805'  :   {   'code':'YE' ,   'id':'69543'    } 
    ,'Q851' :   {   'code':'SA' ,   'id':'' } 
    }
#---
def main2():
    limit = 2000
    #---
    P17 = 'SA'
    quarry = 'SELECT DISTINCT (concat(strafter(str(?item),"/entity/"))  as ?item1) ' 
    quarry = quarry + '?P1566 WHERE { ?item wdt:P1566 ?P1566. ?item wdt:P17 wd:%s. ' % P17
    quarry = quarry + 'FILTER NOT EXISTS {?item wdt:P131 ?P131.}  }'
    #---
    if sys.argv and  len(sys.argv) > 1:
        limit  = sys.argv[1]
    quarry = quarry + 'limit ' + str(limit)
    pywikibot.output(quarry)
    #---
    pagelist = himoBOT.sparql_generator_url(quarry) 
    num = 0
    #---
    for p in pagelist:
        from pplist import List_pp #List_pp
        num = num + 1
        item = p['item1']
        geoname = p['P1566']
        pywikibot.output( '<<lightyellow>>\n----------\n>> %d  / %d >> %s << geoname: %s << js:' % ( num ,len(pagelist),  item , geoname) )
        js = getjson(geoname , ['adminId1' ,'adminName1' , 'adminId2'  , 'adminName2', 'adminId3'  , 'adminName3' , 'countryCode' , 'countryId'])
        #pywikibot.output(js)
        if js:
            #---
            adminId1  , adminId2 , adminId3= js['adminId1'] , js['adminId2'] , js['adminId3']
            #if js["countryCode"] == "YE" or js["countryId"] == "69543":
            if js["countryCode"] == Table[P17]['code'] or js["countryId"] == Table[P17]['id']:
                if adminId3 != '' :
                    pywikibot.output('found adminId3 "%s" for item: "%s"' % (adminId3 , item ) )
                    Work_VA(adminId3 , List_pp , item, 'adminId3')
                elif adminId2 != '' :
                    Work_VA(adminId2 , List_pp , item, 'adminId2')
                elif adminId1 != '' :
                    Work_VA(adminId1 , List_pp , item, 'adminId1')
            else:
                pywikibot.output('CountryCode for "%s" geoname:"%s" not %s: "%s"' % (geoname , item , Table[P17]['code'] , js["countryCode"] ) )
#---
def main3():
    #---
    from items import List
    lenth = len(List)
    num = 0
    for item in List:
        num += 1
        pywikibot.output( '<<lightred>> %d / %d P131: Add "%s" to: "%s".' % (num , lenth , List[item]['p131'] , item) )
        himoAPI.Claim_API2(item , 'P131' , List[item]['p131'])
#---
def main():
    if sys.argv and len(sys.argv) > 2:
        main3()
    else:
        main2()
#---
if __name__ == "__main__":
    main()
#---
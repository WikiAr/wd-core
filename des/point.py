#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


تسمية  عناصر ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
import codecs
import time
import re
#---

from API import printe
import sys
    
#---
from API import himoAPI
#---
from API import himoBOT2
from API import himoBOT
#---
bylangs = False#False#True
#---
limits = { 1: "1000"}
#---
items_done = []
#---
def action( json1 ):
    try:
        total = len(json1)
    except:
        total = 0
    c = 1
    #---
    for tab in json1:    # عنصر ويكي بيانات
        printe.output( tab )
        q = tab["item_q"]
        if not q in items_done:
            c += 1
            printe.output( 'action %d/%d "%s"' % ( c , total , q) )
            label = tab["label"]
            #---
            #year =  re.match( '(\d\d\d\d)', label)
            year = re.sub( '.*(\d+\d+\d+\d+).*' , "\g<1>", label)
            #---
            if year ==label:
                year = ""
            #---
            if year != "" :
                year1 = year#.group(1)
                timestr = "+%s-00-00T00:00:00Z" % year1
                #---
                PP_time = ""
                PP = himoBOT2.Get_Property_API( q , "P585")
                if PP and PP[0] and PP[0]["time"]:
                    PP_time = PP[0]["time"]
                    printe.output( '  * PP:"%s"' % PP[0]["time"] )
                #---
                printe.output( '  * year1:"%s"' % year1 )
                if PP_time != timestr:
                    himoAPI.Claim_API_time(q , "P585", precision = 9, year = year1 , strtime = timestr )
                else:
                    printe.output( ' <<lightred>> * time == timestr.%s ' % timestr )
        else:
            printe.output( ' <<lightred>> * q in items_done. ' % q )
#---
Quarry = {}
Quarry["y"] = '''
SELECT (concat(strafter(str(?item),"/entity/"))  as ?item_q)
 ?label WHERE {
    ?item wdt:P31 ?pp.
    ?pp wdt:P31* wd:Q15275719.
    #OPTIONAL {?item wdt:P641/wdt:P279 wd:Q2215841. }
    #?item wdt:P641/wdt:P279 wd:Q2215841.
    FILTER NOT EXISTS { ?item wdt:P585 ?P585. }
    FILTER NOT EXISTS { ?item wdt:P580 ?P580. }
    #?item rdfs:label ?l . FILTER( REGEX(?l, "(1[89]\u007C20)\\\d\\d") ) 
    ?item rdfs:label ?label . FILTER( REGEX(?label, "(\\\d\\\d\\\d\\\d)") ) 
    #%s
    #?item rdfs:label ?l . FILTER(lang(?l) = "en" && REGEX(?l, "(1[89]\u007C20)\\\d\\d") ) 
}
#LIMIT 2
'''
#---
def main():
    #---
    #python pwb.py des/point -limit:2
    #---
    taxose = ""
    qya = {}
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg =='-limit' :
            printe.output( '<<lightred>>>>  limit ( %s )  ' %  value  )
            limits[1] = value
        #---
        if arg in Quarry :
            printe.output( '<<lightred>>>>  use Quarry:%s . ' % arg)
            qya[arg] = Quarry[arg]
    #---
    if qya == {} : 
        qya = Quarry
    #---
    number = 0 
    for key in qya:
        number += 1
        quuu = qya[key]
        for arg in sys.argv:
            arg, sep, value = arg.partition(':')
            #---
            if arg == 'P31' or arg == '-P31' :
                printe.output( '<<lightred>>>>  P31:%s. ' % value  )
                taxose = "?item wdt:P31/wdt:P279* wd:%s."  % value
            #---
            if arg == 'lang' or arg == '-lang' :
                if value == "fr":
                    quuu = quuu.replace('"en"' , '"fr"' )
                    quuu = quuu.replace('"Category:"' , '"Catégorie:"' )
                    printe.output( '<<lightred>>>> change lang to france. ' )
        #---
        quuu = quuu % taxose
        #---
        if limits[1] != "" : 
            quuu = quuu + '\n LIMIT %s' % limits[1]
        #---
        printe.output("quuu : %d/%d key:%s" %  ( number , len(qya) , key ) ) 
        printe.output(quuu)
        #---
        json1 = himoBOT.sparql_generator_url(quuu)
        action( json1 )
#---
if __name__ == "__main__":
    main()
#---
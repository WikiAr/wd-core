#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python pwb.py wd/koo -page:مارك_فان_بوميل

python3 pwb.py wd/koo -ns:0 -ref:قالب:كووورة

"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
# 
import codecs
import requests
import time as ttime
from datetime import datetime
from pywikibot import textlib

import re
import unicodedata
#---
import sys
#---
sys_argv = sys.argv or []
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
# start of himoAPI.py file
from API import himoAPI_test as himoAPI
#himoAPI.page_put(NewText , summary , title)

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_time(q , property, precision = 9, year = "" , strtime = "" )
#himoAPI.Claim_API_quantity( q , property, quantity )
#himoAPI.Claim_API_string( q , property, string )
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, lab , lang , False, Or_Alii = False, change_des = False)
#himoAPI.Alias_API( Qid, [Alias] , lang , False , Remove = [] )
#himoAPI.Merge( q1, q2)
#himoAPI.wbcreateredirect( From, To)
#himoAPI.Sitelink_API( Qid, title , wiki , enlink="" , ensite = "" )
#himoAPI.Remove_Sitelink( Qid , wiki )
#himoAPI.Add_Labels_if_not_there( Qid, label , lang , ASK = "")
#himoAPI.add_quall(Claimid , quall_prop , {"entity-type":  'item', "numeric-id": qua_id } )
#---
def PPPTemp( text ):
    return named
#---
done = []
#---
def woo( page ):
    #---
    title = page.title(as_link=False)
    text = page.text
    templates = textlib.extract_templates_and_params(text, True, True)
    #---
    id = ''
    info = himoBOT2.Get_page_info_from_wikipedia("ar" , title)
    qid = info.get("q","")
    #---
    for x , y in templates:
        if x.strip() == "كووورة" : 
            for key in sorted(y):
                if key == "1" :
                    id = y[key]
    #---
    pywikibot.output( "koora id:%s" % id )
    #---
    P31 = himoBOT2.Get_Claim_API(qid , "P31") 
    iin = himoBOT2.Get_Property_API( qid , "P8021", titles=title,sites="arwiki")
    #pywikibot.output( "iin:%s" % iin )
    #---
    pywikibot.output( "P31:%s" % P31 )
    #---
    if P31 != "Q5":
        return ''
    #else:
        #pywikibot.output( "P31:%s" % P31 )
    #---
    if not iin and not id in done:
        f = himoAPI.Claim_API_string( qid , "P8021", id )
        done.append(id)
        #pywikibot.output( f )
    #---
def main(*args):
    options= {}
    generator = gent.get_gent(*args)
        
    for page in generator:
        woo(page)
#---
if __name__ == "__main__":
    main()
#---
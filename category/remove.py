#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة خواص وتسميات لمقالات العلاقات بين البلدان

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json

import re
import time
import pywikibot
import codecs
from datetime import datetime
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.page_put(NewText , summary , title)

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_time(q , property, precision = 9, year = "" , strtime = "" )
#himoAPI.Claim_API_string( q , property, string )
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, lab , lang , False, Or_Alii = False, change_des = False)
#himoAPI.Alias_API( Qid, [Alias] , lang , False , Remove = [] )
#himoAPI.Merge( q1, q2)
#himoAPI.wbcreateredirect( From, To)
#himoAPI.Sitelink_API( Qid, title , wiki )
#himoAPI.Remove_Sitelink( Qid , wiki )
#himoAPI.Add_Labels_if_not_there( Qid, label , lang , ASK = "")
#himoAPI.add_quall(Claimid , quall_prop , {"entity-type":  'item', "numeric-id": qua_id } )
#---
removed = [ "علاقات" , "العلاقات" , "العلاقات ال ال" , "علاقات و"  , "علاقات  و" ]
#---
def work(q):
    item = himoBOT2.Get_Item_API_From_Qid( q , sites = "" , titles = "", props = "aliases" )
    aliases = item["aliases"].get("ar" , [] )
    #pywikibot.output( aliases )
    aliases = [ x["value"] for x in aliases  ]
    #aliases2 = aliases
    #---
    pywikibot.output( "q:%s,aliases:%s" % ( q , ",ali: ".join( aliases ) ) )
    #---
    removing = []
    #---
    for x in aliases:
        x2 = x.replace( "  " , " "  )
        #---
        if x2 in removed:
            removing.append( x )
            pywikibot.output( "remove:%s" % x )
        #---
        if x.find(" ال " ) != -1 or x.endswith(" ال" ) or x.endswith(" و" ) or len( x2.split( " " )  ) == 2 :
            removing.append( x )
            pywikibot.output( "remove:%s" % x )
    #---
    himoAPI.Alias_API( q , [] , "ar" , False , Remove = removing )

#---
def main():
    List_Search = himoBOT2.Search( "العلاقات ال ال" )
    for q in List_Search :
        #---
        work(q)
        #---
if __name__ == "__main__":
    #work("Q9346141")
    main()
    
#---













#---
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
from API import himoBOT2
#---
from API import himoAPI
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
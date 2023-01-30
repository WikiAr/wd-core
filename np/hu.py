#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.

#Q13005188 mandal 
'''
'''
import pywikibot
from np.si3 import wd_sparql_query, ISRE
from np.si3 import *
#---
query = '''SELECT ?item WHERE { ?item schema:description  "férfi keresztnév"@hu }'''
#---
pigenerator = wd_sparql_query( query , ddf = True )
#---
totalreads = 0
#---
for wd in pigenerator:
    pywikibot.output( "<<lightblue>> ============" )
    pywikibot.output( wd )
    q = wd['item'].split("/entity/")[1]
    totalreads += 1
    pywikibot.output( "p%d/%d q:%s" % ( totalreads , len(pigenerator) , q ) )
    ISRE( q , totalreads , len(pigenerator) )
    #---

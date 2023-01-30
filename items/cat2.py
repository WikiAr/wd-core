#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update


"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
import json
import time

import codecs
from API.maindir import main_dir

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
# 
#import pwb
import re
import string
#---
import sys
#---
import urllib.request
import urllib.parse

#---
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.


#---
def log( title , logfile ):
    #---
    form = "%s\n" % title
    #---
    #if QS2Rows:
    with codecs.open( "items/list/" + str(logfile) + ".log.csv", "a", encoding="utf-8") as logFil:
      try:   
         logFil.write(form)
      except :
         pass
    logFil.close()
#---
Bi = 40000
def mainwithcat(*args):
    args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Articles_without_Wikidata_item'}
    options = {}
    #---
    generator = gent.get_gent(*args)
        
    numb = 0
    logfile = 1
    s = range(1,50)
    list = [Bi * x for x in s]
    pywikibot.output(list)
    for page in generator:
        numb += 1
        if numb in list:
            logfile += 1
        title = page.title(as_link=False)
        if page:
            pywikibot.output( '*<<lightred>> >%d page "%s" :' % ( numb , title ) )
            log( title , logfile )
        #else:
            #pywikibot.output( '*<<lightred>> >%d error with page "%s" < :' % ( numb , title ) )
            #pass
#---
if __name__ == "__main__":
    mainwithcat()
#---
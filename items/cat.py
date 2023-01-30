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
    with codecs.open( "items/" + logfile + ".log.csv", "a", encoding="utf-8") as logFil:
      try:   
         logFil.write(form)
      except :
         pass
    logFil.close()
#---
BigNumber = 100000
def mainwithcat(*args):
    args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Articles_without_Wikidata_item'}
    options = {}
    #---
    generator = gent.get_gent(*args)
        
    numb = 0
    for page in generator:
        numb += 1
        if numb <= (BigNumber * 1) :
            logfile = '1'
        elif numb <= (BigNumber * 2) :
            logfile = '2'
        elif numb <= (BigNumber * 3) :
            logfile = '3'
        elif numb <= (BigNumber * 4) :
            logfile = '4'
        elif numb <= (BigNumber * 5) :
            logfile = '5'
        elif numb <= (BigNumber * 6) :
            logfile = '6'
        elif numb <= (BigNumber * 7) :
            logfile = '7'
        elif numb <= (BigNumber * 8) :
            logfile = '8'
        elif numb <= (BigNumber * 9) :
            logfile = '9'
        else:
            logfile = '10'
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
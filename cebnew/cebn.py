#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

تحديث صفحات cebwiki

python pwb.py update/update


"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
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
import urllib
import urllib
import urllib.request
import urllib.parse

#---
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.

#---
cebwiki = pywikibot.Site("ceb", "wikipedia")
wikidatasite=pywikibot.Site('wikidata','wikidata') 
repo = wikidatasite.data_repository()
#--- 
from API.category import *
import newupdate
#---
# start of himoBOT.py file
from API import himoBOT
#---
references={
                        "snaks": {
                            "P143": [
                                {
                                    "snaktype": "value",
                                    "property": "P143",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 837615,
                                            "id": "Q837615"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "snaks-order": [
                            "P143"
                        ]
                    }
#---                
def loggg(line , file):#vaul
    pywikibot.output( '**<<lightyellow>> loggg :'  + str(line) )
    logFile = file
    #---
    form = "%s\n"
    ccc  = (form % (line))
    #---
    with codecs.open(JlobalFileFloder + 'log/'+  logFile + ".log.csv", "a", encoding="utf-8") as logfile:
        try:   
            logfile.write(ccc)
        except :
            pass
        logfile.close()
#---
def ISRE(page, pagetitle, num):
    newupdate.ISRE(page, pagetitle, num)
#---
LOOO = {'logname' : 'tot'}

def log_new(title , log):#vaul
    #pywikibot.output( '**<<lightyellow>> log_new :' )
    #---
    log = 'totlog/' +  LOOO['logname'] + log
    title = title + '\n'
    with codecs.open(JlobalFileFloder + log + ".log.csv", "a", encoding="utf-8") as logfile:
        try:   
            logfile.write(title)
        except :
            pass
    logfile.close()
       
test = False#False#True
QS2 = False#False#True

#---        
def mainwithcat(*args):
    pywikibot.output( '**<<lightyellow>> mainwithcat:')
    #---
    #args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Paghimo_ni_bot_2016-10'}
    options = {}
    #---
    generator = gent.get_gent(*args)
        
    num = 0

    for page in generator:
        num += 1
        title = page.title(as_link=False)
        #start(text, title)
        #pywikibot.output(num)
        #ISRE(page , title, num )
        #try:
        if page:
            pywikibot.output( '*<<lightred>> >%d page "%s" :' % ( num , title ) )
            ISRE( page , title, num )
        else:
        #except:
            pywikibot.output( '*<<lightred>> >%d error with page "%s" < :' % ( num , title ) )
            pass
#---
def Get_P_API(q , P):
    url = 'https://www.wikidata.org/w/api.php?action=wbgetclaims&entity=' + q + '&property=' + P + '&format=json'
    html = urllib.request.urlopen(url).read().strip().decode('utf8','ignore')
    json = himoBOT.load_SPARQL_New(sparql = html)
    if P in json['claims']:
        va =  json['claims'][P][0]['mainsnak']["datavalue"]
        if ('value' in va) and ('id' in va['value']):
            return va['value']['id']
    return False
#---
def __NewFindWork__(item):
    q = item.title(as_link=False)
    #pywikibot.output( '**<<lightyellow>> NewFindWork:' )
    #---
    if 'P31' in item.claims:
        file = item.claims['P31'][0].getTarget()#
        #file = 'Q' + str(file).split('Q')[1].split(']')[0]
        file = file.title(as_link=False)
        pywikibot.output(file)
        file = 'P31'
        loggg(line , file)
    #---
    if not item:
        if 'cebwiki' in item.sitelinks:
            title = item.sitelinks['cebwiki']
            #pywikibot.output(title)
            if title !='' :
                page = pywikibot.Page(cebwiki, title)
                pagetitle = page.title(as_link=False)
                pywikibot.output( '**<<lightyellow>> found cebwiki: "%s" in item : %s' % ( title ,  item.title()  ) )
                if page :
                    newupdate.ISRE_Page_Item(page, pagetitle, item)
#---
def NewFindWork(item):
    q = item.title(as_link=False)
    #pywikibot.output( '**<<lightyellow>> NewFindWork:' )
    #---
    findP17 = False
    if item:
        if 'cebwiki' in item.sitelinks:
            title = item.sitelinks['cebwiki']
            #pywikibot.output(title)
            if title !='' :
                page = pywikibot.Page(cebwiki, title)
                pagetitle = page.title(as_link=False)
                pywikibot.output( '**<<lightyellow>> found cebwiki: "%s" in item : %s' % ( title ,  item.title()  ) )
                if page :
                    templatesWithParams = page.templatesWithParams()
                    findP17 = newupdate.find_P17_templatee(templatesWithParams , 'NONONO')
                    newupdate.ISRE_Page_Item(page, pagetitle, item)
    #---
    P31 = Get_P_API( q , 'P31')
    if not findP17:
        findP17 = Get_P_API( q , 'P17')
    #---
    line = q
    if P31:
        #pywikibot.output(P31)       
        file = P31 
        if findP17:
            line = q + '\t' + findP17
        loggg(line , file)
    #---
# finished to Q30511616
def WorkWithWikidata():
    start = 511000
    end   = 1000000
    #---
    if len(sys.argv) > 2:
        start = sys.argv[1]
        end   = sys.argv[2]
    #---
    #start = 1 in sys.argv and sys.argv[1] or 0
    #end   = 2 in sys.argv and sys.argv[2] or 3000000
    num   = 0
    start = int(start) + 30000000
    end = int(end) + 30000000
    list  = range(start , end)
    lenth = len(list)
    #---
    pywikibot.output( '**<<lightyellow>> WorkWithWikidata in %d items (%d,%d)'  % (lenth , start  ,end) )
    #list = range(511000, 3000000)
    #---
    #list = range(511000, 311550)
    
    #for arg in range(30511616, 31000000):
    for arg in list:
        Ca = False
        arg = arg + 30000000
        qitem  = 'Q%d' % arg
        item = pywikibot.ItemPage(repo,qitem.strip())
        if (not(item.isRedirectPage())):
            if item.exists():
                item.get(get_redirect=True)
                Ca = True
                #yield wditem
                num += 1
        #---
        if Ca:
            pywikibot.output( '*<<lightred>> >%d/%d qitem "%s" :' % ( num , lenth , qitem ) )
            NewFindWork(item)
        else:
        #except:
            #pywikibot.output( '*<<lightred>> >%d error with page "%s" < :' % ( num , title ) )
            pass
#---
def Main_Test():
    pywikibot.output( '**<<lightyellow>> Main_Test:')
    TestTitle = 'Agnettahågan'
    #---
JlobalFileFloder = "cebnew/"  
#JlobalFileFloder = "ye/"
#---
MainTest = False#False#True
#---
if __name__ == "__main__":
    if MainTest:
        Main_Test()
    else:
        #mainwithcat()
        WorkWithWikidata()
        
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import urllib
import json
import time
import codecs
from API.maindir import main_dir
import pywikibot
#import pwb
import re
import string
#---
import sys
#---
#wikidatasite=pywikibot.Site('wikidata','wikidata') 
#repo = wikidatasite.data_repository()
#---
def getwditem(title):
    ceb = pywikibot.Site("ceb", "wikipedia") 
    EngPage = pywikibot.Page(ceb, title)
    try:
        item = pywikibot.ItemPage.fromPage(EngPage)
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        #pywikibot.output('*error when item.get() "%s"' % title)
        return False
#---
import new
def ssssssssssss( page , file , CategoryTableNew):
    #---
    pagetitle = page.title(as_link=False)
    item = getwditem(pagetitle)                                         #ايجاد عنصر ويكي بيانات للصفحة
    #---  
    if item:    
        pywikibot.output("* found item: " + item.title() )
    else:
        pywikibot.output("* no item: " )
        text = page.text
        geonames = ''
        pat =  'geonames\s*=\s*(.*)\n'
        OtherName =  re.compile( pat )
        na = OtherName.findall(text)
        if na:
            geonames = na[0].strip()
            p31code = CategoryTableNew[file]['item']
            if geonames !='':
                new.CreateNewItem(geonames, p31code , page)
            else:
                pywikibot.output("*no geonames :" + str(geonames) )
        #else:
            #pywikibot.output("*don't found template: " + str(TargetTemplates) )
#---
def main1(file , CategoryTableNew , nu):
        text = ''
        try:
            with codecs.open( "items/category/" + file + ".log.csv", "r", encoding="utf-8") as logFil:
                text = logFil.read()
                logFil.close()
        except:
            text = ''
            pywikibot.output( '*<<lightblue>> no file')
        #---
        pywikibot.output( '*<<lightblue>> >%d/%d work for file: "%s" :' % ( nu , len(CategoryTableNew.keys()) , file ) )
        if text !='':
            lines = text.split('\n')
            lenth = len(lines)
            page_num = 0
            for page in lines:
                if page !='':
                    page_num += 1
                    title = re.sub( file + '\s*', '' , page)
                    title = title.strip()
                    cebcite = pywikibot.Site("ceb", "wikipedia") 
                    cebPage = pywikibot.Page(cebcite, title)
                    if cebPage:
                        pywikibot.output( '*<<lightred>> >%d/%d page "%s" :' % ( page_num , lenth , title ) )
                        ssssssssssss( cebPage , file , CategoryTableNew)
                    else:
                        pywikibot.output( '*<<lightred>> >%d/%d error with page "%s" < :' % ( page_num , lenth , title ) )
#---
def main():
    from categoryNew import CategoryTableNew#ContriesNew
    nu = 0
    if sys.argv and len(sys.argv) > 1 :
        pywikibot.output(sys.argv)
        if sys.argv[1] in CategoryTableNew:
            main1(sys.argv[1] , CategoryTableNew , nu)
        else:
            pywikibot.output( ' %s not in CategoryTableNew. ' % sys.argv[1])
    else:
        for file in CategoryTableNew.keys():
                nu += 1
                #if file not in ['L.PRK' , 'T.MT' , 'S.DAM']:
                main1(file , CategoryTableNew , nu)
#---
if __name__ == "__main__":
    main()
#---
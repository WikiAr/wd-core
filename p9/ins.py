#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات
in sports
"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json as JJson
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
import urllib.request
import urllib.parse

#---
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
from API import himoAPI
#---
#from item_table import itemTable
itemTable = {}
#---
#from type.cate_type import *
#from type.cate_type import pop_start
#from type.cate_type import pop_format

#from type.cate_P17 import ALL_P17
#from type.cate_P17 import USA_P17
from type.cate_P17 import *
#---
#himo = {}
#himo['pop_start'] = pop_start
#himo['pop_format'] = pop_format
#himo['ALL_P17'] = ALL_P17
#himo['USA_P17'] = USA_P17
#---
def log22(t , ff):
    form = t + '\n'
    with codecs.open(ff, "a", encoding="utf-8") as logfile:
      try:
            logfile.write(form)
      except :
            pywikibot.output("Error writing")
#---
def log(tt, file):
    type = {
        'done' : 'donelist'  
        , 'falsecategory' : 'False_Categories' 
    }
    form = '%s["%s"] = ""\n' % ( type[file] , tt )
    pywikibot.output(form)
    with codecs.open("p971/file/" + file + ".py", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(str(form))
      except:
            pywikibot.output("Error writing")
#---
def makejson(property, numeric):
    #---
    if numeric !='':
        numeric = re.sub('Q','',numeric)
        Q = 'Q' + numeric#          
        Pro = {"mainsnak": {
                    "snaktype": "value",
                    "property": property,
                    "datavalue": {
                        "value": {
                            "entity-type": "item",
                            "numeric-id": numeric,
                            "id": Q
                        },
                        "type": "wikibase-entityid"
                    },
                    "datatype": "wikibase-item"
                },
                "type": "statement",
                "rank": "normal"
            }
        #---
        return Pro
#---
tita_Q = {
    'in sports' : { 'Q': 'Q349' , 'priff' : 'الرياضة في' }
    }
#---
def MakeNew(tit,category, year_q , Contry_q , arlabel):
    js = {}
    data = {}
    data['sitelinks'] = {}
    data['claims'] = {}
    data['claims']['P31'] = [makejson('P31', 'Q4167836')]
    #data['claims']['P971'] = [makejson('P971', Contry_q) , makejson('P971', year_q)]
    data['labels'] = {}
    data['sitelinks']['enwiki'] = {'site' : 'enwiki' , 'title': category}
    #---
    if arlabel != '':
        data['labels']['ar'] = {'language' : 'ar' , 'value': arlabel}
    #---
    data['labels']['en'] = {'language' : 'en' , 'value': category}
    summary = 'Bot: New item from [[w:en:%s|enwiki]].' % category
    sao = himoAPI.New_API22(data, summary)
    if 'success' in sao:
        pywikibot.output('<<lightgreen>> ** %s true. ' % summary )
        #pywikibot.output(sao)
        #try:
        js = JJson.loads(sao)
        #except:
            #pywikibot.output('Error downloading SPARQL? Malformatted JSON? Skiping\n')
        if "entity" in js and "id" in js["entity"]:
            Qid = js["entity"]['id']
            pywikibot.output(' new item is:"%s" .' % Qid)
            #himoAPI.Claim_API2(Qid , 'P31' , 'Q4167836')
            if year_q != '':
                himoAPI.Claim_API2(Qid , 'P971' , year_q)
                #time.sleep(0.5)
            else:
                pywikibot.output(' year_q is:"%s" .' % year_q)
            #---
            if year_q != '':
                himoAPI.Claim_API2(Qid , 'P971' , Contry_q)
                #time.sleep(0.5)             
            else:
                pywikibot.output(' Contry_q is:"%s" .' % Contry_q)
            #---
            if tita_Q[tit]['Q'] != '':
                himoAPI.Claim_API2(Qid , 'P971' , tita_Q[tit]['Q'])
                #time.sleep(0.5)             
            else:
                pywikibot.output(' tita_Q is:"%s" .' % tita_Q[tit]['Q'])
            #---
    else:
        pywikibot.output(sao)
#---
def getwditem(page):
    #encite = pywikibot.Site("en", "wikipedia") 
    #EngPage = pywikibot.Page(encite, title)
    #item = ''
    #---
    try:
        #if title in itemTable :
            #item = pywikibot.ItemPage(repo, itemTable[title])
        #else:
        item = pywikibot.ItemPage.fromPage(page)
        #---
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        pywikibot.output('*error when item.get() "%s"' % page.title(as_link=False)   )   
        return False
#---
def check(q, property , claims , id ):#, checklist
    #skiptable = ['Q215627' , 'Q19660746' , 'Q18658526' , 'Q1322263' ,'Q12131650' ]
    #for x in P971Table:
        #skiptable.append(P971Table[x]['id'])
    #---
    NoClaim = True
    if property in claims:
        #pywikibot.output('find ' + property)
        for claim in claims[property]:
            claim = claim.toJSON()
            va = claim['mainsnak']["datavalue"]
            if ('value' in va) and ('numeric-id' in va['value']):
                q_value = 'Q' + str(va['value']['numeric-id'])
                if q_value == id:
                    pywikibot.output('q_value == id "%s"' % id)
                    NoClaim = False
                #elif q_value in checklist :
                    #pywikibot.output('q_value in checklist ' + str(q_value))
                #elif q_value in skiptable:
                    #pywikibot.output('q_value in skiptable ')
                #else:
                    #pywikibot.output('%s: q_value "%s" != id "%s"' % ( property , q_value, year_q ))
                    #log_duplict(q,property,q_value,id)
                    #NoClaim = False
    return NoClaim
#---
def Find_Add_Claims(tit, item , property, year_q , Contry_q , arlabel):   
    q = item.title(as_link=False)
    #---
    claims = item.claims
    labels = item.labels
    tii_Q = tita_Q[tit]['Q']
    #checklist = [year_q , Contry_q , tii_Q]
    if arlabel != '':
        if not 'ar' in labels:
            himoAPI.Labels_API( q, arlabel , 'ar'  , False)
        else:
            lab = labels["ar"]
            labtest = re.sub( "تصنيف\:\d+\s*في\s*الرياضة" , "" , lab)
            if labtest == '':
                pywikibot.output( 'repalce lab "%s" by "%s"' % (lab ,arlabel ) )
                himoAPI.Labels_API( q, arlabel , 'ar'  , False)
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    if year_q != '':
        NoClaim = check(q, property , claims ,year_q)
        if NoClaim:
            himoAPI.Claim_API2(q , property , year_q) 
    else:
        pywikibot.output(' year_q is:"%s" .' % year_q)
    #---
    if Contry_q != '':
        NoClaim2 = check(q, property , claims , Contry_q )#,  checklist)
        if NoClaim2:
            himoAPI.Claim_API2(q , property , Contry_q)  
    else:
        pywikibot.output(' Contry_q is:"%s" .' % Contry_q)
    #---
    if tii_Q != '':
        NoClaim = check(q, property , claims ,tii_Q)#,  checklist)
        if NoClaim:
            himoAPI.Claim_API2(q , property , tii_Q) 
    else:
        pywikibot.output(' tii_Q is:"%s" .' % tii_Q)
#---
def start_work(tit, cat_page , year , Contry ):#year , Contry )
    category = cat_page.title(asLink = False)
    #---
    if year['ar'] != '' and Contry['ar'] != '' and tita_Q[tit]['priff'] != '' :
        arlabel = "تصنيف:" + year["ar"] + " " + tita_Q[tit]['priff'] + " " + Contry["ar"]
    else:
        arlabel = ""
        #pywikibot.output('<<lightred>>>%s: find empty category year:"%s".' % (Contry['ar'] , year['ar'] ))
    #---
    #if year["Q"] in himo['pop_format']:
        #qq = year["Q"]
        #arlabel = re.sub('~' , Contry["ar"] , himo['pop_format'][qq])
    #---
    pywikibot.output( 'a<<lightblue>>>%s:,ar:"%s" ,cat:"%s"' % (year['ar'] , arlabel , category) )
    #---
    year_q = year['Q']
    Contry_q = Contry['Q']
    #---
    pywikibot.output('<<lightgreen>>>a%s:  cat_page : "%s", ar:"%s"' % (year['ar'], category , arlabel ))
    item = getwditem(cat_page)
    if item:
        pywikibot.output('>a%s: find item:"%s".' % (year['ar'] , item.title()) )
        Find_Add_Claims( tit, item , 'P971' , year_q , Contry_q , arlabel)
    else:
        pywikibot.output('>a%s: no item for :%s' % ( category , year['ar']) )
        MakeNew(tit,category, year_q , Contry_q , arlabel)
#---
#from falsecategory import False_Categories
#---
def work(tit, category , year , Contry ):
    #if not category in False_Categories:
    if category:
        encite = pywikibot.Site("en", "wikipedia") 
        cat_page = pywikibot.Page(encite, category)
        #---
        if cat_page and cat_page.exists():
            start_work(tit, cat_page , year , Contry )
        else:
            pywikibot.output('<<lightred>>>A %s: cand find page for:"%s".' % (year['ar'] , category  ))
            #log(category , 'falsecategory')
    else:
        pywikibot.output('<<lightred>>> category %s: already in False_Categories' % category)
#---
from type.cate_type import *   #years__#decade__#century__#
#---
YDC_C = years__
#for toad in [decade__ , century__]:
    #for ci in toad:
        #YDC_C[ci] = toad[ci]
#---
from list.in_sport import in_sports
#---
in_sports1 = [
    "1910 sports in California",
    "2020_in_sports_in_Florida",
    ]
#---
tita = {
    'in sports' : in_sports
    }
#---
def yemen(tit , tittable):
    num = 0
    pywikibot.output( 'start with "%s":' % tit)
    lenth =  len(tittable) 
    tito = ' %s in ' % tit
    for category in tittable:
        num += 1
        category = re.sub("_" , " " , category)
        if category.find(tito) != -1:
            year = category.split(tito)[0]
            year = year + ' in'
            contry = category.split(tito)[1]
            CAO = True
            if category != '':
            #if gov not in donelist:
                if not year in YDC_C:
                    pywikibot.output( 'year "%s" not in YDC_C' % year)
                    CAO = False
                    log22(year , 'p971/falseyears.log.csv')
                if not contry in P17_final: 
                    pywikibot.output( 'contry "%s" not in P17_final' % contry)
                    CAO = False
                    log22(contry , 'p971/falsecontry.log.csv')
                #---
                category = 'Category:' + category
                pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( num , lenth , category) )
                if CAO:
                    #pywikibot.output( '<<lightblue>> a %d/%d cat:"%s":' % ( num , lenth,  category) )
                    work(tit, category , YDC_C[year] , P17_final[contry] )
                #---
                #log(gov , 'done')
            #else:
                #pywikibot.output( '%d/%d gov "%s" already in donelist.' % ( gov_num ,lenth , gov) )
#---
'''
"python pwb.py p971/caten t:new d:c",
"python pwb.py p971/caten t:new d:d",
"python pwb.py p971/caten t:new d:y",##
"python pwb.py p971/caten t:new d:new",
"python pwb.py p971/caten t:new d:new2",
"python pwb.py p971/caten t:new d:a",
'''
#---
def main():
    tit = 'in sports'
    '''for value in sys.argv:
        #arg, sep, value = arg.partition(':')
        if value == 'd':
            tit = 'disestablishments'
        elif value == 'e':
            tit = 'establishments'
    #---'''
    print('tit: %s' % tit)
    if not tit in tita:
        print('tit: %s not in tita' % tit)
    else:
        yemen(tit , tita[tit])
#---
if __name__ == "__main__":
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات
disestablishments
establishments

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
# start of himoAPI.py file
from API import himoAPI

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#himoAPI.Merge( q1, q2 )
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
    'disestablishments' : { 'Q': 'Q37621071' , 'priff' : 'انحلالات' }
    ,'establishments' : { 'Q': 'Q3406134' , 'priff' : 'تأسيسات' }  # تاريخ التأسيس
    }
#---
def MakeNew(category, pop_q , gov_q , arlabel):
    js = {}
    data = {}
    data['sitelinks'] = {}
    data['claims'] = {}
    data['claims']['P31'] = [makejson('P31', 'Q4167836')]
    #data['claims']['P971'] = [makejson('P971', gov_q) , makejson('P971', pop_q)]
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
            if pop_q != '':
                himoAPI.Claim_API2(Qid , 'P971' , pop_q)
                #time.sleep(0.5)
            else:
                pywikibot.output(' pop_q is:"%s" .' % pop_q)
            #---
            if pop_q != '':
                himoAPI.Claim_API2(Qid , 'P971' , gov_q)
                #time.sleep(0.5)             
            else:
                pywikibot.output(' gov_q is:"%s" .' % gov_q)
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
                    #pywikibot.output('%s: q_value "%s" != id "%s"' % ( property , q_value, pop_q ))
                    #log_duplict(q,property,q_value,id)
                    #NoClaim = False
    return NoClaim
#---
def Find_Add_Claims(tit, item , property, pop_q , gov_q , arlabel):   
    q = item.title(as_link=False)
    #---
    claims = item.claims
    labels = item.labels
    tii_Q = tita_Q[tit]['Q']
    #checklist = [pop_q , gov_q , tii_Q]
    if arlabel != '':
        if not 'ar' in labels:
            himoAPI.Labels_API( q, arlabel , 'ar'  , False)
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    if pop_q != '':
        NoClaim = check(q, property , claims ,pop_q)
        if NoClaim:
            himoAPI.Claim_API2(q , property , pop_q) 
    else:
        pywikibot.output(' pop_q is:"%s" .' % pop_q)
    #---
    if gov_q != '':
        NoClaim2 = check(q, property , claims , gov_q )#,  checklist)
        if NoClaim2:
            himoAPI.Claim_API2(q , property , gov_q)  
    else:
        pywikibot.output(' gov_q is:"%s" .' % gov_q)
    #---
    if tii_Q != '':
        NoClaim = check(q, property , claims ,tii_Q)#,  checklist)
        if NoClaim:
            himoAPI.Claim_API2(q , property , tii_Q) 
    else:
        pywikibot.output(' tii_Q is:"%s" .' % tii_Q)
    #---
head = '{|\n|-\n!city !! CityItem !! Death !! Death_id !! Birth !! Birth_id !! People !! People_id'
#---
def start_work(tit, cat_page , pop , gov ):
    category = cat_page.title(asLink = False)
    #---
    if pop['ar'] != '' and gov['ar'] != '' and tita_Q[tit]['priff'] != '' :
        arlabel = "تصنيف:" + tita_Q[tit]['priff'] + ' ' + pop["ar"] + " " + gov["ar"]
    else:
        arlabel = ""
        #pywikibot.output('<<lightred>>>%s: find empty category pop:"%s".' % (gov['ar'] , pop['ar'] ))
    #---
    #if pop["Q"] in himo['pop_format']:
        #qq = pop["Q"]
        #arlabel = re.sub('~' , gov["ar"] , himo['pop_format'][qq])
    #---
    pywikibot.output( 'a<<lightblue>>>%s:,ar:"%s" ,cat:"%s"' % (pop['ar'] , arlabel , category) )
    #---
    pop_q = pop['Q']
    gov_q = gov['Q']
    #---
    pywikibot.output('<<lightred>>>a%s:  cat_page : "%s", ar:"%s"' % (pop['ar'], category , arlabel ))
    item = getwditem(cat_page)
    if item:
        pywikibot.output('>a%s: find item:"%s".' % (pop['ar'] , item.title()) )
        Find_Add_Claims( tit, item , 'P971' , pop_q , gov_q , arlabel)
    else:
        pywikibot.output('>a%s: no item for :%s' % ( category , pop['ar']) )
        #MakeNew(category, pop_q , gov_q , arlabel)
#---
#from falsecategory import False_Categories
#---
def work(tit, category , pop , gov ):
    #if not category in False_Categories:
    if category:
        encite = pywikibot.Site("en", "wikipedia") 
        cat_page = pywikibot.Page(encite, category)
        #---
        if cat_page and cat_page.exists():
            start_work(tit, cat_page , pop , gov )
        else:
            pywikibot.output('<<lightred>>>A %s: cand find page for:"%s".' % (pop['ar'] , category  ))
            #log(category , 'falsecategory')
    else:
        pywikibot.output('<<lightred>>> category %s: already in False_Categories' % category)
#---
def test():
    pop_num = 0
    gover = ["Ibb (lalawigan)"]
    num = 0
    lenth2 = len(gov) * len(pop_start.keys() ) 
    for gov in gover:
        for pop in pop_start:
            num += 1
            pop_num += 1
            if pop != '' :
                category = 'Category:'+ pop + ' '  + gov
                pywikibot.output( '<<lightblue>>>a%s: %d/%d/%d cat:"%s" :' % (pop['ar'] , pop_num , num ,lenth2,  category) )
                work(category , pop_start[pop] , goverment[gov] )
#---
from type.cate_type import *   #years__#decade__#century__#
#---
YDC_C = years__
for toad in [decade__ , century__ , millennium__]:
    for ci in toad:
        YDC_C[ci] = toad[ci]
#---
from list.distype import disestablishments
from list.estype import establishments
#from list.es2type import establishments
#---
disestablishments = [
    "1000_disestablishments_in_Europe",
    "1000_disestablishments_in_South_America",
    "1000s_disestablishments_in_Asia",
    "1000s_disestablishments_in_Europe",
    "1000s_disestablishments_in_South_America",
    "1002_disestablishments_in_Asia",
    "1003_disestablishments_in_Asia",
    "1006_disestablishments_in_Asia",
    "1006_disestablishments_in_Europe",
    "1008_disestablishments_in_Asia",
    "100s_disestablishments_in_Europe",
    "100s_disestablishments_in_the_Roman_Empire",
    "1010s_disestablishments_in_Africa",
    "1010s_disestablishments_in_Asia",
    "1010s_disestablishments_in_Europe",
    "1010s_disestablishments_in_Sri_Lanka",
    "1011_disestablishments_in_Europe",
    "1017_disestablishments_in_Asia",
    "1017_disestablishments_in_Sri_Lanka",
    ]
#---
establishments_ = [
    "1991_establishments_in_Yemen",
    "00s_establishments_in_the_Roman_Empire",
    "0s_establishments_in_Europe",
    "0s_establishments_in_the_Roman_Empire",
    "1000_establishments_in_Asia",
    "1000_establishments_in_England",
    "1000_establishments_in_Europe",
    "1000_establishments_in_France",
    "1000_establishments_in_Hungary",
    "1000_establishments_in_India",
    "1000_establishments_in_Japan",
    "1000_establishments_in_Spain",
    "1000s_establishments_in_Africa",
    "1000s_establishments_in_Asia",
    "1000s_establishments_in_England",
    "1000s_establishments_in_Europe",
    "1000s_establishments_in_France",
    "1000s_establishments_in_Hungary",
    "1000s_establishments_in_India",
    "1000s_establishments_in_Italy",
    "1000s_establishments_in_Japan",
    "1000s_establishments_in_Spain",
    "1000s_establishments_in_Vietnam",
    "1000s_establishments_in_the_Holy_Roman_Empire",
    ]
#---
tita = {
    'disestablishments' : disestablishments
    ,'establishments' : establishments
    }
#---
def yemen(tit , tittable):
    num = 0
    pywikibot.output( 'start with "%s":' % tit)
    lenth =  len(tittable)  
    tito = ' %s in ' % tit
    keys = tittable
    keys.sort()
    for category in keys:
        num += 1
        category = re.sub("_" , " " , category)
        pywikibot.output( 'category "%s":' % category)
        if category.find(tito) != -1 :
            year = category.split(tito)[0]
            year = re.sub("-century" , " century" , year)
            year = re.sub("-millennium" , " millennium" , year)
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
the_new_contry = {#بلدان جديدة
    "python pwb.py p971/caten t:new d:c",
    "python pwb.py p971/caten t:new d:d",
    "python pwb.py p971/caten t:new d:y",##
    "python pwb.py p971/caten t:new d:new",
    "python pwb.py p971/caten t:new d:new2",
    "python pwb.py p971/caten t:new d:a",
    }
#---
def main():
    tit = 'establishments'
    for value in sys.argv:
        #arg, sep, value = arg.partition(':')
        if value == 'd':
            tit = 'disestablishments'
        elif value == 'e':
            tit = 'establishments'
    #---
    print('tit: %s' % tit)
    if not tit in tita:
        print('tit: %s not in tita' % tit)
    else:
        yemen(tit , tita[tit])
#---
if __name__ == "__main__":
    main()
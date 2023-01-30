#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


العمل مع ثلاثة ملفات
ALL_Years
ALL_Centry
ALL_decades

"""
#
# (C) Ibrahem Qasim, 2022
#
#


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
def getwditem(page):
    try:
        item = pywikibot.ItemPage.fromPage(page)
        #---
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        #pywikibot.output('*error when item.get() "%s"' % title)
        return False
#---
def check2(q, property , claims , id  , art):#, checklist
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
                    pywikibot.output('value ar:%s == id "%s"' % (art , id) )
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
    tii_Q = tit['Q']
    if arlabel != '':
        if not 'ar' in labels:
            #himoAPI.Labels_API( q, arlabel , 'ar'  , False)
            t = '%s\tLar\t"%s"' % ( q , arlabel)
            #log22(t , 'p971/labels_1.log.csv')
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    Xaso = []
    for faso in [tit, pop_q , gov_q]:
        if faso:
            if 'Q' in faso:
                Xaso.append(faso)
            else:
                pywikibot.output('Cant find "Q" in faso ar:%s' % faso.get('ar') )
    #---
    for tt in Xaso:
        art = tt.get('ar')
        ttq = tt['Q']
        #---
        if type(ttq ) != list:
            ttq = [ttq]
        #---
        for qid in ttq:
            if qid and qid != '':
                if type(qid) != str:
                    pywikibot.output('type(qid) == ' + str( type(qid) )  )
                    pywikibot.output(qid)
                NoClaim3 = check2(q, property , claims , qid , art )#,  checklist)
                if NoClaim3:
                    himoAPI.Claim_API2(q , property , qid)  
#---
def start_work(tit, cat_page , year_pop , gov , arlabel ):
    category = cat_page.title(asLink = False)
    #---
    #pywikibot.output('<<lightgreen>>>a%s:  cat_page : "%s", ar:"%s"' % (year_pop['ar'], category , arlabel ))
    item = getwditem(cat_page)
    if item:
        pywikibot.output('>a%s: find item:"%s".' % (year_pop.get('ar') , item.title()) )
        Find_Add_Claims( tit, item , 'P971' , year_pop , gov , arlabel)
    else:
        pywikibot.output('>a%s: no item for :%s' % ( category , year_pop.get('ar')) )
#---
False_YDC_C = []
False_YDC_P17 = []
encite = pywikibot.Site("en", "wikipedia") 
#---
def New_Work2(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel):
    CAO_Y = True
    CAO_C = True
    if category != '':
        #---
        if not year in YDC_C:
            CAO_Y = False
            if not year in False_YDC_C:
                #pywikibot.output( '<<lightyellow>>>> %d/%d year "%s" not in YDC_C' % ( num , lenth , year) )
                #log22(year , 'p971/falseyears_1.log.csv')
                False_YDC_C.append(year)
        #---
        contry2 = contry
        if not contry in YDC_P17: 
            contry2 = re.sub('-' , ' ' , contry)
        if not contry2 in YDC_P17: 
            if not contry2 in False_YDC_P17:
                pywikibot.output( '<<lightyellow>>>> %d/%d contry2 "%s" not in YDC_P17' % ( num , lenth , contry2) )
                #log22(contry2 , 'p971/falsecontry_1.log.csv')
                False_YDC_P17.append(contry2)
            CAO_C = False
        else:
            contry = contry2
        #---
        category = 'Category:' + category
        cat_page = pywikibot.Page(encite, category)
        if cat_page and cat_page.exists():
            pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( num , lenth , category) )
            if CAO_C and CAO_Y:
                #pywikibot.output( '<<lightblue>> a %d/%d cat:"%s":' % ( num , lenth,  category) )
                #---
                start_work(tit, cat_page , YDC_C[year] , YDC_P17[contry]  , arlabel)
            #elif year in YDC_C:
            elif CAO_Y:
                #pywikibot.output( '<<lightblue>> a %d/%d cat:"%s":' % ( num , lenth,  category) )
                start_work(tit, cat_page , YDC_C[year] , False  , arlabel)
            #elif contry in YDC_P17:
            elif CAO_C:
                start_work(tit, cat_page , False , YDC_P17[contry]   , arlabel)
            elif tit:
                pywikibot.output('<<lightred>>>Just tit "%s".' % category )
                start_work(tit, cat_page , False , False  , arlabel)
        else:
            pywikibot.output('<<lightred>>>A %s: cand find page for:"%s".' % (YDC_C[year]['ar'] , category  ))
#---
def yemen(tittable):
    num = 0
    pywikibot.output( 'start with "%s":')
    lenth =  len(tittable) 
    #from done2 import donelist
    tit = ''
    tito = ' in '
    #mha = islahvillage
    for category in tittable:
        num += 1
        #category = re.sub(' ' , '_' , category)
        #pywikibot.output( '<<lightyellow>>>> category: %s ' % category )
        year = category.split(tito)[0]
        year = year + ' in'
        contry = category.split(tito)[1]
        contry = contry.lower()
        New_Work(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth)
                    #log(category , 'falsecategory')
            #else:
                #pywikibot.output('<<lightred>>> category %s: already in False_Categories' % category)
#---
if __name__ == "__main__":
    main()
    #print(type(['ddf']))
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
        #pywikibot.output('*error when item.get() "%s"' % title)
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
                    pywikibot.output('value == id "%s"' % id)
                    NoClaim = False
    return NoClaim
#---
def Find_Add_Claims_2018(tit, item , property, Qlist , arlabel):   
    q = item.title(as_link=False)
    #---
    claims = item.claims
    labels = item.labels
    #tii_Q = tita_Q[tit]['Q']
    #checklist = [pop_q , gov_q , tii_Q]
    if arlabel != '':
        if not 'ar' in labels:
            #himoAPI.Labels_API( q, arlabel , 'ar'  , False)
            t = '%s\tLar\t"%s"' % ( q , arlabel)
            log22(t , 'p971/labels_1.log.csv')
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    for tt in Qlist:
        if type(tt) == list:
            print('type(tt) == list')
            for qid in tt:
                if qid != '':
                    NoClaim3 = check(q, property , claims , qid )#,  checklist)
                    if NoClaim3 and qid:
                        himoAPI.Claim_API2(q , property , qid)  
        else:
            if tt != '':
                NoClaim = check(q, property , claims ,tt)
                if NoClaim:
                    himoAPI.Claim_API2(q , property , tt) 
#---
def start_work_2018(tit, cat_page , Qlist , arlabel):#(tit, cat_page , year_pop , gov , arlabel ):
    category = cat_page.title(asLink = False)
    gov_q = ''
    pop_q = ''
    pop_ar = ''
    #---
    #pywikibot.output('<<lightgreen>>>a%s:  cat_page : "%s", ar:"%s"' % (year_pop['ar'], category , arlabel ))
    item = getwditem(cat_page)
    if item:
        pywikibot.output('>a%s: find item:"%s".' % (pop_ar , item.title()) )
        Find_Add_Claims_2018( tit, item , 'P971' , Qlist , arlabel)
    else:
        pywikibot.output('>a%s: no item for :%s' % ( category , pop_ar) )
#---
False_YDC_C = []
False_YDC_P17 = []
encite = pywikibot.Site("en", "wikipedia") 
#---
def Work_2018(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel):
    Qlist = []
    CAO_C = True
    CAO_Y = True
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
                log22(contry2 , 'p971/falsecontry_1.log.csv')
                False_YDC_P17.append(contry2)
            CAO_C = False
        else:
            contry = contry2
        #---
        category = 'Category:' + category
        cat_page = pywikibot.Page(encite, category)
        if cat_page and cat_page.exists():
            pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( num , lenth , category) )
            if CAO_C:
                Qlist.append(YDC_P17[contry]['Q'])
                #pywikibot.output( '<<lightblue>> a %d/%d cat:"%s":' % ( num , lenth,  category) )
                #---
                #start_work(tit, cat_page , YDC_C[year] , YDC_P17[contry]  , arlabel)
            #elif year in YDC_C:
            if CAO_Y:
                Qlist.append(YDC_C[year]['Q'])
                #pywikibot.output( '<<lightblue>> a %d/%d cat:"%s":' % ( num , lenth,  category) )
                #start_work(tit, cat_page , YDC_C[year] , False  , arlabel)
            #elif contry in YDC_P17:
            if Qlist:
                start_work_2018(tit, cat_page , Qlist , arlabel)
        else:
            pywikibot.output('<<lightred>>>A %s: cand find page for:"%s".' % (YDC_C[year]['ar'] , category  ))
#---
if __name__ == "__main__":
    main()
    #print(type(['ddf']))
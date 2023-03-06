#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

طريقة البوت هذا مملة حيث أن الاحتمالات 70% خاطئة 

يقوم بتجربة جميع السنوات على كل بلد

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
#from API import himoAPI
from API import himoAPI_test as himoAPI
#---
#from item_table import itemTable
itemTable = {}
#---
from type.cate_type import *
#from type.cate_type import pop_start
#from type.cate_type import pop_format

#from type.cate_P17 import ALL_P17
#from type.cate_P17 import USA_P17
from type.cate_P17 import *
#---
himo = {}
himo['pop_start'] = pop_start
himo['pop_format'] = pop_format
himo['ALL_P17'] = ALL_P17
himo['USA_P17'] = USA_P17
#---
def log(tt, file):
    type = {
        'done' : 'donelist' , 'falsecategory' : 'False_Categories' , 
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
def check(q, property , claims , pop_q , gov_q):
    skiptable = ['Q215627' , 'Q19660746' , 'Q18658526' , 'Q1322263' ,'Q12131650' ]
    #for x in P971Table:
        #skiptable.append(P971Table[x]['id'])
    #---
    NoClaim = True
    if property in claims:
        pywikibot.output('find ' + property)
        for claim in claims[property]:
            claim = claim.toJSON()
            va = claim['mainsnak']["datavalue"]
            if ('value' in va) and ('numeric-id' in va['value']):
                q_value = 'Q' + str(va['value']['numeric-id'])
                if q_value == pop_q :
                    pywikibot.output('q_value == pop_q ' + str(q_value))
                    NoClaim = False
                elif q_value == gov_q:
                    pywikibot.output('q_value == gov_q ' + str(gov_q))
                elif q_value in skiptable:
                    pywikibot.output('q_value in skiptable ' + str(gov_q))
                else:
                    pywikibot.output('%s: q_value "%s" != id "%s"' % ( property , q_value, pop_q ))
                    #log_duplict(q,property,q_value,id)
                    NoClaim = False
    return NoClaim
#---
def Find_Add_Claims(item , property, pop_q , gov_q , arlabel):   
    q = item.title(as_link=False)
    #---
    claims = item.claims
    labels = item.labels
    if arlabel != '':
        if not 'ar' in labels:
            himoAPI.Labels_API( q, arlabel , 'ar'  , False)
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    if pop_q != '':
        NoClaim = check(q, property , claims , pop_q , gov_q)
        if NoClaim:
            himoAPI.Claim_API2(q , property , pop_q) 
    else:
        pywikibot.output(' pop_q is:"%s" .' % pop_q)
    #---
    if gov_q != '':
        NoClaim2 = check(q, property , claims , gov_q , pop_q)
        if NoClaim2:
            himoAPI.Claim_API2(q , property , gov_q)  
    else:
        pywikibot.output(' gov_q is:"%s" .' % gov_q)
#---
def start_work(cat_page , pop , gov ):
    category = cat_page.title(asLink = False)
    #---
    if pop['ar'] != '' and gov['ar'] != '' :
        arlabel = "تصنيف:" + pop["ar"] + " " + gov["ar"]
        if gov['ar'] == 'حسب البلد':
            arlabel = re.sub( 'في حسب البلد' , 'حسب البلد' , arlabel)

        #if pop["ar"] == 'تاريخ طبيعي':
            #arlabel = 'تصنيف:تاريخ ' + gov["ar"] + ' الطبيعي'
    else:
        arlabel = ""
        #pywikibot.output('<<lightred>>>%s: find empty category pop:"%s".' % (gov['ar'] , pop['ar'] ))
    #---
    if pop["Q"] in himo['pop_format']:
        qq = pop["Q"]
        arlabel = re.sub('~' , gov["ar"] , himo['pop_format'][qq])
    #---
    pywikibot.output( '<<lightblue>>>a %s: , ar:"%s" :' % (pop['ar'] , arlabel) )
    #---
    pop_q = pop['Q']
    gov_q = gov['Q']
    #---
    #pywikibot.output('<<lightgreen>>>a%s:  cat_page : "%s", ar:"%s"' % (pop['ar'], category , arlabel ))
    item = getwditem(cat_page)
    if item:
        pywikibot.output('>a%s: find item:"%s".' % (pop['ar'] , item.title()) )
        Find_Add_Claims( item , 'P971' , pop_q , gov_q , arlabel)
    else:
        pywikibot.output('>a%s: no item for :%s' % ( category , pop['ar']) )
        #MakeNew(category, pop_q , gov_q , arlabel)
#---
#from falsecategory import False_Categories
#---
def work(category , pop , gov ):
    #if not category in False_Categories:
    if category:
        encite = pywikibot.Site("en", "wikipedia") 
        cat_page = pywikibot.Page(encite, category)
        #---
        if cat_page and cat_page.exists():
            start_work(cat_page , pop , gov )
        else:
            pywikibot.output('<<lightred>>>A %s: cand find page for:"%s".' % (pop['ar'] , category  ))
            log(category , 'falsecategory')
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
from list.ALL_decades import *   #ALL_Decade
from list.ALL_Years import *     #ALL_Year
from list.ALL_Centry import *    #ALL_Centries
#---
#YDC_C = ALL_Year
#for toad in [ALL_Decade , ALL_Centries]:
    #for ci in toad:
        #YDC_C.append(ci)
#---
Main_Type = {
    'd' : ALL_Decade
    ,'y' : ALL_Year
    ,'c' : ALL_Centries
    #, 'ydc' : []#YDC_C
    }
#---
def D_Y_C(goverment , pop_start , type):
    pywikibot.output( 'start with type:"%s"' % type)
    num = 0
    pop_num = 0
    check = False
    if type in Main_Type:
        check = True
    #mha = islahvillage
    pop_st = pop_start#himo['pop_start']
    lenth2 = len(goverment) * len(pop_st.keys() ) 
    for pop in pop_st.keys():
        pop_num += 1
        gov_num = 0
        #if pop != '' :
        if pop != '' and pop_st[pop]['Q']  != '' :
            pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( pop_num , len(pop_st.keys()) , pop) )
            for gov in goverment.keys():
                gov_num += 1
                num += 1
                #if gov != '' :
                if gov != ''  and goverment[gov]['Q'] != '' :
                    tat = pop + ' '  + gov
                    category = 'Category:' + tat
                    #pywikibot.output( '<<lightblue>> a %d a %d a %d cat:"%s":' % ( num , pop_num , lenth2,  category) )
                    #pywikibot.output( '<<lightblue>> a %s: %d/%d/%d cat:"%s":' % (pop['ar'] , pop_num , num ,lenth2,  category) )
                    if check:
                        if tat in Main_Type[type]:
                            pywikibot.output( '<<lightblue>> a %d a %d a %d cat:"%s":' % ( num , pop_num , lenth2,  category) )
                            work(category , pop_st[pop] , goverment[gov] )
                    else:
                        pywikibot.output( '<<lightblue>> a %d a %d a %d cat:"%s":' % ( num , pop_num , lenth2,  category) )
                        work(category , pop_st[pop] , goverment[gov] )
        else:
            pop_num += len(pop_st.keys() ) 
            num += len(pop_st.keys() ) 
#---
import y
def yemen(goverment , pop_start):
    num = 0
    pop_num = 0
    pywikibot.output( 'start with ALL_P17:')
    #from done2 import donelist
    #mha = islahvillage
    pop_st = pop_start#himo['pop_start']
    lenth2 = len(goverment) * len(pop_st.keys() ) 
    for pop in pop_st.keys():
        pop_num += 1
        gov_num = 0
        if pop != '' :
        #if gov not in donelist:
            pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( pop_num , len(pop_st.keys()) , pop) )
            for gov in goverment.keys():
                gov_num += 1
                num += 1
                if gov:
                    #category = 'Category:'+ pop + ' '  + gov
                    category = pop + ' '  + gov
                    #---
                    if pop_st[pop]['ar'] != '' and goverment[gov]['ar'] != '' :
                        arlabel = "تصنيف:" + pop_st[pop]["ar"] + " " + goverment[gov]["ar"]
                        if goverment[gov]['ar'] == 'حسب البلد':
                            arlabel = re.sub( 'في حسب البلد' , 'حسب البلد' , arlabel)

                        #if pop_st[pop]["ar"] == 'تاريخ طبيعي':
                            #arlabel = 'تصنيف:تاريخ ' + goverment[gov]["ar"] + ' الطبيعي'
                    else:
                        arlabel = ""
                        #pywikibot.output('<<lightred>>>%s: find empty category pop:"%s".' % (goverment[gov]['ar'] , pop['ar'] ))
                    #---
                    #pywikibot.output( '<<lightblue>> a %d/%d/%d cat:"%s":' % ( pop_num , num ,lenth2,  category) )
                    y.New_Work('', category , pop , pop_st , gov , goverment , num , lenth2 , arlabel)
                    #pywikibot.output( '<<lightblue>> a %s: %d/%d/%d cat:"%s":' % (pop['ar'] , pop_num , num ,lenth2,  category) )
                    #work(category , pop_st[pop] , goverment[gov] )
            #log(gov , 'done')
        else:
            #pywikibot.output( '%d/%d gov "%s" already in donelist.' % ( gov_num , len(goverment) , gov) )
            pop_num += len(pop_st.keys() ) 
            num += len(pop_st.keys() ) 
#---
allcontry = {#كافة الدول
    #"python pwb.py p971/caten d:c",##
    #"python pwb.py p971/caten d:d",##
    "python pwb.py p971/caten d:y",##
    "python pwb.py p971/caten d:new",##
    "python pwb.py p971/caten d:new2",##
    #"python pwb.py p971/caten d:a",
    }
usa_statuse = { #ولايات أمريكا
    #"python pwb.py p971/caten t:usa d:c",
    "python pwb.py p971/caten t:usa d:d",
    "python pwb.py p971/caten t:usa d:y",##
    #"python pwb.py p971/caten t:usa d:new2",
    #"python pwb.py p971/caten t:usa d:new",
    "python pwb.py p971/caten t:usa d:a",
    }
the_new_contry = {#بلدان جديدة
    "python pwb.py p971/caten t:new d:c",
    "python pwb.py p971/caten t:new d:d",
    "python pwb.py p971/caten t:new d:y",##
    "python pwb.py p971/caten t:new d:new",
    "python pwb.py p971/caten t:new d:new2",
    "python pwb.py p971/caten t:new d:a",
    
    
    "python pwb.py p971/caten t:4 d:ny",
    }
#---
from type.yearnew import * 
def main():
    #goverment = USA_P17 #decade
    #values = {
    #'d' : { 'd' : decade__,'y': years__,'c': century__,'new': New_Pop, },
    #}
    himo['pop_start'] = pop_start
    sao = ALL_P17 #New_Pop
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        if arg =='d':
            if value == 'd':
                himo['pop_start'] = decade__
                print('d: decade')
            elif value == 'y':#
                himo['pop_start'] = years__new
                print('d: new years')#
            elif value == 'ny':#
                himo['pop_start'] = years__#
                print('d: years')
            elif value == 'm':
                himo['pop_start'] = millennium__
                print('d: millennium__')
            elif value == 'c':
                himo['pop_start'] = century__
                print('d: century')
            elif value == 'new':
                himo['pop_start'] = New_Pop
                print('d: New_Pop')
            elif value == 'new2':
                himo['pop_start'] = New_Pop2
                print('d: New_Pop2')
            else:
                himo['pop_start'] = pop_start
        #if arg =='a':
            #if value == 'new':
            #yemen(sao)
        if arg =='t':
            if value == 'usa':
                sao = USA_P17
                print('t: usa')
            elif value == 'new':
                sao = New_P17
            elif value == '4':
                sao = New_P174
                print('t: New_P174')
            else:
                sao = ALL_P17
    yemen(sao , himo['pop_start'])
#---
if __name__ == "__main__":
    #test()
    main()
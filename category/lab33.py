#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة تسميات ويكي بيانات بناءاً على مطابقة اسماء التصانيف

وحسب السنة

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json
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
import urllib
import urllib.request
import urllib.parse

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
# start of himoAPI.py file
from API import himoAPI_test as himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
def log(t , ff):
    #form = t + '\n'
    with codecs.open("category/"+ff+"", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(str(t))
      except :
            pywikibot.output("Error writing")
#---
from type.cate_type import pop_final_Without_Years as popstart
from type.cate_P17 import P17_final #P17_final#P17_final
from type.cate_P17 import USA_P17
from type.cate_type import pop_format
#---
priv = {
    'en': 'Category:' , 
    'ceb': 'Kategoriya:' , 
    'sv': 'Kategori:' , 
    'war': 'Kaarangay:' , 
}
#---
def ttt(p , cat , MainTab, wiki):
    if not 'itemLabel' in p:
        p['itemLabel'] = ''
    if p['title'] == p['itemLabel'] :
        p['itemLabel'] = ''
    #pywikibot.output( ' **<<lightred>> itemLabel: "%s" ,title: "%s" '  %  ( (p['itemLabel'] , p['title']) ))
    ar_year , en_year , ar_lab, en_lab='' , ''  , '' , '' 
    #---
    if re.sub('Q\d+' , '' , p['title']) == '':
        #pywikibot.output( ' **<<lightyellow>> title is Qid '  +  p['title'])
        p['title'] = ''
    if re.sub('Q\d+' , '' , p['itemLabel']) == '':
        #pywikibot.output( ' **<<lightyellow>> title is Qid '  +  p['title'])
        p['itemLabel'] = ''
    #---
    ar = re.sub('تصنيف\:' , '' , p['itemLabel'])
    #ar = re.sub(priv[wiki] + '\:' , '' , p['itemLabel'])
    ar = re.sub(priv[wiki] , '' , p['itemLabel'])
    en = re.sub('تصنيف\:' , '' , p['title'])
    #en = re.sub(priv[wiki] + '\:' , '' , p['title'])
    en = re.sub(priv[wiki]  , '' , p['title'])
    #pywikibot.output( ' ** ar:"%s" ,en:"%s" '  %  (ar , en ) )
    #---    
    re1 = re.compile('\d{4}\–\d{2}')
    en_te = re1.findall(p['title'])
    #---    
    if not en_te:
        re1 = re.compile('\d{4}\-\d{2}')       #سنة 2017-18
        en_te = re1.findall(p['title'])
        
    if not en_te:
        re1 = re.compile('\d{4}')      #سنة 2017
        en_te = re1.findall(p['title'])
        
    if not en_te:
        re1 = re.compile('\d{3}')      #سنة 201
        en_te = re1.findall(p['title'])
        
    if not en_te:
        re1 = re.compile('\d{2}')      #سنة 20
        en_te = re1.findall(p['title'])
        
    if not en_te:
        re1 = re.compile('\d{1}')      #سنة 20
        en_te = re1.findall(p['title'])
    #---
    if en_te:
        en_year = en_te[0]
        #pywikibot.output( ' **<<lightred>> itemLabel: en_te: "%s" ,p[title]: "%s"  '  %  (str(en_te) , p['title']  ) )
        p['en_year'] = en_year
        en_lab =  re.sub(en_year , '&&&&' , en).strip()
        if en_lab not in MainTab:
            MainTab[en_lab] = {'HasArabic': {} , 'NoArabic': {} , 'en_format' : '', 'ar_format' : []}# , 'items' : []}
            #MainTab[en_lab]['s'] = {'en_format' : '', 'ar_format' : [] , 'items' : [] }
        mai = MainTab[en_lab]
        #---
        #re1 = re.compile('(\d\d\d\d)$')
        en_format = re.sub( en_year , '&&&&' , p['title'])
        #mai['s']['en_format'] = en_format
        mai['en_format'] = en_format
        #---
        if p['itemLabel'] != '' :
            ar_te = re1.findall(p['itemLabel'])
            if ar_te:
                ar_year = ar_te[0]
                #ar_lab =  re.sub(ar_year , '' , ar).strip()
                #p['ar_lab'] = ar_lab
                ar_format = re.sub( ar_year , '&&&&' , p['itemLabel'])
                #if not ar_format in mai['s']['ar_format']:
                if not ar_format in mai['ar_format']:
                    #mai['s']['ar_format'].append(ar_format)
                    mai['ar_format'].append(ar_format)
                #---
                    # else:
                #pywikibot.output( ' **<<lightyellow>> ar_te in: '  +  p['itemLabel'])
        #else:
            #mai['s']['items'].append(p['item1'])
            #mai['items'].append(p['item1'])
        #---
        if ar_year != '' :
            if en_year !=  ar_year :
                p['ar_year'] = ar_year
        #---
        Q_item = p['item1']
        arabic = p['itemLabel']
        HasArabic  = mai['HasArabic']
        NoArabic   = mai['NoArabic']
        #---
        test = re.sub('[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , arabic)
        #if arabic != test:
        if p['itemLabel'] != '':
            #p['itemLabel'] = ''
            HasArabic[Q_item] = p
        else:
            NoArabic[Q_item] = p
        #---
        #line = '**'
        #yttt = {'en_te': en_te , 'arlab': p['arlab'], 'title': p['title'] ,'ar_f': ar_format,'en_f': en_format , 'ar_year': ar_year}
        #rao = ['en_te', 'arlab', 'title','ar_f','en_f', 'ar_year']
        #for yt in rao:
            #line += '<<lightpurple>> %s:<<lightblue>>"%s",'  % (yt , yttt[yt] )
        #pywikibot.output(line)
        #pywikibot.output( ' ar : "%s" , en : "%s"  ' % (ar , en) )
        #pywikibot.output( ' ar_year : "%s" , en_year : "%s"  ' % (ar_year , en_year) )
        #if mai['ar_format']:
            #pywikibot.output( ' mai[ar_format] : "%s"  ' % str(mai['ar_format']) )
    #---
    else:
        pywikibot.output( ' **<<lightred>> itemLabel:  no en_te in: "' + p['title'] + '", itemLabel:' +  p['itemLabel'])
    #return p
#---
day = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
YY = {}
NN = {}
#---   
def sopp(item, newlabel ):
    text = himoAPI.Labels_API( item, newlabel , 'ar' , True)
    json1 = json.loads(text)
    #pywikibot.output(json1["error"])
    if 'success' in text:
        pywikibot.output('<<lightgreen>> ** true.' )
    elif 'error' in text :
        #pywikibot.output('<<lightred>> ** error. : ')
        #---
        if ('using the same description text' in text) and ('associated with language code' in text):
            item2 = re.search('(Q\d+)', str(json1["error"]['info'])).group(1)
            pywikibot.output('<<lightred>> - same label item: ' + item2 )
            tt = '|-\n| {{Q|%s}} || %s || {{Q|%s}}\n' % (item2 ,newlabel , item)
            log(tt , 'Duplict.log.csv')
            #himoAPI.Merge( item2, item)
        else:
            pywikibot.output(text)
        #---
    else:
        pywikibot.output(text)
#---
def Woork(MainTab):
    from category.done import donelist
    konum = 0
    MainTab1 = {}
    #---
    #---
    insertformat = False
    for en2 in MainTab:#12
        pywikibot.output(en2 + ' ::' + str(MainTab[en2]['ar_format']))
        if len(MainTab[en2]['ar_format']) > 0:
            MainTab1[en2] = MainTab[en2]
        else:
            #pywikibot.output( MainTab[en2] )
            if insertformat:
                ask = pywikibot.input(' insert Arabic_Demo: for "%s" like:"category:se in &&&&" ! '  % MainTab[en2]['en_format'])
                if ask == 'stop':
                    insertformat = False
                elif ask != re.sub('&' , '' , str(ask)  ):
                    MainTab[en2]['ar_format'].append(ask)
                    pywikibot.output( 'new ar_format : "%s".' % ask )
                    MainTab1[en2] = MainTab[en2]
                else:
                    pywikibot.output( 'wrong insertformat: "%s"' %  ask)
    #---
    #---
    pywikibot.output( 'main lenth : "%d" , new lenth : "%d"' % (len(MainTab.keys()) , len(MainTab1.keys()) ) )
    time.sleep(2)
    #---
    for en_lab in MainTab1:#12
            konum += 1
            #if en_lab not in donelist:
            #sese = MainTab1[cat2]
            sese = MainTab1[en_lab]
            HasArabic = sese['HasArabic']
            NoArabic = sese['NoArabic']
            ar_len = len(HasArabic)
            en_len = len(NoArabic.keys() )
            #pywikibot.output( '<<lightyellow>>> ar_len: %d , en_len: %d ' % ( ar_len , en_len) )
            pywikibot.output( '<<lightblue>> ---------------------------------------- ')
            pywikibot.output( '<<lightblue>>> %d/%d a "%s" :  ar_len: %d , en_len: %d ' % (konum , len(MainTab1.keys()) ,  en_lab  , ar_len , en_len) )
            #---
            if en_len > 0:
                #---
                YY[en_lab] = False
                NN[en_lab] = True
                Art = ''
                #---
                ar_format = []
                for ara in sese['ar_format']:
                    aratest = re.sub('[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , str(ara)  )
                    if ara != aratest:
                        ar_format.append(ara)
                        Art = Art + ',a: ' + ara
                        #pywikibot.output( '<<lightyellow>>>  arabic format "%s". ' % ara)
                    #else:
                        #pywikibot.output( '<<lightred>>> no arabic format "%s".  ' % ara )
                pywikibot.output( '<<lightyellow>>>  en_format "%s", \n ar_format ("%s") ' % ( sese['en_format'], Art) )
                #---
                Arabic_Demo = ''
                if len(ar_format) > 1:
                    for ara1 in ar_format:
                        if Arabic_Demo == '':
                                saaa = pywikibot.input(' Take "%s" as Arabic_Demo? ' % ara1 )
                                if saaa == 'y' or saaa == 'a':
                                    Arabic_Demo = ara1
                    if Arabic_Demo == '':   
                        NN[en_lab] = False
                elif len(ar_format) > 0:
                    Arabic_Demo = ar_format[0]
                #---
                if Arabic_Demo != '' :
                    num_kaka = 0
                    len_NoAr = len(NoArabic)
                    for item in NoArabic:
                        if NN[en_lab]:          # عدم الموافقة على جزء كامل
                                num_kaka += 1
                                #if item in NoArabic:
                                pp = NoArabic[item]
                                if pp['en_year'] != '':
                                    newlabel = re.sub( '&&&&' , pp['en_year'] , Arabic_Demo)
                                #---
                                if newlabel != re.sub('[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , newlabel):
                                    if pp['title'] != re.sub('Category\:' , '' , pp['title']):
                                        if newlabel == re.sub('تصنيف\:' , '' , newlabel):
                                            newlabel = 'تصنيف:' + newlabel
                                    #pywikibot.output(pp)
                                    soooo =  '<<lightyellow>>>a %d/%d -en:"%s" ,q:"%s" enlabel "%s" , newlabel "%s".'
                                    pywikibot.output( soooo % (num_kaka , len_NoAr, en_lab , item , pp['title'] , newlabel) )
                                    #---
                                    if not YY[en_lab]:
                                        sa = pywikibot.input(' Add newlabel Yes or No ? ' )
                                        YES = YY[en_lab]
                                        if sa == 'y':               # الموافقة على واحد فقط
                                            YES = True
                                            sopp( item, newlabel )
                                        elif sa == 'a':             # الموافقة على جزء كامل
                                            YY[en_lab] = True           
                                        elif sa == 'noall':         # عدم الموافقة على جزء كامل
                                            NN[en_lab] = False          
                                    #---
                                    if YY[en_lab]:                      # الموافقة على جزء كامل
                                        sopp( item, newlabel )
                                    #---
            
            else:
                pywikibot.output( ' no ar len(str(sese["ar"] and %d english.' % len(sese['NoArabic']) )
                sop  = ''
                if len(sese['NoArabic']) > 1:
                    log('%s\t%s\t%s\n' % ( en_lab , len(sese['NoArabic']) , sop ) , 'new.log.csv' )
            #log('\ndonelist["%s"] = ""\n' % en_lab , 'done.py' )    
        #else:
            #pywikibot.output( ' en_lab "%s" already in donelist.' % en_lab )   
#---
def usa():
    #---
    qua = """SELECT #?item
 (concat(strafter(str(?item),"/entity/")) as ?item1) ?title ?itemLabel 
 WHERE {
 SERVICE wikibase:mwapi {
  bd:serviceParam wikibase:api "Generator" .
  bd:serviceParam wikibase:endpoint "#en#.wikipedia.org" .
  bd:serviceParam mwapi:gcmtitle "&&&&&" .
  bd:serviceParam mwapi:generator "categorymembers" .
  bd:serviceParam mwapi:gcmprop "ids|title|type" .
  bd:serviceParam mwapi:gcmlimit "max" .
  # out
  ?title wikibase:apiOutput mwapi:title  .
  ?ns wikibase:apiOutput "@ns" .
  ?item wikibase:apiOutputItem mwapi:item .
 }
 #FILTER( ?ns = "14" ) .
 #OPTIONAL { ?item rdfs:label ?arlab filter (lang(?arlab) = "ar") }
 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" . ?item rdfs:label ?itemLabel}
 }
 limit 300
 # """ 
    #wiki = 'en'
    qua = re.sub( '#en#' , wiki , qua)
    categoriees = ['Disestablishments in ~ by year']
    #pywikibot.output(categoriees)
    #MainTab = {}
    #---
    cat_num = 0
    for cat3 in categoriees:#12
        MainTab = {}
        for state in USA_P17:#12
            cat2 = re.sub('~' , state , cat3)
            cat_num += 1
            quarry = re.sub( '&&&&&' , 'Category:' + cat2 , qua)
            quarry = quarry + day
            #quarry = re.sub( '&&&&&' , cat2 , quarry)
            #pywikibot.output(str([quarry]))
            pywikibot.output(quarry)
            #---
            pagelist = himoBOT2.sparql_generator_url(quarry) 
            puy =  '<<lightyellow>>> cat_num: %d/%d : "%s" , lenth_pagelist : "%s"'
            pywikibot.output(puy  % ( cat_num , len(categoriees) * len(USA_P17) , cat2 , len(pagelist)))
            p_num = 0
            for p in pagelist:
                p_num += 1
                ttt(p , cat2 , MainTab, wiki)
        Woork(MainTab)
    #---
    #log(MainTab , 'All.py')
    #Woork(MainTab)
#---
def main2(categories__ , wiki):
    #---
    
    qua = """SELECT #?item
          (concat(strafter(str(?item),"/entity/"))  as ?item1)
          ?title ?itemLabel WHERE {
          SERVICE wikibase:mwapi {
             bd:serviceParam wikibase:api "Generator" .
             bd:serviceParam wikibase:endpoint "#en#.wikipedia.org" .
             bd:serviceParam mwapi:gcmtitle "&&&&&" .
             bd:serviceParam mwapi:generator "categorymembers" .
             bd:serviceParam mwapi:gcmprop "ids|title|type" .
             bd:serviceParam mwapi:gcmlimit "max" .
            # out
            ?title wikibase:apiOutput mwapi:title  .
            ?ns wikibase:apiOutput "@ns" .
            ?item wikibase:apiOutputItem mwapi:item .
          }
    #FILTER( ?ns = "14" ) .
    SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,#en#" } 
    #OPTIONAL { ?item rdfs:label ?itemLabel filter (lang(?itemLabel) = "ar") }
    }
    limit 300
    # """ 
    #wiki = 'en'
    qua = re.sub( '#en#' , wiki , qua)
    MainTab = {}
    categories12 = [
    #("Establishments_in_%s_by_year" % x) for x in USA_P17.keys() , 
    ("Disestablishments_in_%s_by_year" % x) for x in USA_P17.keys()
    ]
    categories123 =[
    "Years_in_the_United_States_by_state",
    "Establishments_in_Indiana_by_year",
    ]
    #---
    cat_num = 0
    for cat2 in categories12:#12
        cat_num += 1
        quarry = qua + day
        if wiki == 'en':
            cat2 = 'Category:' + cat2
        quarry = re.sub( '&&&&&' , cat2 , quarry)
        pywikibot.output( quarry)   
        #---
        pagelist = himoBOT2.sparql_generator_url(quarry) 
        puy =  '<<lightyellow>>> cat_num: %d/%d : "%s" , lenth_pagelist : "%s"'
        pywikibot.output(puy  % ( cat_num , len(categories12) , cat2 , len(pagelist)))
        p_num = 0
        for p in pagelist:
            p_num += 1
            ttt(p , cat2 , MainTab , wiki)
    #---
    #log(MainTab , 'All.py')
    Woork(MainTab)
#---
def sparql(categories__ , wiki):
    #---
    qua = """SELECT 
        (concat(strafter(str(?item),"/entity/"))  as ?item1)
        ?title
        ?itemLabel# ?P585 ?P585Label
        WHERE {
          &&&&&
          #SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" . }
          OPTIONAL { ?item rdfs:label ?itemLabel filter (lang(?itemLabel) = "ar") }
          ?item rdfs:label ?title filter (lang(?title) = "#en#")
        }
        #LIMIT 300
    # """ 
    #wiki = 'en'
    qua = re.sub( '#en#' , wiki , qua)
    MainTab = {}
    categories12 =['Military_history_by_year']
    
    #---
    cat_num = 0
    for cat2 in categories__:#12
        cat_num += 1
        quarry = qua + day
        #if wiki == 'en':
            #cat2 = 'Category:' + cat2
        quarry = re.sub( '&&&&&' , cat2 , quarry)
        pywikibot.output( quarry)   
        #---
        pagelist = himoBOT2.sparql_generator_url(quarry) 
        puy =  '<<lightyellow>>> cat_num: %d/%d : "%s" , lenth_pagelist : "%s"'
        pywikibot.output(puy  % ( cat_num , len(categories__) , cat2 , len(pagelist)))
        p_num = 0
        for p in pagelist:
            p_num += 1
            ttt(p , cat2 , MainTab , wiki)
    #---
    #log(MainTab , 'All.py')
    Woork(MainTab)
#---
def maintest():
    sopp('Q25054214', "تصنيف:رياضة سعودية في 1974")
#---
from lablist import *
wiki = 'en'
#---
def main():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == '1':
            main2(categories1, wiki)
        elif sys.argv[1] == 'log1':
            main2_log(categories1 , 'co1_.py' )
        elif sys.argv[1] == 'usa':
            usa()
        elif sys.argv[1] == 'log':
            main2_log(categories , 'co_.py' )
        else:# sys.argv[1] == '2':
            main2(categories, wiki)
    else:
        pywikibot.output( '<<lightyellow>> no args')
#---
if __name__ == "__main__":
    #maintest()
    #main2(categories, wiki)
    main()
#---
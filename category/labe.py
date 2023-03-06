#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة تسميات ويكي بيانات بناءاً على مطابقة اسماء التصانيف
وليس للسنوات

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
from API import himoAPI_test as himoAPI
#---
from API import himoBOT2
#---
from type.cate_type import pop_final_Without_Years as popstart
from type.cate_type import pop_format
from type.cate_P17	 import P17_final #P17_final#ALL_P17
from type.cate_P17 import USA_P17
#---
def log(t , ff):
    #form = t + '\n'
    with codecs.open("category/"+ff+"", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(str(t))
      except :
            pywikibot.output("Error writing")
#---
priv = {
    'en': 'Category:' , 
    'ceb': 'Kategoriya:' , 
    'sv': 'Kategori:' , 
    'war': 'Kaarangay:' , 
}
#---
#def ttt(p , cat , MainTab, wiki):
def ttt(p , cat3 , MainTab , wiki, en_P17 , p17 , pop_start , type):
    po = {}
    Q_item = p['item1']
    if not 'arlab' in p:
        p['arlab'] = ''
    if p['title'] == p['arlab'] :
        p['arlab'] = ''
    #pywikibot.output( ' **<<lightred>> arlab: "%s" ,title: "%s" '  %  ( (p['arlab'] , p['title']) ))
    ar_tab  , pop , popar, contrylab  = '' , ''  , '' , '' 
    #---
    if re.sub('Q\d+' , '' , p['title']) == '':
        #pywikibot.output( ' **<<lightyellow>> title is Qid '  +  p['title'])
        p['title'] = ''
    if re.sub('Q\d+' , '' , p['arlab']) == '':
        #pywikibot.output( ' **<<lightyellow>> title is Qid '  +  p['title'])
        p['arlab'] = ''
    #---
    ar = re.sub('تصنيف\:' , '' , p['arlab'])
    en = re.sub(priv[wiki]  , '' , p['title'])
    #pywikibot.output( ' ** ar:"%s" ,en:"%s" '  %  (ar , en ) )
    #---    
    re1 = re.compile(type)
    en_te = re1.findall(en)
    #---
    OP = False
    if not en_te:
        re1 = re.compile(type)
        en_te = re1.findall(p17)
        OP = True
    #---
    if en_te:
        pop = en_te[0]
        #pywikibot.output( ' **<<lightred>> pop: "%s" ,p[title]: "%s"  '  %  (str(pop) , p['title']  ) )
        po['pop'] = pop
        contrylab =  re.sub(pop , '' , en).strip()
        if pop not in MainTab:
            MainTab[pop] = {'HasArabic': {} , 'NoArabic': {} , 'en_format' : '', 'ar_format' : []}# , 'items' : []}
            #MainTab[pop]['s'] = {'en_format' : '', 'ar_format' : [] , 'items' : [] }
        mai = MainTab[pop]
        if contrylab in en_P17:
            ar_tab = en_P17[contrylab]['ar']
            #pywikibot.output( ' **<<lightred>> en_P17: ar:"%s" en:"%s"'  % (ar_tab , contrylab) )
        else:
            log('%s\t%s\n' % (contrylab , pop)  , 'contry miss arab.log.csv')
        if pop in pop_start:
            popar = pop_start[pop]['ar']
            #pywikibot.output( ' **<<lightred>> pop_start: ar:"%s" en:"%s"'  % (popar , pop) )
        #---
        ar_format = ''
        #re1 = re.compile('(\d\d\d\d)$')
        en_format = re.sub( contrylab , '&&&&' , p['title'])
        #mai['s']['en_format'] = en_format
        mai['en_format'] = en_format
        po['title'] = p['title']
        #---
        if ar_tab != '':
            if p['arlab'] != '' and (p['title'] != p['arlab']) :
                po['arlab'] = p['arlab']
                ar_format = re.sub( ar_tab , '&&&&' , p['arlab'])
                if ar_format != p['arlab']:
                    #if not ar_format in mai['s']['ar_format']:
                    if not ar_format in mai['ar_format']:
                        #mai['s']['ar_format'].append(ar_format)
                        mai['ar_format'].append(ar_format)
                        #---
                            # else:
                        #pywikibot.output( ' **<<lightyellow>> arlab:"%s",en_format:"%s",ar_format:"%s".' % ( po['arlab'], en_format ,ar_format) )
        #else:
            #mai['s']['items'].append(p['item1'])
            #mai['items'].append(p['item1'])
        #---
        #if ar_tab != '' :
            #if pop !=  ar_tab :
        po['ar_tab'] = ar_tab
        #---
        HasArabic  = mai['HasArabic']
        NoArabic   = mai['NoArabic']
        #---
        test = re.sub('[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , p['arlab'])
        #if p['arlab'] != test:
        if p['arlab'] != '':
            #p['arlab'] = ''
            HasArabic[Q_item] = po
        else:
            NoArabic[Q_item] = po
        #---
        #pywikibot.output(MainTab)
        line = '**'
        yttt = {'pop': pop , 'arlab': p['arlab'], 'title': p['title'] ,'ar_f': ar_format,'en_f': en_format , 'ar_tab': ar_tab}
        rao = ['pop', 'arlab', 'title','ar_f','en_f', 'ar_tab']
        for yt in rao:
            line += '<<lightpurple>> %s:<<lightblue>>"%s",'  % (yt , yttt[yt] )
        #pywikibot.output(line)
        #if mai['ar_format']:
            #pywikibot.output( ' mai[ar_format] : "%s"  ' % str(mai['ar_format']) )
    #---
    else:
        pywikibot.output( ' **<<lightred>> arlab:  no en_te in: "' + p['title'] + '", arlab:' +  p['arlab'])
        log('%s\t%s\n' % (p['title'] , p['arlab'])  , 'no type.log.csv')
        
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
        #pywikibot.output(en2 + ' ::' + str(MainTab[en2]['ar_format']))
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
                    aratest = re.sub( '[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , str(ara)  )
                    if ara != aratest:
                        ar_format.append(ara)
                        Art = Art + ',a: ' + ara
                    elif ara != re.sub( '[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , str(ara)  ):
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
                                if pp['ar_tab'] != '':
                                    newlabel = re.sub( '&&&&' , pp['ar_tab'] , Arabic_Demo)
                                    #if newlabel != re.sub('[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإؤءئ]' , '' , newlabel):
                                    if pp['title'] != re.sub('Category\:' , '' , pp['title']):
                                        if newlabel == re.sub('تصنيف\:' , '' , newlabel):
                                                newlabel = 'تصنيف:' + newlabel
                                                
                                        #pywikibot.output(pp)
                                        soooo =  '<<lightyellow>>>a %d/%d  q:"%s" enlabel "%s" , newlabel "%s".'
                                        pywikibot.output( soooo % (num_kaka , len_NoAr , item , pp['title'] , newlabel) )
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
                                    pywikibot.output( ' pp[ar_tab] == "%s" in "%s"' % ( pp['ar_tab'], pp['title'])  )
                else:
                    pywikibot.output( ' no Arabic_Demo.' )
            
            else:
                pywikibot.output( ' no ar len(str(sese["ar"] and %d english.' % len(sese['NoArabic']) )
                sop  = ''
                if len(sese['NoArabic']) > 1:
                    log('%s\t%s\t%s\n' % ( en_lab , len(sese['NoArabic']) , sop ) , 'new.log.csv' )
            #log('\ndonelist["%s"] = ""\n' % en_lab , 'done.py' )    
        #else:
            #pywikibot.output( ' en_lab "%s" already in donelist.' % en_lab )   
#---
USA_start = popstart#{    "Years in" : { "ar" : "سنوات في" , "Q" : "" } ,    }
#---
ssssssssssssssss = [
    "American Civil War by state navigational boxes",
    "American culture by state",
    "Buildings and structures in the United States by state",
    "Categories by state of the United States",
    "Communications in the United States by state",
    "Demographics of the United States by state",
    "Economy of the United States by state",
    "Education in the United States by state",
    "Environment of the United States by state or territory",
    "Geography of the United States by state",
    "Health in the United States by state",
    "History of the United States by state",
    "Images of the United States by state",
    "Labor relations in the United States by state",
    "Landmarks in the United States by state",
    "Manufacturing in the United States by state",
    "Military history of the United States by state",
    "Native American tribes by state",
    "Nature reserves in the United States by state",
    "Outlines of U.S. states",
    "People by state in the United States",
    "Political history of the United States by state or territory",
    "Science and technology in the United States by state",
    "Society of the United States by state",
    "Sports in the United States by state",
    "State governments of the United States",
    "State law in the United States",
    "States of the United States-related lists",
    "Tourist attractions in the United States by state",
    "Transportation in the United States by state",
    "United States symbols by state",
    "Wildlife management areas by state",
    
    ]
#---
def usa():
    #---
    p17list = [x for x in USA_P17.keys()]
    p17 = '(' + "|".join(p17list) + ')'
    typelist  = [x for x in USA_start.keys()]
    type = '(' + "|".join(typelist) + ')'
    #---
    qua = """SELECT #?item
 (concat(strafter(str(?item),"/entity/")) as ?item1) ?title ?arlab 
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
 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" . ?item rdfs:label ?arlab}
 }
 limit 300
 # """ 
    #wiki = 'en'
    qua = re.sub( '#en#' , wiki , qua)
    categoriees = ssssssssssssssss
    #pywikibot.output(categoriees)
    MainTab = {}
    #---
    cat_num = 0
    for cat3 in categoriees:#12
        #MainTab = {}
        #cat3 = re.sub(' of' , ' by country' , cat2)
        #if cat2 == cat3:
            #cat3 = re.sub(' in' , ' by country' , cat2)
        cat_num += 1
        quarry = re.sub( '&&&&&' , 'Category:' + cat3 , qua)
        quarry = quarry + day
        #if wiki == 'en':
            #cat3 = 'Category:' + cat3
        quarry = re.sub( '&&&&&' , cat3 , quarry)
        pywikibot.output(str([quarry]))
        #---
        pagelist = himoBOT2.sparql_generator_url(quarry) 
        puy =  '<<lightyellow>>> cat_num: %d/%d : "%s" , lenth_pagelist : "%s"'
        pywikibot.output(puy  % ( cat_num , len(categoriees) , cat3 , len(pagelist)))
        p_num = 0
        for p in pagelist:
            p_num += 1
            ttt(p , cat3 , MainTab , wiki, USA_P17 , p17 , USA_start , type)
        #Woork(MainTab)
    #---
    #log(MainTab , 'All.py')
    Woork(MainTab)
#---
wiki = 'en'
#---
def sparql():
    p17list = [x for x in P17_final.keys()]
    p17 = '(' + "|".join(p17list) + ')'
    typelist  = [x for x in popstart.keys()]
    type = '(' + "|".join(typelist) + ')'
    #---
    qua = """SELECT #?item
 (concat(strafter(str(?item),"/entity/")) as ?item1) ?title ?arlab 
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
 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" . ?item rdfs:label ?arlab}
 }
 limit 300
 # """ 
    #wiki = 'en'
    qua = re.sub( '#en#' , wiki , qua)
    categoriees = [x for x in popstart.keys()]
    #pywikibot.output(categoriees)
    MainTab = {}
    #---
    cat_num = 0
    for cat2 in categoriees:#12
        #MainTab = {}
        cat3 = re.sub(' of' , ' by country' , cat2)
        if cat2 == cat3:
            cat3 = re.sub(' in' , ' by country' , cat2)
        cat_num += 1
        quarry = re.sub( '&&&&&' , 'Category:' + cat3 , qua)
        quarry = quarry + day
        #if wiki == 'en':
            #cat3 = 'Category:' + cat3
        quarry = re.sub( '&&&&&' , cat3 , quarry)
        pywikibot.output(quarry)
        #---
        pagelist = himoBOT2.sparql_generator_url(quarry) 
        puy =  '<<lightyellow>>> cat_num: %d/%d : "%s" , lenth_pagelist : "%s"'
        pywikibot.output(puy  % ( cat_num , len(categoriees) , cat3 , len(pagelist)))
        p_num = 0
        for p in pagelist:
            p_num += 1
            ttt(p , cat3 , MainTab , wiki, P17_final , p17 , popstart , type)
        #Woork(MainTab)
    #---
    #log(MainTab , 'All.py')
    Woork(MainTab)
#---
def maintest():
    p = {
      "item1" : "Q1",
      "title" : "Category:Landforms of Honduras",
      "arlab" :   "تصنيف:تضاريس هندوراس",
    }
    p2 = {
      "item1" : "Q2",
      "title" : "Category:Landforms of Angola",
      "arlab" :   "",
    }
    cat = ''
    MainTab = {}
    ttt(p , cat , MainTab, 'en')
    ttt(p2 , cat , MainTab, 'en')
    pywikibot.output(MainTab)
    Woork(MainTab)
#---
def main():
    #goverment = USA_P17
    #goverment = P17_final
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == 'test':
            maintest()
        if sys.argv[1] == 'usa':
            usa()
        else:#
            sparql()
    else:
        sparql()
#---
if __name__ == "__main__":
    #maintest()
    #main2(categories, wiki)
    main()
#---
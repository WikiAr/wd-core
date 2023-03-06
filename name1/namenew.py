#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

اضافة تسميات بناءاً على الاسم الأول واسم العائلة

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
import pywikibot.data.wikidataquery as wdquery
import codecs
from API.maindir import main_dir #used in logfiles, unicoded strings
import unicodedata
import datetime
import json
import urllib
import unicodedata
#---
import sys
#---
import urllib.request
import urllib.parse
    
#---
from API import himoBOT
#---
def logme(q , label):
    verbose = False
    with codecs.open("name/name.log.csv", "a", encoding="utf-8") as logfile:
        #formattedstring = ( '%s\tLar\t"""%s"""\n' % ( q , label) )
        formattedstring = ( '%s\t%s\n' % ( q , label) )
        try:   
          logfile.write(formattedstring)
        except :
          pywikibot.output(" Error writing to logfile on: [%s] [%s]" % (exctype, value))
          verbose = True    #now I want to see what!   
        logfile.close()
    if verbose:
        pywikibot.output(formattedstring)  
#---
from API import himoAPI_test as himoAPI
#---
def AddLabel(item, title):
     Summary= 'Bot: Added ar label: '+title+'' # ملخص التعديل
     ka = True #False#True
     #if (('labels' in item) and ('ar' in item.labels)):
     if item.labels.get('ar' , '') != '':
     #if 'ar' in item.labels:
          pywikibot.output('fond ar label "%s" in "%s"' % ( item.labels['ar'] , item ) ) 
          pass
     else:
          if ka:
                pywikibot.output('%s\t%s' % (item, Summary)) 
     q = item.title(asLink=False)
     himoAPI.Labels_API(q , title , 'ar' , False)
#---
def action_one_item( pa ):
    q = pa ['item']
    #item = pa ['item']
    EnName = re.sub( '\s+\(.*\)$' , '' , pa['enname'])
    #---
    enlabel =  re.sub( '\s+\(.*\)$' , '' , pa['FirstNameE']) + ' ' + re.sub( '\s+\(.*\)$' , '' , pa['LastNameE'])
    pywikibot.output('*EnName : "%s" , enlabel : "%s"' % ( EnName , enlabel ))
    #---
    arlabel =  re.sub( '\s+\(.*\)$' , '' , pa['FirstNameL']) + ' ' + re.sub( '\s+\(.*\)$' , '' , pa['LastNameL'])
    TestArabic = re.sub( '[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإىءئؤ ]' , '' , arlabel)
    pywikibot.output('*TestArabic : "%s" , arlabel : "%s"' % ( TestArabic , arlabel ))
    #---
    site = pywikibot.Site('wikidata', 'wikidata')
    repo = site.data_repository()
    item = pywikibot.ItemPage(repo, q)
    #---
    SameLabel = False
    try:   
        item.get()
    except :
        pywikibot.output('*error when item.get() "%s"' % q)
        pass
    if TestArabic == '' :
        if EnName == enlabel :
            SameLabel = True
        else:
            pywikibot.output('*defrent : names "%s" , label : "%s"' % ( enlabel , EnName ))
    else:
        pywikibot.output('*TestArabic failed' )
        ii = arlabel + '\tTestArabic failed'
        logme( q , ii)
        
    if SameLabel:
        try:   
            AddLabel( item , arlabel )
        except :
            pywikibot.output('*error when item.get() "%s"' % q)
            i = arlabel + '\t' + enlabel + '\t' + EnName
            logme( q , i)
            pass
#---
def GetNameClaims(item , MainLang):
    #ClaimsName = {'FirstNameE':'','item': '','enname':'','LastNameE':'','FirstNameL': '', 'LastNameL': ''}
    ClaimsName = {'FirstNameE':'','LastNameE':'','FirstNameL': '', 'LastNameL': ''}
    s = { 
    'P734' : {'ar': 'LastNameL', MainLang: 'LastNameE'},
    'P735' : {'ar': 'FirstNameL', MainLang: 'FirstNameE'},
    }
    names = {}
    names['item'] = item
    if MainLang in item.labels:
        names['enname'] = item.labels[MainLang]
    #---
    for property in s:
        prop = ClaimsName[c]
        #---
        if (property in wditem1.claims):
            item2 = wditem1.claims[property][1]
            prop2 = item2.toJSON()
            pywikibot.output(prop2)
        #---
        for lang in prop:
            sab = prop[lang]
            pywikibot.output(lang)
            if lang in item2.labels:
                names[sab] = item2.labels[lang]
        #---
        #names[c] = item.labels[lang]
    return names
#---
def main1211():
    limit = '1000'
    language = [  'de' , 'fr', 'nl', 'en' ]
    logme('Q' , 'label')
	
    for lang in language:
        #lang = 'de'
        pywikibot.output('start with query')
        ur = 'SELECT ?item ?enname ?FirstNameL ?LastNameL  ?FirstNameE  ?LastNameE'
        ur = ur + (' WHERE { {?item wdt:P31 wd:Q5.} {?item rdfs:label ?enname filter (lang(?enname) = "%s") . }' % lang )
        ur = ur + ' FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .'
        ur = ur + ' {?item wdt:P734 ?LastName. ?LastName rdfs:label ?LastNameL. FILTER((LANG(?LastNameL)) = "ar")'
        ur = ur + (' . ?LastName rdfs:label ?LastNameE. FILTER((LANG(?LastNameE)) = "%s")'% lang )
        ur = ur + ' ?item wdt:P735 ?FirstName. ?FirstName rdfs:label ?FirstNameL. FILTER((LANG(?FirstNameL)) = "ar")'
        #ur = ur + ' . ?FirstName rdfs:label ?FirstNameE. FILTER((LANG(?FirstNameE)) = "' + lang + '")} }'
        ur = ur + (' . ?FirstName rdfs:label ?FirstNameE. FILTER((LANG(?FirstNameE)) = "%s")} }' % lang )
        ur = ur + '\n limit ' + limit
        pywikibot.output(ur)
        sparql = himoBOT.sparql_generator_url(ur)
        total = len(sparql)
        #---
        num = 0
        for pa in sparql:
            num += 1
            #pa = pigenerator[page]
            pa['item'] = pa['item'].split('/entity/')[1]
            pywikibot.output('<<lightblue>>> %s :%s/%d : %s'  % ( lang , num , total , pa['item'] ) )
            action_one_item(  pa )
#---
debugedo=False
#True#False
#---
ssse = {'FirstNameE':  'wiki'
        ,  'item':  'Q76'
        , 'enname': 'wiki sandbox'
        , 'LastNameE': 'sandbox'
        , 'FirstNameL': 'ملعب'
        , 'LastNameL': 'ويكي بيانات'}
#---
if __name__ == "__main__":  
     if debugedo:
        pywikibot.output("debug is on")
        action_one_item( ssse )
     else:
        main1211()
#---
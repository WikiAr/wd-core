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
from pywikibot import pagegenerators
import pywikibot.data.wikidataquery as wdquery
import codecs
from API.maindir import main_dir #used in logfiles, unicoded strings
import datetime
import json
import urllib
import unicodedata
#---
import sys
#---
import urllib.request
import urllib.parse

    
def logme(q , label):
    verbose = False
    with codecs.open("textfiles/name-logs/name.log.csv", "a", encoding="utf-8") as logfile:
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
#---
#from API.useraccount import *
from API import himoAPI
#---
def AddLabel(item, title):
     data = { 'labels' : {'ar':{}} }
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
          #arlab = { 'ar': title }
          #data['labels']['ar'] = {'language': 'ar','value': title}
          #if item:   
     #try: 
     q = item.title(asLink=False)
     himoAPI.Labels_API(q , title , 'ar' )
     #item.editLabels(labels=arlab, summary=Summary)
     #except:
     #else:
     #pywikibot.output('error when add label to %s' % item) 
          

def action_one_item( pa ):
    q = pa ['item']
    #item = pa ['item']
    EnName = re.sub( '\s+\(.*\)$' , '' , pa['enname'])
    #---
    enlabel =  re.sub( '\s+\(.*\)$' , '' , pa['FirstNameE']) + ' ' + re.sub( '\s+\(.*\)$' , '' , pa['LastNameE'])
    pywikibot.output('*EnName : "%s" , enlabel : "%s"' % ( EnName , enlabel ))
    #---
    #arlabel =  pa['FirstNameL'] + ' ' + pa['LastNameL']
    arlabel =  re.sub( '\s+\(.*\)$' , '' , pa['FirstNameL']) + ' ' + re.sub( '\s+\(.*\)$' , '' , pa['LastNameL'])

    #arlabel =  re.sub( '\s+\(.*\)$' , '' , arlabel)
    #arlabel =  re.sub( '\s+\(.*\)' , '' , arlabel)
    
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
    
def wd_sparql_generator(query):     
  wikidatasite=pywikibot.Site('wikidata','wikidata') 
  generator=pagegenerators.WikidataSPARQLPageGenerator(query,site=wikidatasite)
  for wd in generator:
    wd.get(get_redirect=True)
    yield wd
       
def loadSPARQL(sparql=''):
    json1 = ''
    if sparql:
        try:
            json1 = json.loads(sparql)
            return json1
        except:
            pywikibot.output('Error downloading SPARQL? Malformatted JSON? Skiping\n')
            #return  ''
    else:
        pywikibot.output('Server return empty file')
        #return 
    #return
    
def Gquery2(json1):
    table = {}
    #table = []
    #for head in json1['head']['vars']:
    for result in json1['results']['bindings']:
        q = 'item' in result and result['item']['value'].split('/entity/')[1] or ''
        s = {}
        for se in result:
            s[se] = result[se]['value']
        s['item'] = q
        table[q] = s
    return table
    
def getURL(url=''):
    html = ''
    pywikibot.output(url)
    try:
        html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
        #html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
    except:
        sleep = 10 # seconds
        maxsleep = 60
        while sleep <= maxsleep:
            pywikibot.output('<<lightyellow>> Error while retrieving: %s' % (url))
            pywikibot.output('<<lightyellow>> Retry in %s seconds...' % (sleep))
            time.sleep(sleep)
            try:
                html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
                #html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
            except:
                pywikibot.output('Error')
                pass
            sleep = sleep * 2
    if html !='':
        html = html.decode('utf-8')#.decode('utf-8')
    return html
    
def main():
        faquery="""SELECT ?item ?enname ?FirstNameL ?LastNameL  ?FirstNameE  ?LastNameE
            WHERE {
                {?item wdt:P31 wd:Q5.}
                UNION{ ?item wdt:P106 ?pob . ?pob wdt:P279* wd:Q901 
              .?item wdt:P39 ?pob2 .?item wdt:P569 ?P569 .?item wdt:P27 ?P27
            .?item wdt:P166 ?P166  .?item wdt:P19 ?P19.?item wdt:P106 ?P106.}
                {?item rdfs:label ?enname filter (lang(?enname) = "fa") . }
                OPTIONAL { ?sitelink schema:about ?item . ?sitelink schema:inLanguage "ar" } 
                FILTER(!BOUND(?sitelink))
                FILTER NOT EXISTS { ?item wdt:P106 wd:Q488111.} 
            #  ?pob wdt:P279* wd:Q48352.
                FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .
                {
                ?item wdt:P734 ?LastName. ?LastName rdfs:label ?LastNameL. FILTER((LANG(?LastNameL)) = "ar")
                                        . ?LastName rdfs:label ?LastNameE. FILTER((LANG(?LastNameE)) = "fa")
                ?item wdt:P735 ?FirstName. ?FirstName rdfs:label ?FirstNameL. FILTER((LANG(?FirstNameL)) = "ar")
                                        . ?FirstName rdfs:label ?FirstNameE. FILTER((LANG(?FirstNameE)) = "fa")
              #    SERVICE wikibase:label { bd:serviceParam wikibase:language "fa" }
                }
            }"""  

        #language = [  frquery , enquery, dequery , faquery ]
        #for lang in language:
        query2 =  faquery
        pywikibot.output(query2)

        #query2 =  re.sub( '\$lang\$' , lang , default_query2)
        limit = '100'
        pywikibot.output('start with query')
        fao = urllib.parse.quote(query2)
        
        url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=' + fao +'limit%20'+limit+'&format=json'
        #sparql = urllib.request.urlopen(url).read().strip().decode('utf8','ignore')
        #sparql = urllib.request.urlopen(url).read().strip().decode('utf8')
        #sparql = urllib.request.urlopen(url).read().strip().decode('utf8')
        sparql = getURL(url)
        json1 = loadSPARQL(sparql=sparql)   
        #pywikibot.output(url)
        #pywikibot.output(sparql)
        total = len(json1['results']['bindings'])
        pigenerator = Gquery2(json1)
        num = 0
        #pywikibot.output(pigenerator)
        for page in pigenerator:
            num += 1
            pa = pigenerator[page]
            #pywikibot.output('<<lightblue>>> %s :%s/%d : %s'  % ( lang , num , total , pa['item'] ) )
            pywikibot.output('<<lightblue>>> %s/%d : %s'  % ( num , total , pa['item'] ) )

            #pywikibot.output(pa)
            #pywikibot.output(pa['enname'])
            #wikidataBot.run(lng)
            #print_wikitable(lng)
            action_one_item(  pa )
            
def main1():
    limit = '2000'
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
        
        fao = urllib.parse.quote(ur)
            
        url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=' + fao + 'limit%20'+limit+'&format=json'
        sparql = getURL(url)
        json1 = loadSPARQL(sparql=sparql)   
        #---
        if json1:
            if 'results' in json1:
                if 'bindings' in json1['results']:
                    total = len(json1['results']['bindings'])
                    pigenerator = Gquery2(json1)
                    num = 0
                    #pywikibot.output(pigenerator)
                    
                    for page in pigenerator:
                        num += 1
                        pa = pigenerator[page]
                        pywikibot.output('<<lightblue>>> %s :%s/%d : %s'  % ( lang , num , total , pa['item'] ) )
                        #pywikibot.output('<<lightblue>>> %s/%d : %s'  % ( num , total , pa['item'] ) )

                        #pywikibot.output(pa)
                        #pywikibot.output(pa['enname'])
                        #wikidataBot.run(lng)
                        #print_wikitable(lng)
                        action_one_item(  pa )
            
def main2():
        TestQuery ="""SELECT ?item
            WHERE {
                {?item wdt:P31 wd:Q5.}
                UNION{ ?item wdt:P106 ?pob . ?pob wdt:P279* wd:Q901 
              .?item wdt:P39 ?pob2 .?item wdt:P569 ?P569 .?item wdt:P27 ?P27
            .?item wdt:P166 ?P166  .?item wdt:P19 ?P19.?item wdt:P106 ?P106.}
                {?item rdfs:label ?enname filter (lang(?enname) = "en") . }
                OPTIONAL { ?sitelink schema:about ?item . ?sitelink schema:inLanguage "ar" } 
                FILTER(!BOUND(?sitelink))
                FILTER NOT EXISTS { ?item wdt:P106 wd:Q488111.} 
            #  ?pob wdt:P279* wd:Q48352.
                FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .
                {
                ?item wdt:P734 ?LastName. ?LastName rdfs:label ?LastNameL. FILTER((LANG(?LastNameL)) = "ar")
                                        . ?LastName rdfs:label ?LastNameE. FILTER((LANG(?LastNameE)) = "en")
                ?item wdt:P735 ?FirstName. ?FirstName rdfs:label ?FirstNameL. FILTER((LANG(?FirstNameL)) = "ar")
                                        . ?FirstName rdfs:label ?FirstNameE. FILTER((LANG(?FirstNameE)) = "en")
              #    SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }
                }
        }"""
        #language = [  frquery , enquery, dequery , faquery ]
        #for lang in language:
        Test =  TestQuery + 'limit ' + limit
        pywikibot.output(query2)
        #query2 =  re.sub( '\$lang\$' , lang , default_query2)
        limit = '100'
        pywikibot.output('start with query')
        
        sparql = wd_sparql_generator(Test)
        #json1 = loadSPARQL(sparql=sparql)   
        #pywikibot.output(url)
        #pywikibot.output(sparql)
        total = len(sparql)
        pigenerator = Gquery2(json1)
        num = 0
        #pywikibot.output(pigenerator)
        for page in pigenerator:
            num += 1
            pa = GetNameClaims(page , 'fr')
            #pywikibot.output('<<lightblue>>> %s :%s/%d : %s'  % ( lang , num , total , pa['item'] ) )
            pywikibot.output('<<lightblue>>> %s/%d : %s'  % ( num , total , page.title(asLink=False) ) )
            #pywikibot.output(pa)
            #pywikibot.output(pa['enname'])
            #wikidataBot.run(lng)
            #print_wikitable(lng)
            action_one_item(  pa )

debugedo=False
#True#False

ssse = {'FirstNameE':  'wiki'
        ,  'item':  'Q76'
        , 'enname': 'wiki sandbox'
        , 'LastNameE': 'sandbox'
        , 'FirstNameL': 'ملعب'
        , 'LastNameL': 'ويكي بيانات'}

if __name__ == "__main__":  
     if debugedo:
        pywikibot.output("debug is on")
        action_one_item( ssse )
     else:
        #main2()
        main1()
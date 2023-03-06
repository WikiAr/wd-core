#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت استعلام سباركل والكتابة على صفحة مستخدم

python3 pwb.py c30/stat
python pwb.py c40/stat

"""
#
# (C) Ibrahem Qasim, 2022 
#
#
import re
import time
import json
import pywikibot
import codecs
from API.maindir import main_dir
import urllib
#---
import urllib
import urllib.request
import urllib.parse
#---
from pywikibot.textlib import does_text_contain_section

import string
#import json
from pywikibot import site as Psite
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.



targetlangs = ['ar']
#site = pywikibot.Site('wikidata', 'wikidata')
#repo = site.data_repository()

adress="user:Mr. Ibrahem/stat"
message="update"
pagetop='{| class="wikitable"\n|+«Arabic&nbsp;Description&nbsp;count»'
pagedown='\n|-\n|}'
#---
from API import himoBOT2
#---
def loadSPARQL(sparql=''):
    json1 = ''
    if sparql:
        try:
            json1 = json.loads(sparql)
            return json1
        except:
            pywikibot.output('Error downloading SPARQL? Malformatted JSON? Skiping\n')
            return ''
    else:
        pywikibot.output('Server return empty file')
        return ''
    return ''

def getURL(url=''):
    raw = ''
    req = url#urllib.request.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    try:
        raw = urllib.request.urlopen(req).read().strip().decode('utf-8')
    except:
        sleep = 10 # seconds
        maxsleep = 100
        while sleep <= maxsleep:
            pywikibot.output('Error while retrieving: %s' % (url))
            pywikibot.output('Retry in %s seconds...' % (sleep))
            time.sleep(sleep)
            try:
                raw = urllib.request.urlopen(req).read().strip().decode('utf-8')
            except:
                pass
            sleep = sleep * 2
    return raw
    
def action(total, translation, targetlang,des,name):
   # with codecs.open("stat/q.log.csv", "a", encoding="utf-8") as logfile:
    with codecs.open("stat/new/"+ (name or 'q')+".log.csv", "a", encoding="utf-8") as logfile:

        form = "%d\t'\t%s\t':{'ar':'\t%s\t'},"
        formattedstring = '%s%s' % (form , '\n')
        try:   
           if total > 10:
               logfile.write(formattedstring %  (total, translation, des))
        except :
           pass
    verbose = True#True #now I want to see what!   
    logfile.close()
    if verbose:
        pywikibot.output(form % (total, translation, des) )   #, des
WikidataSite  = pywikibot.Site("wikidata", "wikidata")

def main(Q , test):
    #---
    if test:
        return Q
    #---
    #r = "SELECT  (COUNT(?item) AS ?count)  WHERE {  ?wiki0 schema:about ?item."
    #r =  r + "?wiki0 schema:isPartOf <https://ar.wikipedia.org/>.  ?item wdt:P31 ?sub0.   ?sub0 wdt:P279* wd:"  #Q83620
    #r =  r + Q +  ". } GROUP BY ?count"
    #---
    r = '''
SELECT (COUNT(?item) AS ?count)  WHERE {
  ?wiki0 schema:about ?item.
?wiki0 schema:isPartOf <https://ar.wikipedia.org/>.
  ?item wdt:P31 ?sub0.
  ?sub0 wdt:P279* wd:%s.
} GROUP BY ?count'''
    #---
    r = r % Q
    #---
    #s ='SELECT ?itemDescription (COUNT(?itemDescription) AS ?count) WHERE {  ?item wdt:P31 wd:Q5. ?article     schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . ?item schema:description ?itemDescription .  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" } } GROUP BY ?itemDescription limit 100'
    #---
    fao = urllib.parse.quote( r )
    #---
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query='+ fao +'&format=json'
    pywikibot.output(url)
    sparql = getURL(url=url)
    if sparql == "":
        return  ""
    json3 = loadSPARQL(sparql=sparql)
    json1 = json.loads(sparql)
    #total = len(json1['results']['bindings'])
    #s = json1['results']['bindings']#['count']
    #ss = s['count']['value']
    #---
    #pywikibot.output(json1)
    #{'head': {'vars': ['count']}
    #, 'results': {'bindings': [{'count': {'type': 'literal', 'datatype': 'http://www.w3.org/2001/XMLSchema#integer', 'value': '38123'}}]}
    #}
    #---
    json2 = json1['results']['bindings'][0]
    count = json2['count']['value']
    #---
    #text = text + ('\n|-\n| %s || %s ' % (c , d))
    #for result in json1['results']['bindings'][0]:
      #c = result['count']['value']
      #text = text + ('\n|-\n| %s || %s ' % (c , d))
    #---
    pywikibot.output(count)
    return count
    #pywikibot.output('\n%d items; dis:%s; %s:%s; items %d/%d; queries %d/%d' % (total, translation, targetlang,translations[translation][targetlang], c2, total2, cqueries, totalqueries))
    #action(total, translation, targetlang,translations[translation][targetlang],name) # بدء العمل 
    #pywikibot.output("انتهت بنجاح")
    
def main_New(Q , test):
    #---
    if test:
        return Q
    #---
    r = "SELECT  ?item# (COUNT(?item) AS ?count)\n  WHERE {  ?wiki0 schema:about ?item."
    r =  r + "?wiki0 schema:isPartOf <https://ar.wikipedia.org/>.  ?item wdt:P31 ?sub0.   ?sub0 wdt:P279* wd:"  #Q83620
    r =  r + Q +  ". } #GROUP BY ?count"
    #s ='SELECT ?itemDescription (COUNT(?itemDescription) AS ?count) WHERE {  ?item wdt:P31 wd:Q5. ?article     schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> . ?item schema:description ?itemDescription .  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar" } } GROUP BY ?itemDescription limit 100'
    #---
    fao = urllib.parse.quote( r )
    #---
    url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query='+ fao +'&format=json'
    pywikibot.output(url)
    sparql = getURL(url=url)
    if sparql == "":
        return  ""
    json3 = loadSPARQL(sparql=sparql)
    json1 = json.loads(sparql)
    #total = len(json1['results']['bindings'])
    #s = json1['results']['bindings']#['count']
    #ss = s['count']['value']
    #---
    #pywikibot.output(json1)
    #{'head': {'vars': ['count']}
    #, 'results': {'bindings': [{'count': {'type': 'literal', 'datatype': 'http://www.w3.org/2001/XMLSchema#integer', 'value': '38123'}}]}
    #}
    #---
    json2 = json1['results']['bindings']
    count = len(json2)
    #---
    #text = text + ('\n|-\n| %s || %s ' % (c , d))
    #for result in json1['results']['bindings'][0]:
      #c = result['count']['value']
      #text = text + ('\n|-\n| %s || %s ' % (c , d))
    #---
    pywikibot.output(count)
    return count
    #pywikibot.output('\n%d items; dis:%s; %s:%s; items %d/%d; queries %d/%d' % (total, translation, targetlang,translations[translation][targetlang], c2, total2, cqueries, totalqueries))
    #action(total, translation, targetlang,translations[translation][targetlang],name) # بدء العمل 
    #pywikibot.output("انتهت بنجاح")
    
def GetSub( type , MainTable , test):
     pywikibot.output( '<<lightyellow>> **GetSub: "%s" ' % type)
     result = ''
     lenth = len(MainTable) 
     #---
     pywikibot.output('len: '  + str(lenth) )
     if lenth == 0 :
          return ''
     #---
     ha = '\n'#('===%swiki===\n' %  type )
     head = ha + '{| class="wikitable sortable" style="text-align:right; width: 100%; font-size: 95%;"\n|+ "'
     head = head +  type + 'wiki"' + '\n'
     #---
     r =  '! data-sort-type="number"| Qid'
     r =  r + '\n! usage '
     r =  r + '\n|-\n'
     #---
     #propcat[type] = {}
     #propcat[v].append( id )
     num = 0
     lenMainTable = len(MainTable)
     for Q in MainTable:
        num = num + 1
        pywikibot.output('** %d/%d "%s"' % (num , lenMainTable , Q ) )
        #Quse = main_New(Q , test)
        Quse = main(Q , test)
        #P = logproperty(Q)
        P = ('\n|-\n| {{Q|%s}} || %s ' % ( Q , Quse ))
        result = result + P + '\n'
     #---
     #final = FinalLine(MainTable)
     #result = result + final
     #---
     FinalText = head + r + result + '\n|}\n'
     #pywikibot.output( FinalText )
     #log33(FinalText)
     return FinalText

     
def PPPNew(Paa):    
    c = []
    params = Paa.split('}}}')[0]
    params = params.split('|')
    #params = str(params)
    pywikibot.output(params)
    #---
    for pa in params:
        param = pa.strip()
        Pa2 = re.sub('Q\d+', '' , param)
        if Pa2 == '':
            c.append(param)
        #else:
            #pywikibot.output('** "%s" != '':  ' % Pa2 )
    #---
    pywikibot.output(c)
    return c
    

def GetSection(titl1 , SectionName , sub ):

     pywikibot.output( '<<lightyellow>> **GetSection: "%s" ' % SectionName)
     MainText = ''
     #root = Tk()
     #to = Text(root)
     #---
     title = titl1 + '#' + SectionName
     page = pywikibot.Page(WikidataSite , title)
     text = page.text
     #from pywikibot import site as Psite
     #---
     pywikibot.output( '**<<lightyellow>> GetSection text:' )
     pywikibot.output(text)
     pywikibot.output( '**<<lightyellow>> -------------' )
     #def testSection(self):
     #"""Test section() method."""
     # use same pages as in previous test
     #site = self.get_site()
     #p1 = pywikibot.Page(site, "Help:Test page#Testing")
     #p2 = pywikibot.Page(site, "File:Jean-Léon Gérôme 003.jpg")
     section = page.section()
     #self.assertEqual(p2.section(), None)
     pywikibot.output( '**<<lightyellow>> section:' )
     pywikibot.output(section)
     pywikibot.output( '**<<lightyellow>> -------------' )
     #---
     #pywikibot.showDiff(page.text , MainText)
     """if AskToSave:
          sa = pywikibot.input('Yes or No ' )
          if sa == 'y':
               page.put(MainText , message)
          else:
               pywikibot.output('wrong answer')
     else:
          page.put(MainText , message)"""
     #---

def GetSection2(titl1 , SectionName , sub ):

     pywikibot.output( '<<lightyellow>> **GetSection: "%s" ' % SectionName)
     MainText = ''
     #root = Tk()
     #to = Text(root)
     #---
     title = titl1 + '#' + SectionName
     page = pywikibot.Page(WikidataSite , title)
     text = page.text
     #pywikibot.site.APISite.get_parsed_page(page) 
     #pywikibot.output(pywikibot.site.APISite.get_parsed_page(pywikibot.site.APISite,page) )
     #---
     #pywikibot.site.BaseSite.loadrevisions(page, getText=True, section=None)
     forr = {
        "action": "parse",
        "format": "json",
        "summary": "",
        "page": "مستخدم:Mr._Ibrahem/ملعب9",
        "prop": "sections",
        "disableeditsection": 1,
        "utf8": 1
        }
     #Site = pywikibot.Site('wikidata' ,  "wikidata")
     pppa = {
            "action":"parse",
            "format":"json",
            "page":titl1,
            "prop":'sections',
            "disableeditsection":'1',
            "utf8":'1'
            }
     Ca = pywikibot.data.api.Request(site=Site, parameters = pppa)
     #Ca = Ca.submit()
     #---
     section = page.section()
     if section and does_text_contain_section(page.text,section):
          for se in Ca['parse']['sections']:
               #case = Ca['parse']['sections'][se]
               line = se['line']
               SectionNumber = se['toclevel']
               if line == SectionName:
                    pywikibot.output( '**<<lightyellow>> case == SectionName:' + str(SectionNumber))
                    Sec_Text = pywikibot.site.APISite.loadrevisions(Site, page=page, getText=True, section=SectionNumber) 
                    pywikibot.output( '**<<lightyellow>> Sec_Text:' )
                    pywikibot.output(Sec_Text)
                    pywikibot.output( '**<<lightyellow>> -------------' )
     #---
     #pywikibot.output( '**<<lightyellow>> GetSection2 text:' )
     #pywikibot.output(text)
     #pywikibot.output( '**<<lightyellow>> -------------' )
     #def testSection(self):
     #"""Test section() method."""
     # use same pages as in previous test
     #site = self.get_site()
     #p1 = pywikibot.Page(site, "Help:Test page#Testing")
     #p2 = pywikibot.Page(site, "File:Jean-Léon Gérôme 003.jpg")

          
     
          #self.assertEqual(p2.section(), None)
          #pywikibot.output( '**<<lightyellow>> section:' )
          #pywikibot.output(does_text_contain_section(page.text,section))
          #pywikibot.output( '**<<lightyellow>> -------------' )
     #---
     #pywikibot.showDiff(page.text , MainText)
     """if AskToSave:
          sa = pywikibot.input('Yes or No ' )
          if sa == 'y':
               page.put(MainText , message)
          else:
               pywikibot.output('wrong answer')
     else:
          page.put(MainText , message)"""
     #---

def GetSection3(text , SectionName ):
     pywikibot.output( '<<lightyellow>> **GetSection3: "%s" ' % SectionName)
     #pywikibot.site.APISite.get_parsed_page(page) 
     text2 = text.split('=='+SectionName+'==')[1]
     text2 = text2.split('==')[0]
     #pywikibot.output( '**<<lightyellow>> text2:' )
     #pywikibot.output(text2)
     #pywikibot.output( '<<lightyellow>> **-------------' )
     #pywikibot.output( '**<<lightyellow>> sub:' )
     #pywikibot.output(sub)
     #pywikibot.output( '<<lightyellow>> **-------------' )
     #MainText = re.sub(text2 , sub , text)
     #---
     return text2
     #---

def main2():
    #root = Tk()
    #to = Text(root)
    #---
    titl1 = 'User:Mr._Ibrahem/stat'
    #page = pywikibot.Page(WikidataSite , titl1)
    #text = page.text
    text = himoBOT2.GetarPageText(titl1, sitecode='www', family="wikidata")
    MainText = text
    #---
    find = re.compile('\{\{\{\s*?stat\s*?\|.*?\}\}\}')
    #find = re.compile('\{\{\{\s*?stat\s*?\|.*?\}\}\}' , re.IGNORECASE)
    #find = '[^{]\{\{\s*[iI]ll-WD2\s*\|' + tt + '+\}\}'
    result = re.findall(find , text)
    if result :
    #if result :
          totall  = len(result)
          pywikibot.output('** result totall is: "%s" ' % totall )
          for wiki in result:
               wi = wiki.split('wiki|Q')[0]
               wi = re.sub('\{\{\{stat\|', '' , wi)
               pywikibot.output( '** %s: ' % wi + wiki )
               SectionName = ('%swiki' %  wi )
               Items = PPPNew(wiki)
               sub = GetSub(wi , Items , False)#False#True
               old = GetSection3(text , SectionName )
               MainText = MainText.replace( old , sub )
               #line = main(pp)
    #---
    pywikibot.showDiff(text , MainText)
    uu = """if AskToSave:
          sa = pywikibot.input('Yes or No ' )
          if sa == 'y':
               page.put(MainText , message)
          else:
               pywikibot.output('wrong answer')
     else:
          page.put(MainText , message)"""
    #---
    
    rt = ''

     
if __name__ == "__main__":
    main2()

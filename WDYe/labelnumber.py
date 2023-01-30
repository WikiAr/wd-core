#!/usr/bin/python
# -*- coding: utf-8  -*-
#
import pywikibot
from pywikibot import pagegenerators
from pywikibot import pagegenerators as pg


import codecs
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
import sys
import datetime
from datetime import datetime, date, time

debugedo=True
debugedo=False
debug=False
default_language = 'ar' 
items2do = 0
itemsdone= 0
missing_dict={}

def logme(wditem, numberlabel):
  form = '\n%s\tLar\t%s'
  with codecs.open(main_dir+"wd/labelnumber.log.csv", "a", encoding="utf-8") as logfile:
    try:   
        logfile.write(form % (wditem, numberlabel) )
    except :
        pass
        print(" Error writing to logfile on: [%s]" %  numberlabel)
    verbose = True#True    #now I want to see what!   
    logfile.close()
    if verbose:
       print(form % (wditem, numberlabel) )

def action_one_item(wditem):
  global items2do
  ara = 'ar'
  items2do -= 1
  if wditem.labels: #تسميات موجودة
    if ('en' in wditem.labels): #  تسمية انجليزية متوفرة
      numberlabel = wditem.labels['en'] #  اسم انجليزي
      data = {}
      data.update({'labels':{ara:numberlabel}})
      if debug:
        logme(wditem, numberlabel)
      else:
        wditem.editEntity(data,summary='Bot: add ar label: '+numberlabel)
        logme(wditem, numberlabel)
    else: # الوصف الإنجليزي غير موجود في القائمة
      pass
  return 1     
  return 0
      
def wd_sparql_generator(query):        
  wikidatasite=pywikibot.Site('wikidata','wikidata') 
  generator=pg.WikidataSPARQLPageGenerator(query,site=wikidatasite)
  for wd in generator:
    wd.get(get_redirect=True)
    yield wd
                                         
def wd_from_file():
  repo=pywikibot.Site('wikidata','wikidata').data_repository()
  csvfile=open(main_dir+'wd/LB.csv','r')
  for alllines in csvfile:
    qitem=alllines[alllines.find('Q'):alllines.find(',')]
    if (len(qitem)>0):
      wditem=pywikibot.ItemPage(repo,qitem)
      if (not(wditem.isRedirectPage())):
       if wditem.exists():
        wditem.get(get_redirect=True)
        yield wditem

def main():
    global itemsdone
    itemsdone = 0
    max = 10
    print ("- بدء المهمة") ## تسميات إنجليزية مجرد أرقام دون تسمية عربية
    query = 'SELECT ?item WHERE { ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en"). BIND( REGEX(STR(?cid22), "^([0-9]*)$") AS ?regexresult ) . FILTER( ?regexresult = true ) . FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .} LIMIT '+str(max)+''
    print ("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        try:
          action_one_item(wditem)
          itemsdone += 1
        except: 
          pass
          print('%s تخطي' % wditem)
    print('العناصر المكتملة: %s' % itemsdone)

if __name__ == "__main__":  
 if debugedo:
   print("debug is on")
   site=pywikibot.Site('ar')
   repo=site.data_repository()
   wd = pywikibot.ItemPage(repo,'Q17979303')
   wd.get(get_redirect=True)
   action_one_item(wd)
 else:
   print("(---------- جاهز للبدء ----------)")
   main()

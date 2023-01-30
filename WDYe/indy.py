#!/usr/bin/python
# -*- coding: utf-8  -*-
#
import pywikibot
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

def logme(wditem, newlabel,oldlabel):
  form = '\n%s\tLar\t%s\t%s'
  form2 = '%s update: %s'
  with codecs.open(main_dir+"wd/indynumber.log.csv", "a", encoding="utf-8") as logfile:
    try:   
        logfile.write(form % (wditem, newlabel,oldlabel) )
    except :
        pass
        print(" Error writing to logfile on: [%s]" %  newlabel)
    verbose = True#True    #now I want to see what!   
    logfile.close()
    if verbose:
       print(form2 % (wditem, newlabel) )
	   
def fixlabel(oldlabel):
	new = oldlabel.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤', '4')
	new2 = new.replace('٥', '5').replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')
	return new2

def action_one_item(wditem):
  global items2do
  ara = 'ar'
  items2do -= 1
  if wditem.labels: #تسميات موجودة
    if ('ar' in wditem.labels): 
      oldlabel = wditem.labels['ar'] 
      newlabel = fixlabel(oldlabel)
      data = {}
      data.update({'labels':{ara:newlabel}})
      if debug:
        logme(wditem, newlabel,oldlabel)
      else:
        logme(wditem, newlabel,oldlabel)
        wditem.editEntity(data,summary='Bot: update Arabic label: %s to %s' % (oldlabel, newlabel))
    else: 
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
  csvfile=openmain_dir+('wd/indy.csv','r')
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
    print ("- بدء المهمة تسميات بأرقام هندية") ## تسميات إنجليزية مجرد أرقام دون تسمية عربية
    #query = 'SELECT ?item WHERE { ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en"). BIND( REGEX(STR(?cid22), "^([0-9]*)$") AS ?regexresult ) . FILTER( ?regexresult = true ) . FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .} LIMIT '+str(max)+''
    query = 'SELECT ?item WHERE {  ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en").  ?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar") BIND( REGEX(STR(?itemabel), "^((٠|١|٢|٣|٤|٥|٦|٧|٨|٩)*)$") AS ?regexresult ) .  FILTER( ?regexresult = true ) . } LIMIT '+str(max)+''
    print ("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        try:
          action_one_item(wditem)
          itemsdone += 1
          print('العناصر المكتملة: %s' % itemsdone)
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

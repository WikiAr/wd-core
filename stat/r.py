#!/usr/bin/python
# -*- coding: utf-8  -*-
#

import pywikibot
from pywikibot import pagegenerators as pg
import codecs
from API.maindir import main_dir
import sys
import datetime
from datetime import datetime, date, time

replacedesc={'ar':['سياسي أميركي','',]}
taxondescs={

		'species of brachiopods	':{'ar':'نوع من ذوات القوائم الذراعية'},
		'species of ctenophore':{'ar':'نوع من الممشطيات'},
		#'species of plants':{'ar':'نوع من النباتات'},
		'section of plants':{'ar':'قسم من النباتات'},
		'subgenus of molluscs':{'ar':'جنيس من الرخويات'},
		'subfamily of worms':{'ar':'فُصيلة من الديدان'},
		'tribe of fishes':{'ar':'قبيلة من الأسماك'},
		'tribe of molluscs':{'ar':'قبيلة من الرخويات'},
		'variety of fungi':{'ar':'ضرب من الفطريات'},
		'species of plant':{'ar':'نوع من النباتات'},
		'tribe of birds':{'ar':'قبيلة من الطيور'},
		'tribe of crustaceans':{'ar':'قبيلة من القشريات'},
		'species of molluscs':{'ar':'نوع من الرخويات'},
		'tribe of myriapods':{'ar':'قبيلة من كثيرات الأرجل'},
		'subfamily of sponges':{'ar':'فُصيلة من الإسفنجيات'},
		'species of echinoderms':{'ar':'نوع من الشوكيات'},
		'species of fungi':{'ar':'نوع من الفطريات'},
		'subfamily of myriapods':{'ar':'فُصيلة من كثيرات الأرجل'},
		'subfamily of prokaryotes':{'ar':'فُصيلة من بدائيات النوى'},
		'species of fungi':{'ar':'نوع من الفطريات'},
		'subfamily of myriapods':{'ar':'فُصيلة من كثيرات الأرجل'},
		'subfamily of prokaryotes':{'ar':'فُصيلة من بدائيات النوى'},
	   }
debugedo=True
debugedo=False
debug=True

#default_query='claim[31:16521]'  #all taxons
default_language = 'ar' 

#global variables
items2do = 0
itemsdone= 0
missing_dict={}

def logme(id, desc, lab):
  form = '%s\tDar\t"%s"'
  with codecs.open("stat/r.log.csv", "a", encoding="utf-8") as logfile:
  #with open("desc/s.txt", "a") as logfile:
    formattedstring = '%s%s' % (form , '\n')
    #try:   
    logfile.write(formattedstring % (id, desc) )
        #logfile.write('%s|%s%s' %  (id, desc, '\n'))
    #except :
       #pass
       #print(" Error writing to logfile on: [%s]" %  lab)
    verbose = True#True	#now I want to see what!   
    logfile.close()
    if verbose:
       print(form % (id, desc) )   #, des

def preee(wditem, data, des, en_desc):
	if ('ar' in wditem.labels):
		lab = wditem.labels['ar']
	else:
		if ('en' in wditem.labels):
			lab = wditem.labels['en']
		else:
			lab = ' '
	if debug:
		logme(wditem.title(), des ,lab)
		
	else:
		wditem.editEntity(data,summary='Bot: add Arabic description: '+des)
		#print( '%s Item done' % wditem.id)
		#print( ': %s Item done: %s' % (lab, ar_dict[lang] ))
		#print( ': Item done: %s' % lab)
		#print( ' %s' % ar_dict[lang])
		logme( wditem.title(), des ,lab)
		#print( '%s Item done' % wditem.id)
		#print( ': %s Item done: %s' % (lab, ar_dict[lang] ))
		#print( ': item done: %s' % lab)
		#print( ' %s' % des)

def action_one_item(wditem):
  global items2do
  sss = 'en'
  items2do -= 1

  if ('en' in wditem.descriptions): #وصف انجليزي متوفر في ويكي بيانات
      en_desc = wditem.descriptions['en'] #الوصف الانجليزي
      if (en_desc in taxondescs):   #اذا كان الوصف الانجليزي في القائمة أعلاه
        data = {}
        ar_dict=taxondescs[en_desc]  #الوصف العربي
        for lang in ar_dict:
		  #foo =( '%s %s' % (lab, ar_dict[lang]))
          if ('en' in wditem.descriptions):
            if (wditem.descriptions[sss]):
              data.update({'descriptions':{lang:ar_dict[lang]}})
              preee(wditem, data, ar_dict[lang], en_desc)

      else: # الوصف الإنجليزي غير موجود في القائمة
            if en_desc in missing_dict:
                  missing_dict[en_desc] += 1
            else:
                  missing_dict.update({en_desc:1})
      return 1     
    
      return 0

def main():
	global itemsdone
	itemsdone = 0
	print ("- بدء المهمة")
	
	for desc in taxondescs:
		query = 'SELECT DISTINCT ?item WHERE { BIND("'+desc+'"@en AS ?year) ?item schema:description ?year. OPTIONAL {?item schema:description ?itemabel.FILTER((LANG(?itemabel)) = "ar")  } FILTER(!BOUND(?itemabel)) } LIMIT 5000'
		#query = 'SELECT ?item 	WHERE {  BIND("سياسي أميركي"@ar AS ?des)  ?item schema:description ?des.}'
		#pigenerator = wd_sparql_generator('SELECT ?item WHERE {  ?item wdt:P31 wd:Q16521}')
		print ("--- يتم الان تشغيل الاستعلام")
		print ("---- الوصف المطلوب %s " % desc)
		print ("---- الوصف العربي %s " % taxondescs[desc])
		#pigenerator = wd_from_file(query)
		pigenerator = wd_sparql_generator(query)
		for wditem in pigenerator:
			try:
			  action_one_item(wditem)
			  #addorreplace(wditem)
			  itemsdone += 1
			  #if itemsdone > 25  : break
			except: 
			  pass
			  print('%s pass' % wditem)
	print('Items done: %s' % itemsdone)
	
if __name__ == "__main__":  
 if debugedo:
   print("debug is on")
   site=pywikibot.Site('ar')
   repo=site.data_repository()
   wd = pywikibot.ItemPage(repo,'Q17979303')
   wd.get(get_redirect=True)
   #addorreplace(wd)
   action_one_item(wd)
 else:
   print("(---------- جاهز للبدء ----------)")
   main()

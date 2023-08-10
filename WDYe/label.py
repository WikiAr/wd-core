#!/usr/bin/python
#

import pywikibot
from pywikibot import pagegenerators as pg
import re
import codecs
import sys
import datetime
from datetime import datetime, date, time

replacedesc = {'ar': ['سياسي أميركي', '',]}
taxondescs = {
    # 'American politician' :{'ar':'سياسي أمريكي'},
    'scientific article': {'ar': 'مقالة بحثية'},  # مقالة علمية
    'family name': {'ar': 'اسم العائلة'},
    'male given name': {'ar': 'اسم مذكر معطى'},
    'badminton championships': {'ar': 'بطولة كرة الريشة'},
    'gene of the species Rattus norvegicus': {'ar': 'جين من أنواع الجرذ النرويجي'},
    'Spanish politician': {'ar': 'سياسي إسباني'},
    'German politician': {'ar': 'سياسي ألماني'},
    'x!y~z': {'ar': ''},
}
debugedo = False
debugedo = False
debug = False

# default_query='claim[31:16521]'  #all taxons
default_language = 'ar'

# global variables
items2do = 0
itemsdone = 0
missing_dict = {}


def preee(wditem, data, site):
    wditem.editEntity(data, summary='Bot: Add Arabic label: '+site)


def action_one_item(wditem):
    global items2do
    items2do -= 1
    enwiki = 'arwiki'
    if ('arwiki' in wditem.sitelinks):
        ma = wditem.sitelinks['arwiki']
        # print(ma)
        # site = ma.title
        # if site:
        # print(site)
        if ('ar' in wditem.labels):  # وصف انجليزي متوفر في ويكي بيانات
            print(' تسمية عربية متوفرة: %s ' % wditem.labels['ar'])
            pass
        else:
            print("--- يتم العمل على العنصر %s " % wditem)
            print("-- التسمية :  %s " % ma)
            data = {}
            data.update({'labels': {'ar': ma}})
            # preee(wditem, data, site)
            preee(wditem, data, ma)

    return 1

    return 0


def action_one_item2(wditem):
    global items2do
    items2do -= 1
    enwiki = 'arwiki'
    if ('arwiki' in wditem.sitelinks):
        ma = wditem.sitelinks['arwiki']
    if ('ar' in wditem.sitelinks):
        ma = wditem.sitelinks['arwiki']
        # print(ma)
        # site = ma.title
        # if site:
        # print(site)
        # print ("--- يتم العمل على العنصر %s " % wditem)
        # print ("-- التسمية :  %s " % ma )
        # data = {}
        # data.update({'labels':{'ar':ma}})
        # preee(wditem, data, site)

    return 1

    return 0


"""
def addorreplace(wditem):
  global missing_dict
  sss = 'en'
  if ('en' in wditem.descriptions): #وصف انجليزي متوفر في ويكي بيانات
    en_desc = wditem.descriptions['en'] #الوصف الانجليزي
    if (en_desc in taxondescs):   #اذا كان الوصف الانجليزي في القائمة أعلاه
      data = {}
      ar_dict=taxondescs[en_desc]  #الوصف العربي
      for lang in ar_dict:
        #foo =( '%s %s' % (lab, ar_dict[lang]))
        if (lang in wditem.descriptions): #اذا كان هناك وصف عربي متوفر
            if (wditem.descriptions[lang] in replacedesc[lang]): # اذا كان الوصف موجود في قائمة الاستبدالات
                data.update({'descriptions':{lang:ar_dict[lang]}}) #
                wditem.editEntity(data,summary='change Arabic taxondescription')  #تبديل النص
                print( ': change item description %s' % wditem.descriptions[lang])
        else: # لا يوجد وصف عربي
            data.update({'descriptions':{lang:ar_dict[lang]}}) # إضافة وصف جديد
            preee(wditem, data, ar_dict[lang], en_desc)
    else: # الوصف الإنجليزي غير موجود في القائمة
      if en_desc in missing_dict:
        missing_dict[en_desc] += 1
      else:
        missing_dict.update({en_desc:1})
    return 1     
    
    return 0
	"""


def wd_sparql_generator(query):
    wikidatasite = pywikibot.Site('wikidata', 'wikidata')
    generator = pg.WikidataSPARQLPageGenerator(query, site=wikidatasite)
    for wd in generator:
        wd.get(get_redirect=True)
        yield wd


def main():
    global itemsdone
    itemsdone = 0
    print("- بدء المهمة")

    # for desc in taxondescs:
    query = 'PREFIX schema: <http://schema.org/> PREFIX hint: <http://www.bigdata.com/queryHints#> SELECT ?item WHERE {  {    SELECT ?item WHERE {      hint:Query hint:optimizer "None".      {        SELECT ?item WHERE         {          ?sitelink schema:about ?item.          ?sitelink schema:isPartOf <https://ar.wikipedia.org/>.        }        LIMIT 27000      }      OPTIONAL { ?item rdfs:label ?nameLabelHE.  FILTER((LANG(?nameLabelHE)) = "ar") }     FILTER(!BOUND(?nameLabelHE))    }  }}LIMIT 100'
    print("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        # try:
        action_one_item(wditem)
        # addorreplace(wditem)
        itemsdone += 1
        # if itemsdone > 25  : break
        # except:
        # pass
        # print('%s pass' % (wditem)
    print('Items done: %s' % itemsdone)


if __name__ == "__main__":
    if debugedo:
        print("debug is on")
        site = pywikibot.Site('ar')
        repo = site.data_repository()
        wd = pywikibot.ItemPage(repo, 'Q17979303')
        wd.get(get_redirect=True)
        # addorreplace(wd)
        action_one_item(wd)
    else:
        print("(---------- جاهز للبدء ----------)")
        main()

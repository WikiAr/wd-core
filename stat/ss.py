#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت استعلامات عن الوصوف في ويكي بيانات 

عن الأصنوفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
from pywikibot import pagegenerators as pg
import codecs
from API.maindir import main_dir
from wikidatafun import *
targetlangs = ['ar']
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

def action(total, translation, targetlang,des,name):
   # with codecs.open("o/"+aas+".log.csv", "a", encoding="utf-8") as logfile:
   # with codecs.open("stat/q.log.csv", "a", encoding="utf-8") as logfile:
    with codecs.open("stat/new/"+ (name or 'q')+".log.csv", "a", encoding="utf-8") as logfile:

        form = "%d\t'\t%s\t':{'ar':'\t%s\t'},"
        formattedstring = '%s%s' % (form , '\n')
        try:   
           if total > 10:
               logfile.write(formattedstring %  (total, translation, des))
        except :
           pass
    verbose = True#True	#now I want to see what!   
    logfile.close()
    if verbose:
        print(form % (total, translation, des) )   #, des

def main(translationsNationalities,translationsOccupations):
    translations = {}
    for natkey, natdic in translationsNationalities.items():  # المهن 
        for occupkey, occupdic in translationsOccupations.items():   # الجنسيات
            translations[re.sub('~', natkey, occupkey)] = {}
            for translang in occupdic.keys():                      # المهن حسب اللغة
                #print(occupkey, natkey, translang)
                translations[re.sub('~', natkey, occupkey)][translang] =re.sub('~', natdic[translang], occupdic[translang])# {
                    #re.sub('~', natdic[translang], occupdic[translang]),  '': , }
                name = natkey
                name = natkey
                   
                
    c2 = 1
    total2 = 0
    cqueries = 0
    translations_list = list(translations.keys())
    translations_list.sort()
    totalqueries = len(translations_list) * len(targetlangs)# * len(genders_list) # عدد الاستعلامات للذكور والاناث
    skiptolang = '' #'es'                                                       # لغة يتم تجاهلها 
    skiptoperson = '' #'American politician'                               # وصف يتم تجاهله
    for targetlang in targetlangs:
        if skiptolang:
            if skiptolang != targetlang:         # تجاهل لغة
                print('تخطي اللغة:', targetlang)
                continue
            else: 
                skiptolang = ''
        for translation in translations_list:
            #print(targetlang, translation, translations[translation][targetlang])                 #dddd
            #print(targetlang, translation)
            if skiptoperson:
                if skiptoperson != translation:      # تجاهل وصف 
                   print('Skiping translation:', translation)
                   continue
                else:
                   skiptoperson = ''
            #  الاستعلام
            max = 100000
            url = 'https://query.wikidata.org/bigdata/namespace/wdq/sparql?query=SELECT%20%3Fitem%0AWHERE%20%7B%0A%20%20%20%20%3Fitem%20schema%3Adescription%20%22'+urllib.parse.quote(translation)+'%22%40en.%20%23description%0A%20%20%20%20OPTIONAL%20%7B%20%3Fitem%20schema%3Adescription%20%3FitemDe.%20FILTER(LANG(%3FitemDe)%20%3D%20%22'+targetlang+'%22).%20%20%7D%0A%20%20%20%20FILTER%20(!BOUND(%3FitemDe))%0A%7D%0Alimit%20'+str(max)+''
            url = '%s&format=json' % (url)
            sparql = getURL(url=url)
            json1 = loadSPARQL(sparql=sparql)
            total = len(json1['results']['bindings'])
            total2 += total
            #print(targetlang, translation, translations[translation][targetlang], total)
            #print('\n%d items; dis:%s; %s:%s; items %d/%d; queries %d/%d' % (total, translation, targetlang,translations[translation][targetlang], c2, total2, cqueries, totalqueries))
            action(total, translation, targetlang,translations[translation][targetlang],name) # بدء العمل 
    print("انتهت بنجاح")

if __name__ == "__main__":
    main(translationsNationalities,translationsOccupations)

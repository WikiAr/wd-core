#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import lab33
#---
xsxsx = {}
cat1 = {}
#cat1['en'] = ["Current_events_archives" , "April_events", "Events_by_month"]
#---
xsxsx['en2'] = [
    #"?item wdt:P31 wd:Q39911.",        #حسب البلد
    #"?item wdt:P971 wd:Q29053180.",    #حسب السنة
    "?item wdt:P971 wd:Q21821348.",     #سنة الولادة
    #---
    "?item wdt:P31 wd:Q578.",           #قرن
    "?item wdt:P31 wd:Q39911.",         #عقد    
    "?item wdt:P31 wd:Q577.",           #سنة
    "?item wdt:P31 wd:Q577.",           #سنة
    "?item wdt:P31 wd:Q577.",           #شهر
    #---
    "?item wdt:P31 wd:Q4167836.?item wdt:P971 ?P971.?P971 wdt:P31 wd:Q578.",            #تصانيف عقود
    "?item wdt:P31 wd:Q4167836.?item wdt:P971 ?P971.?P971 wdt:P31 wd:Q39911.",          #تصانيف عقود
    "?item wdt:P31 wd:Q4167836.?item wdt:P971 ?P971.?P971 wdt:P31 wd:Q577.",            #تصانيف سنوات
    ]
#---
#cat1['war'] = ["Kaarangay:Himo_hin_bot"]
#cat1['ceb'] = ["Kategoriya:Paghimo ni bot"]
#cat1['sv'] = ["Kategori:Robotskapade_artiklar"]
#---
#wiki = 'ceb'
#---
cat1['en'] = []
timee = [ 
    "Q36507",   #ألفية  6
    "Q578",     #قرن    7
    "Q39911",   #عقد    8
    "Q577",     #سنة    9
    "Q5151",    #شهر    10
    "Q573",     #يوم    11
    "Q25235",   #ساعة   12
    "Q7727",    #دقيقة  13
    "Q11574",   #ثانية  14
    ]
#---
for tee in timee:
    cat1['en'].append("?item wdt:P31 wd:%s." % tee)                                     # حالة خاصة من
    t2 = "?item wdt:P31 wd:Q4167836.?item wdt:P971 ?P971.?P971 wdt:P31 wd:%s." % tee    #تصانيف
    cat1['en'].append(t2)
#---
for wiki in cat1.keys():
    #---
    #lab33.main2(q11)
    lab33.sparql(cat1[wiki], wiki)
    #---
#---
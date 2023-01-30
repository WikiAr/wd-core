#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إيجاد أسماء البلدان الناقصة

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import codecs
from API.maindir import main_dir

from API import printe
import pywikibot
ALL_Dedcade = [
        "0s BC in Europe"
        ,"0s in Asia"
        ,"0s in Europe"
        ,"0s in the Roman Empire"
        ,"1000s in Africa"
        ,"1000s in Asia"
    ]
    
from NewCategories import NewCate
from ALL_decades import ALL_Decade
from ALL_Centry import ALL_Centries
from ALL_Years import ALL_Year
from estype import establishments
from distype import disestablishments
from type.cate_P17 import *
#---
popo = {}
#for sasa in [ALL_Dedcade]:  
for sasa in [ALL_Decade , ALL_Centries , ALL_Year , disestablishments , establishments]:  
    for cao in sasa:  
        cao = re.sub('_' , ' ' , cao)
        ca = cao.split('in ')[1]
        ca = ca.lower()
        if ca not in popo:
            popo[ca] = 1
        else:
            popo[ca] = popo[ca] + 1
#---
P17_final__ ={}
for P17 in P17_final.keys():  
    p1 = P17.lower()
    P17_final__[p1] = P17_final[P17]
#---
nu = 0
for cao2 in popo:  
    if not cao2 in P17_final__.keys():  
        nu += 1
        ss = '%s\t%d\n' % (cao2 , popo[cao2])
        printe.output( str(cao2) + ' ' + str(popo[cao2]))
        with codecs.open('list/miss_ss2.csv', "a", encoding="utf-8") as logfile:
            logfile.write(ss)
            logfile.close()
#---
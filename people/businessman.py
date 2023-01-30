#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت إضافة الوصوف عن الأشخاص في ويكي بيانات
 
جميع اللغات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
from people.n import *
#import Nationalities as aa
# python pwb.py people/all
# python pwb.py people/businessman

Tabcr = {}
Tabcr["Nationalities"] = translationsNationalities
#Tabcr["Occupations"] = oc.translationsOccupations
Tabcr["Occupations"] = { 
	'~ businessman' : oc.translationsOccupations['~ businessman']
	, '~ businesswomen' : oc.translationsOccupations['~ businesswomen']
	}
#---
TraNat = Tabcr["Nationalities"]
TraOc = Tabcr["Occupations"]
#---
skipnatkey = ''
#---
translations_oi = {}
for natkey, natdic in TraNat.items():   # الجنسيات
    if natkey != skipnatkey:
        for occupkey, occupdic in TraOc.items():  # المهن 
            translations_oi[re.sub('~', natkey, occupkey)] = {}
            talang = occupdic.keys()
            #talang = ['ar']
            for translang in talang:                      # المهن حسب اللغة
                if translang in natdic:
                    #pywikibot.output(occupkey + '\t' + natkey + '\t' + translang)
                    translations_oi[re.sub('~', natkey, occupkey)][translang] = {
                        'male': re.sub('~', natdic[translang]['male'], occupdic[translang]['male']), 
                        'female': re.sub('~', natdic[translang]['female'], occupdic[translang]['female']), 
                    }
#---
if __name__ == "__main__":
    main2( translations_oi )
#---
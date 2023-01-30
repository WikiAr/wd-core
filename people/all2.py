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
#import new
from people.new import *
#import Nationalities as aa
# python pwb.py people/all
# python pwb.py people/all

Tabcr = {}
Tabcr["Nationalities"] = translationsNationalities
Tabcr["Occupations"] = oc.translationsOccupations

if __name__ == "__main__":
    main(Tabcr)
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
#from people.new import *
from people.new import *
#import Nationalities as aa

Tabcr = {}
Tabcr["Nationalities"] = Tab["Nationalities"]
#Tabcr["Nationalities"] ={ 'New Zealander': Tab["Nationalities"][ 'New Zealander' ] }
#Tabcr["Nationalities"] ={ 'Chinese': Tab["Nationalities"][ 'Chinese' ] }
Tabcr["Nationalities"] ={ 'Yemeni': Tab["Nationalities"][ 'Yemeni' ] }
#Tabcr["OccupatiCons"] = { '~ activist'  : Tab["Occupations"][ 'C~ activist' ] } 
#Tabcr["Occupations"] = { '~ footballer'  : Tab["Occupations"][ '~ footballer' ] } 
Tabcr["Occupations"] = Tab["Occupations"]
#Tabcr["Occupations"] = { '~ lexicographer'  : Tab["Occupations"]['~ lexicographer' ] } 

if __name__ == "__main__":
    main(Tabcr)

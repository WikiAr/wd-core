#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت إضافة الوصوف عن الأشخاص في ويكي بيانات
 
جميع اللغات

python3 pwb.py people/ff


"""
#
# (C) Ibrahem Qasim, 2022
#
#python pwb.py people/ff
#import new
#from people.new import *
from people.new import *
#import Nationalities as aa

Tabcr = {}
Tabcr["Nationalities"] = Tab["Nationalities"]
#Tabcr["Nationalities"] ={ 'New Zealander': Tab["Nationalities"][ 'New Zealander' ] }
#Tabcr["Nationalities"] ={ 'Austrian': Tab["Nationalities"][ 'Austrian' ] }
#Tabcr["Nationalities"] ={ 'Chinese': Tab["Nationalities"][ 'Chinese' ] }
#Tabcr["Nationalities"] ={ 'French': Tab["Nationalities"][ 'French' ] }
#Tabcr["Occupations"] = { '~ activist'  : Tab["Occupations"][ '~ activist' ] } 
#Tabcr["Occupations"] = { '~ footballer'  : Tab["Occupations"][ '~ footballer' ] } 
Tabcr["Occupations"] = Tab["Occupations"]
Tabcr["Occupations"] = { '~ sprinter'  : Tab["Occupations"]['~ sprinter' ] } 

if __name__ == "__main__":
    main(Tabcr)
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
import ss
from occupations import *
translationsNationalities = {
		'Infrafamily of':{'ar':'فصيلة ثانوية من'},
		'Infrakingdom of':{'ar':'مملكة فرعية من'},
		'Infralegion of':{'ar':'تحت فيلق من'},
		'Infraorder of':{'ar':'رتبة فرعية من'},

    }
	
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

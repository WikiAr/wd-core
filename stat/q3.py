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
		'Group of':{'ar':'مجموعة من'},
		'Hyperfamily of':{'ar':'فصيلة متوسطة من'},
		'Hyperorder of':{'ar':'رتبة متوسطة من'},
		'Hypoorder of':{'ar':'نطاق من'},

    }
	
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

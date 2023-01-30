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
		'Infraclass of':{'ar':'صُنيف فرعي من'},
		'Infracohort of':{'ar':'أترابية فرعية من'},
		'Infradivision of':{'ar':'شعبة فرعية من'},
		'Infradivision of':{'ar':'كتيوبية من'},

    }
	
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

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
		'Superclass of':{'ar':'عمارة من'},
		'Supercohort of':{'ar':'أترابية عليا من'},
		'Superdivision of':{'ar':'فرقة عليا من'},
    }
	
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

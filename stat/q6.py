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
		'Subseries of':{'ar':'سلسلية من'},
		'Subspecies of':{'ar':'نُويع من'},
		'Subvariety of':{'ar':'ضُّريب من'},
		
    }
	
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

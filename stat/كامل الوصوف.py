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
		'Branch of':{'ar':'فرع من'},
		'Capaxorder of':{'ar':'رتبة كبرى من'},
		'Class of':{'ar':'طائفة من'},
		'Cohort of':{'ar':'أترابية من'},
		'Division of':{'ar':'فرقة من'},
		'Domain of':{'ar':'نطاق من'},
		'Epifamily of':{'ar':'فصيلة إضافية من'},
		'Family of':{'ar':'فصيلة من'},
		'Gigafamily of':{'ar':'فصيلة عملاقة من'},
		'Gigaorder of':{'ar':'رتبة عملاقة من'},
		'Grandfamily of':{'ar':'فصيلة كبرى من'},
		'Grandorder of':{'ar':'رتبة كبرى من'},
		'Group of':{'ar':'مجموعة من'},
		'Hyperfamily of':{'ar':'فصيلة متوسطة من'},
		'Hyperorder of':{'ar':'رتبة متوسطة من'},
		'Hypoorder of':{'ar':'نطاق من'},
		'Infraclass of':{'ar':'صُنيف فرعي من'},
		'Infracohort of':{'ar':'أترابية فرعية من'},
		'Infradivision of':{'ar':'شعبة فرعية من'},
		'Infradivision of':{'ar':'كتيوبية من'},
		'Infrafamily of':{'ar':'فصيلة ثانوية من'},
		'Infrakingdom of':{'ar':'مملكة فرعية من'},
		'Infralegion of':{'ar':'تحت فيلق من'},
		'Infraorder of':{'ar':'رتبة فرعية من'},
		'Infraphylum of':{'ar':'شعبة فرعية من'},
		'Infratribe of':{'ar':'قبيلة فرعية من'},
		'Kingdom of':{'ar':'مملكة من'},
		'Legion of':{'ar':'فوق من'},
		'Magnorder of':{'ar':'رتبة ضخمة من'},
		'Megafamily of':{'ar':'فصيلة ضخمة من'},
		'Megaorder of':{'ar':'رتبة ضخمة من'},
		'Microorder of':{'ar':'رتبة دقيقة من'},
		'Microphylum of':{'ar':'شعبة دقيقة من'},
		'Minorder of':{'ar':'نطاق من'},
		'Mirorder of':{'ar':'رتبة متوسطة من'},
		'Nanorder of':{'ar':'نطاق من'},
		'Order of':{'ar':'رتبة من'},
		'Parvclass of':{'ar':'طيؤوفية من'},
		'Parvkingdom of':{'ar':'مملكة صغرى من'},
		'Parvorder of':{'ar':'رتبة صغرى من'},
		'Phylum of':{'ar':'شعبة من'},
		'Species of':{'ar':'نوع من'},
		'Subclass of':{'ar':'طويئفة من'},
		'Subcohort of':{'ar':'أباشة من'},
		'Subdivision of':{'ar':'كتيبة من'},
		'Subkingdom of':{'ar':'عويلم من'},
		'Sublegion of':{'ar':'فيلق ثانوي من'},
		'Suborder of':{'ar':'رتيبة من'},
		'Subsection of':{'ar':'قسيم من'},
		'Subseries of':{'ar':'سلسلية من'},
		'Subspecies of':{'ar':'نُويع من'},
		'Subvariety of':{'ar':'ضُّريب من'},
		'Superclass of':{'ar':'عمارة من'},
		'Supercohort of':{'ar':'أترابية عليا من'},
		'Superdivision of':{'ar':'فرقة عليا من'},
		'Supergenus of':{'ar':'سبط من'},
		'Superlegion of':{'ar':'فوق فيلق من'},
		'Superorder of':{'ar':'رتبة عليا من'},
		'Superphylum of':{'ar':'شعبة عليا من'},
		'Superspecies of':{'ar':'فوق نوع من'},
		'Supertribe of':{'ar':'قبيلة عليا من'},
		'form of':{'ar':'شكل من'},

    }
done = {
		#'Genus of':{'ar':'جنس من'},
		#'Series of':{'ar':'سلسلة من'},
		#'Section of':{'ar':'قسم من'},
		#'Superfamily of':{'ar':'فصيلة عليا من'},
		#'Subfamily of':{'ar':'فُصيلة من'},
		#'Tribe of':{'ar':'قَبيلة من'},
		#'Subtribe of':{'ar':'عميرة من'},
		#'Subgenus of':{'ar':'جُنيس من'},
		#'Order of':{'ar':'رتبة من'},
		#'Family of':{'ar':'فصيلة من'},
		#'Genus of':{'ar':'جنس من'},
		#'Species of':{'ar':'نوع من'},
		#'Variety of':{'ar':'ضَرْب من'},
    }
if __name__ == "__main__":
    ss.main(translationsNationalities,translationsOccupations)

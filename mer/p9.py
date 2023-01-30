#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

دمج صفحات العزل

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import re
import pywikibot
import codecs
#---
import sys
categories = {
    "Kategoriya:Mga subdibisyon sa Al Mahrah (lalawigan)" : "تصنيف:عزل محافظة المهرة" , 
    "Kategoriya:Mga subdibisyon sa Al Maḩwīt (lalawigan)" : "تصنيف:عزل محافظة المحويت" , 
    "Kategoriya:Mga subdibisyon sa Amanat Al Asimah" : "تصنيف:عزل صنعاء" , #########
    "Kategoriya:Mga subdibisyon sa Ibb (lalawigan)" : "تصنيف:عزل محافظة إب" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Abyan" : "تصنيف:عزل محافظة أبين" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Bayḑā'" : "تصنيف:عزل محافظة البيضاء (اليمن)" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Jawf" : "تصنيف:عزل محافظة الجوف (اليمن)" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Ḩudaydah" : "تصنيف:عزل محافظة الحديدة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at aḑ Ḑāli‘" : "تصنيف:عزل محافظة الضالع" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Dhamār" : "تصنيف:عزل محافظة ذمار" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Laḩij" : "تصنيف:عزل محافظة لحج" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ma'rib" : "تصنيف:عزل محافظة مأرب" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Raymah" : "تصنيف:عزل محافظة ريمة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ta‘izz" : "تصنيف:عزل محافظة تعز" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Şa‘dah" : "تصنيف:عزل محافظة صعدة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ḩajjah" : "تصنيف:عزل محافظة حجة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ḩaḑramawt" : "تصنيف:عزل محافظة حضرموت" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at ‘Adan" : "تصنيف:عزل محافظة عدن" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at ‘Amrān" : "تصنيف:عزل محافظة عمران" , 
    "Kategoriya:Mga subdibisyon sa Sanaa (lalawigan)" : "تصنيف:عزل محافظة صنعاء" , 
    "Kategoriya:Mga subdibisyon sa Shabwah" : "تصنيف:عزل محافظة شبوة" , 
    "Kategoriya:Mga subdibisyon sa Socotra (lalawigan)" : "تصنيف:عزل محافظة أرخبيل سقطرى" 
    }
import p
#---
wiki1 = 'ceb'
arwiki = 'ar'
if __name__ == "__main__":
    p.main2(categories, wiki1, arwiki)
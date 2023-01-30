#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إيجاد تسمية عربية من خلال قوالب 
geobox

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import g

categories = {
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
#---   
if __name__ == '__main__':
     g.main(categories)
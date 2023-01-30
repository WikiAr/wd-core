#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
#---
import sys
#---
#import catenlog
import caten
#---
from type.cate_type import *
pop_fi = {}
for sao in [pop_start , New_Pop , New_Pop2]:
    for sasas in sao.keys():
        pop_fi[sasas] = sao[sasas]
#---
#from type.cate_P17 import *

'''

هذه التصانيف تستخدم السنوات والعقود والقرون

'''
poo = {
    "politics"  : { "ar" : "السياسة" , "Q" : "Q7163" } ,   #   1053
    "religion"  : { "ar" : "الدين" , "Q" : "Q9174" } ,   #   933
    "Christianity"  : { "ar" : "المسيحية" , "Q" : "Q5043" } ,   #   748
    "art"   : { "ar" : "الفن" , "Q" : "Q735" } ,   #   690
    "science"   : { "ar" : "العلم" , "Q" : "Q336" } ,   #   680
    "sports "   : { "ar" : "الرياضة" , "Q" : "Q349" } ,   #   644
    "law"   : { "ar" : "القانون" , "Q" : "Q7748" } ,   #   578
    "military history"  : { "ar" : "التاريخ العسكري" , "Q" : "Q192781" } ,   #   570
    "fiction"   : { "ar" : "الخيال" , "Q" : "Q8253" } ,   #   510
    "music" : { "ar" : "الموسيقى" , "Q" : "Q638" } ,   #   473
    "transport" : { "ar" : "النقل" , "Q" : "Q7590" } ,   #   460
    "the environment"   : { "ar" : "البيئة" , "Q" : "Q2249676" } ,   #   213
    "arts"  : { "ar" : "الفنون" , "Q" : "Q2018526" } ,   #   183
    "international relations"   : { "ar" : "العلاقات الدولية" , "Q" : "Q166542" } ,   #   448
    "economics" : { "ar" : "الاقتصاد" , "Q" : "Q8134" } ,   #   384
    "theatre"   : { "ar" : "المسرح" , "Q" : "Q11635" } ,   #   332
    "cricket"   : { "ar" : "الكريكت" , "Q" : "Q5375" } ,   #   298
    "horse racing"  : { "ar" : "سباق الخيل" , "Q" : "Q187916" } ,   #   272
    "rail transport"    : { "ar" : "السكك الحديدية" , "Q" : "Q3565868" } ,   #   272
    "education" : { "ar" : "التعليم" , "Q" : "Q8434" } ,   #   238
    "chess" : { "ar" : "الشطرنج" , "Q" : "Q718" } ,   #   172
    "association football"  : { "ar" : "كرة القدم" , "Q" : "Q2736" } ,   #   171
    "paleontology"  : { "ar" : "علم الأحياء القديمة" , "Q" : "Q7205" } ,   #   162
    "Gaelic games"  : { "ar" : "" , "Q" : "Q2447366" } ,   #   160
    "technology"    : { "ar" : "التقانة" , "Q" : "Q11016" } ,   #   160
    "Judo"    : { "ar" : "الجودو" , "Q" : "Q11420" } ,   #   160
    "baseball"  : { "ar" : "كرة القاعدة" , "Q" : "Q5369" } ,   #   160
    "rugby union"   : { "ar" : "اتحاد الرجبي" , "Q" : "Q5849" } ,   #   158
    "golf"  : { "ar" : "الغولف" , "Q" : "Q5377" } ,   #   156
    "film"  : { "ar" : "الأفلام" , "Q" : "Q11424" } ,   #   155
    "literature"    : { "ar" : "الأدب" , "Q" : "Q8242" } ,   #   154
    "women's history"   : { "ar" : "تاريخ المرأة" , "Q" : "Q1279400" } ,   #   144
    "rugby league"  : { "ar" : "دوري الرغبي" , "Q" : "Q10962" } ,   #   143
    "tennis"    : { "ar" : "كرة المضرب" , "Q" : "Q847" } ,   #   143
    "ice hockey"    : { "ar" : "هوكي الجليد" , "Q" : "Q41466" } ,   #   142
    #"Norwegian music"   : { "ar" : "" , "Q" : "" } ,   #   155
    #"Australian cricket"    : { "ar" : "" , "Q" : "" } ,   #   136
    #"labour relations"  : { "ar" : "علاقات عمل" , "Q" : "" } ,   #   157
    #"Ontario"   : { "ar" : "أونتاريو" , "Q" : "" } ,   #   178
    #"Quebec"    : { "ar" : "كيبك" , "Q" : "" } ,   #   174
    #"New Brunswick" : { "ar" : "" , "Q" : "" } ,   #   173
    #"Alberta"   : { "ar" : "" , "Q" : "" } ,   #   151
    #"Burma" : { "ar" : "" , "Q" : "" } ,   #   141
    
    #"American law"  : { "ar" : "" , "Q" : "" } ,   #   237
    #"United States case law"    : { "ar" : "" , "Q" : "" } ,   #   225
    #"European sport"    : { "ar" : "" , "Q" : "" } ,   #   224
    #"sports by country" : { "ar" : "" , "Q" : "" } ,   #   223
    #"English sport" : { "ar" : "" , "Q" : "" } ,   #   294
    #"North American sport"  : { "ar" : "" , "Q" : "" } ,   #   177
    "American football" : { "ar" : "كرة القدم الأمريكية" , "Q" : "Q41323" } ,   #   152
    "Australian rules football" : { "ar" : "كرة القدم الأسترالية" , "Q" : "Q50776" } ,   #   145
    "winter sports" : { "ar" : "رياضة شتوية" , "Q" : "Q204686" } ,   #   145
    #"Welsh sport"   : { "ar" : "" , "Q" : "" } ,   #   143
    #"South American sport"  : { "ar" : "" , "Q" : "" } ,   #   143
    "women's sport" : { "ar" : "رياضة نسوية" , "Q" : "Q920057" } ,   #   140
    #"Canadian sports"   : { "ar" : "" , "Q" : "" } ,   #   139
    #"women's sport by country"  : { "ar" : "" , "Q" : "" } ,   #   138
    #"Scottish sport"    : { "ar" : "" , "Q" : "" } ,   #   159
    #"Irish sport"   : { "ar" : "" , "Q" : "" } ,   #   158
    #"American sports"   : { "ar" : "" , "Q" : "" } ,   #   158
    #"Oceanian sport"    : { "ar" : "" , "Q" : "" } ,   #   152
    #"Australian sport"  : { "ar" : "" , "Q" : "" } ,   #   151
    #"British sport" : { "ar" : "" , "Q" : "" } ,   #   294
    #"English cricket"   : { "ar" : "" , "Q" : "" } ,   #   294
    #"the United States by state"    : { "ar" : "" , "Q" : "" } ,   #   277
    #"British law"   : { "ar" : "" , "Q" : "" } ,   #   257
    #"case law"  : { "ar" : "" , "Q" : "" } ,   #   247
    #"the United States by city" : { "ar" : "" , "Q" : "" } ,   #   240
    #"American politics" : { "ar" : "" , "Q" : "" } ,   #   239
    }
#---
poiuh = '''
python pwb.py category/usa d:a
python pwb.py category/usa d:y
python pwb.py category/usa d:d
python pwb.py category/usa d:c
python pwb.py category/usa d:f
'''
#---
if __name__ == "__main__":
    #print('lenth : ' + str( lenth) )
    soo344 = {}
    type = ''
    file = 'usa'
    for arg in sys.argv:#
        arg, sep, value = arg.partition(':')
        if arg =='d':
            type = value
            if value == 'a':
                soo344 , file =  pop_fi,'usa'
            elif value == 'y':
                soo344 , file =  years__,'usa_years'
            #elif value == 'ydc':
                #soo344 , file =  ydc,'usa_ydc'
            elif value == 'd':
                soo344 , file =  decade__,'usa_decade'
            elif value == 'c':
                soo344 , file =  century__,'usa_century'
            elif value == 'f':
                soo344 , file =  pop_final,'usa_final'
    lenth = len(soo344.keys() ) * len(poo.keys() )    
    print('file: ' + file + ' , lenth : ' + str( lenth) )
    #catenlog.yemen(poo , soo344,file)
    caten.D_Y_C(poo , soo344 , type)
#---
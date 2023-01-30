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

import p

categories = {
    "category:Naselja u jemenskoj pokrajini Sada" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - صعدة" #) (2,582 P)

    }
categories1 = {
    "category:Naselja u jemenskoj pokrajini Abjan" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - أبين" #) (13 P)
    , "category:Naselja u jemenskoj pokrajini Ad Dali" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - الضالع" #) (11 P)
    , "category:Naselja u jemenskoj pokrajini Adan" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - عدن" #) (8 P)
    , "category:Naselja u jemenskoj pokrajini Al Baida" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - البيضاء" #) (506 P)
    , "category:Naselja u jemenskoj pokrajini Al Džauf" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - الجوف" #) (691 P)
    , "category:Naselja u jemenskoj pokrajini Al Hudaida" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - الحديدة" #) (41 P)
    , "category:Naselja u jemenskoj pokrajini Al Mahra" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - المهرة" #) (19 P)
    , "category:Naselja u jemenskoj pokrajini Al Mahvit" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - المحويت" #) (9 P)
    , "category:Naselja u jemenskoj pokrajini Amran" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - عمران" #) (800 P)
    , "category:Naselja u jemenskoj pokrajini Dhamar" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - ذمار" #) (12 P)
    , "category:Naselja u jemenskoj pokrajini Hadramaut" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - حضرموت" #) (55 P)
    , "category:Naselja u jemenskoj pokrajini Hadžah" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - حجة" #) (2,593 P)
    , "category:Naselja u jemenskoj pokrajini Ib" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - إب" #) (22 P)
    , "category:Naselja u jemenskoj pokrajini Lahidž" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - لحج" #) (41 P)
    , "category:Naselja u jemenskoj pokrajini Marib" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - مأرب" #) (499 P)
    , "category:Naselja u jemenskoj pokrajini Raima" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - ريمة" #) (499 P)
    , "category:Naselja u jemenskoj pokrajini Sada" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - صعدة" #) (2,582 P)
    , "category:Naselja u jemenskoj pokrajini Sana" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - محافظة صنعاء" #) (79 P)
    , "category:Naselja u jemenskoj pokrajini Šabva" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - شبوة" #) (45 P)
    , "category:Naselja u jemenskoj pokrajini Taiz" : "تصنيف:صفحات تستخدم قالب منطقة يمنية - تعز" #) (619 P)
    }
#---   
wiki1 ='sh'
arwiki ='ar'
if __name__ == "__main__":
    p.main2(categories1, wiki1, arwiki)
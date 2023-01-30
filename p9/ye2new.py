#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

العمل مع ملف

NewCategories

تصانيف لا تحتوي _in_
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
#---
from type.cate_type import *   #pop_start , years__,decade__ , century__, New_Pop , New_Pop2 , millennium__
from type.cate_P17 import *#ALL_P17#USA_P17#P17_final#New_P174
#---
YDC_P17 = {}
for toad in [P17_final , pop_final_Without_Years]:
    for ci in toad:
        ci2 = ci.lower()
        ci2 = ci2.split(' in')[0]
        ci2 = ci2.split(' of')[0]
        YDC_P17[ci2] = toad[ci]
        
YDC_P17['births'] = { "ar" : "مواليد" , "Q" : "Q21821348" }
YDC_P17['deaths'] = { "ar" : "وفيات" , "Q" : "Q21160456" }
YDC_P17['works'] = { "ar" : "أعمال" , "Q" : "Q42213" }
#---
from type.cate_type import *   #years__#decade__#century__#
from type.yearnew import *#years__new
#---
YDC_C = {}
for toad in [ decade__ , century__ , years__new , millennium__]: #years__
    for ci in toad:
        ci2 = ci.split(' in')[0]
        YDC_C[ci2] = toad[ci]
#---
from list.NewCategories import NewCate
import y
#---
def yemen():
    num = 0
    tit = ''
    pywikibot.output( 'start with "%s":' % tit)
    lenth =  len(NewCate) 
    #from done2 import donelist
    #tit = 'disestablishments'
    #tit = 'establishments'
    tito = '(\d+\s*BC|\d+\s*BCE|\d+)\s*.*'
    tita = '(\d+\s*BC|\d+\s*BCE|\d+)\s*(.*)'
    #mha = islahvillage
    for category in NewCate:
        num += 1
        category = re.sub('_' , ' ', category )
        year = re.sub(tito , '\g<1>', category )
        #pywikibot.output( 'year "%s"' % year)
        #year = year.split('\d+_BCE_')[0]
        #year = year.split('\d+_')[0]
        #year = year.split(tito)[0]
        contry = re.sub(tita , '\g<2>', category )
        arlabel = ""
        #---
        if contry in YDC_P17 and year in YDC_C:
            pywikibot.output( 'a<<lightblue>>>p:%s, %s: ,cat:"%s"' % (YDC_P17[contry]['ar'] , YDC_C[year]['ar']  , category) )
            if YDC_C[year]['ar'] != '' and YDC_P17[contry]['ar'] != '':
                con_lab = YDC_P17[contry]['ar']
                year_lab = YDC_C[year]['ar']
                gov_pp = con_lab.split(' في')[0]
                year_pp = year_lab.split(' في')[0]
                #arlabel = "تصنيف:" + tita_Q[tit]['priff'] + ' ' + year_pop["ar"] + " " + YDC_P17[contry]["ar"]
                arlabel = "تصنيف:" + gov_pp + " " + year_pp
                if con_lab == "حسب البلد":
                    arlabel = "تصنيف:" + year_pp + " " +  gov_pp
                pywikibot.output( 'a<<lightblue>>>ar:%s' % arlabel )
        #---
        #pywikibot.output( 'contry "%s"' % contry)
        y.New_Work(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel)
#---
if __name__ == "__main__":
    yemen()
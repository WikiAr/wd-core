#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

العمل مع ثلاثة ملفات
ALL_Years
ALL_Centry
ALL_decades

تصانيف تحتوي _in_
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
from type.cate_type import *   #pop_start , years__,decade__ , century__, New_Pop , New_Pop2
from list.ALL_Centry import ALL_Centries
from list.ALL_decades import ALL_Decade
from list.ALL_Years import ALL_Year
#from list.NewCategories import *#NewCate
#---
from type.yearnew import *#years__new
YDC_C = {}
#for toad in [decade__ , century__, years__new  ,pop_start , New_Pop , New_Pop2 , millennium__]:#years__
for toad in [decade__ , century__, years__new  , millennium__ , years__]:#
    for ci in toad:
        YDC_C[ci] = toad[ci]
#---
from type.cate_P17 import *#ALL_P17#USA_P17#P17_final#New_P173
YDC_P17 = {}
for toad in [New_P174]:#P17_final , pop_final_Without_Years]:
    for ci in toad:
        ci2 = ci.lower()
        YDC_P17[ci2] = toad[ci]
#---
tita = {
    'y' : ALL_Year
    ,'d' : ALL_Decade
    ,'c' : ALL_Centries
    #,'n' : NewCate
    }
import y
#---
def yemen(tittable):
    num = 0
    pywikibot.output( 'start with "%s":')
    lenth =  len(tittable) 
    #from done2 import donelist
    tit = ''
    tito = ' in '
    #mha = islahvillage
    for category in tittable:
        num += 1
        #category = re.sub(' ' , '_' , category)
        
        #pywikibot.output( '<<lightyellow>>>> category: %s ' % category )
        year = category.split(tito)[0]
        year = year + ' in'
        #try:
        contry = category.split(tito)[1]
        contry = contry.lower()
        arlabel = ""
        #---
        if contry in YDC_P17 and year in YDC_C:
            pywikibot.output( 'a<<lightblue>>>p:%s, %s: ,cat:"%s"' % (YDC_P17[contry]['ar'] , YDC_C[year]['ar']  , category) )
            if YDC_C[year]['ar'] != '' and YDC_P17[contry]['ar'] != '':
                con_lab = YDC_P17[contry]['ar']
                year_lab = YDC_C[year]['ar']
                #arlabel = "تصنيف:" + tita_Q[tit]['priff'] + ' ' + year_pop["ar"] + " " + YDC_P17[contry]["ar"]
                arlabel = "تصنيف:" + year_lab + " " + con_lab
                pywikibot.output( 'a<<lightblue>>>ar:%s' % arlabel )
                #if con_lab == "حسب البلد":
                    #arlabel = "تصنيف:" + year_pp + " " +  gov_pp
        #---
        y.New_Work(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel)
            
        #except:
            #pywikibot.output( '<<lightyellow>> except: %s ' % category )
#---
the_new_contry = {
    "python pwb.py p971/ye d",
    "python pwb.py p971/ye c",
    }
#---
def main():
    tit = 'y'
    for value in sys.argv:
        #arg, sep, value = arg.partition(':')
        if value == 'c':
            tit = 'c'
        elif value == 'd':
            tit = 'd'
        elif value == 'y':
            tit = 'y'
        #elif value == 'n':
            #tit = 'n'
    #---
    print('tit: %s' % tit)
    if not tit in tita:
        print('tit: %s not in tita' % tit)
    else:
        yemen(tita[tit])
#---
if __name__ == "__main__":
    #main()
    yemen(tita['y'])
    yemen(tita['d'])
    yemen(tita['c'])
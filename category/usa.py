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
'''ydc = {}
for sao in [years__ , decade__ , century__]:
    for sasas in sao.keys():
        ydc[sasas] = sao[sasas]'''
#---
from type.cate_P17 import *
saop2 = [
    USA_P17 
    #ALL_P17,
    #New_P17 ,
    #New_P172
    ]
P17fi = {}
for sao in saop2:
    for sasas in sao.keys():
        P17fi[sasas] = sao[sasas]
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
    lenth = len(soo344.keys() ) * len(P17fi.keys() )    
    print('file: ' + file + ' , lenth : ' + str( lenth) )
    #catenlog.yemen(P17fi , soo344,file)
    caten.D_Y_C(P17fi , soo344 , type)
#---
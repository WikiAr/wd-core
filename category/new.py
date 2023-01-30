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
import caten_13_8
#import caten
#---
from type.cate_type import *
pop_fi = {}
for sao in [pop_start , New_Pop , New_Pop2]:
    for sasas in sao.keys():
        pop_fi[sasas] = sao[sasas]
#---
from type.cate_P17 import *
saop2 = []
#saop2.append(USA_P17)
#saop2.append(ALL_P17)
#saop2.append(New_P17)
#saop2.append(New_P172)
saop2.append(New_P173)

P17fi = {}
for sao in saop2:
    for sasas in sao.keys():
        P17fi[sasas] = sao[sasas]
#---
poiuh = '''
python pwb.py category/new d:a
python pwb.py category/new d:y
python pwb.py category/new d:d
python pwb.py category/new d:c
python pwb.py category/new d:f
'''
#---
if __name__ == "__main__":
    #print('lenth : ' + str( lenth) )
    soo344 = {}
    type = ''
    file = 'new'
    for arg in sys.argv:#
        arg, sep, value = arg.partition(':')
        if arg =='d':
            type = value
            if value == 'a':
                soo344 , file =  pop_fi,'new'
            elif value == 'y':
                soo344 , file =  years__, file + '_years'
            elif value == 'd':
                soo344 , file =  decade__, file + '_decade'
            elif value == 'c':
                soo344 , file =  century__, file + '_century'
            elif value == 'f':
                soo344 , file =  pop_final, file + '_final'
    lenth = len(soo344.keys() ) * len(P17fi.keys() )    
    print('file: ' + file + ' , lenth : ' + str( lenth) )
    #catenlog.yemen(P17fi , soo344,file)
    caten_13_8.D_Y_C(P17fi , soo344 , type)
#---
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
saop2.append(New_P172)
saop2.append(New_P173)
P17fi = {}
for sao in saop2:
    for sasas in sao.keys():
        P17fi[sasas] = sao[sasas]
#---
saoe = [
    "python pwb.py p971/new d:a"
    ,"python pwb.py p971/new d:y"
    ,"python pwb.py p971/new d:d"
    ,"python pwb.py p971/new d:c"
    ,"python pwb.py p971/new d:f"
    ]
#---
#import catenlog
import caten2
#import caten
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
            elif value == 'd' or  value == 'dd':
                soo344 , file =  decade__, file + '_decade'
            elif value == 'c' or value == 'cc':
                soo344 , file =  century__, file + '_century'
            elif value == 'f':
                soo344 , file =  pop_final, file + '_final'
    lenth = len(soo344.keys() ) * len(P17fi.keys() )    
    print('file: ' + file + ' , lenth : ' + str( lenth) )
    #catenlog.yemen(P17fi , soo344,file)
    caten2.D_Y_C(P17fi , soo344 , type)
#---
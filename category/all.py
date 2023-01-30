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
from type.cate_P17 import *
saop2 = [
    USA_P17 
    ,ALL_P17
    ,New_P17
    ,New_P172
    ]
P17fi = {}
for sao in saop2:
    for sasas in sao.keys():
        P17fi[sasas] = sao[sasas]
#---
poiuh = '''
python pwb.py category/all d:a
python pwb.py category/all d:y
python pwb.py category/all d:d
python pwb.py category/all d:c
python pwb.py category/all d:f
'''
#---
if __name__ == "__main__":
    #print('lenth : ' + str( lenth) )
    soo344 = {}
    type = ''
    file = 'all'
    for arg in sys.argv:#
        arg, sep, value=arg.partition(':')
        if arg =='d':
            type = value
            if value == 'a':
                soo344, file=pop_fi,'all'
            elif value == 'y':
                soo344, file=years__,'all_years'
            elif value == 'd':
                soo344, file=decade__,'all_decade'
            elif value == 'c':
                soo344, file=century__,'all_century'
            elif value == 'f':
                soo344, file=pop_final,'all_final'
    lenth = len(soo344.keys() ) * len(P17fi.keys() )    
    print('file: ' + file + ' , lenth : ' + str( lenth) )
    #catenlog.yemen(P17fi , soo344,file)
    caten.D_Y_C(P17fi , soo344 , type)
#---
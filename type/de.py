#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import codecs
from ALL_decades import ALL_decades_Keys
from cate_type import decade__

'''for ca in ALL_decades_Keys:  
    if not ca in decade__.keys():
        ss = '%s\n' % ca
        print (ss)
        with codecs.open('textfiles/API-log/miss_dec.csv', "a", encoding="utf-8") as logfile:
            logfile.write(ss)
            logfile.close()'''
#---
for ca in decade__.keys():  
    if ca in ALL_decades_Keys:
        ss = '\t"%s": %s,\n' % (ca ,str(decade__[ca]) ) 
    else:
        ss = '\t#"%s": %s,\n' % (ca ,str(decade__[ca]) ) 
    print (ss)
    with codecs.open('textfiles/API-log/miss_dec.csv', "a", encoding="utf-8") as logfile:
        logfile.write(ss)
        logfile.close()
#---
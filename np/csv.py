#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python pwb.py np/csv

"""
#
# (C) Ibrahem Qasim, 2022
#
import json
import codecs
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
from API import printe
import sys
#---
sys_argv = sys.argv or []
#---
Lalo_types = {}
#---
listo = codecs.open( main_dir + "np/si3.csv" , "r", encoding="utf-8-sig").read()
#---
for x in listo.split('\n') : 
    x = x.strip()
    if x in Lalo_types :
        Lalo_types[x] += 1
    else:
        Lalo_types[x] = 1
#---
printe.output( 'len of Lalo_types %d. '  % len(Lalo_types) )
#---
with open( main_dir + "np/new_types.json" , 'w' ) as nfile:
    json.dump( Lalo_types , nfile )
    #---
    #dump['new'] = []
#---



#---
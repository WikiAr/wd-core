#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

python3 pwb.py np/sch ask
python3 pwb.py np/sch

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import sys
import bz2
#import gz
import json
import time
import pywikibot
#---
start = time.time()
t1 = time.time()
#---
c = 0
f = bz2.open('/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2' , 'r')
#---
from np.si3 import make_scientific_art
from np.si3 import *
#---
for line in f:
    line = line.decode('utf-8')
    line = line.strip('\n').strip(',')
    c += 1
    if line.startswith('{') and line.endswith('}'):
        #---
        json1 = json.loads(line)
        q = json1['id']
        #---
        p31_no_ar_lab = []
        item = json1
        item['q'] = q
        #---
        if 'ar' in json1.get('descriptions',{}): continue
        P31 = json1.get('descriptions',{}).get('P31',[])
        for x in P31:
            p31x = x.get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id',"")
            if p31x == 'Q13442814':
                make_scientific_art( item, 'Q13442814', c )
                break
    #---
    if c % 1000 == 0:
        print('%d:%d,%s' % (c, time.time()-t1 , q ) )
        t1 = time.time()
    #---


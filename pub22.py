#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python3 pub22.py ask test issn:2537-0499

python3 pub22.py ask test issn:2735-3435
python3 pub22.py ask test issn:2735-3427
python3 pub22.py ask test issn:

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import os
import sys
sys.dont_write_bytecode = True
#---
from pub import *#add#get_and_load
#---
urlee = "https://api.crossref.org/journals/{}/works"
issns_all = [
    "2537-0464",
    "2537-0472",
    "2537-0480",
    "2537-0499",
    "2537-0456",
    "2537-0448",
    "2537-0421",
    "2537-0405",
    "2537-0413",
    "2537-0812",
    "2537-0863",
    "2537-0839",
    "2537-0804",
    "2537-0855",
    "2537-0820",
    "2537-0871",
    "2537-0383",
    "2537-0391",
    "2735-3745",
    "2735-3737",
    "2735-3729",
    "2735-3710",
]
#---
issns_all.sort()
#---
issns = []
if "all" in sys.argv:
    issns = issns_all
#---
#litt = []
#---
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    if arg.lower() == 'issn' and value != '':
        issns.append(value)
#---
litt = []
#---
for issn in issns:
    ge = urlee.format(issn)
    jso = get_and_load(ge)
    #---
    if type(jso) == dict:
        items = jso.get('message', {}).get('items', [])
        for item in items :
            doi = item.get('DOI') or item.get('doi')
            #---
            if doi:
                doi = doi.strip().upper()
                if not doi in litt:
                    litt.append(doi)
                    add(doi, "DOI")
    #---
    #print("len of  litt: %d" % len(litt))
    #---
    #for id in litt:
        #add(id, "doi")
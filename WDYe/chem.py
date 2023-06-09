#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#

# ---
# start of newdesc.py file
from wd_API import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions
# ---
QS = {}
# QS["Q6979593"] = Qid_Descraptions["Q6979593"]    national association football team
QS["Q11173"] = Qid_Descraptions["Q11173"]  # chemical compound
# ---
for q in QS:
    en = QS[q]["en"]
    quarry = 'SELECT DISTINCT ?item WHERE { ?item wdt:P31 wd:%s. ?item schema:description "%s"@en . } limit 10000' % (
        q, en)
    newdesc.mainfromQuarry2(q, quarry, QS)
# ---

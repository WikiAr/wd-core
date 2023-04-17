#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  python pwb.py wd/wikinews
#
#
#---
lise = {
    "Q8086267" : "تصنيف:1001 حسب البلد",
    "Q7213480" : "تصنيف:1002 حسب البلد",
    "Q8499996" : "تصنيف:يونانيون نازحون إلى نيوزيلندا",
    }

#---
from wd_API import himoAPI_test
#---
for Qid in lise:
    Label = lise[Qid]
    himoAPI_test.Add_Labels_if_not_there( Qid, Label , "ar" , ASK = False )
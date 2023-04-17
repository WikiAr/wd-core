#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#  
#
#
#---
# start of newdesc.py file
from wd_API import newdesc
#   newdesc.main_from_file(file , topic , translations2)
#   newdesc.mainfromQuarry2( topic , Quarry, translations)
#---
translations = {}
translations['Wikimedia module'] = { # 
            'ar': 'وحدة ويكيميديا',#
            'en': 'Wikimedia module',#
            'fr': 'Module Wikimedia',#
            'en-ca': 'Wikimedia module',#
            'en-gb': 'Wikimedia module',#
            'nl': 'Wikimedia-module',
            'he': 'יחידה של ויקימדיה',
            'ilo': 'Modulo ti lua',
            'vi': 'mô đun Lua',
            'ko': '위키미디어 루아 모듈',
            'bg': 'Уикимедия модул',
            'pl': 'moduł Lua',
        }
#---
list = [
    "Q15145755",#   Module test cases
    "Q18711811"#   وحدة بيانات خرائط
    ]
#---
topic = 'Wikimedia module'
#---
for ll in list:
    quarry = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:%s.}' % ll
    newdesc.mainfromQuarry2( topic , quarry, translations)
#---
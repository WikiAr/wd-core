#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
import pywikibot
import re
import time
import urllib
import codecs
import unicodedata
#---
import sys
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#himoAPI.Merge( q1, q2)
#---
# save the edit
#for i in range(1,):
#---
def main():
    pywikibot.output('<<lightred>>  main:' )
    title = 'user:Mr. Ibrahem/duplicate'
    wikidatasite=pywikibot.Site('wikidata','wikidata') 
    page = pywikibot.Page(wikidatasite, title)
    #---
    text = page.text
    text2 = '''|-
|{{Q|Q9986818}} || {{Q|Q32649521}}
|-
|{{Q|Q9965713}} || {{Q|Q32647554}}
|-
|{{Q|Q9933421}} || {{Q|Q32672108}}
|-
|{{Q|Q9929066}} || {{Q|Q32675007}}'''
    text = re.sub('\|\-\n' , '' , text)
    text = re.sub('\|\-', '', text)
    lines = text.split('\n')
    lenth = len(lines)
    num = 0
    for line in lines:
        num += 1
        pywikibot.output('<<lightred>> %d/%d line:' % (num , lenth) )
        #pywikibot.output(line)
        #line = line.split('\|\|')
        line = re.sub('\}\}' , '' , line)
        line = re.sub('\{\{Q\|' , '' , line)
        line = re.sub('\s*\|\|\s*' , ',' , line)
        match = re.search('(Q\d+)\,(Q\d+)',line)
        if match:                                           # إذا وجد وصلة إنجليزية
            #pywikibot.output(match.group())
            q1 = match.group(1)
            q2 = match.group(2)
            himoAPI.Merge( q1, q2)
    #---
    #return False
#---

if __name__ == '__main__':
     main()
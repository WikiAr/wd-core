#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
python pwb.py cy/cy4 -page:كريس_فروم

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import json
import re
import time
#import Nationalities as aa
#import codecs
#from datetime import datetime
#---
import sys
#---
import urllib
import urllib
import urllib.request
import urllib.parse
#---
def PPPNew(text , title):   
    Frist = re.compile( '\{\{نتيجة سباق الدراجات\/بداية\s*?.*?\}\}')
    pas = Frist.findall( text )
    if pas:
        print( 'pas: ' )
        params = str(pas[0])
        #params = re.sub("\s*}}" , "" , params)
        params = re.sub("\s*\=\s*" , "=" , params)
        params = re.sub("\s*\|\s*" , "|" , params)
        print(params)
        #---
        if re.sub("مراحل=نعم", "" , params) != params:
            print("Work with Stage")
        #---
        if re.sub(".*id\=(Q\d+).*" , "" , params) != params :
            print('** found currect line' )
            Qid = re.sub(".*id\=(Q\d+).*" , "\g<1>" , params)
            print('id: ' + Qid)
    #---
    findline =  '\{\{نتيجة سباق الدراجات\/بداية\|id\=(Q\d+)\}\}'
    findline =  '\{\{نتيجة سباق الدراجات\/بداية\|id\=(Q\d+)\}\}'
    newline = re.search(findline, text)
    if newline:
        print(newline)
        print('** found currect line' )
        Qid   = newline.group(1)
        print('id: ' + Qid)
#---
tty = """
===سباقات أو مراحل فاز بها===
{{نتيجة سباق الدراجات/بداية|مراحل=نعم | id = Q623 }}
<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->
{{نتيجة سباق الدراجات/سطر4
|qid = Q3003022
|السباق = [[كريثيديا دو دوفين 2013]]
|البلد = {{Flag|سويسرا}}
|التاريخ = 2013-06-09T00:00:00Z
|المركز = المركز الثاني
|جيرسي = 
|}}
{{نتيجة سباق الدراجات/سطر4
|qid = Q28948862
|السباق = [[كريثيديا دو دوفين 2017]]
|البلد = {{Flag|سويسرا}}
|التاريخ = 2017-06-11T00:00:00Z
|المركز = المركز الثاني
|جيرسي = 
|}}
{{نتيجة سباق الدراجات/نهاية}}

"""
if __name__ == "__main__":
    #main()
    PPPNew(tty , "dfdfdf")
#---
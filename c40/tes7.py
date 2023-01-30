#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت إنشاء صفحة عن شخص بناءاً على بيانات ويكي بيانات

بوت لإنشاء صفحات اعتماداً على ويكي بيانات

البوت يظهر نتائج المحتوى قبل حفظة

"""
#
# (C) Ibrahem Qasim, 2022
#
import codecs
from API.maindir import main_dir
import pywikibot
import re
#import time
#---
import urllib
import urllib
import urllib.request
import urllib.parse
#---
import string
#import json
#from tkinter import *
#import wd2 as wikidata2
from easygui import *
#import sys

   #https://ar.wikipedia.org/w/api.php?
   #action=parse&format=jsonfm&text=
   #%7B%7Bsubst%3Aمستخدم%3AMr._Ibrahem%2Fمشاريع%2Fعسكر%7CQ76%7D%7D
   #&prop=wikitext&pst=1&contentmodel=wikitext&utf8=1
   
def FromWiki(ID):
    text = '{{subst:user:Mr._Ibrahem/مشاريع/عسكر|' + ID + '}}'
    #text = '{{subst:نتيجة سباق الدراجات/جيرسي|' + ID + '}}'
    #text = urllib.parse.quote(text)
    #---
    text = urllib.parse.quote(text)
    #---
    #text = '%7B%7Bsubst%3A%D9%86%D8%AA%D9%8A%D8%AC%D8%A9%20%D8%B3%D8%A8%D8%A7%D9%82%20%D8%A7%D9%84%D8%AF%D8%B1%D8%A7%D8%AC%D8%A7%D8%AA%2F%D8%AC%D9%8A%D8%B1%D8%B3%D9%8A%7C' + ID + '%7D%7D'
    url = 'https://ar.wikipedia.org/w/api.php?action=parse&format=json&text=' + text + '&prop=wikitext&pst=1&contentmodel=wikitext&utf8=1'
    pywikibot.output(url)
    html = urllib.request.urlopen(url).read().strip().decode('utf8','ignore')
    
                                #python 2.7
    #wikidatavalue = html.split('{"value":"')[1].split('"')[0]
    return html

fieldNames = [ "id" ]
msg = "أدخل معرف ويكي بيانات"
title = "Credit Card Application"       

fieldValues = []
val = {}

def log(case , ID):
  with codecs.open("c40/" + ID + ".log.csv", "a", encoding="utf-8") as logfile:
    try:   
      logfile.write(case)
    except :
      pywikibot.output("Error writing")
      
def FromFile(ID):
     with codecs.open("c40/q.py.txt", "r", encoding="utf-8") as logfile:
        # محاولة الحصول على وصلة من الإنجليزية
        #text = '{{subst:user:Mr._Ibrahem/مشاريع/عسكر|' + ID + '}}'
        #---
        text = logfile.read()
        text = re.sub('\{\{\{1\|\}\}\}',  ID , text)
        text = re.sub('\{\{\{1\}\}\}',  ID , text)
        #pywikibot.output(text)
        #---
        #text = '{{نسخ:user:Mr._Ibrahem/مشاريع/عسكر|' + ID + '}}'
        #---
        Site = pywikibot.Site('ar' ,  "wikipedia")
        params = {
            "action":"parse",
            "prop":"wikitext",
            "text":text,
            "contentmodel":'wikitext',
            "pst":1,
            "utf8":1
        }
        categoryname = pywikibot.data.api.Request(site=Site, parameters = params)
        categoryname=categoryname.submit()
        #pywikibot.output(categoryname)
        case = ''
        for item in categoryname['parse']['psttext']:
            case=categoryname['parse']['psttext'][item]
        #---
        case = re.sub('\{\{\{(\w+|\d+)\}\}\}',  '' , case)
        #pywikibot.output(case)
        log(case , ID)
        return case

def out(aa):
    if aa:
        codebox("Contents of file " , "Show File Contents", aa)
            
def main3():
    # we start with blanks for the values
  while 1:
    fieldValues = multenterbox(msg,title, fieldNames)
    errmsg = ""
    #---
    for i in range(len(fieldNames)):
      fo =  fieldNames[i]
      val[fo] = fieldValues[i]
    #---
    #if errmsg == "": break # no problems found
    fieldValues = multenterbox(errmsg, title, fieldNames, fieldValues)
    text = FromFile(val["id"])
    #text = FromWiki(val["id"])
    out(text)
     
if __name__ == '__main__':
     main3()
     #run_with_wikidata('*Q5644466|[[user:Mr._Ibrahem/n4]]', '')
     
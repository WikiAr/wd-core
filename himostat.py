#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
from pywikibot import config
import re
import json
import time
import pywikibot
import codecs
#---
import sys
#---
import urllib.request
import urllib.parse
#---
Work_sql = { 1 : True }
#---
try:
    import MySQLdb
except:
    Work_sql[1] = False
    pywikibot.output('<<lightred>> no MySQLdb')

#---
# start of himoAPI.py file
from API import himoAPI
# himoAPI.page_put(NewText , summary , title)

#---
pagetop='''
{| class="wikitable sortable"
!style="background-color:#808080" align="center"|summary
!style="background-color:#808080" align="center"|count
|-
'''
pagedown='\n|}'

site = pywikibot.Site('wikidata', 'wikidata')
#---
def getquery():
    query = '''SELECT rev_comment ,COUNT(*)
    FROM revision_userindex
    WHERE rev_user_text = 'Mr.Ibrahembot'
    GROUP BY rev_comment
    ORDER BY COUNT(*);'''
    pywikibot.output('Executing query:\n%s' % query)
    #---
    results = []
    #---
    if Work_sql[1]:
        conn = MySQLdb.connect("wikidatawiki.analytics.db.svc.wikimedia.cloud", db=site.dbName(), user=config.db_username, passwd=config.db_password)
        cursor = conn.cursor()
        query = query.encode(site.encoding())
        cursor.execute(query)
        results = cursor.fetchall()
    #---
    return results
#---
adress="user:Mr.Ibrahembot/EditCounts"
message="update"
#---
def work():
    #log_page = pywikibot.Page(site, adress)
    rowfa=' '
    numb =0
    results = getquery()
    for row in results:
        sum = str(row[0])
        count = int(row[1])
        rowfa += '\n|-' % ( sum , count )
    text = pagetop + rowfa + pagedown
    #himoAPI.page_put(text , message , adress)
    himoAPI.page_putWithAsk("", text , message , adress, True)
    #log_page.put(text,message)
#---
if __name__ == "__main__":
    work()
#---
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

تعديل التسميات التي بها أقواس في ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
from pywikibot import pagegenerators
from pywikibot import pagegenerators as pg

import urllib
import urllib.request
import urllib.parse
import re
import json
import codecs
from API.maindir import main_dir
import sys
import datetime
from datetime import datetime, date, time
import time
missing_dict={}

def logme(wditem, newlabel,oldlabel):
  form = '\n%s\tLar\t%s\t%s'
  form2 = '%s update: %s'
  with codecs.open("x\indynumber.log.csv", "a", encoding="utf-8") as logfile:
    try:   
        logfile.write(form % (wditem.title(), newlabel,oldlabel) )
    except :
        pass
        print(" Error writing to logfile on: [%s]" %  newlabel)
    verbose = True#True    #now I want to see what!   
    logfile.close()
    if verbose:
       print(form2 % (wditem.title(), newlabel) )
       
def fixlabel(oldlabel):
    new = oldlabel.split(' (')[0]
    new = new.split('(')[0]
    return new

def action_one_item(item):
  ara = 'ar'
  if item.labels: #تسميات موجودة
    if ('ar' in item.labels): 
      oldlabel = item.labels['ar'] 
      newlabel = fixlabel(oldlabel)
      ss = ('Bot: update Arabic label: %s to "%s"' % (oldlabel, newlabel))
      s = ('Bot: update Arabic label to "%s"' % newlabel)
      pywikibot.output(ss)
      if newlabel != '':
        if newlabel != oldlabel:
          arlab = { 'ar': newlabel }
          if debug:
            logme(item, newlabel,oldlabel)
          else:
            #logme(item, newlabel,oldlabel)
            try:
              item.editLabels(labels=arlab, summary=s)
              #item.editEntity(data, summary=s)
            except:
              pass
  else: 
    pass
  return 1     
  return 0
                           
def wd_from_file():
  repo=pywikibot.Site('wikidata','wikidata').data_repository()
  csvfile=open('name/fix.txt','r')
  for alllines in csvfile:
    qitem=alllines[alllines.find('Q'):alllines.find(',')]
    if (len(qitem)>0):
      wditem=pywikibot.ItemPage(repo,qitem)
      if (not(wditem.isRedirectPage())):
       if wditem.exists():
        wditem.get(get_redirect=True)
        yield wditem
    
def main1():
        pigenerator = wd_from_file()
        num = 0
        for page in pigenerator:
            num += 1
            pywikibot.output('<<lightblue>>> %s: %s'  % ( num  , page.title() ) )
            action_one_item( page )
            
debug=False

if __name__ == "__main__":  
       main1()

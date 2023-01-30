#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

اضافة بيانات التعداد السكاني من الصفحات اليمنية

"""
#
# (C) Ibrahem Qasim, 2022
#
import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
# 
import codecs
import re
import time
import string
import json
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.



wikidatasite=pywikibot.Site('wikidata','wikidata') 
repo = wikidatasite.data_repository()

def AddArabicToWikidata3(titl1value, wditem1):
        QID=wditem1.title()
        site = pywikibot.Site("wikidata", "wikidata")
        repo = site.data_repository()
        testsite = site.data_repository()
        #item = pywikibot.ItemPage(repo, QID)

        #testsite = self.get_repo()
        item = pywikibot.ItemPage(testsite, 'Q4115189')
        item.get()
        #if 'P1082' in item.claims:
            #item.removeClaims(item.claims['P1082'])

        #claim = pywikibot.page.Claim(testsite, 'P1082')#, datatype='wikibase-item')
        #target = pywikibot.ItemPage(testsite, 'Q271')
        #claim.setTarget(target)

        #item.addClaim(claim)

        # set new claim
        claim = pywikibot.page.Claim(testsite, 'P1082', datatype='quantity')
        target = pywikibot.WbQuantity(amount=titl1value)
        claim.setTarget(target)
        item.addClaim(claim)

qualifiers = {
                    "P585": [
                        {
                            "snaktype": "value",
                            "property": "P585",
                            "datavalue": {
                                "value": {
                                    "time": "+2004-00-00T00:00:00Z",
                                    "timezone": 0,
                                    "before": 0,
                                    "after": 0,
                                    "precision": 9,
                                    "calendarmodel": "http://www.wikidata.org/entity/Q1985727"
                                },
                                "type": "time"
                            },
                            "datatype": "time"
                        }
                    ],
                    "P459": [
                        {
                            "snaktype": "value",
                            "property": "P459",
                            "datavalue": {
                                "value": {
                                    "entity-type": "item",
                                    "numeric-id": 12202700,
                                    "id": "Q12202700"
                                },
                                "type": "wikibase-entityid"
                            },
                            "datatype": "wikibase-item"
                        }
                    ]
                }

references={
                        "snaks": {
                            "P248": [
                                {
                                    "snaktype": "value",
                                    "property": "P248",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 12202700,
                                            "id": "Q12202700"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "snaks-order": [
                            "P248"
                        ]
                    }

data33 = {
    "claims": {
        "P1082": [
            {
                "mainsnak": {
                    "snaktype": "value",
                    "property": "P1082",
                    "datavalue": {
                        "value": {
                            "amount": "+222",
                            "unit": "1"
                        },
                        "type": "quantity"
                    },
                    "datatype": "quantity"
                },
                "type": "statement",
                "rank": "normal"
            }
        ]
    }}

def addP1082(titl1value, wditem1):
    #QID='Q4115189'
    QID = wditem1.title()
    #site = pywikibot.Site("wikidata", "wikidata")
    #repo = site.data_repository()
    #item = pywikibot.ItemPage(repo, QID)
    item = wditem1
    item.get()
    value='+' + titl1value

    data = {
    "claims": {
        "P1082": [
            {
                "mainsnak": {
                    "snaktype": "value",
                    "property": "P1082",
                    "datavalue": {
                        "value": {
                            "amount": value,
                            "unit": "1"
                        },
                        "type": "quantity"
                    },
                    "datatype": "quantity"
                },
                "type": "statement",
                "qualifiers":qualifiers ,
                "qualifiers-order": [
                    "P585",
                    "P459"
                ],
                "rank": "normal",
                "references": [references]
            }
        ]
    }
 }
    mySummary ='Bot:Added claim P1082'
    pywikibot.output('write to wikidata')
    item.editEntity(data, summary=mySummary)
    #item.editEntity(data)

def makejson(property, value):
    value='+' + value
    properties =   { property : [
                {"mainsnak": {
                    "snaktype": "value",
                    "property": property,
                    "datavalue": {
                        "value": {
                            "amount": value,
                            "unit": "1"
                        },
                        "type": "quantity"
                    },
                    "datatype": "quantity"
                },
                "type": "statement",
                "qualifiers":qualifiers ,
                "qualifiers-order": [
                    "P585",
                    "P459"
                ],
                "rank": "normal",
                "references": [references]
            }
        ] }
    return properties, property


"""def addClaim(property, value, item):
    #QID='Q4115189'
    QID = item.title()
    #site = pywikibot.Site("wikidata", "wikidata")
    #repo = site.data_repository()
    #item = pywikibot.ItemPage(repo, QID)
    item = item
    item.get()
    value='+' + value

    properties =   { property : [
                {"mainsnak": {
                    "snaktype": "value",
                    "property": property,
                    "datavalue": {
                        "value": {
                            "amount": value,
                            "unit": "1"
                        },
                        "type": "quantity"
                    },
                    "datatype": "quantity"
                },
                "type": "statement",
                "qualifiers":qualifiers ,
                "qualifiers-order": [
                    "P585",
                    "P459"
                ],
                "rank": "normal",
                "references": [references]
            }
        ] }
    data = { "claims":  properties  }

    mySummary ='Bot:Added claim' + property
    pywikibot.output('write %s to wikidata' % property)
    item.editEntity(data, summary=mySummary"""

def addClaims(properties, item, v):
    #QID='Q4115189'
    #QID = item.title()
    #site = pywikibot.Site("wikidata", "wikidata")
    #repo = site.data_repository()
    #item = pywikibot.ItemPage(repo, QID)
    vo = ''

    for vv in v:
        vo = vo + ',' + vv
    vo = '"'+vo+'"'
    vo = re.sub('",', '"', vo)
    item = item
    item.get()
    data = { "claims":  properties  }
    
    mySummary = ('Bot:Added claim/s %s'  % vo)
    pywikibot.output('write %s to wikidata' % vo)
    pywikibot.output(mySummary)
    item.editEntity(data, summary=mySummary)
Targetparams = [ 'تعداد 2004' , 'عدد الأسر 2004', 'الذكور 2004', 'الإناث 2004']

targetparamnew = {'تعداد 2004' : 'P1082',
                  'عدد الأسر 2004' : 'P1538',
                  'الذكور 2004' : 'P1540',
                  'الإناث 2004' : 'P1539',
                  }

def run_with_wikidata(params, titl1, tryy, item):
      properties , v = {}, []
      there = True
      for pa in params:                                             #البحث عن وسيط الاسم العلمي
         """pa = pa.split('\n')[0]
         pa = re.sub('\s*\=\s*', '=', pa)
         pa = '%"'+pa+'%"'
         pa = re.sub('\s*\%\"\s*', '', pa)
         pa = re.sub(',', '', pa)"""
         oo = pa.split('=')[0]
         if oo in targetparamnew:                                     # الاسم العلمي موجود
            there = False
            value = pa.split('=')[1]
            match = re.search('\d{1,9999999}', value)
            property=targetparamnew[oo]
            if match:        
                  pywikibot.output('**found param : %s with value "%s"' % (oo, value) )
                  #if property == 'P1082':
                  #addP1082(value, item)
                  if (property in item.claims):                     #اذا كانت الصفحة بها خاصية الاسم العلمي
                          pywikibot.output('<<lightyellow>>already have ' + property)
                  else:
                          #pywikibot.output(item)
                          sar, vv = makejson(property, value)       #تجربة 
                          properties.update(sar)       #تجربة 
                          v.append(vv)       #تجربة 
                          #v = v + v        #تجربة 
                          #addClaim(property, value, item)       #اساسي 
            else:
                  pywikibot.output('**' + property + ': the value dont match number <<red>> "%s"' % value)
      return properties, v
      if there == True:
         pywikibot.output('**no param : %s' % Targetparams )       # الاسم العلمي غير موجود في القالب

def getwditem(title):
    EngItem=''
    EngSite = pywikibot.Site("ar", "wikipedia") 
    EngPage = pywikibot.Page(EngSite, title)
    try:
        EngItem = pywikibot.ItemPage.fromPage(EngPage)
    except:
        pass
    return EngItem

TargetTemplates = ['منطقة يمنية']

def PPP(params):	
  c = []
  #params = str(params)
  for pa in params:
    pa = '""'+ pa.split('\n')[0] +  '""'
    pa = re.sub('\s*\=\s*', '=', pa)
    pa = re.sub('\s*\"\"\s*', '', pa)
    c.append(pa)
    #pywikibot.output(pa)
  return c


def ISRENEW(page, titl1):
    properties = ''
    pywikibot.output( '\n----------\n<<lightyellow>>>> >> %s << <<' % titl1)          #البدء في العمل في الصفحة
    NoTemplate = True
    item = getwditem(titl1)                                          #ايجاد عنصر ويكي بيانات للصفحة
    #item = getwditem('ويكيبيديا:ويكي بيانات/ملعب ويكي بيانات')                                          #ايجاد عنصر ويكي بيانات للصفحة
    templatesInThePage = page.templates()
    templatesWithParams = page.templatesWithParams()                    #قوالب الصفحة
    if item:                                             #اذا كانت الصفحة بعنصر ويكي بيانات
         for (template, params) in templatesWithParams:
               TargetTemp = template.title(withNamespace=False)
               if TargetTemp in TargetTemplates:                           #ايجاد قالب تصنيف كائن في الصفحة
                    params=PPP(params)
                    pywikibot.output("*found template %s"  % TargetTemp )
                    NoTemplate = False
                    pywikibot.output("*page %s already have wikidata item"  % titl1)
                    """if ('P1082' in item.claims):                     #اذا كانت الصفحة بها خاصية الاسم العلمي
                        pywikibot.output('already have P1082')
                    else:
                        pywikibot.output(item)
                        run_with_wikidata(params, titl1, False, item)"""
                    properties, v = run_with_wikidata(params, titl1, False, item)
                    
                    #run_with_wikidata(params, titl1, True, '')
         if len(properties) >=1:
              addClaims(properties, item, v)
         else:
              pywikibot.output('<<lightred>>nothing to add')
    else:
         pywikibot.output('<<lightred>>no wikidata item')
    if NoTemplate == True:
        pywikibot.output("*<<lightred>>don't found template %s"  % TargetTemplates ) # القالب غير موجود في الصفحة
            
def main(*args):
    #args= {'-cat:صفحات_تستخدم_قالب_منطقة_يمنية_-_تعز'}
    #args = {'-page:عفنة_أجمية'}
    generator = gent.get_gent(*args)
        
    for page in generator:
        #text = page.text
        title1 = page.title(asLink=False)
        #start(text, title)
        #pywikibot.output(num)
        try:
            ISRENEW(page , title1)
        except: 
            pass
        #AddP1082('', '')
        #ISRE(page , title)
        """(text, newtext, always) = add_text(page, addText, summary, regexSkip,
                                           regexSkipUrl, always, up, True,
                                           reorderEnabled=reorderEnabled,
                                           create=talkPage)"""

if __name__ == '__main__':
     main()
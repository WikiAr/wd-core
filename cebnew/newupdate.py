#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update


"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
import codecs
from API.maindir import main_dir

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
# 
#import pwb
import re
import string
#---
import sys
#---
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.


#---
wikidatasite=pywikibot.Site('wikidata','wikidata') 
repo = wikidatasite.data_repository()
#---
Json = {}
QS2Table = {}
#--- 

from API.category import *

#---
logOp = {}
#---
QidP = {
    'P17': {} , 
}
#---
references={
                        "snaks": {
                            "P143": [
                                {
                                    "snaktype": "value",
                                    "property": "P143",
                                    "datavalue": {
                                        "value": {
                                            "entity-type": "item",
                                            "numeric-id": 837615,
                                            "id": "Q837615"
                                        },
                                        "type": "wikibase-entityid"
                                    },
                                    "datatype": "wikibase-item"
                                }
                            ]
                        },
                        "snaks-order": [
                            "P143"
                        ]
                    }
                    
def logQS2(QS2Rows):#vaul
    pywikibot.output( '**<<lightyellow>> logQS2 :' )
    logFile = "P32_Rows_1"
    #---
    if QS2Table['q'] == 'LAST':
        logFile = "P32_New_1"
        QS2Rows =  'CREATE\n' + QS2Rows
        pywikibot.output(QS2Rows)
    #---
    form = "%s\n"
    ccc  = (form % (QS2Rows))
    #---
    if QS2Rows:
       with codecs.open(JlobalFileFloder + logFile + ".log.csv", "a", encoding="utf-8") as logfile:
          try:   
             logfile.write(ccc)
          except :
             pass
       logfile.close()
#---
def makejson(property, numeric):
    #---
    """if property  == 'P17':
        numeric = Get-Qid(property)
        pywikibot.output('*<<lightblue>> numeric = Get-Qid(property) :Q"%s"  ' % numeric  )"""
    #---
    if numeric !='':
        numeric = re.sub('Q','',numeric)
        Q = 'Q' + numeric
        Pro = {"mainsnak": {
                    "snaktype": "value",
                    "property": property,
                    "datavalue": {
                        "value": {
                            "entity-type": "item",
                            "numeric-id": numeric,
                            "id": Q
                        },
                        "type": "wikibase-entityid"
                    },
                    "datatype": "wikibase-item"
                },
                "type": "statement",
                "rank": "normal",
                "references":  [references]
            }
        
        #---
        return Pro
    
def MakeP1566(ss):
    if 'geonames' in ss:
        if ss['geonames'] !='':
            pe =  {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P1566",
                            "datavalue": {
                                "value": ss['geonames'],
                                "type": "string"
                            },
                            "datatype": "external-id"
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references":  [references]
                    }
            if QS2:
                pe = ('%s\tP1566\t"%s"' % (QS2Table['q'] , ss['geonames'] ))
            return pe
    #"amount": "+" + ss['elevation'],
def MakeP2044(ss):
    if 'elevation' in ss:
        if ss['elevation'] !='':
            pe = {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2044",
                            "datavalue": {
                                "value": {
                                    
                                    "amount": ss['elevation'],
                                    "unit": "http://www.wikidata.org/entity/Q11573"
                                },
                                "type": "quantity"
                            },
                            "datatype": "quantity"
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references":  [references]
                    }
            if QS2:
                pe = ('%s\tP2044\t"+%s"' % (QS2Table['q'] , ss['elevation'] ))
            return pe
#---
def getwditem(title):
    ceb = pywikibot.Site("ceb", "wikipedia") 
    item = ''
    EngPage = pywikibot.Page(ceb, title)
    try:
        item = pywikibot.ItemPage.fromPage(EngPage)
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        #pywikibot.output('*error when item.get() "%s"' % title)
        return False
#---

def MakeP625( ss , page ):
    coordinate = page.coordinates(primary_only=True)
    if coordinate:
        pe = {"mainsnak": {"snaktype": "value",
                            "property": "P625",
                            "datavalue": {
                                "value": {
                                    "latitude": coordinate.lat, #ss['lat_d'],
                                    "longitude": coordinate.lon,    #ss['long_d'],
                                    "precision": 1.0e-5,
                                    "globe": "http://www.wikidata.org/entity/Q2"
                                },
                                "type": "globecoordinate"
                            },
                            "datatype": "globe-coordinate"
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references":  [references]
                    }
        coor = '@' + str(coordinate.lat) + '/' + str(coordinate.lon)
        if QS2:
            pe = ('%s\tP625\t%s' % (QS2Table['q'] , coor ))
        return pe       
#---
def logCategoryError(cat , title):#vaul
    pywikibot.output('<<lightgreen>> \t* category:"%s" not in ss page: "%s"' % ( cat , title) )
    logFil = "category_error_2"
    #---
    form = "%s\t%s\n"
    ccc  = (form % (cat , title))
    #---
    #if QS2Rows:
    with codecs.open(JlobalFileFloder + logFil + ".log.csv", "a", encoding="utf-8") as logFil:
      try:   
         logFil.write(ccc)
      except :
         pass
    logFil.close()
       
#---
    
def FindP31(ss):
    if 'category' in ss:
        T = ss['category']
        T2 = re.sub('Mga ' , '' , ss['category'])
        if T in CategoryTable:
            Pro = CategoryTable[T]
            return Pro
        elif T2 in CategoryTable:
            Pro = CategoryTable[T2]
            return Pro
        else:
            logCategoryError( T , ss['title'])
    #---
    return False
    
#---

def MakeP31(ss):
    #pywikibot.output('*<<lightgreen>> MakeP31: ' )
    #--- 
    numeric = FindP31(ss)
    if numeric:
        Pro = makejson( 'P31' , numeric )
        return Pro
    else:
        return False
#---
# start of himoAPI.py file
from API import himoAPI
#---
def fixtitle(title):
    #tit  = title
    #tit  = re.sub( "\'" , "%27" , tit)
    #tit  = re.sub( "\'" , "\\'" , tit)
    #tit  = re.sub( '\"' , '%22' , tit)
    #tit  = re.sub( '\"' , '\\"' , tit)
    return title
#---
def FindP17(page):
    templatesWithParams = page.templatesWithParams()
    Q = find_P17_templatee(templatesWithParams , 'NONONO')
    if Q:
        Js = makejson('P17', Q)
        return Js
    else:
        return False
#---
def AddClaims(item, ss, page ):
    q = item.title(as_link=False)
    QS2Table['q'] = q
    #pywikibot.output( '**<<lightyellow>> Add Claims:' )
    #---
    ToAdd = False
    summary = ''
    summaryyyy = 'Bot: '
    data = {}
    #---
    addlabels = []
    labelss = ['en' , 'ceb']
    pagetitle = page.title(as_link=False)
    label = pagetitle.split('(')[0]
    label = fixtitle(label)
    if item:
        for lang in labelss:
            if lang not in item.labels:
                if "labels" not in data:
                    data["labels"] = {}
                data["labels"][lang] = {'language': lang,'value': label}
                addlabels.append(lang)
    if addlabels : 
        ToAdd = True
        lp = '/'.join(addlabels)
        summary = summary + 'Add labels ' + lp + ','
    #---
    #data["claims"] = {}
    dataclaims = {}
    claims = ['P31' , 'P625' , 'P17' , 'P2044' , 'P1566' , 'P131']
    AlreadyThere = ['P625']
    if item:
        for cla in claims:
            if cla in item.claims:
                AlreadyThere.append(cla)
    #---
    #if AlreadyThere:
        #pywikibot.output( '**<<lightyellow>> AlreadyThere : ' + str(AlreadyThere))
    #---
    addclaims = []
    if 'P31' not in AlreadyThere:
        P31 = MakeP31(ss) #makejson( 'P31' , '')
        if P31:
                dataclaims["P31"] = [P31]
                addclaims.append('P31')
    #---
    if 'P17' not in AlreadyThere:
        P17 = FindP17(page)
        if P17:
                dataclaims["P17"] = [P17]
                addclaims.append('P17')
    #---
    """if 'P625' not in AlreadyThere:
        P625 = MakeP625(ss , page)
        if P625:
            dataclaims["P625"] = [P625]
            addclaims.append('P625')"""
    #---
    if 'P2044' not in AlreadyThere:
        P2044 = MakeP2044(ss)
        if P2044:
            dataclaims["P2044"] = [P2044]
            addclaims.append('P2044')
    #---
    if 'P1566' not in AlreadyThere:
        P1566 = MakeP1566(ss)
        if P1566:
            dataclaims["P1566"] = [P1566]
            addclaims.append('P1566')
    #---
    if addclaims : 
        data["claims"] = dataclaims
        ToAdd = True
        cp = '/'.join(addclaims)
        summary = summary + 'Add claims ' + cp 
    #---
    summary = summaryyyy + summary + '.'
    #---
    if ToAdd:
        pywikibot.output(summary)
        #item.editEntity(data, summary=summary)
        #---
        try:
            update_API2(q, data , summary)
        except:
            pass
    #else:
        #pywikibot.output('* nothing to add..')

def AddClaims__2(data, ss, page , Mysummary):
    #pywikibot.output( '**<<lightyellow>> Add Claims2:' )
    data["claims"] = {}
    #---
    summary = ''
    pagetitle = page.title(as_link=False)
    AlreadyThere = []
    #---
    #---
    #if 'P31' not in AlreadyThere:
    P31 = MakeP31(ss) #makejson( 'P31' , '')
    if P31:
            data["claims"]["P31"] = [P31]
            summary = summary + 'P31/'
    #---
    if 'P17' not in AlreadyThere:
        P17 = FindP17(page)
        if P17:
            data["claims"]["P17"] = [P17]
            summary = summary + 'P17/'
    #---
    """if 'P625' not in AlreadyThere:
        P625 = MakeP625(ss , page)
        if P625:
            data["claims"]["P625"] = [P625]
            summary = summary + 'P625/'"""
    #---
    if 'P2044' not in AlreadyThere:
        P2044 = MakeP2044(ss)
        if P2044:
            data["claims"]["P2044"] = [P2044]
            summary = summary + 'P2044/'
    #---
    if 'P1566' not in AlreadyThere:
        P1566 = MakeP1566(ss)
        if P1566:
            data["claims"]["P1566"] = [P1566]
            summary = summary + 'P1566/'
    #---
    """if 'P131' not in AlreadyThere:
        P131 = MakeP131(ss)
        if P131:
            data["claims"]["P131"] = [P131]
            summary = summary + 'P131/'"""
    #---
    if summary != '':
        summary = Mysummary + ', add: ' + summary + '.'
        summary = re.sub( '\/\.' , '' , summary)
        #---
        if not test:
            pywikibot.output(summary)
            New_API2(data, summary)
            #try:
            #if page:
                #item.editEntity(data, summary = summary)
            #else:
            #except:
                #pywikibot.output( '*<<lightred>> > error with page "%s" < :' % (  page.title(asLink=True) ) )
                #pass
            #treat(page, item)
    else:
        pywikibot.output('* nothing to add..')
    #---
    #return data , summary
#---
def CreateNewItem(ss, page , num):#vaul
        pywikibot.output( '**<<lightyellow>> CreateNewItem:' )
        title = page.title(as_link=False)
        title = fixtitle(title)
        label = title.split('(')[0]
        #---
        # Create a new page, which is unlinked
        data = {}
        data['labels'] = {}
        data['labels']['ceb'] = {'language': 'ceb','value': label}
        data['labels']['en'] = {'language': 'en','value': label}
        data['sitelinks'] = {}
        data['sitelinks']['cebwiki'] = {'site': 'cebwiki','title': title }
        #---
        data3 = {
            'labels': {
                'ceb': {
                    'language': 'ceb',
                    'value': label , 
                },
                'en': {
                    'language': 'en',
                    'value': label , 
                }
            },
            'sitelinks': {
                'cebwiki': {
                    'site': 'cebwiki',
                    'title': title
                }
            },
        }
        #---
        mySummary = ('Bot:New item from [[w:ceb:%s|cebwiki]]'  % page.title(as_link=False))
        #item = pywikibot.ItemPage(repo)
        #---

        AddClaims__2(data, ss, page , mySummary)
            
targetparam = [#'country',
                  #'state',
                  #'state',
                  #'region',
                  #'lat_d',
                  #'long_d',
                  'native_name',
                  'category',
                  'elevation',
                  'geonames',
                  ]
#---
def PPPNew(params):    
    c = {}
    for ta in targetparam:
        c[ta] = ''
    #---
    for pa in params:
        param, sep, value = pa.partition('=')
        param = param.strip()
        #param = param.replace('_', ' ')     
        param = param.replace('  ', ' ')
        #---
        if param in targetparam:
            value = value.split('\n')[0].split('<')[0]
            #value = value.replace('  ', ' ').replace('" ', '"').replace(' "', '"').replace('\s', '').replace('\n', '')
            if value.strip() !='':
                c[param] = value.strip()
    #---
    #pywikibot.output( ' * category : ' + c['category'])
    #---
    #pywikibot.output(c)
    return c
#---
TargetTemplates = ['Geobox' , 'geobox']
#---

Pages_P17_Table = {}

def FindP17(pagetitle):
    if pagetitle in Pages_P17_Table:
        Q =  Pages_P17_Table[pagetitle]
        Js = makejson('P17', Q)
        return Js
    return False
    
def find_P17_templatee(templatesWithParams , pagetitle):
    #paghimo ni bot
    for (template, params) in templatesWithParams:
            TargetTemp = template.title(withNamespace=False)
            #pywikibot.output("* found temp : " + TargetTemp)
            if (TargetTemp == 'paghimo ni bot') or (TargetTemp ==  'Paghimo ni bot'):
                #pywikibot.output("* found temp : paghimo ni bot" )
                for pa in params:
                    pa = pa.strip()
                    pa = re.sub( ' ' , '_' , pa )
                    if pa in P17Table:
                        #pywikibot.output(pa)
                        #params2 = PPPNew(params)
                        pywikibot.output( 'Found contry: "%s" with Q:"%s" , "%s"'  % (pa , P17Table[pa]['Q'] , P17Table[pa]['label'] ) )
                        if pagetitle == 'NONONO':
                            return P17Table[pa]['Q']
                        else:
                            Pages_P17_Table[pagetitle] = P17Table[pa]['Q']
                        

def ISRE(page, pagetitle, num):
    sss =  ''
    item = getwditem(pagetitle)                                         #ايجاد عنصر ويكي بيانات للصفحة
    templatesWithParams = page.templatesWithParams()
    params2 = {}
    #---
    if 'logname' in LOOO:
        if LOOO['logname'] == '':
            LOOO['logname'] = 'tot'
    #---
    s  = {} #
    Notemp = False
    for (template, params) in templatesWithParams:
            TargetTemp = template.title(withNamespace=False)
            if TargetTemp in TargetTemplates:
                params2 = PPPNew(params)
                Notemp = True
    #---
    if Notemp:
        #find_P17_templatee(templatesWithParams , pagetitle)
        params2['title'] = pagetitle
        s = params2
        if item:
            pywikibot.output("* found item: " + item.title() )
            AddClaims(item, s, page )
        else:
            pywikibot.output("* no item: " )
            #P31 = MakeP31(s) #makejson( 'P31' , '')
            #if P31:
                #CreateNewItem(s, page, num)
    else:
        pywikibot.output("*don't found template: " + str(TargetTemplates) )
        
def ISRE_Page_Item(page, pagetitle, item):
    sss =  ''
    templatesWithParams = page.templatesWithParams()
    params2 = {}
    #---
    if 'logname' in LOOO:
        if LOOO['logname'] == '':
            LOOO['logname'] = 'tot'
    #---
    s  = {} #
    Notemp = False
    for (template, params) in templatesWithParams:
            TargetTemp = template.title(withNamespace=False)
            if TargetTemp in TargetTemplates:
                params2 = PPPNew(params)
                Notemp = True
    #---
    if Notemp:
        #find_P17_templatee(templatesWithParams , pagetitle)
        params2['title'] = pagetitle
        s = params2
        if item:
            pywikibot.output("* found item: " + item.title() )
            AddClaims(item, s, page )
    else:
        pywikibot.output("*don't found template: " + str(TargetTemplates) )
        
#---
LOOO = {'logname' : 'tot'}

def log_new(title , log):#vaul
    #pywikibot.output( '**<<lightyellow>> log_new :' )
    #---
    log = 'totlog/' +  LOOO['logname'] + log
    title = title + '\n'
    with codecs.open(JlobalFileFloder + log + ".log.csv", "a", encoding="utf-8") as logfile:
        try:   
            logfile.write(title)
        except :
            pass
    logfile.close()
       
test = False#False#True
QS2 = False#False#True

#---        
def mainwithcat(*args):
    #---
    args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Paghimo_ni_bot_2016-10'}
    pywikibot.output(args)
    options = {}
    #---
    generator = gent.get_gent(*args)
        
    num = 0

    for page in generator:
        num += 1
        title = page.title(as_link=False)
        #start(text, title)
        #pywikibot.output(num)
        #ISRE(page , title, num )
        #try:
        if page:
            pywikibot.output( '*<<lightred>> >%d page "%s" :' % ( num , title ) )
            ISRE( page , title, num )
        else:
        #except:
            pywikibot.output( '*<<lightred>> >%d error with page "%s" < :' % ( num , title ) )
            pass
#---
def update_API2(q, data , summary):
    himoAPI.New_Mult_Des( q, data, summary , False )
#---
def New_API2(data2, summary):
    himoAPI.New_API(data2, summary)
    """data = str(data2)
    data = re.sub(  "u\'" , "'" , data)
    data = re.sub(  'u\"' , '"' , data)
    r4 = session.post(api_url, data={
        "action": "wbeditentity",
        "format": "json",
        "maxlag": "3",
        "new": "item",
        "summary": summary,
        "bot": 1,
        'utf8': 1,
        "data": data , 
        'token': r3.json()['query']['tokens']['csrftoken'],
    })
    #pywikibot.output(data)
    #--- ------
    text = r4.text
    if 'error' in text :
        pywikibot.output ('<<lightred>> ** error. : ')
        #---
        if 'wikibase-api-invalid-json' in text :
            pywikibot.output('<<lightred>>    - "wikibase-api-invalid-json" ')
        else:
            pywikibot.output(text)
            #---
        log_new(data2['sitelinks']['cebwiki']['title'] , '_error')
    else:
        pywikibot.output ('<<lightgreen>> ** true.......................')
        #pywikibot.output (text)
        log_new(data2['sitelinks']['cebwiki']['title'] , '_done')"""

#---
# end of himoAPI.py file
#---
cebwiki = pywikibot.Site("ceb", "wikipedia")

def New_Maino(Jlobal_File_Floder , logname):
    if logname !='' : 
        pywikibot.output(  '<<lightred>> ----------------------\n----------------------\n----------------------\n' )
        pywikibot.output(  '**<<lightyellow>> logname : "%s"' %  logname )
        LOOO['logname'] = logname
        LOOO['Jlobal_File_Floder'] = Jlobal_File_Floder
        num = 0
        #---
        file = Jlobal_File_Floder + logname + ".txt"
        #file = logname + ".txt"         #jupyter
        with codecs.open( file , "r", encoding="utf-8") as logfile:
            Listo = logfile.read()
        logfile.close()
        #---
        #List = Listo.split('\r')
        List = Listo.split('\n')
        LenList = len(List)
        #pywikibot.output(' * text : ')
        #pywikibot.output(text)
        
        #---
        for line in List:
            if line !='' :
                num += 1
                page = pywikibot.Page(cebwiki, line)
                title = page.title(as_link=False)
                pywikibot.output("* %d/%d :  " % ( num , LenList )  + title)
                if page :
                    ISRE(page , title, num )
                    
def Main_Test():
    pywikibot.output( '**<<lightyellow>> Main_Test:')
    TestTitle = 'Agnettahågan'
    #---
    page = pywikibot.Page(cebwiki, TestTitle)
    title = page.title(as_link=False)
    if page:
        ISRE(page , title, 0 )
        
JlobalFileFloder = ""  
#JlobalFileFloder = "ye/"
#---

MainTest = False#False#True

if __name__ == "__main__":
    if MainTest:
        Main_Test()
    else:
        mainwithcat()
        
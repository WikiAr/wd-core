#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

new pages from file

python pwb.py update/update

python pwb.py items/up2 -lang:ceb -file:items/m.txt

"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
import json
import time

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
import urllib.request
import urllib.parse

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
#timesleep = 0
#from category import *
#---
timesleep = {'timesleep': 0 }
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
#---
maxlag = "3" #"3"
import requests
#---
#from API.useraccount import *
from API import useraccount
api_url = 'https://' + 'www.wikidata.org/w/api.php'
username = useraccount.username
password = useraccount.password
#---
session = requests.Session()
# get login token
r1 = session.get(api_url, params={
    'format': 'json',
    'action': 'query',
    'meta': 'tokens',
    'type': 'login',
})
r1.raise_for_status()

# log in
r2 = session.post(api_url, data={
    'format': 'json',
    'action': 'login',
    'lgname': username,
    'lgpassword': password,
    'lgtoken': r1.json()['query']['tokens']['logintoken'],
})
if r2.json()['login']['result'] != 'Success':
    raise RuntimeError(r2.json()['login']['reason'])
#---

def CheckStopNewItem(pp):
    ppvalue = [ 'newitem' , 'claim' , 'desc' , 'labels']
    title = 'user:Mr.Ibrahembot/stop/' + pp
    wikidatasite=pywikibot.Site('wikidata','wikidata') 
    page = pywikibot.Page(wikidatasite, title)
    #---
    if page:
        text = page.text
        if text != '':
            pywikibot.output('<<lightred>>  -----------------------')
            pywikibot.output('<<lightred>> STOOP ME . "%s" ' % pp )
            pywikibot.output('<<lightred>>  -----------------------')
            pywikibot.stopme()
            return sasa
#---
def MakeStr(type , NewDesc):
    value = 'value'
    language = 'language'
    #---
    if type == 'sitelinks':
        language = 'site'
        value = 'title'
    #---
    Newline = ''
    for la in NewDesc:
        test = re.sub( '\'' , '' , NewDesc[la][value])
        #sa = "'" + la + "': " + "{'value': '" + NewDesc[la]['value'] + "', 'language': '" + la + "'},"
        #---
        if test != NewDesc[la][value]:
            sa = '"' + la + '": ' + '{"' + value + '": "' + NewDesc[la][value] + '", "' + language + '": "' + la + '"},'
        else:
            sa = "'" + la + "': " + "{'" + value + "': '" + NewDesc[la][value] + "', '" + language + "': '" + la + "'},"
        #---

        Newline = Newline + sa
    data3 = "'" + type + "' :{ " + Newline + "} , "
    return data3
#---
def Fix_Data_New(data2):
    raws = ''
    claims = {}
    labels = {}
    descriptions = {}
    sitelinks = {}
    #---
    if 'claims' in data2:
        claims = data2['claims']
        ccc = str(claims)
        ccc = re.sub(  "u\'" , "'" , ccc)
        ccc = re.sub(  'u\"' , '"' , ccc)
        #cl = "'claims' :{" + ccc + "}, "
        cl = "'claims' :" + ccc + ", "
        raws = raws + cl
    #---
    if 'labels' in data2:
        labels = data2['labels']
        la = MakeStr('labels' , labels)
        raws = raws + la
    #---
    if 'descriptions' in data2:
        descriptions = data2['descriptions']
        da = MakeStr('descriptions' , descriptions)
        pywikibot.output(da)
        raws = raws + da
    #---
    if 'sitelinks' in data2:
        sitelinks = data2['sitelinks']
        si = MakeStr('sitelinks' , sitelinks)
        raws = raws + si
    #---
    final = '{' + raws + '}'
    return final
#---
def New_API2(data2, summary):
    # get edit token
    r3 = session.get(api_url, params={
        'format': 'json',
        'action': 'query',
        'meta': 'tokens',
    })
    #---
    CheckStopNewItem('newitem')
    data22 = Fix_Data_New(data2)
    dato = {
        "action": "wbeditentity",
        "new": "item",
        "summary": summary,
        "data": data22 , 
    }
    dato['token'] = r3.json()['query']['tokens']['csrftoken']
    dato['bot'] = 1
    dato['format'] = 'json'
    dato['maxlag'] = maxlag
    dato['utf8'] = 1
    r4 = session.post(api_url, data = dato)
    timesleep = 0
    if 'success' in r4.text:
        pywikibot.output('<<lightgreen>> ** New_API2: true. "%s" time.sleep(%s)' % (summary , timesleep) )
        time.sleep(timesleep)
    else:
        pywikibot.output(r4.text)
#---
def makejson(property, numeric):
    #---
    if numeric !='':
        numeric = re.sub('Q','',numeric)
        Q = 'Q' + numeric#          
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
#---
def MakeP1566(geonames):
    pe =  {
        "mainsnak": {
            "snaktype": "value",
            "property": "P1566",
            "datavalue": {
                "value": geonames,
                "type": "string"
            },
            "datatype": "external-id"
        },
        "type": "statement",
        "rank": "normal",
        "references":  [references]
        }
    return pe
#---
def MakeP2044(srtm3, geonames):
    if srtm3 !='':
        try:
            so = int(srtm3)
            if so < 0 or so > 1000:
                return False
            else:
                pe = {
                        "mainsnak": {
                            "snaktype": "value",
                            "property": "P2044",
                            "datavalue": {
                                "value": {
                                    
                                    "amount": srtm3,
                                    "unit": "http://www.wikidata.org/entity/Q11573"
                                },
                                "type": "quantity"
                            },
                            "datatype": "quantity"
                        },
                        "type": "statement",
                        "rank": "normal",
                        "references":  [
                                    {
                                        "snaks": {
                                            "P123": [
                                                {
                                                    "snaktype": "value",
                                                    "property": "P123",
                                                    "datavalue": {
                                                        "value": {
                                                            "entity-type": "item",
                                                            "numeric-id": 830106,
                                                            "id": "Q830106"
                                                        },
                                                        "type": "wikibase-entityid"
                                                    },
                                                    "datatype": "wikibase-item"
                                                }
                                            ],
                                            "P1566": [
                                                {
                                                    "snaktype": "value",
                                                    "property": "P1566",
                                                    "datavalue": {
                                                        "value": geonames,
                                                        "type": "string"
                                                    },
                                                    "datatype": "external-id"
                                                }
                                            ]
                                        },
                                        "snaks-order": [
                                            "P123",
                                            "P1566"
                                        ]
                                    }
                                ]
                        }
                return pe
        except:
            return False
#---
def getwditem(title):
    ceb = pywikibot.Site("ceb", "wikipedia") 
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
                                    "latitude": coordinate.lat, #ss['lat'],
                                    "longitude": coordinate.lon,    #ss['lng'],
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
        return pe       
#---
def logCategoryError(cat , title):#vaul
    pywikibot.output('<<lightgreen>> \t* category:"%s" not in ss page: "%s"' % ( cat , title) )
    logFil = "items/category/" + cat
    #---
    form = "%s\t%s\n"
    ccc  = (form % (cat , title))
    #---
    #if QS2Rows:
    with codecs.open( logFil + ".log.csv", "a", encoding="utf-8") as logFil:
      try:   
         logFil.write(ccc)
      except :
         pass
    logFil.close()
#---
def findtext(id):
    #url = 'api.geonames.org/getJSON?formatted=true&username=ibrahemqasim&lang=ar&geonameId=' + id
    url = 'api.geonames.org/getJSON?formatted=true&username=ibrahemqasim&lang=en&geonameId=' + id
    s = urllib.request.urlopen('http://'+ url).read().strip().decode('utf-8')
    json1 = json.loads(s)
    #pywikibot.output(url)
    #pywikibot.output(json1)
    return json1
#--- 
def update_api(q, data2, summary):
    # get edit token
    r3 = session.get(api_url, params={
        'format': 'json',
        'action': 'query',
        'meta': 'tokens',
    })
    #---
    #CheckStopNewItem('newitem')
    data22 = Fix_Data_New(data2)
    dato = {
        "action": "wbeditentity",
        "id": q,
        "summary": summary,
        "data": data22 , 
    }
    dato['token'] = r3.json()['query']['tokens']['csrftoken']
    dato['bot'] = 1
    dato['format'] = 'json'
    dato['maxlag'] = maxlag
    dato['utf8'] = 1
    #r4 = {}
    #text = {'text'}
    r4 = session.post(api_url, data = dato)
    text = r4.text
    timesleep = 0
    if 'success' in text:
        pywikibot.output('<<lightgreen>> ** New_API2: %s true. "%s" time.sleep(%s)' % (q , summary , timesleep) )
        time.sleep(timesleep)
    elif 'maxlag' in text:
        pywikibot.output('<<lightred>> ** maxlag. time.sleep(3)')
        time.sleep(3)
    else:
        pywikibot.output(text)
#--- 
from P17_Table import P17Table
from categoryNew import CategoryTableNew
from Contries import ContriesTable
#from places import placesTable
from ydn3.places import placesTable
from ydn3 import rep
from ydn3.newlist import NewList
#---
def find_P17_templatee(page):
    pagetitle = page.title(as_link=False)
    templatesWithParams = page.templatesWithParams()
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
                        return P17Table[pa]#['Q']
    return False
#---
list = {}
for catt in CategoryTableNew:
    qqq = CategoryTableNew[catt]['item']
    list[qqq] = CategoryTableNew[catt]
#---
Comma = { 'ar' : "في" 
        , 'en' : "in" 
        , 'fr' : "en" 
        , 'nl' : "in" 
        , 'es' : "en"  
        , 'de' : "im"  
        , 'it' : "in"  
        , 'fa' : "در"  
        , 'eo' : "en"  
        , 'et' : "in"  
        , 'el' : "στην"  
        , 'ru' : "в"  
        , 'sco' : "in"  
        , 'nb' : "i"  
        }
#---
def makeComma(lang ,contry , place):
    cooComma = {
        'de' : { 'coma': 'im' , 'contry' : ['Q794' , 'Q805' , '' , '' ] }
    }
    coma = Comma[lang]
    #---
    if (lang in cooComma) and (contry in cooComma[lang]['contry']):
        coma = cooComma[lang]['coma']
    #---
    return coma
#---
falselabels = [list[x]["ar"] for x in list]
#---
def AddDesc(item , Q_P17 , p31code , CountryName):
    translations = {}
    datee = {}
    pywikibot.output('*Q_P17 "%s",  p31code:"%s" .' % (Q_P17 , p31code) )
    #---
    if Q_P17 in ContriesTable.keys():
        if (p31code in placesTable.keys()):
            langkeys = ContriesTable[Q_P17].keys()
            lar = ContriesTable[Q_P17].get('ar')
            #pywikibot.output('*Q_P17 "%s",p31:"%s", langkeys:"%s"' % ( lar , placesTable[p31code].get('ar') , str(langkeys) ) )
            pywikibot.output('*Q_P17 "%s",p31:"%s"' % ( lar , placesTable[p31code].get('ar')  ) )
            for lang in langkeys:
                if lang in placesTable[p31code]:
                    if not lang in item.descriptions:
                        des3 = placesTable[p31code][lang] + ' ' + makeComma(lang ,Q_P17 , p31code) + ' ' + ContriesTable[Q_P17][lang]
                        des = rep.Make_Des_One_Lang(des3 , lang , p31code , Q_P17 )
                        if des:
                            datee[lang] = des
                            #pywikibot.output('* lang:"%s" des:"%s".' % (lang,des) )
        else:
            pywikibot.output('* p31code:"%s" not in placesTable.' % p31code)
    else:
        pywikibot.output('* Q_P17:"%s" not in ContriesTable.' % Q_P17)
    #---
    sdo = False
    if 'ar' not in item.descriptions:
        sdo  = True
    elif item.descriptions['ar'] in falselabels:
        sdo  = True
    if sdo:
        desc = False
        p31code = p31code#ss['fcl'] + '.' + ss['fcode']
        if CountryName != '':
                if p31code in list and list[p31code]["ar"] != '': 
                    desc = list[p31code]["ar"] + ' في ' + CountryName
                    datee['ar'] = desc
    #---
    if (p31code in NewList) and (Q_P17 in NewList[p31code]):
        for lang4 in NewList[p31code][Q_P17]:
            datee[lang4] = NewList[p31code][Q_P17][lang4]
    #---
    if 'en' in datee.keys():
        datee['en-ca'] = datee['en']
        datee['en-gb'] = datee['en']
    #---
    for lang2 in datee.keys():
        if lang2 not in item.labels:
            datee[lang2] = {'language':lang2,'value': datee[lang2] }
    #pywikibot.output('*Add descriptions: %s' % datee.keys() )
    #pywikibot.output(data['descriptions'])
    return datee
#---
def log2(tt , property , CorrectValue):
    #form = '%s\t%s\t%s\t%s\n' % ( q_value , q , property , CorrectValue )
    #pywikibot.output(form)
    with codecs.open("items/" + property + '_' + CorrectValue + "_False.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(str(tt))
      except:
            pywikibot.output("Error writing")
#---
def check_P31(q, property , claims , CorrectValue ):
    NoClaim = True
    if property in claims:
        #pywikibot.output('find ' + property)
        for claim in claims[property]:
            claim = claim.toJSON()
            va = claim['mainsnak']["datavalue"]
            if ('value' in va) and ('numeric-id' in va['value']):
                q_value = 'Q' + str(va['value']['numeric-id'])
                if q_value == CorrectValue :
                    #pywikibot.output(' Same P31 q_value == CorrectValue ' + str(q_value))
                    NoClaim = False
                else:
                    pywikibot.output('%s: q_value "%s" != id "%s"' % ( property , q_value, CorrectValue ))
                    fao = '%s\t%s\t%s\t%s\n' % ( q_value , q , property , CorrectValue )
                    log2(fao , property , CorrectValue)
                    NoClaim = False
    return NoClaim
#---
def Claims_for_item(item , geonames ,p31code ,  page ):
    #---
    #---
    q = item.title(as_link=False)
    #data["claims"] = {}
    dataclaims = {}
    find_desc = [x for x in item.descriptions.keys()]
    if find_desc:
        pywikibot.output( '**<<lightyellow>> find_desc : ' + str(find_desc))
    #---
    claims = ['P31' , 'P625' , 'P17' , 'P2044' , 'P1566' , 'P131']
    AlreadyThere = []
    if item:
        for cla in claims:
            if cla in item.claims:
                AlreadyThere.append(cla)
    #---
    if AlreadyThere:
        pywikibot.output( '**<<lightyellow>> AlreadyThere : ' + str(AlreadyThere))
    #---
    ss = {}
    data = {}
    addclaims = []
    data["claims"] = {}
    data["descriptions"] = {}
    #summary = ''
    pagetitle = page.title(as_link=False)
    P31 = False
    if p31code != '':
        check_P31(q, 'P31' , item.claims , p31code )
        if 'P31' not in AlreadyThere:
            P31 = pp = makejson( 'P31' , p31code )
            if P31:
                data["claims"]["P31"] = [P31]
                #summary = summary + 'P31/'
                addclaims.append('P31')
            else:
                pywikibot.output('* no P31 ..')
    #---
    CountryName = ''
    P17 = False
    P17_Q = find_P17_templatee(page)#
    if P17_Q:
        Q_P17 = P17_Q['Q']
        check_P31(q, 'P17' , item.claims , Q_P17 )
        CountryName = P17_Q['label']
    #---
    if 'P17' not in AlreadyThere:
        if P17_Q:
            P17 = makejson('P17', Q_P17)
            data["claims"]["P17"] = [P17]
            addclaims.append('P17')
    #---
    if 'P625' not in AlreadyThere:
        P625 = MakeP625(ss , page)
        if P625:
            data["claims"]["P625"] = [P625]
            addclaims.append('P625')
    #---
    if geonames != '':
        if 'P1566' not in AlreadyThere:
            P1566 = MakeP1566(geonames)###
            if P1566:
                data["claims"]["P1566"] = [P1566]
                addclaims.append('P1566')
    #---
    if addclaims :
        if P17_Q and p31code:
            description = AddDesc(item , Q_P17 , p31code  , CountryName)
            data['descriptions'] = description
    deskeys = [x for x in data["descriptions"].keys()]
    #---
    if addclaims :
        #dess = ','.join(deskeys)
        #---
        cp = '/'.join(addclaims)
        summary = 'Bot: Add claims %s from [[w:ceb:%s|cebwiki]]' % (cp , page.title(as_link=False)  )
        if deskeys:
            #summary = summary + ' Add descriptions %s.'  % dess
            summary = summary + ' - Add descriptions:(%d langs).' % ( len(deskeys) )
        pywikibot.output(summary)
        #---
        #New_API2(data, summary)
        update_api(q, data, summary)
    else:
        pywikibot.output('* nothing to add..')
        
    #pywikibot.output('*descriptions : %s' % str(data["descriptions"]) )
    #pywikibot.output('*labels : %s' % str(data["labels"]) )
    #pywikibot.output('*claims : %s' % str(data["claims"].keys()) )
#---
def ISRE(page):
    TargetTemplates = ['Geobox' , 'geobox']
    #---
    pagetitle = page.title(as_link=False)
    #---
    item = getwditem(pagetitle)                                         #ايجاد عنصر ويكي بيانات للصفحة
    #templatesWithParams = page.templatesWithParams()
    #---
    s  = {} #
    Notemp = False
    '''for (template, params) in templatesWithParams:
            TargetTemp = template.title(withNamespace=False)
            if TargetTemp in TargetTemplates:
                for pa in params:
                    param, sep, value = pa.partition('=')
                    if param == 'geonames':
                        geonames = value.split('\n')[0].split('<')[0]
                        geonames = geonames.strip()
                Notemp = True'''
    #---  
    if item:    
        pywikibot.output("* find item: " )
        text = page.text
        geonames = ''
        pat =  'geonames\s*=\s*(.*)\n'
        OtherName =  re.compile( pat )
        na = OtherName.findall(text)
        if na:
            geonames = na[0].strip()
            pywikibot.output("*found geonames " + str(geonames) )
        
        pat2 =  '\<\!\-\-([AHLPR-V]\.[A-Z1-5]{2,5})\-\-\>'
        sssss =  re.compile( pat2 )
        P31 = sssss.findall(text)
        p31code = ''
        if P31:
            #pywikibot.output('findP31new: ' +  P31[0])
            if P31[0] in CategoryTableNew:
                Notemp = True
                p31code = CategoryTableNew[P31[0]]['item']
            else:
                logCategoryError(P31[0] , pagetitle)

        else:
            pywikibot.output("*don't found template: " + str(TargetTemplates) )
        Claims_for_item(item , geonames ,p31code ,  page )

    else:
        pywikibot.output("* no item: ")
#---        
def mainwithcat(*args):
    #args = {'-lang:ceb' , '-page:Ojo_Caliente_(abang_nga_dapit)'}
    if sys.argv:
        if len(sys.argv) < 2 :
                args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Articles_without_Wikidata_item'}
    #pywikibot.output(args)
    options = {}
    #---
    generator = gent.get_gent(*args)
        
    num = 0
    for page in generator:
        num += 1
        title = page.title(as_link=False)
        if page:
            pywikibot.output( '*<<lightred>> >%d page "%s" :' % ( num , title ) )
            ISRE( page )
        else:
            pywikibot.output( '*<<lightred>> >%d error with page "%s" < :' % ( num , title ) )
            pass
#---
if __name__ == "__main__":
    mainwithcat()
#---
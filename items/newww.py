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
def MakeP31(ss , pagetitle , CategoryTableNew):
    if 'fcl' in ss:
        if 'fcode' in ss:
            code = ss['fcl'] + '.' + ss['fcode']
            if code in CategoryTableNew:
                pp = makejson( 'P31' , CategoryTableNew[code]["item"] )
                return pp
            else:
                logCategoryError(code , pagetitle)
        else:
            pywikibot.output('NO fcode.')
            pywikibot.output(ss)
    else:
        pywikibot.output('NO fcl.')
        pywikibot.output(ss)
    return False
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
ISO3166 = {
    "AD" : "Q228",
    "AE" : "Q878",
    "AF" : "Q889",
    "AG" : "Q781",
    "AI" : "Q25228",
    "AL" : "Q222",
    "AM" : "Q399",
    "AN" : "Q25227",
    "AO" : "Q916",
    "AQ" : "Q21590062",
    "AR" : "Q414",
    "AS" : "Q30",
    "AT" : "Q40",
    "AU" : "Q408",
    "AW" : "Q21203",
    "AX" : "Q33",
    "AZ" : "Q227",
    "BA" : "Q225",
    "BB" : "Q244",
    "BD" : "Q902",
    "BE" : "Q31",
    "BF" : "Q965",
    "BG" : "Q219",
    "BH" : "Q398",
    "BI" : "Q967",
    "BJ" : "Q962",
    "BL" : "Q25362",
    "BM" : "Q23635",
    "BN" : "Q921",
    "BO" : "Q750",
    "BQ" : "Q165783",
    "BQ" : "Q55",
    "BR" : "Q155",
    "BS" : "Q778",
    "BT" : "Q917",
    "BV" : "Q23408",
    "BW" : "Q963",
    "BY" : "Q184",
    "BY" : "Q2895",
    "BZ" : "Q242",
    "CA" : "Q16",
    "CC" : "Q36004",
    "CD" : "Q974",
    "CF" : "Q929",
    "CG" : "Q971",
    "CH" : "Q39",
    "CI" : "Q1008",
    "CK" : "Q26988",
    "CL" : "Q298",
    "CM" : "Q1009",
    "CN" : "Q148",
    "CO" : "Q739",
    "CR" : "Q800",
    "CS" : "Q37024",
    "CU" : "Q241",
    "CV" : "Q1011",
    "CW" : "Q25279",
    "CX" : "Q31063",
    "CY" : "Q229",
    "CZ" : "Q213",
    "DD" : "Q16957",
    "DE" : "Q183",
    "DJ" : "Q977",
    "DK" : "Q35",
    "DM" : "Q784",
    "DO" : "Q786",
    "DZ" : "Q262",
    "EC" : "Q736",
    "EE" : "Q191",
    "EG" : "Q79",
    "EH" : "Q6250",
    "ER" : "Q986",
    "ES" : "Q29",
    "ET" : "Q115",
    "FI" : "Q33",
    "FJ" : "Q712",
    "FK" : "Q1249802",
    "FK" : "Q9648",
    "FM" : "Q702",
    "FO" : "Q4628",
    "FR" : "Q142",
    "GA" : "Q1000",
    "GB" : "Q145",
    "GD" : "Q769",
    "GE" : "Q230",
    "GF" : "Q3769",
    "GG" : "Q25230",
    "GH" : "Q117",
    "GI" : "Q1410",
    "GL" : "Q223",
    "GM" : "Q1005",
    "GN" : "Q1006",
    "GP" : "Q17012",
    "GQ" : "Q983",
    "GR" : "Q41",
    "GS" : "Q35086",
    "GT" : "Q774",
    "GU" : "Q16635",
    "GW" : "Q1007",
    "GY" : "Q734",
    "HK" : "Q8646",
    "HM" : "Q131198",
    "HN" : "Q783",
    "HR" : "Q224",
    "HT" : "Q790",
    "HU" : "Q28",
    "ID" : "Q252",
    "IE" : "Q27",
    "IL" : "Q801",
    "IM" : "Q9676",
    "IN" : "Q668",
    "IO" : "Q145",
    "IQ" : "Q796",
    "IR" : "Q794",
    "IS" : "Q189",
    "IT" : "Q38",
    "JE" : "Q785",
    "JM" : "Q766",
    "JO" : "Q810",
    "JP" : "Q17",
    "KE" : "Q114",
    "KG" : "Q813",
    "KH" : "Q424",
    "KI" : "Q710",
    "KM" : "Q970",
    "KN" : "Q763",
    "KP" : "Q423",
    "KR" : "Q884",
    "KW" : "Q817",
    "KY" : "Q5785",
    "KZ" : "Q232",
    "LA" : "Q819",
    "LB" : "Q822",
    "LC" : "Q760",
    "LI" : "Q347",
    "LK" : "Q854",
    "LR" : "Q1014",
    "LS" : "Q1013",
    "LT" : "Q37",
    "LU" : "Q32",
    "LV" : "Q211",
    "LY" : "Q1016",
    "MA" : "Q1028",
    "MC" : "Q235",
    "MD" : "Q217",
    "ME" : "Q236",
    "MF" : "Q126125",
    "MG" : "Q1019",
    "MH" : "Q709",
    "MK" : "Q221",
    "ML" : "Q912",
    "MM" : "Q836",
    "MN" : "Q711",
    "MO" : "Q14773",
    "MP" : "Q16644",
    "MQ" : "Q17054",
    "MR" : "Q1025",
    "MS" : "Q13353",
    "MT" : "Q233",
    "MU" : "Q1027",
    "MV" : "Q826",
    "MW" : "Q1020",
    "MX" : "Q96",
    "MY" : "Q833",
    "MZ" : "Q1029",
    "NA" : "Q1030",
    "NC" : "Q33788",
    "NE" : "Q1032",
    "NF" : "Q31057",
    "NG" : "Q1033",
    "NI" : "Q811",
    "NL" : "Q29999",
    "NL" : "Q55",
    "NO" : "Q20",
    "NP" : "Q837",
    "NR" : "Q697",
    "NU" : "Q34020",
    "NZ" : "Q664",
    "OM" : "Q842",
    "PA" : "Q804",
    "PE" : "Q419",
    "PF" : "Q30971",
    "PG" : "Q691",
    "PH" : "Q928",
    "PK" : "Q843",
    "PL" : "Q36",
    "PM" : "Q34617",
    "PN" : "Q35672",
    "PR" : "Q1183",
    "PS" : "Q407199",
    "PT" : "Q45",
    "PW" : "Q695",
    "PY" : "Q733",
    "QA" : "Q846",
    "RE" : "Q17070",
    "RO" : "Q218",
    "RS" : "Q403",
    "RU" : "Q159",
    "RW" : "Q1037",
    "SA" : "Q851",
    "SB" : "Q685",
    "SC" : "Q1042",
    "SD" : "Q1049",
    "SE" : "Q34",
    "SG" : "Q334",
    "SH" : "Q192184",
    "SI" : "Q215",
    "SJ" : "Q842829",
    "SK" : "Q214",
    "SL" : "Q1044",
    "SM" : "Q238",
    "SN" : "Q1041",
    "SO" : "Q1045",
    "SR" : "Q730",
    "SS" : "Q958",
    "ST" : "Q1039",
    "SV" : "Q792",
    "SX" : "Q26273",
    "SY" : "Q858",
    "SZ" : "Q1050",
    "TC" : "Q145",
    "TD" : "Q657",
    "TF" : "Q129003",
    "TG" : "Q945",
    "TH" : "Q869",
    "TJ" : "Q863",
    "TK" : "Q36823",
    "TL" : "Q574",
    "TM" : "Q874",
    "TN" : "Q948",
    "TO" : "Q678",
    "TR" : "Q43",
    "TT" : "Q754",
    "TV" : "Q672",
    "TW" : "Q865",
    "TZ" : "Q924",
    "UA" : "Q212",
    "UG" : "Q1036",
    "UM" : "Q30",
    "US" : "Q30",
    "UY" : "Q77",
    "UZ" : "Q265",
    "VA" : "Q237",
    "VC" : "Q757",
    "VE" : "Q717",
    "VG" : "Q145",
    "VI" : "Q30",
    "VN" : "Q881",
    "VU" : "Q686",
    "WF" : "Q35555",
    "WS" : "Q683",
    "XK" : "Q1246",
    "YE" : "Q805",
    "YT" : "Q17063",
    "YU" : "Q83286",
    "YU" : "Q838261",
    "ZA" : "Q258",
    "ZM" : "Q953",
    "ZW" : "Q954"
}
def FindP17(ss):
    code2 = ss['countryCode']
    if code2 in ISO3166:
        Q =  ISO3166[code2]
        Js = makejson('P17', Q)
        return Js
    return False
#---
def AddClaims__2(data, geonames ,p31code ,  page , Mysummary):
    #---
    from categoryNew import CategoryTableNew#ContriesNew
    from ContriesNew import ContriesTable#
    #---
    ss = findtext(geonames)
    data["claims"] = {}
    summary = ''
    pagetitle = page.title(as_link=False)
    P31 = pp = makejson( 'P31' , p31code )
    if P31:
        data["claims"]["P31"] = [P31]
        summary = summary + 'P31/'
    else:
        pywikibot.output('* no P31 ..')
    #---
    if P31:
        #---
        if 'name' in ss and ss['name'] != '':
            data['labels']['en'] = {'language': 'en','value': ss['name']}
        #---
        if 'alternateNames' in ss:
            for sds in ss['alternateNames']:
                if 'name' in sds and 'lang' in sds :
                    if sds['lang'] in ['en' , 'fr' , 'de', 'ar', 'fa', 'nl']:
                        lng = sds['lang']
                        value = sds['name']
                        data['labels'][lng] = {'language': lng,'value': value}
        #---
        P17 = False
        if 'countryCode' in ss:
            code2 = ss['countryCode']
            if code2 in ContriesTable:
                Q =  ContriesTable[code2]['item']
                P17 = makejson('P17', Q)
            if P17:
                data["claims"]["P17"] = [P17]
                summary = summary + 'P17/'
        #---
        if P17 and P31:
            desc = False
            code = ss['fcl'] + '.' + ss['fcode']
            countryCode = ss['countryCode']
            if 'ar' in ContriesTable[countryCode]:
                contry = ContriesTable[countryCode]['ar']
                if code in CategoryTableNew and ('ar' in CategoryTableNew[code]):
                    desc = CategoryTableNew[code]["ar"] + ' في ' + contry
            if desc:
                data['descriptions'] = {}
                data['descriptions']['ar'] = {'language':'ar','value': desc}
                pywikibot.output('*ar descriptions: %s' % desc)
        #---
        P2044 = MakeP2044(ss['srtm3'] , geonames)###
        if P2044:
            data["claims"]["P2044"] = [P2044]
            summary = summary + 'P2044/'
        #---
        P625 = MakeP625(ss , page)
        if P625:
            data["claims"]["P625"] = [P625]
            summary = summary + 'P625/'
        #---
        P1566 = MakeP1566(geonames)###
        if P1566:
            data["claims"]["P1566"] = [P1566]
            summary = summary + 'P1566/'
        #---
        if summary != '':
            summary = Mysummary + ', add: ' + summary + '.'
            summary = re.sub( '\/\.' , '' , summary)
            #---
            New_API2(data, summary)
        else:
            pywikibot.output('* nothing to add..')
#---

def CreateNewItem(geonames, p31code , page):#vaul
        #pywikibot.output( '**<<lightyellow>> CreateNewItem:' )
        title = page.title(as_link=False)
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
        mySummary = ('Bot:New item from [[w:ceb:%s|cebwiki]]'  % page.title(as_link=False))
        AddClaims__2(data , geonames, p31code ,  page , mySummary)
#---
def ISRE(page):
    TargetTemplates = ['Geobox' , 'geobox']
    #---
    pagetitle = page.title(as_link=False)
    #---
    item = getwditem(pagetitle)                                         #ايجاد عنصر ويكي بيانات للصفحة
    templatesWithParams = page.templatesWithParams()
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
    text = page.text
    geonames = ''
    pat =  'geonames\s*=\s*(.*)\n'
    OtherName =  re.compile( pat )
    na = OtherName.findall(text)
    if na:
        geonames = na[0].strip()
    from categoryNew import CategoryTableNew#ContriesNew
    pat2 =  '\<\!\-\-([AHLPR-V]\.[A-Z1-5]{2,5})\-\-\>'
    sssss =  re.compile( pat2 )
    P31 = sssss.findall(text)
    p31code = ''
    if P31:
        pywikibot.output('findP31new: ' +  P31[0])
        if P31[0] in CategoryTableNew:
            Notemp = True
            p31code = CategoryTableNew[P31[0]]['item']
            #---
            pywikibot.output("*found template: with " + str(geonames) )
            if item:
                pywikibot.output("* found item: " + item.title() )
            else:
                pywikibot.output("* no item: " )
                if geonames !='':
                    #try:
                        CreateNewItem(geonames, p31code , page)
                    #except:
                        #pass
        else:
            logCategoryError(P31[0] , pagetitle)
    else:
        pywikibot.output("*don't found template: " + str(TargetTemplates) )
#---        
def mainwithcat(*args):
    #args = {'-lang:ceb' , '-page:Ojo_Caliente_(abang_nga_dapit)'}
    if sys.argv:
        if len(sys.argv) < 2 :
                args = {'-lang:ceb' , '-ns:0' , '-catr:Kategoriya:Articles_without_Wikidata_item'}
    pywikibot.output(args)
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
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
                                            "numeric-id": 169514,
                                            "id": "Q169514"
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
    #data22 = Fix_Data_New(data2)
    data22 = json.JSONEncoder().encode(data2)

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
    sv = pywikibot.Site("sv", "wikipedia") 
    EngPage = pywikibot.Page(sv, title)
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
P17Table = {
    "Afghanistan" : { "label": "أفغانستان", "Q": "Q889" ,"cat": "Robotskapade_Afghanistanartiklar" } , 
    "Albanien" : { "label": "ألبانيا", "Q": "Q222" ,"cat": "Robotskapade_Albanienartiklar" } , 
    "Algeriet" : { "label": "الجزائر", "Q": "Q262" ,"cat": "Robotskapade_Algerietartiklar" } , 
    "Amerikanska Samoa" : { "label": "ساموا الأمريكية", "Q": "Q30" ,"cat": "Robotskapade_Amerikanska_Samoaartiklar" } , 
    "Andorra" : { "label": "أندورا", "Q": "Q228" ,"cat": "Robotskapade_Andorraartiklar" } , 
    "Angola" : { "label": "أنغولا", "Q": "Q916" ,"cat": "Robotskapade_Angolaartiklar" } , 
    #"Antarktis" : { "label": "القارة القطبية الجنوبية", "Q": "Q51" ,"cat": "Robotskapade_Antarktisartiklar" } , 
    "Antigua och Barbuda" : { "label": "أنتيغوا وباربودا", "Q": "Q781" ,"cat": "Robotskapade_Antigua_och_Barbudaartiklar" } , 
    "Argentina" : { "label": "الأرجنتين", "Q": "Q414" ,"cat": "Robotskapade_Argentinaartiklar" } , 
    "Armenien" : { "label": "أرمينيا", "Q": "Q399" ,"cat": "Robotskapade_Armenienartiklar" } , 
    "Australien" : { "label": "أستراليا", "Q": "Q408" ,"cat": "Robotskapade_Australienartiklar" } , 
    "Azerbajdzjan" : { "label": "أذربيجان", "Q": "Q227" ,"cat": "Robotskapade_Azerbajdzjanartiklar" } , 
    "Bahamas" : { "label": "باهاماس", "Q": "Q778" ,"cat": "Robotskapade_Bahamasartiklar" } , 
    "Bahrain" : { "label": "البحرين", "Q": "Q398" ,"cat": "Robotskapade_Bahrainartiklar" } , 
    "Bangladesh" : { "label": "بنغلاديش", "Q": "Q902" ,"cat": "Robotskapade_Bangladeshartiklar" } , 
    "Barbados" : { "label": "باربادوس", "Q": "Q244" ,"cat": "Robotskapade_Barbadosartiklar" } , 
    "Belgien" : { "label": "بلجيكا", "Q": "Q31" ,"cat": "Robotskapade_Belgienartiklar" } , 
    "Belize" : { "label": "بليز", "Q": "Q242" ,"cat": "Robotskapade_Belizeartiklar" } , 
    "Benin" : { "label": "بنين", "Q": "Q962" ,"cat": "Robotskapade_Beninartiklar" } , 
    "Bermuda" : { "label": "برمودا", "Q": "Q23635" ,"cat": "Robotskapade_Bermudaartiklar" } , 
    "Bhutan" : { "label": "بوتان", "Q": "Q917" ,"cat": "Robotskapade_Bhutanartiklar" } , 
    "Bolivia" : { "label": "بوليفيا", "Q": "Q750" ,"cat": "Robotskapade_Boliviaartiklar" } , 
    "Bosnien och Hercegovina" : { "label": "البوسنة والهرسك", "Q": "Q225" ,"cat": "Robotskapade_Bosnien_och_Hercegovinaartiklar" } , 
    "Botswana" : { "label": "بوتسوانا", "Q": "Q963" ,"cat": "Robotskapade_Botswanaartiklar" } , 
    "Brasilien" : { "label": "البرازيل", "Q": "Q155" ,"cat": "Robotskapade_Brasilienartiklar" } , 
    "Brunei" : { "label": "بروناي", "Q": "Q921" ,"cat": "Robotskapade_Bruneiartiklar" } , 
    "Bulgarien" : { "label": "بلغاريا", "Q": "Q219" ,"cat": "Robotskapade_Bulgarienartiklar" } , 
    "Burkina Faso" : { "label": "بوركينا فاسو", "Q": "Q965" ,"cat": "Robotskapade_Burkina_Fasoartiklar" } , 
    "Burma" : { "label": "ميانمار", "Q": "Q836" ,"cat": "Robotskapade_Burmaartiklar" } , 
    "Burundi" : { "label": "بوروندي", "Q": "Q967" ,"cat": "Robotskapade_Burundiartiklar" } , 
    "Caymanöarna" : { "label": "جزر كايمان", "Q": "Q5785" ,"cat": "Robotskapade_Caymanöarnaartiklar" } , 
    "Centralafrikanska republiken" : { "label": "جمهورية أفريقيا الوسطى", "Q": "Q929" ,"cat": "Robotskapade_Centralafrikanska_republikenartiklar" } , 
    "Chile" : { "label": "تشيلي", "Q": "Q298" ,"cat": "Robotskapade_Chileartiklar" } , 
    "Colombia" : { "label": "كولومبيا", "Q": "Q739" ,"cat": "Robotskapade_Colombiaartiklar" } , 
    "Cooköarna" : { "label": "جزر كوك", "Q": "Q26988" ,"cat": "Robotskapade_Cooköarnaartiklar" } , 
    "Costa Rica" : { "label": "كوستاريكا", "Q": "Q800" ,"cat": "Robotskapade_Costa_Ricaartiklar" } , 
    "Cypern" : { "label": "قبرص", "Q": "Q229" ,"cat": "Robotskapade_Cypernartiklar" } , 
    "Danmark" : { "label": "الدنمارك", "Q": "Q35" ,"cat": "Robotskapade_Danmarkartiklar" } , 
    "Djibouti" : { "label": "جيبوتي", "Q": "Q977" ,"cat": "Robotskapade_Djiboutiartiklar" } , 
    "Dominica" : { "label": "دومينيكا", "Q": "Q784" ,"cat": "Robotskapade_Dominicaartiklar" } , 
    "Dominikanska republiken" : { "label": "جمهورية الدومينيكان", "Q": "Q786" ,"cat": "Robotskapade_Dominikanska_republikenartiklar" } , 
    "Ecuador" : { "label": "الإكوادور", "Q": "Q736" ,"cat": "Robotskapade_Ecuadorartiklar" } , 
    "Egypten" : { "label": "مصر", "Q": "Q79" ,"cat": "Robotskapade_Egyptenartiklar" } , 
    "Ekvatorialguinea" : { "label": "غينيا الاستوائية", "Q": "Q983" ,"cat": "Robotskapade_Ekvatorialguineaartiklar" } , 
    "Elfenbenskusten" : { "label": "ساحل العاج", "Q": "Q1008" ,"cat": "Robotskapade_Elfenbenskustenartiklar" } , 
    "Eritrea" : { "label": "إريتريا", "Q": "Q986" ,"cat": "Robotskapade_Eritreaartiklar" } , 
    "Estland" : { "label": "إستونيا", "Q": "Q191" ,"cat": "Robotskapade_Estlandartiklar" } , 
    "Etiopien" : { "label": "إثيوبيا", "Q": "Q115" ,"cat": "Robotskapade_Etiopienartiklar" } , 
    "Falklandsöarna" : { "label": "جزر فوكلاند", "Q": "Q9648" ,"cat": "Robotskapade_Falklandsöarnaartiklar" } , 
    "Fiji" : { "label": "فيجي", "Q": "Q712" ,"cat": "Robotskapade_Fijiartiklar" } , 
    "Filippinerna" : { "label": "الفلبين", "Q": "Q928" ,"cat": "Robotskapade_Filippinernaartiklar" } , 
    "Finland" : { "label": "فنلندا", "Q": "Q33" ,"cat": "Robotskapade_Finlandartiklar" } , 
    "Franska Guyana" : { "label": "غويانا الفرنسية", "Q": "Q3769" ,"cat": "Robotskapade_Franska_Guyanaartiklar" } , 
    "Färöarna" : { "label": "جزر فارو", "Q": "Q4628" ,"cat": "Robotskapade_Färöarnaartiklar" } , 
    "Förenade Arabemiraten" : { "label": "الإمارات العربية المتحدة", "Q": "Q878" ,"cat": "Robotskapade_Förenade_Arabemiratenartiklar" } , 
    "Gabon" : { "label": "الغابون", "Q": "Q1000" ,"cat": "Robotskapade_Gabonartiklar" } , 
    "Gambia" : { "label": "غامبيا", "Q": "Q1005" ,"cat": "Robotskapade_Gambiaartiklar" } , 
    "Georgien" : { "label": "جورجيا", "Q": "Q230" ,"cat": "Robotskapade_Georgienartiklar" } , 
    "Ghana" : { "label": "غانا", "Q": "Q117" ,"cat": "Robotskapade_Ghanaartiklar" } , 
    "Grekland" : { "label": "اليونان", "Q": "Q41" ,"cat": "Robotskapade_Greklandartiklar" } , 
    "Grenada" : { "label": "غرينادا", "Q": "Q769" ,"cat": "Robotskapade_Grenadaartiklar" } , 
    "Grönland" : { "label": "جرينلاند", "Q": "Q223" ,"cat": "Robotskapade_Grönlandartiklar" } , 
    "Guadeloupe" : { "label": "غوادلوب", "Q": "Q17012" ,"cat": "Robotskapade_Guadeloupeartiklar" } , 
    "Guam" : { "label": "غوام", "Q": "Q16635" ,"cat": "Robotskapade_Guamartiklar" } , 
    "Guatemala" : { "label": "غواتيمالا", "Q": "Q774" ,"cat": "Robotskapade_Guatemalaartiklar" } , 
    "Guernsey" : { "label": "غيرنزي", "Q": "Q25230" ,"cat": "Robotskapade_Guernseyartiklar" } , 
    "Guinea" : { "label": "غينيا", "Q": "Q1006" ,"cat": "Robotskapade_Guineaartiklar" } , 
    "Guinea-Bissau" : { "label": "غينيا بيساو", "Q": "Q1007" ,"cat": "Robotskapade_Guinea-Bissauartiklar" } , 
    "Guyana" : { "label": "غيانا", "Q": "Q734" ,"cat": "Robotskapade_Guyanaartiklar" } , 
    "Haiti" : { "label": "هايتي", "Q": "Q790" ,"cat": "Robotskapade_Haitiartiklar" } , 
    "Honduras" : { "label": "هندوراس", "Q": "Q783" ,"cat": "Robotskapade_Hondurasartiklar" } , 
    "Hongkong" : { "label": "هونغ كونغ", "Q": "Q8646" ,"cat": "Robotskapade_Hongkongartiklar" } , 
    "Indien" : { "label": "الهند", "Q": "Q668" ,"cat": "Robotskapade_Indienartiklar" } , 
    "Indonesien" : { "label": "إندونيسيا", "Q": "Q252" ,"cat": "Robotskapade_Indonesienartiklar" } , 
    "Irak" : { "label": "العراق", "Q": "Q796" ,"cat": "Robotskapade_Irakartiklar" } , 
    "Iran" : { "label": "إيران", "Q": "Q794" ,"cat": "Robotskapade_Iranartiklar" } , 
    "Irland" : { "label": "جمهورية أيرلندا", "Q": "Q27" ,"cat": "Robotskapade_Irlandartiklar" } , 
    "Island" : { "label": "آيسلندا", "Q": "Q189" ,"cat": "Robotskapade_Islandartiklar" } , 
    "Israel" : { "label": "إسرائيل", "Q": "Q801" ,"cat": "Robotskapade_Israelartiklar" } , 
    "Jamaica" : { "label": "جامايكا", "Q": "Q766" ,"cat": "Robotskapade_Jamaicaartiklar" } , 
    "Jersey" : { "label": "جيرزي", "Q": "Q785" ,"cat": "Robotskapade_Jerseyartiklar" } , 
    "Jordanien" : { "label": "الأردن", "Q": "Q810" ,"cat": "Robotskapade_Jordanienartiklar" } , 
    "Kambodja" : { "label": "كمبوديا", "Q": "Q424" ,"cat": "Robotskapade_Kambodjaartiklar" } , 
    "Kamerun" : { "label": "الكاميرون", "Q": "Q1009" ,"cat": "Robotskapade_Kamerunartiklar" } , 
    "Kanada" : { "label": "كندا", "Q": "Q16" ,"cat": "Robotskapade_Kanadaartiklar" } , 
    "Kap Verde" : { "label": "الرأس الأخضر", "Q": "Q1011" ,"cat": "Robotskapade_Kap_Verdeartiklar" } , 
    "Karibiska Nederländerna" : { "label": "الجزر الكاريبية الهولندية", "Q": "Q55" ,"cat": "Robotskapade_Karibiska_Nederländernaartiklar" } , 
    "Kazakstan" : { "label": "كازاخستان", "Q": "Q232" ,"cat": "Robotskapade_Kazakstanartiklar" } , 
    "Kenya" : { "label": "كينيا", "Q": "Q114" ,"cat": "Robotskapade_Kenyaartiklar" } , 
    "Kina" : { "label": "الصين", "Q": "Q148" ,"cat": "Robotskapade_Kinaartiklar" } , 
    "Kirgizistan" : { "label": "قيرغيزستان", "Q": "Q813" ,"cat": "Robotskapade_Kirgizistanartiklar" } , 
    "Kiribati" : { "label": "كيريباتي", "Q": "Q710" ,"cat": "Robotskapade_Kiribatiartiklar" } , 
    "Kokosöarna" : { "label": "جزر كوكوس", "Q": "Q36004" ,"cat": "Robotskapade_Kokosöarnaartiklar" } , 
    "Komorerna" : { "label": "جزر القمر", "Q": "Q970" ,"cat": "Robotskapade_Komorernaartiklar" } , 
    "Kongo-Brazzaville" : { "label": "جمهورية الكونغو", "Q": "Q971" ,"cat": "Robotskapade_Kongo-Brazzavilleartiklar" } , 
    "Kongo-Kinshasa" : { "label": "جمهورية الكونغو الديمقراطية", "Q": "Q974" ,"cat": "Robotskapade_Kongo-Kinshasaartiklar" } , 
    "Kosovo" : { "label": "كوسوفو", "Q": "Q1246" ,"cat": "Robotskapade_Kosovoartiklar" } , 
    "Kroatien" : { "label": "كرواتيا", "Q": "Q224" ,"cat": "Robotskapade_Kroatienartiklar" } , 
    "Kuba" : { "label": "كوبا", "Q": "Q241" ,"cat": "Robotskapade_Kubaartiklar" } , 
    "Kuwait" : { "label": "الكويت", "Q": "Q817" ,"cat": "Robotskapade_Kuwaitartiklar" } , 
    "Laos" : { "label": "لاوس", "Q": "Q819" ,"cat": "Robotskapade_Laosartiklar" } , 
    "Lesotho" : { "label": "ليسوتو", "Q": "Q1013" ,"cat": "Robotskapade_Lesothoartiklar" } , 
    "Lettland" : { "label": "لاتفيا", "Q": "Q211" ,"cat": "Robotskapade_Lettlandartiklar" } , 
    "Libanon" : { "label": "لبنان", "Q": "Q822" ,"cat": "Robotskapade_Libanonartiklar" } , 
    "Liberia" : { "label": "ليبيريا", "Q": "Q1014" ,"cat": "Robotskapade_Liberiaartiklar" } , 
    "Libyen" : { "label": "ليبيا", "Q": "Q1016" ,"cat": "Robotskapade_Libyenartiklar" } , 
    "Litauen" : { "label": "ليتوانيا", "Q": "Q37" ,"cat": "Robotskapade_Litauenartiklar" } , 
    "Luxemburg" : { "label": "لوكسمبورغ", "Q": "Q32" ,"cat": "Robotskapade_Luxemburgartiklar" } , 
    "Madagaskar" : { "label": "مدغشقر", "Q": "Q1019" ,"cat": "Robotskapade_Madagaskarartiklar" } , 
    "Makedonien" : { "label": "جمهورية مقدونيا", "Q": "Q221" ,"cat": "Robotskapade_Makedonienartiklar" } , 
    "Malawi" : { "label": "ملاوي", "Q": "Q1020" ,"cat": "Robotskapade_Malawiartiklar" } , 
    "Maldiverna" : { "label": "جزر المالديف", "Q": "Q826" ,"cat": "Robotskapade_Maldivernaartiklar" } , 
    "Mali" : { "label": "مالي", "Q": "Q912" ,"cat": "Robotskapade_Maliartiklar" } , 
    "Malta" : { "label": "مالطا", "Q": "Q233" ,"cat": "Robotskapade_Maltaartiklar" } , 
    "Marocko" : { "label": "المغرب", "Q": "Q1028" ,"cat": "Robotskapade_Marockoartiklar" } , 
    "Marshallöarna" : { "label": "جزر مارشال", "Q": "Q709" ,"cat": "Robotskapade_Marshallöarnaartiklar" } , 
    "Mauretanien" : { "label": "موريتانيا", "Q": "Q1025" ,"cat": "Robotskapade_Mauretanienartiklar" } , 
    "Mauritius" : { "label": "موريشيوس", "Q": "Q1027" ,"cat": "Robotskapade_Mauritiusartiklar" } , 
    "Mexiko" : { "label": "المكسيك", "Q": "Q96" ,"cat": "Robotskapade_Mexikoartiklar" } , 
    "Mikronesiens federerade stater" : { "label": "ولايات ميكرونيسيا المتحدة", "Q": "Q702" ,"cat": "Robotskapade_Mikronesiens_federerade_staterartiklar" } , 
    "Moldavien" : { "label": "مولدافيا", "Q": "Q217" ,"cat": "Robotskapade_Moldavienartiklar" } , 
    "Mongoliet" : { "label": "منغوليا", "Q": "Q711" ,"cat": "Robotskapade_Mongolietartiklar" } , 
    "Montenegro" : { "label": "الجبل الأسود", "Q": "Q236" ,"cat": "Robotskapade_Montenegroartiklar" } , 
    "Montserrat" : { "label": "مونتسرات", "Q": "Q13353" ,"cat": "Robotskapade_Montserratartiklar" } , 
    "Nicaragua" : { "label": "نيكاراغوا", "Q": "Q811" ,"cat": "Robotskapade_Nicaraguaartiklar" } , 
    "Nordkorea" : { "label": "كوريا الشمالية", "Q": "Q423" ,"cat": "Robotskapade_Nordkoreaartiklar" } , 
    "Nordmarianerna" : { "label": "جزر ماريانا الشمالية", "Q": "Q16644" ,"cat": "Robotskapade_Nordmarianernaartiklar" } , 
    "Saint Lucia" : { "label": "سانت لوسيا", "Q": "Q760" ,"cat": "Robotskapade_Saint_Luciaartiklar" } , 
    "Schweiz" : { "label": "سويسرا", "Q": "Q39" ,"cat": "Robotskapade_Schweizartiklar" } , 
    "Spanien" : { "label": "إسبانيا", "Q": "Q29" ,"cat": "Robotskapade_Spanienartiklar" } , 
    "Sri Lanka" : { "label": "سريلانكا", "Q": "Q854" ,"cat": "Robotskapade_Sri_Lankaartiklar" } , 
    "Storbritannien" : { "label": "المملكة المتحدة", "Q": "Q145" ,"cat": "Robotskapade_Storbritannienartiklar" } , 
    "Sydgeorgien och Sydsandwichöarna" : { "label": "جورجيا الجنوبية وجزر ساندويتش الجنوبية", "Q": "Q35086" ,"cat": "Robotskapade_Sydgeorgien_och_Sydsandwichöarnaartiklar" } , 
    "Sydkorea" : { "label": "كوريا الجنوبية", "Q": "Q884" ,"cat": "Robotskapade_Sydkoreaartiklar" } , 
    "Sydsudan" : { "label": "جنوب السودان", "Q": "Q958" ,"cat": "Robotskapade_Sydsudanartiklar" } , 
    "Syrien" : { "label": "سوريا", "Q": "Q858" ,"cat": "Robotskapade_Syrienartiklar" } , 
    "Tjeckien" : { "label": "التشيك", "Q": "Q213" ,"cat": "Robotskapade_Tjeckienartiklar" } , 
    "Ungern" : { "label": "المجر", "Q": "Q28" ,"cat": "Robotskapade_Ungernartiklar" } , 
    "Vitryssland" : { "label": "روسيا البيضاء", "Q": "Q184" ,"cat": "Robotskapade_Vitrysslandartiklar" } , 
    "Västsahara" : { "label": "الصحراء الغربية", "Q": "Q6250" ,"cat": "Robotskapade_Västsaharaartiklar" } , 
    "Åland" : { "label": "جزر أولاند", "Q": "Q33" ,"cat": "Robotskapade_Ålandartiklar" } , 
    "Österrike" : { "label": "النمسا", "Q": "Q40" ,"cat": "Robotskapade_Österrikeartiklar" } , 
    }
cattt = {
    'Kapupud-ang_Solomon' : { 'label': 'جزر سليمان', 'Q': 'Q685'} , 
    'Svalbard_and_Jan_Mayen' : { 'label': 'سفالبارد ويان ماين', 'Q': 'Q20'} , 
    'Swisa' : { 'label': 'سويسرا', 'Q': 'Q39'} , 
    'Tailandya' : { 'label': 'تايلاند', 'Q': 'Q869'} , 
    'Tanzania' : { 'label': 'تنزانيا', 'Q': 'Q924'} , 
    'Tayikistan' : { 'label': 'طاجيكستان', 'Q': 'Q863'} , 
    'Togo' : { 'label': 'توغو', 'Q': 'Q945'} , 
    'Tonga' : { 'label': 'تونغا', 'Q': 'Q678'} , 
    'Trinidad_ug_Tobago' : { 'label': 'ترينيداد وتوباغو', 'Q': 'Q754'} , 
    'Tsekya' : { 'label': 'التشيك', 'Q': 'Q213'} , 
    'Tsipre' : { 'label': 'قبرص', 'Q': 'Q229'} , 
    'Tunisia' : { 'label': 'تونس', 'Q': 'Q948'} , 
    'Turkiya' : { 'label': 'تركيا', 'Q': 'Q43'} , 
    'Ireland' : { 'label': 'أيرلندا', 'Q': 'Q27'} , 
    'Turkmenistan' : { 'label': 'تركمانستان', 'Q': 'Q874'} , 
    'Turks_and_Caicos_Islands' : { 'label': 'جزر توركس وكايكوس', 'Q': 'Q145'} ,# Q18221
    'U.S._Virgin_Islands' : { 'label': 'جزر العذراء الأمريكية', 'Q': 'Q30'} , #Q11703
    'Uganda' : { 'label': 'أوغندا', 'Q': 'Q1036'} , 
    'Ukranya' : { 'label': 'أوكرانيا', 'Q': 'Q212'} , 
    'Unggriya' : { 'label': 'المجر', 'Q': 'Q28'} , 
    'United_States_Minor_Outlying_Islands' : { 'label': 'جزر الولايات المتحدة الصغيرة النائية', 'Q': 'Q30'} , #Q16645
    'Uruguay' : { 'label': 'الأوروغواي', 'Q': 'Q77'} , 
    'Uzbekistan' : { 'label': 'أوزبكستان', 'Q': 'Q265'} , 
    'Vanuatu' : { 'label': 'فانواتو', 'Q': 'Q686'} , 
    'Venezuela' : { 'label': 'فنزويلا', 'Q': 'Q717'} , 
    'Wallis_and_Futuna' : { 'label': 'واليس وفوتونا', 'Q': 'Q35555'} , 
    #'Western_Sahara' : { 'label': 'الصحراء الغربية', 'Q': 'Q6250'} , 
    'Yemen' : { 'label': 'اليمن', 'Q': 'Q805'} , 
    'Yibuti' : { 'label': 'جيبوتي', 'Q': 'Q977'} , 
    'Zambia' : { 'label': 'زامبيا', 'Q': 'Q953'} , 
    'Zimbabwe' : { 'label': 'زيمبابوي', 'Q': 'Q954'} , 
    'Aland_Islands' : { 'label': 'جزر أولاند', 'Q': 'Q33'} , #Q33#Q5689
    'Albanya' : { 'label': 'ألبانيا', 'Q': 'Q222'} , 
    'Alemanya' : { 'label': 'ألمانيا', 'Q': 'Q183'} , 
    'American_Samoa' : { 'label': 'ساموا الأمريكية', 'Q': 'Q30'} , #Q16641
    'Amihanang_Korea' : { 'label': 'كوريا الشمالية', 'Q': 'Q423'} , 
    'Andorra' : { 'label': 'أندورا', 'Q': 'Q228'} , 
    'Angola' : { 'label': 'أنغولا', 'Q': 'Q916'} , 
    'Anguilla' : { 'label': 'أنغويلا', 'Q': 'Q25228'} , 
    #'Antarctica' : { 'label': 'القارة القطبية الجنوبية', 'Q': 'Q51'} , 
    'Antigua_ug_Barbuda' : { 'label': 'أنتيغوا وباربودا', 'Q': 'Q781'} , 
    'Apganistan' : { 'label': 'أفغانستان', 'Q': 'Q889'} , 
    'Arabyang_Saudita' : { 'label': 'السعودية', 'Q': 'Q851'} , 
    'Arhelya' : { 'label': 'الجزائر', 'Q': 'Q262'} , 
    'Arhentina' : { 'label': 'الأرجنتين', 'Q': 'Q414'} , 
    'Armenya' : { 'label': 'أرمينيا', 'Q': 'Q399'} , 
    'Aruba' : { 'label': 'أروبا', 'Q': 'Q21203'} , 
    'Aserbaiyan' : { 'label': 'أذربيجان', 'Q': 'Q227'} , 
    'Awstralya' : { 'label': 'أستراليا', 'Q': 'Q408'} , 
    'Awstriya' : { 'label': 'النمسا', 'Q': 'Q40'} , 
    'Bahamas' : { 'label': 'باهاماس', 'Q': 'Q778'} , 
    'Cabo_Verde' : { 'label': 'الرأس الأخضر', 'Q': 'Q1011'} , 
    'Canada' : { 'label': 'كندا', 'Q': 'Q16'} , 
    'Cayman_Islands' : { 'label': 'جزر كايمان', 'Q': 'Q145'} , 
    'Chad' : { 'label': 'تشاد', 'Q': 'Q657'} , 
    'Chile' : { 'label': 'تشيلي', 'Q': 'Q298'} , 
    'Christmas_Island' : { 'label': 'جزيرة عيد الميلاد', 'Q': 'Q408'} , 
    'Colombia' : { 'label': 'كولومبيا', 'Q': 'Q739'} , 
    'Comoros' : { 'label': 'جزر القمر', 'Q': 'Q970'} , 
    'Cook_Islands' : { 'label': 'جزر كوك', 'Q': 'Q664'} , 
    'Costa_Rica' : { 'label': 'كوستاريكا', 'Q': 'Q800'} , 
    'Cuba' : { 'label': 'كوبا', 'Q': 'Q241'} , 
    'Curaçao' : { 'label': 'كوراساو', 'Q': 'Q25279'} , 
    'Dinamarka' : { 'label': 'الدنمارك', 'Q': 'Q35'} , 
    'Dominica' : { 'label': 'دومينيكا', 'Q': 'Q784'} , 
    'Ecuador' : { 'label': 'الإكوادور', 'Q': 'Q736'} , 
    'Ehipto' : { 'label': 'مصر', 'Q': 'Q79'} , 
    'El_Salvador' : { 'label': 'السلفادور', 'Q': 'Q792'} , 
    'Eritrea' : { 'label': 'إريتريا', 'Q': 'Q986'} , 
    'Eslobakya' : { 'label': 'سلوفاكيا', 'Q': 'Q214'} , 
    'Eslobenya' : { 'label': 'سلوفينيا', 'Q': 'Q215'} , 
    'Espanya' : { 'label': 'إسبانيا', 'Q': 'Q29'} , 
    'Estados_Unidos' : { 'label': 'الولايات المتحدة', 'Q': 'Q30'} , 
    'Estonia' : { 'label': 'إستونيا', 'Q': 'Q191'} , 
    'Etiopia' : { 'label': 'إثيوبيا', 'Q': 'Q115'} , 
    'Fiji' : { 'label': 'فيجي', 'Q': 'Q712'} , 
    'Finlandia' : { 'label': 'فنلندا', 'Q': 'Q33'} , 
    'French_Polynesia' : { 'label': 'بولينزيا الفرنسية', 'Q': 'Q142'} , 
    'French_Southern_Territories' : { 'label': 'أراض فرنسية جنوبية وأنتارتيكية', 'Q': 'Q142'} , 
    'Gabon' : { 'label': 'الغابون', 'Q': 'Q1000'} , 
    'Gambia' : { 'label': 'غامبيا', 'Q': 'Q1005'} , 
    'Georgia_(nasod)' : { 'label': 'جورجيا', 'Q': 'Q230'} , 
    'Ghana' : { 'label': 'غانا', 'Q': 'Q117'} , 
    'Gibraltar' : { 'label': 'جبل طارق', 'Q': 'Q1410'} , 
    'Gineang_Ekwatoryal' : { 'label': 'غينيا الاستوائية', 'Q': 'Q983'} , 
    'Greenland' : { 'label': 'جرينلاند', 'Q': 'Q223'} , 
    'Grenada' : { 'label': 'غرينادا', 'Q': 'Q769'} , 
    'Gresya' : { 'label': 'اليونان', 'Q': 'Q41'} , 
    'Guadeloupe' : { 'label': 'غوادلوب', 'Q': 'Q142'} , 
    'Guam' : { 'label': 'غوام', 'Q': 'Q30'} , 
    'Guatemala' : { 'label': 'غواتيمالا', 'Q': 'Q774'} , 
    'Guernsey' : { 'label': 'غيرنزي', 'Q': 'Q25230'} , 
    'Guinea' : { 'label': 'غينيا', 'Q': 'Q1006'} , 
    'Guinea-Bissau' : { 'label': 'غينيا بيساو', 'Q': 'Q1007'} , 
    'Guyana' : { 'label': 'غيانا', 'Q': 'Q734'} , 
    'Bangladesh' : { 'label': 'بنغلاديش', 'Q': 'Q902'} , 
    'Barbados' : { 'label': 'باربادوس', 'Q': 'Q244'} , 
    'Bareyn' : { 'label': 'البحرين', 'Q': 'Q398'} , 
    'Baybayon_sa_Marpil' : { 'label': 'ساحل العاج', 'Q': 'Q1008'} , 
    'Belhika' : { 'label': 'بلجيكا', 'Q': 'Q31'} , 
    'Belize' : { 'label': 'بليز', 'Q': 'Q242'} , 
    'Benin' : { 'label': 'بنين', 'Q': 'Q962'} , 
    'Bermuda' : { 'label': 'برمودا', 'Q': 'Q23635'} , 
    'Bhutan' : { 'label': 'بوتان', 'Q': 'Q917'} , 
    'Biyelorusya' : { 'label': 'روسيا البيضاء', 'Q': 'Q184'} , 
    'Biyetnam' : { 'label': 'فيتنام', 'Q': 'Q881'} , 
    'Bolivia' : { 'label': 'بوليفيا', 'Q': 'Q750'} , 
    'Bonaire,_Saint_Eustatius_and_Saba' : { 'label': 'الجزر الكاريبية الهولندية', 'Q': 'Q55'} , #Q27561
    'Bosnia_ug_Herzegovina' : { 'label': 'البوسنة والهرسك', 'Q': 'Q225'} , 
    'Botswana' : { 'label': 'بوتسوانا', 'Q': 'Q963'} , 
    'Bouvet_Island' : { 'label': 'جزيرة بوفيه', 'Q': 'Q20'} , #Q23408
    'Brasil' : { 'label': 'البرازيل', 'Q': 'Q155'} , 
    'British_Indian_Ocean_Territory' : { 'label': 'إقليم المحيط الهندي البريطاني', 'Q': 'Q145'} , #Q43448
    'British_Virgin_Islands' : { 'label': 'جزر العذراء البريطانية', 'Q': 'Q145'} , #Q25305
    'Brunei' : { 'label': 'بروناي', 'Q': 'Q921'} , 
    'Bulgaria' : { 'label': 'بلغاريا', 'Q': 'Q219'} , 
    'Burkina_Faso' : { 'label': 'بوركينا فاسو', 'Q': 'Q965'} , 
    'Burma' : { 'label': 'ميانمار', 'Q': 'Q836'} , 
    'Burundi' : { 'label': 'بوروندي', 'Q': 'Q967'} , 
    'Mayotte' : { 'label': 'مايوت', 'Q': 'Q142'} , 
    'Mehiko' : { 'label': 'المكسيك', 'Q': 'Q96'} , 
    'Moldabya' : { 'label': 'مولدافيا', 'Q': 'Q217'} , 
    'Monako' : { 'label': 'موناكو', 'Q': 'Q235'} , 
    'Mongolia' : { 'label': 'منغوليا', 'Q': 'Q711'} , 
    'Montenegro' : { 'label': 'الجبل الأسود', 'Q': 'Q236'} , 
    'Montserrat' : { 'label': 'مونتسرات', 'Q': 'Q13353'} , 
    'Mozambique' : { 'label': 'موزمبيق', 'Q': 'Q1029'} , 
    'Namibya' : { 'label': 'ناميبيا', 'Q': 'Q1030'} , 
    'Nauru' : { 'label': 'ناورو', 'Q': 'Q697'} , 
    'Nepal' : { 'label': 'نيبال', 'Q': 'Q837'} , 
    'New_Zealand' : { 'label': 'نيوزيلندا', 'Q': 'Q664'} , 
    'Nicaragua' : { 'label': 'نيكاراغوا', 'Q': 'Q811'} , 
    'Niger' : { 'label': 'النيجر', 'Q': 'Q1032'} , 
    'Nigeria' : { 'label': 'نيجيريا', 'Q': 'Q1033'} , 
    'Noruwega' : { 'label': 'النرويج', 'Q': 'Q20'} , 
    'Olanda' : { 'label': 'هولندا', 'Q': 'Q55'} , 
    'Oman' : { 'label': 'سلطنة عمان', 'Q': 'Q842'} , 
    'Pakistan' : { 'label': 'باكستان', 'Q': 'Q843'} , 
    'Palau' : { 'label': 'بالاو', 'Q': 'Q695'} , 
    'Panama' : { 'label': 'بنما', 'Q': 'Q804'} , 
    'Paraguay' : { 'label': 'باراغواي', 'Q': 'Q733'} , 
    'Peru' : { 'label': 'بيرو', 'Q': 'Q419'} , 
    'Pilipinas' : { 'label': 'الفلبين', 'Q': 'Q928'} , 
    'Polonya' : { 'label': 'بولندا', 'Q': 'Q36'} , 
    'Portugal' : { 'label': 'البرتغال', 'Q': 'Q45'} , 
    'Pransiya' : { 'label': 'فرنسا', 'Q': 'Q142'} , 
    'Republika_sa_Congo' : { 'label': 'جمهورية الكونغو', 'Q': 'Q971'} , 
    'Republika_sa_Tsina' : { 'label': 'تايوان', 'Q': 'Q865'} , 
    'Republikang_Demokratiko_sa_Congo' : { 'label': 'جمهورية الكونغو الديمقراطية', 'Q': 'Q974'} , 
    'Republikang_Dominikano' : { 'label': 'جمهورية الدومينيكان', 'Q': 'Q786'} , 
    'Republikang_Popular_sa_Tsina' : { 'label': 'الصين', 'Q': 'Q148'} , 
    'Republikang_Sentral_Aprikano' : { 'label': 'جمهورية أفريقيا الوسطى', 'Q': 'Q929'} , 
    'Rumanya' : { 'label': 'رومانيا', 'Q': 'Q218'} , 
    'Rusya' : { 'label': 'روسيا', 'Q': 'Q159'} , 
    'Samoa' : { 'label': 'ساموا', 'Q': 'Q683'} , 
    'Senegal' : { 'label': 'السنغال', 'Q': 'Q1041'} , 
    'Serbya' : { 'label': 'صربيا', 'Q': 'Q403'} , 
    'Seychelles' : { 'label': 'سيشل', 'Q': 'Q1042'} , 
    'Sidlakang_Timor' : { 'label': 'تيمور الشرقية', 'Q': 'Q574'} , 
    'Sierra_Leone' : { 'label': 'سيراليون', 'Q': 'Q1044'} , 
    'Singgapura' : { 'label': 'سنغافورة', 'Q': 'Q334'} , 
    'Sint_Maarten' : { 'label': 'سينت مارتن', 'Q': 'Q26273'} , 
    'Siria' : { 'label': 'سوريا', 'Q': 'Q858'} , 
    'Somalia' : { 'label': 'الصومال', 'Q': 'Q1045'} , 
    'Sri_Lanka' : { 'label': 'سريلانكا', 'Q': 'Q854'} , 
    'Sudan' : { 'label': 'السودان', 'Q': 'Q1049'} , 
    'Surinam' : { 'label': 'سورينام', 'Q': 'Q730'} , 
    'Suwasilandiya' : { 'label': 'سوازيلاند', 'Q': 'Q1050'} , 
    'Suwesya' : { 'label': 'السويد', 'Q': 'Q34'} , 
    'Habagatang_Aprika' : { 'label': 'جنوب أفريقيا', 'Q': 'Q258'} , 
    'Habagatang_Korea' : { 'label': 'كوريا الجنوبية', 'Q': 'Q884'} , 
    'Habagatang_Sudan' : { 'label': 'جنوب السودان', 'Q': 'Q958'} , 
    'Haiti' : { 'label': 'هايتي', 'Q': 'Q790'} , 
    'Hapon' : { 'label': 'اليابان', 'Q': 'Q17'} , 
    'Hiniusang_Emiratong_Arabo' : { 'label': 'الإمارات العربية المتحدة', 'Q': 'Q878'} , 
    'Hiniusang_Gingharian' : { 'label': 'المملكة المتحدة', 'Q': 'Q145'} , 
    'Honduras' : { 'label': 'هندوراس', 'Q': 'Q783'} , 
    'Hordanya' : { 'label': 'الأردن', 'Q': 'Q810'} , 
    'Indonesia' : { 'label': 'إندونيسيا', 'Q': 'Q252'} , 
    'Indya' : { 'label': 'الهند', 'Q': 'Q668'} , 
    'Iran' : { 'label': 'إيران', 'Q': 'Q794'} , 
    'Iraq' : { 'label': 'العراق', 'Q': 'Q796'} , 
    'Islandya' : { 'label': 'آيسلندا', 'Q': 'Q189'} , 
    'Litwanya' : { 'label': 'ليتوانيا', 'Q': 'Q37'} , 
    'Luksemburgo' : { 'label': 'لوكسمبورغ', 'Q': 'Q32'} , 
    'Macao' : { 'label': 'ماكاو', 'Q': 'Q14773'} , 
    'Macedonia' : { 'label': 'جمهورية مقدونيا', 'Q': 'Q221'} , 
    'Madagascar' : { 'label': 'مدغشقر', 'Q': 'Q1019'} , 
    'Malasya' : { 'label': 'ماليزيا', 'Q': 'Q833'} , 
    'Malawi' : { 'label': 'ملاوي', 'Q': 'Q1020'} , 
    'Mali' : { 'label': 'مالي', 'Q': 'Q912'} , 
    'Malta' : { 'label': 'مالطا', 'Q': 'Q233'} , 
    'Maruwekos' : { 'label': 'المغرب', 'Q': 'Q1028'} , 
    'Maurisyo' : { 'label': 'موريشيوس', 'Q': 'Q1027'} , 
    'Mauritania' : { 'label': 'موريتانيا', 'Q': 'Q1025'} , 
    'Israel' : { 'label': 'إسرائيل', 'Q': 'Q801'} , 
    'Italya' : { 'label': 'إيطاليا', 'Q': 'Q38'} , 
    'Jamaica' : { 'label': 'جامايكا', 'Q': 'Q766'} , 
    'Jersey' : { 'label': 'جيرزي', 'Q': 'Q785'} , 
    'Kamboya' : { 'label': 'كمبوديا', 'Q': 'Q424'} , 
    'Kamerun' : { 'label': 'الكاميرون', 'Q': 'Q1009'} , 
    'Kasahistan' : { 'label': 'كازاخستان', 'Q': 'Q232'} , 
    'Katar' : { 'label': 'قطر', 'Q': 'Q846'} , 
    'Kenya' : { 'label': 'كينيا', 'Q': 'Q114'} , 
    'Kirgistan' : { 'label': 'قيرغيزستان', 'Q': 'Q813'} , 
    'Kiribati' : { 'label': 'كيريباتي', 'Q': 'Q710'} , 
    'Kosobo' : { 'label': 'كوسوفو', 'Q': 'Q1246'} , 
    'Krowasya' : { 'label': 'كرواتيا', 'Q': 'Q224'} , 
    'Kuwait' : { 'label': 'الكويت', 'Q': 'Q817'} , 
    'Laos' : { 'label': 'لاوس', 'Q': 'Q819'} , 
    'Latvia' : { 'label': 'لاتفيا', 'Q': 'Q211'} , 
    'Lesotho' : { 'label': 'ليسوتو', 'Q': 'Q1013'} , 
    'Libano' : { 'label': 'لبنان', 'Q': 'Q822'} , 
    'Liberya' : { 'label': 'ليبيريا', 'Q': 'Q1014'} , 
    'Libya' : { 'label': 'ليبيا', 'Q': 'Q1016'} , 
    'Liechtenstein' : { 'label': 'ليختنشتاين', 'Q': 'Q347'} , 
    }
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
    #data22 = Fix_Data_New(data2)
    data22 = json.JSONEncoder().encode(data2)
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
    timesleep = 1
    if 'success' in text:
        pywikibot.output('<<lightgreen>> ** New_API2: %s true. "%s" time.sleep(%s)' % (q , summary , timesleep) )
        time.sleep(timesleep)
    elif 'maxlag' in text:
        pywikibot.output('<<lightred>> ** maxlag. time.sleep(3)')
        time.sleep(3)
    else:
        pywikibot.output(text)
#---
from categoryNew import CategoryTableNew

#---
def find_P17_templatee(page):
    #from ContriesNew import P17Table
    pagetitle = page.title(as_link=False)
    templatesWithParams = page.templatesWithParams()
    #paghimo ni bot
    for (template, params) in templatesWithParams:
            TargetTemp = template.title(withNamespace=False)
            #pywikibot.output(TargetTemp)
            #pywikibot.output("* found temp : " + TargetTemp)
            if (TargetTemp == 'paghimo ni bot') or (TargetTemp ==  'Paghimo ni bot') or (TargetTemp ==  'Robotskapad'):
                #pywikibot.output(params)
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
def AddClaims__2(ss , data, geonames ,p31code ,  page , Mysummary):
    #---
    #---
    #ss = findtext(geonames)
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
    CountryName = ''
    P17 = False
    if P31:
        #---
        P17_Q = find_P17_templatee(page)#
        if P17_Q:
            Q_P17 = P17_Q['Q']
            CountryName = P17_Q['label']
            P17 = makejson('P17', Q_P17)
            data["claims"]["P17"] = [P17]
            summary = summary + 'P17/'
        #---
        if P17 and P31:
            desc = False
            p31code = p31code#ss['fcl'] + '.' + ss['fcode']
            countryCode = P17
            if CountryName != '':
                    if p31code in list: #and ('ar' in CategoryTableNew[p31code]):
                        desc = list[p31code]["ar"] + ' في ' + CountryName
            #---
            if desc:
                data['descriptions'] = {}
                data['descriptions']['ar'] = {'language':'ar','value': desc}
                pywikibot.output('*ar descriptions: %s' % desc)
        #---
        if 'srtm3' in ss:
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
        #else:
            #pywikibot.output('* nothing to add..')
#---
def CreateNewItem(geonames, p31code , page):#vaul
        #pywikibot.output( '**<<lightyellow>> CreateNewItem:' )
        title = page.title(as_link=False)
        label = title.split('(')[0]
        #---
        # Create a new page, which is unlinked
        ss = {}#findtext(geonames)
        data = {}
        data['labels'] = {}
        data['labels']['sv'] = {'language': 'sv','value': label}
        data['labels']['en'] = {'language': 'en','value': label}
        data['sitelinks'] = {}
        data['sitelinks']['svwiki'] = {'site': 'svwiki','title': title }
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
        mySummary = ('Bot:New item from [[w:sv:%s|svwiki]]'  % page.title(as_link=False))
        AddClaims__2(ss , data , geonames, p31code ,  page , mySummary)
#---
def Claims_for_item(item , geonames ,p31code ,  page ):
    #---
    #data["claims"] = {}
    dataclaims = {}
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
    #summary = ''
    pagetitle = page.title(as_link=False)
    P31 = False
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
    if 'P1566' not in AlreadyThere:
        P1566 = MakeP1566(geonames)###
        if P1566:
            data["claims"]["P1566"] = [P1566]
            addclaims.append('P1566')
    #---
    #if summary != '':
    if addclaims :
        if P17_Q and p31code:
            if 'ar' not in item.descriptions:
                desc = False
                p31code = p31code#ss['fcl'] + '.' + ss['fcode']
                if CountryName != '':
                        if p31code in list: #and ('ar' in CategoryTableNew[p31code]):
                            desc = list[p31code]["ar"] + ' في ' + CountryName
                #---
                if desc:
                    data['descriptions'] = {}
                    data['descriptions']['ar'] = {'language':'ar','value': desc}
                    pywikibot.output('*ar descriptions: %s' % desc)
        #---
        cp = '/'.join(addclaims)
        summary = 'Bot: Add claims %s from [[w:sv:%s|svwiki]]' % (cp , page.title(as_link=False)  )
        #---
        #New_API2(data, summary)
        q = item.title(as_link=False)
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
    #---  
    #pywikibot.output("* no item: " )
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
        if P31[0] in CategoryTableNew:
            Notemp = True
            p31code = CategoryTableNew[P31[0]]['item']
            pywikibot.output("*found template: with " + str(geonames) )
            if geonames !='':
                if item:    
                    pywikibot.output("* found item: " + item.title() )
                    Claims_for_item(item , geonames ,p31code ,  page )
                else:
                    CreateNewItem(geonames, p31code , page)
            else:
                pywikibot.output("*don't found template: " + str(TargetTemplates) )
        else:
            logCategoryError(P31[0] , pagetitle)
#---        
def mainwithcat(*args):
    #args = {'-lang:sv' , '-page:Ojo_Caliente_(abang_nga_dapit)'}
    #if sys.argv:
        #if len(sys.argv) < 2 :
                #args = {'-lang:sv' , '-ns:0' , '-catr:Kategoriya:Articles_without_Wikidata_item'}
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
def mainwithcat2():
    if sys.argv and len(sys.argv) > 1 :
            mainwithcat(*sys.argv)
    else:
        for cat in P17Table:
            args = ['-lang:sv' , '-ns:0' , '-catr:Kategori:' + P17Table[cat]['cat'] ]
            pywikibot.output('*<<lightred>> ' + str(args))
            mainwithcat(*args)
#---
if __name__ == "__main__":
    
    mainwithcat2()
    #mainwithcat()
#---
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

محاولة ايجاد احداثيات لمقالات قرى وعزل والخ اليمن

python pwb.py findcoord/geojson

python pwb.py findcoord/geojson -catr:تصنيف:قرى_محافظة_إب

"""
#
# (C) Ibrahem Qasim, 2022
#
import codecs
from API.maindir import main_dir

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , "utf-8" )
#---
# 
import re
import time

import urllib
import urllib.request
import urllib.parse
import string
import json
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
#---
from API import himoBOT2
#---
# This is required for the text that is shown when you run this script
# with the parameter -help.


#---
from API import himoBOT
#---
def findtax(titl1value):
    titl1value = ''
    sa = 's'
    qua = 'SELECT ?item WHERE {?item wdt:P1566 "' + titl1value + '". } '#limit 1'
    json1 = himoBOT.wd_sparql_generator_url(qua)
    if json1:
      for item in json1: 
          sa = sa + ' ' + item.title(as_link=False)
    #if sa != '':
       # sa = '\t' + sa
    return sa

def log(item , Ttitle , coord ,fullname,  name , geonames , enwiki):
    #item = item.title(as_link=False)
    geonames = geonames + '\t' + findtax(geonames)
    so = '%s\t%s\t%s\t%s\t%s\t%s\t%s\t\n' % (Ttitle , item , 'P625\t' + coord   , name , geonames, enwiki , fullname)
    #pywikibot.output(so)
    with codecs.open("findcoord/geon.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(so)
      except :
            pywikibot.output("Error writing")
#---
from API import open_url
# open_url.getURL( url )
#---
def findtext(id , adminCode1):
    #---
    fao = urllib.parse.quote(id)
    #---
    #url = 'geonames.org/search.html?q=' + fao + '&country=YE'
    url = 'api.geonames.org/searchJSON?formatted=true&maxRows=3&username=ibrahemqasim&q=' + fao + '&lang=ar&country=YE&dminCode1=' + adminCode1
    #url = 'geonames.org/advanced-search.html?q=' + 'Tawahi' + '&country=YE'
    s = open_url.getURL(url= 'http://'+ url)
    s = json.loads(s)
    #pywikibot.output(s)
    pywikibot.output(url)
    #---
    fat = []
    #if 'geonames' in s:
    if s.get('geonames' , '') != '':
        for raw in s['geonames']:
            if raw['adminCode1'] == adminCode1:
                #pywikibot.output( '<<lightyellow>> raw:' )
                #pywikibot.output(raw)
                vaa = {}
                tab = {}
                soper = ["lng","geonameId","toponymName","fcl","name","fclName","fcodeName","lat","fcode"]
                for sop in soper:
                    if sop in raw:
                        vaa[sop] = str(raw[sop])
                fat.append(vaa)
    #pywikibot.output(fat)
    #---
    return fat
    
def findcoord(tr):
    longitude, latitude = '' , ''
    # coord
    tab = {'coord':''}
    #if 'lng' in tr:
    if tr.get('lng' , '') != '':
        longitude = tr['lng']
    #if 'lat' in tr:
    if tr.get('lat' , '') != '':
        latitude = tr['lat']
    if (longitude and longitude !='') and (latitude and latitude !=''):
        coord = '@' + longitude + '/' + latitude
        #pywikibot.output( '<<lightyellow>> coord:' )
        #pywikibot.output(coord)
        tab['coord'] = coord
    return tab['coord']
    
fcodeNames = {
    "third-order administrative division":"تقسيم من الدرجة الثالثة", 
    "mountain": "جبل", 
    "second-order administrative division": "مديرية", 
    "populated place": "مكان مأهول", 
    "first-order administrative division": "محافظة", 
    }
 
def run_with_wikidata(item , Ttitle , cla , adminCode1):
    coord , name , geonames , fcodeName , enwiki = '' , '' , '' , '', ''
    #---
    # النص  
    text = findtext(cla, adminCode1)
    #---
    tab = {}
    soper = ["lng","geonameId","toponymName","fcl","name","fclName","fcodeName","lat","fcode"]
    if text:
        for tr in text:
            #pywikibot.output( '<<lightyellow>> tr:' )
            #pywikibot.output(tr)
            #---
            # geonames
            if 'geonameId' in tr:
                #pywikibot.output( '<<lightyellow>> geonames:' )
                #pywikibot.output(tr['geonameId'])
                tab['geonameId'] = tr['geonameId']
            #---
            # geonames
            if 'name' in tr:
                #pywikibot.output( '<<lightyellow>> geonames:' )
                #pywikibot.output(tr['geonameId'])
                tab['name'] = tr['name']
            #---
            # fcodeName
            if 'fcodeName' in tr:
                #pywikibot.output( '<<lightyellow>> fcodeName:' )
                #pywikibot.output(tr['fcodeName'])
                if tr['fcodeName'] in fcodeNames:
                    tab['fcodeName'] = fcodeNames[tr['fcodeName']]
                else:
                    tab['fcodeName'] = tr['fcodeName'] 
            #---
            # coord
            coor = findcoord(tr)
            if coor:
                #pywikibot.output( '<<lightyellow>> coord:' )
                #pywikibot.output(coor)
                tab['coord'] = coor
            #---
            #pywikibot.output( '<<lightyellow>> tr:' )
            #pywikibot.output(tr)
            #pywikibot.output( 'tr<<lightyellow>> ----' )

            if ('coord' in tab):
                coord = tab['coord']
                #pywikibot.output(coord)
                
            if ('fcodeName' in tab):
                #pywikibot.output(fullname)
                fcodeName = tab['fcodeName'] 

            if ('name' in tab):
                name = tab['name'] 
                #pywikibot.output(name)
            if ('geonameId' in tab):
                geonames = tab['geonameId'] 
            if ('enwiki' in tab):
                enwiki = tab['enwiki'] 
                #pywikibot.output(name)
            if ('geonameId' in tab):
              pywikibot.output( '<<lightyellow>> tab:' )
              pywikibot.output(tab)
              log(item , Ttitle , coord ,fcodeName,  name , geonames , enwiki)
            #log(item , Ttitle , coord ,fcodeName,  name , geonames)
            #sa = {'coord':'coord','geonames':'geonames','name':'name','fcodeName':'fcodeName'}
        else:
            pywikibot.output('*no name')
#---
adminCode1list = {
    "مأرب":"14", 
    "المهرة": "3", 
    "الضالع": "18", 
    "الجوف": "21", 
    "لحج": "24", 
    "عمران": "19", 
    "عدن": "2", 
    "صنعاء": "16", 
    "صعدة": "15", 
    "ذمار": "11", 
    "حضرموت": "4", 
    "حجة": "22", 
    "تعز": "25", 
    "إب": "23", 
    "المحويت": "10", 
    "الحديدة": "8", 
    "البيضاء": "20", 
    "ريمة": "27", 
    "أبين": "1", 
    "العاصمة": "26", 
    "سقطرى": "28", 
    }
#---
def ISRENEW(page, Ttitle , numb):
    yemen = 'اليمن'
    adminCode1 = 'إب'
    
    if adminCode1 in adminCode1list:
        adminCode1 = adminCode1list [adminCode1]
        
    sp = '%2C+'#', '
    item = himoBOT2.Get_Item_API_From_Qid( "" , sites = "ar" , titles = Ttitle , props = "claims" )
    title = re.sub( '\s+\(.*\)$' , '' , Ttitle)
    title = re.sub( '(قرية|عزلة|حي|مديرية) ' , '' , title)
    #---
    pywikibot.output( '\n----------\n<<lightred>>>> %d >> "%s" << <<' % ( numb , title))
    #---
    name = title# + sp + gov# + sp +  yemen
    #cla2 = yemen + sp + gov + sp + title
    #pywikibot.output( '<<lightyellow>>"%s"' % item )
    if not item:
        pywikibot.output('**no item')
    else:
        if item["claims"] and ('P1566' in item["claims"]):                     #اذا كانت الصفحة بها خاصية الاسم العلمي
            pywikibot.output('already have P1566')
        else:
            run_with_wikidata( item , Ttitle , name , adminCode1)
#---
def main(*args):
    #args['ns'] = '0'
    generator = gent.get_gent(*args)
    numb = 0
    #---
    log('item' , 'Ttitle' , 'coord' , 'fullname',  'name' , 'geonames', 'enwiki')
    #---
    for page in generator:
        title = page.title(as_link=False)
        numb += 1
        ISRENEW(page, title, numb)
        
if __name__ == '__main__':
     main()
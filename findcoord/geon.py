#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

محاولة ايجاد احداثيات لمقالات قرى وعزل والخ اليمن


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
from pywikibot import pagegenerators
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.


    
def getURL2(url=''):
    html = ''
    try:
        html = urllib.request.urlopen(url).read().strip().decode('utf-8')
        #html = urllib.request.urlopen(url).read().strip().decode('utf-8')
    except:
        pass
    if html:
        return html
    else:
        return ''
        
def getURL(url=''):
    html = ''
    try:
        html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
        #html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
    except:
        sleep = 10 # seconds
        maxsleep = 60
        while sleep <= maxsleep:
            pywikibot.output('<<lightyellow>> Error while retrieving: %s' % (url))
            pywikibot.output('<<lightyellow>> Retry in %s seconds...' % (sleep))
            time.sleep(sleep)
            try:
                html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
                #html = urllib.request.urlopen(url).read().strip()#.decode('utf-8')
            except:
                pass
            sleep = sleep * 2
    if html !='':
        html = html.decode('utf-8')#.decode('utf-8')
    return html

def wd_sparql_generator(query):
  try:
    wikidatasite=pywikibot.Site('wikidata','wikidata') 
    repo = wikidatasite.data_repository()
    generator=pagegenerators.WikidataSPARQLPageGenerator(query,site=wikidatasite)
    for wd in generator:
        wd.get(get_redirect=True)
        yield wd
  except :
    return ''
    
def findtax(titl1value):
    titl1value = ''
    sa = 's'
    qua = 'SELECT ?item WHERE {?item wdt:P1566 "' + titl1value + '". } '#limit 1'
    json1 = wd_sparql_generator(qua)
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
    
def findtext(id , adminCode1):
    rid = id.replace( ' ' , '_')#.encode('utf-8')
    #gid = urllib.parse.quote(id)
    #url = 'geonames.org/search.html?q=' + gid + '&country=YE'
    url = 'geonames.org/advanced-search.html?q=' + rid + '&country=YE&lang=ar&adminCode1=' + adminCode1
    #url = 'geonames.org/advanced-search.html?q=' + 'Tawahi' + '&country=YE'
    #s = getURL(url= 'http://'+ url)
    #s = getURL(url= 'http://'+ url)
    s = urllib.request.urlopen('http://'+ url).read().strip().decode('utf-8')
    #s = re.sub( '\<\/name\>' , '</name>\n' , s)
    #s = re.sub( '\>\<' , '>\n<' , s)
    #s = re.sub( '\>\<' , '>\n<' , s)
    s = str(s)
    s = re.sub( '\>\n\<' , '><' , s)
    #---
    #s = s.replace('<table class="restable"><tbody><tr><td>', '<tt class="restable"><tbody><tr><td>')
    s = remove(s)
    s = re.sub('\<script type\=\"text\/javascript\"\>.*\<\/script\>', '' , s )
    s = re.sub('\<script\>.*\<\/script\>', '' , s )
    s = re.sub('\<tr class\=\"tfooter\"\>\<td colspan\=6\>\<\/td\>\<\/tr\>', '' , s )
    #pywikibot.output(s)
    pywikibot.output(url)
    
    #---
    findstate= '\<table class\=\"restable\"\>\s*.*\s*?\<\/table\>'
    OtherName =  re.compile( findstate )
    tables = OtherName.findall(s)
    #tables = re.search(findstate, s)
    lll = []
    if tables:
        for raw in tables:
        #lll = []
            raw = re.sub( "\<tr class\=\"\w+\"\>" , '<tr>' , raw)
            Othtables =  re.compile( '\<tr\>.*?\<\/tr\>' )
            line = Othtables.findall(raw)
            if line:
                #pywikibot.output( '<<lightyellow>> line:' )
                for la in line:
                    #pywikibot.output( '<<lightyellow>> la:' )
                    #pywikibot.output(la)
                    lll.append(la)
                #pywikibot.output( '<<lightyellow>> lll:' )
                #pywikibot.output(lll)
    #---

    return lll
    
def remove(text):
  text = re.sub('\<script type\=\"text\/javascript\"\>', '<script>' , text )
  templatelist = ["script", "SCRIPT", "STYLE", "head", "form", "a"]#, "body"]#, "Template", "a", "img"]#, "body"]
  for Tmain in templatelist:
    #pat =  re.compile( '(?<=\<' + Tmain + '\>)(\s*.*\s*)(?=\<\/' + Tmain + '\>)')
    #pat =  re.compile( '\<' + Tmain + '\>(.+)((\s)+(.+))+\<\/' + Tmain + '\>')
    #pat =  re.compile( '\<' + Tmain + '\>.*<\/' + Tmain + '\>')
    pat =  re.compile( '\<' + Tmain + '\b[^>]*\>.*?\<\/' + Tmain + '\>')
    has = pat.findall(text)
    if has:
      for fa_link in has:
        pywikibot.output( '<<lightyellow>> fa_link:' )
        pywikibot.output(fa_link)
        text = text.replace(fa_link, '')
  return text
  
def findfullname(tr):
    # fullname
    s = ''
    oo =  re.compile( '\<td\>.*?\<\/td\>' )
    cas = oo.findall(tr)
    if cas:
      for hh in cas:
         yh = hh.replace( '<span class="geo" style="display:none;">' ,  '')
         if hh != yh :
            hh = hh.split('<span class="geo" style="display:none;">')[0]
            hh = hh.split('.html">')[1]
            hh = re.sub( "\<(\/|)(a|br|small|td)\>" , ', ' , hh)
            hh = hh.replace( '<img src="/img/20px-Wikipedia-logo.png" width="15" border="0" alt="wikipedia article">' , '')

            hh = re.sub( "\s*,\s*,\s*" , ', ' , hh)
            #hh = re.sub( "\<br>" , ', ' ,  )
            #pywikibot.output( '<<lightyellow>> hh:' )
            #pywikibot.output(hh)
            s = hh#, ,
    s = re.sub( "\s*,\s*$" , '' , s)
    s = re.sub( ",\s*," , ',' , s)
    fuu = s.split(',')
    cas = {}
    for fu in fuu:
        fu = fu.strip()
        cas[fu] = ''
    if cas:
        pywikibot.output(cas)

        sa , arabic = '' , ''
        for ca in cas:
            fa_l = re.sub('[ءاآأئؤبتثجحخدذرزسشصضطظعضفقكلمنهوي]', '',ca)
            if ca == fa_l:
                sa = sa + '\t' + ca 
            else:
                arabic = ca
        #---
        if arabic != '':
            sa = arabic + '\t' + sa
            
        sa = re.sub( "#\t*" , '' , '#' + sa )
        #---
        pywikibot.output( '<<lightyellow>> ----fullname:' )
        pywikibot.output(sa)
        pywikibot.output( '\n<<lightyellow>> ----' )
        
        return sa
    
def findcoord(tr):
    # coord
    tab = {'coord':''}
    lat = re.compile("\<span class\=\"latitude\"\>(\d+\.\d+)?\<\/span\>")
    lon = re.compile("\<span class\=\"longitude\"\>(\d+\.\d+)?\<\/span\>")
    latitude = lat.findall(tr)
    longitude = lon.findall(tr)

    if longitude and latitude:
        coord = '@' + longitude[0] + '/' + latitude[0]
        #pywikibot.output( '<<lightyellow>> coord:' )
        #pywikibot.output(coord)
        #pywikibot.output( '<<lightyellow>> ----' )
        tab['coord'] = coord
    return tab['coord']
    
def findname(tr):
    # name
    tab = {'name':''}
    oo =  re.compile( '\<td\>.*?\<\/td\>' )
    ll = oo.findall(tr)
    if ll:
        for lo in ll:
            rr = lo.replace( '<a href="/countries/YE/yemen.html">Yemen</a>,' ,  '')
            if lo != rr :
                rr = re.sub( "\<(\/|)(small|td)\>" , '' , rr)
                rr = re.sub( "\<br>" , ', ' , rr)
                #pywikibot.output( '<<lightyellow>> name:' )
                #pywikibot.output(rr)
                tab['name'] = rr
    return tab['name']
    
def run_with_wikidata(item , Ttitle , cla , adminCode1):
    coord , name , geonames , fullname , enwiki = '' , '' , '' , '', ''
    #---
    # النص  
    text = findtext(cla, adminCode1)
    #---
    
    if text:
        for tr in text:
            tab = {'enwiki':''}
            tr = re.sub( "\&nbsp\;" , '' , tr)
            tr = re.sub( "\<td nowrap\>(.*)[^<]\<\/td\>" , '' , tr)
            tr = re.sub( "\<small\>\<\/small\>" , '' , tr)
            #---
            #o = '\<a href\=\"\http\:\/\/en\.wikipedia\.org\/wiki\/(.*[^"])\"\>'
            img = '<img src="/img/20px-Wikipedia-logo.png" width="15" border="0" alt="wikipedia article">'
            o = '\<a href\=\"\http\:\/\/en\.wikipedia\.org\/wiki\/(.*[^<>"])\"\>'+img+'\<\/a\>'
            #---
            # enwiki
            oo =  re.compile( o )
            enwiki = oo.findall(tr)
            if enwiki:
              enwiki = enwiki[0]#.split('">')[0]
              #rr = re.sub( "\<br>" , ', ' , rr)
              pywikibot.output( '<<lightyellow>> enwiki:' )
              pywikibot.output(enwiki)
              tab['enwiki'] = enwiki
            #---
            tr = re.sub( o , '' , tr)
            #---
            # fullname
            fullname = findfullname(tr)
            if fullname:
                tab['fullname'] = fullname
                
            #---
            # name
            name = findname(tr)
            if name:
              tab['name'] = name
            
            #---
            # geonames
            geo = "\<a href\=\"http\:\/\/www\.geonames\.org\/(\d+)\/.*\.html\"\>.*?\<\/a\>"             
            geon = re.compile(geo)
            geonames = geon.findall(tr)
            if geonames:
                #pywikibot.output( '<<lightyellow>> geonames:' )
                #pywikibot.output(geonames[0])
                tab['geonames'] = geonames[0]
                
            #---
            # coord
            coord = findcoord(tr)
            if coord:
              tab['coord'] = coord
            #---
            #pywikibot.output( '<<lightyellow>> tr:' )
            #pywikibot.output(tr)
            #pywikibot.output( 'tr<<lightyellow>> ----' )

            if ('coord' in tab):
                coord = tab['coord']
                #pywikibot.output(coord)
                
            if ('fullname' in tab):
                fullname = tab['fullname'] 
                #pywikibot.output(fullname)
                
            if ('name' in tab):
                name = tab['name'] 
                #pywikibot.output(name)
                
            if ('geonames' in tab):
                geonames = tab['geonames'] 
            if ('enwiki' in tab):
                enwiki = tab['enwiki'] 
                #pywikibot.output(name)
            if ('geonames' in tab):
              log(item , Ttitle , coord ,fullname,  name , geonames , enwiki)
            #log(item , Ttitle , coord ,fullname,  name , geonames)
            #sa = {'coord':'coord','geonames':'geonames','name':'name','fullname':'fullname'}
    else:
        pywikibot.output('*no name')
        
#---
# دالة إيجاد رقم المقالة الإنجليزية في ويكي داتا
def FindItemQ(Title):
    site = pywikibot.Site('ar', 'wikipedia')
    page = pywikibot.Page(site, Title)
    try:
        item = pywikibot.ItemPage.fromPage(page)
        #match = re.search('(Q\d+)', str(item))               # استخراج الرقم Q?????
        return item
    except:
        return ''
		
adminCode1list = [
	"مأرب": "72966", 
	"المهرة": "78985", 
	"الضالع": "6201193", 
	"الجوف": "74222", 
	"لحج": "6201197", 
	"عمران": "6201194", 
	"عدن": "80412", 
	"صنعاء": "71132", 
	"صعدة": "71333", 
	"ذمار": "76183", 
	"حضرموت": "75411", 
	"حجة": "6201195", 
	"تعز": "70222", 
	"إب": "6201196", 
	"المحويت": "73200", 
	"الحديدة": "79416", 
	"البيضاء": "79838", 
	"ريمة": "71532", 
	"أبين": "80425", 
	"العاصمة": "6940571", 
	"سقطرى": "9645387",
	]


def ISRENEW(page, Ttitle , numb):
    yemen = 'اليمن'
    adminCode1 = 'الجوف'
	
    if adminCode1 in adminCode1list:
        adminCode1 = adminCode1list [adminCode1]
		
    sp = '%2C+'#', '
    item = FindItemQ(Ttitle)
    title = re.sub( '\s+\(.*\)$' , '' , Ttitle)
    title = re.sub( '(قرية|عزلة|حي|مديرية) ' , '' , title)
    #---
    
    pywikibot.output( '\n----------\n<<lightred>>>> %d >> "%s" << <<' % ( numb , title))
    
    #---
    name = title + sp + gov# + sp +  yemen
    #cla2 = yemen + sp + gov + sp + title
    pywikibot.output( '<<lightyellow>>"%s"' % cla )
    if not item:
        pass
        pywikibot.output('**no item')
    else:
        run_with_wikidata(item.title(as_link=False) , Ttitle , name , adminCode1)
   
def pagegenerator(limit):
    wikidatasite=pywikibot.Site('wikidata','wikidata') 
    repo = wikidatasite.data_repository()
    query = """ SELECT ?item
            WHERE
            { #BIND(wd:Q6965158 AS ?item).
              ?item wdt:P625 ?location . 
              ?item wdt:P1566 ?P1566 . 
              #?item wdt:P131* wd:Q805 .
              ?item wdt:P17* wd:Q805 .
              FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .
              {?item rdfs:label ?itemaen filter (lang(?itemaen) = "en")} .
            }
            LIMIT """ + limit
    generator = pagegenerators.WikidataSPARQLPageGenerator(query,site=wikidatasite)
    for wd in generator:
      wd.get(get_redirect=True)
      yield wd
                      
def wd_from_file():
  repo=pywikibot.Site('wikidata','wikidata').data_repository()
  csvfile=open('geo2/do2.txt','r')
  for alllines in csvfile:
    qitem=alllines[alllines.find('Q'):alllines.find(',')]
    if (len(qitem)>0):
      wditem=pywikibot.ItemPage(repo,qitem)
      if (not(wditem.isRedirectPage())):
       if wditem.exists():
        wditem.get(get_redirect=True)
        yield wditem
        
def main(*args):
    #args['ns'] = '0'
    generator = gent.get_gent(*args)
    numb = 0
    #---
    #sa = {'coord':'coord','geonames':'geonames','name':'name','fullname':'fullname'}
    log('item' , 'Ttitle' , 'coord' , 'fullname',  'name' , 'geonames', 'enwiki')
    #---
    for page in generator:
        #text = page.text
        title = page.title(as_link=False)
        #start(text, title)
        numb += 1
        #try:
        ISRENEW(page, title, numb)
        #except:
            #pywikibot.output( 'pass ' +  title)
        
if __name__ == '__main__':
     main()
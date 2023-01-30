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
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse
#---
import string
import json
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.


#---
# start of himoBOT.py file
from API import himoBOT
#---
wikidatasite=pywikibot.Site('wikidata','wikidata') 
repo = wikidatasite.data_repository()
#---
def log(item , Ttitle , coord , display_name , osm_id):
    item = item.title(as_link=False)
    so = '%s\t%s\t%s\t%s\t%s\t\n' % (Ttitle , item , 'P625\t' + coord , display_name , osm_id)
    pywikibot.output(so)
    with codecs.open("findcoord/marib.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(so)
      except :
            pywikibot.output("Error writing")
    
def findtext(id):
    #---
    fao = urllib.parse.quote(id)
    #---
    url = 'nominatim.openstreetmap.org/search/' + fao + '?format=xml&addressdetails=1&accept-language=ar'
    s = himoBOT.getURL(url= 'http://'+ url)
    #s = re.sub( '\<\/name\>' , '</name>\n' , s)
    s = re.sub( '\>\<' , '>\n<' , s)
    #pywikibot.output(s)
    pywikibot.output(url)
    return s
   
def run_with_wikidata(item , Ttitle , cla):
    coord , display_name , osm_id , state = '' , '' , '' , ''
    #---
    # النص  
    text = findtext(cla)
    #---
    findstate= '\<place place_id\=.*?\>'
    OtherName =  re.compile( findstate )
    Data = OtherName.findall(text)
    #Data = re.search(findstate, text)
    sa = ["osm_id='1226340015'","lat='13.460717'","lon='44.164866'","display_name='قرية سعدة, تعز, اليمن'"]
    tab = {}
    if Data:
        for name in Data:
            name = re.sub( "(\<place|\>)" , '' , name)
            #pywikibot.output( '<<lightyellow>> name:' )
            #pywikibot.output(name)
            Othtables =  re.compile( "\w+\=\'.*?\'" )
            tables = Othtables.findall(name)
            if tables:
                #pywikibot.output( '<<lightyellow>> tables:' )
                #pywikibot.output(tables)
                for ta in tables:
                    ta  = re.sub( "\=[\'\"]" , '=' , ta)
                    ta  = re.sub( "[\'\"]$" , '' , ta)
                    foo = ta.split('=')[0]
                    boo = ta.split('=')[1]
                    tab[foo] = boo
            pywikibot.output( '<<lightyellow>> tab:' )
            pywikibot.output(tab)
            if ('lat' in tab) and ('lon' in tab):
                coord = (   "@%s/%s"   %   ( tab['lat'] , tab['lon'] )  )
                #pywikibot.output(coord)
            if ('display_name' in tab):
                display_name = tab['display_name'] 
                #pywikibot.output(display_name)
            if ('osm_id' in tab):
                osm_id = tab['osm_id'] 
                #pywikibot.output(display_name)
            """name = re.sub( '\<place.*\s*lat\='  , 'lat='  , name)
            name = re.sub( "class\=\'place\'.*\>"  , '\t'  , name)
            Nat_Name = re.search( 'display_name' , name)

            pywikibot.output( '<<lightyellow>> name:' )
            pywikibot.output(name)
            name = re.sub( "lat\=\'(.*)\' lon\=\'(.*)?\'"  , "@\g<1>/\g<2>"  , name)

            pywikibot.output( '<<lightyellow>> name:' )
            pywikibot.output(name)"""
            log(item , Ttitle , coord , display_name , osm_id)
			
    else:
        pywikibot.output('*no name')
        
#---
# دالة إيجاد رقم المقالة الإنجليزية في ويكي داتا
def FindItemQ(Title):
    return himoBOT.GetItem(Title , 'ar')

def ISRENEW(page, Ttitle , numb):
    yemen = 'اليمن'
    gov = 'الجوف'
    sp = '، '
    item = FindItemQ(Ttitle)
    title = re.sub( '\s+\(.*\)$' , '' , Ttitle)
    title = re.sub( '(قرية|عزلة|حي) ' , '' , title)
    #---
    
    pywikibot.output( '\n----------\n<<lightred>>>> %d >> "%s" << <<' % ( numb , title))
    
    #---
    cla = title + sp + gov + sp +  yemen
    cla2 = yemen + sp + gov + sp + title
    pywikibot.output( '<<lightyellow>>"%s"' % cla )
    if not item:
        pywikibot.output('**no item')
    else:
        run_with_wikidata(item , Ttitle , cla)
   
def main(*args):
    #args['ns'] = '0'
    generator = gent.get_gent(*args)
    numb = 0
    for page in generator:
        title = page.title(as_link=False)
        numb += 1
        ISRENEW(page, title, numb)
        
if __name__ == '__main__':
     main()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

python3 pwb.py dump/labels2
python3 pwb.py dump/labels2 test
python3 pwb.py dump/labels2 test nosave

"""
#
# (C) Ibrahem Qasim, 2022
#
#

# Copyright (C) 2017 emijrp <emijrp@gmail.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import re
import bz2
#import gz
import json
import time
import pywikibot
#---
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
#ar_site = pywikibot.Site('ar', 'wikipedia')
title = 'User:Mr. Ibrahem/Language statistics for items'
if 'test' in sys.argv :
    title = 'User:Mr. Ibrahem/Language'
#---
Old = {}
#---
texts = himoBOT2.GetPageText(title.replace(' ','_') , 'www', family='wikidata')
texts = texts.split('|}')[0]
texts = texts.replace('|}','')
texts = texts.replace(',','')
for L in texts.split('|-'):
    L = L.strip()
    L = L.replace('\n','|')
    if L.find('{{#language:') != -1 :
        L = re.sub('\(\d+\.\d+\%\)','',L)
        L = re.sub('\|\|\s*\+\d+\s*','',L)
        L = re.sub('\|\|\s*\-\d+\s*','',L)
        L = re.sub('\s*\{\{\#language\:.*?\}\}\s*','',L)
        L = re.sub('\s*\|\|\s*','||',L)
        L = re.sub('\s*\|\s*','|',L)
        L = L.replace('||||||','||')
        L = L.strip()
        #iu = re.search("(.*?)\|\|(.*?)\|\|(.*?)\|\|(.*?)", L)
        #iu = re.search("\|(.*?)\|\|(\d+?|)\|\|(\d+?|)\|\|(\d+?|)", L)
        iu = re.search("\|(.*?)\|\|(\d*)\|\|(\d*)\|\|(\d*)", L)
        if iu :
            #print(L)
            lang = iu.group(1).strip()
            Old[lang] = {'labels':0,'descriptions':0,'aliases':0}
            
            labels =  iu.group(2)
            if labels:
                Old[lang]['labels'] = int(labels )
            
            descriptions = iu.group(3)
            if descriptions:
                Old[lang]['descriptions'] = int(descriptions )
            
            aliases = iu.group(4)
            if aliases:
                Old[lang]['aliases'] = int(aliases )
        #else:
            #pywikibot.output( 'no iu ' )
#---
All_items = { 1 : 0 } 
Limit = { 1 : 500000000 } 
#---
# python3 pwb.py wd/dump test 
#---
if sys.argv and "test" in sys.argv:
    Limit[1] = 3000
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(':')
    #---
    if arg.startswith('-') : arg = arg[1:]
    #---
    if arg == "limit":
        Limit[1] = int(value)
    #---
# python3 pwb.py dump/dump limit:1000000
#---
def make_cou( num , all ):
    if num == 0 :
        return 0
    fef = ( num / all) * 100
    return str(fef)[:4] + "%"
#---
def mainar():
    #---
    start = time.time()
    t1 = time.time()
    #---
    Main_Table = {}
    #---
    c = 0
    dumpdate = 'latest'
    f = bz2.open('/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2' , 'r')
    #---
    if 'lene' in sys.argv:
        pywikibot.output( 'len of bz2 lines :%d ' % len( json.loads( [ x for x in f if x.startswith('{') and x.endswith('}') ] ) ) )
    #---
    try:
        pywikibot.output( 'len of bz2 lines :%d ' % len( json.loads( [ x for x in f if x.startswith('{') and x.endswith('}') ] ) ) )
    except:
        pywikibot.output('')
    #---
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1
        if c < Limit[1] : 
            if line.startswith('{') and line.endswith('}'):
                #---
                All_items[1] += 1
                #---
                if "printline" in sys.argv and c % 1000 == 0:
                    pywikibot.output( line ) 
                #---
                json1 = json.loads(line)
                #---
                labels = json1.get('labels',{})
                #---
                for code in labels:
                    if not code in Main_Table:
                        Main_Table[code] = {'labels':0,'descriptions':0,'aliases':0}
                    Main_Table[code]['labels'] += 1
                #---
                descriptions = json1.get('descriptions',{})
                for code in descriptions:
                    if not code in Main_Table:
                        Main_Table[code] = {'labels':0,'descriptions':0,'aliases':0}
                    Main_Table[code]['descriptions'] += 1
                #---
                aliases = json1.get('aliases',{})
                for code in aliases:
                    if not code in Main_Table:
                        Main_Table[code] = {'labels':0,'descriptions':0,'aliases':0}
                    Main_Table[code]['aliases'] += 1
                #---
            if c % 1000 == 0:
                print(c, time.time()-t1)
                t1 = time.time()
            #pywikibot.output([[y, x] for x, y in p31.items()])
        else:
            break
    #---
    lisr_old = '''| %s || {{#language:%s|en}} || {{#language:%s}}
| {{subst:formatnum:%d}} (%s) || {{subst:formatnum:%d}} (%s) || {{subst:formatnum:%d}}'''
    #---
    #---
    lisr = '''| %s || {{#language:%s|en}} || {{#language:%s}}
| {{subst:formatnum:%d}} (%s) || +{{subst:formatnum:%s}} || {{subst:formatnum:%d}} (%s) || +{{subst:formatnum:%s}} || {{subst:formatnum:%d}} || +{{subst:formatnum:%s}}'''
    #---
    p31list = list(Main_Table.keys())
    p31list.sort()
    rows = []
    #---
    test_new_descriptions = 0
    #---
    for code in p31list:
        #---
        new_labels = 0
        new_descriptions = 0
        new_aliases = 0
        #---
        if code in Old:
            new_labels = int( Main_Table[code]['labels'] - Old[code]['labels'] )
            new_descriptions = int( Main_Table[code]['descriptions'] - Old[code]['descriptions'] )
            new_aliases = int( Main_Table[code]['aliases'] - Old[code]['aliases'] )
        else:
            pywikibot.output( 'code "%s" not in Old' % code )
        #---
        if new_descriptions != 0 :
            test_new_descriptions = 1
        #---
        line = lisr % (
            code,
            code,
            code,  
            Main_Table[code]['labels'], 
            make_cou(Main_Table[code]['labels'] , All_items[1]), 
            str( new_labels ) ,
            
            Main_Table[code]['descriptions'], 
            make_cou(Main_Table[code]['descriptions'] , All_items[1]), 
            str( new_descriptions ),
            
            Main_Table[code]['aliases'] ,
            str( new_aliases )
            
        )
        line = line.replace("+-" , "-" )
        line = line.replace("+{{subst:formatnum:-" , "-{{subst:formatnum:" )
        line = line.replace("{{subst:formatnum:0}}" , "0" )
        rows.append( line )
    #---
    rows = '\n|-\n'.join(rows)
    #---
    table = """
== Number of labels, descriptions and aliases for items per language ==
{| class="wikitable sortable"
|-
! Language code
! Language (English)
! Language (native)
! data-sort-type="number"|# of labels
! data-sort-type="number"|# new labels
! data-sort-type="number"|# of descriptions
! data-sort-type="number"|# new descriptions
! data-sort-type="number"|# of aliases
! data-sort-type="number"|# new aliases
|-
%s
|}
[[Category:Wikidata statistics|Language statistics]]
""" % rows
    #---
    if test_new_descriptions == 0 : 
        pywikibot.output( 'nothing new.. ' )
        return '' 
    #---
    final = time.time()
    delta = int(final - start)
    #---
    text = ""
    text = "Update: <onlyinclude>%s</onlyinclude>.\n" % dumpdate
    text += "* Total items:{{subst:formatnum:%d}} \n" % All_items[1]
    text += "<!-- bots work done in %d secounds --> \n" % delta
    text += "--~~~~~\n"
    text = text + "\n" + table
    text = text.replace( "0 (0000)" , "0" )
    text = text.replace( "0 (0)" , "0" )
    #---
    if text != "" : 
        #---
        if not 'test' in sys.argv:
            pywikibot.output( text )
        #---
        if not "nosave" in sys.argv:
            if 'test' in sys.argv :
                #title = 'User:Mr. Ibrahem/Language'
                text = text.replace('[[Category:Wikidata statistics|Language statistics]]','')
            from API import himoAPI
            himoAPI.page_putWithAsk('' , text , 'Bot - Updating stats' , title, False)
        else:
            pywikibot.output( text )
    #---
    if not 'test' in sys.argv :
        with open( main_dir + 'dump/dump.labels2.txt' , 'w' ) as f:
            f.write(text)
#---
if __name__ == '__main__':
    #print(make_cou( 70900911 , 84601659 ))
    mainar()
#---
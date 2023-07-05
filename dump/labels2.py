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

import sys
import os
import re
import bz2
#import gz
import json
import time
import pywikibot

Dump_Dir = os.path.dirname(os.path.realpath(__file__))
if not Dump_Dir.endswith('/'): Dump_Dir += '/'

print(f'Dump_Dir: {Dump_Dir}')

from API import himoBOT2

#ar_site = pywikibot.Site('ar', 'wikipedia')
title = 'User:Mr. Ibrahem/Language statistics for items'
if 'test' in sys.argv :
    title = 'User:Mr. Ibrahem/Language'

def make_old_values():
    Old = {}

    texts = himoBOT2.GetPageText(title.replace(' ','_') , 'www', family='wikidata')
    texts = texts.split('|}')[0]
    texts = texts.replace('|}','')
    texts = texts.replace(',','')
    for L in texts.split('|-'):
        L = L.strip()
        L = L.replace('\n','|')
        if L.find('{{#language:') != -1 :
            L = re.sub(r'\(\d+\.\d+\%\)','',L)
            L = re.sub(r'\|\|\s*\+\d+\s*','',L)
            L = re.sub(r'\|\|\s*\-\d+\s*','',L)
            L = re.sub(r'\s*\{\{\#language\:.*?\}\}\s*','',L)
            L = re.sub(r'\s*\|\|\s*','||',L)
            L = re.sub(r'\s*\|\s*','|',L)
            L = L.replace('||||||','||')
            L = L.strip()
            #iu = re.search(r"(.*?)\|\|(.*?)\|\|(.*?)\|\|(.*?)", L)
            #iu = re.search(r"\|(.*?)\|\|(\d+?|)\|\|(\d+?|)\|\|(\d+?|)", L)
            iu = re.search(r"\|(.*?)\|\|(\d*)\|\|(\d*)\|\|(\d*)", L)
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
    return Old

All_items = { 1 : 0 } 
Limit = { 1 : 500000000 } 

# python3 pwb.py wd/dump test 

if sys.argv and "test" in sys.argv:
    Limit[1] = 3000

for arg in sys.argv:

    arg, sep, value = arg.partition(':')

    if arg.startswith('-') : arg = arg[1:]

    if arg == "limit":
        Limit[1] = int(value)

# python3 pwb.py dump/dump limit:1000000

def make_cou( num , all ):
    if num == 0 :
        return 0
    fef = ( num / all) * 100
    return str(fef)[:4] + "%"

def get_data():

    t1 = time.time()
    Main_Table = {}

    c = 0

    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'

    if not os.path.isfile(filename):
        pywikibot.output( f'file {filename} <<lightred>> not found' )
        return

    f = bz2.open(filename, 'r')

    if 'lene' in sys.argv:
        pywikibot.output( 'len of bz2 lines :%d ' % len( json.loads( [ x for x in f if x.startswith('{') and x.endswith('}') ] ) ) )

    try:
        pywikibot.output( 'len of bz2 lines :%d ' % len( json.loads( [ x for x in f if x.startswith('{') and x.endswith('}') ] ) ) )
    except:
        pywikibot.output('')

    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1

        if c > Limit[1] :  break

        if line.startswith('{') and line.endswith('}'):

            All_items[1] += 1

            if "printline" in sys.argv and c % 1000 == 0:   pywikibot.output( line ) 

            json1 = json.loads(line)

            tats = [ 'labels', 'descriptions', 'aliases']

            for x in tats:
                for code in json1.get(x,{}):
                    if not code in Main_Table:  Main_Table[code] = {'labels':0,'descriptions':0,'aliases':0}
                    Main_Table[code][x] += 1

        if c % 1000 == 0:
            print(c, time.time()-t1)
            t1 = time.time()

    return Main_Table

def mainar():

    dumpdate = 'latest'
    start = time.time()

    Old = make_old_values()

    Main_Table = get_data()

    langs = list(Main_Table.keys())
    langs.sort()
    rows = []

    test_new_descriptions = 0

    for code in langs:

        new_labels = 0
        new_descriptions = 0
        new_aliases = 0

        if code in Old:
            new_labels          = int( Main_Table[code]['labels'] - Old[code]['labels'] )
            new_descriptions    = int( Main_Table[code]['descriptions'] - Old[code]['descriptions'] )
            new_aliases         = int( Main_Table[code]['aliases'] - Old[code]['aliases'] )
        else:
            pywikibot.output( 'code "%s" not in Old' % code )

        if new_descriptions != 0 :
            test_new_descriptions = 1

        line = '''| %s || {{#language:%s|en}} || {{#language:%s}}
| {{subst:formatnum:%d}} (%s) || +{{subst:formatnum:%s}} || {{subst:formatnum:%d}} (%s) || +{{subst:formatnum:%s}} || {{subst:formatnum:%d}} || +{{subst:formatnum:%s}}''' % (
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

    rows = '\n|-\n'.join(rows)

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

    if test_new_descriptions == 0 : 
        pywikibot.output( 'nothing new.. ' )
        return '' 

    final = time.time()
    delta = int(final - start)

    text = ""
    text = "Update: <onlyinclude>%s</onlyinclude>.\n" % dumpdate
    text += "* Total items:{{subst:formatnum:%d}} \n" % All_items[1]
    text += "<!-- bots work done in %d secounds --> \n" % delta
    text += "--~~~~~\n"
    text = text + "\n" + table
    text = text.replace( "0 (0000)" , "0" )
    text = text.replace( "0 (0)" , "0" )

    if text == "" : return

    pywikibot.output( text )

    if not 'test' in sys.argv :
        -
        if not "nosave" in sys.argv:
            #title = 'User:Mr. Ibrahem/Language'
            text = text.replace('[[Category:Wikidata statistics|Language statistics]]','')
            from wd_API import himoAPI
            himoAPI.page_putWithAsk('', text, 'Bot - Updating stats', title, False)

        with open( Dump_Dir + 'dumps/dump.labels2.txt' , 'w' ) as f:
            f.write(text)

if __name__ == '__main__':
    #print(make_cou( 70900911 , 84601659 ))
    mainar()

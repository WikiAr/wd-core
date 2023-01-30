#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف للكائنات بناءاً على استعلام جديد


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
import codecs
from API.maindir import main_dir #used in logfiles, unicoded strings
import datetime
import json
#---
import sys
#---
import urllib

import urllib
import urllib.request
import urllib.parse
#---
from all_new_taxo import *
saso = {}
for tab in [Arabic , gens]:
    for key in tab:
        for lang in tab[key].keys():
            saso[lang] = ''
ALl_Lang = [x for x in saso.keys()]
ALl_Lang.sort()
#---
arabi2c = {
    "Q1390":{#/
        'ar': "من الحشرات",
        'an': "d'insecto",
        'gl': 'de insecto',
        'ca': "d'insectes",
        'nl': "van insecten",
        'en': "of insects",
        'es': "de insectos",
        'fr': "d'insectes",
        'id': "serangga",
        'it': "di insetti",
        'pt': "de insetos",
        'pt-br': "de insetos",
        'ro': "de insecte",
        'ru': "род насекомых",
        'sq': "e insekteve",
        }
    }
#---
gen2s = {

    'Q7432' : { 
            "ar": "نوع",
            "an": "especie",
            "en": "species",
            "ca": "espècie",
            "es": "especie",
            "de": "Art",
            "fr": "espèce",
            "gl": "especie",
            "id": "spesies",
            "it": "specie",
            "pt": "espécie",
            "pt-br": "espécie",
            "ro": "specie",
            'sq': 'specie',
            'nl': 'soort',
            'pt-br': 'espécie',
            'pt': 'espécie',
        },
    "Q3025161" : {
            "en": "series",
            "nl": "serie", 
            "ar": "سلسلة" ,
            #'fr': '',
            'de': 'Serie',
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            #'it': 'sottogenere',
        },
    }
#---
ALl_Lang_1 = ['an', 'ar', 'ca', 'cy', 'de', 'en', 'es', 'fr', 'gl']
ALl_Lang_2 = ['he', 'id', 'it', 'nl', 'pt', 'pt-br', 'ro', 'ru', 'sq']
#---
def main2():
    pywikibot.output('main: ')
    pywikibot.output(ALl_Lang)
    translations  = {}
    num = 0
    
    for type in Arabic.keys():
        translations[type] = {}
        pywikibot.output( '== {{Q|%s}} ==' % type )
        for langs in [ALl_Lang_1 , ALl_Lang_2 ] :
            row = '{| class="wikitable sortable" \n|-\n! type !! '
            rows = row + ' !! '.join(langs)
            for gen in gens.keys():
                rows = rows + '\n|-\n'
                rows = rows + '| {{Q|%s}} ||' % gen
                num += 1
                gen_table = {}
                for lang in langs:
                    translations[type][gen] = {}
                    #for lang in ALl_Lang:
                    #for lang in Arabic[type]:
                    p1 = gens[gen].get(lang , '//')
                    p2 = Arabic[type].get(lang , '//')#.lower()
                    gen_table[lang] = p1 + ' ' + p2
                    #translations[type][gen][lang] = p1 + ' ' + p2
                listofdesc = [gen_table[lang] for lang in langs]
                #pywikibot.output( 'desc: "%s"@%s.' % (lang , p1 + ' ' + p2 ) )
                rows = rows + ' || '.join(listofdesc)
            rows = rows + '\n|-\n|}'
            pywikibot.output(rows)
#---
def main3():
    pywikibot.output('main: ')
    pywikibot.output(ALl_Lang)
    translations  = {}
    num = 0
    for type in Arabic.keys():
        translations[type] = {}
        head =  '== {{Q|%s}} ==' % type
        #pywikibot.output(head)
        table =  head + '\n'
        for gen in gens.keys():
            rows = '\n==={{Q|%s}}===\n' % gen
            pywikibot.output(rows)
            #rows = rows + '|+ {{Q|%s}}' % gen
            rows = rows + '{| class="wikitable sortable" \n|-\n'
            for langs in [ALl_Lang_1 , ALl_Lang_2 ] :
                rows = rows + '\n|-\n! ' + ' !! '.join(langs)
                rows = rows + '\n|-\n| '
                num += 1
                gen_table = {}
                for lang in langs:
                    translations[type][gen] = {}
                    #for lang in ALl_Lang:
                    #for lang in Arabic[type]:
                    gen_table[lang] = ''
                    p1 = gens[gen].get(lang , '-')
                    p2 = Arabic[type].get(lang , '+')#.lower()
                    if not (p1 == '-' and p2 == '+'):
                        gen_table[lang] = "'''" + p1 + "''' " + p2
                    #translations[type][gen][lang] = p1 + ' ' + p2
                listofdesc = [gen_table[lang] for lang in langs]
                #pywikibot.output( 'desc: "%s"@%s.' % (lang , p1 + ' ' + p2 ) )
                rows = rows + ' || '.join(listofdesc)
            rows = rows + '\n|-\n|}\n\n'
            table = table + rows
        #pywikibot.output(table)
        with codecs.open("taxo/table.csv", "a", encoding="utf-8") as logfile:
            logfile.write(table)
            logfile.close()
#---
def main():
    pywikibot.output('main: ')
    pywikibot.output(ALl_Lang)
    genskeys = [x for x in gens.keys()]
    genskeys.sort()
    pywikibot.output(genskeys)
    #translations  = {}
    num = 0
    for type in Arabic.keys():
        rows = ''
        #translations[type] = {}
        head =  '== {{Q|%s}} ==\n' % type
        #pywikibot.output(head)
        head = head + '{| class="wikitable" \n|-\n'
        table =  head + '\n'
        #rows = '\n==={{Q|%s}}===\n' % gen
        #pywikibot.output(rows)
        #rows = rows + '|+ {{Q|%s}}' % gen

        gg = [('{{Q|%s}}' % x) for x in genskeys]
        rows = rows +  '\n|-\n! lang !! ' + ' !! '.join(gg)
        rows = rows + '\n|-\n'
        for lang in ALl_Lang:
            lang_table = {}
            for gen in genskeys:
                    #translations[type][gen] = {}
                    #for lang in ALl_Lang:
                    #for lang in Arabic[type]:
                    lang_table[gen] = ''
                    p1 = gens[gen].get(lang , '-')
                    p2 = Arabic[type].get(lang , '+')#.lower()
                    if not (p1 == '-' and p2 == '+'):
                        lang_table[gen] = "'''" + p1 + "''' " + p2
                    #translations[type][gen][lang] = p1 + ' ' + p2
            listofdesc = [lang_table[gen] for gen in genskeys]
            #pywikibot.output( 'desc: "%s"@%s.' % (lang , p1 + ' ' + p2 ) )
            rows = rows + '\n|-\n| %s || '  % lang
            rows = rows + ' || '.join(listofdesc)
        rows = rows + '\n|-\n|}\n\n'
        table = table + rows
        #pywikibot.output(table)
        with codecs.open("taxo/table.csv", "a", encoding="utf-8") as logfile:
            logfile.write(table)
            logfile.close()
#---
if __name__ == "__main__":  
     main()
#---
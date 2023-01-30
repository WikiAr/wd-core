#!/usr/bin/python
# -*- coding: utf-8  -*-
#
"""

python pwb.py taxnew/insect -file:taxnew/insect.csv
python pwb.py taxnew/insect -file:taxnew/in2.csv
python pwb.py taxnew/insect -file:taxnew/in3.csv
python pwb.py taxnew/insect -file:taxnew/in4.csv 

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
from pywikibot import pagegenerators
from pywikibot import pagegenerators as pg

import re
import codecs
import sys
import datetime
from datetime import datetime, date, time
#---
import sys
#---
import urllib

import urllib
import urllib.request
import urllib.parse
#---
# start of himoBOT.py file
from API import himoBOT
#---
import tax
from API.descraptions import Taxon_Descraptions
taxondescs = {  
    'species of insect': Taxon_Descraptions['species of insect'],
    }
#---
def Action_One_Item(item , desc , taxondescs):
    tt = False
    #---
    try:
        item.get()
        tt = True
    except:
        pass
    #---
    #pywikibot.output( '<<lightyellow>>* work 2:' )
	if tt:
		descriptions = item.descriptions
		NewDesc = {}
		addedlangs = []
		q = item.title(as_link=False)
		#---
		for lang in translations[translation].keys():
			if not lang in descriptions.keys():
				#descriptions[lang] = translations[translation][lang]
				NewDesc[lang] = {"language":lang,"value":translations[translation][lang]}
				addedlangs.append(lang)
		#---
		if addedlangs:
			pywikibot.output( '<<lightyellow>>* work 2:%s ' % q )
			#pywikibot.output(NewDesc)
			himoBOT.work_api_desc( NewDesc , q)
		else:
			pywikibot.output( '<<lightred>>* work 2 :%s nothing to add.' % q )

#---
def main2(*args):
    pywikibot.output ("- بدء المهمة")
    options = {}
    #---
    genFactory = pagegenerators.GeneratorFactory()
    local_args = pywikibot.handle_args(args)
    desc = 'species of insect'
    #---
    for arg in local_args:
        arg, sep, value = arg.partition(':')
        options[arg] = value
    pywikibot.output(options)
    #---
    num = 0
    if '-file' in options:
        file = options['-file']
        json1 = himoBOT.wd_from_file('taxnew/in2.csv')
        action( json1 , desc , taxondescs)
    else:
        pywikibot.output('-file not in options:' )     
#---
def main():
    pywikibot.output("- بدء المهمة")
    #---
    desc = 'species of insect'
    tab = taxondescs[desc]
    totalqueries = len(taxondescs) * len(tab.keys())
    Queries = 0
    #---
    for targetlang in tab.keys():
        #---
        #targetlang = 'es'
        #pywikibot.output(targetlang + '\t' + genderlabel + '\t' + desc)#, taxondescs[desc][targetlang][genderlabel])
        #---
        labeeel  = taxondescs[desc][targetlang]
        out = '<<lightgreen>>  *== Quary:%s, %d/%d; %s:. %s=='
        pywikibot.output(out % (desc, Queries, totalqueries, targetlang, str(labeeel) ))
        #  الاستعلام
        Queries += 1
        #qua = 'SELECT ?item WHERE {   VALUES ?occupation { "ar" "ca" "es" "fr" "gl" "he" }  ?item wdt:P31 wd:Q5 .     ?item wdt:P21 wd:' +genderq+ ' .    ?item schema:description "' +translation+ '"@en.  OPTIONAL { ?item schema:description ?itemDe. FILTER(LANG(?itemDe) = ?occupation).  }    FILTER (!BOUND(?itemDe))}'
        qua = 'SELECT ?item WHERE { ?item schema:description "'  + desc+ '"@en.  '
        qua = qua + 'OPTIONAL { ?item schema:description ?de. FILTER(LANG(?de) = "' + targetlang+ '"). } FILTER (!BOUND(?de))'
        qua = qua +  'FILTER NOT EXISTS {?item wdt:P171* wd:Q28319}  } limit 30000'
        #---

        json1 = himoBOT.wd_sparql_generator_url(qua)
        total = len(json1)
        #out = '<<lightgreen>>  *== (Quary: %d/%d; %s:%s:%s;) =='
        #pywikibot.output(out % (Queries, totalqueries, targetlang, genderlabel, desc ))
        #---
        for item in json1:    # عنصر ويكي بيانات
            q = item.title(as_link=False)
            pywikibot.output( '  * action %d/%d "%s"' % ( c , total , q) )
            c += 1
            Action_One_Item(item , desc , taxondescs)
        
                    
if __name__ == "__main__":
    main()
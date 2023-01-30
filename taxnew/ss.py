#!/usr/bin/python
# -*- coding: utf-8  -*-
#
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
from pywikibot import pagegenerators as pg
import occupations as oc
import codecs
from API.maindir import main_dir
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
# start of himoAPI.py file
from API import himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#---
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()

from API.descraptions import Taxon_Descraptions
taxondescs = {  
    'species of insect': Taxon_Descraptions['species of insect'],
    }

desc = 'species of insect'
#---
def wd_from_file(file):
    c = ''
    i = 0
    #---
    with codecs.open(file, "r", encoding="utf-8") as logfile:
        c = logfile.read()
    logfile.close()
    #---
    lines = c.split('\n')
    for line in lines:
        qitem = line[line.find('Q'):line.find(',')]
        #pywikibot.output('line: "%s", qitem: "%s" ' % ( line , qitem)  )
        if (len(qitem)>0):
            wditem=pywikibot.ItemPage(repo,qitem.strip())
            if (not(wditem.isRedirectPage())):
                if wditem.exists():
                    wditem.get(get_redirect=True)
                    yield wditem
                    i += 1
    pywikibot.output('found: "%d" items.' % i  )
#---
def MakeStrDes(NewDesc):
    Newline = ''
    for la in NewDesc:
        test = re.sub( '\'' , '' , NewDesc[la]["value"])
        #sa =  "'" + la + "': " + "{'value': '" + NewDesc[la]['value'] + "', 'language': '" + la + "'},"
        #---
        if test != NewDesc[la]["value"]:
            sa = '"' + la + '": ' + '{"value": "' + NewDesc[la]['value'] + '", "language": "' + la + '"},'
        else:
            sa = "'" + la + "': " + "{'value': '" + NewDesc[la]['value'] + "', 'language': '" + la + "'},"
        Newline = Newline + sa
    data3 = "{'descriptions' :{ " + Newline + "}}"
    return data3
#---
def main():
    pywikibot.output( '<<lightpurple>>------------ main :' )
    file = 'taxnew/' + sys.argv[1] + '.txt'
    json1 = wd_from_file(file)
    print('work with file' + file )
    c = 0
    #tax.action(json1 , desc , taxondescs)
    for item in json1:    # عنصر ويكي بيانات
        q = item.title(as_link=False)
        c += 1
        item.get()
        pywikibot.output( '  * action %d "%s"' % ( c  , q) )
        #---
            #pywikibot.output( '<<lightyellow>>* work 2:' )
        descriptions = item.descriptions
        NewDesc = {}
        addedlangs = []
        q = item.title(as_link=False)
        #---
        for lang in taxondescs[desc].keys():
            if not lang in descriptions.keys():
                #descriptions[lang] = taxondescs[desc][lang]
                NewDesc[lang] = {"language":lang,"value":taxondescs[desc][lang]}
                addedlangs.append(lang)
        #---
        data3 = MakeStrDes(NewDesc)
        #---
        queries_list = [x for x in NewDesc.keys()]
        queries_list.sort()
        dlangs = ','.join(queries_list)
        summary = ('Bot: - Add descriptions: %s' % str(dlangs)) #ملخص العمل
        su = ' ***%s: %s' % (q , str(dlangs))
        #---
        if addedlangs:
            pywikibot.output('* HimoBOT.work_api_desc : '  + str(q) )
            #item.editEntity(data, summary=summary)
            #pywikibot.output(NewDesc)
            try:
                himoAPI.New_Mult_Des_2(q, data3, summary , False)
            except:
                pass
        else:
            pywikibot.output( '  *** no addedlangs')
            
if __name__ == "__main__":
    main()

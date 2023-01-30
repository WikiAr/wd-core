#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

دمج صفحات العزل

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json
import re
import time
import pywikibot
#import Nationalities as aa
import codecs
from API.maindir import main_dir
from datetime import datetime
#---
import sys
#---
import urllib
import urllib
import urllib.request
import urllib.parse

#---
# start of himoAPI.py 
#from API import himoAPI
from API import himoAPI_test as himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#---
# start of himoBOT.py file
from API import himoBOT
#---

categories = {
    "Kategoriya:Mga subdibisyon sa Al Mahrah (lalawigan)" : "تصنيف:عزل محافظة المهرة" , 
    }
#---
def fixkey(key):
    key = re.sub( 'عزلة ' , '', key)
    key = re.sub( '[آأإ]' , 'ا', key)
    key = re.sub( 'ة' , 'ه', key)
    key = re.sub( 'ى' , 'ي', key)
    return key
#---
def getquaary(cat , wiki1, wiki2):
    #---
    qua = 'SELECT (concat(strafter(str(?ss),"/entity/"))  as ?item) ?itemabel ?page ?P131Label\n'
    qua = qua + 'WHERE {\n'
    qua = qua + 'SERVICE wikibase:mwapi {\n'
    qua = qua + 'bd:serviceParam wikibase:api "Generator" .\n'
    qua = qua + 'bd:serviceParam wikibase:endpoint "%s.wikipedia.org" .\n' % str(wiki1)
    #qua = qua + 'bd:serviceParam mwapi:gcmtitle "%s" .' % str(cat)
    #qua = qua + 'bd:serviceParam mwapi:gcmtitle "' + cat + '" .\n'
    qua = qua + 'bd:serviceParam mwapi:gcmtitle "sosososos" .\n'
    qua = qua + 'bd:serviceParam mwapi:generator "categorymembers" .\n'
    qua = qua + 'bd:serviceParam mwapi:gcmprop "ids|title|type" .\n'
    qua = qua + 'bd:serviceParam mwapi:gcmlimit "max" .\n'
    qua = qua + '?page wikibase:apiOutput mwapi:title  .\n'
    qua = qua + '?ns wikibase:apiOutput "@ns" .\n'
    qua = qua + '?ss wikibase:apiOutputItem mwapi:item . }\n'
    qua = qua + 'OPTIONAL {?ss rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .\n'
    qua = qua + 'FILTER NOT EXISTS {?ss wdt:P31 wd:Q6617100.} .\n'
    qua = qua + 'OPTIONAL {?ss wdt:P131 ?P131.} .\n'
    qua = qua + 'FILTER (?ns = "0")\n'
    #if type == 'ar':
    qua = qua + 'FILTER NOT EXISTS {?article schema:about ?ss ;schema:isPartOf <https://%s.wikipedia.org/> .}\n' % wiki2
    #else:
        #qua = qua + '''FILTER NOT EXISTS {?article schema:about ?ss ;schema:isPartOf <https://ar.wikipedia.org/> .} '''
    qua = qua + 'SERVICE wikibase:label {bd:serviceParam wikibase:language "ar,en,fr,de"   } '
    qua = qua + '. }'
    try:
        fao = urllib.parse.quote(qua)
    except:
        fao = urllib.parse.quote(qua)
    #cat = re.sub( ' ' , '_' , cat)
    cat = re.sub( ' ' , '%20' , cat)
    cat = re.sub( ':' , '%3A' , cat)
    fao = re.sub( 'sosososos' , cat , fao)
    return fao
#---
def main2(categories, wiki1, arwiki):
    options = {}
    #---
    listo = {}
    list = {}
    nolenth = {}
    number = 0
    catelenth = len(categories.keys())
    #---
    for category in categories.keys():
        number +=1
        pywikibot.output('<<lightred>> %d/%d start with cat: %s'  % (number ,catelenth , category ) )
        #CategoryID = categories[category]['id']
        #quarry = re.sub( 'Q4117509' , CategoryID , quarry)
        #---
        # التصنيف العربي
        listo[category] = {}
        list[category] = {}
        nolenth[category] = {}
        quarry2 = getquaary(categories[category] , arwiki , wiki1)
        #quarry2 = re.sub( 'YYY' , categories[category], quarry2)
        #quarry2 = re.sub( 'ceb\.wikipedia\.org' , 'ar.wikipedia.org', quarry2)
        #pywikibot.output(quarry2)
        pagelist2 = himoBOT.sparql_generator_url2(quarry2) 
        #pywikibot.output('--------')
        for pp in pagelist2:
            #pywikibot.output(pp)
            if pp['itemabel'] !='':
                #key = re.sub( 'عزلة ' , '', pp['itemabel'])
                key = fixkey(pp['itemabel'])
                list[category][key] = []
                listo[category][key] = []
                #fao = { pp['item'] : {'item': pp['item'] , 'page': pp['page']}}#
                fao = {'item': pp['item'] , 'page': pp['page'] , 'P131Label': pp['P131Label']}
                list[category][key].append(fao)
            else:
                with codecs.open("mer/NoLabel_ar.log.csv", "a", encoding="utf-8") as log_file2:
                    log_file2.write(str(pp))
                    log_file2.close()
        #pywikibot.output('list[category]:--------')
        #pywikibot.output(list[category])
        #---
        # التصنيف الأخر
        quarry = getquaary(category , wiki1, arwiki)
        #pywikibot.output(quarry)

        #quarry = re.sub( 'ar\.wikipedia\.org' , 'ceb.wikipedia.org', quarry)
        pagelist = himoBOT.sparql_generator_url2(quarry) 
        for ppp in pagelist:
            #pywikibot.output(ppp)
            if ppp['itemabel'] !='':
                #key2 = re.sub( 'عزلة ' , '', ppp['itemabel'])
                key2 = fixkey(ppp['itemabel'])
                if not key2 in list[category]:
                    listo[category][key2] = []
                    list[category][key2] = []
                #fao = { ppp['item'] : {'item': ppp['item'] , 'page': ppp['page']}}#
                fao = {'item': ppp['item'] , 'page': ppp['page'] , 'P131Label': ppp['P131Label']}
                if ppp['item'] not in listo[category][key2]:
                    list[category][key2].append(fao)
                else:
                    pywikibot.output( '%s already there' % ppp['item'])
            else:
                with codecs.open("mer/NoLabel_ceb.log.csv", "a", encoding="utf-8") as log_file3:
                    log_file3.write(str(ppp)+ '\n')
                    log_file3.close()
        #---
        pywikibot.output('list[category]:--------')
        num = 0
        lenth = len(list[category].keys())
        #pywikibot.output('list[category].keys():--------\n%s\n----------' % str(list[category].keys()))
        #pywikibot.output(list[category])
        Tao = False
        for ll in list[category]:
            num += 1
            #pywikibot.output('<<lightyellow>>++++\n %d/%d name: %s Merrage: ' % ( num , lenth , ll) )
            cas = list[category][ll]
            #pywikibot.output(cas)
            if len(cas) > 1:
                #if len(cas) > 1:
                Tao = False
                pywikibot.output('<<lightyellow>>++++\n %d/%d name: %s Merrage: ' % ( num , lenth , ll) )
                for lpl in cas:
                    pywikibot.output('item: %s , page: %s, P131: %s' % ( lpl['item'] , lpl['page'] , lpl['P131Label'] ) )
                    #pywikibot.output(lpl)
                #pywikibot.output('Merrage %s to %s ?') 
                if not Tao:
                    ask = pywikibot.input('Merrage %s to %s ?' % (cas[0]['item'] , cas[1]['item']) )
                    if ask == 'a' or ask == 'y' :#or ask == '':
                        Tao = True
                    else:
                        pywikibot.output('wrong answer. "%s"' % ask)
                if Tao:
                    try:
                        himoAPI.Merge( cas[0]['item'], cas[1]['item'])
                    except:
                        pass
                        pywikibot.output('pass')
            else:
                #pywikibot.output('len(cas) %d' % len(cas))
                #pywikibot.output(cas)
                nolenth[category][ll] = cas
        #---
        pywikibot.output('lene: -------- %d.' % len(nolenth[category].keys()))
        #pywikibot.output(nolenth[category].keys() )
        for lene in nolenth[category]:
            with codecs.open("mer/nolenth.log.csv", "a", encoding="utf-8") as logfile2:
                logfile2.write(str(nolenth[category][lene])+ '\n')
                logfile2.close()
        #---
def main():
    if sys.argv and len(sys.argv) > 1:
        if sys.argv[1] == '1':
            main1()
        elif sys.argv[1] == '2':
            main2()
        elif sys.argv[1] == '3':
            main3()
    else:
        pywikibot.output( '<<lightyellow>> no args')
#---
wiki1 = 'ceb'
arwiki = 'ar'
if __name__ == "__main__":
    main2(categories, wiki1, arwiki)
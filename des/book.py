#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف للكتب والقصص


python3 pwb.py des/book optional
python3 pwb.py des/book ask

python pwb.py des/book

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
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
import datetime
import json
#---
from API import printe
import sys
#---
import urllib
import urllib.request
import urllib.parse
#---
from API import himoBOT2
from API import himoBOT
#---
wikidatasite = pywikibot.Site('wikidata', 'wikidata')
repo = wikidatasite.data_repository()
#---
AskSave = { 1 : True }
Qlist = {}

Qlist['Q49084'] = {#قصة قصيرة
    'ar' : 'قصة قصيرة',
    'en' : 'short story',
    'de' : 'Kurzgeschichte',
    'fr' : 'nouvelle',
    'nl' : 'kort verhaal',
    }
Qlist['Q1318295'] = {# قصة
    'ar' : 'قصة' ,
    'en' : 'story' ,
    'de' : 'Erzählung' ,
    'fr' : 'récit' ,
    'nl' : 'verhaal' ,
    }
"""Qlist['Q19389637'] = {# مقالة سيرة ذاتية
                'ar' : 'مقالة سيرة ذاتية' ,
                'en' : 'biographical article' ,
                'de' : 'biographischer Artikel' ,
                'fr' : 'article biographique' ,
                'nl' : 'biografisch artikel' ,
        }"""
Qlist['novel'] = {# رواية
    'ar' : 'رواية' ,
    'en' : 'novel' ,
    'de' : 'Roman' ,
    'fr' : 'roman' ,
    'nl' : 'roman' ,
    }
Qlist['Q1760610'] = {# كتاب هزلي
    'ar' : 'كتاب هزلي' ,
    'en' : 'comic book' ,
    'de' : 'Comicbuch' ,
    'fr' : 'comic book' ,
    'nl' : 'stripboek' ,
    }
Qlist['Q482994'] = {# ألبوم
    'ar' : 'ألبوم' ,
    'en' : 'album' ,
    #'de' : 'Comicbuch' ,
    'fr' : 'album' ,
    #'es' : 'álbum' ,
    'nl' : 'muziekalbum' ,
    }
#---
def logme(q, label):
    verbose = False
    filename = main_dir + "textfiles/name-logs/name.log.csv"
    with codecs.open(filename, "a", encoding="utf-8") as logfile:
        formattedstring = ( '%s\t%s\n' % ( q, label) )
        try:
            logfile.write(formattedstring)
        except Exception as e:
            pywikibot.output( '<<lightred>> Traceback (most recent call last):' )
            pywikibot.output("Error writing to file: %s " % filename )
            pywikibot.output( "<<lightred>> Exception:%s." % e )
            pywikibot.output( 'CRITICAL:' )
            verbose = True    #now I want to see what!
        logfile.close()
    if verbose:
        printe.output(formattedstring)
#---
def action_one_item( Qid, pa, lang, keys):
    item = himoBOT2.Get_Item_API_From_Qid( pa['item'] )
    if item:
        #desc = MakeDesc(Qid, auth, lang)
        #Summary= 'Bot: - Add descriptions: '+ lang
        keys = list(keys)
        keys.sort()
        #---
        if 'en' in keys:
            keys.append('en-gb')
            keys.append('en-ca')
        printe.output('keys:' + str(keys))
        #---
        descriptions = item["descriptions"]
        NewDesc = {}
        addedlangs = []
        #---
        for lang in keys:
            if lang not in descriptions.keys():
                #---
                lang2 = lang
                if lang in ('en-ca', 'en-gb'):
                    lang2 = 'en'
                #---
                des =  MakeDesc(Qid, pa, lang2)
                if des :
                    NewDesc[lang] = {"language":lang,"value": des }
                    dns = ''
                    if 'endes' in pa:
                        dns = pa['endes']
                    printe.output('newar:%s,en:%s' % (des, dns) )
                    addedlangs.append(lang)
                else:
                    printe.output('*no desc for "%s"' % lang)
        #---
        if addedlangs:
            qitem = Qid#item.title(as_link=False)
            if AskSave[1]:
                printe.output('================== + '  + str(addedlangs))
                for lan in NewDesc.keys():
                    printe.output( 'lang:%s, value: "%s"'  % (lan, NewDesc[lan]['value'] ) )
                saaa = pywikibot.input('<<lightyellow>> Add as descriptions? ' )
                if saaa == 'y' or saaa == 'a' or saaa == '':
                    if saaa == 'a':
                        AskSave[1] = False
                    himoBOT.work_api_desc( NewDesc, qitem)
                else:
                    printe.output('* rong answer' )
            else:
                himoBOT.work_api_desc( NewDesc, qitem)
#---
Comma = {
        "an": " y ",
        "ar": "/" ,
        #"ar": "، و" ,
        "ast": " y ",
        "ca": " i ",
        "de": " und ",
        "es": " y ",
        "ext": " y ",
        "fr": " et ",
        "he": " ו",
        "gl": " e ",
        "it": " e ",
        "nl": " en ",
        "oc": " e ",
        "pt": " e ",
        "ro": " și ",
        "sv": " och ",
        'en' : ", ",

    }
Comma2 = {
        'ar' : "، و" ,
        'en' : ", ",
        'de' : ", ",
        'fr' : ", ",
        'nl' : ", "
    }
#---
def GetQuery(Qid, lang, keys):
    #---
    P50 = 'P50'
    if Qid == 'Q482994':
        P50 = 'P175'
    #---
    #sa = ('?item wdt:P136 wd:Q8261 . ?item wdt:P31* wd:Q7725634 .\n')
    sa = ('?item wdt:P31 wd:%s .\n' % Qid )
    if Qid == 'novel':
        sa = ('?item wdt:P136 wd:Q8261 . ?item wdt:P31 wd:Q7725634 .\n')
    #---
    ur = ('SELECT ?item (GROUP_CONCAT(DISTINCT(?auth%s); separator="%s") as ?%s) '% ( lang, Comma[lang],lang ) )
    #---
    for lan in keys:
        if lan != lang:
            ur = ur + ('\n(GROUP_CONCAT(DISTINCT(?auth%s); separator="%s") as ?%s) '% ( lan, Comma[lan], lan ) )
    #---
    ur = ur  + ('WHERE { ?item wdt:%s ?auths .\n' % P50 )+ sa
    #---
    for lan in keys:
        if lan != lang:
            ur = ur + ('OPTIONAL {?auths rdfs:label ?auth%s filter (lang(?auth%s) = "%s")} .\n' % (lan, lan, lan) )
    #---
    if sys.argv and 'optional' in sys.argv:
        ur = ur + (' OPTIONAL { ?auths rdfs:label ?auth%s filter (lang(?auth%s) = "%s") } .' % (lang, lang, lang) )
    else:
        ur = ur + (' ?auths rdfs:label ?auth%s filter (lang(?auth%s) = "%s") .' % (lang, lang, lang) )
    #---
    ur = ur + ('\nOPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "%s")}' % lang )
    ur = ur + 'FILTER(!BOUND(?itemDes))  }\n GROUP BY ?item '
    #---
    #printe.output(ur)
    #---
    return ur
#---
def Gquery2(json1):
    table = {}
    #table = []
    #for head in json1['head']['vars']:
    for result in json1['results']['bindings']:
        q = 'item' in result and result['item']['value'].split('/entity/')[1] or ''
        s = {}
        for se in result:
            s[se] = result[se]['value']
        s['item'] = q
        table[q] = s
    return table
#---
Off = { 1 : 0 }
limit = { 1 : 0 }
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(':')
    #---
    if arg == 'off':
        Off[1] = int(value)
    #---
    if arg == 'limit':
        limit[1] = int(value)
    #---
def wd_sparql_query( query, ddf = False ):
    #---
    New_List = []
    #---
    qua = query
    #---
    if qua == '':
        return New_List
    #---
    #if limit[1] != 0 :
        #query = query + " limit " + str( limit[1] )
    #---
    #wikidatasite=pywikibot.Site('wikidata','wikidata')
    #generator=pg.WikidataSPARQLPageGenerator(query,site=wikidatasite)
    #---
    Keep = True
    offset = 0
    #---
    if Off[1] != 0 :
        offset = Off[1]
    #---
    while Keep:
        #---
        quarry = qua
        #---
        #if ddf:
        if limit[1] != 0 :
            quarry = quarry + "\n limit " + str( limit[1] )
        if offset != 0 :
            quarry = quarry + " offset " + str( offset )
        #else: Off[1] != 0 :
            #quarry = quarry + " offset " + str( Off[1] )
        #---
        #printe.output( quarry )
        #---
        printe.output( 'quarry "%s"' % quarry )
        #---
        generator = himoBOT.sparql_generator_url( quarry )
        #---
        for x in generator:
            New_List.append( x )
        #---
        offset = int( offset + limit[1] )
        #---
        if not generator or generator == [] or "nokeep" in sys.argv :
            Keep = False
        #---
        if not ddf or limit[1] == 0 :
            Keep = False
    #---
    return New_List
#---
def WorkWithOneLang( Qid, lang, keys ):
    printe.output( '*<<lightyellow>> WorkWithOneLang: ')
    #---
    query = GetQuery(Qid, lang, keys)
    #---
    #printe.output(query)
    #---
    PageList = wd_sparql_query( query, ddf = True )
    #---
    printe.output('* PageList: ')
    SAO = Qlist[Qid][lang]
    #---
    total = len(PageList)
    num = 0
    #---
    for pa in PageList:
        #printe.output(pa)
        num += 1
        pa['item'] = pa['item'].split('/entity/')[1]
        printe.output('<<lightblue>>> %s "%s" :%s/%d : %s'  % ( lang, SAO, num, total, pa['item'] ) )
        action_one_item( Qid, pa, lang, keys )
#---
by_list = {
    'ar' : "من تأليف",
    'en' : "by",
    'fr' : "de",
    'de' : "von",
    'nl' : "van",
    'ca' : "per",
    'cs' : "od",
    'la' : "ab",
    'it' : "da",
    'io' : "da",
    'eo' : "de",
    'da' : "af",
    'pl' : "przez",
    'ro' : "de",
    'es' : "por",
    'sv' : "av"
    }
#---
def MakeDesc(Qid, pa, lang):
    #for lang in language:
    #auth
    description = False
    english = ['en-gb', 'en-ca' ]
    if lang in english:
        lang = 'en'
    #---
    if not lang in by_list:
        printe.output('<<lightblue>>> cant find "by" in by_list for lang: "%s"'  % lang )
        return False
    #---
    co = by_list[lang] + ' '
    if (Qid == 'Q482994') and (lang == 'ar'):
        #co = 'ل'
        co = 'من أداء '
    #---
    if (lang in pa) and (pa[lang] != ''):
        auth = pa[lang]
        if auth:
            if lang in Qlist[Qid]:
                    des = Qlist[Qid][lang]
                    d = des                             # الوصف
                    #d = d + ' '                        # الرابط by
                    d = d + ' ' + co     # الرابط by
                    d = d + auth                        # المؤلف
                    #printe.output( 'd' )
                    #printe.output( d )
                    description = d
    #else:
        #description = False
    #---
    if description and lang == "ar" :
        description = description.replace("/", "، و" )
    #---
    if lang == 'ar':
        if description and description != re.sub( '[abcdefghijklmnobqrstuvwxyz]', '', description):
            printe.output( '<<lightred>> arabic description test failed "%s".' % description )
            description = False
    return description
#---
def main():
    #---
    for arg in sys.argv:
        #---
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'save':
            AskSave[1] = False
    #---
    #language = [ 'fr']
    Queries = 0
    printe.output('start with query')
    #logme('Q', 'label')
    #---
    for Qid in Qlist:
        Queries += 1

        keys = Qlist[Qid].keys()
        keys = [ 'ar' ]

        totalqueries = len(Qlist.keys()) * len(Qlist[Qid].keys())
        printe.output('*Qid "%s":'  % Qid )
        out = '<<lightgreen>>  *== Quary:"%s", %d/%d. =='
        printe.output(out % (Qlist[Qid]['ar'], Queries, totalqueries,  ))
        #printe.output( 'lab: "%s". ' % Qlist[Qid]['ar'] )
        for lang in keys:
            #printe.output( Qlist[Qid][lang] )
            WorkWithOneLang( Qid, lang, keys )
#---
test=False
def test():
        printe.output("debug is on")
        Q = 'film'
        #for lang in language:
        keys = Qlist[Q].keys()
        #printe.output( 'lang: "%s" with value: ' % 'fr' )
        WorkWithOneLang( Q, 'ar', keys)
#---
if __name__ == "__main__":
     main()
#---
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
#!/usr/bin/env python3

أوصاف مناطق جغرافية

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot

from API import printe
import codecs
from API.maindir import main_dir
import time
#---
# start of himoBOT.py file
from API import himoBOT2
from API import himoBOT
#---
#from correct import CorrectList
from des.contries2 import ContriesTable2
from des.places import placesTable
from des.done import donelist
#---
bylangs = False#False#True
#---
placesTable["Q29701762"] = {        
        "ar": "مستوطنة"
        }
#---
def check_quarry(qua):
    qua = qua + 'limit 1000'
    json = himoBOT.sparql_generator_url2(qua)
    if json and len(json) != 0:
        return True
    else:
        return False
#---
def log(lang , desc , contry , place):
    fo  = '| {{Q|%s}}|| %s || || {{Q|%s}} \n|-\n' % (place , desc , contry)
    with codecs.open("ydn/log/"+lang+".log.csv", "a", encoding="utf-8") as logfile:
        #try:
            logfile.write(fo)
        #except :
            #printe.output("Error writing")
#---
def logdone(tt , vaa):
    form = 'donelist["%s"] = "%s"\n\n' % (tt,vaa)
    printe.output(form)
    with codecs.open("ydn/done.py", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(str(form))
      except:
            printe.output("<<lightred>>---------------------\n")
            printe.output("<<lightred>> Error writing:")
            printe.output(form)
            printe.output("<<lightred>>---------------------\n")
#---
def action(json1 , topic , translations):
    tatose = translations
    #total = len(json1['results']['bindings'])
    try:
        total = len(json1)
    except:
        total = 0

    c = 1
    #---
    if 'en' in tatose[topic].keys():
        tatose[topic]['en-ca'] = tatose[topic]['en']
        tatose[topic]['en-gb'] = tatose[topic]['en']
    #---
    for item in json1:    # عنصر ويكي بيانات
        q = item.title(as_link=False)
        c += 1
        item.get()
        printe.output( '  * action %d/%d "%s"' % ( c , total , q) )
        #---
            #printe.output( '<<lightyellow>>* work 2:' )
        #---
        descriptions = item.descriptions
        NewDesc = {}
        addedlangs = []
        q = item.title(as_link=False)
        #---
        for lang in tatose[topic].keys():
            if not lang in descriptions.keys():
                #descriptions[lang] = tatose[topic][lang]
                NewDesc[lang] = {"language":lang,"value":tatose[topic][lang]}
                addedlangs.append(lang)
        #---
        if addedlangs:
            printe.output( '<<lightyellow>>* work 2:%s ' % q )
            #printe.output(NewDesc)
            himoBOT.work_api_desc( NewDesc , q)
        else:
            printe.output( '<<lightred>>* work 2 :%s nothing to add.' % q )
#---
def mainfromQuarry( topic , Quarry, translations):
    #printe.output( '*<<lightyellow>> mainfromQuarry:' )
    #Quarry = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q17633526.}'
    json1 = himoBOT2.wd_sparql_generator_url(Quarry)
    action(json1 , topic , translations)
#---
def workOneplace(place , contry , topic , ConTable , placesTable , placenum):
    tras = {}
    tras[topic] = {}
    lenth_place =  len(ConTable) *  len(placesTable)
    tt = tras[topic]
    #---
    newlangs = ['ar']
    #for lang in Comma.keys():
    langs = [x for x in placesTable[place].keys()]
    tras[topic] , newlangs = Make_Des(langs , newlangs , tras[topic] , place , contry , ConTable , placesTable)
    #for lang in placesTable[place]:
        #tras[topic] , newlangs = Make_Des(langs , newlangs , tras[topic] ,  lang , place , contry , ConTable , placesTable)
    #---
    tao = topic
    if 'ar' in tras[topic]:
        tao = tras[topic]['ar']
    elif 'en' in tras[topic]:
        tao = tras[topic]['en']
    #---
    #table = tras[topic]
    qua ='SELECT ?item WHERE {'
    qua = qua + ( '?item wdt:P31 wd:%s.' %  place )
    qua = qua + ( '?item wdt:P17 wd:%s.' %  contry )
    #---
    aaaa = '<<lightred>> %d/%d contry:"%s", place:"%s", tao:"%s". '
    xa =  aaaa % (placenum , lenth_place ,  contry , place  ,tao)
    printe.output(xa)
    if bylangs:
        check = check_quarry(qua + ' }')
        if check:
            for lang in newlangs:
                #qua ='SELECT ?item WHERE {'
                #qua = qua + ( '?item wdt:P31 wd:%s.' %  place )
                #qua = qua + ( '?item wdt:P17 wd:%s.' %  contry )
                Qqua = qua + ('\nFILTER NOT EXISTS {?item schema:description ?des. FILTER((LANG(?des)) = "%s")} . ' % lang)
                Qqua = Qqua + '}'
                #---
                #printe.output(Qqua)
                mainfromQuarry( topic , Qqua, tras)
    else:
        lenth =  len(ConTable) *  len(placesTable)
        printe.output( '*<<lightred>> a > : %d/%d %s:' % (  placenum , lenth , tao ) )
        #if 'ar' in tras[topic]:
            #qua = qua + '\nFILTER NOT EXISTS  {?item schema:description ?des. FILTER((LANG(?des)) = "ar") . '
        #else:
            #qua = qua + '\nFILTER NOT EXISTS  {?item schema:description ?des. FILTER((LANG(?des)) = "en") . '
        qua = qua + '}'
        #---
        #printe.output(qua)
        mainfromQuarry( topic , qua, tras)
        #time.sleep(2)
#---
def workOneplace_ar(place , contry , topic , ConTable , placesTable , placenum):
    tras = {}
    tras[topic] = {}
    lenth_place =  len(ConTable) *  len(placesTable)
    #---
    lang = 'ar'
    #---
    if lang in placesTable[place] and lang in ConTable[contry] :
        tras[topic]['ar'] = placesTable[place][lang] + ' في ' + ConTable[contry][lang]
    #---
    tao = topic
    if 'ar' in tras[topic]:
        tao = tras[topic]['ar']
    #---
    aaaa = '<<lightred>> %d/%d contry:"%s", place:"%s", tao:"%s". '
    xa =  aaaa % (placenum , lenth_place ,  contry , place  ,tao)
    printe.output(xa)
    #---
    Qqua ='SELECT ?item WHERE { ?item wdt:P31 wd:%s. ?item wdt:P17 wd:%s. ' % ( place , contry )
    #---
    Qqua = Qqua + ('\nFILTER NOT EXISTS {?item schema:description ?des. FILTER((LANG(?des)) = "%s")} . }' % lang)
    #---
    mainfromQuarry( topic , Qqua, tras)
#---
def main(ConTable ,placesTable , bylangs):
    tras = {}
    #---
    placenum = 0
    contrynumber = 0
    #langs.sort()
    lenth_all =  len(ConTable) *  len(placesTable)# *  len(langs)
    lenth_contry =  len(ConTable)
    lenth_place =  len(ConTable) *  len(placesTable)
    for contry in ConTable:
        contrynumber += 1
        printe.output( '<<lightyellow>> %d/%d contry:"%s": ' % (contrynumber , lenth_contry , contry) )
        for place in placesTable:
            placenum += 1
            #printe.output( '<<lightblue>> %d/%d contry:"%s", place:"%s": ' % (contrynumber , lenth_place , contry , place) )
            topic = contry + ' ' + place
            #try:
            if place:
                if topic not in donelist:
                    workOneplace_ar(place , contry , topic , ConTable , placesTable , placenum)
                else:
                    printe.output( '%d/%d en_lab "%s" already in donelist.' % (placenum , lenth_place , topic )  )
            #except:
            else:
                pass
#---
def test():
    co1 = {"Q55" : ContriesTable2["Q55"]}
    pT = {"Q44782" : placesTable["Q44782"]}
    main(co1, placesTable, bylangs)
#---
if __name__ == "__main__":
    #test()
    main(ContriesTable2, placesTable, bylangs)
#---

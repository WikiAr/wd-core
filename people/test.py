#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

بوت إضافة الوصوف عن الأشخاص في ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
from new import *

def Main_Test_one_page():
    pywikibot.output( '**<<lightyellow>> Main_Test:')
    import Nationalities as naa
    #---
    QO = {
        #'American': '~ football player', 
        #'Australian': '~ rules footballer', 
        'Albanian': '~ athletics competitor', 
    }
    translations2 = {}
    for natkey in QO:
        occupkey = QO[natkey]
        #---
        occupdic  = oc.translationsOccupations[occupkey]
        natdic  = naa.translationsNationalities[natkey]
        #---
        #translation = 'French politician'
        translation = re.sub('~', natkey, occupkey)
        translations2[re.sub('~', natkey, occupkey)] = {}
        for translang in occupdic.keys():                      # المهن حسب اللغة
            if translang in natdic:
                #pywikibot.output(occupkey + '\t' + natkey + '\t' + translang)
                translations2[re.sub('~', natkey, occupkey)][translang] = {
                    'male': re.sub('~', natdic[translang]['male'], occupdic[translang]['male']), 
                    'female': re.sub('~', natdic[translang]['female'], occupdic[translang]['female']), 
                }
            else:
                pywikibot.output('**<<lightred>> %s translang: "%s" not in {translationsNationalities} "%s"'  % (occupkey ,  translang , natkey) )
    #---
    Qlist = { 
        'male': [ 'Q73319'] # , '' , '', '', '', ''] , 
        #, 'female': [ 'Q30342921' , 'Q30341493' , 'Q30341815', 'Q30346873', 'Q30435693', 'Q30414734']
        ,}
    #---
    for genderlabel , QQ in Qlist.items():
        for q in QQ:
            item = pywikibot.ItemPage(repo, q)
            item.get()
            work2(item , translations2 , translation , genderlabel )
            
import Nationalities as naa

def Main_Test():
    pywikibot.output( '**<<lightyellow>> Main_Test:')
    
    #---
    QO = {
        #'American': '~ football player', 
        #'Australian': '~ rules footballer', 
        'Chinese': '~ journalist', 
    }
    #---Argentinian 
    translations2 = {}
    #occupkey = '~ rules footballer'
    #natkey = 'Australian'
    #---
    #occupkey = '~ politician'
    #natkey = 'French'
    #---
    skipnatkey = ''
    for natkey in QO:
        if natkey != skipnatkey:
            occupkey = QO[natkey]
            #---
            occupdic  = oc.translationsOccupations[occupkey]
            natdic  = naa.translationsNationalities[natkey]
            #---
            #translation = 'French politician'
            translation = re.sub('~', natkey, occupkey)
            translations2[re.sub('~', natkey, occupkey)] = {}
            for translang in occupdic.keys():                      # المهن حسب اللغة
                if translang in natdic:
                    #pywikibot.output(occupkey + '\t' + natkey + '\t' + translang)
                    translations2[re.sub('~', natkey, occupkey)][translang] = {
                        'male': re.sub('~', natdic[translang]['male'], occupdic[translang]['male']), 
                        'female': re.sub('~', natdic[translang]['female'], occupdic[translang]['female']), 
                    }
                else:
                    pywikibot.output('**<<lightred>> %s translang: "%s" not in {translationsNationalities} "%s"'  % (occupkey ,  translang , natkey) )
    #---
    #pywikibot.output( '**<<lightyellow>> translations2:')
    #pywikibot.output( translations2 )
    #---
    c2 = 1
    Queries = 0
    translations_list = list(translations2.keys())
    translations_list.sort()
    totalqueries = len(translations_list) * len(genders_list)# * len(targetlangs) # عدد الاستعلامات للذكور والاناث
    skiptolang = '' #'es'                                                       # لغة يتم تجاهلها 
    skiptogender = '' #'male'                                                 # جنس يتم تجاهله 
    skiptoperson = '' #'American politician'                               # وصف يتم تجاهله
    EndOfQuarry = '}'
    #---
    # 1 -  بدء العمل في  الاستعلامات 
    for translation in translations_list:                   
        #OOutPut( '<<lightblue>>------------\nmain :' )
        OOutPut(translation)
        #---
        #  2 - العمل حسب الجنس ذكر أو أنثى
        for genderq, genderlabel in genders_list:
            #---
            # 3 - العمل حسب اللغة
            for targetlang in translations2[translation].keys():            #q = 'Q30342921' #female
                #targetlang = 'ar'
                #---
                #OOutPut(targetlang + '\t' + genderlabel + '\t' + translation)#, translations2[translation][targetlang][genderlabel])
                #---
                labeeel  = translations2[translation][targetlang][genderlabel]
                out = '<<lightgreen>>  *== Quary:%s, %d/%d; %s:%s. %s=='
                pywikibot.output(out % (translation, Queries, totalqueries, targetlang, genderlabel , str(labeeel) ))
                #  الاستعلام
                Queries += 1
                #qua = 'SELECT ?item WHERE {   VALUES ?occupation { "ar" "ca" "es" "fr" "gl" "he" }  ?item wdt:P31 wd:Q5 .     ?item wdt:P21 wd:' +genderq+ ' .    ?item schema:description "' +translation+ '"@en.  OPTIONAL { ?item schema:description ?itemDe. FILTER(LANG(?itemDe) = ?occupation).  }    FILTER (!BOUND(?itemDe))}'
                qua = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q5 . ?item wdt:P21 wd:' + genderq 
                qua = qua + ' . ?item schema:description "'  + translation+ '"@en.  '
                qua = qua + 'OPTIONAL { ?item schema:description ?de. FILTER(LANG(?de) = "' + targetlang+ '"). } FILTER (!BOUND(?de))'
                #--- عند إزالة السطر السابق يجب إزالة الاستعلام حسب اللغة أعلاه
                qua = qua + EndOfQuarry
                EndOfQuarry =  EndOfQuarry + ' #'
                #---

                json1 = himoBOT.wd_sparql_generator_url(qua)
                #out = '<<lightgreen>>  *== (Quary: %d/%d; %s:%s:%s;) =='
                #OOutPut(out % (Queries, totalqueries, targetlang, genderlabel, translation ))
                #---
                action(json1 , translation , genderlabel , translations2)
                
if __name__ == "__main__":
    Main_Test()
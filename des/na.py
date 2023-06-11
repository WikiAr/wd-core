#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


تسمية  عناصر ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
import codecs
import time
import re
#---

from API import printe
import sys
    
#---
from wd_API import himoAPI_test as himoAPI 
#---
from wd_API import wd_bot
#---
bylangs = False#False#True
#---
limits = { 1: "1000"}
#---
items_done = []
#---
def action( json1 ):
    try:
        total = len(json1)
    except:
        total = 0
    c = 1
    #---
    lang = "ar"
    for tab in json1:    # عنصر ويكي بيانات
        q = tab["item_q"]
        if not q in items_done:
            en_name = tab["en_name"]
            item_en = tab["item_en"]
            ar_lab = tab["ar_name"]
            #---
            kaka =  re.sub(r"[abcdefghijklmnopqrstuvwxyz]" , "" , ar_lab)
            if ar_lab != "" and kaka == ar_lab :
                printe.output( '  * ar_lab:"%s",en_name:"%s"' % (ar_lab  , en_name) )
                c += 1
                printe.output( '  * action %d/%d "%s"' % ( c , total , q) )
                himoAPI.Labels_API( q, ar_lab , "ar" , False, Or_Alii = True)
        else:
            printe.output( ' <<lightred>> * q in items_done. ' % q )
#---
def make_quarry( ar_suff = "", item_p31_cat = "" , en_suff  = "", en_priff  = "") :
    quaaa = '''
#تسمية تصانيف مواليد في
SELECT DISTINCT  #?item ?label ?item_ar
(concat("" , strafter(str(?cat),"/entity/") , "")  as ?item_q)
(concat('%s' , str(?item_ar) )  as ?ar_name)
(concat( str(?item_en)) as ?en_name)
?item_en ?cat_en
WHERE {
    %s
    %s
    FILTER NOT EXISTS {?cat rdfs:label ?catar filter (lang(?catar) = "ar")} .
    ?item rdfs:label ?item_ar filter (lang(?item_ar) = "ar") .
    ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .
    ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .

    BIND( concat("%s" , str(?item_en) , "%s") as ?change_name)
    FILTER ( str(?cat_en) = str(?change_name) )
}
'''
    quaaa = quaaa % ( ar_suff , "%s" , item_p31_cat , en_suff , en_priff ) 
    return quaaa
#---
Quarry = {
    #---
    'items' : '''# تسمية  عناصر طبقاً لاسم التصنيف
SELECT DISTINCT #?item ?label ?cat_ar
(concat("" , strafter(str(?item),"/entity/") , "")  as ?item_q)
(concat( (strafter(str(?cat_ar),"تصنيف:")) )  as ?ar_name)
(concat( str(?item_en)) as ?en_name)
?item_en
?cat_en
WHERE {
    #?item wdt:P31* wd:Q18608583.
    #?item wdt:P31* wd:Q18608583.
    %s
    ?item wdt:P910 ?cat.
    FILTER NOT EXISTS {?item rdfs:label ?itemar filter (lang(?itemar) = "ar")} .
    ?cat rdfs:label ?cat_ar filter (lang(?cat_ar) = "ar") .
    ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .
    ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .

    #BIND( strafter(str(?cat_en),"Category:") as ?change_name)
    #FILTER ( str(?item_en) = str(?change_name) )

    BIND( concat("Category:" , str(?item_en)) as ?change_name)
    FILTER ( str(?cat_en) = str(?change_name) )
}'''
    #---
    ,'from' : make_quarry( 
        ar_suff = "تصنيف:أشخاص من ", 
        item_p31_cat = "?item wdt:P1792 ?cat." , 
        en_suff  = "Category:People from ", 
        )
    #---
    ,'alumni' : make_quarry( 
        ar_suff = "تصنيف:خريجو ", 
        item_p31_cat = "?item wdt:P3876 ?cat." , 
        en_suff  = "Category:", 
        en_priff  = " alumni", 
        )
    #---
    ,'Taken' : make_quarry( 
        ar_suff = "تصنيف:صور التقطت باستخدام ", 
        item_p31_cat = "?item wdt:P2033 ?cat." , 
        en_suff  = "Category:Taken with ", 
        en_priff  = "", 
        )
    #---
    ,'basin' : make_quarry( 
        ar_suff = "تصنيف:حوض ", 
        item_p31_cat = "?item wdt:P1200 ?cat." , 
        en_suff  = "Category:", 
        en_priff  = " basin", 
        )
    #---
    ,'shot' : make_quarry( 
        ar_suff = "تصنيف:أفلام مصورة في ", 
        item_p31_cat = "?item wdt:P1740 ?cat." , 
        en_suff  = "Category:Films shot in ", 
        en_priff  = "", 
        )
    #---
    ,'employees' : make_quarry( 
        ar_suff = "تصنيف:موظفي ", 
        item_p31_cat = "?item wdt:P4195 ?cat." , 
        en_suff  = "Category:", 
        en_priff  = " employees", 
        )
    #---
    ,'faculty' : make_quarry( 
        ar_suff = "تصنيف:هيئة تدريس ", 
        item_p31_cat = "?item wdt:P4195 ?cat." , 
        en_suff  = "Category:", 
        en_priff  = " faculty", 
        )
    #---
    ,'buried' : make_quarry( 
        ar_suff = "تصنيف:مدفونون في ", 
        item_p31_cat = "?item wdt:P1791 ?cat." , 
        en_suff  = "Category:Burials at ", 
        )
    #---
    ,'Births' : make_quarry( 
        ar_suff = "تصنيف:مواليد في ", 
        item_p31_cat = "?item wdt:P1464 ?cat." , 
        en_suff  = "Category:Births in ", 
        )
    #---
    ,'Deaths' : make_quarry( 
        ar_suff = "تصنيف:وفيات في ", 
        item_p31_cat = "?item wdt:P1465 ?cat." , 
        en_suff  = "Category:Deaths in ", 
        )
    #---
    }
Quarry[1] = '''
#تسمية تصانيف طبقاً لاسماء العناصر
SELECT DISTINCT  #?item ?label ?item_ar
(concat("" , strafter(str(?cat),"/entity/") , "")  as ?item_q)
(concat('تصنيف:' , str(?item_ar)  ) as ?ar_name)
(concat( str(?cat_en)) as ?en_name)
?item_en
?cat_en
WHERE {
    ?item wdt:P910 ?cat.
    %s
    #?item wdt:P31/wdt:P279* wd:Q12973014.
    FILTER NOT EXISTS {?cat rdfs:label ?catar filter (lang(?catar) = "ar")} .
    ?item rdfs:label ?item_ar filter (lang(?item_ar) = "ar") .
    ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .
    ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .

    BIND( concat("Category:" , str(?item_en)) as ?change_name)
    FILTER ( str(?cat_en) = str(?change_name) )
}
'''
#---
Quarry["Births2"] = '''
#تسمية تصانيف مواليد في
SELECT DISTINCT  #?item ?label ?item_ar
(concat("" , strafter(str(?cat),"/entity/") , "")  as ?item_q)
(concat('تصنيف:مواليد في ' , str(?item_ar) )  as ?ar_name)
?item_en ?cat_en
(concat( str(?item_en)) as ?en_name)
WHERE {
    %s
    ?item wdt:P1464 ?cat.
    FILTER NOT EXISTS {?cat rdfs:label ?catar filter (lang(?catar) = "ar")} .
    ?item rdfs:label ?item_ar filter (lang(?item_ar) = "ar") .
    ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .
    ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .

    BIND( concat("Category:Births in " , str(?item_en)) as ?change_name)
    FILTER ( str(?cat_en) = str(?change_name) )
}
'''
#---
Quarry["items"] = '''
# تسمية  عناصر طبقاً لاسم التصنيف
SELECT DISTINCT #?item ?label ?cat_ar
(concat("" , strafter(str(?item),"/entity/") , "")  as ?item_q)
(concat( (strafter(str(?cat_ar),"تصنيف:")) )  as ?ar_name)
(concat( str(?item_en)) as ?en_name)
?item_en
?cat_en
WHERE {
    #?item wdt:P31* wd:Q18608583.
    #?item wdt:P31* wd:Q18608583.
    %s
    ?item wdt:P910 ?cat.
    FILTER NOT EXISTS {?item rdfs:label ?itemar filter (lang(?itemar) = "ar")} .
    ?cat rdfs:label ?cat_ar filter (lang(?cat_ar) = "ar") .
    ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .
    ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .

    #BIND( strafter(str(?cat_en),"Category:") as ?change_name)
    #FILTER ( str(?item_en) = str(?change_name) )

    BIND( concat("Category:" , str(?item_en)) as ?change_name)
    FILTER ( str(?cat_en) = str(?change_name) )
}
'''
#---
def main():
    #---
    #python pwb.py des/na
    #python pwb.py des/na Deaths
    #python pwb.py des/na Births 
    #python pwb.py des/na from 
    #python pwb.py des/na alumni 
    #python pwb.py des/na Taken 
    #python pwb.py des/na basin
    #python pwb.py des/na shot 
    #python pwb.py des/na faculty 
    #python pwb.py des/na employees 
    #python pwb.py des/na buried 
    #python pwb.py des/na items
    #python pwb.py des/na -P31:Q515
    #python pwb.py des/na -P31:Q151885
    #python pwb.py des/na items -P31:Q151885
    #python pwb.py des/na items -P31:Q874405
    #python pwb.py des/na -limit:100 items -P31:Q12973014
    #python pwb.py des/na items -P31:Q15221623
    #python pwb.py des/na items -limit:10 lang:fr
    #python pwb.py des/na -limit:1000
    #---
    taxose = ""
    qya = {}
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg =='-limit' :
            printe.output( '<<lightred>>>>  limit ( %s )  ' %  value  )
            limits[1] = value
        #---
        if arg in Quarry :
            printe.output( '<<lightred>>>>  use Quarry:%s . ' % arg)
            qya[arg] = Quarry[arg]
    #---
    if qya == {} : 
        qya = Quarry
    #---
    number = 0 
    for key in qya:
        number += 1
        quuu = qya[key]
        for arg in sys.argv:
            arg, sep, value = arg.partition(':')
            #---
            if arg == 'P31' or arg == '-P31' :
                printe.output( '<<lightred>>>>  P31:%s. ' % value  )
                taxose = "?item wdt:P31/wdt:P279* wd:%s."  % value
            #---
            if arg == 'lang' or arg == '-lang' :
                if value == "fr":
                    quuu = quuu.replace('"en"' , '"fr"' )
                    quuu = quuu.replace('"Category:"' , '"Catégorie:"' )
                    printe.output( '<<lightred>>>> change lang to france. ' )
        #---
        quuu = quuu % taxose
        #---
        if limits[1] != "" : 
            quuu = quuu + '\n LIMIT %s' % limits[1]
        #---
        printe.output("quuu : %d/%d key:%s" %  ( number , len(qya) , key ) ) 
        printe.output(quuu)
        #---
        json1 = wd_bot.sparql_generator_url(quuu)
        action( json1 )
#---
if __name__ == "__main__":
    main()
#---
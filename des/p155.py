#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة تسميات عناصر ويكي بيانات

بناءاً على خاصية سبقه أو تبعه


"""
#
# (C) Ibrahem Qasim, 2022
#
#


import re
import codecs
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
import time
import pywikibot
#---
from API import printe
import sys
#---
import urllib
import urllib.request
import urllib.parse
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
# start of himoAPI.py file
from API import himoAPI_test as himoAPI
#himoAPI.page_put(NewText , summary , title)

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, lab , lang , False, Or_Alii = False)
#himoAPI.Alias_API( Qid, [Alias] , lang , False)
#himoAPI.Merge( q1, q2)
#himoAPI.Sitelink_API( Qid, title , wiki )
#---
Usema = { 1: True }
Ask = { 1: True }
Limit = { 1: "100"}
yes_answer = [ "y" , "a" , "" , "Y" , "A", "all"]
#---
from des.p155tables import cccccups, Mako_keys_4, Mako_keys2, Mako_keys, International_Federation, olympics
#---
from des.p155tables import keys_1, Sports_Keys_Lab,Sports_Keys_Team 
#---
log_done = []
#---
def log( en , ar , type ):
    lio = '"%s":"%s",\n' %  ( en.lower() , ar )
    loogfile = main_dir + "des/labels_to_add.csv.log"
    #---
    if type == "en":
        lio = '%s\n' % en.lower()
        loogfile = main_dir + "des/en_to_find_lab.csv.log"
    #---
    if not en.lower() in log_done or type == "en": 
        if en != "" and ( ar != "" or type == "en" ) : 
            with codecs.open( loogfile, "a", encoding="utf-8") as logfile:
                try:
                    logfile.write( lio )
                    log_done.append( en.lower() )
                except:
                    printe.output("Error writing")
#---
years = "(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)"
tests_en = '[abcdefghijklmnopqrstuvwxyz]'
tests_ar = '[ابتثجحخدذرزسشصضطظعغفقكلمنهويأآإىءئؤة1234567890\–\-\.]'
#---
def make_newlabel( label , ar , en ):
    #---
    printe.output( '<<lightblue>>make_newlabel label:"%s",ar:"%s",en:"%s" ' % ( label , ar , en ) )
    newlabel = ''
    #---
    label = label.lower() + " "
    label = label.replace("' " , " " )
    label = label.replace(" double " , " doubles " )
    label = label.replace(" single " , " singles " )
    label = label.replace(" kilometre " , " kilometres " )
    label = label.replace(" metre " , " metres " )
    label = label.replace(" championship " , " championships " )
    #---
    en = en.lower() + " "
    en = en.replace("' " , " " )
    en = en.replace(" double " , " doubles " )
    en = en.replace(" single " , " singles " )
    en = en.replace(" kilometre " , " kilometres " )
    en = en.replace(" metre " , " metres " )
    en = en.replace(" championship " , " championships " )
    #---
    en2 = en
    if en.find("(") != -1 : 
        en2 = en.lower().split("(")[0]
    #---
    #if re.sub( tests_en , "" , newlabel , flags = re.IGNORECASE ).strip() != newlabel : 
    #if re.sub( tests_ar , "" , newlabel , flags = re.IGNORECASE ).strip() != "" : 
    if en.lower().strip() != "" and ar.lower().strip() != "" : 
        if label.lower().strip() == en.lower().strip() : 
            newlabel = ar
        elif label.find( en.lower() ) != -1  : 
            newlabel = ar + " " + label.replace( en.lower() , '' )
            log( en , ar  , "ar")
        elif en2 != en and label.find( en2 ) != -1  : 
            newlabel = ar + " " + label.replace( en2.lower() , '' )
            log( en2 , ar , "ar")
        else : 
            newlabel = label
    else : 
        newlabel = label
    #---
    printe.output( '<<lightblue>>olympics newlabel:"%s" ' % newlabel )
    #---
    for oll in olympics:
        newlabel = re.sub( oll , olympics[oll] , newlabel , flags = re.IGNORECASE )
    #---
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) time trial' , ' سباق \g<1> ضد الساعة للرجال ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) road race' , ' سباق الطريق \g<1> للرجال ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase' , ' رجال \g<1> متر حواجز خيول ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase' , ' رجال \g<1> متر حواجز خيول ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) hurdles' , ' رجال \g<1> متر حواجز ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m) walk' , ' رجال \g<1> متر مشي ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+)\s*(?:metres|m)' , ' رجال \g<1> متر ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+) metre' , ' رجال \g<1> متر ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+) kg' , ' رجال \g<1> كجم ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' men\'s (\d+|\d+\.\d+) kilometres' , ' رجال \g<1> كيلوجرام ' , newlabel , flags = re.IGNORECASE )
    #---
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m) time trial' , ' سباق \g<1> ضد الساعة للسيدات ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m) road race' , ' سباق الطريق \g<1> للسيدات ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m) steeplechase' , ' سيدات \g<1> متر حواجز خيول ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m) hurdles' , ' سيدات \g<1> متر حواجز ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m) walk' , ' سيدات \g<1> متر مشي ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+)\s*(?:metres|m)' , ' سيدات \g<1> متر ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+) metre' , ' سيدات \g<1> متر ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+) kg' , ' سيدات \g<1> كجم ' , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( ' women\'s (\d+|\d+\.\d+) kilometres' , ' سيدات \g<1> كيلوجرام ' , newlabel , flags = re.IGNORECASE )
    #---
    newlabel = re.sub( ' (\d|\d+|\d+\.\d+) to (\d|\d+|\d+\.\d+) ton' , ' \g<1> إلى \g<2> طن' , newlabel , flags = re.IGNORECASE )
    #---
    #newlabel2 = newlabel
    #---
    for aeo in cccccups :
        newlabel = re.sub( aeo , cccccups[aeo] , newlabel , flags = re.IGNORECASE )
    #---
    for x in Mako_keys:
        newlabel = re.sub( x , Mako_keys[x] , newlabel , flags = re.IGNORECASE )
    #---
    for xx in Mako_keys2:
        newlabel = re.sub( xx , Mako_keys2[xx] , newlabel , flags = re.IGNORECASE )
    #---
    newlabel = re.sub( "at the summer olympics" , "في الألعاب الأولمبية الصيفية" , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( "at the summer youth olympics" , "في الألعاب الأولمبية الشبابية الصيفية" , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( "at the winter youth olympics" , "في الألعاب الأولمبية الشبابية الشتوية" , newlabel , flags = re.IGNORECASE )
    newlabel = re.sub( "at the winter olympics" , "في الألعاب الأولمبية الشتوية" , newlabel , flags = re.IGNORECASE )
    #---
    for aeo in Mako_keys_4:
        newlabel = re.sub( " " + aeo , " " + Mako_keys_4[aeo] , newlabel , flags = re.IGNORECASE )
    #---
    for rrr in International_Federation:
        newlabel = re.sub( " " + rrr , " " + International_Federation[rrr] , newlabel , flags = re.IGNORECASE )
    #---
    for ccc in Sports_Keys_Lab:
        newlabel = re.sub( " " + ccc , " " + Sports_Keys_Lab[ccc] , newlabel , flags = re.IGNORECASE )
    #---
    for hgh in keys_1:
        newlabel = re.sub( " " + hgh , " " + keys_1[hgh] , newlabel , flags = re.IGNORECASE )
    #---
    newlabel = newlabel.replace("  " , " ")
    #---
    #if newlabel2 != newlabel:
        #printe.output( '<<lightblue>> newlabel2:%s, newlabel:"%s" ' % ( newlabel2 , newlabel ) )
    #---
    printe.output( '<<lightblue>> label:%s, newlabel:"%s" ' % ( label , newlabel ) )
    #---
    if newlabel.strip() == "" : 
        printe.output( '<<lightblue>> newlabel = "" ' )
        return ''
    #---
    newlabel = newlabel.strip()
    mat = re.match( "^" + years + "\sفي\s.*" , newlabel )
    if not mat :
        newlabel = re.sub( "^" + years + "\s*(.*)\-(.*)" , "\g<2> \g<1> - \g<3>" , newlabel , flags = re.IGNORECASE ).strip()
        newlabel = re.sub( "^" + years + "\s*(.*)\–(.*)" , "\g<2> \g<1> - \g<3>" , newlabel , flags = re.IGNORECASE ).strip()
        newlabel = re.sub( "^" + years + "\s*(.*)" , "\g<2> \g<1>" , newlabel , flags = re.IGNORECASE ).strip()
    #---
    leb_test = re.sub( tests_ar , "" , newlabel , flags = re.IGNORECASE )
    if leb_test.strip() != "" : 
        printe.output( '<<lightblue>> leb_test(%s) == '' '  % leb_test.strip() )
        log( leb_test.strip() , ''  , "en")
        newlabel = ''
    #---
    newlabel = newlabel.replace("ألعاب أولمبية شتوية" , "الألعاب الأولمبية الشتوية")
    newlabel = newlabel.replace("ألعاب أولمبية صيفية" , "الألعاب الأولمبية الصيفية")
    newlabel = newlabel.replace("  " , " ")
    #---
    return newlabel.strip()
    #---
def Item( item ):
    #---
    q = item['item']
    #---#
    #item[''] = re.sub("shooting at the 2016 summer olympics"  , "" , item['dden'], flags = re.IGNORECASE  )
    item['dden'] = re.sub("(.*) at the (\d+) (Winter|summer) olympics"  , "\g<2> \g<1> at the \g<3> olympics" , item['dden'] , flags = re.IGNORECASE )
    item['label'] = re.sub("(.*) at the (\d+) (Winter|summer) olympics"  , "\g<2> \g<1> at the \g<3> olympics" , item['label'], flags = re.IGNORECASE  )
    item['dden'] = re.sub("(.*) at the (\d+) (Winter|summer) youth olympics"  , "\g<2> \g<1> at the \g<3> youth olympics" , item['dden'] , flags = re.IGNORECASE )
    item['label'] = re.sub("(.*) at the (\d+) (Winter|summer) youth olympics"  , "\g<2> \g<1> at the \g<3> youth olympics" , item['label'], flags = re.IGNORECASE  )
    #---
    lline = ",".join( [ "%s:%s" % ( x , item[x] ) for x in item ] )
    printe.output( lline )
    #---
    en = re.sub("^(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d) "  , "" , item['dden'] , flags = re.IGNORECASE)
    if en == item['dden'] :
        en = re.sub(" (\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)$"  , "" , item['dden'] , flags = re.IGNORECASE)
    en = en.strip()
    #---
    ar = re.sub("^(\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d) "  , "" , item['ddar'] , flags = re.IGNORECASE)
    if ar == item['ddar'] :
        ar = re.sub(" (\d\d\d\d\–\d\d\d\d|\d\d\d\d\-\d\d\d\d|\d\d\d\d\–\d\d|\d\d\d\d\-\d\d|\d\d\d\d)$"  , "" , ar , flags = re.IGNORECASE)
    ar = ar.strip()
    #---
    if Usema[1] :
        if (ar == item['ddar'].strip() and ar.lower().strip() != "" ) or ( en == item['dden'].strip() and en.lower().strip() != "" ) :
            printe.output( "<<lightred>> ar == item['ddar'] or en == item['dden'] " )
            printe.output( "<<lightred>> en:%s,dden:%s " % (en , item['dden']) )
            printe.output( "<<lightred>> ar:%s,ddar:%s " % (ar , item['ddar']) )
            #return ''
            ar = ''
            en = ''
    #---
    label = item['label'].lower()
    #---
    newlabel = make_newlabel( label , ar , en )
    #---
    year = ''
    mat = re.match( ".*" + years + ".*" , item['label'] )
    if mat :
        year = mat.group(1)
    #---
    if newlabel.strip() != '' and year.strip() != "" and newlabel.find( year.strip() ) == -1  : 
        printe.output( "<<lightred>> cant find year:%s, at newlabel (%s) " % ( year , newlabel ) )
        return ''
    #---
    if newlabel.strip() != "" :
        if Ask[1]:
            sa = pywikibot.input('<<lightyellow>>himoAPI: Labels_API Add "%s" as label to "%s"? ([y]es, [N]o):'  % (newlabel,q))
            if sa in yes_answer:
                himoAPI.Labels_API( q , newlabel , "ar" , False , Or_Alii = True)
            if sa == "a" :
                Ask[1] = False
        else:
            himoAPI.Labels_API( q , newlabel , "ar" , False , Or_Alii = True)
    #---
Quarry = {}
Quarry['use'] = ""
Quarry[0] = '''
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
  ?item wdt:P31/wdt:P279* wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item wdt:P3450 ?dd.
  #?dd wdt:P31/wdt:P279* wd:Q8463186.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
}
LIMIT '''
#---
Quarry[1] = '''
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 # ?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item (wdt:P3450|wdt:P361) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
}
LIMIT '''
#---
#python pwb.py des/p155 qua2 P31:Q18536594 limit:1000
Quarry[2]  = '''
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
 #  ?dd wdt:P527 ?item.
  #?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  {
  ?item wdt:P155 ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    } union {
  ?item wdt:P156 ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    }
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
  
}
LIMIT  '''
#---
Quarry[3]  = '''
SELECT DISTINCT ?item ?label
?dden ?ddar
WHERE {
   # ?item2 wdt:P31 wd:Q27020041.
    ?item2 rdfs:label ?ddar filter (lang(?ddar) = "ar") .
    ?item2 rdfs:label ?dden filter (lang(?dden) = "en") .
    { ?item2 wdt:P155 ?item. } union {?item2 wdt:P156 ?item. }
    ?item rdfs:label ?label filter (lang(?label) = "en") .
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
  
} 
LIMIT  '''

#---
Quarry[4]  = '''
SELECT DISTINCT ?item ?label
?dden ?ddar
WHERE {
    #?item2 wdt:P31 wd:Q27020041.
    ?item2 rdfs:label ?ddar filter (lang(?ddar) = "ar") .
    ?item2 rdfs:label ?dden filter (lang(?dden) = "en") .
    { ?item2 wdt:P155 ?item. } union {?item2 wdt:P156 ?item. }
    ?item rdfs:label ?label filter (lang(?label) = "en") .
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
    #sr
} 
LIMIT  '''
#---
#python pwb.py des/p155 qua5 P31:Q18536594 limit:1000
Quarry[5]  = '''
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
 #  ?dd wdt:P527 ?item.
  #?item wdt:P31 wd:Q27020041.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  optional {
  ?item (wdt:P155|wdt:P156) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    }
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
  #sr
  
}
LIMIT  '''
#---
Quarry[6]  = '''
SELECT DISTINCT ?item ?dden ?ddar ?label
WHERE {
 #  values ?dd { wd:Q27792093 }
  ?item wdt:P641 ?p641.
  #?item wdt:P31 wd:Q27020041.
  ?item (wdt:P31|wdt:P361) ?tt.
  #?tt wdt:P31/wdt:P279* wd:Q1344963.
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  ?item (wdt:P156|wdt:P155) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
  FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
#sr

}
LIMIT 
'''
#---
Quarry[7]  = '''
SELECT DISTINCT ?item ?label ?dden ?ddar
WHERE {
    ?item rdfs:label ?label filter (lang(?label) = "en") .
	?item wdt:P31 ?dd.?dd wdt:P279 wd:Q13219666.
  #?item (wdt:P361|wdt:P3450|wdt:P31) ?dd.
  ?dd rdfs:label ?ddar filter (lang(?ddar) = "ar") .
  ?dd rdfs:label ?dden filter (lang(?dden) = "en") .
    #sr
    FILTER NOT EXISTS {?item rdfs:label ?ar filter (lang(?ar) = "ar")} .
} 
LIMIT  '''
#---
Quarry[8]  = '''
SELECT ?item ?ddar ?dden ?label
WHERE {
  ?io wdt:P31 wd:Q27020041.
  ?io p:P3450 ?statement .
  ?statement pq:P155 ?item.
  ?statement pq:P156 ?after.
  ?io rdfs:label ?dden filter (lang(?dden) = "en")
  ?io rdfs:label ?ddar filter (lang(?ddar) = "ar")
  FILTER NOT EXISTS {?item rdfs:label ?ara filter (lang(?ara) = "ar")} .
  ?item rdfs:label ?label filter (lang(?label) = "en") .
  #sr
  
}
LIMIT 
'''
#---
Quarry['use'] = Quarry[2]
#---
def main():
    #---
    #python pwb.py des/p155 qua0 P17:Q145
    #python pwb.py des/p155 qua0 
    #python pwb.py des/p155 qua1
    #python pwb.py des/p155 qua1 sky
    #
    #python pwb.py des/p155 qua8 -limit:400
    #python pwb.py des/p155 qua2 -limit:400
    #python pwb.py des/p155 qua3 -limit:400
    #python pwb.py des/p155 qua4 -limit:400
    #python pwb.py des/p155 -limit:400
    #---
    printe.output( sys.argv )
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'qua0':
            Quarry['use'] = Quarry[0]
            Usema[1] = False
        #---
        if arg == 'qua7':
            Quarry['use'] = Quarry[7]
            Usema[1] = False
        #---
        if arg == 'qua1':
            Quarry['use'] = Quarry[1]
            Usema[1] = False
        #---
        if arg == 'qua2':
            Quarry['use'] = Quarry[2]
        #---
        if arg == 'qua3':
            Quarry['use'] = Quarry[3]
        #---
        if arg == 'qua4':
            Quarry['use'] = Quarry[4]
        #---
        if arg == 'qua5':
            Quarry['use'] = Quarry[5]
        #---
        if arg == 'qua6':
            Quarry['use'] = Quarry[6]
        #---
        if arg == 'qua8':
            Quarry['use'] = Quarry[8]
        #---
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'sky':
            #Quarry['use']  = Quarry['use'].replace("#sr" , "?item (wdt:P3450|wdt:P361) ?P361. ?P361 (wdt:P3450|wdt:P361) wd:Q285389. \n#sr\n" )
            Quarry['use']  = Quarry['use'].replace("#sr" , "?item (wdt:P31|wdt:P361) ?P361. ?P361 (wdt:P31/wdt:P279*|wdt:P361) wd:Q18536594. \n#sr\n" )
        #---
        if arg == 'save':
            Ask[1] = False
            printe.output('<<lightred>> Ask = False.')
        #---
        if arg == '-limit' or arg == 'limit':
            Limit[1] = value
            printe.output('<<lightred>> Limit = %s.' % value )
        #---#
        # python pwb.py des/p155 qua0 P279:Q1079023
        if arg == '-P279':
            tart = "?item wdt:P31/wdt:P279* wd:%s."  % value
            printe.output( 'tart: "%s"' % tart )
            Quarry['use'] = Quarry['use'].replace("#sr" , tart + "\n#sr")
        #---#
        # python pwb.py des/p155 qua2 P31:Q18536594
        elif arg.startswith("P") and value.startswith("Q"):
            tart = "?item wdt:%s wd:%s."  % (arg , value)
            printe.output( 'tart: "%s"' % tart )
            Quarry['use'] = Quarry['use'].replace("#sr" , tart + "\n#sr")
        #---#
    Quaa = Quarry['use'] + Limit[1]
    printe.output( Quaa )
    sparql = himoBOT2.sparql_generator_url(Quaa)
    #---
    Table = {}
    for item in sparql:
        q = item['item'].split("/entity/")[1]
        item['item'] = q
        Table[q] = item
    #---
    num = 0
    for item in Table:
        tabj = Table[ item ]
        num += 1
        printe.output( '<<lightblue>> %d/%d item:"%s" ' % (num ,len(Table.keys() ), item ) )
        Item ( tabj )
    #---
def test():
    #cc = "2010 World Figure Skating Championships - ladies' singles free skating"
    #ar = make_newlabel( cc , '' , '' )
    #ar = make_newlabel( "2020 Volleyball at the Summer olympics" , 'الألعاب الأولمبية الصيفية 2020' , '2020 Summer Olympics' )
    #ar = make_newlabel( "1988 Ski jumping at the Winter olympics – Large hill individual" , '' , '' )
    #ar = make_newlabel( "1998 cross-country skiing at the winter olympics – women's 10 kilometre freestyle pursuit" , '' , '' )
    #ar = make_newlabel( "1964 weightlifting at the summer olympics – men's 82.5 kg" , '' , '' )
    ar = make_newlabel( "2014 world team table tennis championships" , '' , '' )
    #printe.output( cc )
    printe.output( ar )
#---
if __name__ == "__main__":
    if sys.argv and "test" in sys.argv:
        test()
    else:
        main()
    #Item({'ddar': 'بطولة العالم لتنس الطاولة 1932', 'dden': '1932 World Table Tennis Championships', 'item': 'Q203962', 'label': '1933 World Table Tennis Championships (January)'})
    #Item({'ddar': 'بطولة العالم للشطرنج 1975', 'dden': 'World Chess Championship 1975', 'item': 'Q1999918', 'label': 'World Chess Championship 1978'})
#---


#python pwb.py des/p155 qua7 -P279:Q13219666 limit:200
#python pwb.py des/p155 qua4 -P279:Q1344963 limit:200
#python pwb.py des/p155 qua4 -P279:Q1079023 limit:200






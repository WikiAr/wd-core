#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة خواص وتسميات لمقالات العلاقات بين البلدان

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json

import re
import time

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
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

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
from API import himoAPI
#---
from API import himoBOT2
#---
en_labels = {}
Nationalities = {}
#---
from make.Nationality import All_Nat
#---
New_Nat = All_Nat
#New_Nat["جنوبيون أفريقيون"] = "جنوب أفريقيا"
New_Nat["south african2"] = {
        "men":      "جنوبي أفريقي"
        #,"mens":      "جنوبيون أفريقيون"
        ,"mens":      "جنوبيون أفريقيون"
        ,"women":      "جنوبية أفريقية"
        ,"womens":      "جنوبيات أفريقيات"
        ,"en":      "south africa"
        ,"ar":      "جنوب أفريقيا"
      }
New_Nat["central african republic1"] = {
        "men":      "وسط أفريقي"
        ,"mens":      "أفارقة أوسطيون"
        ,"women":      "أفريقية أوسطية"
        ,"womens":      "أفريقيات أوسطيات"
        ,"en":      "Central African Republic"
        ,"ar":      "جمهورية أفريقيا الوسطى"
      }
New_Nat["icelandic_2"] = {
        "men":      "آيسلندي"
        ,"mens":      "آيسلنديون"
        ,"women":      "آيسلندية"
        ,"womens":      "آيسلنديات"
        ,"en":      "iceland"
        ,"ar":      "آيسلندا"
      }
New_Nat["bahamian2"] = {
        "men":      "باهاماسي"
        ,"mens":      "باهاماسيون"
        ,"women":      "باهاماسية"
        ,"womens":      "باهاماسيات"
        ,"en":      "bahamas"
        ,"ar":      "باهاماس"
      }
#---
for x in New_Nat : 
    nam = "ال" + New_Nat[x]["women"]
    #---
    Nationalities[nam] = New_Nat[x]
    
    #---
Nationalities["الوسط أفريقية"] = New_Nat["central african republic1"]
Nationalities["الجنوب أفريقية"] = New_Nat["south african2"]
Nationalities["الأمريكية"] = New_Nat["american"]
Nationalities["الكورية الجنوبية"] = New_Nat["south korean"]
Nationalities["الكورية الشمالية"] = New_Nat["north korean"]
#---
P17Table_Qids = {
    "اسكتلندا": "Q22",
    "فلسطين": "Q23792",
    "تركمانستان": "Q874",
    "غينيا بيساو": "Q1007",
    "الإكوادور": "Q736",
    "أروبا": "Q21203",
    "اليابان": "Q17",
    "سريلانكا": "Q854",
    "مصر": "Q79",
    "ناميبيا": "Q1030",
    "قبرص": "Q229",
    "بولينزيا الفرنسية": "Q30971",
    "ليختنشتاين": "Q347",
    "هونغ كونغ": "Q8646",
    "كوراساو": "Q25279",
    "اليمن": "Q805",
    "دومينيكا": "Q784",
    "الكويت": "Q817",
    "ساموا": "Q683",
    "روسيا": "Q159",
    "سفالبارد ويان ماين": "Q842829",
    "كندا": "Q16",
    "تايلاند": "Q869",
    "البحرين": "Q398",
    "جيرزي": "Q785",
    "جيبوتي": "Q977",
    "فيجي": "Q712",
    "بورتوريكو": "Q1183",
    "تونس": "Q948",
    "غوام": "Q16635",
    "نيكاراغوا": "Q811",
    "القارة القطبية الجنوبية": "Q51",
    "سيراليون": "Q1044",
    "ليبيا": "Q1016",
    "غرينادا": "Q769",
    "تنزانيا": "Q924",
    "ترينيداد وتوباغو": "Q754",
    "جزيرة بوفيه": "Q23408",
    "السنغال": "Q1041",
    "موناكو": "Q235",
    "جزر مارشال": "Q709",
    "موزمبيق": "Q1029",
    "سنغافورة": "Q334",
    "جزر الولايات المتحدة الصغيرة النائية": "Q16645",
    "سوازيلاند": "Q1050",
    "المملكة المتحدة": "Q145",
    "صربيا": "Q403",
    "أوكرانيا": "Q212",
    "فانواتو": "Q686",
    "البرتغال": "Q45",
    "زامبيا": "Q953",
    "طاجيكستان": "Q863",
    "أفغانستان": "Q889",
    "منغوليا": "Q711",
    "السعودية": "Q851",
    "الجبل الأسود": "Q236",
    "جزيرة عيد الميلاد": "Q31063",
    "لاتفيا": "Q211",
    "جورجيا الجنوبية وجزر ساندويتش الجنوبية": "Q35086",
    "بوروندي": "Q967",
    "ألبانيا": "Q222",
    "فنلندا": "Q33",
    "جزر فوكلاند": "Q9648",
    "بوليفيا": "Q750",
    "فرنسا": "Q142",
    "سلوفينيا": "Q215",
    "تشاد": "Q657",
    "الكاميرون": "Q1009",
    "إسبانيا": "Q29",
    "السويد": "Q34",
    "مولدافيا": "Q217",
    "رواندا": "Q1037",
    "جزر العذراء الأمريكية": "Q11703",
    "أرمينيا": "Q399",
    "مالطا": "Q233",
    "جمهورية الكونغو الديمقراطية": "Q974",
    "اليونان": "Q41",
    "جزر القمر": "Q970",
    "الغابون": "Q1000",
    "بنغلاديش": "Q902",
    "جنوب السودان": "Q958",
    "المغرب": "Q1028",
    "جمهورية أفريقيا الوسطى": "Q929",
    "مالي": "Q912",
    "بنما": "Q804",
    "موريتانيا": "Q1025",
    "إندونيسيا": "Q252",
    "نيوزيلندا": "Q664",
    "غوادلوب": "Q17012",
    "رومانيا": "Q218",
    "سيشل": "Q1042",
    "لاوس": "Q819",
    "جزر سليمان": "Q685",
    "كرواتيا": "Q224",
    "جنوب أفريقيا": "Q258",
    "ساو تومي وبرينسيب": "Q1039",
    "غيرنزي": "Q25230",
    "غويانا الفرنسية": "Q3769",
    "فنزويلا": "Q717",
    "إقليم المحيط الهندي البريطاني": "Q43448",
    "أنغولا": "Q916",
    "غواتيمالا": "Q774",
    "كوسوفو": "Q1246",
    "إستونيا": "Q191",
    "ناورو": "Q697",
    "بيرو": "Q419",
    "غانا": "Q117",
    "سانت فينسنت والغرينادين": "Q757",
    "المجر": "Q28",
    "باراغواي": "Q733",
    "ألمانيا": "Q183",
    "كوريا الجنوبية": "Q884",
    "إسرائيل": "Q801",
    "كينيا": "Q114",
    "جزر كايمان": "Q5785",
    "التشيك": "Q213",
    "بولندا": "Q36",
    "إيطاليا": "Q38",
    "باربادوس": "Q244",
    "السودان": "Q1049",
    "تيمور الشرقية": "Q574",
    "جزيرة أيرلندا": "Q22890",
    "الفلبين": "Q928",
    "تركيا": "Q43",
    "هايتي": "Q790",
    "إريتريا": "Q986",
    "سان بيير وميكلون": "Q34617",
    "جامايكا": "Q766",
    "ليبيريا": "Q1014",
    "تونغا": "Q678",
    "النرويج": "Q20",
    "سورينام": "Q730",
    "ميانمار": "Q836",
    "جزر أولاند": "Q5689",
    "تجمع سان مارتين": "Q126125",
    "بوركينا فاسو": "Q965",
    "سانت هيلانة": "Q34497",
    "برمودا": "Q23635",
    "كوريا الشمالية": "Q423",
    "الصحراء الغربية": "Q6250",
    "واليس وفوتونا": "Q35555",
    "أنتيغوا وباربودا": "Q781",
    "فيتنام": "Q881",
    "الصومال": "Q1045",
    "الأرجنتين": "Q414",
    "باكستان": "Q843",
    "سان بارتيلمي": "Q25362",
    "ماكاو": "Q14773",
    "الأوروغواي": "Q77",
    "أذربيجان": "Q227",
    "سلوفاكيا": "Q214",
    "بنين": "Q962",
    "ولايات ميكرونيسيا المتحدة": "Q702",
    "آيسلندا": "Q189",
    "ملاوي": "Q1020",
    "قطر": "Q846",
    "أنغويلا": "Q25228",
    "أوغندا": "Q1036",
    "مايوت": "Q17063",
    "أندورا": "Q228",
    "النمسا": "Q40",
    "لا ريونيون": "Q17070",
    "توغو": "Q945",
    "سانت لوسيا": "Q760",
    "كوبا": "Q241",
    "ساموا الأمريكية": "Q16641",
    "الجزر الكاريبية الهولندية": "Q27561",
    "روسيا البيضاء": "Q184",
    "بروناي": "Q921",
    "بالاو": "Q695",
    "بليز": "Q242",
    "بوتسوانا": "Q963",
    "الجزائر": "Q262",
    "بلجيكا": "Q31",
    "أستراليا": "Q408",
    "الولايات المتحدة": "Q30",
    "غيانا": "Q734",
    "جزر العذراء البريطانية": "Q25305",
    "كازاخستان": "Q232",
    "جمهورية الكونغو": "Q971",
    "مدغشقر": "Q1019",
    "جزيرة هيرد وجزر ماكدونالد": "Q131198",
    "الهند": "Q668",
    "العراق": "Q796",
    "البوسنة والهرسك": "Q225",
    "سينت مارتن": "Q26273",
    "كيريباتي": "Q710",
    "بلغاريا": "Q219",
    "هولندا": "Q55",
    "السلفادور": "Q792",
    "الصين": "Q148",
    "تايوان": "Q865",
    "غامبيا": "Q1005",
    "كاليدونيا الجديدة": "Q33788",
    "زيمبابوي": "Q954",
    "كوستاريكا": "Q800",
    "ليتوانيا": "Q37",
    "إثيوبيا": "Q115",
    "المكسيك": "Q96",
    "لبنان": "Q822",
    "جبل طارق": "Q1410",
    "موريشيوس": "Q1027",
    "نيبال": "Q837",
    "كمبوديا": "Q424",
    "سوريا": "Q858",
    "بوتان": "Q917",
    "جزر كوك": "Q26988",
    "الرأس الأخضر": "Q1011",
    "جورجيا": "Q230",
    "الضفة الغربية وقطاع غزة": "Q407199",
    "هندوراس": "Q783",
    "النيجر": "Q1032",
    "أراض فرنسية جنوبية وأنتارتيكية": "Q129003",
    "لوكسمبورغ": "Q32",
    "سانت كيتس ونيفيس": "Q763",
    "باهاماس": "Q778",
    "الدنمارك": "Q35",
    "أوزبكستان": "Q265",
    "جزر ماريانا الشمالية": "Q16644",
    "الأردن": "Q810",
    "بابوا غينيا الجديدة": "Q691",
    "إيران": "Q794",
    "سلطنة عمان": "Q842",
    "ليسوتو": "Q1013",
    "الإمارات العربية المتحدة": "Q878",
    "نيجيريا": "Q1033",
    "كولومبيا": "Q739",
    "جرينلاند": "Q223",
    "جمهورية الدومينيكان": "Q786",
    "جزر توركس وكايكوس": "Q18221",
    "مونتسرات": "Q13353",
    "غينيا": "Q1006",
    "سويسرا": "Q39",
    "ماليزيا": "Q833",
    "جزيرة مان": "Q9676",
    "غينيا الاستوائية": "Q983",
    "تشيلي": "Q298",
    "قيرغيزستان": "Q813",
    "جزر بيتكيرن": "Q35672",
    "جمهورية مقدونيا": "Q221",
    "البرازيل": "Q155",
    "جزيرة نورفولك": "Q31057",
    "ساحل العاج": "Q1008",
    }
#---
'''
from category.P17 import P17Table
for x in P17Table:
    P17Table_Qids[ P17Table[x]["ar"] ] = P17Table[x]["Q"]
    #pywikibot.output( '   "%s": "%s", ' % ( P17Table[x]["ar"] , P17Table[x]["Q"] )   )
'''
#---
def check( cat_q , property , claims , id , skip = [] , quallprop = "" , quallid = "" ):
    skiptable = ['Q215627' , 'Q19660746' , 'Q18658526' , 'Q1322263' ,'Q12131650' ]
    pywikibot.output('skip:"%s" , id:"%s" '  % (",".join(skip) , id) )
    #for x in P971Table:
        #skiptable.append(P971Table[x]['id'])
    #---
    NoClaim = True
    if property != "" and property in claims:
        pywikibot.output('find ' + property)
        for claim in claims[property]:
            try:
                claim = claim.toJSON()
            except:
                claim = claim
                print("no  toJSON" ) 
            #pywikibot.output( "claim: %s" % str(claim) )
            claimid = claim.get( 'id' , "" )
            va = claim['mainsnak']["datavalue"]
            #pywikibot.output( "va: %s" % str( va ) )
            #---
            if ('value' in va) and ('numeric-id' in va['value']):
                q_value = 'Q' + str(va['value']['numeric-id'])
                pywikibot.output( "<<lightyellow>> q_value: '%s' in cat :'%s'" % (q_value , cat_q) )
                pywikibot.output( claim.get( 'qualifiers' , "qualifiers" ) )
                if q_value == id :
                    pywikibot.output( 'q_value == id:"%s",quallprop:"%s"' % (str(q_value),quallprop) )
                    #---
                    NoClaim = False#
                    if quallprop != "":
                        if claim.get( 'qualifiers' , False ) : 
                            qualifiers = claim.get( 'qualifiers' , False )
                            if quallprop in qualifiers : 
                                NoClaim = False
                            else:
                                pywikibot.output( 'quallprop:"%s" not in Claim qualifiers, return claimid:%s ' % (quallprop , claimid)  )
                                NoClaim = True
                                return claimid
                        else:
                            pywikibot.output( "no qualifiers.., return claimid:'%s'" % claimid )
                            NoClaim = True
                            return claimid
                    #---
                elif q_value in skip:
                    pywikibot.output('<<lightyellow>> q_value in skip ' + ",".join(skip) )
                elif q_value in skiptable:
                    pywikibot.output('<<lightyellow>> q_value in skiptable ' + ",".join(skip) )
                else:
                    pywikibot.output('<<lightred>> %s: q_value "%s" != id "%s"' % ( property , q_value, id ))
                    #log_duplict( cat_q ,property,q_value,id)
                    NoClaim = False
    else:
        pywikibot.output('property not in claims ' + property)
    pywikibot.output( 'NoClaim is %s ' % str(NoClaim) )
    return NoClaim
#---
def Find_Add_Claims(item , property, id , skip = []):   
    q = ""
    claims = {}
    #---
    if property == "" or id == "" :
        pywikibot.output( 'property == "%s", id == "%s" ' % (property, id) )
        return "" 
    #---
    if type( item ) == dict :
        q = item.get("q" , False)
        claims = item["claims"]
    else:
        q = item.title(as_link=False)
        claims = item.claims
    #---
    NoClaim = check(q, property , claims , id , skip=skip)
    #---
    if NoClaim and property != "" :
        #AddClaims(q, property, id )
        id = re.sub( 'Q' , '' , id )
        himoAPI.Claim_API2(q , property , id)  
#---
def Find_Add_Claims_With_Quall( item , property , id , quall_prop , quall_id , claimid = "" ):   
    #if item.get("q" , False) : 
    #pywikibot.output( "type: %s " % str(type({})) )
    if type( item ) == dict :
        q = item.get("q" , False)
        claims = item["claims"]
    else:
        q = item.title(as_link=False)
        claims = item.claims
    #---
    Claimid = claimid
    #---
    q = "Q4115189"
    #---
    #pywikibot.output( claims.get(property , False) )
    #---
    NoClaim = check(q, property , claims , id ,skip="" , quallprop = quall_prop , quallid = quall_id)
    #---
    id = re.sub( 'Q' , '' , id )
    #---
    if type(NoClaim) == str :
        if Claimid == "" or type(Claimid) != str :
            Claimid = NoClaim
    #---
    if NoClaim:
        #AddClaims(q, property, id )
        if Claimid != "" : 
            qua_id = re.sub('Q' , '' , quall_id)
            valueline = {"entity-type": "item" , "numeric-id": qua_id }
            himoAPI.add_quall(Claimid , quall_prop , valueline  ) 
        else:
            Claim_id = himoAPI.Claim_API_With_Quall(q , property , id, quall_prop , quall_id , returnClaimid = True )  
            return Claim_id
    #else:
        #himoAPI.Claim_API_With_Quall(q , property , id, quall_prop , quall_id)  
    #---
P971Table = {}
#---
MainTable = {}
#---
Jobs_key = {
    "صحفيون" : "Q1930187",
    "علماء وراثة" : "Q3126128",
    }
#---#
TEST = { 1 : False  } 
#---
def Add_en_desc( Qid , lab1 , lab2 , itemdescs ):
    #---
    # إضافة وصف إنجليزي
    #---
    if lab1 != "" and lab2 != "" : 
        lab1 = lab1.replace(lab1[0], lab1[0].upper() , 1)
        lab2 = lab2.replace(lab2[0], lab2[0].upper() , 1)
        #---
        en_desc = "Bilateral relations between %s and %s" % ( lab1 ,lab2 )
        if en_desc != "" and itemdescs.get("en"  , "" ) == "" :
            himoAPI.Des_API( Qid , en_desc , "en" )
    else:
        pywikibot.output( 'lab1:%s" or lab2:"%s" == "" .' % ( lab1 , lab2 ) )
    #---
def log( nat , title ):
    form = nat + '\t' + title + '\n'
    pywikibot.output( "log nat:'%s', not in Nationalities" % nat )
    with codecs.open("category/re1.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(form)
      except :
            pywikibot.output("Error writing")
#---
def GetType( title ):
    title = title.replace("_" , " ") 
    MainTitle = title
    pywikibot.output('*GetType for "%s"' % MainTitle)
    #---
    if not MainTitle.startswith("العلاقات "): 
        print("title not start")
        return ""
    #---
    # python pwb.py category/re1 -ref:قالب:علاقات_كوريا_الجنوبية_الخارجية
    # python pwb.py category/re1 -ref:قالب:علاقات_كوريا_الشمالية_الخارجية
    # python pwb.py category/re1 -ref:قالب:علاقات_جنوب_أفريقيا_الخارجية
    # python pwb.py category/re1 -ref:قالب:علاقات_جنوب_السودان_الخارجية
    # python pwb.py category/re1 -ref:قالب:علاقات_جمهورية_أفريقيا_الوسطى_الخارجية
    # python pwb.py category/re1 -ref:قالب:علاقات_شمال_مقدونيا_الخارجية
    # python pwb.py category/re1 -ref:
    # python pwb.py category/re1 -ref:
    # python pwb.py category/re1 -ref:
    # python pwb.py category/re1 -ref:
    # python pwb.py category/re1 -ref:
    #---
    MainTitle = MainTitle.replace("الجنوب أفريقية" , "الجنوب_أفريقية") 
    MainTitle = MainTitle.replace("الكورية الشمالية" , "الكورية_الشمالية") 
    MainTitle = MainTitle.replace("الكورية الجنوبية" , "الكورية_الجنوبية") 
    MainTitle = MainTitle.replace("الجنوب سودانية" , "الجنوب_سودانية") 
    MainTitle = MainTitle.replace("الوسط أفريقية" , "الوسط_أفريقية") 
    MainTitle = MainTitle.replace("الشمال مقدونية" , "الشمال_مقدونية") 
    MainTitle = MainTitle.replace("العلاقات" , "") 
    Table_lab_women = {}
    Table = {}
    parts = MainTitle.strip().split(" ")
    pywikibot.output(",".join(parts))
    #pywikibot.output( cers )
    #---
    if len(parts) == 2 :
        contry1 = parts[0].replace("_" , " " )
        contry2 = parts[1].replace("_" , " " )
        Qids = []
        pywikibot.output( "contry1:%s,contry2:%s" % ( contry1 , contry2 ) )
        for x in parts :#
            x = x.replace("_" , " " )
            Table[x] = { "ar" : "" , "en" : "" , "q" : "" , "women" : "" }
            #---
            ar = ""
            if x in Nationalities:
                pywikibot.output( "x:%s, in  Nationalities" % x )
                Table[x]["ar"] = Nationalities[x]["ar"]
                ar = Nationalities[x]["ar"]
                Table[x]["en"] = Nationalities[x]["en"]
                Table[x]["women"] = Nationalities[x]["women"]
                Table_lab_women[x] = "ال" + Nationalities[x]["women"]
                #---
                if Table_lab_women[x].find(" شمالية") != -1 : 
                    Table_lab_women[x] = Table_lab_women[x].replace(" شمالية" , " الشمالية" )
                #---
                if Table_lab_women[x].find(" جنوبية") != -1 : 
                    Table_lab_women[x] = Table_lab_women[x].replace(" جنوبية" , " الجنوبية" )
                #---
            else:
                log( x ,  title)
                #Table[x]["ar"] = x
                Table[x]["women"] = re.sub("^ال" , "" , x )
                if Table[x]["women"] == x :
                    Table[x]["women"] = ""
            #---
            if ar in P17Table_Qids:
                pywikibot.output( "x:%s,ar in P17Table_Qids:%s" % (ar , P17Table_Qids[ar]  ) )
                Table[x]["q"] = P17Table_Qids[ar]
                Qids.append( P17Table_Qids[ar] )
            else:
                pywikibot.output( "x:%s,ar:%s not in P17Table_Qids." % (x,ar)  )
        #---
        #MainTable[city]['Death'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['Birth'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['People'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['film'] = {'cat': '' , 'cat_id': ''}
        #---
        # إضافة Allai
        ar_desc = ""
        Allai = [ "العلاقات %s %s" % ( contry2 , contry1 ) ]
        #---
        if contry2 not in Table_lab_women or contry1 not in Table_lab_women:
            pywikibot.output( "contry2 not in Table_lab_women or contry1 not in Table_lab_women"  )
            return ''
        #---
        if Table_lab_women[contry2] != "" and Table_lab_women[contry1] != "" :
            Allai.append( "العلاقات %s %s" % ( Table_lab_women[contry2]  , Table_lab_women[contry1]  ) )
            Allai.append( "العلاقات %s %s" % ( Table_lab_women[contry1]  , Table_lab_women[contry2]  ) )
        #---
        #---
        if Table[contry2]["women"] != "" and Table[contry1]["women"] != "" :
            Allai.append( "علاقات %s %s" % ( Table[contry2]["women"] , Table[contry1]["women"] ) )
            Allai.append( "علاقات %s %s" % ( Table[contry1]["women"] , Table[contry2]["women"] ) )
        #---
        if  Table[contry2]["ar"] != "" and Table[contry1]["ar"] != "" :
            ar_desc = "العلاقات الثنائية بين %s و%s" % ( Table[contry1]["ar"] , Table[contry2]["ar"] )
            Allai.append( "علاقات %s و%s" % ( Table[contry1]["ar"] , Table[contry2]["ar"] ) )
            Allai.append( "علاقات %s و%s" % ( Table[contry2]["ar"] , Table[contry1]["ar"] ) )
            #---
            Allai.append( "العلاقات بين %s و%s" % ( Table[contry2]["ar"] , Table[contry1]["ar"] ) )
            Allai.append( "العلاقات بين %s و%s" % ( Table[contry1]["ar"] , Table[contry2]["ar"] ) )
        #---
        # علاقات الأرجنتين وأذربيجان الثنائية
            Allai.append( "علاقات %s و%s الثنائية"  % ( Table[contry2]["ar"] , Table[contry1]["ar"] ) )
            Allai.append( "علاقات %s و%s الثنائية" % ( Table[contry1]["ar"] , Table[contry2]["ar"] ) )
        #---
        #---
        en_title = ""
        en_Allai = ""
        files = []
        #---
        contry1_en = Table[contry1]["en"]
        contry2_en = Table[contry2]["en"]
        #---
        contry1_en = re.sub("^the " , "" , contry1_en.lower().strip() )
        contry2_en = re.sub("^the " , "" , contry2_en.lower().strip() )
        #---
        if contry1_en != "" and contry2_en != "" :
            contry1_en = contry1_en.replace(contry1_en[0], contry1_en[0].upper() , 1)
            contry2_en = contry2_en.replace(contry2_en[0], contry2_en[0].upper() , 1)
      #  if contry1_en != "" and  contry2_en != "":
            #---
            en_title = "%s–%s relations" % ( contry1_en , contry2_en )
            en_Allai = "%s–%s relations" % ( contry2_en , contry1_en )
            #---
            files.append( "%s %s Locator.svg" % ( contry1_en , contry2_en ) ) 
            files.append( "%s %s Locator.svg" % ( contry2_en , contry1_en ) ) 
        #---himoAPI.Claim_API_string( q , property, string )
        Qid = ""
        item = himoBOT2.Get_Item_API_From_Qid( "" , sites = "arwiki" , titles = title , props = "" )
        #---
        if item:
            #---
            Qid = item["q"]
            Add_en_desc( Qid , Table[contry1]["en"] , Table[contry2]["en"] , item["descriptions"] )
            #---
            if Allai != [] : 
                if TEST[1]:
                    pywikibot.output( "Allai:%s"  %  "\n,".join(Allai) )
                else:
                    himoAPI.Alias_API( Qid, Allai , "ar" , False)
            #himoAPI.Add_Labels_if_not_there( Qid, label , lang , ASK = "")
            #---
            P31 = Find_Add_Claims(item , "P31" , "Q15221623" ,skip='') # علاقات ثنائية
            #---
            #if len(Qids) == 2 : 
            for qq in Qids :
                Find_Add_Claims(item , "P17" , qq ,skip = Qids ) # إضافة البلد الأول
              #  P17_2 = Find_Add_Claims(item , "P17" , Qids[1] ,skip = Qids ) # إضافة البلد الثاني
                #---
            Cat_title = "تصنيف:" + title
            Cat_title_en = ""
            Cat_item = himoBOT2.Get_Item_API_From_Qid( "" , sites = "arwiki" , titles = Cat_title , props = "" )
            if Cat_item : 
                Cat_title_en = Cat_item["labels"].get("en"  , "" )
                Cat_q = Cat_item["q"]
                P910 = Find_Add_Claims( item , "P910" , Cat_q ,skip = [] ) # التصنيف الرئيسي للموضوع
                P301 = Find_Add_Claims( Cat_item , "P301" , Qid ,skip = [] ) # الموضوع الرئيسي للتصنيف
            #---
            if Cat_title_en != "" : 
                en_title2 = Cat_title_en.replace( "Category:" , "" )
                if en_title2.lower() != en_title.lower() : 
                    en_Allai = en_title
                    en_title = en_title2
            #---
            if en_title != "" : 
                himoAPI.Add_Labels_if_not_there( Qid, en_title , "en" , ASK = "")
            #---
            en_Allai = re.sub("The " , "" , en_Allai.strip() )
            if en_Allai != "" : 
                himoAPI.Alias_API( Qid, [en_Allai] , "en" , False)
            #---
            if ar_desc != "" : 
                himoAPI.Des_API( Qid , ar_desc , "ar" )
            #---
            # خريطة عامة للموقع
            #for x in files : 
                #himoAPI.Claim_API_string( Qid , "P242" , x )
            #---
            pywikibot.output('* title[%s]: done..' % title )
#---
notinfile_list = []
#---
def main(*args):
    options = {}
    #---
    #lenth = len(pywikibot.handle_args(args))
    #if lenth == 0:
    args = {}
    #---
    #python pwb.py category/re1 -ref:قالب:علاقات_جمهورية_أفريقيا_الوسطى_الخارجية
    #python pwb.py category/re1 -ref:قالب:معلومات_علاقات_ثنائية
    #python pwb.py category/re1 -ref:قالب:معلومات_علاقات_ثنائية notinfile:category/list.txt
    #---
    Table = {}
    List = []
    #---
    notinfile = ""
    file = ""
    argg = False
    University = False
    pywikibot.output('len(sys.argv): %d'% len(sys.argv) )
    #---
    num = 0
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'file' or arg == '-file':
            file = value
        #---
        elif arg == 'notinfile' or arg == '-notinfile':
            notinfile = value
        #---
        elif arg == 'cat' or arg == '-cat':
            vap = value
            vap = vap.replace( "_" , " " )
            List.append( vap )
        #---lntlimit
        elif arg =='quarry' or arg =='-quarry':
            mlist = himoBOT2.getquarry( value )
            for cat in mlist:
                List.append( cat )
    #---
    text3 = ""
    List2 = []
    if file != "" :
        text3 = codecs.open(file, "r", encoding="utf-8").read()
        List2 = [ x.replace( "_" , " " ).strip() for x in text3.split("\n") if x.strip() != ""  ]
    #---notinfile_list
    if notinfile != "" :
        text3 = codecs.open(notinfile, "r", encoding="utf-8").read()
        for x in text3.split("\n"):
            if x.strip() != "" :
                notinfile_list.append( x.replace( "_" , " " ).strip() )
    #---
    for x in List2:
        List.append(  x  )
    #---
        #if arg == 'subcats' or arg == '-subcats':
    if List == [] :
        generator = gent.get_gent(*args)
        
        #---
        for Page in generator:
            title = Page.title(as_link=False)
            #List.append( title )
            num = num + 1
            pywikibot.output( '<<lightyellow>>\n----------\n>> %d>%d > %s << <<' % ( num , len(List) , title) )
            if not title in notinfile_list:
                GetType(title)
    #---
    for MainTitle in List:
        num = num + 1
        pywikibot.output( '<<lightyellow>>\n----------\n>> %d>%d > %s << <<' % ( num , len(List) , MainTitle) )
        if not MainTitle in notinfile_list:
            GetType(MainTitle)
    #---
if __name__ == "__main__":
    #GetType( "العلاقات السويسرية القبرصية" )
    #GetType( "العلاقات السويسرية الفيتنامية" )
    #GetType( "العلاقات الباربادوسية الليختنشتانية" )
    #GetType( "العلاقات الآيسلندية الرومانية" )
    #GetType( "العلاقات الأرجنتينية الباهاماسية" )
    #GetType( "العلاقات الإماراتية العراقية" )
    #GetType( "العلاقات البنغلاديشية التركية" )
    #GetType( "العلاقات_الجنوب_سودانية_السويسرية" )
    #GetType( "العلاقات_الإستونية_الجنوب_سودانية" )
    #GetType( "العلاقات_الإستونية_الجنوب_أفريقية" )
    #GetType( "العلاقات_الأمريكية_الوسط_أفريقية" )
    #---
    #GetType( "العلاقات_الأمريكية_الكورية_الجنوبية" )
    #GetType( "العلاقات_الأمريكية_الكورية_الشمالية" )
    #---
    main()
#---
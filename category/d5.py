#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json
import json as JJson
import re
import time

import pywikibot
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title , arsite.encoding() )
#---
# 
from pywikibot import pagegenerators
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

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.page_put(NewText , summary , title)

#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, lab , lang , False, Or_Alii = False)
#himoAPI.Alias_API( Qid, [Alias] , lang , False)
#himoAPI.Merge( q1, q2)
#himoAPI.wbcreateredirect( From, To)
#himoAPI.Sitelink_API( Qid, title , wiki )
#himoAPI.Remove_Sitelink( Qid , wiki )
#himoAPI.Add_Labels_if_not_there( Qid, label , lang, ASK="")
#---
# start of himoBOT2.py file
from API import himoBOT
from API import himoBOT2
#---
en_labels = {}
#---
P17Table_Qids = {
    "اسكتلندا": "Q22",
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
def log_duplict(item,property,q1,q2):
    form = '|-\n| {{Q|%s}} || {{P|%s}}  || {{Q|%s}}  || {{Q|%s}} ' %  (item,property,q1,q2)
    form = re.sub( '\[\[\:\]\]' , '' , form)
    form = re.sub( '\{\{Q\|\}\}' , '' , form)
    pywikibot.output( 'duplict: ' + str(form) )
    #himoAPI.Merge( q1, q2)
    form = form + '\n'
    with codecs.open("category/log/duplict2.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(form)
      except :
            pywikibot.output("Error writing")
#---
def log(table , type):
    CA = {'CityItem': '' , 'Death': {'cat': '' , 'cat_id': ''} 
    , 'Birth': {'cat': '' , 'cat_id': ''} 
    , 'People': {'cat': '' , 'cat_id': ''}
    }
    pywikibot.output( str(table) )

    #---#University !! UniversityItem !! category
    #form = '|-\n| [[:%s]] || {{Q|%s}} ' %  (table['CityItem'] , table[type+'Item'])
    form = '|-\n| [[:%s]] || {{Q|%s}} ' %  (table[type] , table[type+'Item'])
    if type == 'City':
        keys = [ 'Death' , 'Birth' , 'People']
    else:
        keys = [ 'cat']
    #---
    for key in table:
        if 'cat' in table[key]:
            ta = '|| [[:%s]] || {{Q|%s}} ' % (table[key]['cat'], table[key]['cat_id'])
            form = form + ta
    form = re.sub( '\[\[\:\]\]' , '' , form)
    form = re.sub( '\{\{Q\|\}\}' , '' , form)
    pywikibot.output(str(form) )
    form = form + '\n'
    with codecs.open("category/log/"+type+"2.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(form)
      except :
            pywikibot.output("Error writing")

#---
def getwditem(title, site="ar" ):
    ara = pywikibot.Site(site, "wikipedia") 
    item = ''
    EngPage = pywikibot.Page(ara, title)
    try:
        item = pywikibot.ItemPage.fromPage(EngPage)
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        pywikibot.output('*error when item.get() "%s"' % title)
        return False
#---
def check( cat_q , property , claims , id, skip="", quallprop="", quallid="" ):
    skiptable = ['Q215627' , 'Q19660746' , 'Q18658526' , 'Q1322263' ,'Q12131650' ]
    pywikibot.output('skip:"%s" , id:"%s" '  % (skip , id) )
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
                elif q_value == skip:
                    pywikibot.output('<<lightyellow>> q_value == skip ' + str(skip))
                elif q_value in skiptable:
                    pywikibot.output('<<lightyellow>> q_value in skiptable ' + str(skip))
                else:
                    pywikibot.output('<<lightred>> %s: q_value "%s" != id "%s"' % ( property , q_value, id ))
                    log_duplict( cat_q ,property,q_value,id)
                    NoClaim = False
    else:
        pywikibot.output('property not in claims ' + property)
    pywikibot.output( 'NoClaim is %s ' % str(NoClaim) )
    return NoClaim
#---
def get_qid( tata, CityItem , property):  
    #---
    list = []
    if CityItem:
        claims = CityItem.claims
        if property in claims:
            for claim in claims[property]:
                claim = claim.toJSON()
                va = claim['mainsnak']["datavalue"]
                if ('value' in va) and ('numeric-id' in va['value']):
                    q_value = 'Q' + str(va['value']['numeric-id'])
                    list.append( q_value )
    #---
    if len(list) == 1 : 
        return list[0]
    elif list == [] :
        return False
    #---
    return list
#---
def Find_Add_Claims(item , property, id, skip=''):   
    q = item.title(as_link=False)
    #---
    if property == "" or id == "" :
        pywikibot.output( 'property == "%s", id == "%s" ' % (property, id) )
        return "" 
    #---
    claims = item.claims
    NoClaim = check(q, property , claims , id , skip=skip)
    #---
    if NoClaim and property != "" :
        #AddClaims(q, property, id )
        id = re.sub( 'Q' , '' , id )
        himoAPI.Claim_API2(q , property , id)  
#---
def Find_Add_Claims_With_Quall( item , property , id , quall_prop , quall_id, claimid="" ):   
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
    NoClaim = check(q, property , claims , id, skip="" , quallprop = quall_prop , quallid = quall_id)
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
P971Table['Death']= {
          'cat': 'تصنيف:وفيات في'
        , 'Opposite': 'Birth'
        , 'encat': "Category:Deaths in "
        , 'template': 'قالب:تصنيف_وفيات_في'                             
        , 'P4224_Property': 'P20'                    
        , 'P4224_Q': 'Q5'                        
        , 'P971_id': 'Q18658526'                             #مكان الوفاة
        #, 'P' : 'P971'
        #, 'PName' : 'موضوعان أو أكثر يجمعهما التصنيف'
        , 'Prop' : 'P1465'
        , 'PropName' : 'تصنيف للأشخاص الذين ماتوا هنا'
        , 'Opposite_P1013_Quall' : 'Q21012909'          #ولادة أو وفاة شخص كضد
        }
#---
P971Table['Presidential']= {
          'cat': 'تصنيف:انتخابات رئاسية في'
        ,  'resub': 'تصنيف\:(انتخابات رئاسية|الانتخابات الرئاسية) في'
        , 'Opposite': ''
        , 'encat': "Category:Presidential elections in "
        , 'template': ''                             
        , 'P4224_Property': 'P276'                    
        , 'P4224_Q': 'Q858439'                       #الانتخابات الرئاسية
        , 'P971_id': ''                             #
        #, 'P' : 'P971'
        #, 'PName' : 'موضوعان أو أكثر يجمعهما التصنيف'
        , 'Prop' : ''
        , 'PropName' : ''
        , 'Opposite_P1013_Quall' : ''          #ولادة أو وفاة شخص كضد
        }
#---
P971Table['Birth'] = {
          'cat': 'تصنيف:مواليد في'                            
        , 'Opposite': 'Death'                            
        , 'template': 'قالب:تصنيف_مواليد_في'                  
        , 'encat': "Category:Births in "          
        , 'P4224_Property': 'P19'                    
        , 'P4224_Q': 'Q5'                        
        , 'P971_id': 'Q1322263'                              #مكان الولادة
        , 'Prop' : 'P1464'
        , 'PropName' : 'تصنيف للأشخاص الذين ولدوا هنا'
        , 'Opposite_P1013_Quall' : 'Q21012909'          #ولادة أو وفاة شخص كضد
        } 
P971Table['buried'] = {
          'cat': 'تصنيف:أشخاص دفنوا في'                            
        , 'Opposite': ''                            
        , 'P4224_Property': 'P119'                        # مكان الدفن      
        , 'P4224_Q': 'Q5'                        
        , 'P971_id': 'Q12131650'                             # مكان الدفن      
        , 'Prop' : 'P1791'
        , 'PropName' : 'تصنيف للأشخاص الذين دفنوا هنا'
        } #':
#---
P971Table['People'] = {
          'cat': 'تصنيف:أشخاص من'                            
        , 'Opposite': ''          
        , 'P4224_Property': ''                      #
        , 'P4224_Q': ''                               #        
        , 'P971_id': 'Q19660746'                             #شخص مرتبط بهذا المكان
        , 'Prop' : 'P1792'
        , 'PropName' : 'تصنيف للأشخاص المرتبطين'
        , 'Opposite_P1013_Quall' : ''           #
        }
P971Table['University'] ={                                  #
          'cat': 'تصنيف:أشخاص من'                            
        , 'Opposite': ''                            
        , 'P4224_Property': 'P69'                      #
        , 'P4224_Q': ''                               #
        , 'P971_id': 'Q508719'                            #خريجون
        , 'Prop' : 'P3876'
        , 'PropName' : 'تصنيف الخريجين من المؤسسة التعليمية'
        , 'Opposite_P1013_Quall' : ''           #
        }
#---
P971Table['filmset'] = {                                        #تصنيف:أفلام تقع أحداثها في 
          'cat': 'تصنيف:أفلام تقع أحداثها في'                            
        , 'Opposite': 'filmshot'                            
        , 'P4224_Property': 'P840'                      #موقع السرد
        , 'P4224_Q': 'Q11424'                            #فيلم
        , 'P971_id': 'Q19502208'                             # الخيار الجغرافي للأفلام
        , 'Prop' : 'P1740'
        , 'PropName' : 'تصنيف للأفلام المصورة في هذا المكان'
        , 'Opposite_P1013_Quall' : 'Q21012904'          #filming location and location of film setting
        }
#---
P971Table['filmshot'] = {                                       #تصنيف:أفلام مصورة في 
          'cat': 'تصنيف:أفلام مصورة في'                            
        , 'Opposite': 'filmset'                            
        , 'P4224_Property': 'P915'                      # موقع التصوير
        , 'P4224_Q': 'Q11424'                            #فيلم
        , 'P971_id': 'Q1045481'                             # موقع التصوير
        , 'Prop' : 'P1740'
        , 'PropName' : 'تصنيف للأفلام المصورة في هذا المكان'
        , 'Opposite_P1013_Quall' : 'Q21012904'          #filming location and location of film setting
        }
        
P971Table['s'] ={                                  
          'cat': ''                                 # بداية التصنيف         
        , 'Opposite': ''                            # الجدول الضد     
        , 'P4224_Q': ''                              # عنصر خاصية هي قائمة بـ
        , 'P4224_Property': ''                       # خاصية العنصر 
        , 'P971_id': ''                             # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'Prop' : ''                               # الخاصية الرئيسية للتصنيف
        , 'PropName' : ''                           # اسم الخاصية
        , 'Opposite_P1013_Quall' : ''               # معيار الضد
        }       
#---
def ClaimsToCat(cat_item , CityItem , tata ):   
    pywikibot.output( '<<lightyellow>> ** ClaimsToCat: tata:"%s", cat_item="%s" ' % (tata ,  cat_item ) ) 
    #pywikibot.output(params)
    cat_q = cat_item.title(as_link=False)
    QCityItem = ''
    if CityItem:
        QCityItem = CityItem.title(as_link=False)
    #---
    #pywikibot.output(cat_item)
    Find_Add_Claims(cat_item , 'P971' , P971Table[tata]['P971_id'] , skip = QCityItem)
    #---
    if CityItem:
        Find_Add_Claims(cat_item, 'P971' , QCityItem ,skip=P971Table[tata]['P971_id'] )     #إضافة المدينة إلى تصنيفين أو أكثر
#---
def AddP4224(cat_item , CityItem , tata ):           #هي قائمة بـ
    #if (tata == 'Death') or (tata == 'Birth') or (tata == 'University') or (tata == 'filmset') or (tata == 'filmshot'):
    cao = P971Table[tata]['P4224_Q']
    if cao != '':
        pywikibot.output( '<<lightyellow>> ** AddP4224: ')
        PQuall = P971Table[tata]['P4224_Property']                    # P19 or P20
        if CityItem:#
            QCityItem = CityItem.title(as_link=False)
            Find_Add_Claims_With_Quall(cat_item , 'P4224' , cao  , PQuall , QCityItem)      
        else:
            Find_Add_Claims(cat_item , 'P4224' , cao, skip='')                                 #هي قائمة بـ
#---
def AddOpposite(MainTitle , Cat_item , tata, city , CityItem):#Q21012909
        Opposite = P971Table[tata]['Opposite']
        if Opposite != '' :
            #if (tata == 'Death') or (tata == 'Birth') or (tata == 'filmset') or (tata == 'filmshot'):
            #if tata != 'University' and tata != 'People' and tata != 'buried':
            pywikibot.output( '<<lightyellow>> ** AddOpposite: tata : "%s"'  % tata)
            Property = 'P461'               #الضد
            PQuall = 'P1013'                #المعيار المستخدم
            Pid = P971Table[tata]['Opposite_P1013_Quall']        
            NewCat = ''
            cat = ''
            q_Cat_item = Cat_item.title(as_link=False)
            #---
            NewCatItem = False
            #if tata == 'Death':
            NewCat = P971Table[Opposite]['cat'] + ' ' + city
            '''elif tata == 'Birth':
                NewCat = 'تصنيف:وفيات في ' + city
                Opposite = 'Death'
            elif tata == 'filmset':
                NewCat = 'تصنيف:أفلام مصورة في ' + city
                Opposite = 'filmshot'
            elif tata == 'filmshot':
                NewCat = 'تصنيف:أفلام تقع أحداثها في ' + city
                Opposite = 'filmset'''
            if NewCat !='':
                NewCatItem = getwditem(NewCat)
            #---
            if not NewCatItem:
                q_cc = get_qid( tata , CityItem , P971Table[Opposite]['Prop'] )
                if q_cc:
                    NewCatItem = himoBOT.GetItemFromQid( q_cc )
            #---
            pywikibot.output( ' NewCat: "%s"'  % NewCat)
            if NewCatItem:
                Q_NewCat = NewCatItem.title(as_link=False)
                MainTable[city][Opposite] = {'cat': NewCat , 'cat_id': Q_NewCat}
                pywikibot.output( '<<lightyellow>> **  Opposite for "%s" with value "%s", Q: %s' % (MainTitle , NewCat , Q_NewCat) )
                #Find_Add_Claims(Cat_item , Property , Q_NewCat )
                #---
                himoAPI.Add_Labels_if_not_there( Q_NewCat, NewCat , "ar", ASK="")
                #---
                # إضافة الضد إلى التصنيف القديم
                Find_Add_Claims_With_Quall(Cat_item , Property , Q_NewCat , PQuall , Pid)
                pywikibot.output( '<<lightyellow>> **  Opposite for "%s" with value "%s", Q: %s' % (NewCat , MainTitle , q_Cat_item) )
                #---
                # إضافة الضد إلى التصنيف الجديد
                Find_Add_Claims_With_Quall(NewCatItem , Property , q_Cat_item , PQuall , Pid)
#---
def Death(Cat_item , tata, CityItem, city , MainTitle): 
    pywikibot.output('*%s for "%s"' % (tata , MainTitle) )
    #tata = 'Death'#Death#Birth#People
    #MainTable[city] = {'CityItem': '' , 'Death': {} , 'Birth': {} , 'People': {} }
    MainTable[city][tata] = {'cat': MainTitle , 'cat_id': ''}
    #---
    if Cat_item:
        MainTable[city][tata]['cat_id'] = Cat_item.title(as_link=False)
        if tata  != "Presidential" : 
            ClaimsToCat(Cat_item , CityItem , tata )
        AddP4224(Cat_item , CityItem , tata )
        if P971Table[tata]['Opposite_P1013_Quall'] != "" : 
            AddOpposite(MainTitle , Cat_item , tata, city , CityItem)
    #---
    Prop = P971Table[tata]['Prop']
    PropName = P971Table[tata]['PropName'] 
    if CityItem and Cat_item and Prop != "" :
        MainTable[city][tata+'Item'] = CityItem.title(as_link=False)
        pywikibot.output('* Add "%s" "%s" to CityItem ' % (Prop , PropName ))
        Find_Add_Claims(CityItem, Prop , Cat_item.title(as_link=False), skip='')
        # إضافة تصنيف للأشخاص الذين ماتوا هنا إلى المدينة
    elif Prop == "" :
        pywikibot.output('* Prop == "%s" , PropName: "%s". ' % (Prop , PropName ))
    #---
MainTable = {}
def GetCity(ncity):
    ncity = str(ncity)
    city = ncity
    city = re.sub( '_' , ' ' , city)
    #---
    Cat_is_english = False
    if ncity.startswith("Category:") : 
        Cat_is_english = True
    #---
    for yy in P971Table:
        if Cat_is_english and P971Table[yy].get("encat" , "" ) != "" :
            #---#'encat'
            city = re.sub( P971Table[yy].get("encat" , "" ) , '' , city )
    #---
    for yy in P971Table:
        if P971Table[yy].get("cat" , "" ) != "" : 
            cdf = P971Table[yy].get("cat" , "" )#.replace( "تصنيف:" , "" )
            city = re.sub( cdf , '' , city )
        #---
        if P971Table[yy].get("resub" , "" ) != "" : 
            city = re.sub( P971Table[yy].get("resub" , "" ) , '' , city )
    #---
    city = re.sub( 'تصنيف\:' , '' , city)
    city = re.sub( 'أشخاص من ' , '' , city)
    city = re.sub( 'وفيات في ' , '' , city)
    city = re.sub( 'مواليد في ' , '' , city)
    city = re.sub( 'أفلام تقع أحداثها في ' , '' , city)
    #---
    MainTable[city] = {}
    if Cat_is_english :
        city = city.replace("the " , "" )
        CityItem = getwditem(city, site="en" )
    else:
        CityItem = getwditem(city)
    #---
    pywikibot.output('<<lightred>> city : "%s"' % city)
    #---
    if CityItem:
        pywikibot.output('CityItem :' + CityItem.title() )
        return city , CityItem
    else:
        return city , False
#---
def makejson(property, numeric):
    #---
    if numeric !='':
        numeric = re.sub('Q','',numeric)
        Q = 'Q' + numeric#          
        Pro = {"mainsnak": {
                    "snaktype": "value",
                    "property": property,
                    "datavalue": {
                        "value": {
                            "entity-type": "item",
                            "numeric-id": numeric,
                            "id": Q
                        },
                        "type": "wikibase-entityid"
                    },
                    "datatype": "wikibase-item"
                },
                "type": "statement",
                "rank": "normal"
            }
        #---
        return Pro
#---
def MakeNew( title , en_label4 , tata ):
    js = {}
    data = {}
    data['sitelinks'] = {}
    data['claims'] = {}
    data['claims']['P31'] = [makejson('P31', 'Q4167836')]
    data['labels'] = {}
    data['sitelinks']['arwiki'] = {'site' : 'arwiki' , 'title': title}
    data['labels']['ar'] = {'language' : 'ar' , 'value': title}
    if en_label4 != "" and 'encat' in P971Table[tata] :
        envat = P971Table[tata]['encat'] + en_label4
        data['labels']['en'] = {'language' : 'en' , 'value': envat}
    summary = 'Bot: New item from [[w:ar:%s|arwiki]].' % title
    sao = himoAPI.New_API22(data, summary)
    if 'success' in sao:
        pywikibot.output('<<lightgreen>> ** %s true. ' % summary )
        js = JJson.loads(sao)
        if "entity" in js and "id" in js["entity"]:
            Qid = js["entity"]['id']
            pywikibot.output(' new item is:"%s" .' % Qid)
            return Qid
            #himoAPI.Claim_API2(Qid , 'P971' , pop_q)
            #himoAPI.Claim_API2(Qid , 'P971' , gov_q)  
    else:
        pywikibot.output(sao)
    return False
#---
Jobs_key = {
    "صحفيون" : "Q1930187",
    "علماء وراثة" : "Q3126128",
    }
#---#
from make.Nationality import All_Nat_o3
New_Nat = All_Nat_o3
New_Nat["جنوبيون أفريقيون"] = "جنوب أفريقيا"
New_Nat["سوفييت"] = "الاتحاد السوفيتي"
#---
def work_jobs( MainTitle , x ):
    pywikibot.output('*work_jobs for "%s" , x : %s' % (MainTitle , x ) )
    #---
    Cat_item = himoBOT2.Get_Item_API_From_Qid("", sites="arwiki" , titles = MainTitle )
    job_q = ""
    tata_jobs = x
    nat = re.sub( "تصنيف:%s" % x , '' , MainTitle )
    nat = nat.strip()
    country_qid = ""
    nat_q = False
    #---
    if nat in New_Nat : 
        country_ar = New_Nat[nat]
        if country_ar in P17Table_Qids : 
            country_qid = P17Table_Qids[country_ar]
        #---
        if country_qid == "":
            nat_q = himoBOT2.Get_page_info_from_wikipedia( "arwiki" , country_ar )
        #---
        if country_qid == "" and nat_q : 
            country_qid = nat_q["q"]
        #---
    else:
        pywikibot.output('<<lightred>>* nat "%s" not in  New_Nat' % nat)
    #---
    if x in Jobs_key : 
        job_q = Jobs_key[x]
    #---
    jobs_table = {
          'cat': 'تصنيف:%s' % x                             
        , 'P4224_Property': 'P4224'
        , 'P4224_Q': "Q5"
        , 'quall' : 'P106'
        , 'quall_id' : Jobs_key[x]
        , 'PropName' : 'يحتوي التصنيف على'
        }
    #---
    Q5 = jobs_table['P4224_Q']
    #---
    claim_id = ""
    if tata_jobs : 
        pywikibot.output('<<lightblue>>* tata_jobs is "%s"' % tata_jobs)
        #---
        P4224 = jobs_table['P4224_Property']

        #---
        if Cat_item:  
        #---
            if Q5 != '':
                claim_id = Find_Add_Claims_With_Quall( Cat_item , 'P4224' , Q5 , jobs_table['quall'] , jobs_table['quall_id'] )      
        #---        #---
        pywikibot.output('* MainTable[%s]: done..' % tata_jobs )
    #---
    if country_qid != "" : 
        pywikibot.output('<<lightblue>>* nat is "%s" , country_qid is "%s"' % ( nat , country_qid ) )
        if Cat_item:  
        #---
            if Q5 != '':
                Find_Add_Claims_With_Quall( Cat_item , 'P4224' , Q5 , "P27" , country_qid , claimid = claim_id )      
        #---        #---
        pywikibot.output('* MainTable[%s]: done..' % tata_jobs )
    #---
def GetType( MainTitle ):
    pywikibot.output('*GetType for "%s"' % MainTitle)
    not_Jobbs = True
    #---
    site = "ar"
    Cat_is_english = False
    if MainTitle.startswith("Category:") : 
        Cat_is_english = True
        site = "en"
    #---
    if MainTitle !='':
        job_q = ""
        tata_jobs = ""
        for x in Jobs_key:
            if MainTitle.startswith("تصنيف:%s" % x ) : 
                not_Jobbs = False
                work_jobs( MainTitle , x)
    #---
    if not_Jobbs:
        city , CityItem = GetCity(MainTitle)
        Cat_item = getwditem(MainTitle , site = site)
        MainTitle = str(MainTitle)
        #---
        tot = MainTitle#re.sub( '_' , ' ' , MainTitle )
        DeathTest = re.sub( 'تصنيف:وفيات' , '' , tot )
        BirthTest = re.sub( 'تصنيف:مواليد' , '' , tot )
        PeopleTest = re.sub( 'تصنيف:أشخاص' , '' , tot )
        filmsetTest = re.sub( 'تصنيف:أفلام تقع أحداثها في' , '' , tot )
        filmshotTest = re.sub( 'تصنيف:أفلام مصورة في' , '' , tot )
        #---
        MainTable[city] = {'City': city , 'CityItem': '' }
        #MainTable[city]['Death'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['Birth'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['People'] = {'cat': '' , 'cat_id': ''}
        #MainTable[city]['film'] = {'cat': '' , 'cat_id': ''}
        #---
        tata = False
        #---
        en_label4 = ""
        ar_label = ""
        if CityItem:
            qo = CityItem.title(as_link=False)
            tabd = himoBOT2.Get_Sitelinks_from_qid( ssite = "" , ids = qo )
            #pywikibot.output( table6 )
            if "sitelinks" in tabd:
                #pywikibot.output( tabd["sitelinks"] )
                if "enwiki" in tabd["sitelinks"]:
                    en_labelff = tabd["sitelinks"]["enwiki"]
                    if en_labelff != "Ashland, Oregon" :
                        en_label4 = en_labelff
                        en_labels[city] = tabd["sitelinks"]["enwiki"]
                        pywikibot.output('* en_label "%s"' % en_label4)
                if "arwiki" in tabd["sitelinks"]:
                        ar_label = tabd["sitelinks"]["arwiki"]
                        pywikibot.output('* ar_label "%s"' % ar_label)
                else:
                    if "labels" in tabd and "ar" in tabd["labels"]:
                            ar_label = tabd["labels"]["ar"]
        #---
        #if Cat_item:
        if DeathTest != MainTitle:
            tata = 'Death'
        elif BirthTest != MainTitle:
            tata = 'Birth' 
        elif PeopleTest != MainTitle:
            tata = 'People' 
        elif filmsetTest != MainTitle:
            tata = 'filmset' 
        elif filmshotTest != MainTitle:
            tata = 'filmshot' 
        #else:
            #pywikibot.output('* No Cat item. for "%s"' % MainTitle)
        #---
        for yy in P971Table:
            if not tata and P971Table[yy].get("cat" , "" ) != "" : 
                faTest = re.sub( P971Table[yy].get("cat" , "" ) , '' , MainTitle )
                if faTest != MainTitle:
                    tata = yy
                #---#'encat'
                if P971Table[yy].get("resub" , "" ) != "" : 
                    faTest2 = re.sub( P971Table[yy].get("resub" , "" ) , '' , MainTitle )
                    if not tata and faTest2 != MainTitle:
                        tata = yy
                #---#'encat'
                if Cat_is_english and P971Table[yy].get("encat" , "" ) != "" : 
                    faTest4 = re.sub( P971Table[yy].get("encat" , "" ) , '' , MainTitle )
                    if not tata and faTest4 != MainTitle:
                        tata = yy
        #---
        if not tata:
            pywikibot.output("* Can't get the cate type. for '%s'" % MainTitle)
        #---
        if tata : 
            pywikibot.output('<<lightblue>>* tata is "%s"' % tata)
            #---
            if P971Table[tata]['cat'] != "" :
                if Cat_is_english and Cat_item and ar_label != "" :
                    ar_label = P971Table[tata]['cat'].strip() + " " + ar_label
                    if type(Cat_item) != dict:
                        labels4 = Cat_item.labels
                        qqq = Cat_item.title(as_link=False)
                    else:
                        labels4 = Cat_item.get("labels" , False)
                        qqq = Cat_item.get("q" , False)
                    if labels4 : 
                        if not "ar" in labels4:
                            pywikibot.output('* ar_label "%s"' % ar_label)
                            himoAPI.Add_Labels_if_not_there( qqq , ar_label , "ar", ASK="")
            #---
            if not Cat_item:
                property = P971Table[tata]['Prop']
                cc = get_qid( tata , CityItem  , property )
                if cc:
                    q = himoAPI.Sitelink_API( cc, MainTitle , "arwiki" )
                    himoAPI.Add_Labels_if_not_there( cc, MainTitle , "ar", ASK="")
                else:
                    q = MakeNew( MainTitle , en_label4 , tata )
                Cat_item = getwditem( MainTitle , site = site )
            #---
            MainTable[city][tata] = {'cat': '' , 'cat_id': ''}
            Death(Cat_item , tata , CityItem , city , MainTitle)
            #---
            pywikibot.output('* MainTable[%s]: done..' % tata )
            #log(MainTable[city] , tata)
#---
def University(Cat_item, UniItem, Uni , MainTitle): 
    tata = 'University'
    pywikibot.output('*%s for "%s"' % (tata , MainTitle) )
    #---
    #if Cat_item:
    ClaimsToCat(Cat_item , UniItem , tata )
    #AddP4224(Cat_item , UniItem , tata )
    #AddOpposite(Cat_item , tata, Uni)
    #---
    #if UniItem and Cat_item:
    if UniItem:
        MainTable[Uni]['UniversityItem'] = UniItem.title(as_link=False)
        pywikibot.output('* Add "%s" "%s" to UniItem ' % (P971Table[tata]['Prop'] , P971Table[tata]['PropName'] ))
        Find_Add_Claims(UniItem, P971Table[tata]['Prop'] , Cat_item.title(as_link=False) )    
#---
def univer(MainTitle):
    pywikibot.output('*univer for "%s"' % MainTitle)
    MainTitle = str(MainTitle)
    if MainTitle !='':
        Uni = str(MainTitle)
        Uni = re.sub( '_' , ' ' , Uni)
        Uni = re.sub( 'تصنيف\:خريجو ' , '' , Uni)
        pywikibot.output('<<lightred>> Uni : "%s"' % Uni)
        #---
        if Uni != MainTitle:
            MainTable[Uni] = {'University': Uni , 'UniversityItem': '', 'category' : {} }
            MainTable[Uni]['category'] = {'cat': MainTitle , 'cat_id': ''}
            UniItem = getwditem(Uni)
            Cat_item = getwditem(MainTitle)
            #---
            if Cat_item:
                MainTable[Uni]['category'] = {'cat': MainTitle , 'cat_id': Cat_item.title(as_link=False)}
                University(Cat_item , UniItem , Uni , MainTitle)
            else:
                pywikibot.output('* No Cat item. for "%s"' % MainTitle)
        else:
            pywikibot.output('* Can\' get the cate type. for "%s"' % MainTitle)
        #---
        pywikibot.output('* MainTable[Uni]:' )
        log(MainTable[Uni] , 'University')
        #---
def list_template_usage():
    arsite = pywikibot.Site("ar", "wikipedia")
    tmpl_name = 'نتيجة_سباق_الدراجات/بداية'
    name = "{}:{}".format(arsite.namespace(10), tmpl_name)
    tmpl_page = pywikibot.Page(arsite, name)
    ref_gen = pagegenerators.ReferringPageGenerator(tmpl_page, onlyTemplateInclusion=True)
    filter_gen = pagegenerators.NamespaceFilterPageGenerator(ref_gen, namespaces=[0])
    generator = arsite.preloadpages(filter_gen, pageprops=True)
    return generator
#---
def log2(s):
    with codecs.open("category/log/d5.log.csv", "a", encoding="utf-8") as logfile:
      try:
            logfile.write(s)
      except :
            pywikibot.output("Error writing")
#---
head = '{|\n|-\n!city !! CityItem !! Death !! Death_id !! Birth !! Birth_id !! People !! People_id'
Unhead = '{|\n|-\n!University !! UniversityItem !! category !! categoryitem'
def main(*args):
    options = {}
    #---
    #lenth = len(pywikibot.handle_args(args))
    #if lenth == 0:
    args = {}
    #args = {'-ref:قالب:تصنيف_وفيات_في' , '-ns:14'}
    #args = {'-ref:قالب:تصنيف_مواليد_في' , '-ns:14'}
    #---
    #python pwb.py category/d5 Presidential
    #python pwb.py category/d5 jobs
    #python pwb.py category/d5 birth3
    #python pwb.py category/d5 death3
    #python pwb.py category/d5 death
    #python pwb.py category/d5 quarry:280463
    #python pwb.py category/d5 cat:تصنيف:علماء_وراثة_اسكتلنديون
    #python pwb.py category/d5 -subcats:تصنيف:علماء_وراثة_حسب_الجنسية
    #python pwb.py category/d5 cat:تصنيف:وفيات_في_ونزر_\(باركشير\)
    #python pwb.py category/d5 cat:تصنيف:وفيات_في_أوستر_\(سويسرا\)
    #python pwb.py category/d5 cat:تصنيف:وفيات_في_ونزر_(باركشير)
    #---
    Table = {}
    Table["death3"] = 'category/file/d.txt'
    Table["birth3"] = 'category/file/p.txt'
    Table["death"] = 'category/file/death.txt'
    Table["death2"] = 'category/file/death2.txt'
    Table["birth2"] = 'category/file/birth2.txt'
    Table["birth"] = 'category/file/birth.txt'
    Table["people"] = 'category/file/people.txt'
    Table["people2"] = 'category/file/people2.txt'
    Table["people3"] = 'category/file/people3.txt'
    Table["filmset"] = 'category/file/filmset.txt'
    Table["filmshot"] = 'category/file/filmshot.txt'
    Table["jobs"] = 'category/file/jobs.txt'
    Table["Presidential"] = 'category/file/Presidential.txt'
    Table["Presidential1"] = 'category/file/Presidential1.txt'
    #---
    List = []
    #---
    file = ""
    argg = False
    University = False
    pywikibot.output('len(sys.argv): %d'% len(sys.argv) )
    #---
    if sys.argv and len(sys.argv) > 1:
        argg = True
        pywikibot.output(sys.argv)
        if sys.argv[1] == 'univer':
            #args = {'-catr:خريجون_حسب_الجامعة_أو_الكلية_في_اليمن' , '-ns:14'}
            args = {'-file:category/file/University.txt'}
            University = True
        #---
        elif sys.argv[1] in Table:
            file = Table[sys.argv[1]]
        #---
        elif sys.argv[1] == 'test':
            TestMain()
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == 'cat' or arg == '-cat':
            vap = value
            vap = vap.replace( "_" , " " )
            List.append( vap )
        #---lntlimit
        if arg =='quarry' or arg =='-quarry':
            mlist = himoBOT2.getquarry( value )
            for cat in mlist:
                List.append( cat )
        #---
        if arg =='subcats' or arg =='-subcats':
            generator = gent.get_gent(*args)
        
            for Page in generator:
                title = Page.title(as_link=False)
                List.append( title )
        #---
    text3 = ""
    List2 = []
    if file != "" :
        text3 = codecs.open(file, "r", encoding="utf-8").read()
        List2 = [ x.replace( "_" , " " ).strip() for x in text3.split("\n") if x.strip() != ""  ]
    #---
    if List2:
        for x in List2:
            if x.find("تصنيف:") != -1:
                xp = "تصنيف:" + x.split("تصنيف:")[1]
                List.append(  xp  )
            elif x.find("Category:") != -1:
                xp = "Category:" + x.split("Category:")[1]
                List.append(  xp  )
    #---
    num = 0
    if List:
        if University:
            log2(Unhead)
        else:
            log2(head)
        #---
        for MainTitle in List:
            num = num + 1
            #text = page.text
            #start(text, title)
            #try:   #start(text, title)
            pywikibot.output( '<<lightyellow>>\n----------\n>> %d >> %s << <<' % ( num , MainTitle) )
            #---
            if University:
                univer(MainTitle)
            else:
                GetType(MainTitle)
        #---
        log2('\n|}\n\n')
#---
def TestMain():
    pywikibot.output( '<<lightyellow>> **TestMain: ')
    #pywikibot.output(skiptable)
    item = getwditem('تصنيف:وفيات_في_ونزر_(باركشير)')
    #log2(head)
    page = ''
    #univer(page , 'تصنيف:خريجو_جامعة_العلوم_والتكنولوجيا_(اليمن)')
    #GetType(page , 'تصنيف:وفيات في ندولا')
    #---
    if item:
        Q = item.title(as_link=False)
        Find_Add_Claims(item , 'P971', 'Q234453', skip='Q19660746')
    #---
    #log2('\n|}\n\n')
#---
if __name__ == "__main__":
    main()
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import json as JJson
import re
import time
import pywikibot
#import Nationalities as aa
import codecs
from datetime import datetime
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse

#---
site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
from API import himoAPI
#---
#from item_table import itemTable
itemTable = {}
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
def MakeNew(category, pop_q , gov_q , arlabel):
    js = {}
    data = {}
    data['sitelinks'] = {}
    data['claims'] = {}
    data['claims']['P31'] = [makejson('P31', 'Q4167836')]
    #data['claims']['P971'] = [makejson('P971', gov_q) , makejson('P971', pop_q)]
    data['labels'] = {}
    data['sitelinks']['cebwiki'] = {'site' : 'cebwiki' , 'title': category}
    data['labels']['ar'] = {'language' : 'ar' , 'value': arlabel}
    data['labels']['ceb'] = {'language' : 'ceb' , 'value': category}
    summary = 'Bot: New item from [[w:ceb:%s|cebwiki]].' % category
    sao = himoAPI.New_API22(data, summary)
    if 'success' in sao:
        pywikibot.output('<<lightgreen>> ** %s true. ' % summary )
        #pywikibot.output(sao)
        #try:
        js = JJson.loads(sao)
        #except:
            #pywikibot.output('Error downloading SPARQL? Malformatted JSON? Skiping\n')
        if "entity" in js and "id" in js["entity"]:
            Qid = js["entity"]['id']
            pywikibot.output(' new item is:"%s" .' % Qid)
            #himoAPI.Claim_API2(Qid , 'P31' , 'Q4167836')
            himoAPI.Claim_API2(Qid , 'P971' , pop_q)
            himoAPI.Claim_API2(Qid , 'P971' , gov_q)  
    else:
        pywikibot.output(sao)
#---
def getwditem(title):
    ara = pywikibot.Site("ceb", "wikipedia") 
    EngPage = pywikibot.Page(ara, title)
    item = ''
    #---
    try:
        if title in itemTable :
            item = pywikibot.ItemPage(repo, itemTable[title])
        else:
            item = pywikibot.ItemPage.fromPage(EngPage)
        #---
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    except:
        #pywikibot.output('*error when item.get() "%s"' % title)
        return False
#---
def check(q, property , claims , id ,skip=''):
    skiptable = ['Q215627' , 'Q19660746' , 'Q18658526' , 'Q1322263' ,'Q12131650' ]
    #for x in P971Table:
        #skiptable.append(P971Table[x]['id'])
    #---
    NoClaim = True
    if property in claims:
        pywikibot.output('find ' + property)
        for claim in claims[property]:
            claim = claim.toJSON()
            va = claim['mainsnak']["datavalue"]
            if ('value' in va) and ('numeric-id' in va['value']):
                q_value = 'Q' + str(va['value']['numeric-id'])
                if q_value == id :
                    #pywikibot.output('q_value == id ' + str(q_value))
                    NoClaim = False
                elif q_value == skip:
                    pywikibot.output('q_value == skip ' + str(skip))
                elif q_value in skiptable:
                    pywikibot.output('q_value in skiptable ' + str(skip))
                else:
                    pywikibot.output('%s: q_value "%s" != id "%s"' % ( property , q_value, id ))
                    #log_duplict(q,property,q_value,id)
                    NoClaim = False
    return NoClaim
#---
def Find_Add_Claims(item , property, pop_q , gov_q , arlabel):   
    q = item.title(as_link=False)
    #---
    claims = item.claims
    labels = item.labels
    if not 'ar' in labels:
        himoAPI.Labels_API( q, arlabel , 'ar'  , False)
    #---
    if not 'P31' in claims:
        himoAPI.Claim_API2(q , 'P31' , 'Q4167836')
    #---
    NoClaim = check(q, property , claims , pop_q , gov_q)
    #---
    if NoClaim:
        himoAPI.Claim_API2(q , property , pop_q) 
    #---
    NoClaim2 = check(q, property , claims , gov_q , pop_q)
    if NoClaim2:
        himoAPI.Claim_API2(q , property , gov_q)  
#---
head = '{|\n|-\n!city !! CityItem !! Death !! Death_id !! Birth !! Birth_id !! People !! People_id'
#---
mha = [
    "محافظة البيضاء (اليمن)",
    "محافظة البيضاء",
    "محافظة الجوف",
    "محافظة الحديدة",
    "محافظة الضالع",
    "محافظة المحويت",
    "محافظة المهرة",
    "محافظة إب",
    "محافظة أبين",
    "محافظة أمانة العاصمة",
    "محافظة تعز",
    "محافظة حجة",
    "محافظة حضرموت",
    "محافظة ذمار",
    "محافظة ريمة",
    "محافظة سقطرى",
    "محافظة شبوة",
    "محافظة صعدة",
    "محافظة صنعاء",
    "محافظة عمران",
    "محافظة لحج",
    "محافظة مأرب",
    "محافظة أرخبيل سقطرى",
    "محافظة سقطرى",
    ]
#---
pop_end = {
    'sa nasud' : { 'ar' : 'حسب البلد' ,  'Q' : ''  } , 
    'sa' : { 'ar' : '' ,  'Q' : ''  } , 
    'sa' : { 'ar' : '' ,  'Q' : ''  } , 
    }
goverment = {
    "Al Mahrah (lalawigan)": { "Q": "Q275752",  "ar": "محافظة المهرة"},
    "Al Maḩwīt (lalawigan)": { "Q": "Q388280",  "ar": "محافظة المحويت" },
    "Amanat Al Asimah": { "Q": "Q2471", "ar": "أمانة العاصمة" },
    "Ibb (lalawigan)": { "Q": "Q388274",    "ar": "محافظة إب" },
    "Muḩāfaz̧at Abyan": { "Q": "Q241774",   "ar": "محافظة أبين" },
    "Muḩāfaz̧at Dhamār": { "Q": "Q328193",  "ar": "محافظة ذمار" },
    "Muḩāfaz̧at Laḩij": { "Q": "Q388318",   "ar": "محافظة لحج" },
    "Muḩāfaz̧at Ma'rib": { "Q": "Q498465",  "ar": "محافظة مأرب" },
    "Muḩāfaz̧at Raymah": { "Q": "Q475033",  "ar": "محافظة ريمة" },
    "Muḩāfaz̧at Ta‘izz": { "Q": "Q388330",  "ar": "محافظة تعز" },
    "Muḩāfaz̧at al Bayḑā'": { "Q": "Q221212",   "ar": "محافظة البيضاء" },
    "Muḩāfaz̧at al Jawf": { "Q": "Q328128", "ar": "محافظة الجوف" },
    "Muḩāfaz̧at al Ḩudaydah": { "Q": "Q275755", "ar": "محافظة الحديدة" },
    "Muḩāfaz̧at aḑ Ḑāli‘": { "Q": "Q328187",    "ar": "محافظة الضالع" },
    "Muḩāfaz̧at Şa‘dah": { "Q": "Q275732",  "ar": "محافظة صعدة" },
    "Muḩāfaz̧at Ḩajjah": { "Q": "Q328158",  "ar": "محافظة حجة" },
    "Muḩāfaz̧at Ḩaḑramawt": { "Q": "Q241135",   "ar": "محافظة حضرموت" },
    "Muḩāfaz̧at ‘Adan": { "Q": "Q275729",   "ar": "محافظة عدن" },
    "Muḩāfaz̧at ‘Amrān": { "Q": "Q275720",  "ar": "محافظة عمران" },
    "Sanaa (lalawigan)": { "Q": "Q388291",  "ar": "محافظة صنعاء" },
    "Shabwah": { "Q": "Q328180",    "ar": "محافظة شبوة" },
    "Socotra (lalawigan)": { "Q": "Q15728745",  "ar": "محافظة أرخبيل سقطرى" },
    "Yemen": { "Q": "Q805", "ar": "اليمن" },
    }
#---
P17Table = {
    "Aland Islands" :  { "ar": "جزر أولاند", "Q": "Q5689"} , 
    "Albanya" :  { "ar": "ألبانيا", "Q": "Q222"} , 
    "Alemanya" :  { "ar": "ألمانيا", "Q": "Q183"} , 
    "American Samoa" :  { "ar": "ساموا الأمريكية", "Q": "Q16641"} , 
    "Amihanang Korea" :  { "ar": "كوريا الشمالية", "Q": "Q423"} , 
    "Andorra" :  { "ar": "أندورا", "Q": "Q228"} , 
    "Angola" :  { "ar": "أنغولا", "Q": "Q916"} , 
    "Anguilla" :  { "ar": "أنغويلا", "Q": "Q25228"} , 
    "Antarctica" :  { "ar": "القارة القطبية الجنوبية", "Q": "Q51"} , 
    "Antigua ug Barbuda" :  { "ar": "أنتيغوا وباربودا", "Q": "Q781"} , 
    "Apganistan" :  { "ar": "أفغانستان", "Q": "Q889"} , 
    "Arabyang Saudita" :  { "ar": "السعودية", "Q": "Q851"} , 
    "Arhelya" :  { "ar": "الجزائر", "Q": "Q262"} , 
    "Arhentina" :  { "ar": "الأرجنتين", "Q": "Q414"} , 
    "Armenya" :  { "ar": "أرمينيا", "Q": "Q399"} , 
    "Aruba" :  { "ar": "أروبا", "Q": "Q21203"} , 
    "Aserbaiyan" :  { "ar": "أذربيجان", "Q": "Q227"} , 
    "Awstralya" :  { "ar": "أستراليا", "Q": "Q408"} , 
    "Awstriya" :  { "ar": "النمسا", "Q": "Q40"} , 
    "Bahamas" :  { "ar": "باهاماس", "Q": "Q778"} , 
    "Bangladesh" :  { "ar": "بنغلاديش", "Q": "Q902"} , 
    "Barbados" :  { "ar": "باربادوس", "Q": "Q244"} , 
    "Bareyn" :  { "ar": "البحرين", "Q": "Q398"} , 
    "Baybayon sa Marpil" :  { "ar": "ساحل العاج", "Q": "Q1008"} , 
    "Belhika" :  { "ar": "بلجيكا", "Q": "Q31"} , 
    "Belize" :  { "ar": "بليز", "Q": "Q242"} , 
    "Benin" :  { "ar": "بنين", "Q": "Q962"} , 
    "Bermuda" :  { "ar": "برمودا", "Q": "Q23635"} , 
    "Bhutan" :  { "ar": "بوتان", "Q": "Q917"} , 
    "Biyelorusya" :  { "ar": "روسيا البيضاء", "Q": "Q184"} , 
    "Biyetnam" :  { "ar": "فيتنام", "Q": "Q881"} , 
    "Bolivia" :  { "ar": "بوليفيا", "Q": "Q750"} , 
    "Bonaire, Saint Eustatius and Saba" :  { "ar": "الجزر الكاريبية الهولندية", "Q": "Q27561"} , 
    "Bosnia ug Herzegovina" :  { "ar": "البوسنة والهرسك", "Q": "Q225"} , 
    "Botswana" :  { "ar": "بوتسوانا", "Q": "Q963"} , 
    "Bouvet Island" :  { "ar": "جزيرة بوفيه", "Q": "Q23408"} , 
    "Brasil" :  { "ar": "البرازيل", "Q": "Q155"} , 
    "British Indian Ocean Territory" :  { "ar": "إقليم المحيط الهندي البريطاني", "Q": "Q43448"} , 
    "British Virgin Islands" :  { "ar": "جزر العذراء البريطانية", "Q": "Q25305"} , 
    "Brunei" :  { "ar": "بروناي", "Q": "Q921"} , 
    "Bulgaria" :  { "ar": "بلغاريا", "Q": "Q219"} , 
    "Burkina Faso" :  { "ar": "بوركينا فاسو", "Q": "Q965"} , 
    "Burma" :  { "ar": "ميانمار", "Q": "Q836"} , 
    "Burundi" :  { "ar": "بوروندي", "Q": "Q967"} , 
    "Cabo Verde" :  { "ar": "الرأس الأخضر", "Q": "Q1011"} , 
    "Canada" :  { "ar": "كندا", "Q": "Q16"} , 
    "Cayman Islands" :  { "ar": "جزر كايمان", "Q": "Q5785"} , 
    "Chad" :  { "ar": "تشاد", "Q": "Q657"} , 
    "Chile" :  { "ar": "تشيلي", "Q": "Q298"} , 
    "Christmas Island" :  { "ar": "جزيرة عيد الميلاد", "Q": "Q31063"} , 
    "Colombia" :  { "ar": "كولومبيا", "Q": "Q739"} , 
    "Comoros" :  { "ar": "جزر القمر", "Q": "Q970"} , 
    "Cook Islands" :  { "ar": "جزر كوك", "Q": "Q26988"} , 
    "Costa Rica" :  { "ar": "كوستاريكا", "Q": "Q800"} , 
    "Cuba" :  { "ar": "كوبا", "Q": "Q241"} , 
    "Curaçao" :  { "ar": "كوراساو", "Q": "Q25279"} , 
    "Dinamarka" :  { "ar": "الدنمارك", "Q": "Q35"} , 
    "Dominica" :  { "ar": "دومينيكا", "Q": "Q784"} , 
    "Ecuador" :  { "ar": "الإكوادور", "Q": "Q736"} , 
    "Ehipto" :  { "ar": "مصر", "Q": "Q79"} , 
    "El Salvador" :  { "ar": "السلفادور", "Q": "Q792"} , 
    "Eritrea" :  { "ar": "إريتريا", "Q": "Q986"} , 
    "Eslobakya" :  { "ar": "سلوفاكيا", "Q": "Q214"} , 
    "Eslobenya" :  { "ar": "سلوفينيا", "Q": "Q215"} , 
    "Espanya" :  { "ar": "إسبانيا", "Q": "Q29"} , 
    "Estados Unidos" :  { "ar": "الولايات المتحدة", "Q": "Q30"} , 
    "Estonia" :  { "ar": "إستونيا", "Q": "Q191"} , 
    "Etiopia" :  { "ar": "إثيوبيا", "Q": "Q115"} , 
    "Fiji" :  { "ar": "فيجي", "Q": "Q712"} , 
    "Finlandia" :  { "ar": "فنلندا", "Q": "Q33"} , 
    "French Polynesia" :  { "ar": "بولينزيا الفرنسية", "Q": "Q30971"} , 
    "French Southern Territories" :  { "ar": "أراض فرنسية جنوبية وأنتارتيكية", "Q": "Q129003"} , 
    "Gabon" :  { "ar": "الغابون", "Q": "Q1000"} , 
    "Gambia" :  { "ar": "غامبيا", "Q": "Q1005"} , 
    "Georgia (nasod)" :  { "ar": "جورجيا", "Q": "Q230"} , 
    "Ghana" :  { "ar": "غانا", "Q": "Q117"} , 
    "Gibraltar" :  { "ar": "جبل طارق", "Q": "Q1410"} , 
    "Gineang Ekwatoryal" :  { "ar": "غينيا الاستوائية", "Q": "Q983"} , 
    "Greenland" :  { "ar": "جرينلاند", "Q": "Q223"} , 
    "Grenada" :  { "ar": "غرينادا", "Q": "Q769"} , 
    "Gresya" :  { "ar": "اليونان", "Q": "Q41"} , 
    "Guadeloupe" :  { "ar": "غوادلوب", "Q": "Q17012"} , 
    "Guam" :  { "ar": "غوام", "Q": "Q16635"} , 
    "Guatemala" :  { "ar": "غواتيمالا", "Q": "Q774"} , 
    "Guernsey" :  { "ar": "غيرنزي", "Q": "Q25230"} , 
    "Guinea" :  { "ar": "غينيا", "Q": "Q1006"} , 
    "Guinea-Bissa" :  { "ar": "غينيا بيساو", "Q": "Q1007"} , 
    "Guyana" :  { "ar": "غيانا", "Q": "Q734"} , 
    "Guyane" :  { "ar": "غويانا الفرنسية", "Q": "Q3769"} , 
    "Habagatang Aprika" :  { "ar": "جنوب أفريقيا", "Q": "Q258"} , 
    "Habagatang Korea" :  { "ar": "كوريا الجنوبية", "Q": "Q884"} , 
    "Habagatang Sudan" :  { "ar": "جنوب السودان", "Q": "Q958"} , 
    "Haiti" :  { "ar": "هايتي", "Q": "Q790"} , 
    "Hapon" :  { "ar": "اليابان", "Q": "Q17"} , 
    "Heard Island and McDonald Islands" :  { "ar": "جزيرة هيرد وجزر ماكدونالد", "Q": "Q131198"} , 
    "Hiniusang Emiratong Arabo" :  { "ar": "الإمارات العربية المتحدة", "Q": "Q878"} , 
    "Hiniusang Gingharian" :  { "ar": "المملكة المتحدة", "Q": "Q145"} , 
    "Honduras" :  { "ar": "هندوراس", "Q": "Q783"} , 
    "Hong Kong" :  { "ar": "هونغ كونغ", "Q": "Q8646"} , 
    "Hordanya" :  { "ar": "الأردن", "Q": "Q810"} , 
    "Indonesia" :  { "ar": "إندونيسيا", "Q": "Q252"} , 
    "Indya" :  { "ar": "الهند", "Q": "Q668"} , 
    "Iran" :  { "ar": "إيران", "Q": "Q794"} , 
    "Iraq" :  { "ar": "العراق", "Q": "Q796"} , 
    "Ireland" :  { "ar": "جزيرة أيرلندا", "Q": "Q22890"} , 
    "Islandya" :  { "ar": "آيسلندا", "Q": "Q189"} , 
    "Isle of Man" :  { "ar": "جزيرة مان", "Q": "Q9676"} , 
    "Israel" :  { "ar": "إسرائيل", "Q": "Q801"} , 
    "Italya" :  { "ar": "إيطاليا", "Q": "Q38"} , 
    "Jamaica" :  { "ar": "جامايكا", "Q": "Q766"} , 
    "Jersey" :  { "ar": "جيرزي", "Q": "Q785"} , 
    "Kamboya" :  { "ar": "كمبوديا", "Q": "Q424"} , 
    "Kamerun" :  { "ar": "الكاميرون", "Q": "Q1009"} , 
    "Kapupud-ang Falkland" :  { "ar": "جزر فوكلاند", "Q": "Q9648"} , 
    "Kapupud-ang Marshall" :  { "ar": "جزر مارشال", "Q": "Q709"} , 
    "Kapupud-ang Solomon" :  { "ar": "جزر سليمان", "Q": "Q685"} , 
    "Kasahistan" :  { "ar": "كازاخستان", "Q": "Q232"} , 
    "Katar" :  { "ar": "قطر", "Q": "Q846"} , 
    "Kenya" :  { "ar": "كينيا", "Q": "Q114"} , 
    "Kirgistan" :  { "ar": "قيرغيزستان", "Q": "Q813"} , 
    "Kiribati" :  { "ar": "كيريباتي", "Q": "Q710"} , 
    "Kosobo" :  { "ar": "كوسوفو", "Q": "Q1246"} , 
    "Krowasya" :  { "ar": "كرواتيا", "Q": "Q224"} , 
    "Kuwait" :  { "ar": "الكويت", "Q": "Q817"} , 
    "Laos" :  { "ar": "لاوس", "Q": "Q819"} , 
    "Latvia" :  { "ar": "لاتفيا", "Q": "Q211"} , 
    "Lesotho" :  { "ar": "ليسوتو", "Q": "Q1013"} , 
    "Libano" :  { "ar": "لبنان", "Q": "Q822"} , 
    "Liberya" :  { "ar": "ليبيريا", "Q": "Q1014"} , 
    "Libya" :  { "ar": "ليبيا", "Q": "Q1016"} , 
    "Liechtenstein" :  { "ar": "ليختنشتاين", "Q": "Q347"} , 
    "Litwanya" :  { "ar": "ليتوانيا", "Q": "Q37"} , 
    "Luksemburgo" :  { "ar": "لوكسمبورغ", "Q": "Q32"} , 
    "Macao" :  { "ar": "ماكاو", "Q": "Q14773"} , 
    "Macedonia" :  { "ar": "جمهورية مقدونيا", "Q": "Q221"} , 
    "Madagascar" :  { "ar": "مدغشقر", "Q": "Q1019"} , 
    "Malasya" :  { "ar": "ماليزيا", "Q": "Q833"} , 
    "Malawi" :  { "ar": "ملاوي", "Q": "Q1020"} , 
    "Mali" :  { "ar": "مالي", "Q": "Q912"} , 
    "Malta" :  { "ar": "مالطا", "Q": "Q233"} , 
    "Maruwekos" :  { "ar": "المغرب", "Q": "Q1028"} , 
    "Maurisyo" :  { "ar": "موريشيوس", "Q": "Q1027"} , 
    "Mauritania" :  { "ar": "موريتانيا", "Q": "Q1025"} , 
    "Mayotte" :  { "ar": "مايوت", "Q": "Q17063"} , 
    "Mehiko" :  { "ar": "المكسيك", "Q": "Q96"} , 
    "Micronesia" :  { "ar": "ولايات ميكرونيسيا المتحدة", "Q": "Q702"} , 
    "Moldabya" :  { "ar": "مولدافيا", "Q": "Q217"} , 
    "Monako" :  { "ar": "موناكو", "Q": "Q235"} , 
    "Mongolia" :  { "ar": "منغوليا", "Q": "Q711"} , 
    "Montenegro" :  { "ar": "الجبل الأسود", "Q": "Q236"} , 
    "Montserrat" :  { "ar": "مونتسرات", "Q": "Q13353"} , 
    "Mozambique" :  { "ar": "موزمبيق", "Q": "Q1029"} , 
    "Namibya" :  { "ar": "ناميبيا", "Q": "Q1030"} , 
    "Naur" :  { "ar": "ناورو", "Q": "Q697"} , 
    "Nepal" :  { "ar": "نيبال", "Q": "Q837"} , 
    "New Caledonia" :  { "ar": "كاليدونيا الجديدة", "Q": "Q33788"} , 
    "New Zealand" :  { "ar": "نيوزيلندا", "Q": "Q664"} , 
    "Nicaragua" :  { "ar": "نيكاراغوا", "Q": "Q811"} , 
    "Niger" :  { "ar": "النيجر", "Q": "Q1032"} , 
    "Nigeria" :  { "ar": "نيجيريا", "Q": "Q1033"} , 
    "Norfolk Island" :  { "ar": "جزيرة نورفولك", "Q": "Q31057"} , 
    "Northern Mariana Islands" :  { "ar": "جزر ماريانا الشمالية", "Q": "Q16644"} , 
    "Noruwega" :  { "ar": "النرويج", "Q": "Q20"} , 
    "Olanda" :  { "ar": "هولندا", "Q": "Q55"} , 
    "Oman" :  { "ar": "سلطنة عمان", "Q": "Q842"} , 
    "Pakistan" :  { "ar": "باكستان", "Q": "Q843"} , 
    "Pala" :  { "ar": "بالاو", "Q": "Q695"} , 
    "Palestinian Territory" :  { "ar": "الضفة الغربية وقطاع غزة", "Q": "Q407199"} , 
    "Panama" :  { "ar": "بنما", "Q": "Q804"} , 
    "Papua New Guinea" :  { "ar": "بابوا غينيا الجديدة", "Q": "Q691"} , 
    "Paraguay" :  { "ar": "باراغواي", "Q": "Q733"} , 
    "Per" :  { "ar": "بيرو", "Q": "Q419"} , 
    "Pilipinas" :  { "ar": "الفلبين", "Q": "Q928"} , 
    "Pitcairn" :  { "ar": "جزر بيتكيرن", "Q": "Q35672"} , 
    "Polonya" :  { "ar": "بولندا", "Q": "Q36"} , 
    "Portugal" :  { "ar": "البرتغال", "Q": "Q45"} , 
    "Pransiya" :  { "ar": "فرنسا", "Q": "Q142"} , 
    "Puerto Rico" :  { "ar": "بورتوريكو", "Q": "Q1183"} , 
    "Republika sa Congo" :  { "ar": "جمهورية الكونغو", "Q": "Q971"} , 
    "Republika sa Tsina" :  { "ar": "تايوان", "Q": "Q865"} , 
    "Republikang Demokratiko sa Congo" :  { "ar": "جمهورية الكونغو الديمقراطية", "Q": "Q974"} , 
    "Republikang Dominikano" :  { "ar": "جمهورية الدومينيكان", "Q": "Q786"} , 
    "Republikang Popular sa Tsina" :  { "ar": "الصين", "Q": "Q148"} , 
    "Republikang Sentral Aprikano" :  { "ar": "جمهورية أفريقيا الوسطى", "Q": "Q929"} , 
    "Reunion" :  { "ar": "لا ريونيون", "Q": "Q17070"} , 
    "Rumanya" :  { "ar": "رومانيا", "Q": "Q218"} , 
    "Rusya" :  { "ar": "روسيا", "Q": "Q159"} , 
    "Rwanda" :  { "ar": "رواندا", "Q": "Q1037"} , 
    "Saint Barthelemy" :  { "ar": "سان بارتيلمي", "Q": "Q25362"} , 
    "Saint Helena" :  { "ar": "سانت هيلانة", "Q": "Q34497"} , 
    "Saint Kitts ug Nevis" :  { "ar": "سانت كيتس ونيفيس", "Q": "Q763"} , 
    "Saint Lucia" :  { "ar": "سانت لوسيا", "Q": "Q760"} , 
    "Saint Martin" :  { "ar": "تجمع سان مارتين", "Q": "Q126125"} , 
    "Saint Pierre and Miquelon" :  { "ar": "سان بيير وميكلون", "Q": "Q34617"} , 
    "Saint Vincent ug ang Grenadines" :  { "ar": "سانت فينسنت والغرينادين", "Q": "Q757"} , 
    "Samoa" :  { "ar": "ساموا", "Q": "Q683"} , 
    "Sao Tome and Principe" :  { "ar": "ساو تومي وبرينسيب", "Q": "Q1039"} , 
    "Senegal" :  { "ar": "السنغال", "Q": "Q1041"} , 
    "Serbya" :  { "ar": "صربيا", "Q": "Q403"} , 
    "Seychelles" :  { "ar": "سيشل", "Q": "Q1042"} , 
    "Sidlakang Timor" :  { "ar": "تيمور الشرقية", "Q": "Q574"} , 
    "Sierra Leone" :  { "ar": "سيراليون", "Q": "Q1044"} , 
    "Singgapura" :  { "ar": "سنغافورة", "Q": "Q334"} , 
    "Sint Maarten" :  { "ar": "سينت مارتن", "Q": "Q26273"} , 
    "Siria" :  { "ar": "سوريا", "Q": "Q858"} , 
    "Somalia" :  { "ar": "الصومال", "Q": "Q1045"} , 
    "South Georgia and the South Sandwich Islands" :  { "ar": "جورجيا الجنوبية وجزر ساندويتش الجنوبية", "Q": "Q35086"} , 
    "Sri Lanka" :  { "ar": "سريلانكا", "Q": "Q854"} , 
    "Sudan" :  { "ar": "السودان", "Q": "Q1049"} , 
    "Surinam" :  { "ar": "سورينام", "Q": "Q730"} , 
    "Suwasilandiya" :  { "ar": "سوازيلاند", "Q": "Q1050"} , 
    "Suwesya" :  { "ar": "السويد", "Q": "Q34"} , 
    "Svalbard and Jan Mayen" :  { "ar": "سفالبارد ويان ماين", "Q": "Q842829"} , 
    "Swisa" :  { "ar": "سويسرا", "Q": "Q39"} , 
    "Tailandya" :  { "ar": "تايلاند", "Q": "Q869"} , 
    "Tanzania" :  { "ar": "تنزانيا", "Q": "Q924"} , 
    "Tayikistan" :  { "ar": "طاجيكستان", "Q": "Q863"} , 
    "Togo" :  { "ar": "توغو", "Q": "Q945"} , 
    "Tonga" :  { "ar": "تونغا", "Q": "Q678"} , 
    "Trinidad ug Tobago" :  { "ar": "ترينيداد وتوباغو", "Q": "Q754"} , 
    "Tsekya" :  { "ar": "التشيك", "Q": "Q213"} , 
    "Tsipre" :  { "ar": "قبرص", "Q": "Q229"} , 
    "Tunisia" :  { "ar": "تونس", "Q": "Q948"} , 
    "Turkiya" :  { "ar": "تركيا", "Q": "Q43"} , 
    "Turkmenistan" :  { "ar": "تركمانستان", "Q": "Q874"} , 
    "Turks and Caicos Islands" :  { "ar": "جزر توركس وكايكوس", "Q": "Q18221"} , 
    "U.S. Virgin Islands" :  { "ar": "جزر العذراء الأمريكية", "Q": "Q11703"} , 
    "Uganda" :  { "ar": "أوغندا", "Q": "Q1036"} , 
    "Ukranya" :  { "ar": "أوكرانيا", "Q": "Q212"} , 
    "Unggriya" :  { "ar": "المجر", "Q": "Q28"} , 
    "United States Minor Outlying Islands" :  { "ar": "جزر الولايات المتحدة الصغيرة النائية", "Q": "Q16645"} , 
    "Uruguay" :  { "ar": "الأوروغواي", "Q": "Q77"} , 
    "Uzbekistan" :  { "ar": "أوزبكستان", "Q": "Q265"} , 
    "Vanuat" :  { "ar": "فانواتو", "Q": "Q686"} , 
    "Venezuela" :  { "ar": "فنزويلا", "Q": "Q717"} , 
    "Wallis and Futuna" :  { "ar": "واليس وفوتونا", "Q": "Q35555"} , 
    "Western Sahara" :  { "ar": "الصحراء الغربية", "Q": "Q6250"} , 
    "Yemen" :  { "ar": "اليمن", "Q": "Q805"} , 
    "Yibuti" :  { "ar": "جيبوتي", "Q": "Q977"} , 
    "Zambia" :  { "ar": "زامبيا", "Q": "Q953"} , 
    "Zimbabwe" :  { "ar": "زيمبابوي", "Q": "Q954"} , 
    }
        
#---
pop_start = {
    "Sa dagway sa yuta sa" : { "ar" : "تضاريس" ,  "Q" : "Q186131"  } , 
    "Kabukiran sa" :    { "ar" : "جبال" ,  "Q" : "Q8502"  } , 
    "Heyograpiya sa" :  { "ar" : "جغرافيا" ,  "Q" : "Q1071"  } , 
    "Kapuloan sa" :     { "ar" : "جزر" ,  "Q" : "Q23442"  } , 
    #"Mga subdibisyon sa" :     { "ar" : "تقسيمات" ,  "Q" : ""  } , 
    "Busay sa" :    { "ar" : "شلالات" ,  "Q" : "Q34038"  } ,    #H.FLLS
    "Mga bolkan sa" :  { "ar" : "براكين" ,  "Q" : "Q8072"  } , 
    "Mga bungtod sa" :     { "ar" : "تلال" ,  "Q" : "Q54050"  } , 
    "Nga bato nga pormasyon sa" :   { "ar" : "تكوينات صخرية في" ,  "Q" : "Q631305"  } , 
    "Mga estretso sa" :    { "ar" : "مضائق" ,  "Q" : "Q37901"  } , 
    "Mga gintang sa" :     { "ar" : "ممرات جبلية في" ,  "Q" : "Q133056"  } , 
    "Mga kamadan sa" :  { "ar" : "صحاري" ,  "Q" : "Q8514"  } , 
    "Mga lapyahan sa" :    { "ar" : "شواطئ" ,  "Q" : "Q40080"  } , 
    #"Mga lawis sa" :   { "ar" : "" ,  "Q" : ""  } , 
    "Mga luuk sa" :    { "ar" : "خلجان" ,  "Q" : "Q39594"  } , 
    #"Mga patag sa" :   { "ar" : "" ,  "Q" : ""  } , 
    #"Mga dapit sa" :   { "ar" : "منطقة ملح" ,  "Q" : ""  } , 
    #"Mga dapit sa asin sa" :    { "ar" : "منطقة ملح" ,  "Q" : ""  } , 
    #"Mga suba sa" :    { "ar" : "أنهار" ,  "Q" : "Q4022"  } , 
    "Mga tubud sa" :   { "ar" : "ينابيع" ,  "Q" : "Q124714"  } , 
    "Mga walog sa" :   { "ar" : "أودية" ,  "Q" : "Q39816"  } , 
    "Mga lasang sa" :  { "ar" : "غابات" ,  "Q" : "Q4421"  } , 
    "Kagaangan sa" :    { "ar" : "شعاب مرجانية في" ,  "Q" : "Q11292"  } , 
    #"Mga lungsod sa" :    { "ar" : "المستوى الثالث من التقسيم الإداري في" ,  "Q" : "Q13221722"  } , 
    "Salog sa dagat sa" :    { "ar" : "مياه ضحلة في" ,  "Q" : "Q28337"  } , 
    #"Kagaangan sa" :    { "ar" : "" ,  "Q" : ""  } , #T.BAR
    }
#---
def work(category , pop , gov ):
    ara = pywikibot.Site("ceb", "wikipedia") 
    cat_page = pywikibot.Page(ara, category)
    arlabel = "تصنيف:" + pop["ar"] + " "  + gov["ar"]
    pop_q = pop['Q']
    gov_q = gov['Q']
    if cat_page and cat_page.exists():
        #---
        #pywikibot.output('<<lightgreen>> cat_page : "%s", ar:"%s"' % (category , arlabel ))
        item = getwditem(category)
        if item:
            pywikibot.output('find item:"%s".' % item.title() )
            Find_Add_Claims( item , 'P971' , pop_q , gov_q , arlabel)
        else:
            pywikibot.output('no item for :' + category )
            #MakeNew(category, pop_q , gov_q , arlabel)
    else:
        pywikibot.output('<<lightred>> cand find page for:"%s", ar:"%s"' % (category , arlabel ))
#---
def test():
    gov = "Ibb (lalawigan)"
    for pop in pop_start:
        category = 'Kategoriya:'+ pop + ' '  + gov
        pywikibot.output( '<<lightblue>> pop:"%s" , cat:"%s" :' % (  pop , category) )
        work(category , pop_start[pop] , goverment[gov] )
#---
def yemen():
    gov_num = 0
    pop_num = 0
    goverment = P17Table
    #mha = islahvillage
    lenth = len(goverment) * len(pop_start.keys() ) 
    for gov in goverment:
        gov_num += 1
        pywikibot.output( '<<lightyellow>>>> %d/%d >> %s << <<' % ( gov_num , len(goverment) , gov) )
        for pop in pop_start:
            pop_num += 1
            category = 'Kategoriya:'+ pop + ' '  + gov
            pywikibot.output( '<<lightblue>> %d/%d pop:"%s" , cat:"%s" :' % ( pop_num , lenth , pop , category) )
            work(category , pop_start[pop] , goverment[gov] )
#---
if __name__ == "__main__":
    #test()
    yemen()
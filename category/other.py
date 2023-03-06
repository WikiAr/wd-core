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
import re
import time
import pywikibot
from pywikibot import pagegenerators
#import Nationalities as aa
import codecs
from API.maindir import main_dir
from datetime import datetime
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse

site = pywikibot.Site('wikidata', 'wikidata')
repo = site.data_repository()
#---
from API import himoAPI
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
def log(citytable , type):
    CA = {'CityItem': '' , 'Death': {'cat': '' , 'cat_id': ''} 
    , 'Birth': {'cat': '' , 'cat_id': ''} 
    , 'People': {'cat': '' , 'cat_id': ''}
    }
    #pywikibot.output( str(citytable) )

    #---#University !! UniversityItem !! category
    #form = '|-\n| [[:%s]] || {{Q|%s}} ' %  (citytable['CityItem'] , citytable[type+'Item'])
    #form = '|-\n| [[:%s]] || {{Q|%s}} ' %  (citytable[type] , citytable[type+'Item'])
    form = '|-\n| [[:%s]] || {{Q|%s}} ' %  (citytable['City'] , citytable['CityItem'])
    if type == 'City':
        keys = [ 'Death' , 'Birth' , 'People']
    else:
        keys = [ 'cat']
    #---
    for key in citytable:
        if 'cat' in citytable[key]:
            ta = '|| [[:%s]] || {{Q|%s}} ' % (citytable[key]['cat'], citytable[key]['cat_id'])
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
itemTable1 = {
    "محافظة أبين" : "Q241774",
    "محافظة أرخبيل سقطرى" : "Q15728745",

    }
#---
from item_table import itemTable
#---
def getwditem(title):
    ara = pywikibot.Site("ar", "wikipedia") 
    item = ''
    #---
    #try:
    if title != "" :
        EngPage = pywikibot.Page(ara, title)
        if title in itemTable :
            item = pywikibot.ItemPage(repo, itemTable[title])
        else:
            item = pywikibot.ItemPage.fromPage(EngPage)
        #---
        item.get()
        #pywikibot.output( '**<<lightyellow>> GetItem "%s":' %  title )
        return item
    else:#except#else
        pywikibot.output('*error when item.get() "%s"' % title)
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
                    log_duplict(q,property,q_value,id)
                    NoClaim = False
    return NoClaim
#---
def Find_Add_Claims(item , property, id ,skip=''):   
    q = item.title(as_link=False)
    #---
    if id != '':
        claims = item.claims
        NoClaim = check(q, property , claims , id , skip)
        #---
        if NoClaim:
            #AddClaims(q, property, id )
            id = re.sub( 'Q' , '' , id )
            himoAPI.Claim_API2(q , property , id)  
    else:
        pywikibot.output( '<<lightred>> Find_Add_Claims: cant find id "%s" ' % id )
#---
def Find_Add_Claims_With_Quall(item , property, id , quall_prop , quall_id,skip=''):   
    q = item.title(as_link=False)
    if id != '':
        #---
        claims = item.claims
        NoClaim = check(q, property , claims , id ,skip)
        #---
        if NoClaim:
            #AddClaims(q, property, id )
            #id = re.sub( 'Q' , '' , id )
            if quall_prop and quall_prop != '':
                himoAPI.Claim_API_With_Quall(q , property , id, quall_prop , quall_id)  
            else:
                himoAPI.Claim_API2(q , property , id)
    else:
        pywikibot.output( '<<lightred>> Find_Add_Claims_With_Quall: cant find id "%s" ' % id )
#---
def ClaimsToCat(cat_item , CityItem , tata ):   
    pywikibot.output( '<<lightyellow>> ** Claims: "%s" ' % tata )
    #pywikibot.output(params)
    cat_q = cat_item.title(as_link=False)
    QCityItem = ''
    if CityItem:
        QCityItem = CityItem.title(as_link=False)
    #---
    pywikibot.output(cat_item)  
    car = False
    if 'P971_id' in P971Table[tata]:    
        if P971Table[tata].get('P971_id') != '':
            car = True
        else:
            pywikibot.output( '<<lightred>> ClaimsToCat: cant find P971_id "%s" ' % P971Table[tata].get('P971_id') )
    #---
    P971_id = P971Table[tata].get('P971_id' , "")
    P971_id_Quall = P971Table[tata].get('P971_id_Quall' , "") # تصفية للعنصر السابق
    P971_id_Quall_id = P971Table[tata].get('P971_id_Quall_id' , "")   # قيمة التصفية للعنصر
    #---
    if P971_id != '' :
        P971_id = P971Table[tata].get('P971_id')                                # عنصر موضوعان أو أكثر يجمعهما التصنيف
        if P971_id_Quall != '' :
            if P971_id_Quall_id != '' :
                Find_Add_Claims_With_Quall(cat_item , 'P971' , P971_id , P971_id_Quall , P971_id_Quall_id , skip = P971_id )
        else:
            Find_Add_Claims(cat_item , 'P971' , P971_id , skip = QCityItem)
    else:
        pywikibot.output( '<<lightred>> ClaimsToCat: cant find P971_id "%s" ' % P971_id )
    #---
    Prop_Quall = P971Table[tata].get('P971_City_Quall', "")                # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
    Prop_Quall_id = P971Table[tata].get('P971_City_Quall_id', "")           # عنصر التصفية السابقة
    if CityItem:
        #Find_Add_Claims(cat_item, 'P971' , QCityItem ,skip=P971Table[tata]['P971_id'] )     #إضافة المدينة إلى تصنيفين أو أكثر
        Find_Add_Claims_With_Quall(cat_item , 'P971' , QCityItem , Prop_Quall , Prop_Quall_id , skip = P971_id )
#---
def AddP360(cat_item , CityItem , tata ):           #هي قائمة بـ
    #if (tata == 'Death') or (tata == 'Birth') or (tata == 'University') or (tata == 'filmset') or (tata == 'filmshot'):
    if 'P360_Q' in P971Table[tata]:
        cao = P971Table[tata].get('P360_Q')
        if cao and cao != '':
            pywikibot.output( '<<lightyellow>> **AddP360: ')
            PQuall = P971Table[tata].get('P360_Property')                    # P19 or P20
            if CityItem and PQuall: #
                QCityItem = CityItem.title(as_link=False)
                Find_Add_Claims_With_Quall(cat_item , 'P360' , cao  , PQuall , QCityItem , skip='' )      
            else:
                Find_Add_Claims(cat_item , 'P360' , cao ,skip='')                                 #هي قائمة بـ
#---
def AddOpposite(MainTitle , Cat_item , tata, city):#Q21012909
    if 'Opposite' in P971Table[tata]:
        toto = P971Table[tata]['Opposite']
        if toto != '' :
            #if (tata == 'Death') or (tata == 'Birth') or (tata == 'filmset') or (tata == 'filmshot'):
            #if tata != 'University' and tata != 'People' and tata != 'buried':
            pywikibot.output( '<<lightyellow>> ** AddOpposite: tata : "%s"'  % tata)
            Property = 'P461'               #الضد
            PQuall = 'P1013'                #المعيار المستخدم
            Pid = P971Table[tata].get('Opposite_P1013_Quall')    
            NewCat = ''
            cat = ''
            q_Cat_item = Cat_item.title(as_link=False)
            #---
            NewCatItem = False
            #if tata == 'Death':
            NewCat = P971Table[tata]['cat'] + ' ' + city
            '''elif tata == 'Birth':
                NewCat = 'تصنيف:وفيات في ' + city
                toto = 'Death'
            elif tata == 'filmset':
                NewCat = 'تصنيف:أفلام مصورة في ' + city
                toto = 'filmshot'
            elif tata == 'filmshot':
                NewCat = 'تصنيف:أفلام تقع أحداثها في ' + city
                toto = 'filmset'''
            if NewCat !='':
                NewCatItem = getwditem(NewCat)
            #---
            pywikibot.output( ' NewCat: "%s"'  % NewCat)
            if NewCatItem:
                Q_NewCat = NewCatItem.title(as_link=False)
                MainTable[city][toto] = {'cat': NewCat , 'cat_id': Q_NewCat}
                pywikibot.output( '<<lightyellow>> **  Opposite for "%s" with value "%s", Q: %s' % (MainTitle , NewCat , Q_NewCat) )
                #Find_Add_Claims(Cat_item , Property , Q_NewCat )
                #---
                # إضافة الضد إلى التصنيف القديم
                Find_Add_Claims_With_Quall(Cat_item , Property , Q_NewCat , PQuall , Pid , skip='' )
                pywikibot.output( '<<lightyellow>> **  Opposite for "%s" with value "%s", Q: %s' % (NewCat , MainTitle , q_Cat_item) )
                #---
                # إضافة الضد إلى التصنيف الجديد
                Find_Add_Claims_With_Quall(NewCatItem , Property , q_Cat_item , PQuall , Pid , skip='' )
#---
def Death(Cat_item , tata, CityItem, city , MainTitle): 
    pywikibot.output('*%s for "%s"' % (tata , MainTitle) )
    #tata = 'Death'#Death#Birth#People
    #MainTable[city] = {'CityItem': '' , 'Death': {} , 'Birth': {} , 'People': {} }
    MainTable[city][tata] = {'cat': MainTitle , 'cat_id': ''}
    #---
    if Cat_item:
        MainTable[city][tata]['cat_id'] = Cat_item.title(as_link=False)
        ClaimsToCat(Cat_item , CityItem , tata )
        AddP360(Cat_item , CityItem , tata )
        AddOpposite(MainTitle , Cat_item , tata, city)
    #---
    if 'Prop' in P971Table[tata]:
        if P971Table[tata]['Prop'] != '':
            if CityItem and Cat_item:
                MainTable[city][tata+'Item'] = CityItem.title(as_link=False)
                pywikibot.output('* Add "%s" "%s" to CityItem ' % (P971Table[tata]['Prop'] , P971Table[tata]['PropName'] ))
                Find_Add_Claims(CityItem, P971Table[tata]['Prop'] , Cat_item.title(as_link=False) ,skip='')
                # إضافة تصنيف للأشخاص الذين ماتوا هنا إلى المدينة
#---
P971Table = {}
xsxsxss ={                                  
#P971Table['s'] ={                                  
          'cat': ' '                                # بداية التصنيف         
        , 'Opposite': ''                            # الجدول الضد     
        , 'Opposite_P1013_Quall' : ''               # معيار الضد
        #---
        , 'P360_Q': ''                              # عنصر خاصية هي قائمة بـ
        , 'P360_Property': ''                       # خاصية العنصر 
        #---
        , 'P971_id': ''                             # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': ''                       # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                    # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''                    # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''                 # عنصر التصفية السابقة
        #---
        , 'Prop' : ''                               # الخاصية الرئيسية للتصنيف 
        , 'PropName' : ''                           # اسم الخاصية
        }
#---

        
P971Table['islah'] = {                  # عزل مديرية              
          'cat': 'تصنيف:عزل '                   # بداية التصنيف         
        , 'cattest': 'تصنيف:عزل مديرية '                   # بداية التصنيف         
        #---
        , 'P360_Q': 'Q12225020'                     # عنصر خاصية هي قائمة بـ
        , 'P360_Property': 'P131'                   # خاصية العنصر 
        #---
        , 'P971_id': 'Q12225020'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': 'P1659'                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': 'P31'                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : 'P1659'               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : 'P131'             # عنصر التصفية السابقة
        }
P971Table['islahvillage'] = {                  # قرى مديرية               
          'cat': 'تصنيف:قرى '                   # بداية التصنيف         
        , 'cattest': 'تصنيف:قرى عزلة '                   # بداية التصنيف         
        #---
        , 'P360_Q': 'Q28371991'                     # عنصر خاصية هي قائمة بـ قرية يمنية
        , 'P360_Property': 'P131'                   # خاصية العنصر 
        #---
        , 'P971_id': 'Q28371991'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': 'P1659'                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': 'P31'                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : 'P1659'               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : 'P131'             # عنصر التصفية السابقة
        }
P971Table['village'] = {                  # قرى مديرية               
          'cat': 'تصنيف:قرى '                   # بداية التصنيف         
        , 'cattest': 'تصنيف:قرى مديرية '                   # بداية التصنيف         
        #---
        , 'P360_Q': 'Q28371991'                     # عنصر خاصية هي قائمة بـ قرية يمنية
        #, 'P360_Property': 'P131'                   # خاصية العنصر 
        #---
        , 'P971_id': 'Q28371991'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': 'P1659'                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': 'P31'                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : 'P1659'               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        #, 'P971_City_Quall_id' : 'P131'             # عنصر التصفية السابقة
        }
#---
P971Table['district'] = {               # مديريات محافظة                     
          'cat': 'تصنيف:مديريات '                   # بداية التصنيف         
        #---
        , 'P360_Q': 'Q6617100'                      # عنصر خاصية هي قائمة بـ
        , 'P360_Property': 'P131'                   # خاصية العنصر 
        #---
        , 'P971_id': 'Q6617100'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': 'P1659'                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': 'P31'                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : 'P1659'               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : 'P131'             # عنصر التصفية السابقة
        }
#---
P971Table['islah_a'] = {                  # عزل محافظة              
          'cat': 'تصنيف:عزل '                   # بداية التصنيف         
        , 'cattest': 'تصنيف:عزل محافظة '                   # بداية التصنيف         
        #---
        , 'P971_id': 'Q12225020'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': ''                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''             # عنصر التصفية السابقة
        }
#---
P971Table['village_'] = {                  # قرى محافظة
          'cat': 'تصنيف:قرى '                   # بداية التصنيف         
        , 'cattest': 'تصنيف:قرى محافظة '                   # بداية التصنيف         
        #---
        , 'P971_id': 'Q28371991'                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': ''                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''             # عنصر التصفية السابقة
        }
#---
P971Table['Subdivisions'] = {                  # تقسيمات محافظة 
        'cat': 'تصنيف:تقسيمات '                   # بداية التصنيف         
        #---
        , 'P971_id': ''                     # عنصر موضوعان أو أكثر يجمعهما التصنيف
        , 'P971_id_Quall': ''                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''             # عنصر التصفية السابقة
        }
#---
P971Table['Populated'] = {                  # 
          'cat': 'تصنيف:أماكن مأهولة في '                   # بداية التصنيف         
        #---
        , 'P971_id': 'Q486972'                     # مستوطنة # human settlement
        , 'P971_id_Quall': ''                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''             # عنصر التصفية السابقة
        }
#---
P971Table['Subdivisions'] = {                  # جغرافيا محافظة 
        'cat': 'تصنيف:جغرافيا '                   # بداية التصنيف         
        #---
        , 'P971_id': 'Q1071'                     # جغرافيا
        , 'P971_id_Quall': ''                  # تصفية للعنصر السابق
        , 'P971_id_Quall_id': ''                 # قيمة التصفية للعنصر
        #---
        , 'P971_City_Quall' : ''               # إضافة خاصية أنظر أيضاً تحت عنصر المدينة في خاصية P971
        , 'P971_City_Quall_id' : ''             # عنصر التصفية السابقة
        }
#---
MainTable = {}
def GetCity(ncity):
    city = str(ncity)
    #city = re.sub( '_' , ' ' , city)
    #city = re.sub( 'تصنيف\:' , '' , city)
    #city = re.sub( 'أشخاص من ' , '' , city)
    #city = re.sub( 'وفيات في ' , '' , city)
    #city = re.sub( 'مواليد في ' , '' , city)
    #city = re.sub( 'أفلام تقع أحداثها في ' , '' , city)
    #---
    pywikibot.output('<<lightred>> city : "%s"' % city)
    MainTable[city] = {}
    CityItem = getwditem(city)
    if CityItem:
        pywikibot.output('CityItem :' + CityItem.title() )
        return city , CityItem
    else:
        return city , False
#---
def GetType2(MainTitle):
    pywikibot.output('*GetType for "%s"' % MainTitle)
    teee = False
    tata = False
    if MainTitle !='':
        city_fo = ''
        #MainTitle = str(MainTitle)
        Cat_item = getwditem(MainTitle)
        if Cat_item:
            for tat in P971Table.keys():
                if not teee:
                    #---
                    if 'cattest' in P971Table[tat]: 
                        tr = P971Table[tat]['cattest']          # للتفريق بين تصنيف:عزل مديرية وتصنيف:عزل محافظة
                    else:
                        tr = P971Table[tat]['cat']
                    #---
                    tottest = re.sub( tr , '' , MainTitle )
                    type = re.sub(P971Table[tat]['cat'] , '' , MainTitle )
                    if tottest != MainTitle:
                        tata = tat
                        city_fo = type
                        teee = True
            #---
            #city , CityItem = GetCity(MainTitle)
            city , CityItem = GetCity(city_fo)
            MainTable[city] = {'City': city , 'CityItem': '' }
            #---
            if tata : 
                MainTable[city][tata] = {'cat': '' , 'cat_id': ''}
                Death(Cat_item , tata , CityItem , city , MainTitle)
                #---
                pywikibot.output('* MainTable[%s]:' % tata )
                log(MainTable[city] , tata)
            else:
                pywikibot.output('* Can\' get the cate type. for "%s"' % MainTitle)
            #---
        else:
            pywikibot.output('* No Cat item. for "%s"' % MainTitle)
#---
'''def GetType(page , MainTitle):
    pywikibot.output('*GetType for "%s"' % MainTitle)
    if MainTitle !='':
        city , CityItem = GetCity(MainTitle)
        Cat_item = getwditem(MainTitle)
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
        if Cat_item:
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
            else:
                pywikibot.output('* Can\' get the cate type. for "%s"' % MainTitle)
        else:
            pywikibot.output('* No Cat item. for "%s"' % MainTitle)
        #---
        if tata : 
            MainTable[city][tata] = {'cat': '' , 'cat_id': ''}
            Death(Cat_item , tata , CityItem , city , MainTitle)
            #---
            pywikibot.output('* MainTable[%s]:' % tata )
            log(MainTable[city] , tata)'''
        #---
def University(Cat_item, UniItem, Uni , MainTitle): 
    tata = 'University'
    pywikibot.output('*%s for "%s"' % (tata , MainTitle) )
    #---
    #if Cat_item:
    ClaimsToCat(Cat_item , UniItem , tata )
    #AddP360(Cat_item , UniItem , tata )
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
from islahvillage import islahvillage
moma = {
    "مديرية البيضاء"    :   "Q4117784",
    "مديرية التحيتا"    :   "Q4117542",
    "مديرية التعزية"    :   "Q1884248",
    "مديرية التواهي"    :   "Q4818151",
    "مديرية الثورة" :   "Q4117271",
    "مديرية الجبين" :   "Q4117615",
    "مديرية الجراحي"    :   "Q4117451",
    "مديرية الجعفرية"   :   "Q4117518",
    "مديرية الجميمة"    :   "Q4117517",
    "مديرية الجوبة" :   "Q4117643",
    "الحالي (مديرية)"   :   "Q4117610",
    "مديرية الحالي" :   "Q4117610",
    "مديرية الحجيلة"    :   "Q4117457",
    "مديرية الحد"   :   "Q4117515",
    "مديرية الحزم"  :   "Q4117277",
    "مديرية الحشاء" :   "Q4117227",
    "مديرية الحشوة" :   "Q4117593",
    "مديرية الحصين" :   "Q4117328",
    "مديرية الحميدات"   :   "Q4117250",
    "مديرية الحوطة" :   "Q4117591",
    "الحوك (مديرية)"    :   "Q4117595",
    "مديرية الحوك"  :   "Q4117595",
    "مديرية الخبت"  :   "Q4117341",
    "مديرية الخلق"  :   "Q4117347",
    "مديرية الخوخة" :   "Q4704229",
    "مديرية الدريهمي"   :   "Q4117496",
    "مديرية الديس"  :   "Q4117698",
    "مديرية الرجم"  :   "Q4117345",
    "مديرية الرضمة" :   "Q4117625",
    "مديرية الروضة" :   "Q10734682",
    "مديرية الرياشية"   :   "Q4117791",
    "مديرية الريدة وقصيعر"  :   "Q4117638",
    "مديرية الزاهر" :   "Q4117810",
    "مديرية الزهرة" :   "Q4117630",
    "مديرية الزيدية"    :   "Q4117462",
    "مديرية السبرة" :   "Q4117612",
    "مديرية السبعين"    :   "Q4117333",
    "مديرية السخنة" :   "Q4117635",
    "مديرية السدة"  :   "Q4117599",
    "مديرية السلفية"    :   "Q4118313",
    "مديرية السوادية"   :   "Q4118414",
    "مديرية السود"  :   "Q4117539",
    "مديرية السودة" :   "Q4117524",
    "مديرية السوم"  :   "Q4117602",
    "مديرية السياني"    :   "Q4117787",
    "مديرية الشاهل" :   "Q4804442",
    "مديرية الشحر"  :   "Q4117645",
    "مديرية الشرية" :   "Q4117709",
    "مديرية الشعر"  :   "Q4118427",
    "مديرية الشعيب" :   "Q4117318",
    "مديرية الشغادرة"   :   "Q4117322",
    "مديرية الشمايتين"  :   "Q4165477",
    "مديرية الصافية"    :   "Q4117279",
    "مديرية الصعيد" :   "Q4118418",
    "مديرية الصفراء"    :   "Q4117492",
    "مديرية الصلو"  :   "Q4118425",
    "مديرية الصليف" :   "Q1884201",
    "مديرية الصومعة"    :   "Q4117807",
    "مديرية الضالع" :   "Q1884227",
    "مديرية الضحي"  :   "Q4117503",
    "مديرية الضليعة"    :   "Q4117682",
    "مديرية الطفة"  :   "Q4117705",
    "مديرية الطلح"  :   "Q4117694",
    "مديرية الطويلة"    :   "Q4812416",
    "مديرية الظاهر" :   "Q4117607",
    "مديرية الظهار" :   "Q4118413",
    "مديرية العبدية"    :   "Q4117555",
    "مديرية العبر"  :   "Q4117641",
    "مديرية العدين" :   "Q4117786",
    "مديرية العرش"  :   "Q4117776",
    "مديرية العشة"  :   "Q4703500",
    "مديرية الغيظة" :   "Q4117605",
    "مديرية الغيل"  :   "Q4117300",
    "مديرية القاهرة"    :   "Q4117619",
    "مديرية القبيطة"    :   "Q4117561",
    "مديرية القريشية"   :   "Q4118316",
    "مديرية القطن"  :   "Q4117526",
    "مديرية القف"   :   "Q4117689",
    "مديرية القفر"  :   "Q4117691",
    "مديرية القناوص"    :   "Q4117609",
    "مديرية اللحية" :   "Q4733335",
    "مديرية المتون" :   "Q4704407",
    "مديرية المحابشة"   :   "Q4117340",
    "مديرية المحفد" :   "Q4117574",
    "مديرية المحويت"    :   "Q4117248",
    "مديرية المخاء" :   "Q1650840",
    "مديرية المخادر"    :   "Q4117820",
    "مديرية المدان" :   "Q4117467",
    "مديرية المراوعة"   :   "Q4117620",
    "المسراخ"   :   "Q4118993",
    "مديرية المسيلة"    :   "Q4118398",
    "مديرية المسيمير"   :   "Q4704515",
    "مديرية المشنة" :   "Q4117706",
    "مديرية المصلوب"    :   "Q4117324",
    "مديرية المطمة" :   "Q1884259",
    "مديرية المظفر" :   "Q4117614",
    "مديرية المعافر"    :   "Q4117693",
    "مديرية المعلا" :   "Q3696048",
    "مديرية المغربة"    :   "Q4117504",
    "مديرية المغلاف"    :   "Q4117529",
    "مديرية المفتاح"    :   "Q285269",
    "مديرية المفلحي"    :   "Q4117631",
    "مديرية المقاطرة"   :   "Q4117600",
    "المكلا"    :   "Q310772",
    "مديرية الملاجم"    :   "Q4117799",
    "مديرية الملاح" :   "Q4117611",
    "المنصورة (عدن)"    :   "Q3696034",
    "مديرية المنصورية"  :   "Q4117598",
    "مديرية المواسط"    :   "Q4120341",
    "الميناء (مديرية)"  :   "Q4117627",
    "مديرية الميناء"    :   "Q4117627",
    "مديرية النادرة"    :   "Q4118324",
    "مديرية الوازعية"   :   "Q4117685",
    "مديرية الوحدة" :   "Q4117329",
    "مديرية الوضيع" :   "Q4117454",
    "مديرية إب" :   "Q4117701",
    "مديرية أحور"   :   "Q4117549",
    "مديرية أزال"   :   "Q4117188",
    "مديرية أسلم"   :   "Q4117502",
    "مديرية أفلح الشام" :   "Q4117422",
    "مديرية أفلح اليمن" :   "Q4117521",
    "مديرية باجل"   :   "Q2217814",
    "مديرية باقم"   :   "Q4117547",
    "مديرية بدبدة"  :   "Q4117653",
    "مديرية برط العنان" :   "Q4117229",
    "مديرية برع"    :   "Q4117582",
    "مديرية بروم ميفع"  :   "Q4117805",
    "مديرية بعدان"  :   "Q4117700",
    "مديرية بكيل المير" :   "Q4117425",
    "مديرية بلاد الطعام"    :   "Q4117553",
    "مديرية بني الحارث" :   "Q4117305",
    "مديرية بني العوام" :   "Q4117407",
    "مديرية بني سعد"    :   "Q4117337",
    "مديرية بني صريم"   :   "Q4117563",
    "مديرية بني قيس الطور"  :   "Q4117530",
    "مديرية بيت الفقيه" :   "Q4874935",
    "مديرية بيحان"  :   "Q4117801",
    "مديرية تبن"    :   "Q4117488",
    "مديرية تريم"   :   "Q4117824",
    "مديرية ثلاء"   :   "Q4117440",
    "مديرية ثمود"   :   "Q4117622",
    "مديرية جبل حبشي"   :   "Q4119006",
    "مديرية جبل راس"    :   "Q4117601",
    "مديرية جبل عيال يزيد"  :   "Q4117537",
    "مديرية جبل مراد"   :   "Q4117618",
    "مديرية جبلة"   :   "Q4117703",
    "مديرية جبن"    :   "Q4117516",
    "مديرية جحاف"   :   "Q4117376",
    "مديرية جردان"  :   "Q4118423",
    "مديرية جيشان"  :   "Q4117520",
    "مديرية حات"    :   "Q4117708",
    "مديرية حالمين" :   "Q4117621",
    "مديرية حبان"   :   "Q3125264",
    "مديرية حبيش"   :   "Q4118310",
    "مديرية حبيل جبر"   :   "Q4117473",
    "مديرية حجة"    :   "Q4117505",
    "مديرية حجر"    :   "Q4117687",
    "مديرية حجر الصيعر" :   "Q4117648",
    "مديرية حديبو"  :   "Q5751685",
    "مديرية حرض"    :   "Q1884189",
    "مديرية حرف سفيان"  :   "Q4117617",
    "مديرية حريب"   :   "Q4117540",
    "مديرية حريب القرامش"   :   "Q4117533",
    "مديرية حريضة"  :   "Q4118387",
    "مديرية حزم العدين" :   "Q4118421",
    "مديرية حصوين"  :   "Q4117683",
    "مديرية حطيب"   :   "Q4117727",
    "مديرية حفاش"   :   "Q4117243",
    "مديرية حوث"    :   "Q4117418",
    "مديرية حورة ووادي العين"   :   "Q4117652",
    "مديرية حوف"    :   "Q4117695",
    "مديرية حيدان"  :   "Q4117573",
    "مديرية حيران"  :   "Q4117436",
    "مديرية حيس"    :   "Q4117624",
    "مديرية حيفان"  :   "Q4118985",
    "مديرية خارف"   :   "Q4117448",
    "مديرية خب والشعف"  :   "Q4117286",
    "مديرية خدير"   :   "Q4118319",
    "مديرية خراب المراشي"   :   "Q4117302",
    "مديرية خمر"    :   "Q3196049",
    "مديرية خنفر"   :   "Q4117538",
    "خور مكسر"  :   "Q13641424",
    "مديرية خيران المحرق"   :   "Q4117331",
    "مديرية دار سعد"    :   "Q4117565",
    "مديرية دمت"    :   "Q4117240",
    "مديرية دهر"    :   "Q5269080",
    "مديرية دوعن"   :   "Q4117696",
    "مديرية ذباب"   :   "Q4118401",
    "ذمار (مدينة)"  :   "Q955523",
    "مديرية مدينة ذمار" :   "Q955523",
    "مديرية ذي السفال"  :   "Q4118321",
    "مديرية ذي ناعم"    :   "Q4117714",
    "مديرية ذيبين"  :   "Q4117514",
    "مديرية رازح"   :   "Q4117523",
    "مديرية رجوزة"  :   "Q4117304",
    "مديرية رحبة"   :   "Q4117567",
    "مديرية رخية"   :   "Q4117554",
    "مديرية رداع"   :   "Q4118334",
    "مديرية ردفان"  :   "Q4117512",
    "مديرية ردمان"  :   "Q4117692",
    "مديرية رصد"    :   "Q4117586",
    "مديرية رضوم"   :   "Q4117802",
    "مديرية رغوان"  :   "Q4117603",
    "مديرية رماه"   :   "Q4117633",
    "مديرية ريدة"   :   "Q4117431",
    "مديرية زبيد"   :   "Q4117562",
    "مديرية زمخ ومنوخ"  :   "Q4117646",
    "مديرية زنجبار" :   "Q580992",
    "مديرية ساقين"  :   "Q4117500",
    "مديرية سامع"   :   "Q7408406",
    "مديرية ساه"    :   "Q4117543",
    "مديرية سباح"   :   "Q4117509",
    "مديرية سحار"   :   "Q1884209",
    "مديرية سرار"   :   "Q4117544",
    "مديرية سيحوت"  :   "Q1656398",
    "مديرية سيئون"  :   "Q4117557",
    "مديرية شبام"   :   "Q4117552",
    "مديرية شبام كوكبان"    :   "Q4117372",
    "مديرية شحن"    :   "Q4117616",
    "مديرية شداء"   :   "Q4117551",
    "مديرية شرس"    :   "Q4117343",
    "مديرية شرعب الرونة"    :   "Q4120339",
    "مديرية شرعب السلام"    :   "Q4120340",
    "مديرية شعوب"   :   "Q4117252",
    "مديرية شهارة"  :   "Q665937",
    "مديرية صالة"   :   "Q4117815",
    "مديرية صباح"   :   "Q4117712",
    "مديرية صبر الموادم"    :   "Q4118385",
    "مديرية صرواح"  :   "Q4117559",
    "مديرية صعدة"   :   "Q4117548",
    "مديرية صنعاء القديمة"  :   "Q1650596",
    "مديرية صوير"   :   "Q4117464",
    "مديرية طور الباحة" :   "Q4117589",
    "مديرية ظليمة حبور" :   "Q4117558",
    "مديرية عبس"    :   "Q4117405",
    "مديرية عتق"    :   "Q4118415",
    "مديرية عرماء"  :   "Q4792482",
    "مديرية عسيلان" :   "Q4117697",
    "مديرية عمد"    :   "Q4117560",
    "مديرية عمران"  :   "Q1650593",
    "مديرية عيال سريح"  :   "Q4117525",
    "مديرية عين"    :   "Q4117782",
    "مديرية غمر"    :   "Q4117613",
    "مديرية غيل باوزير" :   "Q4117550",
    "مديرية غيل بن يمين"    :   "Q4117704",
    "مديرية فرع العدين" :   "Q4117678",
    "مديرية قارة"   :   "Q4117506",
    "مديرية قشن"    :   "Q4117812",
    "مديرية قطابر"  :   "Q283304",
    "مديرية قعطبة"  :   "Q1884217",
    "مديرية قفل شمر"    :   "Q4117511",
    "مديرية قفلة عذر"   :   "Q4117577",
    "مديرية قلنسية وعبد الكوري" :   "Q7272759",
    "مديرية كتاف والبقع"    :   "Q4117637",
    "مديرية كحلان الشرف"    :   "Q4117527",
    "مديرية كحلان عفار" :   "Q4117411",
    "كريتر" :   "Q2263449",
    "مديرية كسمة"   :   "Q1884237",
    "مديرية كشر"    :   "Q4117508",
    "مديرية كعيدنة" :   "Q4117507",
    "مديرية كمران"  :   "Q17067582",
    "مديرية لودر"   :   "Q1164303",
    "مديرية ماهلية" :   "Q4117604",
    "مديرية ماوية"  :   "Q4117789",
    "مديرية مأرب"   :   "Q6762513",
    "مديرية مبين"   :   "Q4117532",
    "مديرية مجز"    :   "Q4117546",
    "مديرية مجزر"   :   "Q4117576",
    "مديرية مدغل الجدعان"   :   "Q4117580",
    "مديرية مدينة البيضاء"  :   "Q4703572",
    "مديرية مذيخرة" :   "Q4117793",
    "مديرية مرخة السفلى"    :   "Q4118417",
    "مديرية مرخة العليا"    :   "Q4117780",
    "مديرية مزهر"   :   "Q4117569",
    "مديرية مستباء" :   "Q4117513",
    "مديرية مسور"   :   "Q4117443",
    "مديرية مسورة"  :   "Q4117716",
    "مديرية مشرعة وحدنان"   :   "Q4118869",
    "مديرية معين"   :   "Q4117338",
    "مديرية مقبنة"  :   "Q4118981",
    "مديرية مكيراس" :   "Q4118389",
    "مكيراس"    :   "Q986772",
    "مديرية ملحان"  :   "Q6851806",
    "مديرية منبة"   :   "Q4117482",
    "مديرية منعر"   :   "Q4117680",
    "مديرية مودية"  :   "Q4117556",
    "مديرية موزع"   :   "Q4118996",
    "مديرية ميدي"   :   "Q4117541",
    "مديرية ميفعة"  :   "Q4117822",
    "مديرية ناطع"   :   "Q4117794",
    "مديرية نجرة"   :   "Q4117428",
    "مديرية نصاب"   :   "Q4117809",
    "مديرية نعمان"  :   "Q4117725",
    "همدان (مديرية)"    :   "Q4117299",
    "مديرية همدان"  :   "Q4117299",
    "مديرية وشحة"   :   "Q4117433",
    "مديرية وضرة"   :   "Q4117352",
    "مديرية ولد ربيع"   :   "Q4118409",
    "مديرية يافع"   :   "Q4117606",
    "مديرية يبعث"   :   "Q4117608",
    "مديرية يريم"   :   "Q4117699",
    "مديرية يهر"    :   "Q4117470"
    }
#---
def yemen():
    num = 0
    mha = moma
    #keys = [ 'مديريات' , 'عزل' , 'قرى', 'تقسيمات' , 'أماكن مأهولة في']
    keys = ['قرى']
    for key in keys:
        for title in mha:
            num = num + 1
            title = 'تصنيف:'+ key + ' '  + title
            pywikibot.output( '<<lightyellow>>\n----------\n>> %d >> %s << <<' % ( num , title) )
            GetType2(title)
#---
def main():
    options = {}
    #---
    #lenth = len(pywikibot.handle_args(args))
    #if lenth == 0:
    args = {}
    #args = {'-ref:قالب:تصنيف_وفيات_في' , '-ns:14'}
    #args = {'-ref:قالب:تصنيف_مواليد_في' , '-ns:14'}
    #---
    file = ""
    argg = False
    University = False
    #---
    Table = {}
    Table["death"] = 'category/file/death.txt'
    Table["death2"] = 'category/file/death2.txt'
    Table["birth2"] = 'category/file/birth2.txt'
    Table["birth"] = 'category/file/birth.txt'
    Table["people"] = 'category/file/people.txt'
    Table["people2"] = 'category/file/people2.txt'
    Table["people3"] = 'category/file/people3.txt'
    Table["filmset"] = 'category/file/filmset.txt'
    Table["filmshot"] = 'category/file/filmshot.txt'
    #---
    pywikibot.output('len(sys.argv): %d'% len(sys.argv) )
    if sys.argv and len(sys.argv) > 1:
        argg = True
        pywikibot.output(sys.argv)
        if sys.argv[1] == 'univer':
            #args = {'-catr:خريجون_حسب_الجامعة_أو_الكلية_في_اليمن' , '-ns:14'}
            file = 'category/University.txt'
            University = True
        #---
        elif sys.argv[1] in Table:
            file = Table[sys.argv[1]]
        #---
        elif sys.argv[1] == 'yemen':
            yemen()
        #---
        elif sys.argv[1] == 'test':
            TestMain()
        #---
        pywikibot.output('no sys.argv')
        #---
    #---
    text3 = ""
    List2 = []
    if file != "" :
        text3 = codecs.open(file, "r", encoding="utf-8").read()
        List2 = [ x.strip() for x in text3.split("\n") if x.strip() != ""  ]
    #---
    List = []
    if List2:
        for x in List2:
            if x.find("تصنيف:") != -1:
                xp = "تصنيف:" + x.split("تصنيف:")[1]
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
            MainTitle = re.sub("_" , " " , MainTitle)
            #try:   #start(text, title)
            pywikibot.output( '<<lightyellow>>\n----------\n>> %d >> %s << <<' % ( num , MainTitle) )
            #---
            if University:
                univer(MainTitle)
            else:
                GetType2(MainTitle)
                
        #---
        log2('\n|}\n\n')
#---
def TestMain():
    pywikibot.output( '<<lightyellow>> **TestMain: ')
    #pywikibot.output(skiptable)
    item = getwditem('تصنيف:أشخاص_من_ذيذيموتيخو')
    #log2(head)
    page = ''
    #univer(page , 'تصنيف:خريجو_جامعة_العلوم_والتكنولوجيا_(اليمن)')
    #GetType(page , 'تصنيف:وفيات في ندولا')
    #---
    if item:
        Q = item.title(as_link=False)
        Find_Add_Claims(item , 'P971', 'Q234453' , skip='Q19660746')
    #---
    #log2('\n|}\n\n')
#---
if __name__ == "__main__":
    GetType2("تصنيف:أشخاص من منطقة عسير")
    #main()
#---
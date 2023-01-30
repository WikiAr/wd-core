#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

العمل مع ثلاثة ملفات
ALL_Years
ALL_Centry
ALL_decades

تصانيف تحتوي _in_
"""
#
# (C) Ibrahem Qasim, 2022
#
#

from pywikibot import config
import re
import pywikibot
import codecs
#---
import sys

#---
try:
    import MySQLdb
    My_SQL = True
except:
    pywikibot.output('<<lightred>> No MySQLdb')
    #pywikibot.stopme()
    #sys.exit()
#--- 
from type.cate_type import *   #pop_start , years__,decade__ , century__, New_Pop , New_Pop2
from list.ALL_Centry import ALL_Centries
from list.ALL_decades import ALL_Decade
from list.ALL_Years import ALL_Year
#from list.NewCategories import *#NewCate
#---
from type.yearnew import *#years__new
from type.month import Month__new
YDC_C = {}
#for toad in [decade__ , century__, years__new  ,pop_start , New_Pop , New_Pop2 , millennium__]:#years__
for toad in [ years__ , decade__ , century__ , millennium__ , years__new , Month__new]:#
    for ci in toad:
        ci2 = ci.split(' in')[0]
        YDC_C[ci2] = toad[ci]
        
YDC_C['September 2018'] = {"Q":"Q38601074","ar":"سبتمبر 2018"}
YDC_C['November 2020'] = {"Q":"Q38575003","ar":"نوفمبر 2020"}
#---
from type.cate_P17 import *#ALL_P17#USA_P17#P17_final#New_P173
YDC_P17 = {}
for toad in [P17_final]:#P17_final , pop_final_Without_Years]:
    for ci in toad:
        ci2 = ci.lower()
        YDC_P17[ci2] = toad[ci]
#---
tittable2 =[
    "2017_sports_events",
    "2017_events",
    "January_2017_events",
    "January_2017_events_by_continent",
    "January_2017_crimes_by_country",
    "2017_events_by_country",
    "January_2017_events_in_Africa",
    "January_2017_events_in_Europe",
    "January_2017_sports_events",
    "January_2017_sports_events_by_country",
    ]
#---
tittable =[
    "April_1983_sports_events",
    "April_1983_events_in_Europe",
    "April_1982_sports_events_in_Europe",
    "April_1981_sports_events_in_Europe",
    "April_1980_sports_events_in_Europe",
    ]
#---
en_site = pywikibot.Site('en')
def MySQLdb_finder_New(mo , mo2 = ""):
    pywikibot.output('<<lightred>> sql . MySQLdb_finder %s: '  %  mo)
    if mo != "" :
        #---
        #---
        cats = []
        encats = []
        mo = re.sub(" " , "_" , mo)
        #        ' page_title like "%{}%" or page_title like "%{}%" AND page_namespace = 14  ' + \
        #---start sql---------------------------------------
        Queris = 'SELECT CONCAT("Category:",page_title) AS titl FROM page WHERE ' + \
                ' {}  AND page_namespace = 14  ' + \
                ' ' + \
                ' GROUP BY page_title limit 600; '
        #---
        popo = 'page_title like "%{}%"'.format(mo)
        #---
        if mo2 != "" : 
            popo = 'page_title like "%{}%" OR page_title like "%{}%"'.format(mo, mo2)
        #---
        queries = Queris.format(popo)
        #---
        if "newsql" in sys.argv:
            queries = newqueries.format(mo , mo.lower() )
        #---
        pywikibot.output(queries)
        #try:
        if mo != "" :
            cn = MySQLdb.connect("enwiki.analytics.db.svc.wikimedia.cloud", db=en_site.dbName()+ '_p', user=config.db_username, passwd=config.db_password)
            cn.set_character_set('utf8')
            cur = cn.cursor()
            cur.execute(queries)
            en_results = cur.fetchall()
            cn.close()
            #---end of sql--------------------------------------------
            for raw in en_results:
                tit = raw[0]
                tit = re.sub(' ', '_' , tit)
                encats.append(tit)
            #---
            pywikibot.output( "encats: <<lightred>> %d"  %  len(encats)    )
            #---
            if encats != []:
                return encats
            else:
                return False
        else:
        #except:
            return False
    return False    
#---
import ynew
#import t2018
from list.month_list import New_Month_list
from type.cate_type import * 
from type.yearnew import * 
#---
MONTHSTR = '(January|February|March|April|May|June|July|August|September|October|November|December)'
typeTable = {
        'crimes' : {'ar': 'جرائم' , 'Q' : 'Q83267'}, 
        'attacks' : {'ar': 'هجمات' , 'Q' : 'Q81672'}, 
        #'peer reviews' : {'ar': 'مراجعة الأقران' , 'Q' : 'Q215028'}, 
        'events' : {'ar': 'أحداث' , 'Q' : 'Q1190554'}, 
        #'sports events' : {'ar': 'أحداث' , 'Q' : ['Q1190554' , 'Q349'] , 's': 'الرياضية' }, 
        'sports events' : {'ar': 'أحداث' , 'Q' : 'Q16510064' , 's': 'الرياضية' }, 
    }
#---
def yemen(New_Month_list):
    num = 0
    pywikibot.output( 'start with "%s":')
    #New_Month_list = tittable
    lenth =  len(New_Month_list) 
    tit = {}
    safo = '|'.join(typeTable.keys() )
    #tito = ' in '
    yy = "\w+\s*\d+"
    #tits = '^' + MONTHSTR + '_\d+_.*'
    #tits = MONTHSTR + '(\d+_sports_events|\d+_events)_.*'
    tits = '(\w+\s*\d+)\s*(sports\s*events|events)\s*.*'
    tita = '('+ yy +')\s*('+safo+'|)( in|)\s*(.*)'
    #mha = islahvillage
    for category in New_Month_list:
        #try:
            num += 1
            category = re.sub('_' , ' ' , category)
            category = re.sub('Category:' , '' , category)
            pywikibot.output( '<<lightyellow>>>> category:%s ' % category )
            year = re.sub(tita , '\g<1>', category )
            typeo = re.sub(tita , '\g<2>', category )
            In = re.sub(tita , '\g<3>', category )
            contry = re.sub(tita , '\g<4>', category )
            #year = category.split(tito)[0]
            #contry = category.split(tito)[1]
            contry = contry.lower()
            pywikibot.output( 'year:"%s" , typeo:"%s" , In:"%s", contry:"%s"' % ( year , typeo , In , contry ) )
            arlabel = "تصنيف:"
            #---
            year_lab , suf = '' , ''
            #---
            Qafo = []
            if typeo in typeTable:
                tit = typeTable[typeo]
                sa = typeTable[typeo]['ar']
                arlabel = arlabel + sa
                if 's' in typeTable[typeo]:
                    suf = typeTable[typeo]['s']
                typeq = typeTable[typeo]['Q']
                #if type(typeq) == list:
                    #Qafo = typeq
                #else:
                    #Qafo.append(typeq)
                #pywikibot.output( 'a<<lightblue>>>%s' % arlabel )
            #---
            if year in YDC_C:
                year_lab = re.sub(' في$' , '' , YDC_C[year]['ar'] )
                arlabel = arlabel + ' ' + year_lab
                ycs = YDC_C[year]['Q']
                #if not ycs in Qafo:
                    #Qafo.append(ycs)
            #---
            #if contry == '' and In == '':
            if contry == '' and In == '':
                #pywikibot.output( 'a<<lightblue>>>No contry: ar:%s' % arlabel )
                if suf != '':
                    arlabel = arlabel  + ' ' + suf
                #arlabel = re.sub(' في$' , ' ', arlabel)
                pywikibot.output( 'a<<lightblue>>>No contry: ar:%s' % arlabel )
                ynew.New_Work2(tit, category , year , YDC_C , '' , {} , num , lenth , arlabel)
            #---
            elif contry != '' and contry in YDC_P17:
                
                pywikibot.output( 'a<<lightblue>>>p:%s, %s: ,cat:"%s"' % (YDC_P17[contry]['ar'] , year_lab  , category) )
                if YDC_P17[contry]['ar'] != '':
                    BY = False
                    con_lab = YDC_P17[contry]['ar']
                    if re.sub('^حسب' , '' , con_lab) != con_lab :
                        BY = True
                    if In == ' in':
                        con_lab = 'في ' + con_lab
                    #arlabel = "تصنيف:" + tita_Q[tit]['priff'] + ' ' + year_pop["ar"] + " " + YDC_P17[contry]["ar"]
                    #if BY and suf != '':
                    if suf != '':
                        arlabel = arlabel + ' ' + suf + ' ' + con_lab
                    else:
                        arlabel = arlabel + ' ' + con_lab
                        #if suf != '':
                            #arlabel = arlabel  + ' ' + suf
                    #if con_lab == "حسب البلد":
                        #arlabel = "تصنيف:" + year_pp + " " +  gov_pp
                #---
                pywikibot.output( 'a<<lightblue>>>ar:%s' % arlabel )
                #if typeq != '' :
                #YDC_C[year]['Q'] = Qafo
                #pywikibot.output( 'a<<lightblue>>>Qafo:%s' % str(Qafo) )
                #t2018.Work_2018(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel)
                ynew.New_Work2(tit, category , year , YDC_C , contry , YDC_P17 , num , lenth , arlabel)
#---
the_new_contry = {
    "python pwb.py p971/ye d",
    "python pwb.py p971/ye c",
    }
#---
def main_sql2(list):#
    pywikibot.output( '<<lightblue>> main_sql2' )
    #---
    for value in list:
        list = MySQLdb_finder_New(value, mo2 = "")
        if list:
            yemen(list)
#---
def ma_MakeNewCat():
    #python pwb.py p9/event o:s
    #python pwb.py p9/event o:year
    #python pwb.py p9/event o:de
    #python pwb.py p9/event o:ce
    #python pwb.py p9/event o:new
    #python pwb.py p9/event o:new2
    #python pwb.py p9/event o:mi 
    #python pwb.py p9/event o:all 
    #python pwb.py p9/event o:n17 
    #python pwb.py p9/event o:n172 
    #python pwb.py p9/event o:n173 
    #python pwb.py p9/event o:n174
    #python pwb.py p9/event o:usa
    #python pwb.py p9/event test:2019
    pywikibot.output('<<lightgreen>> ma_MakeNewCat')
    #---
    oioii = {
        's' : pop_start , 
        'year' : years__ , 
        'de' : decade__ , 
        'ce' : century__ , 
        'new' : New_Pop , 
        'new2' : New_Pop2 , 
        'mi' : millennium__ ,
        'all' : ALL_P17 ,
        'n17' : New_P17 ,
        'n172' : New_P172 ,
        'n173' : New_P173 ,
        'n174' : New_P174 ,
        'usa' : USA_P17 ,
    }
    #---# [USA_P17 , ALL_P17,New_P17 , New_P172 , New_P173 , New_P174]
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg =='o':
            if value in oioii:
                main_sql2(oioii[value])
                break
        #---
        if arg =='test':
            main_sql2([value])
            break
        #---
        if arg =='page':
            yemen([value])
            break
        #---
    pywikibot.output('<<lightgreen>> Finish ma_MakeNewCat')
#---
if __name__ == "__main__":
    ma_MakeNewCat()
#---
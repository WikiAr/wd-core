#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


python3 pwb.py dump/arw2
python3 pwb.py dump/arw2 test nosave
python3 pwb.py dump/arw2 test nosave p31
python3 pwb.py dump/arw2 test nosave printline
python3 pwb.py dump/arw2 test nosave limit:5000

"""
#
# (C) Ibrahem Qasim, 2017


import sys
import bz2
#import gz
import json
import time
import pywikibot
#---
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
#---
# start of arAPI.py file
#from API import arAPI 
# arAPI.post( params, family="", lang="")
# arAPI.purge(title)


# arAPI.create_Page(text , summary , title, ask )
# arAPI.Add_To_Bottom(appendtext , summary , title , ask)
# arAPI.Add_To_Head(prependtext , summary , title, Ask)
#---
#ar_site = pywikibot.Site('ar', 'wikipedia')
title = u'ويكيبيديا:مشروع_ويكي_بيانات/تقرير_P31'
#---
fancota = { u"count" : 0 
    , u"labels" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    , u"descriptions" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    , u"aliases" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    }
#---
priffixeso = [
    u"مقالة",
    u"نقاش:",
    u"مستخدم:",
    u"نقاش المستخدم:",
    u"ويكيبيديا:",
    u"نقاش ويكيبيديا:",
    u"ملف:",
    u"نقاش الملف:",
    u"ميدياويكي:",
    u"نقاش ميدياويكي:",
    u"قالب:",
    u"نقاش القالب:",
    u"مساعدة:",
    u"نقاش المساعدة:",
    u"تصنيف:",
    u"نقاش التصنيف:",
    u"بوابة:",
    u"نقاش البوابة:",
    u"وحدة:",
    u"نقاش الوحدة:",
    u"إضافة:",
    u"نقاش الإضافة:",
    u"تعريف الإضافة:",
    u"نقاش تعريف الإضافة:",
    u"موضوع:",
    ]
#---
priffixes = {}
#---
for x in priffixeso:
    priffixes[x] = { u"count" : 0 
    , u"labels" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    , u"descriptions" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    , u"aliases" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
    }
#---
Table_no_ab2 = {}
Table_no_ar_lab = {}
#---
p31_main_tab = {}
All_items = { 1 : 0 } 
All_ar_sitelinks = { 1 : 0 } 
sitelinks_no_ar = { 1 : 0 } 
#---
Offset = { 1 : 0 } 
Limit = { 1 : 500000000 } 
#---
# python3 pwb.py wd/dump test 
#---
def ns_stats():
    texts = """
== حسب النطاق  ==
"""
    #---
    xline = '' # |x=مقالة,تصنيف,قالب,بوابة,ويكيبيديا,وحدة,مساعدة,ملف
    yline = '' # |y1=718532,564152,46493,4292,1906,850,137,7
    #---
    Chart = """
{| class="floatleft sortable" style="text-align:right"
|-
|
{{Graph:Chart|width=170|height=170|xAxisTitle=الشهر|yAxisTitle=عدد المقالات
|type=pie|showValues1=offset:8,angle:45
|x=%s
|y1=%s
|legend=الخاصية
}}
|-
|}"""
    #---
    tables = """
{| class="wikitable sortable plainrowheaders"
|-
! class="sortable" rowspan="2" | النطاق
! class="sortable" rowspan="2" | العدد
! class="unsortable" colspan="4" | labels
! class="unsortable" colspan="4" | descriptions
! class="unsortable" colspan="4" | aliases
|-
! نعم !! لا !! عربي !! دون عربي !! نعم !! لا !! عربي !! دون عربي !! نعم !! لا !! عربي !! دون عربي
|-

"""
    #---
    #lists = [ [ y[u"count"] , x ] for x, y in priffixes.items()]
    #lists.sort(reverse=True)
    #---
    #for x , ns in lists :
        #count = x # priffixes[ns][u"count"] 
    for ns in priffixes : 
        count = priffixes[ns][u"count"] 
        #pywikibot.output('priffixes[ns]')
        #pywikibot.output(priffixes[ns])
        #pywikibot.output('priffixes[ns]')
        if count != 0 :  
            #w_la = count - priffixes[ns][u"labels"]
            #w_de = count - priffixes[ns][u"descriptions"]
            #w_al = count - priffixes[ns][u"aliases"]
            ns2 = ns.replace(":","")
            tables += '\n'
            #---
            row = u"| %s || %d" % ( ns2 , count )
            xline += u",%s" % ns2
            yline += u",%d" % count
            #---{ "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
            fafa = u"\n| %d || %d || %d || %d" 
            row += fafa % ( priffixes[ns][u"labels"]["yes"],priffixes[ns][u"labels"]["no"],priffixes[ns][u"labels"]["yesar"],priffixes[ns][u"labels"]["noar"] )
            #---
            row += fafa % ( priffixes[ns][u"descriptions"]["yes"],priffixes[ns][u"descriptions"]["no"],priffixes[ns][u"descriptions"]["yesar"],priffixes[ns][u"descriptions"]["noar"] )
            #---
            row += fafa % ( priffixes[ns][u"aliases"]["yes"],priffixes[ns][u"aliases"]["no"],priffixes[ns][u"aliases"]["yesar"],priffixes[ns][u"aliases"]["noar"] )
            #---
            tables += row
            tables += '\n|-'
    #---
    Chart = Chart % (xline , yline)
    #---
    tables += u"\n|}\n"
    #---
    texts += Chart.replace("=,","=")
    texts += tables
    #---
    return texts
#---
sys_argv = sys.argv or []
#---
if u"test" in sys_argv:
    Limit[1] = 15000
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(u':')
    #---
    if arg.startswith('-') : arg = arg[1:]#print('change arg to %s ' % arg )
    #---
    if arg == "offset" or arg == "off" :
        Offset[1] = int(value)
    #---
    if arg == "limit":
        Limit[1] = int(value)
    #---
# python3 pwb.py dump/dump limit:1000000
#---
p31_no = { 1 : 0 }
#---
def make_textP31():
    #---
    tatone = """
{| class="wikitable sortable"
! # !! {{P|P31}} !! الاستخدام  
|-
%s
|}"""
    #---
    textP31 = ''
    #---
    for x , tab in p31_main_tab.items():
        section_others = 0
        if x in priffixeso and tab != {}:
            p31list = [[y, xfx] for xfx, y in tab.items()]
            try:
                p31list.sort(reverse=True)
            except:
                pywikibot.output('p31list.sort(reverse=True)')
                pywikibot.output(p31list)
            rows = []
            c = 1
            #for xx, yy in p31list[:500]:
            #---
            li = 100 
            if x != u'مقالة' : li = 10
            #---
            for xx, yy in p31list:
                #if xx > li : 
                if xx > li and len(rows) < 150 : 
                    yf = u"{{Q|%s}}" % yy
                    if yy != u"no" : 
                        rows.append( u'| %s || %s || %s ' % ( c, yf, xx ))
                    c += 1
                else:
                    section_others += xx
            #---
            #for xd, ny in p31list[500:]:
                #section_others += xd
            #---
            if rows != [] :
                rows = '\n|-\n'.join(rows)
                #---
                P31_table = tatone % rows
                #---
                #df = u"\n;%s\n" % x
                df = u"\n=== %s ===\n" % x.replace(':','')
                #---
                textP31 = textP31 + df + P31_table
                #---
    #---
    return textP31
#---
def mainar():
    #p31_no[1] = 0
    #---
    start = time.time()
    t1 = time.time()
    #---
    no_claims = 0
    #---
    c = 0
    dumpdate = 'latest'
    f = bz2.open('/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2' , 'r')
    #---
    try:
        pywikibot.output( 'len of f lines :%d ' % len(f) )
    except:
        print('')
    #---
    others = 0
    #---
    #---
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1
        if c < Limit[1] :
            if c > Offset[1]: 
                #---
                if line.startswith('{') and line.endswith('}'):
                    #---
                    p31_no_ar_lab = []
                    #---
                    if "printline" in sys_argv and ( c % 1000 == 0 or c == 1 ) :
                        pywikibot.output( line ) 
                    #---
                    All_items[1] += 1
                    json1 = json.loads(line)
                    q = json1['id']
                    #---
                    if 'sitelinks' in json1 and not 'arwiki' in json1['sitelinks'] :
                        sitelinks_no_ar[1] += 1
                    #---
                    if 'sitelinks' in json1 and ('arwiki' in json1['sitelinks']):
                        #---
                        All_ar_sitelinks[1] += 1
                        #---
                        arlink = json1['sitelinks']['arwiki']['title']
                        #pywikibot.output(arlink)
                        arlink_type = u"مقالة"
                        #---
                        # { u"count" : 0 , u"labels" : 0 , u"descriptions" : 0 ,u"aliases" : 0 }
                        for pri in priffixes:
                            if arlink.startswith( pri ) :
                                priffixes[pri][u"count"] += 1
                                arlink_type = pri
                                break
                        #---
                        if not arlink_type in p31_main_tab:
                            p31_main_tab[arlink_type] = {}
                        #---
                        if arlink_type == u"مقالة" : 
                            priffixes[u"مقالة"][u"count"] += 1
                        #---
                        p31x = 'no' 
                        #---
                        if 'claims' in json1 and 'P31' in json1['claims']:
                            for x in json1['claims']['P31']:
                                p31x = x.get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id')
                                #if 'mainsnak' in x and \
                                 #  'datavalue' in x['mainsnak'] and \
                                  # 'value' in x['mainsnak']['datavalue'] and \
                                   #'id' in x['mainsnak']['datavalue']['value']:
                                    #p31x = x['mainsnak']['datavalue']['value']['id']
                                #else:
                                    #continue
                                #if p31x:
                                    #print(q, 'P31', p31x , json1['sitelinks']['arwiki']  )
                                #---
                                if p31x :
                                    if not p31x in p31_no_ar_lab:
                                        p31_no_ar_lab.append(p31x)
                                    #---
                                    if p31x in p31_main_tab[arlink_type]:
                                        p31_main_tab[arlink_type][p31x] += 1
                                    else:
                                        p31_main_tab[arlink_type][p31x] = 1
                                    #---
                                #---
                        #---
                        elif u'claims' in json1 :
                            p31_no[1] += 1
                        else:
                            p31_no[1] += 1
                            no_claims += 1
                        #---{ "yesar" : 0 , "noar" : 0 , "no" : 0 , "yes" : 0 }
                        if 'labels' in json1 :
                            priffixes[arlink_type]['labels'][u"yes"] += 1
                            #---
                            # تسمية عربي
                            if u'ar' in json1['labels']:
                                priffixes[arlink_type][u"labels"]["yesar"] += 1
                            else:
                                priffixes[arlink_type][u"labels"]["noar"] += 1
                        else:
                            # دون عربي
                            priffixes[arlink_type][u"labels"]["no"] += 1
                        #---
                        #if 'descriptions' in json1 and u'ar' in json1['descriptions']:
                                #priffixes[arlink_type][u"descriptions"] += 1
                        #---
                        if 'descriptions' in json1 :
                            priffixes[arlink_type]['descriptions'][u"yes"] += 1
                            #---
                            # تسمية عربي
                            if u'ar' in json1['descriptions']:
                                priffixes[arlink_type][u"descriptions"]["yesar"] += 1
                            else:
                                priffixes[arlink_type][u"descriptions"]["noar"] += 1
                        else:
                            # دون عربي
                            priffixes[arlink_type][u"descriptions"]["no"] += 1
                        #---
                        #if 'aliases' in json1 and u'ar' in json1['aliases']:
                                #priffixes[arlink_type][u"aliases"] += 1
                        #---
                        if 'aliases' in json1 :
                            priffixes[arlink_type]['aliases'][u"yes"] += 1
                            #---
                            # تسمية عربي
                            if u'ar' in json1['aliases']:
                                priffixes[arlink_type][u"aliases"]["yesar"] += 1
                            else:
                                priffixes[arlink_type][u"aliases"]["noar"] += 1
                        else:
                            # دون عربي
                            priffixes[arlink_type][u"aliases"]["no"] += 1
                    #---
                    #else:
                    #---
                    ar_desc = json1.get('descriptions',{}).get('ar',False)
                    if u'p31' in sys_argv:
                        #---
                        if not ar_desc :
                            for x in json1.get('claims',{}).get('P31',[]):
                                p31d = x.get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id')
                                #---
                                #if not p31d in p31_no_ar_lab:
                                    #p31_no_ar_lab.append(p31d)
                                #---
                                #if p31d in Table_no_ab2 and not q in Table_no_ab2[p31d] :
                                   #Table_no_ab2[p31d].append(q)
                                #else:
                                    #Table_no_ab2[p31d] = [q]
                                #---
                                if p31d:
                                    if p31d in Table_no_ar_lab  :
                                        Table_no_ar_lab[p31d] += 1
                                    else:
                                        Table_no_ar_lab[p31d] = 1
                        #---
                    #---
                        #if c % 1000 == 0:
                            #print(q, 'P31', p31x , json1['sitelinks']['arwiki']["title"]  )
                            #try:
                                #pywikibot.output(q + ' P31 ' + p31x + " " +  json1['sitelinks']['arwiki'] )
                            #except:
                                #pywikibot.output(q + ' P31 ' + p31x )
                        #---
                #---
                if c % 1000 == 0:
                    dii = time.time()-t1
                    pywikibot.output( 'c:%d, time:%d' % (c, dii ) )
                    t1 = time.time()
                #pywikibot.output([[y, x] for x, y in p31_main_tab.items()])
                #---
            else:
                if c % 1000 == 0:
                    dii = time.time()-t1
                    pywikibot.output( 'Offset c:%d, time:%d' % (c, dii ) )
            #---
        else:
            break
    #---
    #---
    #---
    text = u""
    final = time.time()
    delta = int( final - start )
    #---
    text = u"* تقرير تاريخ: " + dumpdate + u" تاريخ التعديل ~~~~~.\n"
    text += u"* جميع عناصر ويكي بيانات المفحوصة: %d \n" % All_items[1]
    text += u"* عناصر ويكي بيانات بها وصلة عربية: %d \n" % All_ar_sitelinks[1]
    text += u"* عناصر بوصلات لغات بدون وصلة عربية: %d \n" % sitelinks_no_ar[1]
    text += u"<!-- bots work done in %d secounds --> \n" % delta
    text += u"__TOC__\n"
    #---
    NS_table = ns_stats()
    #---
    text = text + NS_table
    #---
    #---
    no_P31 = p31_no[1]
    #---
    #---
    textP31 = make_textP31()
    #---
    P31_secs_Old = """
== استخدام خاصية P31 == 
* %s صفحة بدون خاصية P31.
* %s صفحة بها خواص أخرى دون خاصية P31.
* %s صفحة دون أية خواص.
""" % ( no_P31 , p31_no[1] , no_claims )
    #--- 
    #--- 
    P31_secs = '== استخدام خاصية P31 == '
    P31_secs += '\n* %s صفحة بدون خاصية P31.' % no_P31
    P31_secs += '\n* %s صفحة بها خواص أخرى دون خاصية P31.' % p31_no[1]
    P31_secs += '\n* %s صفحة دون أية خواص.' % no_claims
    #--- 
    text = text + u"\n" + P31_secs + u"\n" + textP31.strip() + u"\n"
    #---
    Table_no_ar_lab_rows = []
    #---
    #po_list = [ [ len(dyy) , xxx] for xxx, dyy in Table_no_ab2.items() ]
    po_list = [ [ dyy , xxx] for xxx, dyy in Table_no_ar_lab.items() ]
    #---
    po_list.sort(reverse=True)
    cd = 0
    for xf, gh in po_list:
        #if xf > 100 : 
        if len(Table_no_ar_lab_rows) < 100 : 
            cd += 1
            yf = u"{{Q|%s}}" % gh
            Table_no_ar_lab_rows.append( u'| %s || %s || %s ' % (cd, yf, xf))
    Table_no_ar = '\n|-\n'.join(Table_no_ar_lab_rows)
    #---
    P31_table_no = """
== استخدام خاصية P31 بدون وصف عربي == 
{| class="wikitable sortable"
! # !! {{P|P31}} !! الاستخدامات
|-
%s
|}""" % Table_no_ar 
    #---
    text = text + u"\n" + P31_table_no
    #---
    if text != "" : 
        pywikibot.output( text )
        if not "nosave" in sys_argv:
            from API import arAPI 
            arAPI.page_put(oldtext="", newtext=text, summary=u'Bot - Updating stats', title=title)
    #---
    if not 'test' in sys_argv :
        with open( main_dir +  u'dump/arw2.txt' , 'w' ) as f:
            f.write(text)
        #---
        for qid, List in Table_no_ab2.items() :
            if len(List) > 1000 :
                tex = "\n".join( List )
                with open( main_dir +  u'dump/ar/%s.txt' % qid , 'w' ) as f:
                    f.write(tex)
        #---
    #---
    #---
if __name__ == '__main__':
    mainar()
#---

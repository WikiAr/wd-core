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
import os
import bz2
import json
import time
import pywikibot
#---
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
if not Dump_Dir.endswith('/'): Dump_Dir += '/'
#---
print(f'Dump_Dir: {Dump_Dir}')
#---
title = 'ويكيبيديا:مشروع_ويكي_بيانات/تقرير_P31'
#---
fancota = {
    "count" : 0,
    "labels" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
    "descriptions" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
    "aliases" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
    }
#---
priffixeso = [
    "مقالة",
    "نقاش:",
    "مستخدم:",
    "نقاش المستخدم:",
    "ويكيبيديا:",
    "نقاش ويكيبيديا:",
    "ملف:",
    "نقاش الملف:",
    "ميدياويكي:",
    "نقاش ميدياويكي:",
    "قالب:",
    "نقاش القالب:",
    "مساعدة:",
    "نقاش المساعدة:",
    "تصنيف:",
    "نقاش التصنيف:",
    "بوابة:",
    "نقاش البوابة:",
    "وحدة:",
    "نقاش الوحدة:",
    "إضافة:",
    "نقاش الإضافة:",
    "تعريف الإضافة:",
    "نقاش تعريف الإضافة:",
    "موضوع:",
    ]
#---
priffixes = {}
#---
for x in priffixeso:
    priffixes[x] = {
        "count" : 0,
        "labels" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
        "descriptions" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
        "aliases" : { "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 },
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
    #lists = [ [ y["count"] , x ] for x, y in priffixes.items()]
    #lists.sort(reverse=True)
    #---
    #for x , ns in lists :
        #count = x # priffixes[ns]["count"] 
    for ns in priffixes : 
        count = priffixes[ns]["count"] 
        #pywikibot.output('priffixes[ns]')
        #pywikibot.output(priffixes[ns])
        #pywikibot.output('priffixes[ns]')
        if count != 0 :  
            #w_la = count - priffixes[ns]["labels"]
            #w_de = count - priffixes[ns]["descriptions"]
            #w_al = count - priffixes[ns]["aliases"]
            ns2 = ns.replace(":","")
            tables += '\n'
            #---
            row = "| %s || %d" % ( ns2 , count )
            xline += ",%s" % ns2
            yline += ",%d" % count
            #---{ "yes" : 0 , "no" : 0 , "yesar" : 0 , "noar" : 0 }
            fafa = "\n| %d || %d || %d || %d" 
            row += fafa % ( priffixes[ns]["labels"]["yes"],priffixes[ns]["labels"]["no"],priffixes[ns]["labels"]["yesar"],priffixes[ns]["labels"]["noar"] )
            #---
            row += fafa % ( priffixes[ns]["descriptions"]["yes"],priffixes[ns]["descriptions"]["no"],priffixes[ns]["descriptions"]["yesar"],priffixes[ns]["descriptions"]["noar"] )
            #---
            row += fafa % ( priffixes[ns]["aliases"]["yes"],priffixes[ns]["aliases"]["no"],priffixes[ns]["aliases"]["yesar"],priffixes[ns]["aliases"]["noar"] )
            #---
            tables += row
            tables += '\n|-'
    #---
    Chart = Chart % (xline , yline)
    #---
    tables += "\n|}\n"
    #---
    texts += Chart.replace("=,","=")
    texts += tables
    #---
    return texts
#---
#---
if "test" in sys.argv:
    Limit[1] = 15000
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(':')
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
    for x, tab in p31_main_tab.items():
        section_others = 0
        #---
        if not x in priffixeso or tab == {}: continue
        #---
        p31list = [[y, xfx] for xfx, y in tab.items()]
        #---
        try:
            p31list.sort(reverse=True)
        except:
            pywikibot.output('p31list.sort(reverse=True)')
            pywikibot.output(p31list)
        #---
        rows = []
        c = 1
        #---
        li = 100 
        if x != 'مقالة' : li = 10
        #---
        for xx, yy in p31list:
            if xx > li and len(rows) < 150 : 
                yf = "{{Q|%s}}" % yy
                #---
                if yy != "no" :    rows.append( '| %s || %s || %s ' % ( c, yf, xx ))
                #---
                c += 1
            else:
                section_others += xx
        #---
        #for xd, ny in p31list[500:]: section_others += xd
        #---
        if rows == [] : continue
        #---
        rows = '\n|-\n'.join(rows)
        #---
        P31_table = tatone % rows
        #---
        #df = "\n;%s\n" % x
        df = "\n=== %s ===\n" % x.replace(':','')
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
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    #---
    if not os.path.isfile(filename):
        pywikibot.output( f'file {filename} <<lightred>> not found' )
        return
    #---
    f = bz2.open(filename, 'r')
    #---
    try:
        pywikibot.output( 'len of f lines :%d ' % len(f) )
    except:
        print("can't make len of file...")
    #---
    if f == None or f == '' or f == []:
        print(f'file {filename} is empty')
        return
    #---
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        #---
        if not line.startswith('{') or not line.endswith('}'): continue
        #---
        c += 1
        #---
        if c < Limit[1] : break
        #---
        if c < Offset[1]: 
            if c % 1000 == 0:
                dii = time.time()-t1
                pywikibot.output( 'Offset c:%d, time:%d' % (c, dii ) )
            continue
        #---
        if c % 1000 == 0:
            dii = time.time()-t1
            pywikibot.output( 'c:%d, time:%d' % (c, dii ) )
            t1 = time.time()
        #---
        if "printline" in sys.argv and ( c % 1000 == 0 or c == 1 ) :
            pywikibot.output( line ) 
        #---
        # جميع عناصر ويكي بيانات المفحوصة
        All_items[1] += 1
        #---
        json1 = json.loads(line)
        q = json1['id']
        #---
        sitelinks = json1.get('sitelinks',{})
        #---
        if not sitelinks or sitelinks == {} : continue
        #---
        arwiki = sitelinks.get('arwiki',{})
        #---
        if arwiki == {} :
            # عناصر بوصلات لغات بدون وصلة عربية
            sitelinks_no_ar[1] += 1
            continue
        #---
        p31_no_ar_lab = []
        #---
        arlink = arwiki.get('title', '')
        #---
        if arlink == '' : continue
        #---
        # عناصر ويكي بيانات بها وصلة عربية
        All_ar_sitelinks[1] += 1
        #---
        arlink_type = "مقالة"
        #---
        for pri in priffixes:
            if arlink.startswith( pri ) :
                priffixes[pri]["count"] += 1
                arlink_type = pri
                break
        #---
        if not arlink_type in p31_main_tab:
            p31_main_tab[arlink_type] = {}
        #---
        if arlink_type == "مقالة" : 
            priffixes["مقالة"]["count"] += 1
        #---
        p31x = 'no' 
        #---
        claims = json1.get('claims',{})
        #---
        if claims == {} :
            # صفحات دون أية خواص
            no_claims += 1
        #---
        P31 = claims.get('P31',{})
        #---
        if P31 == {} :
            # صفحة بدون خاصية P31
            p31_no[1] += 1
        #---
        for x in P31:
            p31x = x.get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id')
            #---
            if not p31x : continue
            #---
            if not p31x in p31_no_ar_lab:   p31_no_ar_lab.append(p31x)
            #---
            if not p31x in p31_main_tab[arlink_type]:   p31_main_tab[arlink_type][p31x] = 0
            #---
            p31_main_tab[arlink_type][p31x] += 1
            #---
        #---
        tat = ['labels', 'descriptions', 'aliases']
        #---
        for x in tat:
            #---
            if not x in json1 :
                # دون عربي
                priffixes[arlink_type][x]["no"] += 1
                continue
            #---
            priffixes[arlink_type][x]["yes"] += 1
            #---
            # تسمية عربي
            if 'ar' in json1[x]:
                priffixes[arlink_type][x]["yesar"] += 1
            else:
                priffixes[arlink_type][x]["noar"] += 1
        #---
        ar_desc = json1.get('descriptions',{}).get('ar',False)
        #---
        if not ar_desc :
            # استخدام خاصية 31 بدون وصف عربي
            for x in json1.get('claims',{}).get('P31',[]):
                p31d = x.get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id')
                #---
                if p31d:
                    if not p31d in Table_no_ar_lab  :   Table_no_ar_lab[p31d] = 0
                    #---
                    Table_no_ar_lab[p31d] += 1
    #---
    text = ""
    final = time.time()
    delta = int( final - start )
    #---
    text = "* تقرير تاريخ: " + dumpdate + " تاريخ التعديل ~~~~~.\n"
    text += "* جميع عناصر ويكي بيانات المفحوصة: %d \n" % All_items[1]
    text += "* عناصر ويكي بيانات بها وصلة عربية: %d \n" % All_ar_sitelinks[1]
    text += "* عناصر بوصلات لغات بدون وصلة عربية: %d \n" % sitelinks_no_ar[1]
    text += "<!-- bots work done in %d secounds --> \n" % delta
    text += "__TOC__\n"
    #---
    NS_table = ns_stats()
    #---
    text = text + NS_table
    #---
    no_P31 = p31_no[1]
    #---
    textP31 = make_textP31()
    #---
    P31_secs = '== استخدام خاصية P31 == '
    P31_secs += '\n* %s صفحة بدون خاصية P31.' % no_P31
    P31_secs += '\n* %s صفحة بها خواص أخرى دون خاصية P31.' % p31_no[1]
    P31_secs += '\n* %s صفحة دون أية خواص.' % no_claims
    #--- 
    text = text + "\n" + P31_secs + "\n" + textP31.strip() + "\n"
    #---
    Table_no_ar_lab_rows = []
    #---
    po_list = [ [ dyy , xxx] for xxx, dyy in Table_no_ar_lab.items() ]
    #---
    po_list.sort(reverse=True)
    cd = 0
    for xf, gh in po_list:
        #if xf > 100 : 
        if len(Table_no_ar_lab_rows) < 100 : 
            cd += 1
            yf = "{{Q|%s}}" % gh
            Table_no_ar_lab_rows.append( '| %s || %s || %s ' % (cd, yf, xf))
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
    text = text + "\n" + P31_table_no
    #---
    if All_items[1] == 0 :
        print('nothing to update')
        return
    #---
    if text != "" : 
        pywikibot.output( text )
        if not "nosave" in sys.argv:
            from API import arAPI 
            arAPI.page_put(oldtext="", newtext=text, summary='Bot - Updating stats', title=title)
    #---
    if not 'test' in sys.argv :
        with open( Dump_Dir +  'dumps/arw2.txt' , 'w' ) as f:
            f.write(text)
        #---
        for qid, List in Table_no_ab2.items() :
            if len(List) > 1000 :
                tex = "\n".join( List )
                with open( Dump_Dir +  'ar/%s.txt' % qid , 'w' ) as f:
                    f.write(tex)
#---
if __name__ == '__main__':
    mainar()
#---

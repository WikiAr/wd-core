#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


python3 pwb.py dump/p31 jsonnew
python3 pwb.py dump/p31 claimse4
python3 pwb.py dump/p31 makereport claimse4
python3 pwb.py dump/p31
python3 pwb.py dump/p31 test nosave

67474000 : 0.4667012691497803.
67475000 : 0.410783052444458.


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import sys
import os
import bz2
#import gz
import json
import time
import pywikibot

Dump_Dir = os.path.dirname(os.path.realpath(__file__))
if not Dump_Dir.endswith('/'): Dump_Dir += '/'

print(f'Dump_Dir: {Dump_Dir}')

#ar_site = pywikibot.Site('ar', 'wikipedia')
title = 'User:Mr. Ibrahem/p31'

Limit = { 1 : 500000000 } 
saveto = { 1 : '' } 

# python3 pwb.py wd/dump test 

if sys.argv and "test" in sys.argv:
    Limit[1] = 30010

for arg in sys.argv:

    arg, sep, value = arg.partition(':')

    if arg.startswith('-') : arg = arg[1:]

    if arg == "limit":
        Limit[1] = int(value)

    if arg == "saveto":
        saveto[1] = value

tab = {} 
tab['done'] = 0
tab['items_0_claims'] = 0
tab['items_1_claims'] = 0
tab['items_no_P31'] = 0
tab['All_items'] = 0
tab['all_claims_2020'] = 0
#tab['lenth_of_claims_for_property'] = {} 
#tab['lenth_of_usage'] = {} 
tab['Main_Table'] = {} 

lamo = [
    'done',
    'items_0_claims',
    'items_1_claims',
    'items_no_P31',
    'All_items',
    'all_claims_2020',
    #'lenth_of_claims_for_property',
    #'lenth_of_usage',
    'Main_Table',
    ]

jsonname = Dump_Dir + 'dumps/claimsep31.json'

jsonname2 = jsonname
#---python3 pwb.py dump/p31 jsonnew
if 'jsonnew' in sys.argv:
    with open( jsonname , 'w' ) as fe:
        fe.write('{}')
        pywikibot.output( "clear jsonname:%s" % jsonname )

elif not 'test' in sys.argv :
    try:
        ff = open( jsonname2 , 'r' ).read()
        SS = json.loads( ff )
        tab = SS
        pywikibot.output( "tab['done'] == %d" % tab['done'] )
    except:
        pywikibot.output('cant read %s ' % jsonname )

sections_done = { 1 : 0 }
sections_false = { 1 : 0 }

def make_section( P , table , Len ):
    texts = '== {{P|%s}}  =='  % P

    if sections_done[1] == 50 : 
        return ''

    pywikibot.output( ' make_section for property:%s' % P )

    texts += '\n* Total items use these property:%d' % Len

    if tab['Main_Table'].get(P,{}).get('lenth_of_claims_for_property'):
        texts += '\n* Total number of claims with these property:%d' % tab['Main_Table'].get(P,{}).get('lenth_of_claims_for_property')
    texts += '\n'

    pywikibot.output( texts )

    if table['props'] == {} :
        pywikibot.output( '%s table["props"] == {} ' % P )
        return ''

    xline = '' # |x=مقالة,تصنيف,قالب,بوابة,ويكيبيديا,وحدة,مساعدة,ملف
    yline = '' # |y1=718532,564152,46493,4292,1906,850,137,7
    #---style="text-align:left"
    Chart = """
{| class="floatright sortable" 
|-
|
{{Graph:Chart|width=140|height=140|xAxisTitle=value|yAxisTitle=Number
|type=pie|showValues1=offset:8,angle:45
|x=%s
|y1=%s
|legend=value
}}
|-
|}"""

    tables = """
{| class="wikitable sortable plainrowheaders"
|-
! class="sortable" | #
! class="sortable" | value
! class="sortable" | Numbers
|-
"""

    lists = [ [ y , xff ] for xff, y in table['props'].items()]
    lists.sort(reverse=True)

    num = 0

    other = 0

    for ye , x in lists :

        #if ye == 0 or ye == 1 and sections_false[1] < 100:
        if ye == 0 and sections_false[1] < 100:
            pywikibot.output( 'p(%s),x(%s) ye == 0 or ye == 1 ' % (P,x) )
            sections_false[1] += 1
            return ''

        num += 1
        #if num == 51 : 
            #break

        if num < 501 : 

            tables += '\n'
            if x.startswith('Q'):
                row = "| %d || {{Q|%s}} || {{subst:formatnum:%d}} " % ( num , x , ye )
            else:
                row = "| %d || %s || {{subst:formatnum:%d}} " % ( num , x , ye )
            xline += ",%s" % x
            yline += ",%d" % ye

            tables += row
            tables += '\n|-'
        else:
            other += ye

    num += 1 

    #tables += '\n|-'
    tables += "\n| %d || others || {{subst:formatnum:%d}} " % ( num,other)
    tables += '\n|-'

    Chart = Chart % ( xline , yline )

    tables += "\n|}\n{{clear}}\n"

    texts += Chart.replace("=,","=")
    texts += tables

    sections_done[1] += 1

    return texts

ttypes = [
    "wikibase-entityid",
    "time",
    "monolingualtext",
    "quantity",
    #"string",
    ]

dump_done = { 1 : 0 }

def log_dump():
    if not 'test' in sys.argv :
        with open(jsonname, 'w') as outfile:
            json.dump( tab , outfile )
        dump_done[1] += 1
        pywikibot.output( 'log_dump %d done ' % dump_done[1] )

def workondata():
    t1 = time.time()
    diff = 20000

    if 'test' in sys.argv:
        diff = 1000

    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'

    if not os.path.isfile(filename):
        pywikibot.output( f'file {filename} <<lightred>> not found' )
        return

    fileeee = bz2.open(filename, 'r')

    if 'lene' in sys.argv:
        pywikibot.output( 'len of bz2 lines :%d ' % len( json.loads( [ x for x in fileeee if x.startswith('{') and x.endswith('}') ] ) ) )

    done2 = 0
    done = 0
    offset = 0

    if tab['done'] != 0 :
        offset = tab['done']
        pywikibot.output( 'offset == %d' % offset )

    log_done = 0

    for line in fileeee:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        done += 1

        if offset != 0 and done < offset: 
            continue

        if tab['done'] > Limit[1] :  break

        if "output" in sys.argv and tab['done'] < 2 : 
            pywikibot.output( line )

        if line.startswith('{') and line.endswith('}'):

            done2 += 1

            tab['All_items'] += 1

            if "printline" in sys.argv and tab['done'] % 1000 == 0:
                pywikibot.output( line ) 

            json1 = json.loads(line)

            claimse = json1.get('claims',{})

            if len(claimse) == 1 :
                tab['items_1_claims'] += 1

            if not 'P31' in claimse :
                tab['items_no_P31'] += 1
                tab['items_no_P31'] += 1
                continue
            elif len(claimse) == 0 :
                tab['items_0_claims'] += 1
                continue

            P31 = 'P31'

            if not P31 in tab['Main_Table']:
                tab['Main_Table'][P31] = {'props' : {} , 'lenth_of_usage' : 0  , 'lenth_of_claims_for_property' : 0 }

            tab['Main_Table'][P31]['lenth_of_usage'] += 1

            tab['all_claims_2020'] += len(json1['claims'][P31])

            for claim in json1['claims'][P31]:

                #tab['lenth_of_claims_for_property'][P31] += 1
                tab['Main_Table'][P31]['lenth_of_claims_for_property'] += 1

                #pywikibot.output( claim ) 
                #id = P31[claim].get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id')


                datavalue = claim.get('mainsnak',{}).get('datavalue',{})#.get('value',{}).get('id')
                ttype = datavalue.get('type')

                val = datavalue.get('value',{})

                if ttype == "wikibase-entityid":
                    #pywikibot.output( datavalue['value'] ) 
                    id = datavalue.get('value',{}).get('id')
                    if id :
                        if id in tab['Main_Table'][P31]['props']:
                            tab['Main_Table'][P31]['props'][id] += 1 
                        else:
                            tab['Main_Table'][P31]['props'][id] = 1


            tab['done'] = done


        #pywikibot.output([[y, x] for x, y in p31.items()])

        if done % diff == 0 or done == 1000:
            pywikibot.output('{} : {}.'.format( done, time.time()-t1) )
            t1 = time.time()

        #if done2 % diff == 0 or done2 == 100000:
            #if done2 != log_done :
                #log_done = done2
                #log_dump()

        if done2 == 500000:
            done2 = 1
            log_dump()

dumpdate = 'latest'

def mainar():

    time_start = time.time()

    pywikibot.output('time_start:%s' % str(time_start) )

    sections = ''
    #---s
    if not 'makereport' in sys.argv :
        workondata()

    property_other = 0

    p31list = [[y['lenth_of_usage'], x] for x, y in tab['Main_Table'].items() if y['lenth_of_usage'] != 0 ]
    p31list.sort(reverse=True) 

    for Len , P in p31list:
        sections += make_section( P , tab['Main_Table'][P] , Len )

    final = time.time()
    delta = int( final - time_start )

    text = ""
    text = "Update: <onlyinclude>%s</onlyinclude>.\n" % dumpdate
    text += "* Total items:{{subst:formatnum:%d}} \n" % tab['All_items']
    text += "* Items without P31:{{subst:formatnum:%d}} \n" % tab['items_no_P31']
    text += "* Items with 1 claim only:{{subst:formatnum:%d}} \n" % tab['items_1_claims']
    text += "* Items with no claim:{{subst:formatnum:%d}} \n" % tab['items_0_claims']
    text += "* Total number of claims:{{subst:formatnum:%d}} \n" % tab['all_claims_2020']
    text += "<!-- bots work done in %d secounds --> \n" % delta
    text += "--~~~~~\n"

    text = text + "\n" + sections
    text = text.replace( "0 (0000)" , "0" )
    text = text.replace( "0 (0)" , "0" )

    title = 'User:Mr. Ibrahem/p31'

    # python3 pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != '' :
        with open( Dump_Dir + 'dumps/%s.txt' % saveto[1] , 'w' ) as f:
            f.write(text)

    if text == "" : return

    if 'test' in sys.argv and not 'noprint' in sys.argv :
        pywikibot.output( text )

    if not "nosave" in sys.argv:

        if 'test' in sys.argv : title = 'User:Mr. Ibrahem/p311'

        from wd_API import himoAPI
        himoAPI.page_putWithAsk( '' , text , 'Bot - Updating stats' , title, False)

        # with open( jsonname, 'w' ) as fe: fe.write('{}')

    to_log = Dump_Dir + 'dumps/p31.txt'

    if 'test' in sys.argv :
        to_log = Dump_Dir + 'dumps/p31_1.txt'

    with open( to_log , 'w' ) as f:
        f.write(text)

if __name__ == '__main__':
    #pywikibot.output(make_cou( 70900911 , 84601659 ))
    mainar()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python3 pwb.py dump/claims5 jsonnew
python3 pwb.py dump/claims5 makereport
python3 pwb.py dump/claims5
python3 pwb.py dump/claims5 test nosave
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
import json
import time
import pywikibot
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
if not Dump_Dir.endswith('/'): Dump_Dir += '/'
print(f'Dump_Dir: {Dump_Dir}')
title = 'User:Mr. Ibrahem/claims'
Limit = { 1 : 500000000 } 
saveto = { 1 : '' } 
if sys.argv and "test" in sys.argv:
    Limit[1] = 30010
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    if arg.startswith('-') : arg = arg[1:]
    if arg == "limit":
        Limit[1] = int(value)
    if arg == "saveto":
        saveto[1] = value
# python3 pwb.py dump/dump limit:1000000
tab = {} 
tab['done'] = 0
tab['len_of_all_properties'] = 0
tab['items_1_claims'] = 0
tab['items_no_claims'] = 0
tab['All_items'] = 0
tab['all_claims_2020'] = 0
#tab['lenth_of_claims_for_property'] = {} 
#tab['lenth_of_usage'] = {} 
tab['Main_Table'] = {} 
lamo = [
    'done',
    'len_of_all_properties',
    'items_1_claims',
    'items_no_claims',
    'All_items',
    'all_claims_2020',
    #'lenth_of_claims_for_property',
    #'lenth_of_usage',
    'Main_Table',
    ]
jsonname = Dump_Dir + 'dumps/claimse.json'
#---claimse4.json
jsonname2 = jsonname
if 'claimse4' in sys.argv : jsonname2 = Dump_Dir + 'dumps/claimse4.json'
#---python3 pwb.py dump/claims5 jsonnew
if 'jsonnew' in sys.argv:
    with open( jsonname , 'w' ) as fe:
        fe.write('{}')
        pywikibot.output( "clear jsonname:%s" % jsonname )
elif 'test' not in sys.argv :
    try:
        ff = open( jsonname2 , 'r' ).read()
        SS = json.loads( ff )
        tab = SS
        #for x in lamo :
            #g = SS.get(x)
            #if g != {} and g != 0 : tab[x] = g
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
    xline = ''
    yline = ''
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
        if num < 51 : 
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
    if 'test' not in sys.argv :
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
        if done % diff == 0 or done == 1000:
            pywikibot.output('{} : {}.'.format( done, time.time()-t1) )
            t1 = time.time()
        if done2 == 500000:
            done2 = 1
            log_dump()
        if tab['done'] > Limit[1] : break
        if "output" in sys.argv and tab['done'] < 2 : 
            pywikibot.output( line )
        if not line.startswith('{') or not line.endswith('}'): continue
        done2 += 1
        tab['All_items'] += 1
        if "printline" in sys.argv and tab['done'] % 1000 == 0:
            pywikibot.output( line ) 
        json1 = json.loads(line)
        claimse = json1.get('claims',{})
        if claimse == {} :
            tab['items_no_claims'] += 1
        if len(claimse) == 1 :
            tab['items_1_claims'] += 1
        for P31 in claimse:
            if not P31 in tab['Main_Table']:
                tab['Main_Table'][P31] = {'props' : {} , 'lenth_of_usage' : 0  , 'lenth_of_claims_for_property' : 0 }
            #if not P31 in tab['lenth_of_usage']:   tab['lenth_of_usage'][P31] = 0
            #if not P31 in tab['lenth_of_claims_for_property']: tab['lenth_of_claims_for_property'][P31] = 0
            #tab['lenth_of_usage'][P31] += 1
            tab['Main_Table'][P31]['lenth_of_usage'] += 1
            tab['all_claims_2020'] += len(claimse[P31])
            for claim in claimse[P31]:
                tab['Main_Table'][P31]['lenth_of_claims_for_property'] += 1
                datavalue = claim.get('mainsnak',{}).get('datavalue',{})
                ttype = datavalue.get('type')
                '''
                if ttype == "wikibase-entityid":
                    #if ('value' in datavalue) and ('id' in datavalue['value']):
                        #pywikibot.output( datavalue['value'] ) 
                        id = datavalue['value']['id']
                        if id in tab['Main_Table'][P31]:
                            tab['Main_Table'][P31][id] += 1 
                        else:
                            tab['Main_Table'][P31][id] = 1
                '''
                val = datavalue.get('value',{})
                if ttype == "wikibase-entityid":
                    id = datavalue.get('value',{}).get('id')
                    if id :
                        if not id in tab['Main_Table'][P31]['props']: tab['Main_Table'][P31]['props'][id] = 0
                        tab['Main_Table'][P31]['props'][id] += 1 
                '''elif ttype in ttypes:
                    continue
                    #pywikibot.output( datavalue['value'] ) 
                    #id = datavalue.get('value',{}).get('id')
                    id = val.get('id') or val.get('time') or val.get('text') or val.get('amount')
                    if id:
                        if id in tab['Main_Table'][P31]['props']:
                            tab['Main_Table'][P31]['props'][id] += 1 
                        else:
                            tab['Main_Table'][P31]['props'][id] = 1
                elif ttype == "string":
                    value = datavalue.get('value')
                    if value:
                        if value in tab['Main_Table'][P31]['props']:
                            tab['Main_Table'][P31]['props'][value] += 1 
                        else:
                            tab['Main_Table'][P31]['props'][value] = 1
                        dd34535 = {"datavalue": {"value": "Landforms of Guatemala","type": "string"} }
                elif ttype == "globecoordinate":
                    cord = str(val.get('latitude','')) + ',' + str(val.get('longitude',''))
                    if cord:
                        if cord in tab['Main_Table'][P31]['props']:
                            tab['Main_Table'][P31]['props'][cord] += 1 
                        else:
                            tab['Main_Table'][P31]['props'][cord] = 1
                        dddff = { "datavalue": {"value": {
                                    "latitude": 15.5,
                                    "longitude": 48,
                                    "altitude": 'null',
                                    "precision": 0.1,
                                    "globe": "http://www.wikidata.org/entity/Q2"
                                },"type": "globecoordinate"}
                            }
                #---'''
        tab['done'] = done
    log_dump()
dumpdate = 'latest'
def mainar():
    time_start = time.time()
    pywikibot.output('time_start:%s' % str(time_start) )
    sections = ''
    xline = '' 
    yline = '' 
    #---style="text-align:left"
    Chart2 = """
{| class="floatright sortable" 
|-
|
{{Graph:Chart|width=900|height=100|xAxisTitle=property|yAxisTitle=usage|type=rect
|x=%s
|y1=%s
}}
|-
|}"""
    if 'makereport' not in sys.argv :
        workondata()
    property_other = 0
    tab['len_of_all_properties'] = 0 
    #p31list = [[y, x] for x, y in tab['lenth_of_usage'].items() if y != 0 ]
    p31list = [[y['lenth_of_usage'], x] for x, y in tab['Main_Table'].items() if y['lenth_of_usage'] != 0 ]
    p31list.sort(reverse=True) 
    rows = []
    for Len , P in p31list:
        tab['len_of_all_properties'] += 1 
        #if mni == 101 : 
        #if sections_done[1] == 50 : 
            #break
        if tab['len_of_all_properties'] < 27 : 
            xline += ",%s" % P
            yline += ",%d" % Len
        sections += make_section( P , tab['Main_Table'][P] , Len )
        if len(rows) < 51 : 
            rows.append( '| %d || {{P|%s}} || {{subst:formatnum:%d}} ' % ( tab['len_of_all_properties'] , P , Len )  )
        else:
            property_other += int(Len)
    #Chart2 = Chart2 % ( xline , yline )
    Chart2 = Chart2.replace( '|x=%s'  , '|x='  + xline )
    Chart2 = Chart2.replace( '|y1=%s' , '|y1=' + yline )
    Chart2 = Chart2.replace("=,","=")
    #mni += 1 
    #pywikibot.output(property_other)
    rows.append( '| 52 || others || {{subst:formatnum:%d}} ' % property_other  )
    rows = '\n|-\n'.join(rows)
    table = """
{| class="wikitable sortable"
|-
! #
! property
! usage
|-
%s
|}
""" % rows
    final = time.time()
    delta = int( final - time_start )
    text = ""
    text = "Update: <onlyinclude>%s</onlyinclude>.\n" % dumpdate
    text += "* Total items:{{subst:formatnum:%d}} \n" % tab['All_items']
    text += "* Items without claims:{{subst:formatnum:%d}} \n" % tab['items_no_claims']
    text += "* Items with 1 claim only:{{subst:formatnum:%d}} \n" % tab['items_1_claims']
    text += "* Total number of claims:{{subst:formatnum:%d}} \n" % tab['all_claims_2020']
    text += "* Number of properties of the report:{{subst:formatnum:%d}} \n" % tab['len_of_all_properties']
    text += "<!-- bots work done in %d secounds --> \n" % delta
    text += "--~~~~~\n"
    text = text + "== Numbers ==\n"
    text = text + "\n" + Chart2
    text = text + "\n" + table
    text = text + "\n" + sections
    text = text.replace( "0 (0000)" , "0" )
    text = text.replace( "0 (0)" , "0" )
    title = 'User:Mr. Ibrahem/claims'
    # python3 pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != '' :
        with open( Dump_Dir + 'dumps/%s.txt' % saveto[1] , 'w' ) as f:
            f.write(text)
    if text == "" : return ''
    if 'test' in sys.argv and 'noprint' not in sys.argv :
        pywikibot.output( text )
    if "nosave" not in sys.argv:
        if 'test' in sys.argv : title = 'User:Mr. Ibrahem/claims1'
        from wd_API import himoAPI
        himoAPI.page_putWithAsk( '' , text , 'Bot - Updating stats' , title, False)
        # with open( jsonname , 'w' ) as fe:  fe.write('{}')
    if 'test' not in sys.argv :
        with open( Dump_Dir + 'dumps/claims.txt' , 'w' ) as f:
            f.write(text)
    else:
        with open( Dump_Dir + 'dumps/claims1.txt' , 'w' ) as f:
            f.write(text)
if __name__ == '__main__':
    #pywikibot.output(make_cou( 70900911 , 84601659 ))
    mainar()
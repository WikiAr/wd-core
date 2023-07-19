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
if not Dump_Dir.endswith('/'):
    Dump_Dir += '/'
print(f'Dump_Dir: {Dump_Dir}')
title = 'User:Mr. Ibrahem/claims'
Limit = {1: 500000000}
saveto = {1: ''}
if sys.argv and "test" in sys.argv:
    Limit[1] = 30010
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    if arg.startswith('-'):
        arg = arg[1:]
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
tab['Main_Table'] = {}
lamo = [
    'done',
    'len_of_all_properties',
    'items_1_claims',
    'items_no_claims',
    'All_items',
    'all_claims_2020',
    'Main_Table',
]
jsonname = Dump_Dir + 'dumps/claimse.json'
# ---
jsonname2 = jsonname
# ---
if 'jsonnew' in sys.argv:
    with open(jsonname, 'w') as fe:
        fe.write('{}')
        pywikibot.output("clear jsonname:%s" % jsonname)
elif 'test' not in sys.argv:
    try:
        ff = open(jsonname2, 'r').read()
        SS = json.loads(ff)
        tab = SS
        pywikibot.output("tab['done'] == %d" % tab['done'])
    except:
        pywikibot.output('cant read %s ' % jsonname)
sections_done = {1: 0}
sections_false = {1: 0}


def make_section(P, table, Len):
    texts = '== {{P|%s}}  ==' % P
    if sections_done[1] == 50:
        return ''
    pywikibot.output(f'make_section for property:{P}')
    texts += f'\n* Total items use these property:{Len}'
    # ---
    lnnn = tab['Main_Table'].get(P, {}).get('lenth_of_claims_for_property')
    if lnnn:
        texts += f'\n* Total number of claims with these property:{lnnn}'
    # ---
    texts += '\n'
    pywikibot.output(texts)
    if table['props'] == {}:
        pywikibot.output('%s table["props"] == {} ' % P)
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
    lists = [[y, xff] for xff, y in table['props'].items()]
    lists.sort(reverse=True)
    num = 0
    other = 0
    for ye, x in lists:
        if ye == 0 and sections_false[1] < 100:
            pywikibot.output('p(%s),x(%s) ye == 0 or ye == 1 ' % (P, x))
            sections_false[1] += 1
            return ''
        num += 1
        if num < 51:
            tables += '\n'
            if x.startswith('Q'):
                row = "| %d || {{Q|%s}} || {{subst:formatnum:%d}} " % (num, x, ye)
            else:
                row = "| %d || %s || {{subst:formatnum:%d}} " % (num, x, ye)
            xline += ",%s" % x
            yline += ",%d" % ye
            tables += row
            tables += '\n|-'
        else:
            other += ye
    num += 1
    tables += f"\n| {num} || others || {other:,}\n|-"
    Chart = Chart % (xline, yline)
    tables += "\n|}\n{{clear}}\n"
    texts += Chart.replace("=,", "=")
    texts += tables
    sections_done[1] += 1
    return texts


ttypes = [
    "wikibase-entityid",
    "time",
    "monolingualtext",
    "quantity",
    # "string",
]
dump_done = {1: 0}


def log_dump():
    if 'test' not in sys.argv:
        with open(jsonname, 'w') as outfile:
            json.dump(tab, outfile)
        dump_done[1] += 1
        pywikibot.output('log_dump %d done ' % dump_done[1])


def workondata():
    t1 = time.time()
    diff = 20000
    if 'test' in sys.argv:
        diff = 1000
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    if not os.path.isfile(filename):
        pywikibot.output(f'file {filename} <<lightred>> not found')
        return
    fileeee = bz2.open(filename, 'r')
    if 'lene' in sys.argv:
        pywikibot.output('len of bz2 lines :%d ' % len(json.loads([x for x in fileeee if x.startswith('{') and x.endswith('}')])))
    done2 = 0
    done = 0
    offset = 0
    if tab['done'] != 0:
        offset = tab['done']
        pywikibot.output('offset == %d' % offset)
    log_done = 0
    for line in fileeee:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        done += 1
        if offset != 0 and done < offset:
            continue
        if done % diff == 0 or done == 1000:
            pywikibot.output('{} : {}.'.format(done, time.time()-t1))
            t1 = time.time()
        if done2 == 500000:
            done2 = 1
            log_dump()
        if tab['done'] > Limit[1]:
            break
        if "output" in sys.argv and tab['done'] < 2:
            pywikibot.output(line)
        if not line.startswith('{') or not line.endswith('}'):
            continue
        done2 += 1
        tab['All_items'] += 1
        if "printline" in sys.argv and tab['done'] % 1000 == 0:
            pywikibot.output(line)
        json1 = json.loads(line)
        claimse = json1.get('claims', {})
        if claimse == {}:
            tab['items_no_claims'] += 1
        if len(claimse) == 1:
            tab['items_1_claims'] += 1
        for P31 in claimse:
            if not P31 in tab['Main_Table']:
                tab['Main_Table'][P31] = {'props': {}, 'lenth_of_usage': 0, 'lenth_of_claims_for_property': 0}
            tab['Main_Table'][P31]['lenth_of_usage'] += 1
            tab['all_claims_2020'] += len(claimse[P31])
            for claim in claimse[P31]:
                tab['Main_Table'][P31]['lenth_of_claims_for_property'] += 1
                datavalue = claim.get('mainsnak', {}).get('datavalue', {})
                ttype = datavalue.get('type')
                val = datavalue.get('value', {})
                if ttype == "wikibase-entityid":
                    id = datavalue.get('value', {}).get('id')
                    if id:
                        if not id in tab['Main_Table'][P31]['props']:
                            tab['Main_Table'][P31]['props'][id] = 0
                        tab['Main_Table'][P31]['props'][id] += 1
        tab['done'] = done
    log_dump()


def mainar():
    time_start = time.time()
    pywikibot.output('time_start:%s' % str(time_start))
    sections = ''
    xline = ''
    yline = ''
    # ---
    Chart2 = "{| class='floatright sortable' \n|-\n|"
    Chart2 += "{{Graph:Chart|width=900|height=100|xAxisTitle=property|yAxisTitle=usage|type=rect\n|x=%s\n|y1=%s\n}}"
    Chart2 += "|-\n|}"
    # ---
    if 'makereport' not in sys.argv:
        workondata()
    # ---
    property_other = 0
    tab['len_of_all_properties'] = 0
    p31list = [[y['lenth_of_usage'], x] for x, y in tab['Main_Table'].items() if y['lenth_of_usage'] != 0]
    p31list.sort(reverse=True)
    rows = []
    for Len, P in p31list:
        tab['len_of_all_properties'] += 1
        if tab['len_of_all_properties'] < 27:
            xline += f",{P}"
            yline += f",{Len}"
        sections += make_section(P, tab['Main_Table'][P], Len)
        if len(rows) < 51:
            rows.append('| %d || {{P|%s}} || {{subst:formatnum:%d}} ' % (tab['len_of_all_properties'], P, Len))
        else:
            property_other += int(Len)

    Chart2 = Chart2.replace('|x=%s', f'|x={xline}')
    Chart2 = Chart2.replace('|y1=%s', f'|y1={yline}')
    Chart2 = Chart2.replace("=,", "=")
    # ---
    rows.append(f'| 52 || others || {property_other:,}')
    rows = '\n|-\n'.join(rows)
    table = '\n{| ' + f'class="wikitable sortable"\n|-\n! #\n! property\n! usage\n|-\n{rows}\n' + '|}'
    # ---
    final = time.time()
    delta = int(final - time_start)
    text = ""
    all_itms = tab['All_items']
    no_itms = tab['items_no_claims']
    items_1_claims = tab['items_1_claims']
    all_claims_2020 = tab['all_claims_2020']
    len_of_all_properties = tab['len_of_all_properties']

    text = f"Update: <onlyinclude>latest</onlyinclude>.\n"
    text += f"* Total items:{all_itms:,}\n"
    text += f"* Items without claims:{no_itms:,}\n"
    text += f"* Items with 1 claim only:{items_1_claims:,}\n"
    text += f"* Total number of claims:{all_claims_2020:,} \n"
    text += f"* Number of properties of the report:{len_of_all_properties:,} \n"
    text += f"<!-- bots work done in {delta} secounds --> \n"
    text += "--~~~~~\n"
    text = text + "== Numbers ==\n"
    text = text + f"\n{Chart2}\n{table}\n{sections}"
    text = text.replace("0 (0000)", "0")
    text = text.replace("0 (0)", "0")
    # ---
    title = 'User:Mr. Ibrahem/claims'
    # ---
    # python3 pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != '':
        with open(Dump_Dir + 'dumps/%s.txt' % saveto[1], 'w') as f:
            f.write(text)
    # ---
    if text == "":
        return ''
    if 'test' in sys.argv and 'noprint' not in sys.argv:
        pywikibot.output(text)
    if "nosave" not in sys.argv:
        if 'test' in sys.argv:
            title = 'User:Mr. Ibrahem/claims1'
        from wd_API import himoAPI
        himoAPI.page_putWithAsk('', text, 'Bot - Updating stats', title, False)
        # ---
    if 'test' not in sys.argv:
        with open(Dump_Dir + 'dumps/claims.txt', 'w') as f:
            f.write(text)
    else:
        with open(Dump_Dir + 'dumps/claims1.txt', 'w') as f:
            f.write(text)


if __name__ == '__main__':
    mainar()

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
# ---
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
# ---
Limit = {1: 900000000}
saveto = {1: ''}
sections_done = {1: 0}
sections_false = {1: 0}
dump_done = {1: 0}
# ---
if sys.argv and "test" in sys.argv:
    Limit[1] = 30010
# ---
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    if arg.startswith('-'):
        arg = arg[1:]
    if arg == "limit":
        Limit[1] = int(value)
    if arg == "saveto":
        saveto[1] = value
# ---
# python3 pwb.py dump/dump limit:1000000
tab = {
    'done': 0,
    'len_of_all_properties': 0,
    'items_1_claims': 0,
    'items_no_claims': 0,
    'All_items': 0,
    'all_claims_2020': 0,
    'Main_Table': {},
}
# ---
tab2 = tab.copy()
# ---
jsonname = f'{Dump_Dir}/dumps/claimse.json'
# ---
if 'jsonnew' in sys.argv:
    # dump tab to json
    json.dump(tab, open(jsonname, 'w'))
    pywikibot.output("clear jsonname:%s" % jsonname)
elif 'test' not in sys.argv:
    try:
        # read json
        tab = json.loads(open(jsonname, 'r').read())
        for k, v in tab2.items():
            if not k in tab:
                tab[k] = v
        pywikibot.output("tab['done'] == %d" % tab['done'])
    except:
        pywikibot.output('cant read %s ' % jsonname)


def make_section(P, table, Len):
    """
    Creates a section for a given property in a table.

    Args:
        P (str): The property value.
        table (dict): The table data.
        Len (int): The length of the property.

    Returns:
        str: The section text.

    """
    # ---
    if sections_done[1] == 50:
        return ''
    # ---
    texts = '== {{P|%s}}  ==' % P
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
        pywikibot.output(f'{P} table["props"] == empty.')
        return ''
    # ---
    Chart = '{| class="floatright sortable"\n|-\n|\n'
    Chart += "{{Graph:Chart|width=140|height=140|xAxisTitle=value|yAxisTitle=Number\n|type=pie|showValues1=offset:8,angle:45"
    Chart += "\n|x=%s\n|y1=%s\n|legend=value\n}}\n|-\n|}"
    # ---
    tables = '''{| class="wikitable sortable plainrowheaders"\n|-\n! class="sortable" | #\n! class="sortable" | value\n! class="sortable" | Numbers\n|-\n'''
    # ---
    lists = [[y, xff] for xff, y in table['props'].items()]
    lists.sort(reverse=True)
    # ---
    xline = ''
    yline = ''
    # ---
    num = 0
    other = 0
    # ---
    for ye, x in lists:
        if ye == 0 and sections_false[1] < 100:
            pywikibot.output(f'p({P}), x({x}) ye == 0 or ye == 1 ')
            sections_false[1] += 1
            return ''
        # ---
        num += 1
        if num < 51:
            # ---
            if x.startswith('Q'):
                x = "{{Q|%s}}" % x
            # ---
            row = f"| {num} || {x} || {ye:,}"
            # ---
            xline += f",{x}"
            yline += f",{ye:,}"
            # ---
            tables += f"\n{row}\n|-\n"
        else:
            other += ye
    # ---
    num += 1
    # ---
    tables += f"\n| {num} || others || {other:,}\n|-"
    Chart = Chart % (xline, yline)
    tables += "\n|}\n{{clear}}\n"
    # ---
    texts += Chart.replace("=,", "=")
    texts += tables
    # ---
    sections_done[1] += 1
    return texts


def log_dump():
    """
    Logs the dump of the current process.
    """
    if 'test' not in sys.argv:
        with open(jsonname, 'w') as outfile:
            json.dump(tab, outfile)
        dump_done[1] += 1
        pywikibot.output('log_dump %d done ' % dump_done[1])


def workondata():
    """
    This function performs some operations on data.
    It reads a JSON file, processes the lines, and counts various statistics.
    The function takes no parameters.

    Parameters:
        None

    Returns:
        None
    """
    t1 = time.time()
    diff = 20000
    # ---
    if 'test' in sys.argv:
        diff = 1000
    # ---
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


def save_to_wd(text):
    if "nosave" in sys.argv:
        return
    # ---
    title = 'User:Mr. Ibrahem/claims'
    # ---
    if 'test' in sys.argv:
        title = 'User:Mr. Ibrahem/claims1'
    # ---
    from wd_API import himoAPI
    himoAPI.page_putWithAsk('', text, 'Bot - Updating stats', title, False)
    # ---


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
    # ---
    text = (
        "<onlyinclude>latest</onlyinclude>.\n"
        "* Total items: {All_items:,}\n"
        "* Items without claims: {items_no_claims:,}\n"
        "* Items with 1 claim only: {items_1_claims:,}\n"
        "* Total number of claims: {all_claims_2020:,}\n"
        "* Number of properties of the report: {len_of_all_properties:,}\n"
    ) .format_map(tab)
    # ---
    text += (
        f"<!-- bots work done in {delta} secounds --> \n"
        "--~~~~~\n"
        "== Numbers ==\n"
        f"\n{Chart2}\n{table}\n{sections}"
    )
    text = text.replace("0 (0000)", "0")
    text = text.replace("0 (0)", "0")
    # ---
    # python3 pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != '':
        with open(f'{Dump_Dir}/dumps/%s.txt' % saveto[1], 'w') as f:
            f.write(text)
    # ---
    if text == "":
        return ''
    # ---
    if 'test' in sys.argv and 'noprint' not in sys.argv:
        pywikibot.output(text)
    # ---
    save_to_wd(text)
    # ---
    if 'test' not in sys.argv:
        with open(f'{Dump_Dir}/dumps/claims.txt', 'w') as f:
            f.write(text)
    else:
        with open(f'{Dump_Dir}/dumps/claims1.txt', 'w') as f:
            f.write(text)


if __name__ == '__main__':
    mainar()

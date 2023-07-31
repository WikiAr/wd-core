#!/usr/bin/env python3
"""
python3 core8/pwb.py dump/labels2
python3 core8/pwb.py dump/labels2 test
python3 core8/pwb.py dump/labels2 test nosave
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os
import codecs
import bz2
import json
import time

from dump.bots.labels_old_values import make_old_values  # make_old_values()
Dump_Dir = os.path.dirname(os.path.realpath(__file__))

title = 'User:Mr. Ibrahem/Language statistics for items'

if 'test' in sys.argv:
    title = 'User:Mr. Ibrahem/Language'

main_table_head = """
== Number of labels, descriptions and aliases for items per language ==
{| class="wikitable sortable"
! rowspan="2" |Language code
! colspan="2" |Language 
! colspan="3" data-sort-type="number" |Labels
! colspan="3" data-sort-type="number" |Descriptions
! colspan="2" data-sort-type="number" |Aliases
|-
!English !!Native !!All !! % !!New !!All !! % !!New !!All !!New
|-
"""

new_data_to_dump = {}
All_items = {1: 0}
Limit = {1: 500000000}

# python3 core8/pwb.py dump/labels2 test
if "test" in sys.argv:
    Limit[1] = 3000
for arg in sys.argv:
    arg, sep, value = arg.partition(':')
    if arg.startswith('-'):
        arg = arg[1:]
    if arg == "limit":
        Limit[1] = int(value)
# python3 core8/pwb.py dump/labels2 test limit:1000000

himo_API = {1: False}


def save(text, title_):
    if not himo_API[1]:
        from wd_API import himoAPI
        himo_API[1] = himoAPI
    himo_API[1].page_putWithAsk('', text, 'Bot - Updating stats', title_, False)


def make_cou(num, _all):
    if num == 0:
        return 0
    fef = (num / _all) * 100
    return str(fef)[:4] + "%"


def get_data():
    t1 = time.time()
    Main_Table = {}
    c = 0
    # ---
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    # ---
    if not os.path.isfile(filename):
        print(f'file {filename} <<lightred>> not found')
        return
    # ---
    f = bz2.open(filename, 'r')
    # ---
    try:
        print(f'len of bz2 lines :{len(f)} ')
    except:
        print("can't print the lenth of file lines")
    # ---
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1
        # ---
        if c > Limit[1]:
            break
        # ---
        if line.startswith('{') and line.endswith('}'):
            All_items[1] += 1
            # ---
            if "printline" in sys.argv and c % 1000 == 0 or c == 1:
                print(line)
            # ---
            json1 = json.loads(line)
            tats = ['labels', 'descriptions', 'aliases']
            for x in tats:
                for code in json1.get(x, {}):
                    if not code in Main_Table:
                        Main_Table[code] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
                    Main_Table[code][x] += 1
        # ---
        if c % 1000 == 0:
            print(c, time.time()-t1)
            t1 = time.time()
    return Main_Table


def dump_new_data(): 
    # ---
    if "nosave" in sys.argv or 'test' in sys.argv: return
    # ---
    file = f'{Dump_Dir}/new_data.json'
    try:
        json.dump(new_data_to_dump, codecs.open(file, 'w', 'utf-8'), indent=4)
    except OSError:
        json.dump(new_data_to_dump, codecs.open(f'{Dump_Dir}/new_data1.json', 'w', 'utf-8'), indent=4)


def save_counts_template():
    """
    Generate a template containing language code counts and save it.

    Args:
        new_data_to_dump (dict): A dictionary containing the language code counts.

    Returns:
        None
    """
    if "nosave" in sys.argv or 'test' in sys.argv:
        return
    titlex = 'Template:Tr langcodes counts'
    counts = "{{#switch:{{{c}}}"
    for x, tab in new_data_to_dump.items():
        counts += f"\n|{x}=" + str(tab['labels'])
    counts += "\n}}"
    save(counts, titlex)


def mainar():
    dumpdate = 'latest'
    start = time.time()

    Old = make_old_values()

    Main_Table = get_data()

    langs = list(Main_Table.keys())
    langs.sort()

    rows = []

    test_new_descs = 0

    for code in langs:
        new_labels = 0
        new_descs = 0
        new_aliases = 0

        _labels_ = Main_Table[code]['labels']
        _descriptions_ = Main_Table[code]['descriptions']
        _aliases_ = Main_Table[code]['aliases']

        new_data_to_dump[code] = {'labels': _labels_, 'descriptions': _descriptions_, 'aliases': _aliases_}

        if code in Old:
            new_labels = _labels_ - Old[code]['labels']
            new_descs = _descriptions_ - Old[code]['descriptions']
            new_aliases = _aliases_ - Old[code]['aliases']
        else:
            print(f'code "{code}" not in Old')
        if new_descs != 0:
            test_new_descs = 1

        langs_tag_line = "{{#language:%s|en}}" % code
        langs_tag_line_2 = "{{#language:%s}}" % code

        labels_co = make_cou(_labels_, All_items[1])
        descs_co = make_cou(_descriptions_, All_items[1])
        # ---
        line = f'''| {code} || {langs_tag_line} || {langs_tag_line_2}\n| {_labels_:,} || {labels_co} || +{new_labels:,} || {_descriptions_:,} || {descs_co} || +{new_descs:,} || {_aliases_:,} || +{new_aliases:,}'''
        # ---
        line = line.replace("+-", "-")

        rows.append(line)
    # ---
    dump_new_data()
    # ---
    save_counts_template()
    # ----
    rows = '\n|-\n'.join(rows)
    # ----
    table = main_table_head
    # ----
    table += rows
    # ----
    table += "\n|}\n[[Category:Wikidata statistics|Language statistics]]"
    # ----
    if test_new_descs == 0 and 'test' not in sys.argv:
        print('nothing new.. ')
        return ''
    # ----
    final = time.time()
    delta = int(final - start)
    text = ""
    text = f"Update: <onlyinclude>{dumpdate}</onlyinclude>.\n"
    text += f"* Total items:{All_items[1]:,} \n"
    text += f"<!-- bots work done in {delta} secounds --> \n"
    text += "--~~~~~\n"
    text = text + "\n" + table
    text = text.replace("0 (0000)", "0")
    text = text.replace("0 (0)", "0")

    if text == "":
        return

    print(text)
    if 'test' not in sys.argv:

        if "nosave" not in sys.argv:
            text = text.replace('[[Category:Wikidata statistics|Language statistics]]', '')
            save(text, title)
        with open(f'{Dump_Dir}/dumps/dump.labels2.txt', 'w', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    mainar()

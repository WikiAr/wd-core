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

Dump_Dir = os.path.dirname(os.path.realpath(__file__))

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


def dump_new_data():
    # ---
    if "nosave" in sys.argv or 'test' in sys.argv:
        return
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
    counts = "{{#switch:{{{c}}}"
    for x, tab in new_data_to_dump.items():
        counts += f"\n|{x}=" + str(tab['labels'])
    counts += "\n}}"
    return counts


def mainar(Main_Table):
    start = time.time()

    Old = json.load(codecs.open(f'{Dump_Dir}/old_data.json', 'r', 'utf-8'))

    dumpdate = Main_Table.get('file_date') or 'latest'

    langs_table = Main_Table['langs']

    langs = list(langs_table.keys())
    langs.sort()

    rows = []

    test_new_descs = 0

    for code in langs:
        new_labels = 0
        new_descs = 0
        new_aliases = 0

        _labels_ = langs_table[code]['labels']
        _descriptions_ = langs_table[code]['descriptions']
        _aliases_ = langs_table[code]['aliases']

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

        labels_co = make_cou(_labels_, Main_Table['All_items'])
        descs_co = make_cou(_descriptions_, Main_Table['All_items'])
        # ---
        line = f'''| {code} || {langs_tag_line} || {langs_tag_line_2}\n| {_labels_:,} || {labels_co} || +{new_labels:,} || {_descriptions_:,} || {descs_co} || +{new_descs:,} || {_aliases_:,} || +{new_aliases:,}'''
        # ---
        line = line.replace("+-", "-")

        rows.append(line)
    # ---
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
    text += f"* Total items:{Main_Table['All_items']:,} \n"
    text += f"<!-- bots work done in {delta} secounds --> \n"
    text += "--~~~~~\n"
    text = text + "\n" + table
    text = text.replace("0 (0000)", "0")
    text = text.replace("0 (0)", "0")

    if text == "":
        return

    return text


if __name__ == '__main__':
    tabb = json.load(open(f'{Dump_Dir}/dumps/labels.json'))
    # ---
    text = mainar(tabb)
    # ---
    title = 'User:Mr. Ibrahem/Language statistics for items'

    if 'test' in sys.argv:
        title = 'User:Mr. Ibrahem/Language'
    # ---
    dump_new_data()
    # ---

    tmp_text = save_counts_template()
    # ----
    if 'test' not in sys.argv:
        if "nosave" not in sys.argv:
            text = text.replace('[[Category:Wikidata statistics|Language statistics]]', '')
            # ---
            # save(text, title)
            # ---
            open(f'{Dump_Dir}/labels.txt', 'w', encoding='utf-8').write(text)
            # ---
            tmp_title = 'Template:Tr langcodes counts'
            open(f'{Dump_Dir}/template.txt', 'w', encoding='utf-8').write(tmp_text)
            # save(tmp_text, tmp_title)
    # ----

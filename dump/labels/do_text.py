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
from pathlib import Path
import codecs
import json
import time
# ---
try:
    from dump.labels.labels_old_values import make_old_values# make_old_values()
except:
    from labels_old_values import make_old_values# make_old_values()
# ---
# Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
Himo_Dir = Path(__file__).parent.parent.parent.parent  # Dump_Dir:/data/project/himo
# ---
Dump_Dir = "/data/project/himo/dumps"
# Dump_Dir = f"{Himo_Dir}/dumps"
# ---
print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
# ---
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


def make_cou(num, _all):
    if num == 0 or _all == 0:
        return 0
    fef = (num / _all) * 100
    return str(fef)[:4] + "%"


def mainar(Main_Table):
    start = time.time()

    Old = make_old_values()

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
    # ----
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


def make_temp_text(ttab):
    langs_tab = ttab.get('langs', {})
    # ---
    tmp_text = "{{#switch:{{{c}}}"
    # ---
    for x, tab in langs_tab.items():
        tmp_text += f"\n|{x}=" + str(tab['labels'])
    # ---
    tmp_text += "\n}}"
    # ---
    return tmp_text


def main_labels(tabb):
    # ---
    # from dump.labels.do_text import main_labels# main_labels(tabb)
    # ---
    text = mainar(tabb)
    # ---
    tmp_text = make_temp_text(tabb)
    # ----
    if "nosave" in sys.argv:
        return
    # ----
    text = text.replace('[[Category:Wikidata statistics|Language statistics]]', '')
    # ----
    labels_file = f'{Dump_Dir}/labels.txt'
    template_file = f'{Dump_Dir}/template.txt'
    # ----
    if 'test' in sys.argv:
        labels_file = f'{Dump_Dir}/labels_test.txt'
        template_file = f'{Dump_Dir}/template_test.txt'
    # ----
    with codecs.open(labels_file, 'w', encoding='utf-8') as outfile:
        outfile.write(text)
    # ----
    with codecs.open(template_file, 'w', encoding='utf-8') as outfile:
        outfile.write(tmp_text)
    # ----


if __name__ == '__main__':
    file = f'{Dump_Dir}/labels.json'
    if 'test' in sys.argv:
        file = f'{Dump_Dir}/labels_test.json'
    # ---
    tabb = json.load(codecs.open(file, 'r', encoding='utf-8'))
    # ---
    main_labels(tabb)

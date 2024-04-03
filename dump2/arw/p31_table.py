#!/usr/bin/env python3
"""
python3 wd_core/dump/arw2.py test
python3 core8/pwb.py dump/arw2
python3 core8/pwb.py dump/arw2 test nosave
python3 core8/pwb.py dump/arw2 test nosave p31
python3 core8/pwb.py dump/arw2 test nosave printline
python3 core8/pwb.py dump/arw2 test nosave limit:5000
"""
import sys

CHART_TEMPLATE = """
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

TABLE_TEMPLATE = """
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


def generate_table_row(ns, count, nt_labels, nt_descriptions, nt_aliases):
    # ---
    # Remove unnecessary escape characters
    row = f"\n| {ns.replace(':', '')} || {count:,}"

    # Use format_map for better readability and conciseness
    fafa = "\n| {yes:,} || {no:,} || {yesar:,} || {noar:,}"

    # Apply format_map to each category
    row += fafa.format_map(nt_labels)
    row += fafa.format_map(nt_descriptions)
    row += fafa.format_map(nt_aliases)

    # Use the newline character directly for better readability
    return row + "\n|-"


def ns_stats(prefixes):
    texts = """\n== حسب النطاق  ==\n"""
    xline = ''  # |x=مقالة,تصنيف,قالب,بوابة,ويكيبيديا,وحدة,مساعدة,ملف
    yline = ''  # |y1=718532,564152,46493,4292,1906,850,137,7
    tables = TABLE_TEMPLATE
    # ---
    for ns, nstab in prefixes.items():
        count = nstab["count"]
        # ---
        if count == 0:
            continue
        # ---
        xline += f",{ns.replace(':', '')}"
        yline += f",{count}"
        # ---
        table_row = generate_table_row(ns, count, nstab["labels"], nstab["descriptions"], nstab["aliases"])
        # ---
        tables += table_row
    # ---
    chart = CHART_TEMPLATE % (xline, yline)
    # ---
    texts += chart.replace("=,", "=")
    texts += tables + "\n|}\n"
    # ---
    del xline, yline, tables, chart
    # ---
    return texts


def format_section(section, rows, section_others):
    tr = '\n|-\n'
    section_table = '{| class="wikitable sortable"\n'
    section_table += '! # !! {{P|P31}} !! الاستخدام'
    section_table += tr

    section_table += tr.join(rows)

    section_table += f'{tr}! - !! أخرى !! {section_others}\n'
    section_table += '|}\n'

    return f"=== {section.replace(':', '')} ===\n{section_table}"


def make_text_p31(p31_main_tab, prefixes):
    formatted_sections = []
    # ---
    for section, tab in p31_main_tab.items():
        if section not in prefixes or not tab:
            continue

        sorted_items = sorted(tab.items(), key=lambda x: x[1], reverse=True)

        rows = []
        c = 1
        threshold = 100 if section != 'مقالة' else 10
        section_others = 0

        for qid, count in sorted_items:
            if qid == "no":
                continue
            if count > threshold and len(rows) < 150:
                yf = "{{Q|%s}}" % qid
                rows.append(f'| {c} || {yf} || {count:,} ')
                c += 1
            else:
                section_others += count

        formatted_section = format_section(section, rows, section_others)
        formatted_sections.append(formatted_section)

        del rows, sorted_items, section_others
    # ---
    return '\n'.join(formatted_sections)


def create_p31_table_no(table_no_ar_lab, max_rows=100):
    # ---
    table_no_ar_lab_rows = []
    # ---
    # Sort the items in reverse order based on their values
    sorted_items = sorted(table_no_ar_lab.items(), key=lambda x: x[1], reverse=True)
    # ---
    index = 0
    # ---
    other_count = 0
    # ---
    for qid, count in sorted_items:
        if len(table_no_ar_lab_rows) <= max_rows:
            index += 1
            label_link = "{{Q|%s}}" % qid
            table_no_ar_lab_rows.append(f'| {index} || {label_link} || {count:,} ')
        else:
            other_count += count
    # ---
    # Build the P31 table
    tr = '\n|-\n'
    # ---
    p31_table_no = '\n== استخدام خاصية P31 بدون وصف عربي ==\n'
    # ---
    p31_table_no += '{| class="wikitable sortable"\n! # !! {{P|P31}} !! الاستخدامات'
    # ---
    p31_table_no += tr
    # ---
    p31_table_no += tr.join(table_no_ar_lab_rows)
    # ---
    p31_table_no += f'{tr}! - !! أخرى !! {other_count:,}\n'
    # ---
    p31_table_no += "|}\n"
    # ---
    return p31_table_no

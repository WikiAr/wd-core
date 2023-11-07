#!/usr/bin/env python3
"""
python3 wd_core/dump/arw2.py test
python3 core8/pwb.py dump/arw2
python3 core8/pwb.py dump/arw2 test nosave
python3 core8/pwb.py dump/arw2 test nosave p31
python3 core8/pwb.py dump/arw2 test nosave printline
python3 core8/pwb.py dump/arw2 test nosave limit:5000
"""
#
# (C) Ibrahem Qasim, 2017
import sys
import os
import bz2
import json
import time
# ---
from dump.memory import print_memory
# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r'I:\core\dumps'):
    Dump_Dir = r'I:\core\dumps'
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
if True:
    Offset = {
        1: 0
    }
    Limit = {
        1: 900000000
    }
    # ---
    if "test" in sys.argv:
        Limit[1] = 15000
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(':')
        if arg.startswith('-'):
            arg = arg[1:]
        if arg == "offset" or arg == "off":
            Offset[1] = int(value)
        if arg == "limit":
            Limit[1] = int(value)
# ---
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
# ---
priffixes = {}
# ---
for x in priffixeso:
    priffixes[x] = {
        "count": 0,
        "labels": {
            "yes": 0,
            "no": 0,
            "yesar": 0,
            "noar": 0
        },
        "descriptions": {
            "yes": 0,
            "no": 0,
            "yesar": 0,
            "noar": 0
        },
        "aliases": {
            "yes": 0,
            "no": 0,
            "yesar": 0,
            "noar": 0
        },
    }
# ---
stats_tab = {
    'all_items': 0,
    'all_ar_sitelinks': 0,
    'sitelinks_no_ar': 0,
    'no_p31': 0,
    'no_claims': 0,
    'other_claims_no_p31': 0,
    'Table_no_ar_lab': {},
    'p31_main_tab': {},
    'delta': 0,
}
# ---
Chart_head = """
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
# ---
tables_head = """
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
# ---


def ns_stats():
    texts = """\n== حسب النطاق  ==\n"""
    xline = ''  # |x=مقالة,تصنيف,قالب,بوابة,ويكيبيديا,وحدة,مساعدة,ملف
    yline = ''  # |y1=718532,564152,46493,4292,1906,850,137,7
    tables = tables_head
    # ---
    fafa = "\n| %d || %d || %d || %d"
    # ---
    for ns, nstab in priffixes.items():
        count = nstab["count"]
        # ---
        nstab_labls = nstab["labels"]
        nstab_descs = nstab["descriptions"]
        nstab_alies = nstab["aliases"]
        # ---
        if count != 0:
            ns2 = ns.replace(":", "")
            row = f"| {ns2} || {count:,}"
            # ---
            xline += f",{ns2}"
            yline += f",{count}"
            # ---
            row += fafa % (nstab_labls["yes"], nstab_labls["no"], nstab_labls["yesar"], nstab_labls["noar"])
            row += fafa % (nstab_descs["yes"], nstab_descs["no"], nstab_descs["yesar"], nstab_descs["noar"])
            row += fafa % (nstab_alies["yes"], nstab_alies["no"], nstab_alies["yesar"], nstab_alies["noar"])
            # ---
            tables += f'\n{row}\n|-'
    # ---
    Chart = Chart_head % (xline, yline)
    # ---
    tables += "\n|}\n"
    # ---
    texts += Chart.replace("=,", "=")
    texts += tables
    # ---
    del xline, yline, tables, Chart
    # ---
    return texts


def make_textP31():
    textP31 = ''
    for x, tab in stats_tab['p31_main_tab'].items():
        # ---
        if x not in priffixes or tab == {}:
            continue
        # ---
        p31list = [[y, xfx] for xfx, y in tab.items()]
        # ---
        try:
            p31list.sort(reverse=True)
        except Exception:
            print('p31list.sort(reverse=True)')
            print(p31list)
        # ---
        rows = []
        c = 1
        li = 100
        # ---
        if x != 'مقالة':
            li = 10
        # ---
        section_others = 0
        # ---
        for xx, yy in p31list:
            if yy != "no":
                if xx > li and len(rows) < 150:
                    yf = "{{Q|%s}}" % yy
                    rows.append(f'| {c} || {yf} || {xx} ')
                    c += 1
                else:
                    section_others += xx
        # ---
        if rows == []:
            del p31list
            continue
        # ---
        tatone = '\n{| class="wikitable sortable"\n! # !! {{P|P31}} !! الاستخدام \n|-\n'
        tatone += '\n|-\n'.join(rows)
        # ---
        tatone += f'\n|-\n! - !! أخرى !! {section_others}\n|-\n'
        # ---
        tatone += '\n|}\n'
        # ---
        x2 = x.replace(":", "")
        # ---
        del rows, p31list, section_others
        # ---
        textP31 += f"\n=== {x2} ===\n{tatone}"
    # ---
    return textP31


def save_to_wp(text):
    if text == "":
        print('text is empty')
        return
    # ---
    print(text)
    # ---
    if "nosave" in sys.argv or "test" in sys.argv:
        return
    # ---
    title = 'ويكيبيديا:مشروع_ويكي_بيانات/تقرير_P31'
    # ---
    from API import arAPI
    arAPI.page_put(oldtext="", newtext=text, summary='Bot - Updating stats', title=title)
    # ---
    del text
    del arAPI


def read_data():
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    # ---
    if not os.path.isfile(filename):
        print(f'file {filename} <<lightred>> not found')
        return
    # ---
    t1 = time.time()
    # ---
    c = 0
    # ---
    with bz2.open(filename, "r") as f:
        for line in f:
            line = line.decode("utf-8").strip("\n").strip(",")
            if line.startswith('{') and line.endswith('}'):
                c += 1
                # ---
                if c > Limit[1]:
                    print('c>Limit[1]')
                    break
                # ---
                if c < Offset[1]:
                    if c % 1000 == 0:
                        dii = time.time() - t1
                        print('Offset c:%d, time:%d' % (c, dii))
                    continue
                # ---
                if (c % 1000 == 0 and c < 100000) or c % 100000 == 0:
                    dii = time.time() - t1
                    print(f'c:{c}, time:{dii}')
                    t1 = time.time()
                    print_memory()
                # ---
                if "printline" in sys.argv and (c % 1000 == 0 or c == 1):
                    print(line)
                # ---
                # جميع عناصر ويكي بيانات المفحوصة
                stats_tab['all_items'] += 1
                # ---
                p31_no_ar_lab = []
                json1 = json.loads(line)
                # ---
                # q = json1['id']
                sitelinks = json1.get('sitelinks', {})
                if not sitelinks or sitelinks == {}:
                    del json1
                    continue
                # ---
                arlink = sitelinks.get('arwiki', {}).get('title', '')
                if not arlink:
                    # عناصر بوصلات لغات بدون وصلة عربية
                    stats_tab['sitelinks_no_ar'] += 1
                    del json1, sitelinks
                    continue
                # ---
                # عناصر ويكي بيانات بها وصلة عربية
                stats_tab['all_ar_sitelinks'] += 1
                arlink_type = "مقالة"
                # ---
                for pri, _ in priffixes.items():
                    if arlink.startswith(pri):
                        priffixes[pri]["count"] += 1
                        arlink_type = pri
                        break
                # ---
                if arlink_type not in stats_tab['p31_main_tab']:
                    stats_tab['p31_main_tab'][arlink_type] = {}
                # ---
                if arlink_type == "مقالة":
                    priffixes["مقالة"]["count"] += 1
                # ---
                p31x = 'no'
                # ---
                claims = json1.get('claims', {})
                # ---
                if claims == {}:
                    # صفحات دون أية خواص
                    stats_tab['no_claims'] += 1
                # ---
                P31 = claims.get('P31', {})
                # ---
                if P31 == {}:
                    # صفحة بدون خاصية P31
                    stats_tab['no_p31'] += 1
                    # ---
                    if len(claims) > 0:
                        # خواص أخرى بدون خاصية P31
                        stats_tab['other_claims_no_p31'] += 1
                # ---
                for x in P31:
                    p31x = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
                    if not p31x:
                        continue
                    # ---
                    if p31x not in p31_no_ar_lab:
                        p31_no_ar_lab.append(p31x)
                    # ---
                    if p31x in stats_tab['p31_main_tab'][arlink_type]:
                        stats_tab['p31_main_tab'][arlink_type][p31x] += 1
                    else:
                        stats_tab['p31_main_tab'][arlink_type][p31x] = 1
                # ---
                tat = ['labels', 'descriptions', 'aliases']
                # ---
                for x in tat:
                    if x not in json1:
                        # دون عربي
                        priffixes[arlink_type][x]["no"] += 1
                        continue
                    # ---
                    priffixes[arlink_type][x]["yes"] += 1
                    # ---
                    # تسمية عربي
                    if 'ar' in json1[x]:
                        priffixes[arlink_type][x]["yesar"] += 1
                    else:
                        priffixes[arlink_type][x]["noar"] += 1
                # ---
                ar_desc = json1.get('descriptions', {}).get('ar', False)
                # ---
                if not ar_desc:
                    # استخدام خاصية 31 بدون وصف عربي
                    for x in json1.get('claims', {}).get('P31', []):
                        p31d = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
                        if p31d:
                            if p31d not in stats_tab['Table_no_ar_lab']:
                                stats_tab['Table_no_ar_lab'][p31d] = 0
                            stats_tab['Table_no_ar_lab'][p31d] += 1
    # ---


def make_P31_table_no():
    # ---
    Table_no_ar_lab_rows = []
    # ---
    po_list = [[dyy, xxx] for xxx, dyy in stats_tab['Table_no_ar_lab'].items()]
    po_list.sort(reverse=True)
    # ---
    cd = 0
    # ---
    other = 0
    # ---
    for xf, gh in po_list:
        if len(Table_no_ar_lab_rows) < 100:
            cd += 1
            yf = "{{Q|%s}}" % gh
            Table_no_ar_lab_rows.append(f'| {cd} || {yf} || {xf} ')
        else:
            other += 1
    # ---
    P31_table_no = """\n== استخدام خاصية P31 بدون وصف عربي ==\n"""
    P31_table_no += """{| class="wikitable sortable"\n! # !! {{P|P31}} !! الاستخدامات\n|-\n"""
    P31_table_no += '\n|-\n'.join(Table_no_ar_lab_rows)
    # ---
    P31_table_no += f'\n|-\n! - !! أخرى !! {other}\n|-\n'
    # ---
    P31_table_no += "\n|}\n"
    # ---
    return P31_table_no


def mainar():
    start = time.time()
    # ---
    read_data()
    # ---
    final = time.time()
    # ---
    stats_tab['delta'] = int(final - start)
    # ---
    text = "* تقرير تاريخ: latest تاريخ التعديل ~~~~~.\n"
    text += "* جميع عناصر ويكي بيانات المفحوصة: {all_items:,} \n"
    text += "* عناصر ويكي بيانات بها وصلة عربية: {all_ar_sitelinks:,} \n"
    text += "* عناصر بوصلات لغات بدون وصلة عربية: {sitelinks_no_ar:,} \n"
    text += "<!-- bots work done in {delta} secounds --> \n"
    text += "__TOC__\n"
    # ---
    text = text.format_map(stats_tab)
    # ---
    NS_table = ns_stats()
    # ---
    P31_secs = '== استخدام خاصية P31 ==\n'
    P31_secs += '* {no_claims:,} صفحة دون أية خواص.\n'
    P31_secs += '* {no_p31:,} صفحة بدون خاصية P31.\n'
    P31_secs += '* {other_claims_no_p31:,} صفحة بها خواص أخرى دون خاصية P31.\n'
    # ---
    P31_secs = P31_secs.format_map(stats_tab)
    # ---
    textP31 = make_textP31()
    # ---
    P31_table_no = make_P31_table_no()
    # ---
    text += f"\n{NS_table}"
    text += f"\n{P31_secs}"
    text += f"\n{textP31}"
    text += f"\n{P31_table_no}"
    # ---
    print(text)
    # ---
    if stats_tab['all_items'] == 0:
        print('nothing to update')
        return
    # ---
    save_to_wp(text)
    # ---
    if 'test' not in sys.argv:
        with open(f'{Dump_Dir}/texts/arw2.txt', 'w', encoding='utf-8') as f:
            f.write(text)


if __name__ == '__main__':
    mainar()

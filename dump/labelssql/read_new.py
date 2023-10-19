#!/usr/bin/env python3
"""

python3 core8/pwb.py dump/labels/read_new

https://dumps.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_term_in_lang.sql.gz
https://dumps.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_text_in_lang.sql.gz
عبر كود بايثون:
اريد تحميل الملفين:

https://dumps.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_term_in_lang.sql.gz
https://dumps.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_text_in_lang.sql.gz

ثم إنشاء قاعدة بيانات محلية تحتوي الجدولين
wbt_term_in_lang
wbt_text_in_lang
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os
import json
# ---
try:
    from dump.labels.labels_old_values import make_old_values  # make_old_values()
    from dump.labels.sql_db import new_pymysql_connect  # new_pymysql_connect(query, db='', host='')
except ImportError:
    from labels_old_values import make_old_values  # make_old_values()
    from sql_db import new_pymysql_connect             # new_pymysql_connect(query, db='', host='')
# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r'I:\core\dumps'):
    Dump_Dir = r'I:\core\dumps'
# ---
print(f'Dump_Dir:{Dump_Dir}')

tab_o = {
    'All_items': 0,
    'langs': {},
    'file_date': '',
}


def log_dump(tab):
    # jsonname = f"{Dump_Dir}/labels_new.json"
    jsonname = f"{Dump_Dir}/labels.json"
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/labels_new_test.json"
    with open(jsonname, "w", encoding='utf-8') as outfile:
        json.dump(tab, outfile)
    print("log_dump done")


def sql_wikidata(query):
    # ---
    host = "wikidatawiki.analytics.db.svc.wikimedia.cloud"
    # ---
    dbs_p = 'wikidatawiki_p'
    # ---
    rows = new_pymysql_connect(query, db=dbs_p, host=host)
    # ---
    return rows


def work_one_lang(lang):
    langs = f'"{lang}"'
    # ---
    if isinstance(lang, list):
        langs = ','.join([f'"{x}"' for x in lang])
    # ---
    print(f'langs:{langs}')
    # ---
    query = f"""
        SELECT
            CASE
                WHEN wbtl.wbtl_type_id = 1 THEN 'labels'
                WHEN wbtl.wbtl_type_id = 2 THEN 'descriptions'
                WHEN wbtl.wbtl_type_id = 3 THEN 'aliases'
            END AS wby_name,
            wbxl.wbxl_language as lang,
            COUNT(*) AS count
        FROM
            wbt_term_in_lang wbtl
            INNER JOIN wbt_text_in_lang wbxl ON wbxl.wbxl_id = wbtl.wbtl_text_in_lang_id
        WHERE
            wbxl.wbxl_language in ({langs})
        GROUP BY
            wbxl.wbxl_language,
            wbtl.wbtl_type_id
            ;"""
    # ---
    result = sql_wikidata(query)
    # ---
    for x in result:
        # wby_name, lang, count
        # ---
        lal = x['lang']
        # ---
        if lal not in tab_o['langs']:
            tab_o['langs'][lal] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
        # ---
        count = x['count'] if isinstance(x['count'], int) else int(x['count'])
        # ---
        kk = x['wby_name']
        # ---
        tab_o['langs'][lal][kk] = count
    # ---
    return result


def get_languages():
    qua = '''SELECT distinct wbxl_language FROM wbt_text_in_lang'''
    # ---
    result = sql_wikidata(qua)
    # ---
    return result


def work_for_each_lang(old_tab):
    # ---
    # old_tab = {k: v for k, v in sorted(old_tab.items(), key=lambda item: item[1], reverse=False)}
    # ---
    n = 0
    # ---
    for lang, old_co in old_tab.items():
        # ---
        n += 1
        # ---
        print('_________')
        print(n, len(old_tab), f'lang:{lang}.')
        # ---
        print(f'old_co:{old_co:,}')
        # ---
        tab = work_one_lang(lang)
        # ---
        if 'test1' in sys.argv:
            print(tab)
            break
        # ---


def work_for_multiple_langs(old_tab):
    """
    العمل في اللغات التي قيمتها قليلة
    """
    lenn = 10
    done = 0
    for i in range(0, len(list(old_tab.keys())), lenn):
        keys = list(old_tab.keys())[i:i+lenn]
        # ---
        print(f'i:{i}', f'all:{len(old_tab.keys())}', f'done:{done}')
        # ---
        work_one_lang(keys)
        done += lenn
        # ---
        log_dump(tab_o)
        # ---
        if 'test1' in sys.argv and 'test2' not in sys.argv:
            break


def get_data():
    # ---
    old = make_old_values()
    # ---
    # if y has key 'all' then return all else count other keys values
    def dod(y): return y['all'] if 'all' in y else sum(y.values())
    # ---
    old_tab = {x: dod(y) for x, y in old.items()}
    # ---
    langs = get_languages()
    # ---
    for a in langs:
        if a['wbxl_language'] not in old_tab:
            old_tab[a['wbxl_language']] = 0
    # ---
    print(f'len old_tab:{len(old_tab)}')
    # ---
    for ddde in old_tab:
        tab_o['langs'][ddde] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
    # ---
    # split old_tab to 2 parts
    lent = len(old_tab) // 2
    # Create two new dictionaries with the first and second halves of old_tab
    # ---
    '''
    # من الأكثر إلى الأقل
    # sort old_tab by values
    old_tab = {k: v for k, v in sorted(old_tab.items(), key=lambda item: item[1], reverse=True)}
    # ---
    part1 = dict(list(old_tab.items())[:lent])
    part2 = dict(list(old_tab.items())[lent:])
    '''
    # ---
    # من الاقل للأكثر
    # sort old_tab by values
    old_tab = {k: v for k, v in sorted(old_tab.items(), key=lambda item: item[1], reverse=False)}
    # ---
    part2 = dict(list(old_tab.items())[:lent])
    part1 = dict(list(old_tab.items())[lent:])
    # ---
    # CRITICAL: Exiting due to uncaught exception TypeError: unhashable type: 'slice'
    # العمل على اللغات التي قيمتها قليلة
    work_for_multiple_langs(part2)
    # ---
    if 'test1' not in sys.argv:
        # العمل على اللغات التي قيمتها كبيرة
        work_for_each_lang(part1)
    # ---
    # log results
    log_dump(tab_o)
    # ---
    return tab_o


if __name__ == "__main__":
    get_data()

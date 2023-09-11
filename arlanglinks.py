"""
python3 core8/pwb.py dump/arlanglinks
"""
import sqlite3
import sys
import os
import json
from pathlib import Path
# ---
# ---
# Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
Himo_Dir = Path(__file__).parent.parent.parent.parent # Dump_Dir:/data/project/himo
# ---
Dump_Dir =  "/data/project/himo/dumps"
Dump_Dir = f"{Himo_Dir}/dumps"
# ---
print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
# ---
# ---
from api_sql import wiki_sql
# ---
dump_file = f'{Dump_Dir}/langlinks.json'
# ---
qua = '''select
CONCAT('"Category:', p1.page_title, '"') AS en, CONCAT(':"',ll_title, '",') AS ar
from page AS p1, langlinks
where p1.page_id = ll_from
AND ll_lang = "ar"
AND p1.page_namespace = 14

'''
# ---
table = {}
# ---
all = 1000
# ---
TEST = True if 'test' in sys.argv else False
# ---
if TEST:
    all = 20
# ---
offset = 0
# ---
for i in range(1, all):
    limit = 200000
    # ---
    if i != 1:
        offset += limit
    # ---
    line = f'limit {limit} offset {offset}'
    # ---
    print(line)
    # ---
    qun = qua
    # ---
    qun += line
    # ---
    if TEST:
        continue
    # ---
    result = wiki_sql.sql_new(qun, wiki="en", printqua=False)
    # ---
    if not result or len(result) == 0:
        print('result is empty...')
        break
    # ---
    for x in result:
        en = x['en'].replace('_', ' ')
        ar = x['ar'].replace('_', ' ')
        table[en] = ar
    # ---
    print(f'len of table:{len(table)}')
    # ---
    if TEST:
        break
    # ---
    json.dump(table, open(dump_file, 'w'))
# ---

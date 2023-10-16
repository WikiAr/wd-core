#!/usr/bin/env python3
"""

python3 core8/pwb.py dump/labels/read_n

عبر كود بايثون:
اريد تحميل الملفين:

/mnt/nfs/dumps-clouddumps1002.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_term_in_lang.sql.gz
/mnt/nfs/dumps-clouddumps1002.wikimedia.org/wikidatawiki/latest/wikidatawiki-latest-wbt_text_in_lang.sql.gz

ثم إنشاء قاعدة بيانات محلية تحتوي الجدولين
wbt_term_in_lang
wbt_text_in_lang
"""
#
# (C) Ibrahem Qasim, 2023
#
#
# ---
import sqlite3
import gzip
import os
import tqdm
from pathlib import Path
# ---
try:
    Dir = Path(__file__).parent
except BaseException:
    Dir = '/content'
# ---
# قاموس يحتوي على الروابط وأسماء الملفات
file_links = [
    "wikidatawiki-latest-wbt_term_in_lang.sql.gz",
    "wikidatawiki-latest-wbt_text_in_lang.sql.gz"
]


def open_file2(filename):
    print(f'open file:{open_file}')
    # sql_content = open(filename, 'rb').read().decode('utf-8')
    # ---
    # افتح الملف باستخدام gzip
    # with gzip.open(filename, 'rt', encoding='utf-8') as file:
    # sql_content = file.read()
    # ---
    with gzip.open(filename, 'rt', encoding='utf-8') as file:
        # استخدم tqdm لإضافة شريط التقدم أثناء قراءة الملف
        with tqdm.tqdm(total=os.path.getsize(filename), unit='B', unit_scale=True) as pbar:
            sql_content = ""
            for line in file:
                sql_content += line
                pbar.update(len(line))
    # ---
    return sql_content


def open_file(filename):
    print(f'open file:{filename}')
    sql_content = ""
    # ---
    # sql_content = open(filename, 'rb').read().decode('utf-8')
    # ---
    with gzip.open(filename, 'rb') as term_gzip_file:
        sql_content = term_gzip_file.read().decode('utf-8')
    # ---
    return sql_content


for local_filename in file_links:
    # ---
    filename = f'/mnt/nfs/dumps-clouddumps1002.wikimedia.org/wikidatawiki/latest/{local_filename}'
    # ---
    print(f'filename:{filename}')
    # ---
    if os.path.isfile(filename):
        # ---
        sql_content = open_file(filename)
        # ---
        # Connect to SQLite database
        print('start SQLite:')
        # ---
        db_connection = sqlite3.connect(f'{Dir}/wikidata_database.db')

        # Create tables and insert data
        cursor = db_connection.cursor()
        cursor.execute(sql_content)

        # Commit changes and close the database connection
        db_connection.commit()
        db_connection.close()

print("Database created successfully.")

#!/usr/bin/env python3
"""

python3 core8/pwb.py dump/labels/down

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
# ---
import requests
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
file_links = ["wikidatawiki-latest-wbt_term_in_lang.sql.gz", "wikidatawiki-latest-wbt_text_in_lang.sql.gz"]
# ---
# تنفيذ عملية التحميل وإنشاء قاعدة البيانات باستخدام القاموس
for local_filename in file_links:
    url = f"https://dumps.wikimedia.org/wikidatawiki/latest/{local_filename}"
    # ---
    filename = f'{Dir}/{local_filename}'
    # ---
    print(f'filename:{filename}')
    # ---
    if os.path.isfile(filename):
        sql_content = open(filename, 'rb').read().decode('utf-8')
        print('file already exists')
        # ---
    else:
        print(f'start downloading {local_filename}')
        # ---
        response = requests.get(url, stream=True)
        '''
        # ---
        with open(filename, 'wb') as local_file:
            shutil.copyfileobj(response.raw, local_file)
        '''
        # ---
        # استخدام tqdm لعرض شريط التقدم
        with tqdm.wrapattr(open(filename, "wb"), "write", miniters=1, total=int(response.headers.get('content-length', 0)), desc=filename) as local_file:
            for data in response.iter_content(chunk_size=1024):
                local_file.write(data)
        # ---
        print('done downloading... ')
        # ---
        with gzip.open(filename, 'rb') as gzip_file:
            sql_content = gzip_file.read().decode('utf-8')

    # Connect to SQLite database
    db_connection = sqlite3.connect(f'{Dir}/wikidata_database.db')

    # Create tables and insert data
    cursor = db_connection.cursor()
    cursor.execute(sql_content)

    # Commit changes and close the database connection
    db_connection.commit()
    db_connection.close()

print("Database created successfully.")

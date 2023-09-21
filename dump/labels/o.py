"""
python3 wd_core/dump/labels/o.py

"""
from pathlib import Path
import sqlite3
import os
import gzip
# make memory to 20GB
gzip._OUTPUT_BUFSIZ = 20 * 1024 * 1024
#---
Dir = Path(__file__).parent
print(f'Dir:{Dir}')
# ---
# تجهيز قاعدة بيانات
# ---
# database_file = f'{Dir}/wikidata_database.db'
database_file = f'wikidata_database.db'
# ---
if os.path.isfile(database_file):
    os.remove(database_file)
# ---
if True:
    db_connection = sqlite3.connect(database_file)
    print("start SQLite:")
    # Create tables and insert data
    cursor = db_connection.cursor()
    # ---
    cursor.execute('''
        CREATE TABLE wbt_term_in_lang (
            wbtl_id INTEGER PRIMARY KEY AUTOINCREMENT,
            wbtl_type_id INTEGER NOT NULL,
            wbtl_text_in_lang_id INTEGER NOT NULL,
            FOREIGN KEY (wbtl_type_id) REFERENCES wbt_text_in_lang(wbxl_id),
            UNIQUE(wbtl_text_in_lang_id, wbtl_type_id)
            );
        ''')
    # ---
    cursor.execute('''
        CREATE TABLE wbt_text_in_lang (
            wbxl_id INTEGER PRIMARY KEY AUTOINCREMENT,
            wbxl_language TEXT NOT NULL,
            wbxl_text_id INTEGER NOT NULL,
            UNIQUE(wbxl_text_id, wbxl_language)
        );
        ''')
    # ---
    db_connection.commit()
# ---
# فتح الملفات
# ---
def read_dp(file):
    # Extract the gzipped SQL files
    print(f"read file:{file}")
    n = 0
    with gzip.open(file, 'rb') as hhh:
        term_sql_content = hhh.read()
        for line in term_sql_content.splitlines():
            line = line.decode('utf-8')
            if line.startswith('insert') or line.startswith('INSERT'):
                n += 1
                # add line to db
                cursor.execute(line)
                db_connection.commit()
                if n % 10000 == 0:
                    print(line)
                    print(f"n:{n}")
# ---
# Local filenames for the downloaded files
dump_dir = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/wikidatawiki/latest'
# ---
# dd = f"{dump_dir}/wikidatawiki-latest-user_former_groups.sql.gz"
# read_dp(dd)
# ---
local_filename_term = f"{dump_dir}/wikidatawiki-latest-wbt_term_in_lang.sql.gz"
local_filename_text = f"{dump_dir}/wikidatawiki-latest-wbt_text_in_lang.sql.gz"
# ---
read_dp(local_filename_term)
# ---
read_dp(local_filename_text)
# ---
print("read files.done")
# ---
# ادخال البيانات
# ---
db_connection.close()
print("close db_connection")
# ---
print("Database created successfully.")

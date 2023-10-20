#!/usr/bin/python
"""

بوت قواعد البيانات

from dump.labels.sql_db import new_pymysql_connect# new_pymysql_connect(query, db='', host='')
"""
#
# (C) Ibrahem Qasim, 2023
#
#
from pywikibot import config
import pywikibot
import time
import traceback
import pymysql
import pymysql.cursors
# ---
db_username = config.db_username
db_password = config.db_password
# ---
if config.db_connect_file is None:
    credentials = {
        'user': db_username,
        'password': db_password
    }
else:
    credentials = {
        'read_default_file': config.db_connect_file
    }


def resolve_bytes(rows):
    decoded_rows = []
    # ---
    for row in rows:
        decoded_row = {}
        for key, value in row.items():
            if isinstance(value, bytes):
                try:
                    value = value.decode('utf-8')  # Assuming UTF-8 encoding
                except Exception:
                    value = value
            decoded_row[key] = value
        decoded_rows.append(decoded_row)
    # ---
    return decoded_rows


def connect_pymysql(query, db='', host=''):
    # ---
    print('sql_db.py: start connect_pymysql:')
    # ---
    Typee = pymysql.cursors.DictCursor
    # ---
    args2 = {
        'host': host,
        'db': db,
        'charset': 'utf8mb4',
        'cursorclass': Typee,
        'use_unicode': True,
        'autocommit': True,
    }
    # ---
    params = None
    # ---
    try:
        connection = pymysql.connect(**args2, **credentials)
    except Exception:
        pywikibot.output('Traceback (most recent call last):')
        pywikibot.output(traceback.format_exc())
        pywikibot.output('CRITICAL:')
        return []
    # ---
    with connection as conn, conn.cursor() as cursor:
        # ---
        # skip sql errors
        try:
            cursor.execute(query, params)

        except Exception:
            pywikibot.output('Traceback (most recent call last):')
            pywikibot.output(traceback.format_exc())
            pywikibot.output('CRITICAL:')
            return []
        # ---
        results = []
        # ---
        try:
            results = cursor.fetchall()
        except Exception:
            pywikibot.output('Traceback (most recent call last):')
            pywikibot.output(traceback.format_exc())
            pywikibot.output('CRITICAL:')
            return []
        # ---
        # yield from cursor
        return results


def new_pymysql_connect(query, db='', host=''):
    # ---
    start = time.time()
    final = time.time()
    # ---
    if query == '':
        print("query == ''")
        return []
    # ---
    # print('<<lightyellow>> newsql::')
    # ---
    rows = connect_pymysql(query, db=db, host=host)
    # ---
    rows = resolve_bytes(rows)
    # ---
    final = time.time()
    # ---
    delta = int(final - start)
    # ---
    print(f'sql_db.py sql_new len(rows) = "{len(rows)}", in {delta} seconds')
    # ---
    return rows


# ---

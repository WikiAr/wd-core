#!/usr/bin/python3
""" """
import logging
import os
import time

import pymysql
import pymysql.cursors
from pywikibot import config

logger = logging.getLogger(__name__)

db_username = config.db_username
db_password = config.db_password

if config.db_connect_file is None:
    credentials = {"user": db_username, "password": db_password}
else:
    credentials = {"read_default_file": config.db_connect_file}

can_use_sql_db = {1: True}

dir1 = "/mnt/nfs/labstore-secondary-tools-project/"
dir2 = "/data/project/"

if not os.path.isdir(dir1) and not os.path.isdir(dir2) or os.path.isdir("I:/core/bots"):
    can_use_sql_db[1] = False


def decode_value(value):
    try:
        value = value.decode("utf-8")  # Assuming UTF-8 encoding
    except BaseException:
        try:
            value = str(value)
        except BaseException:
            return ""
    return value


def resolve_bytes(rows):
    decoded_rows = []
    # ---
    for row in rows:
        decoded_row = {}
        for key, value in row.items():
            if isinstance(value, bytes):
                value = decode_value(value)
            decoded_row[key] = value
        decoded_rows.append(decoded_row)
    # ---
    return decoded_rows


def GET_SQL():
    return can_use_sql_db[1]


def make_labsdb_dbs_p(wiki):
    """Generate host and database name for a given wiki.

    This function takes a wiki name as input, processes it to conform to
    specific naming conventions, and generates the corresponding host and
    database name. It handles certain predefined wiki names by mapping them
    to standardized formats. The function ensures that the resulting names
    are suitable for use in a database connection context.

    Args:
        wiki (str): The name of the wiki, which may include a suffix or hyphens.

    Returns:
        tuple: A tuple containing the host string and the database name string.
    """
    # host, dbs_p = make_labsdb_dbs_p('ar')
    # ---
    pre_defined_db_mapping = {
        "gsw": "alswiki_p",
        "sgs": "bat_smgwiki_p",
        "bat-smg": "bat_smgwiki_p",
        "be-tarask": "be_x_oldwiki_p",
        "bho": "bhwiki_p",
        "cbk": "cbk_zamwiki_p",
        "cbk-zam": "cbk_zamwiki_p",
        "vro": "fiu_vrowiki_p",
        "fiu-vro": "fiu_vrowiki_p",
        "map-bms": "map_bmswiki_p",
        "nds-nl": "nds_nlwiki_p",
        "nb": "nowiki_p",
        "rup": "roa_rupwiki_p",
        "roa-rup": "roa_rupwiki_p",
        "roa-tara": "roa_tarawiki_p",
        "lzh": "zh_classicalwiki_p",
        "zh-classical": "zh_classicalwiki_p",
        "nan": "zh_min_nanwiki_p",
        "zh-min-nan": "zh_min_nanwiki_p",
        "yue": "zh_yuewiki_p",
        "zh-yue": "zh_yuewiki_p",
    }
    # ---
    wiki_normalized = wiki.strip().lower().removesuffix("_p").removesuffix("wiki")
    if wiki_normalized in pre_defined_db_mapping:
        dbs_p = f"{pre_defined_db_mapping[wiki_normalized]}"
        sub_host = dbs_p.removesuffix("_p")
        host = f"{sub_host}.analytics.db.svc.wikimedia.cloud"
        return host, dbs_p
    # ---
    wiki = wiki.removesuffix("wiki")
    # ---
    wiki = wiki.replace("-", "_")
    # ---
    databases = {
        "wikidata": "wikidatawiki",
        "be-x-old": "be_x_old",
        "be_tarask": "be_x_old",
        "be-tarask": "be_x_old",
    }
    # ---
    wiki = databases.get(wiki, wiki)
    # ---
    valid_ends = [
        "wiktionary",
    ]
    # ---
    if not (any((wiki.endswith(x)) for x in valid_ends)) and wiki.find("wiki") == -1:
        wiki = f"{wiki}wiki"
    # ---
    dbs = wiki
    # ---
    host = f"{wiki}.analytics.db.svc.wikimedia.cloud"
    dbs_p = f"{dbs}_p"
    # ---
    return host, dbs_p


def sql_connect_pymysql(
    query,
    db="",
    host="",
    update=False,
    default_return=None,
    return_dict=False,
    values=None,
):
    # ---
    if not default_return:
        default_return = []
    # ---
    logger.debug("start sql_connect_pymysql:")
    Typee = pymysql.cursors.DictCursor if return_dict else pymysql.cursors.Cursor
    # ---
    args2 = {
        "host": host,
        "db": db,
        "charset": "utf8mb4",
        "cursorclass": Typee,
        "use_unicode": True,
        "autocommit": True,
    }
    # ---
    params = None
    # ---
    if values:
        params = values
    # ---
    # connect to the database server without error
    # ---
    try:
        connection = pymysql.connect(**args2, **credentials)
    except Exception:
        logger.exception("Exception:", exc_info=True)
        return default_return
    # ---
    with connection as conn, conn.cursor() as cursor:
        # ---
        # skip sql errors
        try:
            cursor.execute(query, params)

        except Exception:
            logger.exception("Exception:", exc_info=True)
            return default_return
        # ---
        results = default_return
        # ---
        try:
            results = cursor.fetchall()

        except Exception:
            logger.exception("Exception:", exc_info=True)
            return default_return
        # ---
        # yield from cursor
        return results


def make_sql_connect(
    query,
    db="",
    host="",
    update=False,
    default_return=None,
    return_dict=False,
    values=None,
):
    # ---
    if not default_return:
        default_return = []
    # ---
    if not query:
        logger.debug("query == ''")
        return default_return
    # ---
    logger.debug("<<lightyellow>> newsql::")
    # ---
    rows = sql_connect_pymysql(
        query,
        db=db,
        host=host,
        update=update,
        default_return=default_return,
        return_dict=return_dict,
        values=values,
    )
    # ---
    if return_dict:
        rows = resolve_bytes(rows)
    # ---
    return rows


def sql_new(
    queries,
    wiki="",
    values=None,
):
    # ---
    logger.debug(f"wiki_sql.py sql_new wiki '{wiki}'")
    # ---
    host, dbs_p = make_labsdb_dbs_p(wiki)
    # ---
    if not GET_SQL():
        logger.info("no GET_SQL()")
        return []
    # ---
    start = time.time()
    final = time.time()
    # ---
    rows = make_sql_connect(queries, db=dbs_p, host=host, return_dict=True, values=values)
    # ---
    final = time.time()
    # ---
    delta = int(final - start)
    # ---
    logger.info(f'wiki_sql.py sql_new len(encats) = "{len(rows)}", in {delta} seconds')
    # ---
    return rows

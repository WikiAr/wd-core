#!/usr/bin/python3
"""
QS Bot - QuickStatements API wrapper

This module provides functions for working with the QuickStatements API.
"""

import logging
import time
from datetime import datetime
from pathlib import Path

import requests

from .utils.useraccount import qs_token, qs_tokenbot

logger = logging.getLogger(__name__)
Dir = Path(__file__).parent.parent
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")


def QS_New_API(data2):
    # ---
    # if "qs" not in sys.argv:
    # return ''
    # ---
    # logger.info(data2)#{'sitelinks': {'enwiki': {'site': 'enwiki', 'title': 'Category:Medical outbreaks in Slovakia'}, 'arwiki': {'site': 'arwiki', 'title': 'تصنيف:تفشي طبي في سلوفاكيا'}}, 'claims': {'P31': [{'mainsnak': {'snaktype': 'value', 'property': 'P31', 'datavalue': {'value': {'entity-type': 'item', 'numeric-id': '4167836', 'id': 'Q4167836'}, 'type': 'wikibase-entityid'}, 'datatype': 'wikibase-item'}, 'type': 'statement', 'rank': 'normal'}]}, 'labels': {'ar': {'language': 'ar', 'value': 'تصنيف:تفشي طبي في سلوفاكيا'}, 'en': {'language': 'en', 'value': 'Category:Medical outbreaks in Slovakia'}}}
    # ---
    # ---
    CREATE = "CREATE||"
    for ss in data2.get("sitelinks", {}):
        dd = data2.get("sitelinks", {})
        tit = dd[ss]["title"]
        wik = dd[ss]["site"]
        wik2 = dd[ss]["site"].replace("wiki", "")
        CREATE += f'LAST|S{wik}|"{tit}"||'
        CREATE += f'LAST|L{wik2}|"{tit}"||'
    # ---
    claims = data2.get("claims", {})
    for Claim in claims:
        for P in claims[
            Claim
        ]:  # {'mainsnak': {'snaktype': 'value', 'property': 'P31', 'datavalue': {'value': {'entity-type': 'item', 'numeric-id': '4167836', 'id': 'Q4167836'}, 'type': 'wikibase-entityid'}, 'datatype': 'wikibase-item'}, 'type': 'statement', 'rank': 'normal'}
            # logger.info(P)
            value = P["mainsnak"]["datavalue"].get("value", {}).get("id", "")
            # value = P["datavalue"].get("value",{}).get("id","")
            if value:
                CREATE += f"LAST|{P['mainsnak']['property']}|{value}||"
    # ---
    CREATE = f"{CREATE}XX"
    CREATE = CREATE.replace("||XX", "")
    # CREATE = CREATE.replace("|","%7C")
    # ---
    menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
    # ---
    r2 = requests.Session().post(
        "https://quickstatements.toolforge.org/api.php",
        data={
            "format": "v1",
            "action": "import",  # create
            # 'type': 'item',
            "compress": 1,
            "submit": 1,
            "batchname": menet,
            "username": "Mr. Ibrahem",
            "token": qs_token,
            "data": CREATE,
        },
    )
    # ---
    if not r2:
        return False
    # ---
    logger.info(f"QS_New_API: {str(r2.text)}")


def QS_line(line, user="Mr. Ibrahem"):
    # ---
    # https://quickstatements.toolforge.org/api.php?format=v1&action=import&compress=1&submit=1&batchname=df&username=Mr.Ibrahembot&token=$2&data=Q24173161|Dar|"جين في متفطرة خراجية"
    # ---
    # if "qs" not in sys.argv:
    # return ''
    # ---
    tokens = {
        "Mr. Ibrahem": qs_token,
        "Mr.Ibrahembot": qs_tokenbot,
    }
    # ---
    session = requests.session()
    session.headers.update({"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"})
    # ---
    r2 = session.post(
        "https://quickstatements.toolforge.org/api.php",
        data={
            "format": "v1",
            "action": "import",  # create
            # 'type': 'item',
            "compress": 1,
            "submit": 1,
            "batchname": menet,
            "username": user,
            "token": tokens.get(user),
            "data": line,
        },
    )
    # ---
    if not r2:
        return False
    # ---
    logger.info(r2.text)
    # ---
    # {"status":"OK","batch_id":35429}
    try:
        with open(f"{str(Dir)}/textfiles/API-log/qsstatus.csv", "a", encoding="utf-8") as logfile:
            lena = len(line.split("||"))
            lli = f"{str(r2.text)}\t{lena}\n"
            logfile.write(lli)
        logfile.close()
    except Exception:
        logger.exception("Exception:", exc_info=True)
    # ---
    # if "try2020" in sys.argv: return csdhg
    # ---
    time.sleep(2)

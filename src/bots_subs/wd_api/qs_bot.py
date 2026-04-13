#!/usr/bin/python3
""" """

import os
import logging
import time
from datetime import datetime
from pathlib import Path

import requests

Dir = Path(__file__).parent.parent
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")

qs_token = os.getenv("QS_TOKEN", "")
qs_tokenbot = os.getenv("QS_TOKEN_BOT", "")

logger = logging.getLogger(__name__)


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
    token = tokens.get(user)
    # ---
    if token and not token.startswith("$2y$10$"):
        token = "$2y$10$" + token
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
            "token": token,
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

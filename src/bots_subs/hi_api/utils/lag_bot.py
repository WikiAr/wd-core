"""
Lag handling functionality

This module provides functions for handling lag in Wikidata API requests.
"""

import logging
import re
import sys
import time

import requests

logger = logging.getLogger(__name__)


session = {1: None}

if "testwikidata" in sys.argv:
    session["url"] = "https://test.wikidata.org/w/api.php"
else:
    session["url"] = "https://www.wikidata.org/w/api.php"

newsleep = {1: 1}

maxlag = 5  # "3"

if "maxlag2" in sys.argv:
    maxlag = 1

FFa_lag = {1: maxlag, 2: maxlag}
Find_Lag = {}
Find_Lag_o = {1: True}
Find_Lag[2] = time.time()
Find_Lag[3] = 0


def find_lag(err) -> None:
    # ---
    lagese = int(err.get("lag", "0"))
    # ---
    if lagese != FFa_lag[1]:
        FFa_lag[1] = lagese
        logger.info(f"<<lightpurple>> max lag: sleep for {FFa_lag[1]} secound.")
    else:
        logger.info(f"<<lightpurple>> lagese == FFa_lag[1] ({FFa_lag[1]})")
    # ---
    logger.info(f"<<lightred>> max lag: sleep for {lagese+1} secound.")
    # ---
    time.sleep(FFa_lag[1] + 1)


def make_sleep_def():
    # ---
    frr = int(time.time() - Find_Lag[2])
    # ---
    params = {
        "action": "query",
        "format": "json",
        "maxlag": -1,
        "titles": "MediaWiki",
    }
    # ---
    if Find_Lag_o[1] or frr > 119:
        # ---
        Find_Lag_o[1] = False
        # ---
        Find_Lag[3] += 1
        Find_Lag[2] = time.time()
        # ---
        r4fttext = ""
        # ---
        if not session[1]:
            session[1] = requests.session()
            headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
            session[1].headers.update(headers)
        # ---
        try:
            r4ft = session[1].post(session["url"], data=params)
            r4fttext = r4ft.text
            # ---
        except Exception as e:
            logger.warning(f"{e} - log Error writing")
        # ---
        lag = re.match(r".*Waiting for [^ ]*: (\d+\.*\d*) seconds.*", r4fttext)
        # ---
        if lag:
            FFa_lag[1] = int(float(lag.group(1)))
            logger.info(f"<<lightpurple>> bot.py {Find_Lag[3]} find lag:{float(lag.group(1))}, frr:{frr}")
    # ---
    fain = 0
    # ---
    if FFa_lag[1] != FFa_lag[2]:
        # ---
        fain = FFa_lag[1]
        # ---
        logger.info(f"<<lightpurple>> bot.py make_sleep_def: {fain=}")
        # ---
        FFa_lag[2] = FFa_lag[1]
        # ---
        if FFa_lag[1] <= 1 or FFa_lag[1] <= 2:
            fain = 0
        # ---
        elif FFa_lag[1] <= 3 or FFa_lag[1] <= 4:
            fain = 1
        # ---
        elif FFa_lag[1] <= 5 or FFa_lag[1] <= 6:
            fain = 2
        # ---
        elif FFa_lag[1] <= 7 or FFa_lag[1] <= 8:
            fain = 3
        # ---
        elif FFa_lag[1] <= 9 or FFa_lag[1] <= 10:
            fain = 4
    # ---
    if newsleep[1] != fain:
        logger.info(f"change newsleep from {newsleep[1]} to {fain}, <<lightpurple>>  max lag:{FFa_lag[1]}.")
        # logger.info( '<<lightpurple>> bot.py make_sleep_def...' )
        newsleep[1] = fain


def do_lag():
    GG = False
    # ---
    numb = 0
    # ---
    make_sleep_def()
    # ---
    if FFa_lag[1] > 5:
        GG = True
    # ---
    # while FFa_lag[1] > 5:
    while GG is True:
        numb += 1
        # ---
        sleeptime = FFa_lag[1] * 2
        # ---
        diff = int(time.time() - Find_Lag[2])
        # ---
        logger.info(f" lag = ({FFa_lag[1]}) > 5, {numb=}, {diff=}, {sleeptime=}")
        # ---
        make_sleep_def()
        # ---
        time.sleep(sleeptime)
        # ---
        if FFa_lag[1] < 5:
            GG = False
        else:
            GG = False


def bad_lag(nowait):
    # ---
    if "testwikidata" in sys.argv:
        return False
    # ---
    # if lag_bot.bad_lag(nowait): return ""
    # ---
    if nowait and FFa_lag[1] > 5:
        return True
    # ---
    return False

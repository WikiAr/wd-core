#!/usr/bin/python3
"""
POST bot - Labels functionality

This module provides functions for working with labels in Wikidata.
"""

import logging
import re
import sys

from ..himo_wd_bots.bot_wd import WD_Functions
from ..utils import lag_bot
from ..utils.out_json import outbot_json

logger = logging.getLogger(__name__)
bot_wd = WD_Functions()

Get_item_descriptions_or_labels = bot_wd.Get_item_descriptions_or_labels
Get_Property_API = bot_wd.Get_Property_API


label_ask = {1: True}
Save_2020_wd = {1: False}


def ask_put(s):
    yes_answer = ["y", "a", "", "Y", "A", "all", "aaa"]
    sa = input(s)
    if sa not in yes_answer:
        print(" bot: wrong answer")
        return False
    if sa == "a" or sa == "A":
        return "a"
    return True


class WD_Labels:
    def __init__(self, wdapi_new, Des_API):
        self.wdapi_new = wdapi_new
        self.session_post = self.wdapi_new.post_to_newapi
        self.Des_API_funcs = Des_API
        # pass

    def Alias_API(self, Qid, Alias, lang, ret, Remove=[], nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        # save the edit
        NN = "|".join(Alias)
        out = f'{Qid} alia:"{lang}"@{NN}.'
        Params = {
            "action": "wbsetaliases",
            "id": Qid,
            "language": lang,
        }
        # ---
        if Remove != []:
            lala = "|".join(Remove)
            Params["remove"] = lala
            out = f'{Qid} alia remove:"{lang}"@{lala}.'
        else:
            Params["add"] = NN
        # ---
        r4 = self.session_post(params=Params)
        # ---
        if not r4:
            return False
        # ---
        text = str(r4)
        if ret:
            return text
        # ---
        d = outbot_json(r4, fi=out, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)

    def Labels_API(
        self, Qid, label, lang, ret, Or_Alii=False, change_des=False, number=0, nowait=False, tage="", remove=False
    ):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        if not Qid:
            logger.info("Labels_API Qid == '' ")
            return False
        # ---
        if label == "" and not remove:
            logger.info("Labels_API label == '' and remove = False ")
            return False
        # ---
        # save the edit
        out = f'{Qid} label:"{lang}"@{label}.'
        if number:
            out = f'{number} {Qid} label:"{lang}"@{label}.'
        r4 = self.session_post(
            params={
                "action": "wbsetlabel",
                "id": Qid,
                "language": lang,
                "value": label,
            },
            tage=tage,
        )
        # ---
        if not r4:
            logger.info("Labels_API r4 == {} ")
            return False
        # ---
        text = str(r4)
        if ("using the same description text" in text) and ("associated with language code" in text):
            item2 = re.search(r"(Q\d+)", str(r4["error"]["info"])).group(1)
            logger.info(f"<<lightred>>API: same label item: {item2}")
            if change_des is True:
                self.find_des_and_replace(Qid, label, lang)
            elif Or_Alii is True:
                self.Alias_API(Qid, [label], lang, ret)
        if ret:
            return text
        # ---
        d = outbot_json(r4, fi=out, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)

    def Add_Labels_if_not_there(self, Qid, label, lang, ASK="", Or_Alii=False, nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        # save the edit
        _out = f'{Qid} label:"{lang}"@{label}.'
        # ---
        jj = self.session_post(
            params={
                "action": "wbgetentities",
                "ids": Qid,
                "props": "labels",
                "languages": f"{lang}|mul",
            }
        )
        # ---
        if not jj:
            return False
        # ---
        labels = jj.get("entities", {}).get(Qid, {}).get("labels", {})
        # ---
        lang_labels = labels.get(lang, {}).get("value", "")
        # ---
        if lang_labels:
            logger.info(f'<<purple>> already there {lang} lab "{lang_labels}" in {Qid}')
            return False
        # ---
        mul_labels = labels.get("mul", {}).get("value", "")
        # ---
        if mul_labels == label:
            logger.info(f'<<purple>> already there "mul" lab "{mul_labels}" in {Qid}')
            return False
        # ---
        if ASK or "ask" in sys.argv and label_ask[1]:
            asa = ask_put(f'<<lightyellow>>: Do you want add "{label}" to "{Qid}"?')
            if asa == "a":
                label_ask[1] = False
            if not asa:
                return False
        # ---
        return self.Labels_API(Qid, label, lang, False, Or_Alii=Or_Alii)

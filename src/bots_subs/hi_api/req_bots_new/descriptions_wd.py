#!/usr/bin/python3
"""
!
"""

import json
import sys

from ..utils import lag_bot
from ..utils.out_json import outbot_json
from bots_subs.qs_bot import QS_line

import logging

logger = logging.getLogger(__name__)

Main_User = {1: ""}
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


class WD_Descriptions:
    def __init__(self, wdapi_new):
        self.wdapi_new = wdapi_new
        self.post_continue_wrap = self.wdapi_new.post_continue
        self.session_post = self.wdapi_new.post_to_newapi
        # pass

    def Des_API(self, Qid, desc, lang, ask="", rea=True, nowait=False):
        """Set the description for a given item in a specified language.

        This function updates the description of an item identified by its Qid
        in the specified language. It checks for lag conditions and prompts the
        user for confirmation if certain conditions are met. If the description
        is empty, it logs an error message. The function also handles potential
        warnings and retries the operation if necessary.

        Args:
            Qid (str): The identifier of the item whose description is to be set.
            desc (str): The new description to be assigned to the item.
            lang (str): The language code in which the description is to be set.
            ask (str?): A flag to prompt the user for confirmation. Defaults to an empty string.
            rea (bool?): A flag indicating whether to retry the operation on failure. Defaults to
                True.
            nowait (bool?): A flag indicating whether to wait for a response. Defaults to False.

        Returns:
            bool: True if the description was successfully set, False otherwise.
        """

        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        if not desc.strip():
            logger.info("<<red>> Des_API desc is empty.")
            return
        # ---
        # save the edit
        out = (
            f'def Des_API: {Qid} description:"{lang}"@{desc}, maxlag:{lag_bot.FFa_lag[1]}, sleep({lag_bot.newsleep[1]})'
        )
        # ---
        if not Save_2020_wd[1] and (ask is True or "ask" in sys.argv):
            # ---
            sa = ask_put(
                f'<<lightyellow>> bot.py Add desc:<<lightyellow>>"{lang}:{desc}"<<default>> for {Qid} Yes or No ? {Main_User[1]} '
            )
            if not sa:
                return False
            # ---
            if sa == "a":
                logger.info("<<lightgreen>> ---------------------------------")
                logger.info("<<lightgreen>> bot.py save all without asking.")
                logger.info("<<lightgreen>> ---------------------------------")
                Save_2020_wd[1] = True
        # ---
        r4 = self.session_post(
            params={
                "action": "wbsetdescription",
                "id": Qid,
                "language": lang,
                "value": desc,
            }
        )
        # ---
        if not r4:
            return False
        # ---
        cf = outbot_json(r4, fi=out, NoWait=nowait)
        # ---
        if cf == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        if cf == "reagain":
            if rea:
                return self.Des_API(Qid, desc, lang, rea=False)
            elif "descqs" in sys.argv:
                qsline = f'{Qid}|D{lang}|"{desc}"'
                QS_line(qsline, user="Mr.Ibrahembot")

    def New_Mult_Des(self, q, data2, summary, ret, nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        data = json.JSONEncoder().encode(data2)
        logger.info("bot.New_Mult_Des: ")
        # ---
        r4 = self.session_post(
            params={
                "action": "wbeditentity",
                "errorformat": "wikitext",
                "id": q,
                "summary": summary,
                "data": data,
            }
        )
        # ---
        if not r4:
            return False
        # ---
        d = outbot_json(r4, fi=summary, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        if ret:
            return str(r4)

    def New_Mult_Des_2(self, q, data2, summary, ret, ask=False, rea=True, nowait=False, tage="", return_result=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        logger.info(f"<<lightblue>> bot.New_Mult_Des_2:q:{q}")
        # ---
        if not Save_2020_wd[1] and (ask is True or "ask" in sys.argv):
            logger.info(f"<<lightyellow>> summary:{summary}")
            # ---
            sa = ask_put(
                f'<<lightyellow>> New_Mult_Des_2 "{q}" <<lightgreen>> (Yes or No ?)<<default>> ,{Main_User[1]} '
            )
            if not sa:
                return False
            # ---
            if sa == "a":
                logger.info("<<lightgreen>> ---------------------------------")
                logger.info("<<lightgreen>> bot.py save all without asking.")
                logger.info("<<lightgreen>> ---------------------------------")
                Save_2020_wd[1] = True
        # ---
        if isinstance(data2, dict):
            data2 = json.JSONEncoder().encode(data2)
        # ---
        paramse = {
            "action": "wbeditentity",
            "id": q,
            "summary": summary,
            "data": str(data2),
        }
        # ---
        r4 = self.session_post(params=paramse, tage=tage)
        # ---
        summary2 = f"New_Mult_Des_2: {summary}"
        # ---
        if not r4:
            return False
        # ---
        cf = outbot_json(r4, fi=summary2, NoWait=nowait)
        # ---
        if cf == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        if cf is True:
            logger.info(
                f"<<lightgreen>> ** true. lag_bot.newsleep[1].sleep({lag_bot.newsleep[1]}), maxlag:({lag_bot.FFa_lag[1]})"
            )
        else:
            # ---
            if cf == "reagain" and rea:
                return self.New_Mult_Des_2(
                    q, data2, summary, ret, rea=False, tage=tage, return_result=(return_result or ret)
                )
        # ---
        if ret or return_result:
            return str(r4)
        # ---
        return False

#!/usr/bin/python3
"""
POST bot - Claims functionality

This module provides functions for working with claims in Wikidata.
"""

import json
import logging
import re

from ..utils import lag_bot
from ..utils.out_json import outbot_json

logger = logging.getLogger(__name__)


class WD_Claims:
    def __init__(self, wdapi_new):
        self.wdapi_new = wdapi_new
        self.session_post = self.wdapi_new.post_to_newapi
        # pass

    def add_quall(self, Claimid, quall_prop, valueline, hashx="", nowait=False):
        """Add a qualifier to a claim.

        This function adds a specified qualifier to a given claim identified by
        the Claimid. It first checks for any lag conditions and then prepares
        the necessary parameters for the action. If the numeric ID in the
        valueline matches the ID extracted from the Claimid, it will not proceed
        with adding the qualifier. The function also handles optional parameters
        such as hash and nowait to modify its behavior.

        Args:
            Claimid (str): The identifier of the claim to which the qualifier is added.
            quall_prop (str): The property name of the qualifier being added.
            valueline (dict): A dictionary containing the value details for the qualifier.
            hash (str?): An optional hash value for the qualifier. Defaults to an empty string.
            nowait (bool?): A flag indicating whether to wait for a response. Defaults to False.

        Returns:
            dict or bool: Returns a dictionary with the result of the operation if
                successful,
                or False if the operation fails.
        """

        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        valueline2 = json.JSONEncoder().encode(valueline)
        logger.info(f'add_quall Claimid: "{Claimid}" ,{valueline2}: ')
        # ---
        id2 = Claimid.split("$")[0].replace("Q", "")
        numeric = valueline.get("numeric-id", False)
        if numeric and numeric == id2:
            logger.info(f"<<lightred>> add_quall {quall_prop}: q:Q{id2} == numeric:Q{numeric}.")
            return ""
        # ---
        papams = {
            "action": "wbsetqualifier",
            "claim": Claimid,
            "snaktype": "value",
            "property": quall_prop,
            "value": valueline2,
        }
        # ---
        if hashx:
            papams["snakhash"] = hashx
        # ---
        nhh = numeric or valueline.get("time", valueline.get("amount", ""))
        out = f'Add qualifier "{quall_prop}":"{nhh}" to Claimid {Claimid}. '
        # ---
        if hashx:
            out = f'change qualifier "{quall_prop}":"{nhh}" in Claimid {Claimid}. '
        # ---
        r6 = self.session_post(params=papams)
        # ---
        if not r6:
            return False
        # ---
        d = outbot_json(r6, fi=out, line=valueline2, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        return d

    def _Set_Quall(self, js, quall_prop, quall_id, nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        out = f'Add qualifier "{quall_prop}":"{quall_id}" to Claimid: '
        # logger.info(out)
        # ---
        Claimid = ""
        # ---
        entitytype = "item"
        qua_id = re.sub(r"Q", "", quall_id)
        if quall_id != re.sub(r"P", "", quall_id):
            entitytype = "property"
            qua_id = re.sub(r"P", "", quall_id)
        value = '{"entity-type":"' + entitytype + '","numeric-id":' + qua_id + "}"
        # ---
        Claimid = js.get("claim", {}).get("id", "")
        # ---
        if not Claimid:
            logger.info('Claimid == ""')
            return False
        # ---
        logger.info(f'Claimid: "{Claimid}"')
        # ---
        r6 = self.session_post(
            params={
                "action": "wbsetqualifier",
                "claim": Claimid,
                "snaktype": "value",
                "property": quall_prop,
                "value": value,
            }
        )
        # ---
        if not r6:
            return False
        # ---
        d = outbot_json(r6, fi=out, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        return Claimid

    def _Set_Quall2(self, js, qualifiers, nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        Claimid = js.get("claim", {}).get("id", "")
        # ---
        if not Claimid:
            logger.info(f'cant find Claimid in: "{str(js)}"')
        # ---
        logger.info(f'<<lightyellow>> _Set_Quall2: Claimid: "{Claimid}"')
        # ---
        for qua in qualifiers:
            quall_prop = qua["property"]
            value = qua["value"]
            ty_pe = qua["type"]
            valueline = {}
            if ty_pe == "time":  # , 'time': '+2003-04-27T00:00:00Z'
                if value.get("time"):
                    valueline = value
                else:
                    valueline = {
                        "after": 0,
                        "calendarmodel": "http://www.wikidata.org/entity/Q1985727",
                        "time": "",
                        "timezone": 0,
                        "before": 0,
                        "precision": 11,
                    }
                    valueline["time"] = value  # '+2003-04-27T00:00:00Z'
            elif ty_pe == "quantity":
                # valueline["property"] = quall_prop
                # valueline["type"] = "quantity"
                # valueline["value"] = {}
                # valueline = value
                # if type(value) != dict:
                valueline = {"amount": "+" + str(value), "unit": "1"}
                # else:
                #  valueline["value"] = value
            else:
                entitytype = "item"
                quat = ""
                if value.get("numeric-id", False):
                    valueline = value
                    quat = value.get("numeric-id", "")
                else:
                    quat = value
                    qua_id = re.sub(r"Q", "", quat)
                    if quat != re.sub(r"P", "", quat):
                        entitytype = "property"
                        qua_id = re.sub(r"P", "", quat)
                    valueline = {"entity-type": entitytype, "numeric-id": qua_id}
            # ---
            self.add_quall(Claimid, quall_prop, valueline)

    def Claim_API2(self, uid, proprty, numeric, qualifiers=[], nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        try:
            numeric = re.sub(r"Q", "", numeric)
        except Exception as e:
            logger.warning(f"{e} - {numeric}")
        out = f"Claim_API2: {uid}: {proprty}:Q{numeric}."
        # logger.info(out)
        # ---
        if uid == "" or proprty == "" or numeric == "":
            logger.info(f"one of (id '{uid}' proprty '{proprty}' numeric '{numeric}') == '' ")
            return False
        # ---
        if not numeric:
            logger.info(f'numeric is "{numeric}"')
            return ""
        # ---
        qq = re.sub(r"Q", "", uid)
        if qq == numeric:
            logger.info(out)
            logger.info(f"<<lightred>> Claim_API2 {proprty}:  id:Q{uid} == numeric:Q{numeric}.")
            return ""
        # ---
        r4 = self.session_post(
            params={
                "action": "wbcreateclaim",
                "entity": uid,
                "snaktype": "value",
                "property": proprty,
                "value": '{"entity-type":"item","numeric-id":' + numeric + "}",
            }
        )
        # ---
        if not r4:
            return False
        # ---
        d = outbot_json(r4, fi=out, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)
        # ---
        if qualifiers != []:
            self._Set_Quall2(r4, qualifiers)

    def Claim_API_time(self, q, proprty, precision=9, year="", strtime="", nowait=False):
        # ---
        if lag_bot.bad_lag(nowait):
            return ""
        # ---
        out = f"{q}: {proprty}:{year}."
        # logger.info(out)
        if precision == 9 and strtime == "":
            strtime = f"+{year}-00-00T00:00:00Z"
        time = {
            "after": 0,
            "before": 0,
            "calendarmodel": "http://www.wikidata.org/entity/Q1985727",
            "precision": precision,
            "time": strtime,
            "timezone": 0,
        }
        # ---
        if not strtime:
            logger.info(f'strtime is "{strtime}"')
        # ---

        r4 = self.session_post(
            params={
                "action": "wbcreateclaim",
                "entity": q,
                "snaktype": "value",
                "property": proprty,
                "value": json.JSONEncoder().encode(time),
            }
        )
        # ---
        if not r4:
            return False
        # ---
        d = outbot_json(r4, fi=out, NoWait=nowait)
        # ---
        if d == "warn":
            logger.exception("Exception:", exc_info=True)

#!/usr/bin/python3
"""
https://www.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q4167836
https://www.wikidata.org/w/api.php?action=wbgetentities&format=json&ids=Q4167836

https://www.wikidata.org/w/rest.php/wikibase/v1/entities/items/Q42
https://doc.wikimedia.org/Wikibase/master/js/rest-api/#/items/getItem

python3 core8/pwb.py wd_api/wd_bots/wb_rest_api

Usage:

from .wd_bots import wb_rest_api
# infos = wb_rest_api.Get_item_infos(qids)
# q_infos = wb_rest_api.Get_one_qid_info(qid, only="sitelinks|labels|descriptions|aliases|statements")
# p373 wb_rest_api.Get_P373(qid)


"""

import logging
import sys

from bots_subs.hi_api import NewHimoAPIBot

logger = logging.getLogger(__name__)

WD_API_Bot = NewHimoAPIBot(mr_or_bot="bot", www="www")

get_rest_result = WD_API_Bot.get_rest_result


wd_cach = {}


def Get_one_qid_info(qid, only=None):
    """Retrieve information for a given Wikidata entity.

    This function fetches detailed information about a specific Wikidata
    entity identified by its QID. It retrieves various properties such as
    labels, descriptions, aliases, sitelinks, and statements. If a specific
    property is requested through the `only` parameter, the function will
    return only that property. The results are cached for efficiency.

    Args:
        qid (str): The QID of the Wikidata entity to retrieve information for.
        only (str?): A specific property to retrieve. Must be one of
            "sitelinks", "labels", "descriptions", "aliases", or "statements".

    Returns:
        dict: A dictionary containing the requested information about the entity,
            including labels, descriptions, aliases, sitelinks, statements, and
            the QID itself.
    """

    # ---
    key_c = tuple([qid, only])
    # ---
    if key_c in wd_cach:
        return wd_cach[key_c]
    # ---
    props = ["sitelinks", "labels", "descriptions", "aliases", "statements"]
    # ---
    main_table = {
        "labels": {},
        "descriptions": {},
        "aliases": {},
        "sitelinks": {},
        "statements": {},
        "qid": qid,
    }
    # ---
    url = f"https://www.wikidata.org/w/rest.php/wikibase/v1/entities/items/{qid}"
    # ---
    if only in props:
        url += "/" + only
    # ---
    if "printurl" in sys.argv:
        logger.info(url)
    # ---
    result = get_rest_result(url)
    # ---
    if only in props:
        result = {only: result}
    # ---
    main_table["labels"] = result.get("labels", {})
    main_table["descriptions"] = result.get("descriptions", {})
    main_table["aliases"] = result.get("aliases", {})
    # ---
    main_table["sitelinks"] = {x: v["title"] for x, v in result.get("sitelinks", {}).items()}
    # ---
    main_table["statements"] = result.get("statements", {})
    # ---
    # if only in props: main_table = main_table[only]
    # ---
    wd_cach[key_c] = main_table
    # ---
    return main_table


def Get_item_infos(qids):
    # ---
    logger.info(f"Get_item_infos {len(qids)=}")
    # ---
    table = {}
    # ---
    for qid in qids:
        # ---
        logger.info(f"Get_item_infos work for one qid: {qid}")
        # ---
        table[qid] = Get_one_qid_info(qid)
    # ---
    return table


def Get_P373(qid):
    # ---
    infos = Get_one_qid_info(qid)
    # ---
    value = infos.get("statements", {}).get("P373", [{}])[0].get("value", {}).get("content", "")
    # ---
    if not value:
        value = infos.get("sitelinks", {}).get("commonswiki", "").replace("Category:", "")
    # ---
    return value

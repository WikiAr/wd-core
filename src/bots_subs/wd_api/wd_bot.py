""" """

import logging

from .submit_bot import submitAPI

logger = logging.getLogger(__name__)


def format_sitelinks(sitelinks):
    return {x["site"]: x["title"] for d, x in sitelinks.items()}


def format_labels_descriptions(labels):
    return {x["language"]: x["value"] for _, x in labels.items()}


def Get_infos_wikidata(params):
    # ---
    table = {"labels": {}, "sitelinks": {}, "q": ""}
    # ---
    json1 = submitAPI(params)
    # ---
    if not json1:
        return table
    # ---
    success = json1.get("success", False)
    if not success or success != 1:
        return table
    # ---
    entities = json1.get("entities", {})
    # ---
    if "-1" in entities:
        return table
    # ---
    props = params["props"].split("|")
    # ---
    for q, qprop in entities.items():
        table["q"] = q
        # ---
        table["labels"] = format_labels_descriptions(qprop.get("labels", {}))
        # ---
        table["sitelinks"] = format_sitelinks(qprop.get("sitelinks", {}))
        # ---
        for x in props:
            if x in qprop and x not in table:
                table[x] = qprop[x]
    # ---
    return table


def Get_item_descriptions_or_labels(q, ty="descriptions or labels"):
    """Retrieve item descriptions or labels from a given entity ID.

    This function queries an API to obtain either descriptions or labels for
    a specified entity ID. It constructs a request based on the provided
    entity ID and the type of information requested. If the type is not
    explicitly set to "descriptions" or "labels", it defaults to
    "descriptions". The function processes the API response and returns a
    dictionary mapping languages to their respective descriptions or labels.
    If the API call is unsuccessful or returns no valid entities, an empty
    dictionary is returned.

    Args:
        q (str): The entity ID for which descriptions or labels are to be retrieved.
        ty (str): The type of information to retrieve, either "descriptions" or "labels".
            Defaults to
            "descriptions or labels".

    Returns:
        dict: A dictionary where keys are language codes and values are the
            corresponding descriptions or labels.
    """

    # ---
    params = {"action": "wbgetentities", "ids": q}
    # ---
    if ty == "descriptions or labels":
        ty = "descriptions"
    # ---
    if ty in ["descriptions", "labels"]:
        params["props"] = ty
    # ---
    json1 = submitAPI(params)
    # ---
    if not json1:
        return {}
    # ---
    success = json1.get("success", False)
    entities = json1.get("entities", {})
    # ---
    if not success or success != 1:
        return {}
    if "-1" in entities:
        return {}
    # ---
    table = {}
    for q in entities:
        qprop = entities[q].get(ty, {})
        # ---
        table = format_labels_descriptions(qprop)
    # ---
    return table


def Get_Item_API_From_Qid(q, sites="", titles="", props=""):
    # "sites": "arwiki",
    # "titles": "ويكيبيديا:مشروع_ويكي_بيانات",
    # url = 'wikidata.org/w/api.php?action=wbgetentities&ids=' + q + '&format=json'
    # json = tools.loads_json( html)
    params = {"action": "wbgetentities"}
    # ---
    sitecode = sites
    # ---
    sitecode = sitecode.removesuffix("wiki")
    sitecode = f"{sitecode}wiki"
    # ---
    if props:
        params["props"] = props
    # ---
    if q:
        params["ids"] = q
    elif sitecode and titles:
        params["titles"] = titles
        params["sites"] = sitecode
        params["normalize"] = 1
    # ---
    table = {
        "sitelinks": {},
        "aliases": {},
        "labels": {},
        "descriptions": {},
        "claims": {},
        "q": "",
    }
    json1 = submitAPI(params)
    # ---
    if not json1:
        return table
    # ---
    success = json1.get("success", False)
    if not success or success != 1:
        return table
    # ---
    entities = json1.get("entities", {})
    # ---
    if "-1" in entities:
        return table
    # ---
    for q_id, ppe in entities.items():
        table["q"] = q_id
        # ---#aliases
        table["labels"] = format_labels_descriptions(ppe.get("labels", {}))
        table["descriptions"] = format_labels_descriptions(ppe.get("descriptions", {}))
        table["sitelinks"] = format_sitelinks(ppe.get("sitelinks", {}))
        table["aliases"] = ppe.get("aliases", {})
        table["claims"] = ppe.get("claims", {})
    # ---
    return table


def Get_Property_API(q="", p="", titles="", sites=""):
    # url = 'https://www.wikidata.org/w/api.php?action=wbgetclaims&entity=' + q + '&property=' + p + '&format=json'
    # json1 = tools.loads_json( html)
    # ---
    params = {
        "action": "wbgetclaims",
        "entity": q,
        "property": p,
        # "": 1,
    }
    # ---
    if q == "" and titles and sites:
        del params["entity"]
        params["sites"] = sites
        params["titles"] = titles
    # ---
    json1 = submitAPI(params) or {}
    # ---
    listo = []
    # ---
    if not json1:
        return listo
    # ---
    claims_p = json1.get("claims", {}).get(p, {})
    # ---
    for claims in claims_p:
        datavalue = claims.get("mainsnak", {}).get("datavalue", {})
        # method = datavalue.get("type", False)
        value = datavalue.get("value", "")
        # ---
        if isinstance(value, dict):
            if value.get("id", False):
                value = value.get("id")
        # ---
        listo.append(value)
    # ---
    return listo

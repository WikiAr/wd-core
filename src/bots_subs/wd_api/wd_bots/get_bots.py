
"""

"""
import logging

from .submit_bot import submitAPI
from .wb_rest_api import Get_one_qid_info

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


def Get_Sitelinks_From_wikidata(site, title, ssite="", ids="", props="", add_props=None, return_main_table=False):
    # ---
    sitewiki = site
    if site.find("wiki") == -1:
        sitewiki = f"{site}wiki"
    # ---
    params = {
        "action": "wbgetentities",
        "props": "sitelinks",
        # "props": "sitelinks|templates",
        "sites": sitewiki,
        "titles": title,
        "normalize": 1,
        # "tlnamespace": "10",
        # "tllimit": "max",
        # "tltemplates": "Template:Category redirect",
    }
    # ---
    if props:
        params["props"] = props
    # ---
    if isinstance(add_props, (list, tuple)):
        for x in add_props:
            if x not in params["props"]:
                params["props"] += f"|{x}"
    # ---
    if ids:
        params["ids"] = ids
        del params["sites"]
        del params["titles"]
    # ---
    table = Get_infos_wikidata(params)
    # ---
    if return_main_table:
        return table
    # ---
    if table:
        table["site"] = sitewiki
    # ---
    ssite2 = ssite
    if not ssite.endswith("wiki"):
        ssite2 += "wiki"
    # ---
    if ssite:
        sitelinks = table.get("sitelinks", {})
        result = sitelinks.get(ssite) or sitelinks.get(ssite2) or ""
        return result
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
    if sitecode.endswith("wiki"):
        sitecode = sitecode[:-4]
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
    table = {"sitelinks": {}, "aliases": {}, "labels": {}, "descriptions": {}, "claims": {}, "q": ""}
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


def Get_Property_API_1(q="", p="", titles="", sites=""):
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
        # Type = datavalue.get("type", False)
        value = datavalue.get("value", "")
        # ---
        if isinstance(value, dict):
            if value.get("id", False):
                value = value.get("id")
        # ---
        listo.append(value)
    # ---
    return listo

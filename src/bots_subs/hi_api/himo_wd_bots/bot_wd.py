"""
Wikidata functions

This module provides Wikidata-specific functionality.
example:

bot_wd = WD_Functions()

Get_item_descriptions_or_labels = bot_wd.Get_item_descriptions_or_labels
Get_Property_API = bot_wd.Get_Property_API

"""

import logging

logger = logging.getLogger(__name__)


class WD_Functions:
    def __init__(self):
        # self.post_continue = post_continue
        # super().__init__()
        pass

    def format_labels_descriptions(self, labels):
        return {x["language"]: x["value"] for _, x in labels.items()}

    def Get_item_descriptions_or_labels(self, post_continue, q, ty="descriptions or labels"):
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
        json1 = post_continue(params)
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
            table = self.format_labels_descriptions(qprop)
        # ---
        return table

    def Get_Property_API(self, post_continue, q="", p="", titles="", sites=""):
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
        json1 = post_continue(params) or {}
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

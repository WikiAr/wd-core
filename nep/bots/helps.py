# -*- coding: utf-8 -*-
"""
from nep.bots.helps import Get_P_API_id, Get_P_API_time, log_new_types
"""
import os
import sys
import json
from pathlib import Path
from nep import read_json

Dir = Path(__file__).parent.parent

def Get_P_API_id(item, P):
    # ---
    # q = 'claims' in item and item['claims'][P]['mainsnak']['datavalue']['value']['id'] or False
    lista = []
    claims = item.get("claims", {}).get(P, {})
    for c in claims:
        if (
            q := c.get("mainsnak", {})
            .get("datavalue", {})
            .get("value", {})
            .get("id", False)
        ):
            lista.append(q)
    # ---
    return lista


def Get_P_API_time(item, P):
    qlist = []
    # ---
    if not item or not isinstance(item, dict):
        return False
    claims = item.get("claims", {}).get(P, [])
    for PP31 in claims:
        vv = PP31.get("mainsnak", {}).get("datavalue", {}).get("value", {})
        if isinstance(vv, dict) and vv.get("time"):
            qlist.append(vv)
    # ---
    if not qlist:
        return False
    if len(qlist) == 1:
        return qlist[0]
    # ---
    sasa = [
        x["time"].split("-")[0].split("+0000000")[1]
        for x in qlist
        if x["time"].startswith("+0000000")
    ]
    Faso = {i: "" for i in sasa}
    return qlist[0] if len(Faso.keys()) == 1 else False

def log_new_types(lists):
    # ---
    if "nolog" in sys.argv:
        return ""
    # ---
    if "log2" in sys.argv:
        jsonfils = Dir / "new_types2.json"
    # ---
    jsonfils = Dir / "tables/new_types.json"
    # ---
    tabe = {}
    # ---
    if os.path.exists(jsonfils):
        with open(jsonfils, "r", encoding="utf-8-sig") as listt:
            try:
                tabe = json.load(listt)
            except Exception:
                print(f"Cant read {jsonfils} ")
                tabe = read_json.read_bad_json(jsonfils)
    # ---
    for lenth, p31 in lists:
        if p31 in tabe:
            tabe[p31] += lenth
        else:
            tabe[p31] = lenth
            print(f"log new types Adding {p31}. ")
    # ---
    with open(jsonfils, "w", encoding="utf-8") as nfile:
        json.dump(tabe, nfile)


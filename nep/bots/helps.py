"""
Import the traceback and pywikibot modules to handle exceptions.

Usage:

from nep.bots.helps import Get_P_API_id, Get_P_API_time, log_new_types, get_female_for_p17, Get_label, get_label_txt, get_lng_description, Get_label_from_item, get_mainsnak
"""
import os
import sys
import json
from pathlib import Path
from nep import read_json
from nep.tables.cash import labels_cach
from nep.tables.nats import nationalities
from wd_api import wd_bot
from newapi.except_err import exception_err

Dir = Path(__file__).parent.parent
lng_canbeused = []


def Get_P_API_id(item, P):
    # ---
    # q = 'claims' in item and item['claims'][P]['mainsnak']['datavalue']['value']['id'] or False
    lista = []
    claims = item.get("claims", {}).get(P, {})
    for c in claims:
        if q := c.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", False):
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
    sasa = [x["time"].split("-")[0].split("+0000000")[1] for x in qlist if x["time"].startswith("+0000000")]
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
        with open(jsonfils, encoding="utf-8-sig") as listt:
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
    try:
        with open(jsonfils, "w", encoding="utf-8") as nfile:
            json.dump(tabe, nfile)
    # Handle the exception and log the traceback.
    except Exception as e:
        exception_err(e)


def Get_label(qid):
    # ---
    lng = "ar"
    label = ""
    # ---
    if lng not in labels_cach:
        labels_cach[lng] = {}
    # ---
    if qid in labels_cach.get(lng, {}):
        return labels_cach[lng][qid]
    # ---
    if not qid:
        return label
    # ---
    WDI = wd_bot.Get_Item_API_From_Qid(qid, sites="", titles="", props="labels")
    # ---
    if lng in WDI.get("labels", {}):
        label = WDI.get("labels", {})[lng]
    # ---
    if label:
        label = label.replace(" (كوكبة)", "")
        label = label.replace(" (نجم)", "")
        label = label.replace(" (مجرة)", "")
        # label = label.replace("كوكبة ",'')
        labels_cach[lng][qid] = label
    # ---
    return label


def get_female_for_p17(contry_lab, tyy):
    # ---
    if not contry_lab.strip():
        return ""
    # ---
    lab = nationalities.get(contry_lab, {}).get(tyy, "")
    # ---
    if contry_lab not in nationalities:
        print(f"contry_lab:{contry_lab} not in nationalities")
    # ---
    return lab


def get_label_txt(lng, wdi, property, array=0, fallback=False):
    if property in wdi.get("claims", {}):
        if len(wdi.get("claims", {}).get(property, "")) > array:
            lnkProperty = wdi.get("claims", {}).get(property)[array].getTarget()
            if propwdi := wd_bot.Get_Item_API_From_Qid(lnkProperty):
                if lng in propwdi.get("labels", {}):
                    return propwdi.get("labels", {}).get(lng)
                elif fallback:
                    if lng != "ar":
                        for fallbacklng in lng_canbeused:
                            if fallbacklng in propwdi.get("labels", {}):
                                return propwdi.get("labels", {}).get(fallbacklng, "")
    return ""


def get_lng_description(language, wikidataitem):
    return wikidataitem.get("descriptions", {}).get(language, "")


def Get_label_from_item(lng, wditem):
    if wditem and isinstance(wditem, dict):
        labels = wditem.get("labels", {})
        # ---
        if lng in labels:
            return labels[lng]
    # ---
    return ""


def get_mainsnak(datavalue):
    return datavalue.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")

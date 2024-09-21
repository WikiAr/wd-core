#!/usr/bin/python3
"""

from nep.new_way import P1433_ids, do_P1433_ids, P1433_en_to_qid

python3 core8/pwb.py neq/nldes3 a2r sparql:Q13433827,Q265158,Q191067,Q19389637,Q953806 all:1000 doar

"""
from nep.bots.its import its_a_generalthing

P1433_ids = {
    "Q13433827": {
        "en": "encyclopedia article",
        "false_labs": ["مقالة موسوعية", "مقالة", ""],
        "props": [
            {"p": "P1433", "lab": "مقالة في"},
            {"p": "P361", "lab": "مقالة في"},
        ],
    },
    "Q265158": {
        "en": "review",
        "false_labs": ["مراجعة", "", ""],
        "props": [
            {"p": "P1433", "lab": "مراجعة منشورة في"},
        ],
    },
    "Q191067": {
        "en": "article",
        "false_labs": ["مقالة موسوعية", "مقالة", ""],
        "props": [
            {"p": "P1433", "lab": "مقالة في"},
            {"p": "P361", "lab": "مقالة في"},
        ],
    },
    "Q19389637": {
        "en": "biographical article",
        "false_labs": ["مقالة سيرة ذاتية", "مقالة", ""],
        "props": [
            {"p": "P50", "lab": "مقالة سيرة ذاتية للمؤلف"},
            {"p": "P1433", "lab": "مقالة سيرة ذاتية منشورة في"},
            {"p": "P921", "lab": "مقالة سيرة ذاتية عن"},
        ],
    },
    "Q953806": {
        "en": "bus stop",
        "false_labs": ["محطة حافلات", "محطة", ""],
        "props": [
            {"p": "P669", "lab": "محطة حافلات في"},
            {"p": "P131", "lab": "محطة حافلات في"},
        ],
    },
}

P1433_en_to_qid = {}

for q, tab in P1433_ids.items():
    if tab.get("en"):
        P1433_en_to_qid[tab["en"].lower()] = q


def do_P1433_ids(wditem, p31, orig_desc):
    # ---
    print(f"do_P1433_ids: {p31=}, {orig_desc=}")
    # ---
    # if p31 == "Q265158" and orig_desc in ["", "مراجعة"]:
    #     my_description = its_a_generalthing(wditem, "مراجعة", "مراجعة منشورة في", "P1433")
    # # ---
    # elif p31 == "Q13433827" and orig_desc in ["", "مقالة موسوعية"]:
    #     my_description = its_a_generalthing(wditem, "مقالة موسوعية", "مقالة في", "P1433")
    # # ---
    # elif p31 == "Q191067" and orig_desc in ["مقالة", ""]:
    #     my_description = its_a_generalthing(wditem, "", "مقالة في ", "P1433")
    # # ---
    if p31 not in P1433_ids:
        print(f"do_P1433_ids: {p31} not in {P1433_ids.keys()}")
        return ""
    # ---
    tab = P1433_ids[p31]
    # ---
    if orig_desc not in tab["false_labs"]:
        print(f"do_P1433_ids: {orig_desc} not in {tab['false_labs']}")
        return ""
    # ---
    for prop in tab["props"]:
        desc = its_a_generalthing(wditem, "", prop["lab"], prop["p"])
        if desc != "" and desc.strip() != prop["lab"]:
            print(f"do_P1433_ids: {desc}")
            return desc
    # ---
    return ""

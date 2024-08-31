#!/usr/bin/python3
"""

from nep.new_way import P1433_ids, do_P1433_ids

"""
from nep.bots.its import its_a_generalthing

P1433_ids = {
    "Q13433827": {
        "false_labs": ["مقالة موسوعية", "مقالة", ""],
        "props": [{"p": "P1433", "lab": "مقالة في"}],
    },
    "Q265158": {
        "false_labs": ["مراجعة", "", ""],
        "props": [{"p": "P1433", "lab": "مراجعة منشورة في"}],
    },
    "Q191067": {
        "false_labs": ["مقالة موسوعية", "مقالة", ""],
        "props": [{"p": "P1433", "lab": "مقالة في"}],
    },
}


def do_P1433_ids(q, p31, orig_desc):
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
        return ""
    # ---
    tab = P1433_ids[p31]
    # ---
    if orig_desc not in tab["false_labs"]:
        return ""
    # ---
    for prop in tab["props"]:
        desc = its_a_generalthing(q, "", prop["lab"], prop["p"])
        if desc != "":
            print(f"do_P1433_ids: {desc}")
            return desc
    # ---
    return ""

#!/usr/bin/python3
"""


"""

import os
import sys
import requests

# ---
filepath = str(os.path.abspath(__file__)).replace("\\", "/")
# ---
paths = [
    "/data/project/himo/bots/core1/",
    "/data/project/himo/bots/wd_core/",
]
# ---
if "/data/project/" not in filepath and "labstore-secondary-tools-project" not in filepath:
    paths = ["I:/core/bots/wd_core/", "I:/core/bots/core1/"]
# ---
for x in paths:
    if os.path.isdir(x):
        sys.path.append(x)
# ---
if "wd" in sys.argv:
    from wikidataintegrator import wdi_helpers
    from wikidataintegrator import wdi_login
else:
    from wikidataintegrator2 import wdi_helpers
    from wikidataintegrator2 import wdi_login
# ---
from API import useraccount

# ---
username = useraccount.hiacc
password = useraccount.hipass
# ---
login = wdi_login.WDLogin(username, password)
# ---
Test = {1: False}
Ask = {1: False}
# ---
if "ask" in sys.argv:
    Ask[1] = True
if "test" in sys.argv:
    Test[1] = True
# ---


def print_test(line, color=""):
    colors = {"red": "\033[91m%s\033[00m", "blue": "\033[94m%s\033[00m"}
    if color and colors.get(color):
        line = colors[color] % line
    # ---
    if Ask[1] or Test[1]:
        print(line)


def get_and_load(url):
    # ---
    print_test(url)
    # ---
    # get url content
    try:
        content = requests.get(url)
        data = content.json()
        return data
    except Exception as e:
        print(f"Error: {e}")
        return {}


def get_article_info(ext_id, id_type):
    # ---
    id_types = {"MED", "PMC", "PMID", "EUROPEPMC", "PAT", "NBK", "HIR", "ETH", "CTX", "CBA", "AGR", "DOI"}
    # ---
    if id_type.upper() not in id_types:
        print(f"id_type must be in {id_types}")
    # ---
    id_type = id_type.lower()
    # ---
    print_test(f" get_article_info for {id_type}")
    # ---
    url = f"https://www.ebi.ac.uk/europepmc/webservices/rest/search?query={ext_id}&resulttype=core&format=json"
    # ---
    do = get_and_load(url)
    # ---
    hit = do.get("resultList", {}).get("result", [])
    # ---
    da_true = {}
    # ---
    for da in hit:
        id_in = da.get(id_type, "")
        # ---
        if id_in == ext_id:
            da_true = da
            break
    # ---
    if not da_true:
        print("No results")
        # ---
        return False
    # ---
    print(f"da_true id: {da_true['id']}")
    # ---
    return "europepmc"


def add(id, typee):
    print_test(f'typee: "{typee}"')
    # ---
    if typee.lower() == "pmc":
        typee = "PMID"
    # ---
    source = get_article_info(id, typee)
    # ---
    typee = typee.lower()
    # ---
    if source:
        ty = ""
        # ---
        if "wd" in sys.argv:
            qid, a, b = wdi_helpers.PublicationHelper(id, id_type=typee, source=source).get_or_create(login)
        else:
            qid, a, b, ty = wdi_helpers.PublicationHelper(id, id_type=typee, source=source).get_or_create(login)
        # ---
        if ty == "old":
            print(f'already in wikidata: <a target="_blank" href="https://www.wikidata.org/wiki/{qid}">{qid}</a>')
            print_test(f"already in wikidata:{qid}", "red")
        elif ty == "new":
            print(f'Create success: <a target="_blank" href="https://www.wikidata.org/wiki/{qid}">{qid}</a>')
            print_test(f"Create success:{qid}", "blue")
        # ---
        print_test(f"qid: {qid}")
        print_test(f"a: {a}")
        print_test(f"b: {b}")
        print_test(f"ty: {ty}")


if __name__ == "__main__":
    br = "</br>"
    # python3 core8/pwb.py pub type:PMC id:4080339
    print_test(f"TestMain:{br}")
    typee = "MED"
    if sys.argv:
        # lenth = len(sys.argv)
        # print_test(str(lenth) + str(sys.argv) )
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            if arg == "type" and value:
                typee = value
            if arg == "id" and value:
                id = value
    # ---
    id = id.replace("https://doi.org/", "")
    # ---
    if id:
        add(id, typee)
    else:
        print("id empty..")

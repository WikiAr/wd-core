#!/usr/bin/env python3
"""
"""
#
# (C) Ibrahem Qasim, 2022
#
#
import sys
import os
import bz2
import json
import time

# ---
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
# ---
Limit = {1: 900000000}
saveto = {1: ""}
sections_done = {1: 0, 'max': 100}
sections_false = {1: 0}
dump_done = {1: 0}
# --
jsonname = f"{Dump_Dir}/dumps/claims.json"
# ---
tab = {
    "done": 0,
    "len_of_all_properties": 0,
    "items_0_claims": 0,
    "items_1_claims": 0,
    "items_no_P31": 0,
    "All_items": 0,
    "all_claims_2020": 0,
    "Main_Table": {},
}
# ---
def workondata():
    """
    This function performs some operations on data.
    It reads a JSON file, processes the lines, and counts various statistics.
    The function takes no parameters.

    Parameters:
        None

    Returns:
        None
    """
    t1 = time.time()
    diff = 20000
    # ---
    if "test" in sys.argv:
        diff = 1000
    # ---
    filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
    if not os.path.isfile(filename):
        print(f"file {filename} <<lightred>> not found")
        return
    fileeee = bz2.open(filename, "r")
    # ---
    done2 = 0
    done = 0
    offset = 0
    if tab["done"] != 0:
        offset = tab["done"]
        print(f"offset == {offset}")
    # ---
    for line in fileeee:
        line = line.decode("utf-8")
        line = line.strip("\n").strip(",")
        # ---
        done += 1
        # ---
        if offset != 0 and done < offset:
            continue
        # ---
        if done % diff == 0 or done == 1000:
            print(f"{done} : {time.time() - t1}.")
            t1 = time.time()
        # ---
        if done2 == 5000000:
            done2 = 1
            log_dump()
        # ---
        if tab["done"] > Limit[1]:
            break
        # ---
        if not line.startswith("{") or not line.endswith("}"):
            continue
        # ---
        done2 += 1
        # ---
        tab["All_items"] += 1
        # ---
        if "printline" in sys.argv and tab["done"] % 1000 == 0:
            print(line)
        # ---
        json1 = json.loads(line)
        claimse = json1.get("claims", {})
        # ---
        if len(claimse) == 0:
            tab["items_0_claims"] += 1
            continue
        # ---
        if len(claimse) == 1:
            tab["items_1_claims"] += 1
        # ---
        if "P31" not in claimse:
            tab["items_no_P31"] += 1
            continue
        # ---
        claims_to_work = claimse.keys()
        # ---
        if props_tos != "all":
            claims_to_work = [props_tos]
        # ---
        for P31 in claims_to_work:
            if P31 not in tab["Main_Table"]:
                tab["Main_Table"][P31] = {
                    "props": {},
                    "lenth_of_usage": 0,
                    "lenth_of_claims_for_property": 0,
                }
            # ---
            tab["Main_Table"][P31]["lenth_of_usage"] += 1
            tab["all_claims_2020"] += len(claimse[P31])
            # ---
            for claim in claimse[P31]:
                tab["Main_Table"][P31]["lenth_of_claims_for_property"] += 1

                datavalue = claim.get("mainsnak", {}).get("datavalue", {})
                ttype = datavalue.get("type")
                # val = datavalue.get("value", {})
                # ---
                if ttype == "wikibase-entityid":
                    idd = datavalue.get("value", {}).get("id")
                    if idd:
                        if not id in tab["Main_Table"][P31]["props"]:
                            tab["Main_Table"][P31]["props"][idd] = 0
                        tab["Main_Table"][P31]["props"][idd] += 1
        # ---
        tab["done"] = done
    # --
    with open(jsonname, "w") as outfile:
            json.dump(tab, outfile)

"""
from dump.read_dump import read_file

python3 wd_core/dump/read_dump.py test

"""
import os
import sys
import bz2
import json
# ---
dump_done = 0
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
# ---
test_limit = {1: 30000}
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


def log_dump():
    global dump_done
    if "test" in sys.argv:
        return
    jsonname = f"{Dump_Dir}/dumps/claims.json"
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/dumps/claims_test.json"
    # jsonname = "dumps/claims_c.json"
    with open(jsonname, "w") as outfile:
        json.dump(tab, outfile)
    dump_done += 1
    print(f"log_dump %d done {dump_done}")


def do_claims(claimse):
    for p in claimse.keys():
        if p not in tab["Main_Table"]:
            tab["Main_Table"][p] = {
                "props": {},
                "lenth_of_usage": 0,
                "lenth_of_claims_for_property": 0,
            }

        tab["Main_Table"][p]["lenth_of_usage"] += 1

        tab["all_claims_2020"] += len(claimse[p])

        for claim in claimse[p]:

            tab["Main_Table"][p]["lenth_of_claims_for_property"] += 1

            datavalue = claim.get("mainsnak", {}).get("datavalue", {})
            ttype = datavalue.get("type")

            if ttype == "wikibase-entityid":
                idd = datavalue.get("value", {}).get("id")
                if idd:
                    if not id in tab["Main_Table"][p]["props"]:
                        tab["Main_Table"][p]["props"][idd] = 0
                    tab["Main_Table"][p]["props"][idd] += 1


def read_file():
    filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"

    if not os.path.isfile(filename):
        print(f"file {filename} <<lightred>> not found")
        return

    print(f"read file: {filename}")

    fileeee = bz2.open(filename, "r")
    c = 0

    for line in fileeee:
        line = line.decode("utf-8")
        line = line.strip("\n").strip(",")
        tab["done"] += 1
        if line.startswith("{") and line.endswith("}"):

            tab["All_items"] += 1

            c += 1
            if c > test_limit[1]:
                print('c>test_limit[1]')
                break

            json1 = json.loads(line)

            claims = json1.get("claims", {})

            if len(claims) == 0:
                tab["items_0_claims"] += 1
            else:
                if len(claims) == 1:
                    tab["items_1_claims"] += 1
                if "P31" not in claims:
                    tab["items_no_P31"] += 1
                do_claims(claims)

    log_dump()

    return tab


if __name__ == "__main__":
    read_file()

"""
from dump.claims.read_dump import read_file
python3 wd_core/dump/claims/read_dump.py test

https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2

"""
import os
import sys
import bz2
import json
import time
from datetime import datetime
from pathlib import Path
# ---
# ---
# split after /dump
core_dir = str(Path(__file__)).replace('\\', '/').split("/dump/", maxsplit=1)[0]
print(f'core_dir:{core_dir}')
sys.path.append(core_dir)
print(f'sys.path.append:core_dir: {core_dir}')
# ---
from dump.memory import print_memory
# ---
Dump_Dir = "/data/project/himo/dumps"
filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
test_limit = {1: 15000}
# ---
tab = {
    "done": 0,
    "file_date": '',
    "len_of_all_properties": 0,
    "items_0_claims": 0,
    "items_1_claims": 0,
    "items_no_P31": 0,
    "All_items": 0,
    "all_claims_2020": 0,
    "Main_Table": {},
    "langs": {},
}


def log_dump(tab):
    jsonname = f"{Dump_Dir}/claims.json"
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/claims_test.json"
    with open(jsonname, "w", encoding='utf-8') as outfile:
        json.dump(tab, outfile)
    print("log_dump done")


def get_file_info(file_path):
    # Get the time of last modification
    last_modified_time = os.path.getmtime(file_path)

    # Convert the timestamp to a readable format
    readable_time = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d')

    return readable_time

def read_file():
    print(f"read file: {filename}")

    if not os.path.isfile(filename):
        print(f"file {filename} not found")
        return {}

    t1 = time.time()
    tab['file_date'] = get_file_info(filename)
    print(f"file date: {tab['file_date']}")

    print(f"file {filename} found, read it:")
    c = 0

    with bz2.open(filename, "r") as f:
        for line in f:
            line = line.decode("utf-8").strip("\n").strip(",")
            tab['done'] += 1
            # ---
            if 'pp' in sys.argv:
                print(line)
            # ---
            if line.startswith("{") and line.endswith("}"):
                tab['All_items'] += 1
                c += 1
                if 'test' in sys.argv:
                    if c % 1000 == 0:
                        print(f'c:{c}')
                        print(f"done:{tab['done']}")

                    if c > test_limit[1]:
                        print('c>test_limit[1]')
                        break

                json1 = json.loads(line)
                # ---
                tats = ['labels', 'descriptions', 'aliases']
                for x in tats:
                    for code in json1.get(x, {}):
                        if not code in tab['langs']:
                            tab['langs'][code] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
                        tab['langs'][code][x] += 1
                # ---
                claims = json1.get("claims", {})
                # ---
                if len(claims) == 0:
                    tab['items_0_claims'] += 1
                    del json1
                    del claims
                    continue
                # ---
                if len(claims) == 1:
                    tab['items_1_claims'] += 1
                # ---
                if "P31" not in claims:
                    tab['items_no_P31'] += 1
                # ---
                for p in claims.keys():
                    Type = claims[p][0].get("mainsnak", {}).get("datatype", '')
                    if Type == "wikibase-entityid":
                        if p not in tab['Main_Table']:
                            tab['Main_Table'][p] = {
                                "props": {},
                                "lenth_of_usage": 0,
                                "lenth_of_claims_for_property": 0,
                            }
                        tab['Main_Table'][p]["lenth_of_usage"] += 1
                        tab['all_claims_2020'] += len(claims[p])
                        for claim in claims[p]:
                            tab['Main_Table'][p]["lenth_of_claims_for_property"] += 1
                            datavalue = claim.get("mainsnak", {}).get("datavalue", {})
                            ttype = datavalue.get("type")
                            if ttype == "wikibase-entityid":
                                idd = datavalue.get("value", {}).get("id")
                                if idd:
                                    if not idd in tab['Main_Table'][p]["props"]:
                                        tab['Main_Table'][p]["props"][idd] = 0
                                    tab['Main_Table'][p]["props"][idd] += 1
                                del idd
                            del datavalue
                            del ttype
                # ---
                del json1
                del claims
            # ---
            if (c % 1000 == 0 and c < 100000) or c % 100000 == 0:
                print(c, time.time()-t1)
                t1 = time.time()
                # print memory usage
                print_memory()
            # ---
    # ---
    print(f"read all lines: {tab['done']}")
    # ---
    for x, xx in tab['Main_Table'].copy().items():
        tab['Main_Table'][x]["len_of_qids"] = len(xx["props"])
    # ---
    log_dump(tab)


if __name__ == "__main__":
    read_file()

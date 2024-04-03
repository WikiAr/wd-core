"""
from dump.claims.read_dump import read_file
python3 core8/pwb.py dump/claims/read_dump test nodump
python3 /data/project/himo/wd_core/dump2/claims/do_tab.py test

https://dumps.wikimedia.org/wikidatawiki/entities/latest-all.json.bz2

"""
import os
import psutil
import ujson as json
import sys
import time
# ---
items_file = "/data/project/himo/wd_core/dump2/jsons/items.json"
jsonname = "/data/project/himo/wd_core/dump2/jsons/claims.json"
# ---
if "test" in sys.argv:
    items_file = "/data/project/himo/wd_core/dump2/jsons/items_test.json"
    jsonname = "/data/project/himo/wd_core/dump2/jsons/claims_test.json"
# ---
tt = {1: time.time()}
# ---
tab = {
    "delta": 0,
    "done": 0,
    "file_date": "",
    "len_all_props": 0,
    "items_0_claims": 0,
    "items_1_claims": 0,
    "items_no_P31": 0,
    "All_items": 0,
    "total_claims": 0,
    "properties": {},
    "langs": {},
}


def print_memory():
    _yellow_ = "\033[93m%s\033[00m"
    usage = psutil.Process(os.getpid()).memory_info().rss
    print(_yellow_ % f"memory usage: psutil {usage / 1024 / 1024} MB")

def log_dump(tab):
    if "nodump" in sys.argv:
        return
    # ---
    with open(jsonname, "w", encoding="utf-8") as outfile:
        json.dump(tab, outfile)
    # ---
    print("log_dump done")

def do_line(json1):
    tab["All_items"] += 1
    tab["done"] += 1

    claims = json1.get("claims", {})

    # Instead of repeatedly checking length, calculate it once
    claims_length = len(claims)

    if claims_length == 0:
        tab["items_0_claims"] += 1
    elif claims_length == 1:
        tab["items_1_claims"] += 1

    if "P31" not in claims:
        tab["items_no_P31"] += 1

    # json1 = {"qid": "Q31", "labels": ["el", "ay"], "descriptions": ["cy", "sk", "mk", "vls"], "sitelinks": ["itwikivoyage", "zhwikivoyage", "ruwikivoyage", "fawikiquote", "dewikivoyage"], "claims": {"P1344": ["Q1088364"], "P31": ["Q3624078", "Q43702", "Q6256", "Q20181813", "Q185441", "Q1250464", "Q113489728"]}}

    for p, p_qids in claims.items():
        
        tab["total_claims"] += len(p_qids)

        p_tab = tab["properties"].get(p)

        if not p_tab:
            p_tab = {
                "qids": {"others": 0},
                "lenth_of_usage": 0,
                "len_prop_claims": 0,
            }

        p_tab["lenth_of_usage"] += 1
        p_tab["len_prop_claims"] += len(p_qids)

        for qid in p_qids:
            if qid:
                p_tab["qids"][qid] = p_tab["qids"].get(qid, 0) + 1
        
        tab["properties"][p] = p_tab

def get_lines():

    with open(items_file, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    for line in lines:
        if line.strip():
            yield json.loads(line.strip())
    
def read_lines():
    print("def read_lines():")
    # ---
    lines = get_lines()
    # ---
    for cc, line in enumerate(lines):
        # ---
        do_line(line)
        # ---
        if cc % 100000 == 0:
            print(cc, time.time() - tt[1])
            tt[1] = time.time()
            # print memory usage
            print_memory()
        # ---
        if cc % 1000000 == 0:
            log_dump(tab)

def read_file():
    # ---
    time_start = time.time()
    # ---
    read_lines()
    # ---
    print(f"read all lines: {tab['done']}")
    # ---
    for x, xx in tab["properties"].items():
        tab["properties"][x]["len_of_qids"] = len(xx["qids"])
    # ---
    tab["len_all_props"] = len(tab["properties"])
    # ---
    end = time.time()
    delta = int(end - time_start)
    print(f"read_file: done in {delta}")
    # ---
    tab["delta"] = f"{delta:,}"
    # ---
    log_dump(tab)

if __name__ == "__main__":
    read_file()

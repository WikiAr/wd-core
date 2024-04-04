"""
python3 /data/project/himo/wd_core/dump2/read_d.py one
python3 /data/project/himo/wd_core/dump2/read_d.py test
tfj run dump2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 /data/project/himo/wd_core/dump2/read_d.py"


"""
import os
import psutil
import json
import sys
import time
from qwikidata.json_dump import WikidataJsonDump
# ---
time_start = time.time()
print(f"time_start:{str(time_start)}")
# ---
filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
# ---
done_lines = "/data/project/himo/wd_core/dump2/done_lines.txt"
items_file = "/data/project/himo/wd_core/dump2/jsons/items.json"

if "test" in sys.argv:
    items_file = "/data/project/himo/wd_core/dump2/jsons/items_test.json"

with open(done_lines, "w", encoding="utf-8") as f:
    f.write("")


def print_memory():
    _yellow_ = "\033[93m%s\033[00m"
    usage = psutil.Process(os.getpid()).memory_info().rss
    print(_yellow_ % f"memory usage: psutil {usage / 1024 / 1024} MB")

def dump_lines(lines):
    if not lines:
        return
    text = "\n".join([json.dumps(line) for line in lines])
    
    with open(items_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def fix_property(pv):
    pv_example = [
        {"mainsnak": {"snaktype": "value", "property": "P1344", "datavalue": {"value": {"entity-type": "item", "numeric-id": 1088364, "id": "Q1088364"}, "type": "wikibase-entityid"}, "datatype": "wikibase-item"}, "type": "statement", "id": "Q31$7C0DCA8A-CFAE-4ED9-B5FD-69BB380CE331", "rank": "normal"},
        {"mainsnak": {"snaktype": "value", "property": "P1344", "datavalue": {"value": {"entity-type": "item", "numeric-id": 1088364, "id": "Q1088364"}, "type": "wikibase-entityid"}, "datatype": "wikibase-item"}, "type": "statement", "id": "Q31$7C0DCA8A-CFAE-4ED9-B5FD-69BB380CE331", "rank": "normal"},
    ]

    qids = []
    # qids is list of mainsnak>datavalue>value>id

    qids = [claim.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id") for claim in pv]

    return qids


def do_line(json1):
    # json1.keys = ['type', 'id', 'labels', 'descriptions', 'aliases', 'claims', 'sitelinks', 'pageid', 'ns', 'title', 'lastrevid', 'modified']

    claims = json1.get("claims", {})

    qid_text = {}

    qid_text["qid"]          = json1["title"]
    qid_text["labels"]       = list(json1.get("labels", {}).keys())
    qid_text["descriptions"] = list(json1.get("descriptions", {}).keys())
    qid_text["aliases"]      = list(json1.get("aliases", {}).keys())
    qid_text["sitelinks"]    = list(json1.get("sitelinks", {}).keys())

    # qid_text["claims_keys"] = claims.keys()

    qid_text["claims"] = {p: fix_property(pv) for p, pv in claims.items() if pv[0].get("mainsnak", {}).get("datatype", "") == "wikibase-item"}

    if "one" in sys.argv:
        print("qid_text:")
        for key, tab in qid_text.items():
            print(f"\033[93m{key}:\033[00m")
            print(tab)
    # ---
    return qid_text

def read_lines(do_test, tst_limit):
    print("def read_lines():")
    # ---
    tt = time.time()
    # ---
    numbs = 500 if do_test else 100000
    # ---
    wjd = WikidataJsonDump(filename)
    # ---
    lines = []
    # ---
    for cc, entity_dict in enumerate(wjd):
        # ---
        if entity_dict["type"] == "item":
            # ---
            line = do_line(entity_dict)
            lines.append(line)
            # ---
            if cc % 10000 == 0:
                dump_lines(lines)
                lines = []
                print(f"dump_lines:{cc}, len lines:{len(lines)}")
            # ---
            if cc % numbs == 0:
                print("cc:", cc, time.time() - tt)
                tt = time.time()
                print_memory()
            # ---
            if do_test and cc > tst_limit:
                print("cc>tst_limit")
                break
            # ---
            if cc % 1000000 == 0:
                with open(done_lines, "a", encoding="utf-8") as f:
                    f.write(f"done: {cc:,}\n")
    # ---
    dump_lines(lines)
    
    
def main():
	time_start = time.time()
	# ---
	do_test = "test" in sys.argv
    # ---
    with open(items_file, "w", encoding="utf-8") as f:
        f.write("")
    # ---
    test_limit = {1: 50000}
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        if arg == "-limit":
            test_limit[1] = int(value)
    # ---
	read_lines(do_test, test_limit[1])
	# ---
    end = time.time()
    delta = int(end - time_start)
    print(f"read_file: done in {delta}")

if __name__ == "__main__":
    main()

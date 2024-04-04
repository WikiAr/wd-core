import os
import psutil
import json
import sys
import time
from pathlip import Path
from qwikidata.json_dump import WikidataJsonDump
def get_most_props():
    # ---
    properties_path = va_dir / "properties.json"
    with open(properties_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    # ---
    return data
    
most_props = get_most_props()

def print_memory():
    _yellow_ = "\033[93m%s\033[00m"
    usage = psutil.Process(os.getpid()).memory_info().rss
    print(_yellow_ % f"memory usage: psutil {usage / 1024 / 1024} MB")

def dump_lines(lines, items_file):
    if not lines:
        return
    text = "\n".join([json.dumps(line) for line in lines])
    with open(items_file, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def fix_property(pv):
    return [claim.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id") for claim in pv]

def do_line(json1):
    claims = json1.get("claims", {})
    qid_text = {
        "qid": json1["title"],
        "labels": list(json1.get("labels", {}).keys()),
        "descriptions": list(json1.get("descriptions", {}).keys()),
        "aliases": list(json1.get("aliases", {}).keys()),
        "sitelinks": list(json1.get("sitelinks", {}).keys()),
        "claims": {p: fix_property(pv) for p, pv in claims.items() if p in most_props}
    }
    return qid_text

def read_lines(do_test, tst_limit, filename, items_file):
    wjd = WikidataJsonDump(filename)
    lines = []
    numbs = 500 if do_test else 100000
    
    for cc, entity_dict in enumerate(wjd):
        if entity_dict["type"] == "item":
            line = do_line(entity_dict)
            lines.append(line)
            
            if cc % 10000 == 0:
                dump_lines(lines, items_file)
                lines = []
                
            if cc % numbs == 0:
                print_memory()
                
            if do_test and cc > tst_limit:
                break
                
            if cc % 1000000 == 0:
                with open(done_lines, "a", encoding="utf-8") as f:
                    f.write(f"done: {cc:,}\n")
                    
    dump_lines(lines, items_file)

def main():
    time_start = time.time()
    do_test = "test" in sys.argv
    items_file = "/data/project/himo/wd_core/dump2/jsons/items.json"
    
    if do_test:
        items_file = "/data/project/himo/wd_core/dump2/jsons/items_test.json"
    
    with open(items_file, "w", encoding="utf-8") as f:
        f.write("")
        
    test_limit = 50000# if "-limit" in sys.argv else None
    
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        if arg == "-limit":
            test_limit = int(value)
            
    read_lines(do_test, test_limit, "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2", items_file)
    
    end = time.time()
    delta = int(end - time_start)
    
    print(f"read_file: done in {delta}")

if __name__ == "__main__":
    main()

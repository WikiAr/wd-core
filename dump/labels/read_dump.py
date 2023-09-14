#!/usr/bin/env python3
"""
python3 core8/pwb.py dump/labels/read_dump
python3 core8/pwb.py dump/labels2 test
python3 core8/pwb.py dump/labels2 test nosave
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os
from pathlib import Path
import bz2
import json
import time
from datetime import datetime
# ---
# Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
Himo_Dir = Path(__file__).parent.parent.parent.parent  # Dump_Dir:/data/project/himo
# ---
Dump_Dir = "/data/project/himo/dumps"
Dump_Dir = f"{Himo_Dir}/dumps"
# ---
print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
# ---
test_limit = {1: 15000}
# ---


def log_dump(tab):
    jsonname = f"{Dump_Dir}/labels.json"
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/labels_test.json"
    # jsonname = "dumps/claims_c.json"
    with open(jsonname, "w") as outfile:
        json.dump(tab, outfile)
    print("log_dump done")


def get_file_info(file_path):
    # Get the time of last modification
    last_modified_time = os.path.getmtime(file_path)

    # Convert the timestamp to a readable format
    readable_time = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d')

    return readable_time


def get_data():
    t1 = time.time()
    Main_Table = {
        'All_items': 0,
        'langs': {},
        'file_date': '',
    }
    c = 0
    # ---
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    # ---
    file_date = get_file_info(filename)
    print(f'file date: {file_date}')
    Main_Table['file_date'] = file_date
    # ---
    if not os.path.isfile(filename):
        print(f'file {filename} <<lightred>> not found')
        return
    # ---
    f = bz2.open(filename, 'r')
    # ---
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1
        # ---
        if 'test' in sys.argv:
            if c % 1000 == 0:
                print(f'c:{c}')

            if c > test_limit[1]:
                print('c>test_limit[1]')
                break

        if line.startswith('{') and line.endswith('}'):
            Main_Table['All_items'] += 1
            # ---
            if "printline" in sys.argv and c % 1000 == 0 or c == 1:
                print(line)
            # ---
            json1 = json.loads(line)
            tats = ['labels', 'descriptions', 'aliases']
            for x in tats:
                for code in json1.get(x, {}):
                    if not code in Main_Table['langs']:
                        Main_Table['langs'][code] = {'labels': 0, 'descriptions': 0, 'aliases': 0}
                    Main_Table['langs'][code][x] += 1
        # ---
        if c % 1000 == 0:
            print(c, time.time()-t1)
            t1 = time.time()

    log_dump(Main_Table)

    return Main_Table


if __name__ == "__main__":
    get_data()

"""
python3 wd_core/dump/labels/read_dump.py
python3 core8/pwb.py dump/labels/read_dump test
python3 core8/pwb.py dump/labels/read_dump test nosave
"""
import sys
import codecs
import os
from pathlib import Path
import bz2
import json
import time
from datetime import datetime
# ---
time_start = time.time()
print(f"time_start:{str(time_start)}")
# ---
# split after /dump
core_dir = str(Path(__file__)).replace('\\', '/').split("/dump/", maxsplit=1)[0]
print(f'core_dir:{core_dir}')
sys.path.append(core_dir)
print(f'sys.path.append:core_dir: {core_dir}')
# ---
from dump.memory import print_memory
# ---
labels_dir = Path(__file__).parent
# ---
filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r'I:\core\dumps'):
    Dump_Dir = r'I:\core\dumps'
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
test_limit = {1: 15000}
# ---
for arg in sys.argv:
    arg, _, value = arg.partition(':')
    if arg == "-limit":
        test_limit[1] = int(value)
# ---
tab = {
    "delta": 0,
    "done": 0,
    "file_date": '',
    "All_items": 0,
    "langs": {},
}


def dump_it(tab):
    jsonname = f"{Dump_Dir}/labels.json"
    # ---
    if 'test' in sys.argv:
        jsonname = f"{Dump_Dir}/labels_test.json"
    # ---
    with open(jsonname, "w", encoding='utf-8') as outfile:
        json.dump(tab, outfile)
    # ---
    print("dump_it done")


def get_file_info(file_path):
    # Get the time of last modification
    last_modified_time = os.path.getmtime(file_path)

    # Convert the timestamp to a readable format
    readable_time = datetime.fromtimestamp(last_modified_time).strftime('%Y-%m-%d')

    return readable_time


def check_file_date(file_date):
    with codecs.open(f"{labels_dir}/file_date.txt", "r", encoding='utf-8') as outfile:
        old_date = outfile.read()
    # ---
    print(f"file_date: {file_date}, old_date: {old_date}")
    # ---
    if old_date == file_date and 'test' not in sys.argv:
        print(f"file_date: {file_date} <<lightred>> unchanged")
        sys.exit(0)                


def read_file():
    # ---
    print(f"read_file: read file: {filename}")

    if not os.path.isfile(filename):
        print(f"file {filename} <<lightred>> not found")
        return {}

    t1 = time.time()
    tab['file_date'] = get_file_info(filename)
    print(f"file date: {tab['file_date']}")

    print(f"file {filename} found, read it:")
    c = 0
    # ---
    check_file_date(tab['file_date'])
    # ---
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
                    if c % 100 == 0:
                        print(f'c:{c}')
                        print(f"done:{tab['done']}")
                        # ---
                        print(c, time.time()-t1)
                        t1 = time.time()

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
                del json1
            # ---
            if (c % 1000 == 0 and c < 100000) or c % 100000 == 0:
                print(c, time.time()-t1)
                t1 = time.time()
                # print memory usage
                print_memory()
                if c % 1000000 == 0:
                    dump_it(tab)
            # ---
    # ---
    print(f"read all lines: {tab['done']}")
    # ---
    end = time.time()
    # ---
    delta = int(end - time_start)
    tab['delta'] = f'{delta:,}'
    # ---
    dump_it(tab)
    # ---
    with codecs.open(f"{labels_dir}/file_date.txt", "w", encoding='utf-8') as outfile:
        outfile.write(tab['file_date'])
    # ---


if __name__ == "__main__":
    read_file()

#!/usr/bin/env python3
"""
python3 core8/pwb.py dump/claims5 jsonnew
python3 core8/pwb.py dump/claims5 makereport
python3 core8/pwb.py dump/claims5 makereport ask
python3 core8/pwb.py dump/claims5 test nosave
"""
#
# (C) Ibrahem Qasim, 2022
#
#
from dump.claims.do_text import make_text
from dump.claims.read_dump import read_file
import sys
import os
from pathlib import Path
import json
import time
# ---
time_start = time.time()
print(f"time_start:{str(time_start)}")
# ---
# ---
# Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
Himo_Dir = Path(__file__).parent.parent.parent.parent # Dump_Dir:/data/project/himo
# ---
Dump_Dir =  "/data/project/himo/dumps"
Dump_Dir = f"{Himo_Dir}/dumps"
# ---
print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
# ---
# ---
Limit = {1: 900000000}
saveto = {1: ""}
dump_done = {1: 0}
# ---
jsonname = ""
# ---
if "test" in sys.argv:
    Limit[1] = 30010
# ---
for arg in sys.argv:
    arg, sep, value = arg.partition(":")
    if arg.startswith("-"):
        arg = arg[1:]
    if arg == "limit":
        Limit[1] = int(value)
    if arg == "saveto":
        saveto[1] = value
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
tab2 = tab.copy()
# ---


def load_tab(ty):
    """
    Loads the tab from a json file.
    """
    # ---
    global tab, tab2, jsonname
    # ---
    ta = "claims" if ty == "all" else ty.lower()
    # ---
    jsonname = f"{Dump_Dir}/{ta}.json"
    # ---
    if "jsonnew" in sys.argv:
        # dump tab to json
        json.dump(tab, open(jsonname, "w"), indent=4)
        print(f"clear jsonname:{jsonname}")
    elif "test" not in sys.argv:
        if 'read' in sys.argv:
            # read json
            print(f'read file: {jsonname}')
            tab = json.loads(open(jsonname).read())
            print("tab['done'] == %d" % tab.get('done', 0))
        else:
            try:
                # read json
                print(f'read file: {jsonname}')
                tab = json.loads(open(jsonname).read())
                print("tab['done'] == %d" % tab.get('done', 0))
            except Exception as e:
                print(f"cant read {jsonname} ")
                print(f"error: {e}")
    # ---
    for k, v in tab2.items():
        if not k in tab:
            tab[k] = v
    # ---
    return tab


def log_dump():
    """
    Logs the dump of the current process.
    """
    global jsonname
    if "test" not in sys.argv:
        with open(jsonname, "w") as outfile:
            json.dump(tab, outfile)
        dump_done[1] += 1
        print("log_dump %d done " % dump_done[1])


def workondata(props_tos="all"):
    global tab
    tab = read_file()
    log_dump()


def save_to_wd(text, ta):
    if "nosave" in sys.argv:
        return
    # ---
    ta = ta.lower()
    # ---
    title = f"User:Mr. Ibrahem/{ta}"
    # ---
    if "test" in sys.argv:
        title = f"User:Mr. Ibrahem/{ta}_test"
    # ---
    from wd_API import himoAPI

    himoAPI.page_putWithAsk("", text, "Bot - Updating stats", title, False)


def mainar(ty="all"):
    global tab
    # ---
    tab = load_tab(ty)
    # ---
    if "makereport" not in sys.argv:
        workondata(props_tos=ty)
    # ---
    text, text_p31 = make_text(tab, ty=ty)
    # ---
    if text_p31 != "":
        with open(f"{Dump_Dir}/p31_new.txt", "w", encoding="utf-8") as f:
            f.write(text_p31)
        # ---
        save_to_wd(text_p31, 'p31')
    # ---
    # python3 core8/pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != "":
        with open(f"{Dump_Dir}/{saveto[1]}.txt", "w", encoding="utf-8") as f:
            f.write(text)
    # ---
    if text == "":
        print("no data")
        return ""
    # ---
    if "test" in sys.argv and "noprint" not in sys.argv:
        print(text)
    # ---
    if tab["All_items"] == 0:
        print("no data")
        return
    # ---
    ta = "claims" if ty == "all" else ty
    # ---
    save_to_wd(text, ta)
    # ---
    to_log = f"{Dump_Dir}/{ta}.txt"
    if "test" in sys.argv:
        to_log = f"{Dump_Dir}/{ta}_test.txt"
    # ---
    with open(to_log, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    # print(make_cou( 70900911 , 84601659 ))
    mainar(ty="all")

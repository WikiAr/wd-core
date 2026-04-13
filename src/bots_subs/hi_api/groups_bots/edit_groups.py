#!/usr/bin/python3
"""

# from .groups_bots.edit_groups import build_editgroups_summary

"""
import json
import os
import random
import sys
from datetime import datetime, timedelta
from pathlib import Path

Dir = Path(__file__).parent

# get the code from json file
file = Dir / "editgroups.json"

main_keys = {
    "newitems",
    "setsitelink",
    "catelabels",
    "wbremovereferences",
    "wbsetreference",
    "others",
}


def read_it():
    data = {}
    # ---
    print("editgroups read_it:")
    # ---
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    except BaseException:
        print(f"{file} error")
    # ---
    return data


def dump_it(data):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, sort_keys=True, ensure_ascii=False)

    except BaseException:
        print(f"{file} error")


def make_new():
    # ---
    print("editgroups make_new data:")
    # ---
    data = {}
    # ---
    for k in main_keys:
        new_str = f"{random.randrange(0, 2 ** 48):x}"
        data[k] = new_str
    # ---
    dump_it(data)
    # ---
    return data


def load_from_file():
    # ---
    # get file change date
    file_date = os.path.getmtime(file)
    file_date = datetime.fromtimestamp(file_date).strftime("%Y-%b-%d")
    # ---
    todaydate = datetime.now().strftime("%Y-%b-%d")
    # date_after_7 = (datetime.now() + timedelta(days=8)).strftime("%Y-%b-%d")
    # ---
    # if the diff date > 1 week then return {}
    diff = (datetime.strptime(todaydate, "%Y-%b-%d") - datetime.strptime(file_date, "%Y-%b-%d")).days
    # ---
    print(f"{file} diff:{diff}")
    # ---
    if diff > 7:
        return {}
    # ---
    return read_it()


if not file.exists():
    tage_table_for_bot = make_new()
else:
    tage_table_for_bot = load_from_file()
    if not tage_table_for_bot:
        tage_table_for_bot = make_new()


fafo_rand = tage_table_for_bot.get("others") or f"{random.randrange(0, 2 ** 48):x}"
fafo = f"([[:toollabs:editgroups/b/CB/{fafo_rand}|details]])"


def build_editgroups_summary(usernamex, data, editgroups, tage):
    excluded_actions = [
        "wbsearchentities",
        "edit",
    ]

    if editgroups:
        return f"([[:toollabs:editgroups/b/CB/{editgroups}|details]])"
    else:
        if usernamex.find("bot") != -1:
            if data["action"] not in excluded_actions and not data["action"].startswith("wbget"):
                if tage and tage in tage_table_for_bot:
                    return f"([[:toollabs:editgroups/b/CB/{tage_table_for_bot[tage]}|details]])"

        elif "editgroups" in sys.argv:
            return fafo

    return ""

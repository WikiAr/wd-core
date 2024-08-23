#!/usr/bin/python3
"""


"""
#
# (C) Ibrahem Qasim, 2023
#
#

import json as JJson
import re

import traceback

# ---
from newapi import printe

# ---
from newapi.except_err import exception_err
try:
    import pywikibot
except ImportError:
    pywikibot = False


def printo(s):
    if pywikibot:
        pywikibot.output(s)
    else:
        printe.output(s)


def read_bad_list(file):
    try:
        List = []
        with open(file) as listt:
            done_list7 = JJson.load(listt)
        # ---
        for type in done_list7:
            printe.output(f'find {len(done_list7[type])} cats in done_list7. "{type}" , file:"{file}"')
            for catee in done_list7[type]:
                catee = catee.strip()
                catee = re.sub(r'"', "", catee)
                if catee not in List:
                    List.append(catee)
        print(f'Good JJson "{file}"')
        return List
    except Exception as e:
        exception_err(e)
        # ---
        List = []
        with open(file) as listt:
            list2 = listt.read()
        # ---
        listo = list2.split("[")[1].split("]")[0]
        listo = listo.split(",")
        for catee in listo:
            catee = catee.strip()
            catee = re.sub(r'"', "", catee)
            if catee not in List:
                List.append(catee)
        print(f'Bad JJson "{file}"')
        return List
    # ---
    return False


def read_bad_json(file):
    try:
        with open(file) as listt:
            done_list7 = JJson.load(listt)
        # ---
        print(f'Good JJson "{file}"')
        return done_list7
    except Exception as e:
        exception_err(e)
        lala = {}
        with open(file, "r", encoding="utf-8-sig") as listt2:
            lala = listt2.read()
        # ---
        fa = str(lala)
        fa = fa.split("{")[1].split("}")[0]
        fa = f"{{fa}}"
        wd_file = JJson.loads(fa)
        print(f'Bad JJson "{file}"')
        return wd_file
    # ---
    return {}


def main(file, Type):
    try:
        if Type == "dict":
            return read_bad_json(file)
        elif Type == "list":
            return read_bad_list(file)
        else:
            print(f"* unknow type :{Type}")
    except Exception as e:
        exception_err(e, text=f'* Cant work file:"{file}" , Type:"{Type}"')
    return False


# ---
if __name__ == "__main__":
    main("{}", "dict")
# ---

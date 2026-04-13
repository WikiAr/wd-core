#!/usr/bin/python3
""" """


import json
import logging
import re

logger = logging.getLogger(__name__)


def printo(s):
    logger.info(s)


def read_bad_list(file):
    try:
        list_data = []
        with open(file) as listt:
            done_list7 = json.load(listt)
        # ---
        for type in done_list7:
            logger.info(f'find {len(done_list7[type])} cats in done_list7. "{type}" , file:"{file}"')
            for catee in done_list7[type]:
                catee = catee.strip()
                catee = re.sub(r'"', "", catee)
                if catee not in list_data:
                    list_data.append(catee)
        print(f'Good json "{file}"')
        return list_data
    except Exception:
        logger.exception("Exception:", exc_info=True)
        # ---
        list_data = []
        with open(file) as listt:
            list2 = listt.read()
        # ---
        listo = list2.split("[")[1].split("]")[0]
        listo = listo.split(",")
        for catee in listo:
            catee = catee.strip()
            catee = re.sub(r'"', "", catee)
            if catee not in list_data:
                list_data.append(catee)
        print(f'Bad json "{file}"')
        return list_data


def read_bad_json(file):
    try:
        with open(file) as listt:
            done_list7 = json.load(listt)
        # ---
        print(f'Good json "{file}"')
        return done_list7
    except Exception:
        logger.exception("Exception:", exc_info=True)
        lala = {}
        with open(file, "r", encoding="utf-8-sig") as listt2:
            lala = listt2.read()
        # ---
        fa = str(lala)
        fa = fa.split("{")[1].split("}")[0]
        fa = f"{{fa}}"
        wd_file = json.loads(fa)
        print(f'Bad json "{file}"')
        return wd_file
    # ---
    return {}


def main(file, o_type):
    try:
        if o_type == "dict":
            return read_bad_json(file)
        elif o_type == "list":
            return read_bad_list(file)
        else:
            print(f"* unknow type :{o_type}")
    except Exception:
        logger.exception("Exception:", exc_info=True)
    return False


if __name__ == "__main__":
    main("{}", "dict")

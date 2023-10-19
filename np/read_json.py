#!/usr/bin/python

"""


"""
#
# (C) Ibrahem Qasim, 2023
#
#

import json as JJson
import re
import codecs
import traceback
# ---
from API import printe
# ---
try:
    import pywikibot
except BaseException:
    pywikibot = False
# ---

# ---
# ---


def printo(s):
    if pywikibot:
        pywikibot.output(s)
    else:
        printe.output(s)
# ---


def read_bad_list(file):
    try:
        List = []
        with open(file) as listt:
            done_list7 = JJson.load(listt)
            listt.close()
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
    except Exception:
        pywikibot.output('<<lightred>> Traceback (most recent call last):')
        pywikibot.output(traceback.format_exc())
        pywikibot.output('CRITICAL:')
        # ---
        List = []
        with open(file) as listt:
            list2 = listt.read()
            listt.close()
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
# ---


def read_bad_json(file):
    try:
        with open(file) as listt:
            done_list7 = JJson.load(listt)
            listt.close()
        # ---
        print(f'Good JJson "{file}"')
        return done_list7
        '''for type in done_list7:
            printe.output( 'find %d cats in done_list7. "%s"' % (len(done_list7[type])  , type) )
            for catee in done_list7[type]:
                catee = catee.strip()
                catee = re.sub(r'"', "" , catee)
                if not catt in List:
                    List.append(catee)'''
    except Exception:
        pywikibot.output('<<lightred>> Traceback (most recent call last):')
        pywikibot.output(traceback.format_exc())
        pywikibot.output('CRITICAL:')
        lala = {}
        with codecs.open(file, "r", encoding="utf-8-sig") as listt2:
            lala = listt2.read()
            listt2.close()
        # ---
        fa = str(lala)
        fa = fa.split("{")[1].split("}")[0]
        fa = "{" + fa + "}"
        wd_file = JJson.loads(fa)
        print(f'Bad JJson "{file}"')
        return wd_file
    # ---
    return {}
# ---


def main(file, Type):
    try:
        if Type == "dict":
            return read_bad_json(file)
        elif Type == "list":
            return read_bad_list(file)
        else:
            print(f"* unknow type :{Type}")
    except Exception:
        pywikibot.output('<<lightred>> Traceback (most recent call last):')
        pywikibot.output(f'* Cant work file:"{file}" , Type:"{Type}"')
        pywikibot.output(traceback.format_exc())
        pywikibot.output('CRITICAL:')
    return False


# ---
if __name__ == "__main__":
    main("{}", "dict")
# ---

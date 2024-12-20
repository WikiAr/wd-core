#!/usr/bin/python3
"""

from nep.wr_people import work_people

"""

import re

from wd_api import wd_desc

from newapi import printe
from people.new3 import translations_o

from nep.tables.lists import en_des_to_ar
from nep.tables.si_tables import genders
from people.people_get_topic import get_topic


def add_only_ar(q, ara):
    # ---
    tab = {"ar": {"language": "ar", "value": ara}}
    wd_desc.work_api_desc(tab, q, fixlang=[])
    # ---
    return


def get_claim_id(item, prop):
    return item.get("claims", {}).get(prop, [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")


def work_people2(item, topic, num=0, years=""):
    # ---
    q = item["q"]
    # ---
    p21 = get_claim_id(item, "P21")
    # ---
    translations = translations_o[2]
    # ---
    taber = translations.get(topic, {})
    # ---
    if not taber:
        printe.output(f" no table descraptions for topic:{topic}")
    # ---
    printe.output(" work_people:")
    # ---
    if not taber:
        return ""
    # ---
    # printe.output(taber)
    # ---
    descriptions = item.get("descriptions", {})
    # ---
    NewDesc = {}
    # ---
    p21_c = genders.get(p21)
    # ---
    if not p21_c:
        print(f" work_people2 p21_c == {p21_c} ")
        return
    # ---
    for lang, lang_tab in taber.items():
        # ---
        if lang_tab.get(p21_c) and lang not in descriptions.keys():
            NewDesc[lang] = {"language": lang, "value": lang_tab.get(p21_c)}
            # ---
            if years and lang in ["en", "ar", "en-ca", "en-gb"]:
                NewDesc[lang]["value"] += years
    # ---
    if not NewDesc:
        print(" work_people nothing to add. ")
        return
    # ---
    printe.output(f"<<lightyellow>> **{num}: work_people:{q}  ({topic})")
    # ---
    wd_desc.work_api_desc(NewDesc, q, fixlang=[])


def work_people(item, topic, num, ardes):
    q = item["q"]
    # ---
    topic = topic.lower().strip() or get_topic(item).lower()
    # ---
    if not topic:
        return ""
    # ---
    years = ""
    # ---
    if topic.find("(") != -1:
        if hhh := re.match(r"^(.*?) (\([\d\–-]+\))", topic):
            topic = hhh.group(1)
            years = f" {hhh.group(2)}"
            print(f"topic:{topic},years:{years}")
    # ---
    if en_des_to_ar.get(topic, "") != "":
        ara = en_des_to_ar[topic]
        # ---
        if years:
            ara += f" {years}"
        # ---
        return add_only_ar(q, ara)
    # ---
    if topic.startswith("researcher (orcid ") and (ardes.strip() == "" or ardes.startswith("باحث (orcid ")):
        arr = topic.replace("researcher (orcid ", "باحث (معرف أورسيد ")
        # ---
        return add_only_ar(q, arr)

    # ---
    work_people2(item, topic, num, years)

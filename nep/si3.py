#!/usr/bin/python3
"""

"""

#
# (C) Ibrahem Qasim, 2022
#
import sys
import re
from pathlib import Path
from datetime import datetime

# ---
from wd_api import himoAPI
from wd_api import wd_desc

# ---
from des.ru_st_2_latin import make_en_label
from des.desc import work_one_item
from des.places import placesTable
from des.railway import railway_tables, work_railway

# ---
from API import printe
from wd_api import wd_bot
from people.new3 import translations_o

# ---
from desc_dicts.descraptions import replace_desc

# ---
from nep.bots.helps import Get_P_API_id, log_new_types
from nep.tables.lists import space_list_and_other, others_list, others_list_2, en_des_to_ar
from nep.scientific_article import make_scientific_article
from nep.nldesc import Make_space_desc, Make_others_desc
from nep.bots.tax_desc import work_taxon_desc

# ---
from nep.tables.si_tables import genders, MainTestTable, new_types, offsetbg, Qids_translate, Add_en_labels, Geo_List

# ---
Dir = Path(__file__).parent
# ---
printe.output(f"<<lightyellow>> Dir = {Dir}")
# ---
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")


# ---
def make_scientific_art(item, P31, num):
    # ---
    table = make_scientific_article(item, P31, num, TestTable=MainTestTable[1])
    # ---
    NewDesc = table["descriptions"]
    qid = table["qid"]
    rep_langs = table["fixlang"]
    # ---
    work_a_desc(NewDesc, qid, rep_langs)


def work_new_list(item, p31, ardes):
    # ---
    printe.output(" work_new_list:")
    # ---
    q = item["q"]
    NewDesc = {}
    # ---
    gg = Qids_translate.get(p31) or others_list.get(p31) or placesTable.get(p31) or {}
    # ---
    for lang in gg.keys():
        if lang not in item.get("descriptions", {}).keys():
            if gg[lang]:
                NewDesc[lang] = {"language": lang, "value": gg[lang]}
    # ---
    orig_desc = item.get("descriptions", {}).get("ar", "")
    # ---
    if p31 in others_list or p31 in others_list_2:
        print("Make_others_desc ::::")
        ar_desc = Make_others_desc("ar", item, p31, orig_desc)
    else:
        print("Make_space_desc ::::")
        ar_desc = Make_space_desc("ar", item, p31, orig_desc)
    # ---
    # if ar_desc and ardes != ar_desc :
    if ar_desc:
        NewDesc["ar"] = {"language": "ar", "value": ar_desc}
    # ---
    # printe.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )
    if NewDesc != {}:
        printe.output(f"<<lightyellow>> ** work_new_list p31:{p31}")
        work_a_desc(NewDesc, q, [])
    else:
        print("work_new_list nothing to add. ")


def work_people(item, topic, num, ardes):
    q = item["q"]
    # ---
    translations = translations_o[2]
    # ---
    topic = topic.lower().strip()
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
        himoAPI.Des_API(q, ara, "ar")
        return ""
    # ---
    taber = translations.get(topic, {})
    # ---
    printe.output(" work_people:")
    # ---
    if not taber:
        printe.output(f" no table descraptions for topic:{topic}")
        return ""
    # ---
    printe.output(taber)
    # ---
    if topic.startswith("researcher (orcid ") and (ardes.strip() == "" or ardes.startswith("باحث (orcid ")):
        arr = topic.replace("researcher (orcid ", "باحث (معرف أورسيد ")
        himoAPI.Des_API(q, arr, "ar")
    # ---
    p21 = item.get("claims", {}).get("P21", [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")
    printe.output(p21)
    # ---
    descriptions = item.get("descriptions", {})
    NewDesc = {}
    if p21_c := genders.get(p21):
        for lang in taber.keys():
            if taber[lang].get(p21_c):
                if lang not in descriptions.keys():
                    NewDesc[lang] = {"language": lang, "value": taber[lang].get(p21_c)}
                    if years and lang in ["en", "ar", "en-ca", "en-gb"]:
                        NewDesc[lang]["value"] += years
    # ---
    if NewDesc != {}:
        printe.output(f"<<lightyellow>> **{int(num)}: work_people:{q}  ({topic})")
        work_a_desc(NewDesc, q, [])
    else:
        print(" work_people nothing to add. ")


def work_qid_desc(item, topic, num):
    printe.output("<<lightyellow>>  work_qid_desc: ")
    q = item["q"]
    descriptions = item.get("descriptions", {})
    NewDesc = {}
    addedlangs = []
    # ---
    for lang in Qids_translate[topic].keys():
        # ---
        des_for_lang = replace_desc.get(lang, {})
        # ---
        if lang not in descriptions.keys():
            # descriptions[lang] = Qids_translate[topic][lang]
            NewDesc[lang] = {"language": lang, "value": Qids_translate[topic][lang]}
            addedlangs.append(lang)
        elif descriptions[lang] in des_for_lang:
            orgdisc = descriptions[lang]
            NewDesc[lang] = {"language": lang, "value": des_for_lang[orgdisc]}
    # ---
    if not NewDesc:
        print("work_qid_desc nothing to add. ")
        return
    # ---
    printe.output(f"<<lightyellow>> **{int(num)}: work_qid_desc:{q}  ({topic})")
    work_a_desc(NewDesc, q, [])


def ISRE(qitem, num, lenth, no_donelist=True, P31_list=False):
    # ---
    printe.output(f"--- *<<lightyellow>> >{num}/{lenth}: q:{qitem}")
    # ---
    if num < offsetbg[1]:
        return ""
    # ---
    item = wd_bot.Get_Item_API_From_Qid(qitem, props="claims|descriptions|labels")
    # ---
    q = qitem
    # ---
    if not item:
        printe.output(f'*<<lightred>> >{int(num)} error with item "{q}" < :')
        return
    # ---
    if item.get("q", q) != q:
        q = item.get("q", q)
        print(f"new qid:{q}")
    # ---
    if Add_en_labels[1]:
        labels = item.get("labels", {})
        if labels.get("en", "") == "":
            printe.output("item enlabel == ''")
            make_en_label(labels, q, Add=Add_en_labels[1])
    # ---
    P31_table = []
    # ---
    if P31_list and P31_list != [] and isinstance(P31_list, list):
        P31_table = P31_list
    else:
        P31_table = Get_P_API_id(item, "P31")
    # ---
    descriptions = item.get("descriptions", {})
    endes = descriptions.get("en", "")
    if not endes:
        endes = descriptions.get("nl", "")
    ardes = descriptions.get("ar", "")
    # ---
    if len(P31_table) == 0:
        printe.output("no P31 at item. skip..")
    # ---
    for P31 in P31_table:
        # ---
        if not P31:
            continue
        # ---
        # printe.output( item )
        printe.output(f'q:"{q}", P31:"{P31}", en:"{endes}", ar:"{ardes}"')
        # ---
        if P31 == "Q5":
            # printe.output( 'endes "%s"' % endes )
            work_people(item, endes.lower(), num, ardes)
            break
        # ---
        elif P31 in railway_tables:
            work_railway(item, P31)
            break
        # ---
        elif P31 in space_list_and_other or P31 in others_list or P31 in others_list_2:
            work_new_list(item, P31, ardes)
            break
        # ---
        elif P31 == "Q16521":
            work_taxon_desc(item, endes)
            break
        # ---
        elif P31 in Geo_List and placesTable.get(P31, {}).get("ar"):
            work_one_item(placesTable.get(P31, {}).get("ar"), "ar", {"q": item["q"]}, 0, 1, findlab=True)
            break
        # ---
        elif P31 == "Q13442814":
            sc_desc = ["", "مقالة علمية", "مقالة بحثية"]
            if ardes in sc_desc:
                if "workibrahem" not in sys.argv:
                    make_scientific_art(item, P31, num)
            break
        # ---
        elif P31 in Qids_translate:
            work_qid_desc(item, P31, num)
            break
        # ---
        elif not ardes:
            printe.output(f"*<<lightred>> >P31 :{P31} not in Qids_translate.")
            # ---
            if P31 not in new_types:
                new_types[P31] = 0
            # ---
            new_types[P31] += 1


def print_new_types():
    lists = [[y, x] for x, y in new_types.items()]
    lists.sort(reverse=True)
    # ---
    log_new_types(lists)
    # ---
    for lenth, p31 in lists:
        # ---
        printe.output(f"find:{int(lenth)} : P31:{p31}")


def work_a_desc(NewDesc, qid, fixlang):
    # ---
    if MainTestTable[1] or "dd" in sys.argv:
        printe.output("<<lightyellow>> Without save:")
        printe.output(NewDesc.keys())
        printe.output(NewDesc)
        return ""
    # ---
    wd_desc.work_api_desc(NewDesc, qid, fixlang=fixlang)

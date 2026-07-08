#!/usr/bin/python3
""" """

import logging
import sys

from wd_api import wd_bot
from wd_api.wd_desc import work_api_desc

from des.desc import work_one_item
from des.places import PLACES_TABLE
from des.railway import railway_tables, work_railway
from des.ru_st_2_latin import make_en_label
from desc_dicts.descraptions_dict_new import get_data
from nep.bots.helps import Get_P_API_id, log_new_types
from nep.bots.scientific_article import make_scientific_article
from nep.bots.tax_desc import work_taxon_desc
from nep.new_way import P1433_en_to_qid, P1433_ids, do_P1433_ids
from nep.space_others import Make_others_desc, Make_space_desc
from nep.tables.lists import others_list, others_list_2, space_list_and_other
from nep.tables.si_tables import (
    Add_en_labels,
    Geo_List,
    MainTestTable,
    Qids_translate,
    new_types,
    offsetbg,
)
from nep.wr_people import work_people
from people.people_get_topic import print_new_jobs

logger = logging.getLogger(__name__)


def work_a_desc(new_desc_data, qid, fixlang) -> str:
    # ---
    if MainTestTable[1] or "dd" in sys.argv:
        logger.info("<<lightyellow>> Without save:")
        logger.info(new_desc_data.keys())
        logger.info(new_desc_data)
        return ""
    # ---
    work_api_desc(new_desc_data, qid, fixlang=fixlang)


def make_scientific_art(item, p31, num: int) -> None:
    # ---
    table = make_scientific_article(item, p31, num, testtable=MainTestTable[1])
    # ---
    new_desc_data = table["descriptions"]
    qid = table["qid"]
    rep_langs = table["fixlang"]
    # ---
    work_a_desc(new_desc_data, qid, rep_langs)


def do_P1433_new_list(item, p31) -> None:
    # ---
    logger.info(" do_P1433_new_list: ")
    # ---
    q = item["q"]
    new_desc_data = {}
    # ---
    orig_desc = item.get("descriptions", {}).get("ar", "")
    # ---
    ar_desc = do_P1433_ids(item, p31, orig_desc)
    # ---
    if ar_desc:
        new_desc_data["ar"] = {"language": "ar", "value": ar_desc}
        logger.info(f"<<lightyellow>> ** do_P1433_new_list p31:{p31}")
        work_a_desc(new_desc_data, q, [])
    else:
        print("do_P1433_new_list nothing to add. ")


def work_new_list(item, p31, ardes) -> None:
    # ---
    logger.info(f" work_new_list: {ardes=}")
    # ---
    q = item["q"]
    new_desc_data = {}
    # ---
    gg = Qids_translate.get(p31) or others_list.get(p31) or PLACES_TABLE.get(p31) or {}
    ggx = {}
    # ---
    for lang in ggx.keys():
        if lang not in item.get("descriptions", {}).keys():
            if gg[lang]:
                new_desc_data[lang] = {"language": lang, "value": gg[lang]}
    # ---
    orig_desc = item.get("descriptions", {}).get("ar", "")
    en_desc = item.get("descriptions", {}).get("en", "")
    # ---
    # ar_desc = Make_others_desc("ar", item, p31, orig_desc)
    # # ---
    # if not ar_desc:
    #     ar_desc = Make_space_desc("ar", item, p31, orig_desc)
    # ---
    if p31 in others_list or p31 in others_list_2:
        print("Make_others_desc ::::")
        ar_desc = Make_others_desc("ar", item, p31, orig_desc)

    elif p31 in P1433_ids or en_desc.lower() in P1433_en_to_qid:
        ar_desc = do_P1433_ids(item, p31, orig_desc)

    else:
        ar_desc = Make_space_desc("ar", item, p31, orig_desc)
    # ---
    # if ar_desc and ardes != ar_desc :
    if ar_desc:
        new_desc_data["ar"] = {"language": "ar", "value": ar_desc}
    # ---
    # logger.info( '<<lightyellow>>  new_desc_data' + str(new_desc_data) )
    if new_desc_data != {}:
        logger.info(f"<<lightyellow>> ** work_new_list p31:{p31}")
        work_a_desc(new_desc_data, q, [])
    else:
        print("work_new_list nothing to add. ")


def work_qid_desc(item, topic, num: int) -> None:
    logger.info("<<lightyellow>>  work_qid_desc: ")
    q = item["q"]
    descriptions = item.get("descriptions", {})
    new_desc_data = {}
    addedlangs = []
    # ---
    replace_descraptions = get_data("replace_descraptions")
    # ---
    for lang in Qids_translate[topic].keys():
        # ---
        des_for_lang = replace_descraptions.get(lang, {})
        # ---
        if lang not in descriptions.keys():
            # descriptions[lang] = Qids_translate[topic][lang]
            new_desc_data[lang] = {"language": lang, "value": Qids_translate[topic][lang]}
            addedlangs.append(lang)
        elif descriptions[lang] in des_for_lang:
            orgdisc = descriptions[lang]
            new_desc_data[lang] = {"language": lang, "value": des_for_lang[orgdisc]}
    # ---
    if not new_desc_data:
        print("work_qid_desc nothing to add. ")
        return
    # ---
    if len(new_desc_data) < 5:
        logger.info(f"<<lightyellow>> len of new_desc_data < 5: ({str(new_desc_data)})")
        return
    # ---
    logger.info(f"<<lightyellow>> **{num}: work_qid_desc:{q}  ({topic})")
    work_a_desc(new_desc_data, q, [])


def ISRE(qitem, num: int, lenth, no_donelist: bool = True, p31_list: bool = False, get_nl_des: bool = True):
    # ---
    logger.info(f"--- *<<lightyellow>> >{num}/{lenth}: q:{qitem}")
    # ---
    if num < offsetbg[1]:
        return ""
    # ---
    item = wd_bot.Get_Item_API_From_Qid(qitem, props="claims|descriptions|labels")
    # ---
    q = qitem
    # ---
    if not item:
        logger.info(f'*<<lightred>> >{num} error with item "{q}" < :')
        return None
    # ---
    if item.get("q", q) != q:
        q = item.get("q", q)
        print(f"new qid:{q}")
    # ---
    if Add_en_labels[1]:
        labels = item.get("labels", {})
        if labels.get("en", "") == "":
            logger.info("item enlabel == ''")
            make_en_label(labels, q, add_it=Add_en_labels[1])
    # ---
    P31_table = []
    # ---
    if p31_list and p31_list != [] and isinstance(p31_list, list):
        P31_table = p31_list
    else:
        P31_table = Get_P_API_id(item, "P31")
    # ---
    descriptions = item.get("descriptions", {})
    endes = descriptions.get("en", "")
    # ---
    if not endes and get_nl_des:
        endes = descriptions.get("nl", "")
    # ---
    ardes = descriptions.get("ar", "")
    # ---
    if len(P31_table) == 0:
        # print(item)
        logger.info("no P31 at item. skip..")
    # ---
    for P31 in P31_table:
        # ---
        if not P31:
            continue
        # ---
        logger.info(f'q:"{q}", P31:"{P31}", en:"{endes}", ar:"{ardes}"')
        # ---
        if P31 == "Q5":
            work_people(item, endes.lower(), num, ardes)
            break
        # ---
        elif P31 == "Q16521":
            work_taxon_desc(item, endes)
            break
        # ---
        elif P31 in railway_tables:
            work_railway(item, P31)
            break
        # ---
        elif P31 in P1433_ids or endes.lower() in P1433_en_to_qid:
            do_P1433_new_list(item, P31)
            break
        # ---
        elif P31 in space_list_and_other or P31 in others_list or P31 in others_list_2:
            work_new_list(item, P31, ardes)
            break
        # ---
        elif P31 in Geo_List and PLACES_TABLE.get(P31, {}).get("ar"):
            work_one_item(
                PLACES_TABLE.get(P31, {}).get("ar"),
                "ar",
                {"q": item["q"]},
                0,
                1,
                findlab=True,
            )
            break
        # ---
        elif P31 == "Q13442814":
            if "workibrahem" not in sys.argv:
                make_scientific_art(item, P31, num)
        # ---
        elif P31 in Qids_translate:
            work_qid_desc(item, P31, num)
            break
        # ---
        elif not ardes:
            logger.info(f"*<<lightred>> >P31 :{P31} not in Qids_translate.")
            # ---
            if P31 not in new_types:
                new_types[P31] = 0
            # ---
            new_types[P31] += 1


def print_new_types() -> None:
    lists = [[y, x] for x, y in new_types.items()]
    lists.sort(reverse=True)
    # ---
    log_new_types(lists)
    # ---
    for lenth, p31 in lists:
        # ---
        logger.info(f"find:{lenth} : P31:{p31}")
    # ---
    print_new_jobs()

#!/usr/bin/python3
"""

from bots_subs.wd_api import wd_desc
# wd_desc.wwdesc(NewDesc, qid, i, fixlang, ask="", tage='')
# wd_desc.work_api_desc(NewDesc, qid)

"""

import json
import logging
import os
import sys
import time
from datetime import datetime

from bots_subs.hi_api import NewHimoAPIBot

WD_API_Bot = NewHimoAPIBot(mr_or_bot="bot", www="www")


logger = logging.getLogger(__name__)

file_name = os.path.basename(__file__)

menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")

# [[Topic:Xr8nyeau0ysm1zop]]
langs_to_del = ["en-gb", "en-ca", "de-at", "de-ch", "zh-cn", "zh-sg", "zh-my", "zh-hk", "zh-mo", "zh-tw"]


def del_keys(d):
    for key in langs_to_del:
        if key in d:
            del d[key]
    return d


def wwdesc(NewDesc, qid, i, fixlang, ask="", tage=""):
    """Process and update descriptions for a given query ID.

    This function takes a dictionary of new descriptions and processes it to
    update the descriptions associated with a specific query ID. It filters
    out languages that are not in the `fixlang` list, sorts the remaining
    languages, and prepares a summary of the actions taken. The function
    handles various scenarios, including skipping certain languages and
    retrying the operation if necessary. It also manages potential errors
    related to API calls and outputs relevant information for debugging.

    Args:
        NewDesc (dict): A dictionary containing new descriptions keyed by language codes.
        qid (str): The query ID for which the descriptions are being updated.
        i (int): The attempt number for the operation.
        fixlang (list): A list of language codes that should be fixed or updated.
        ask (str?): Additional parameters for the operation (default is an empty string).
        tage (str?): Tags associated with the operation (default is an empty string).

    Returns:
        tuple: A tuple containing a boolean indicating success and the updated NewDesc
            dictionary.
    """

    # ---
    NewDesc = del_keys(NewDesc)
    # ---
    queries_list = []
    # ---
    for x in NewDesc.keys():
        if x not in fixlang:
            queries_list.append(x)
    # ---
    queries_list.sort()
    # ---
    data = {"descriptions": NewDesc}
    data3 = json.JSONEncoder().encode(data)
    # ---
    langes = list(NewDesc.keys())
    # ---
    if len(langes) == 2 and "en-gb" in langes and "en-ca" in langes:
        logger.info("wwdesc: only en-gb and en-ca, Skipp... ")
        return
    # ---
    # dlangs = ','.join(queries_list)
    # summary = ('Bot: - Add descriptions:(%d langs) %s' % ( len(queries_list), str(dlangs) )) #ملخص العمل
    summary = "Bot: "
    # ---
    if queries_list:
        summary += f"- Add descriptions:({len(queries_list)} langs)."
    # ---
    if fixlang:
        for ii in fixlang:
            if ii not in NewDesc.keys():
                fixlang.remove(str(ii))
                logger.info(f'remove "{ii}" from fixlang because it\'s not in NewDesc')
        # ---
        fixed = ",".join(fixlang)
        # ---
        summary = f"{summary}- fix descriptions:({len(fixlang)}: {str(fixed)})."
    # ---
    logger.info(summary)
    # ---
    if "workibrahem" in sys.argv:
        summary = ""
    # ---
    skipplang = []
    # ---
    if queries_list == [] and fixlang == []:
        logger.info("  *** no addedlangs")
        return
    # ---
    value = ""
    if "ar" in NewDesc:
        value = NewDesc["ar"]["value"]
    elif queries_list:
        try:
            key = queries_list[0]
            value = f"{NewDesc[key]['value']}@{key}"
        except Exception as e:
            logger.exception("Exception:", exc_info=True)
            value = ""
    # ---
    logger.info(
        f'* wd_desc.py wwdesc "{qid}" try number:"{i}", len NewDesc:"{len(NewDesc)}", len queries_list:"{len(queries_list)}"'
    )
    # ---
    logger.info(f'*work_api_desc {str(qid)} "{value}": try "{i}",{menet}:')
    # ---
    if "printdisc" in sys.argv:
        logger.info(data3)
    # ---
    skipp = WD_API_Bot.New_Mult_Des_2(qid, data3, summary, "", return_result=True, ask=ask, tage=tage)
    # ---
    if not skipp:
        logger.info("<<lightred>> - no skipp ")
        return
    # ---
    err_wait = "احترازًا من الإساء، يُحظر إجراء هذا الفعل مرات كثيرة في فترةٍ زمنية قصيرة، ولقد تجاوزت هذا الحد"
    # ---
    if "success" in skipp:
        # logger.info(summary)
        logger.info(f"<<lightgreen>> **{qid} true. {summary}")
        return True, NewDesc
    # ---
    if ("using the same description text" in skipp) and ("associated with language code" in skipp):
        skipp = skipp.split("using the same description text")[0].split("associated with language code")[1]
        skipplang = skipp.strip().split(",")
        # ---
        NewDesc2 = NewDesc
        if len(skipplang) != 0:
            logger.info(f'skiping languages: "{str(skipplang)}"')
            # logger.info(keys)
            for lango in skipplang:
                if lango:
                    del NewDesc2[lango]
        # ---
        i += 1
        logger.info(f"<<lightred>> try {i} again with remove skipplang ")
        wwdesc(NewDesc2, qid, i, fixlang, ask=ask, tage=tage)
        # ---
    elif "wikibase-api-invalid-json" in skipp:
        logger.info('<<lightred>> - "wikibase-api-invalid-json" ')
        logger.info(NewDesc)

    elif err_wait in skipp:
        logger.info(f'<<lightred>> {file_name} - "{err_wait} time.sleep(5) " ')
        time.sleep(5)

    else:
        logger.info(skipp)


def work_api_desc(NewDesc, qid, fixlang=[]):
    # ---
    NewDesc = del_keys(NewDesc)
    # ---
    langes = list(NewDesc.keys())
    # ---
    lang_to_skip = ["tg-latn", "en-gb", "en-ca"]
    # ---
    if len(langes) == 1:
        lang = list(NewDesc.keys())[0]
        # ---
        if lang in lang_to_skip:
            logger.info(f'work_api_desc:"{qid}" only en-gb and en-ca, Skipp... ')
            return
        # ---
        onedesc = NewDesc[lang]["value"]
        logger.info(f'work_api_desc:"{qid}" only one desc"{lang}:{onedesc}"')
        WD_API_Bot.Des_API(qid, onedesc, lang)
        return
    # ---
    elif len(langes) == 2 and langes[0] in lang_to_skip and langes[1] in lang_to_skip:
        logger.info(f'work_api_desc:"{qid}" only en-gb and en-ca, Skipp... ')
        return
    # ---
    for fix in fixlang:
        if fix not in NewDesc.keys():
            fixlang.remove(str(fix))
    fixlang.sort()
    # ---
    wwdesc(NewDesc, qid, 1, fixlang)

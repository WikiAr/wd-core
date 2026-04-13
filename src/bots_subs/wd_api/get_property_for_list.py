#!/usr/bin/python3
"""

Usage:
# from bots_subs.wd_api import get_property_for_list
# get_property_for_list.get_property_label_for_qids( [property] , List )
# get_property_for_list.get_properties_label( [property] , List )

"""
import json
import logging
import sys
from api_page import load_main_api

from . import wd_sparql_bot


logger = logging.getLogger(__name__)


def get_property_label_for_qids(properties, List):
    # ---
    # logger.info('start get_property_label_for_qids:' )
    # ---
    title = "ويكيبيديا:ملعب"
    text = ""
    # ---
    num = 0
    # ---
    for qid in List:
        num += 1
        lino = "{{subst:user:Mr._Ibrahem/line2|%s" % qid
        for prop in properties:
            lino += f"|{prop}"
        lino += "}}\n"
        # if num == 1 : logger.info(lino)
        text += lino
    # ---
    if "printprase" in sys.argv:
        print(text)
    # ---
    api = load_main_api("ar")
    jso = api.NEW_API().Parse_Text(text, "ويكيبيديا:ملعب")
    # ---
    if not jso:
        logger.info('get_property_label_for_qids: jso == ""')
        return False
    # ---
    elif jso == text:
        logger.info("<<lightred>> get_property_label_for_qids: jso == text ")
        return False
    # ---
    newtabe = json.loads("{\n" + jso + '\n"cdcdcd":{}\n}')
    # ---
    if newtabe:
        del newtabe["cdcdcd"]
    # ---
    # logger.info( newtabe )
    # ---
    return newtabe


def add_prop(x, qua):
    # qua = qua
    # ---
    print(f"add_prop:x:{x}")
    # ---
    if not x.strip():
        return qua
    # ---
    qua = qua.replace("#sr1", f'(GROUP_CONCAT(?{x}zllabel; SEPARATOR = "@") AS ?{x})\n#sr1')
    qua = qua.replace("#sr2", "optional {" + f"?item wdt:{x} ?{x}z." + "}\n#sr2")
    qua = qua.replace("#sr3", f"?{x}z rdfs:label ?{x}zllabel.\n#sr3")
    # ---
    return qua


def get_properties_label(properties, qids):
    # ---
    qu1_qid = """
        SELECT DISTINCT
        ?page
        (concat(strafter(str(?item),"/entity/")) as ?q )
        #(GROUP_CONCAT(?P27zllabel; SEPARATOR = "@") AS ?P27)
        #sr1

        WHERE {
            VALUES ?item { %s }
            #?item wdt:P27 ?P27z.
            #sr2
            ?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ;  schema:name ?page .
            SERVICE wikibase:label {
                bd:serviceParam wikibase:language "ar,en" .
                #?P27z rdfs:label ?P27zllabel.
                #sr3
            }
        }
        GROUP BY ?item ?page
    """
    # ---
    qui = qu1_qid % " ".join([f"wd:{q}" for q in qids])
    # ---
    for x in properties:
        qui = add_prop(x, qui)
    # ---
    if "doerr" in sys.argv:
        logger.info(qui)
    # ---
    wdo = wd_sparql_bot.sparql_generator_url(qui)
    # ---
    wd = {}
    # ---
    for x in wdo:
        q = x["q"]
        del x["q"]
        wd[q] = x
    # ---
    return wd

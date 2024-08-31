#!/usr/bin/python3
"""
from nep.bots.tax_desc import work_taxon_desc
"""
import sys
from himo_api import himoAPI
from wd_api import wd_bot
from newapi import printe
from desc_dicts.taxones import lab_for_p171, labforP105
from desc_dicts.taxones import tax_translationsNationalities, taxone_list

# ---
from nep.bots.helps import Get_P_API_id

tax_translations_lower = {}
# ---
for tax_key, tax_lab in taxone_list.items():  # الأصنوفة
    if tax_lab.strip() and tax_key.strip():
        for natkey in sorted(tax_translationsNationalities.keys()):  # النوع
            natar = tax_translationsNationalities[natkey]
            if natkey.strip() and natar.strip():
                kkey = tax_key.replace("~", natkey)
                tax_translations_lower[kkey.lower()] = tax_lab.replace("~", natar)


def make_tax_des_new(item):
    q = item["q"]
    # ---
    P171 = Get_P_API_id(item, "P171")
    # ---
    if not P171:
        return ""
    # ---
    P105 = Get_P_API_id(item, "P105")
    P105ar = next((labforP105[p] for p in P105 if p in labforP105), "")
    # ---
    if not P105ar:
        return ""
    # ---
    nan = """SELECT DISTINCT ?item ?P171 ?item105
    WHERE {
        BIND(wd:Q111771064 AS ?item)
    VALUES ?P171 {
    %s
    }
        ?item wdt:P31 wd:Q16521.
        ?item wdt:P171* ?P171.
        ?P171 wdt:P105 wd:Q37517.
        ?item wdt:P105 ?item105.
    }""" % " ".join(
        [f"wd:{x}" for x in lab_for_p171.keys()]
    )
    nan = nan.replace("Q111771064", q)
    # ---
    if "err" in sys.argv:
        printe.output(nan)
    # ---
    bs = wd_bot.sparql_generator_url(nan)
    # ---
    if bs != []:
        bs = bs[0]
        printe.output("bs:")
        printe.output(bs)
        # ---
        # [
        # {'P171': 'http://www.wikidata.org/entity/Q1390',
        # 'item': 'http://www.wikidata.org/entity/Q111771066',
        # 'item105': 'http://www.wikidata.org/entity/Q7432'}
        # ]
        itq = bs["item"].split("/entity/")[1]
        if itq == q:
            item105 = bs["item105"].split("/entity/")[1]
            P171 = bs["P171"].split("/entity/")[1]
            # ---
            if P171 in lab_for_p171.keys():
                P171ar = lab_for_p171[P171]
                ar_lab = f"{P105ar} {P171ar}"
                himoAPI.Des_API(q, ar_lab, "ar")


def work_taxon_desc(item, endesc):
    # ---
    ardesc = tax_translations_lower.get(endesc.lower(), "")  # .get("ar", '')
    q = item["q"]
    # printe.output( ' work_taxon_desc:endesc:"%s", ardesc:"%s"' % (endesc, ardesc) )
    printe.output(f' work_taxon_desc:ardesc:"{ardesc}"')
    if not ardesc:
        print(f" no ardesc for en:{endesc}.")
        make_tax_des_new(item)

    himoAPI.Des_API(q, ardesc, "ar")

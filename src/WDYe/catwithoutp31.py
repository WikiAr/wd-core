#!/usr/bin/python3
"""

إضافة حالة خاصة من تصنيف ويكيميديا
للتصانيف دون ذلك

python3 core8/pwb.py WDYe/catwithoutp31

"""
import logging
import re

from bots_subs.hi_api import HimoAPIBot
from bots_subs.wd_api import wd_bot, wd_sparql_bot
from bots_subs.wd_api.wd_bot import Get_infos_wikidata
from bots_subs.wd_api.wd_desc import work_api_desc
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions

logger = logging.getLogger(__name__)
WD_API_Bot = HimoAPIBot(mr_or_bot="bot", www="www")

Tras = {
    "Q4167836": DescraptionsTable.get("Wikimedia category") or Qid_Descraptions.get("Q4167836") or {},
}


# python pwb.py np/d -family:wikidata -lang:wikidata -newpages:10
# python pwb.py np/d -family:wikidata -lang:wikidata -ns:0 -start:Q32000000

quaries = {
    "ar": """ SELECT ?item
        WHERE
        {
        ?item wikibase:statements 0 .
        ?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?title .
        FILTER(strstarts(str(?title),"تصنيف:") )
        }
        LIMIT 1000""",
    "en": """ SELECT ?item
        WHERE
        {
        ?item wikibase:statements 0 .
        ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?title .
        FILTER(strstarts(str(?title),"Category:") )
        }
        LIMIT 1000""",
}


def Get_Sitelinks_From_wikidata(site, title, ssite="", ids="", props="", add_props=None, return_main_table=False):
    # ---
    sitewiki = site
    if site.find("wiki") == -1:
        sitewiki = f"{site}wiki"
    # ---
    params = {
        "action": "wbgetentities",
        "props": "sitelinks",
        # "props": "sitelinks|templates",
        "sites": sitewiki,
        "titles": title,
        "normalize": 1,
        # "tlnamespace": "10",
        # "tllimit": "max",
        # "tltemplates": "Template:Category redirect",
    }
    # ---
    if props:
        params["props"] = props
    # ---
    if isinstance(add_props, (list, tuple)):
        for x in add_props:
            if x not in params["props"]:
                params["props"] += f"|{x}"
    # ---
    if ids:
        params["ids"] = ids
        del params["sites"]
        del params["titles"]
    # ---
    table = Get_infos_wikidata(params)
    # ---
    if return_main_table:
        return table
    # ---
    if table:
        table["site"] = sitewiki
    # ---
    ssite2 = ssite
    if not ssite.endswith("wiki"):
        ssite2 += "wiki"
    # ---
    if ssite:
        sitelinks = table.get("sitelinks", {})
        result = sitelinks.get(ssite) or sitelinks.get(ssite2) or ""
        return result
    # ---
    return table


def work_one_item(q):
    # ---
    # claims
    P31 = wd_bot.Get_Property_API(q=q, p="P31")
    # ---
    P31 = P31[0] if P31 and isinstance(P31, list) else ""
    # ---
    links = Get_Sitelinks_From_wikidata("", "", ssite="", ids=q)
    # ---
    labels = wd_bot.Get_item_descriptions_or_labels(q, "labels")
    descriptions = wd_bot.Get_item_descriptions_or_labels(q, "descriptions")
    # ---
    if not P31 or P31 != "Q4167836":
        WD_API_Bot.Claim_API2(q, "P31", "Q4167836")
    # ---
    # labels
    data2 = {"labels": {}}
    # ---
    for site in links.keys():
        label = str(links[site])
        lang = re.sub(r"wiki$", "", str(site))
        if lang != label and lang not in labels.keys():
            data2["labels"][lang] = {"language": lang, "value": label}
    # ---
    logger.info(f"<<lightred>>* links :{links}")
    logger.info(f"<<lightred>>* labels :{labels}")
    logger.info(f"<<lightred>>* data2[\"labels\"] :{data2['labels']}")
    # ---
    if len(data2["labels"].keys()) > 0:
        summary = f"Bot: - Add labels:({len(data2['labels'])} langs)."
        WD_API_Bot.New_Mult_Des(q, data2, summary, False)
    # ---
    catdesc = Tras["Q4167836"]
    # ---
    if "en" in catdesc.keys():
        catdesc["en-ca"] = catdesc["en"]
        catdesc["en-gb"] = catdesc["en"]
    # ---
    NewDesc = {
        str(lang): {"language": str(lang), "value": str(catdesc[lang])}
        for lang in catdesc.keys()
        if lang not in descriptions.keys()
    }
    # ---
    if NewDesc:
        logger.info(f"<<lightyellow>>* adding descriptions to :{q} ")
        work_api_desc(NewDesc, q)
    else:
        logger.info(f"<<lightred>>* work 2 :{q} no descriptions to add.")


def main():
    # ---
    for qua_a in quaries:
        qua = quaries[qua_a]
        # ---
        json1 = wd_sparql_bot.wd_sparql_generator_url(qua, returnq=True)
        # ---
        total = len(json1)
        # ---
        for c, q in enumerate(json1, start=1):
            # ---
            logger.info(f'  * action {c}/{total} "{q}"')
            # ---
            work_one_item(q)


if __name__ == "__main__":
    main()

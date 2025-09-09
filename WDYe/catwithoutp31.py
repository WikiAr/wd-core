#!/usr/bin/python3
"""

إضافة حالة خاصة من تصنيف ويكيميديا
للتصانيف دون ذلك

python3 core8/pwb.py WDYe/catwithoutp31

"""
import pywikibot
import re
from wd_api import wd_desc
from wd_api import wd_bot

# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="bot", www="www")
# ---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions

Tras = {
    "Q4167836": DescraptionsTable.get("Wikimedia category") or Qid_Descraptions.get("Q4167836") or {},
}


# python pwb.py np/d -family:wikidata -lang:wikidata -newpages:10
# python pwb.py np/d -family:wikidata -lang:wikidata -ns:0 -start:Q32000000
# ---
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


def work_one_item(q):
    # ---
    # claims
    P31 = wd_bot.Get_Property_API(q=q, p="P31")
    # ---
    P31 = P31[0] if P31 and isinstance(P31, list) else ""
    # ---
    links = wd_bot.Get_Sitelinks_from_qid(ids=q)
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
    pywikibot.output(f"<<lightred>>* links :{links}")
    pywikibot.output(f"<<lightred>>* labels :{labels}")
    pywikibot.output(f"<<lightred>>* data2[\"labels\"] :{data2['labels']}")
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
    NewDesc = {str(lang): {"language": str(lang), "value": str(catdesc[lang])} for lang in catdesc.keys() if lang not in descriptions.keys()}
    # ---
    if NewDesc:
        pywikibot.output(f"<<lightyellow>>* adding descriptions to :{q} ")
        wd_desc.work_api_desc(NewDesc, q)
    else:
        pywikibot.output(f"<<lightred>>* work 2 :{q} no descriptions to add.")


def main():
    # ---
    for qua_a in quaries:
        qua = quaries[qua_a]
        # ---
        json1 = wd_bot.wd_sparql_generator_url(qua, returnq=True)
        # ---
        total = len(json1)
        # ---
        for c, q in enumerate(json1, start=1):
            # ---
            pywikibot.output(f'  * action {c}/{total} "{q}"')
            # ---
            work_one_item(q)


if __name__ == "__main__":
    main()

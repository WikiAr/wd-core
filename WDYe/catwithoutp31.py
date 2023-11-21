#!/usr/bin/python3
"""

إضافة حالة خاصة من تصنيف ويكيميديا
للتصانيف دون ذلك

python3 core8/pwb.py WDYe/catwithoutp31

"""
#
# (C) Ibrahem Qasim, 2022
#

import pywikibot

# import pwb
import re

# ---
# ---
from wd_api import wd_bot
from wd_api import wd_desc

# ---
from wd_api import himoAPI

# ---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions

Tras = {'Q4167836': DescraptionsTable.get('Wikimedia category') or Qid_Descraptions.get('Q4167836') or {}}


def Get_P_API2(item, P):
    if item:
        item.get()
        claims = item.claims
        if P in claims:
            PP31 = item.claims[P][0].toJSON()
            q = PP31['mainsnak']['datavalue']['value']['numeric-id'] or ''
            if q:
                qq = 'Q' + str(q)
                # pywikibot.output('%s: %s.' % (P,qq) )
                return qq
    return False


# ---
# python pwb.py np/d -family:wikidata -lang:wikidata -newpages:10
# python pwb.py np/d -family:wikidata -lang:wikidata -ns:0 -start:Q32000000
# ---
quaries = {}
quaries[
    "ar"
] = """ SELECT ?item
WHERE
{
  ?item wikibase:statements 0 .
  ?article schema:about ?item ; schema:isPartOf <https://ar.wikipedia.org/> ; schema:name ?title .
  FILTER(strstarts(str(?title),"تصنيف:") )
}
LIMIT 1000"""

quaries[
    "en"
] = """ SELECT ?item
WHERE
{
  ?item wikibase:statements 0 .
  ?article schema:about ?item ; schema:isPartOf <https://en.wikipedia.org/> ; schema:name ?title .
  FILTER(strstarts(str(?title),"Category:") )
}
LIMIT 1000"""


def work_one_item(item):
    item.get()
    # ---
    q = item.title(as_link=False)
    # ---
    # claims
    P31 = Get_P_API2(item, 'P31')
    if not P31 or P31 != "Q4167836":
        himoAPI.Claim_API2(q, "P31", "Q4167836")
    # ---
    # ---
    # labels
    data2 = {}
    data2["labels"] = {}
    labels = item.labels
    links = item.sitelinks
    # ---
    for site in links.keys():
        label = links[site]
        lang = re.sub(r"wiki$", "", site)
        if lang != label and lang not in labels.keys():
            data2['labels'][lang] = {'language': lang, 'value': label}
    # ---
    pywikibot.output(f'<<lightred>>* links :{links}')
    pywikibot.output(f'<<lightred>>* labels :{labels}')
    pywikibot.output(f"<<lightred>>* data2[\"labels\"] :{data2['labels']}")
    if len(data2["labels"].keys()) > 0:
        summary = f"Bot: - Add labels:({len(data2['labels'])} langs)."
        himoAPI.New_Mult_Des(q, data2, summary, False)
    # ---
    # ---
    # ---
    # descriptions
    NewDesc = {}
    descriptions = item.descriptions
    catdesc = Tras["Q4167836"]
    # ---
    if 'en' in catdesc.keys():
        catdesc['en-ca'] = catdesc['en']
        catdesc['en-gb'] = catdesc['en']
    # ---
    for lang in catdesc.keys():
        if lang not in descriptions.keys():
            NewDesc[lang] = {"language": lang, "value": catdesc[lang]}
    # ---
    if NewDesc:
        pywikibot.output(f'<<lightyellow>>* adding descriptions to :{q} ')
        wd_desc.work_api_desc(NewDesc, q)
    else:
        pywikibot.output(f'<<lightred>>* work 2 :{q} no descriptions to add.')


def main(*args):
    # ---
    for qua_a in quaries:
        c = 0
        qua = quaries[qua_a]
        json1 = wd_bot.wd_sparql_generator_url(qua)
        total = len(json1)
        for item in json1:
            c += 1
            # ---
            q = item.title(as_link=False)
            pywikibot.output('  * action %d/%d "%s"' % (c, total, q))
            work_one_item(item)


# ---
if __name__ == "__main__":
    # work_one_item(item)
    main()
# ---

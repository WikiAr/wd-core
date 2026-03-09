#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
"""
#استعلام خنافس

SELECT DISTINCT
?en  (COUNT(?en) AS ?count) WHERE {
  ?item wdt:P171* wd:Q22671.
  ?item wdt:P105 wd:Q7432.
  #?item schema:description ?en.
  ?item schema:description ?en. FILTER((LANG(?en)) = "en")
}

GROUP BY ?en
ORDER BY DESC(?count)
#LIMIT 3000
"""

# ---


#   newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
#

import logging
logger = logging.getLogger(__name__)

# import sys
# import urllib
# import urllib.request
# import urllib.parse
# ---
import sys

# ---
# ---
from wd_api import wd_bot

# ---
from wd_api import wd_desc

# wd_desc.wwdesc(NewDesc, qid, i, fixlang, ask="", tage='')
# wd_desc.work_api_desc(NewDesc, qid)
# ---
quuu = {
    "species of beetle": """
SELECT DISTINCT
?item WHERE {
    BIND("species of beetle"@en AS ?en) ?item schema:description ?en.

    BIND("espèces de coléoptères"@fr AS ?fr)
    BIND("specie di coleottero"@it AS ?it)
    {?item schema:description ?it. } UNION {?item schema:description ?fr.}
    #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 20000""",
    "species of insect": """
SELECT DISTINCT
?item WHERE {
    BIND("species of insect"@en AS ?en) ?item schema:description ?en.
    BIND("espèce de coléoptères"@fr AS ?fr)
    BIND("specie di coleottero"@it AS ?it)
    {?item schema:description ?it. } UNION {?item schema:description ?fr.}
    #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 100000""",
}
# ---


# newdesc.work22(q , topic, translations)

# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
# from API.replacement import replacement
# ---
translations = {
    "species of beetle": {
        "it": "specie di coleotteri",
        # 'fr': 'espèces de coléoptères',
        "fr": "espèce de coléoptères",
    },
    "species of insect": {
        "it": "specie di insetti",
        # 'fr': "espèces d'insectes",
        "fr": "espèce d'insectes",
    },
}


def work2(q, topic):
    # ---
    ItemDescriptions = wd_bot.Get_item_descriptions_or_labels(q, "descriptions")
    # ---
    if "en" in ItemDescriptions.keys():
        en = ItemDescriptions["en"]  # ['value']
        # ---
        if en in translations.keys():
            replacement = translations[en]
            NewDesc = {}
            fixlang = []
            for lang in replacement.keys():
                if lang in ItemDescriptions.keys():
                    value = ItemDescriptions[lang]  # ['value']
                    if value != replacement[lang]:
                        NewDesc[lang] = {"language": lang, "value": replacement[lang]}
                        logger.info(f'<<lightyellow>> {lang}:replace "{value}" by: "{replacement[lang]}".')
                        fixlang.append(lang)
                else:
                    NewDesc[lang] = {"language": lang, "value": translations[topic][lang]}
                    # addedlangs.append(lang)
            # ---
            # logger.info( '<<lightyellow>>  NewDesc' + str(NewDesc) )
            wd_desc.wwdesc(NewDesc, q, 1, fixlang, ask=False)


def mam():
    topic = "species of insect"
    logger.info("*<<lightyellow>> mainfromQuarry:")
    Quarry = quuu[topic]
    if sys.argv and "OFFSET" in sys.argv:
        Quarry = f"{Quarry} OFFSET 100000"
    json = wd_bot.wd_sparql_generator_url(Quarry, returnq=True)
    lenth = len(json)
    # topic = 'Wikinews article'
    # ---
    for num, q in enumerate(json, start=1):
        logger.info(f'<<lightyellow>>*mainfromQuarry: {num}/{lenth} topic:"{topic}" , q:"{q}".')
        work2(q, topic)


if __name__ == "__main__":
    mam()

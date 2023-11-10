#!/usr/bin/env python3
#
#
#
#

import pywikibot
# ---
# ---
# ---
from wd_api import wd_bot
# wd_bot.wd_from_file(file)
# wd_bot.GetItemFromQid(q)
# ---
from wd_api import newdesc
# newdesc.main_from_file(file , topic , translations2)
# newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
replacement_ke = {
    'ar': ['قرية', 'مستوطنة', "مديرية"],
    'en': ['köy', "village", "district"],  # , "district of Turkey"
}
# ---
fas = {
    'Q1529096': {
        'ar': 'قرية في %s، تركيا',
        'en': 'köy in %s, Turkey',
        # 'en': 'village in %s, Turkey',
    },
    'Q1147395': {
        'ar': 'مديرية في %s، تركيا',
        'en': 'district in %s, Turkey',
    },
    'Q28371991': {
        'ar': 'قرية في %s، اليمن',
        'en': 'village in %s, Yemen',
    },
    'Q28373319': {
        'ar': 'محلة في %s، اليمن',
        'en': 'mahallah in %s, Yemen',
    },
    'Q12225020': {
        'ar': 'عزلة في %s، اليمن',
        'en': 'islah in %s, Yemen',
    },
    'Q28372019': {
        'ar': 'حي سكني في %s، اليمن',
        'en': 'neighborhood in %s, Yemen',
    }
}
# ---
translations = {}
'''
translations['Q1529096'] = {
            'ar': 'قرية في تركيا',
            #'en': 'village in Turkey',
            'en': 'köy in Turkey',
        }
translations['Q1147395'] = {
            'ar': 'مديرية في تركيا',
            'en': 'district in Turkey',
        }
'''
translations['Q28373319'] = {
    'ar': 'محلة في اليمن',
    'en': 'mahallah in Yemen',
}
translations['Q28371991'] = {
    'ar': 'قرية في اليمن',
    'en': 'village in Yemen',
}
translations['Q12225020'] = {
    'ar': 'عزلة في اليمن',
    'en': 'islah in Yemen',
}
translations['Q28372019'] = {
    'ar': 'حي سكني في اليمن',
    'en': 'neighborhood in Yemen',
}


def action_one_item(x, pa, new_translations):
    item = wd_bot.GetItemFromQid(pa['item'])
    if item:
        ks = {}
        ks[x] = new_translations
        # newdesc.work2(item , x, ks)
        newdesc.work2_with_replacement(item, x, ks, replacement_ke)


def make_translations(x, pa):
    ar, en = False, False
    # ---
    descriptions = {}
    # ---
    if pa["ar"] != "":
        ar = True
    if pa["en"] != "":
        en = True
    # ---
    if x in translations:
        descriptions = translations[x]
    # ---
    if ar and x in fas and "ar" in fas[x]:
        descriptions["ar"] = fas[x]["ar"] % pa["ar"]
    # ---
    if en and x in fas and "en" in fas[x]:
        descriptions["en"] = fas[x]["en"] % pa["en"]
    # ---
    return descriptions


def mainfromQuarry(x, Quarry, translations):
    PageList = wd_bot.sparql_generator_url(Quarry)
    total = len(PageList)
    num = 0
    # pywikibot.output('* PageList: ')
    for pa in PageList:
        pa['item'] = pa['item'].split('/entity/')[1]
        pywikibot.output(pa)
        num += 1
        pywikibot.output('<<lightblue>>> %s/%d : %s' % (num, total, pa['item']))
        new_translations = make_translations(x, pa)
        pywikibot.output(new_translations)
        action_one_item(x, pa, new_translations)


# ---
for x in translations:
    quarry = 'SELECT ?item ?ar ?en '
    quarry += 'WHERE { ?item wdt:P31 wd:%s.' % x
    quarry += ' ?item wdt:P131 ?P131. '
    quarry += 'OPTIONAL {?P131 rdfs:label ?ar filter (lang(?ar) = "ar")} . '
    quarry += 'OPTIONAL {?P131 rdfs:label ?en filter (lang(?en) = "en")} . '
    quarry += 'OPTIONAL {?item schema:description ?des filter(lang(?des) = "ar")}'
    quarry += 'FILTER(!BOUND(?des)) } '
    # quarry += 'LIMIT 9000 '
    mainfromQuarry(x, quarry, translations)
# ---

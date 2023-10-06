#!/usr/bin/env python3
#  python pwb.py wd/wikicatategory
#
#
from wd_api import newdesc
# site = pywikibot.Site('wikidata', 'wikidata')
# repo = site.data_repository()
from desc_dicts.descraptions import DescraptionsTable

translations = {}
translations['Wikimedia category'] = DescraptionsTable['Wikimedia category']

# import pywikibot

# item = pywikibot.ItemPage(repo, 'Q20509009')
# item.get()
list = [
    # "Q15407973",#   تصنيف ويكيميديا لصفحات التوضيح
    "Q15647814",  # تصنيف إدارة ويكيميديا
    "Q23894233",  # تصنيف قوالب ويكيميديا
    "Q24046192",  # تصنيف ويكيميديا عن البذور
    "Q24514938",  # تصنيف تتبع استخدام الخاصية
    "Q24574745",  # Commons category
    "Q29848066",  # تصنيف حول حدث في سنة أو فترة زمنية محددة
    "Q30330522",  # Unknown parameters category
]
topic = 'Wikimedia category'

quarry2 = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:Q4167836.}'
# newdesc.mainfromQuarry( topic , quarry2, translations)

for ll in list:
    quarry = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:%s.}' % ll
    newdesc.mainfromQuarry2(topic, quarry, translations)

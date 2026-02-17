#!/usr/bin/python3
"""

إضافة تسميات عناصر تصنيفات في ويكي بيانات

نسخ تسمية العنصر إلى التصنيف المطابق له في الإسم


"""
#
# (C) Ibrahem Qasim, 2022
#
#

import logging
logger = logging.getLogger(__name__)
from wd_api import wd_bot

# ---
import sys

# ---

# ---


# ---
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="mr", www="www")
# ---

# ---
Limit = {1: "500"}


def main():
    # python pwb.py wd/category
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(':')
        # ---
        if arg in ['-limit', 'limit']:
            Limit[1] = value
            logger.info(f'<<lightred>> Limit = {value}.')
            # ---#
    Quaa = '''
SELECT DISTINCT
?cat
(concat("" , str(?item_ar) , ''  )  as ?ar_name)
WHERE {
  #?item wdt:P31* wd:Q18608583.
  #?item wdt:P31* wd:Q18608583.
  #?item wdt:P31* wd:Q27020041.
 { ?cat wdt:P301 ?item. } UNION {  ?item wdt:P910 ?cat. }
 # ?item wdt:P31 wd:Q51031626.
 # ?item wdt:P910 ?cat.
   FILTER NOT EXISTS {?cat rdfs:label ?catar filter (lang(?catar) = "ar")} .
   ?item rdfs:label ?item_ar filter (lang(?item_ar) = "ar") .
   ?item rdfs:label ?item_en filter (lang(?item_en) = "en") .
   ?cat rdfs:label ?cat_en filter (lang(?cat_en) = "en") .
   BIND( concat("Category:" , str(?item_en)) as ?change_name)

  FILTER ( str(?cat_en) = str(?change_name) )
}
LIMIT '''
    Quaa += Limit[1]
    logger.info(Quaa)
    sparql = wd_bot.sparql_generator_url(Quaa)
    # ---
    Table = {}
    for item in sparql:
        q = item['cat'].split("/entity/")[1]
        Table[q] = item["ar_name"]
    for num, (item, value_) in enumerate(Table.items(), start=1):
        # if num < 2:
        logger.info(f'<<lightgreen>> {num}/{len(Table.keys())} item:"{item}" ')
        # logger.info( Table[item] )
        if value_:
            lab = f'تصنيف:{Table[item]}'
            WD_API_Bot.Labels_API(item, lab, "ar", False, Or_Alii=True)

    # ---


if __name__ == "__main__":
    main()
# ---

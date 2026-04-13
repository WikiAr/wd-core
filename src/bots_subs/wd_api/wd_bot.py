#!/usr/bin/python3
"""

"""
from . import wd_sparql_bot
from .wd_bots.get_bots import (
    Get_Item_API_From_Qid,
    Get_item_descriptions_or_labels,
    Get_Property_API_1,
    Get_Sitelinks_From_wikidata,
)

def sparql_generator_url(quary, printq=False, add_date=True, key="", geterror=False, returndict=False):
    return wd_sparql_bot.sparql_generator_url(
        quary, printq=printq, add_date=add_date, key=key, geterror=geterror, returndict=returndict
    )


def sparql_generator_big_results(spq, offset=0, limit=20000, alllimit=0):
    return wd_sparql_bot.sparql_generator_big_results(spq, offset=offset, limit=limit, alllimit=alllimit)


__all__ = [
    "Get_Sitelinks_From_wikidata",
    "Get_item_descriptions_or_labels",
    "Get_Item_API_From_Qid",
    "Get_Property_API_1",
    "sparql_generator_url",
    "sparql_generator_big_results",
]

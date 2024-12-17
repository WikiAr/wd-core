#!/usr/bin/python3
"""

python3 core8/pwb.py nep/si3g_qua

"""
from newapi import printe
from nep import si3
from wd_api import wd_bot

qua = """
SELECT DISTINCT
?item
(concat(strafter(str(?item),"/entity/"))  as ?qid)

WHERE {
        ?item wdt:P31 wd:Q5 .
        ?item wdt:P21 ?p211.
        ?item wdt:P27 ?p27.
        ?item wdt:P106 ?p106.

  FILTER NOT EXISTS {?item schema:description ?en filter (lang(?en) = "en")} .
}

LIMIT 100
"""


def main():
    printe.output("*<<lightred>> > main:")
    # ---
    lista = wd_bot.sparql_generator_url(qua)
    # ---
    printe.output("*<<lightred>> > mainwithcat2 :")
    # ---
    for num, tab in enumerate(lista, start=1):
        qid = tab["qid"]
        # {'item': 'http://www.wikidata.org/entity/Q21457154', 'qid': 'Q21457154'}
        si3.ISRE(qid, num, len(lista))
    # ---
    si3.print_new_types()


if __name__ == "__main__":
    main()

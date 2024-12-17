#!/usr/bin/python3
"""

python3 core8/pwb.py nep/si3g_qua

python3 core8/pwb.py nep/si3g_qua -p27:Q805

"""
import sys
from newapi import printe
from nep import si3
from wd_api import wd_bot
from people.people_get_topic import print_new_jobs, job_to_qid, nat_to_qid

qua = """
SELECT DISTINCT
?item
(concat(strafter(str(?item),"/entity/"))  as ?qid)

WHERE {
    #sr
    ?item wdt:P31 wd:Q5 .
    ?item wdt:P21 ?p211.
    ?item wdt:P27 ?p27.
    ?item wdt:P106 ?p106.
    FILTER NOT EXISTS {?item schema:description ?en filter (lang(?en) = "en")} .
}

"""
limit = {1: "500"}
P106 = {1: []}
P27 = {1: []}

for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg.startswith("-"):
        arg = arg[1:]
    # ---
    if arg == "limit":
        limit[1] = value
    # ---
    if arg.lower() == "p106":
        P106[1].append(value)
    # ---
    if arg.lower() == "p27":
        P27[1].append(value)

qua += f"\n limit {limit[1]}"
# ---
if P106[1]:
    line = "values ?p106 {" + " ".join([f"wd:{x}" for x in P106[1]]) + "} \n #sr"
    qua = qua.replace("#sr", line, 1)
# ---
if P27[1]:
    line = "values ?p27 {" + " ".join([f"wd:{x}" for x in P27[1]]) + "} \n #sr"
    qua = qua.replace("#sr", line, 1)


def main():
    printe.output("*<<lightred>> > main:")
    # ---
    lista = wd_bot.sparql_generator_url(qua)
    # ---
    printe.output(f"*<<yellow>> {qua} :")
    # ---
    for num, tab in enumerate(lista, start=1):
        qid = tab["qid"]
        # {'item': 'http://www.wikidata.org/entity/Q21457154', 'qid': 'Q21457154'}
        si3.ISRE(qid, num, len(lista), get_nl_des=False)
    # ---
    print_new_jobs()


if __name__ == "__main__":
    main()

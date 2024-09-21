#!/usr/bin/python3
"""
python3 core8/pwb.py neq/nldes3 a2r sparql:Q953806 ask all:100 doar

python3 core8/pwb.py neq/nldes3 test

python3 core8/pwb.py neq/nldes3 a2r sparql:dfd ask
python3 core8/pwb.py neq/nldes3 a2r sparql:Q7889 ask
python3 core8/pwb.py neq/nldes3 a2r sparql:Q7889 ask

"""
import sys
import re
import random
from newapi import printe
from nep.nldesc import action_one_item
from neq.quarries import SPARQLSE
from wd_api import wd_sparql_bot

sparqler = {1: ""}
Offq = {1: 0}
Off = {1: 0}
limit = {1: 0}
totallimit = {1: 10000}

for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg.startswith("-"):
        arg = arg[1:]
    # ---
    if arg == "off":
        Off[1] = int(value)
        printe.output("Off[1] = %d" % Off[1])
    # ---
    if arg == "offq":
        Offq[1] = int(value)
        printe.output("Offq[1] = %d" % Offq[1])
    # ---
    if arg in ["totallimit", "all"]:
        totallimit[1] = int(value)
        printe.output("totallimit[1] = %d" % totallimit[1])
    # ---
    if arg == "limit":
        limit[1] = int(value)
        printe.output("limit[1] = %d" % limit[1])
    # ---
    if arg == "sparql":
        sparqler[1] = value
        printe.output(f'sparqler[1] = "{sparqler[1]}"')


def just_get_ar(label):
    parts = label.split("@@")
    arabic_parts = [part for part in parts if part.lower() == re.sub(r"[a-z@]", "", part.lower()) and part]

    if arabic_parts:
        claim_str = "، و".join(arabic_parts)
        printe.output(f"just_get_ar: {claim_str}.")
        return claim_str

    return ""


def get_sparql_queries():
    if sparqler[1].strip() == "" or "allkeys" in sys.argv:
        return random.sample(list(SPARQLSE.values()), len(SPARQLSE))
    # ---
    quas = [x.strip() for x in sparqler[1].split(",")]
    # ---
    quaries = []
    # ---
    for x in quas:
        quaa = f"SELECT ?item WHERE {{ ?item wdt:P31 wd:{x} . FILTER NOT EXISTS {{ ?item schema:description ?itemar. FILTER((LANG(?itemar)) = 'ar') }} }}"
        # ---
        quaries.append(SPARQLSE.get(x, quaa))
    # ---
    return quaries


def process_item(wd, n, total_reads):
    q = wd["item"].split("/entity/")[1]
    # ---
    printe.output(f"p{n}/{total_reads} q:{q}")
    # ---
    claim_str = just_get_ar(wd.get("lab", ""))
    # ---
    action_one_item("ar", q, claimstr=claim_str)


def main():
    sparql_queries = get_sparql_queries()
    # ---
    for query_num, sparql_query in enumerate(sparql_queries, 1):
        printe.output("-------------------------")
        printe.output(f"<<lightblue>> query {query_num} from {len(sparql_queries)} :")
        # ---
        if Offq[1] > 0 and Offq[1] > query_num:
            continue
        # ---
        pigenerator = wd_sparql_bot.sparql_generator_big_results(sparql_query, offset=Off[1], limit=limit[1], alllimit=totallimit[1])
        # ---
        for n, wd in enumerate(pigenerator, start=1):
            printe.output("<<lightblue>> ============")
            process_item(wd, n, len(pigenerator))


if __name__ == "__main__":
    if "test" in sys.argv:
        action_one_item("ar", "Q162210")
    else:
        main()

#!/usr/bin/python3
"""

python3 core8/pwb.py neq/nldes3 test

python3 core8/pwb.py neq/nldes3 a2r sparql:dfd ask
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



def just_get_ar(labe):
    lab = labe.split("@@")
    tab = []
    # ---
    claimstr = ""
    # ---
    for o in lab:
        test = re.sub(r"[abcdefghijklmnopqrstuvwxyz@]", "", o.lower())
        if test.lower() == o.lower() and o:
            tab.append(o)
    # ---
    if tab != []:
        claimstr = "، و".join(tab)
        printe.output(f"just_get_ar:{claimstr}.")
    # ---
    return claimstr


def main():
    # ---
    sasa = SPARQLSE.get(sparqler[1].strip(), "")
    # ---
    if not sasa:
        printe.output(f"({sparqler[1]}) not in SPARQLSE")
        sasa = """SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = 'ar') } } """ % sparqler[1]
    # ---
    ssqq = [sasa]
    if sparqler[1].strip() == "" or "allkeys" in sys.argv:
        ssqq = [SPARQLSE[x] for x in SPARQLSE.keys()]
        printe.output(f"work in all SPARQLSE.keys() len: {len(ssqq)}")
    # ---
    numg = 0
    # ---
    ssqq = random.sample(ssqq, len(ssqq))
    # ---
    for sparql_query in ssqq:
        # ---
        numg += 1
        # ---
        printe.output("-------------------------")
        printe.output(f"<<lightblue>> query {numg} from {len(ssqq)} :")
        # ---
        if Offq[1] > 0 and Offq[1] > numg:
            continue
        # ---
        pigenerator = wd_sparql_bot.sparql_generator_big_results(sparql_query, offset=Off[1], limit=limit[1])
        # ---
        for totalreads, wd in enumerate(pigenerator, start=1):
            printe.output("<<lightblue>> ============")
            q = wd["item"].split("/entity/")[1]
            printe.output(f"p{totalreads}/{len(pigenerator)} q:{q}")
            # ---
            claimstr = just_get_ar(wd.get("lab", ""))
            # ---
            _, thisone = action_one_item("ar", q, claimstr=claimstr)


if __name__ == "__main__":
    if "test" in sys.argv:
        action_one_item("ar", "Q162210")
    else:
        main()

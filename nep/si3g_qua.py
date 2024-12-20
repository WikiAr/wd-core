#!/usr/bin/python3
"""
tfj run egy --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py nep/si3g_qua returnlab -p27:Q79"

python3 core8/pwb.py nep/si3g_qua returnlab -lang:ar

python3 core8/pwb.py nep/si3g_qua returnlab

python3 core8/pwb.py nep/si3g_qua returnlab ask -p27:Q1028
python3 core8/pwb.py nep/si3g_qua returnlab -p27:Q79

"""
import time
import random
import sys
from newapi import printe

# from nep import si3
from wd_api import wd_bot
from nep.wr_people import work_people
from people.people_get_topic import print_new_jobs, qid_to_p27, qid_to_job

limit = {1: "500"}
P106 = {1: []}
P27 = {1: []}
nolang = {1: "en"}
# ---
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
    if arg.lower() == "lang" and value:
        nolang[1] = value
    # ---
    if arg.lower() == "p106":
        P106[1].append(value)
    # ---
    if arg.lower() == "p27":
        P27[1].append(value)
# ---
if not P106[1]:
    P106[1] = list(set(qid_to_job.keys()))
# ---
if not P27[1]:
    P27[1] = list(set(qid_to_p27.keys()))

# ---
random.shuffle(P106[1])
random.shuffle(P27[1])
# ---


def get_qua():
    # ---
    lang = nolang[1].strip() or "en"
    # ---
    no_lang_line = f'?item schema:description ?{lang} filter (lang(?{lang}) = "{lang}")'
    # ---
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
        #p27
        FILTER NOT EXISTS {#nolang}.
    }

    """
    # ---
    qua = qua.replace("#nolang", no_lang_line, 1)
    # ---
    qua += f"\n limit {limit[1]}"
    # ---
    printe.output(f" len P106 :{len(P106[1])}")
    # ---
    printe.output(f" len P27 :{len(P27[1])}")
    # ---
    if P106[1]:
        line = "values ?p106 {" + " ".join([f"wd:{x}" for x in P106[1]]) + "} \n #sr"
        qua = qua.replace("#sr", line, 1)
    # ---
    # if P27[1]:
    #     line = "values ?p27 {" + " ".join([f"wd:{x}" for x in P27[1]]) + "} \n #sr"
    #     qua = qua.replace("#sr", line, 1)
    # ---
    return qua


def one_item(qid, num):
    # {'item': 'http://www.wikidata.org/entity/Q21457154', 'qid': 'Q21457154'}
    item = wd_bot.Get_Item_API_From_Qid(qid, props="claims|descriptions|labels")
    # ---
    if not item:
        printe.output(f'*<<lightred>> >{num} error with item "{qid}" < :')
        return
    # ---
    descriptions = item.get("descriptions", {})
    endes = descriptions.get("en", "")
    # ---
    ardes = descriptions.get("ar", "")
    # ---
    work_people(item, "", num, ardes)


def main():
    printe.output("*<<lightred>> > main:")
    # ---
    base_qua = get_qua()
    # ---
    # printe.output(f"*<<yellow>> {base_qua} :")
    # ---
    for n, nat_qid in enumerate(P27[1], start=1):
        # ---
        printe.output(f"n:{n}/{len(P27[1])} work:")
        # ---
        line = f"?item wdt:P27 wd:{nat_qid}. # " + qid_to_p27.get(nat_qid, "")
        # ---
        qua = base_qua
        # ---
        qua = qua.replace("#p27", line, 1)
        # ---
        if n == 1:
            print(qua)
        # ---
        lista = wd_bot.sparql_generator_url(qua)
        # ---
        for num, tab in enumerate(lista, start=1):
            qid = tab["qid"]
            # ---
            printe.output(f'*<<lightred>> >{num}/{len(lista)} one_item "{qid}" < :')
            # si3.ISRE(qid, num, len(lista), get_nl_des=False)
            one_item(qid, num)
            # ---
            # sleep one second after 5 items
            if num % 5 == 0:
                time.sleep(1)
    # ---
    print_new_jobs()


if __name__ == "__main__":
    main()

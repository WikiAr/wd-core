#!/usr/bin/python3
"""

tfj run ghu --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py nep/si3g -usercontribs:Ghuron"
tfj run Q482994 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py neq/nldes3 a2r sparql:Q482994"

إضافة وصف لعناصر ويكي بيانات الجديدة

python3 core8/pwb.py nep/si3g -ns:0 -offset:5000 -newpages:10000

python3 core8/pwb.py nep/si3g -newpages:200
python3 core8/pwb.py nep/si3g -newpages:100 ask

python3 core8/pwb.py nep/si3g ask -page:Q21205603
python3 core8/pwb.py nep/si3g ask -page:
python3 core8/pwb.py nep/si3g ask -page:
python3 core8/pwb.py nep/si3g ask -page:
python3 core8/pwb.py nep/si3g -page:Q130212038
python3 core8/pwb.py nep/si3g -page:Q129594209
python3 core8/pwb.py nep/si3g -page:Q112167358
python3 core8/pwb.py nep/si3g -page:Q122652815
python3 core8/pwb.py nep/si3g -page:Q113510544
python3 core8/pwb.py nep/si3g -page:Q111771063
python3 core8/pwb.py nep/si3g -start:Q98512481
python3 core8/pwb.py nep/si3g -start:Q97950000
python3 core8/pwb.py nep/si3g -start:Q97949000
python3 core8/pwb.py nep/si3g -start:Q111771064 err

python3 core8/pwb.py nep/si3g -newpages:200

python pwb.py nep/si3g -newpages:200
python3 core8/pwb.py nep/si3g -newpages:200 ask
# ---
# python3 core8/pwb.py nep/si3g -newpages:50
# python3 core8/pwb.py nep/si3g -newpages:500
# python pwb.py nep/si3g -newpages:100
# python3 core8/pwb.py nep/si3g -limit:3000 -ns:0 -usercontribs:Research_Bot
# python3 core8/pwb.py nep/si3g -limit:6000 -ns:0 -usercontribs:Succu
# python3 core8/pwb.py nep/si3g -limit:6000 -ns:0 -usercontribs:LargeDatasetBot
# python3 core8/pwb.py nep/si3g -limit:6000 -ns:0 -usercontribs:Research_Bot
# ---
"""

#
# (C) Ibrahem Qasim, 2023
#
import sys

# ---
sys.argv.append("-family:wikidata")
sys.argv.append("-lang:wikidata")
# ---
import time
from pathlib import Path

# ---
from newapi import printe
import gent
from nep import si3
from newapi.page import NEW_API

api_new = NEW_API("www", family="wikidata")
api_new.Login_to_wiki()

main_dir1 = f"{str(Path(__file__).parent.parent)}/"

printe.output(f"<<lightyellow>> main_dir1 = {main_dir1}")


def mainwithcat2():
    printe.output("*<<lightred>> > mainwithcat2:")
    # ---
    # python3 core8/pwb.py nep/si3g -newpages:10
    # python3 core8/pwb.py nep/si3g -newpages:1000
    # python3 core8/pwb.py nep/si3g -newpages:20000
    # ---
    start = time.time()
    # ---
    user = ""
    user_limit = 3000
    # ---
    namespaces = "0"
    file = ""
    newpages = ""
    # ---
    lista = []
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg in ["-limit", "limit"]:
            user_limit = value
        # ---
        if arg == "-arfile":
            file = f"dump/ar/{value}.txt"
        elif arg == "-newpages":
            newpages = value
        # ---
        # python3 core8/pwb.py nep/si3g -file:dump/artest/Q7187.txt
        # python3 core8/pwb.py nep/si3g -file:dump/artest/Q1457376.txt
        if arg == "-file":
            file = value
        # ---
        # python3 core8/pwb.py nep/si3g -artest:Q523
        # python3 core8/pwb.py nep/si3g -artest:Q318
        # python3 core8/pwb.py nep/si3g -artest:Q13442814
        # python3 core8/pwb.py nep/si3g -artest:Q21672098
        # python3 core8/pwb.py nep/si3g -artest:Q1516079
        # python3 core8/pwb.py nep/si3g -artest:Q427087
        # python3 core8/pwb.py nep/si3g -artest:Q79007
        # python3 core8/pwb.py nep/si3g -artest:Q7187
        if arg == "-artest":
            file = f"dump/artest/{value}.txt"
        # ---
        if arg == "-page":
            lista.append(value)
        # ---
        # python3 core8/pwb.py nep/si3g -ns:0 -usercontribs:Edoderoobot
        # python3 core8/pwb.py nep/si3g -ns:0 -usercontribs:Ghuron
        if arg in ["-user", "-usercontribs"]:
            user = value
        # ---
        if arg == "-ns":
            namespaces = value
    # ---
    if file:
        if not file.startswith(main_dir1):
            file = main_dir1 + file
        with open(file, "r", encoding="utf-8") as f:
            oco = f.read().split("\n")
        lista = [x.strip() for x in oco if x.strip() != ""]
    # ---
    elif newpages:
        lista = api_new.Get_Newpages(limit=newpages, namespace=namespaces, rcstart="", user="")
    # ---
    elif user:
        lista = api_new.UserContribs(user, limit=user_limit, namespace=namespaces, ucshow="new")
    # ---
    if not lista:
        lista = gent.get_gent(listonly=True)
        # lista = [page.title(as_link=False) for page in genet]
    # ---
    try:
        lena = len(lista)
    except Exception:
        lena = 0
    # ---
    printe.output("*<<lightred>> > mainwithcat2 :")
    # ---
    for num, q in enumerate(lista, start=1):
        si3.ISRE(q, num, lena)
    # ---
    si3.print_new_types()
    # ---
    final = time.time()
    delta = int(final - start)
    # ---
    printe.output(f"si3.py mainwithcat2 done in {delta} seconds")


if __name__ == "__main__":
    mainwithcat2()

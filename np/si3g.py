#!/usr/bin/python
"""

python3 core8/pwb.py np/si3g -usercontribs:Ghuron

إضافة وصف لعناصر ويكي بيانات الجديدة

python3 core8/pwb.py np/si3g -ns:0 -offset:5000 -newpages:10000

python3 core8/pwb.py np/si3g -newpages:200 descqs
python3 core8/pwb.py np/si3g -newpages:100 ask

python3 core8/pwb.py np/si3g -page:Q112167358
python3 core8/pwb.py np/si3g -page:Q122652815
python3 core8/pwb.py np/si3g -page:Q113510544
python3 core8/pwb.py np/si3g -page:Q111771063
python3 core8/pwb.py np/si3g -start:Q98512481
python3 core8/pwb.py np/si3g -start:Q97950000
python3 core8/pwb.py np/si3g -start:Q97949000
python3 core8/pwb.py np/si3g -start:Q111771064 err

python3 core8/pwb.py np/si3g -newpages:200

python pwb.py np/si3g -newpages:200
python3 core8/pwb.py np/si3g -newpages:200 ask

"""
#
# (C) Ibrahem Qasim, 2023
#
import sys
sys.argv.append('-family:wikidata')
sys.argv.append('-lang:wikidata')
# ---
import codecs
import time
from pathlib import Path
# ---
from API import printe
# ---
Dir = Path(__file__).parent
main_dir1 = str(Path(__file__).parent.parent) + '/'
# ---
printe.output(f'<<lightyellow>> main_dir1 = {main_dir1}')
# ---
import gent
# generator = gent.get_gent(*args)
# ---
from newapi.page import NEW_API
# ---
api_new = NEW_API('www', family='wikidata')
login = api_new.Login_to_wiki()
# pages    = api_new.Find_pages_exists_or_not(liste)
# json1    = api_new.post_params(params)
# pages    = api_new.Get_All_pages(start='', namespace="0", limit="max", apfilterredir='', limit_all=0)
# search   = api_new.Search(value, ns="", offset='', srlimit="max", RETURN_dict=False, addparams={})
# newpages = api_new.Get_Newpages(limit="max", namespace="0", rcstart="", user='')
# ---
from np import si3
# ---


def mainwithcat2():
    printe.output('*<<lightred>> > mainwithcat2:')
    # ---
    # python3 core8/pwb.py np/si3g -newpages:10
    # python3 core8/pwb.py np/si3g -newpages:1000
    # python3 core8/pwb.py np/si3g -newpages:20000
    # ---
    start = time.time()
    # ---
    user = ''
    user_limit = 3000
    # ---
    namespaces = '0'
    file = ''
    newpages = ''
    # ---
    lista = []
    # ---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        # ---
        if arg == "-limit" or arg == "limit":
            user_limit = value
        # ---
        if arg == "-newpages":
            newpages = value
        # ---
        # python3 core8/pwb.py np/si3g -arfile:Q7187
        if arg == "-arfile":
            file = f'dump/ar/{value}.txt'
        # ---
        # python3 core8/pwb.py np/si3g -file:dump/artest/Q7187.txt
        # python3 core8/pwb.py np/si3g -file:dump/artest/Q1457376.txt
        if arg == "-file":
            file = value
        # ---
        # python3 core8/pwb.py np/si3g -artest:Q523
        # python3 core8/pwb.py np/si3g -artest:Q318
        # python3 core8/pwb.py np/si3g -artest:Q13442814
        # python3 core8/pwb.py np/si3g -artest:Q21672098
        # python3 core8/pwb.py np/si3g -artest:Q1516079
        # python3 core8/pwb.py np/si3g -artest:Q427087
        # python3 core8/pwb.py np/si3g -artest:Q79007
        # python3 core8/pwb.py np/si3g -artest:Q7187
        if arg == "-artest":
            file = f'dump/artest/{value}.txt'
        # ---
        if arg == '-page':
            lista.append(value)
        # ---
        # python3 core8/pwb.py np/si3g -ns:0 -usercontribs:Edoderoobot
        # python3 core8/pwb.py np/si3g -ns:0 -usercontribs:Ghuron
        if arg == "-user" or arg == "-usercontribs":
            user = value
        # ---
        if arg == "-ns":
            namespaces = value
    # ---
    if file != "":
        if not file.startswith(main_dir1):
            file = main_dir1 + file
        oco = codecs.open(file, "r", encoding="utf-8").read().split('\n')
        lista = [x.strip() for x in oco if x.strip() != '']
    # ---
    elif newpages != "":
        lista = api_new.Get_Newpages(limit=newpages, namespace=namespaces, rcstart="", user='')
    # ---
    elif user != "":
        lista = api_new.UserContribs(user, limit=user_limit, namespace=namespaces, ucshow="new")
    # ---
    if lista == []:
        genet = gent.get_gent()
        lista = [page.title(as_link=False) for page in genet]
    # ---
    # ---
    num = 0
    printe.output('*<<lightred>> > mainwithcat2 :')
    for q in lista:
        num += 1
        si3.ISRE(q, num, len(lista))
    # ---
    si3.print_new_types()
    # ---
    final = time.time()
    delta = int(final - start)
    # ---
    printe.output(f'si3.py mainwithcat2 done in {delta} seconds')


# ---
if __name__ == "__main__":
    mainwithcat2()
# ---
# python3 core8/pwb.py np/si3g -newpages:50
# python3 core8/pwb.py np/si3g -newpages:500
# python pwb.py np/si3g -newpages:100
# python3 core8/pwb.py np/si3g -limit:3000 -ns:0 -usercontribs:Research_Bot
# python3 core8/pwb.py np/si3g -limit:6000 -ns:0 -usercontribs:Succu
# python3 core8/pwb.py np/si3g -limit:6000 -ns:0 -usercontribs:LargeDatasetBot
# python3 core8/pwb.py np/si3g -limit:6000 -ns:0 -usercontribs:Research_Bot
# ---

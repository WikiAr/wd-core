#!/usr/bin/python3
"""
إضافة وصف لعناصر ويكي بيانات الجديدة
"""

import logging
import sys
import time
from pathlib import Path

from shared.api_page import load_main_api

from nep import si3
from wd_core import wd_gent

logger = logging.getLogger(__name__)

sys.argv.append("-family:wikidata")
sys.argv.append("-lang:wikidata")

main_dir1 = f"{str(Path(__file__).parent.parent)}/"

logger.info(f"<<lightyellow>> main_dir1 = {main_dir1}")


def mainwithcat2() -> None:
    logger.info("*<<lightred>> > mainwithcat2:")
    # ---
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
        if arg == "-file":
            file = value
        # ---
        if arg == "-artest":
            file = f"dump/artest/{value}.txt"
        # ---
        if arg == "-page":
            lista.append(value)
        # ---
        if arg in ["-user", "-usercontribs"]:
            user = value
        # ---
        if arg == "-ns":
            namespaces = value
    # ---
    api = load_main_api("www", "wikidata")
    api_new = api.NewApi()
    # ---
    if file:
        if not file.startswith(main_dir1):
            file = main_dir1 + file
        with open(file, "r", encoding="utf-8") as f:
            oco = f.read().split("\n")
        lista = [x.strip() for x in oco if x.strip() != ""]
    # ---
    elif newpages:
        lista = api_new.Get_Newpages(limit=newpages, namespace=namespaces, offset_minutes=20)
    # ---
    elif user:
        lista = api_new.UserContribs(user, limit=user_limit, namespace=namespaces, ucshow="new")
    # ---
    if not lista:
        lista = wd_gent.get_gent_list()
        # lista = [page.title(as_link=False) for page in genet]
    # ---
    try:
        lena = len(lista)
    except Exception:
        lena = 0
    # ---
    logger.info("*<<lightred>> > mainwithcat2 :")
    # ---
    for num, q in enumerate(lista, start=1):
        si3.ISRE(q, num, lena)
    # ---
    si3.print_new_types()
    # ---
    final = time.time()
    delta = int(final - start)
    # ---
    logger.info(f"si3.py mainwithcat2 done in {delta} seconds")


if __name__ == "__main__":
    mainwithcat2()

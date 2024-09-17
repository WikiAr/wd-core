#!/usr/bin/python3
# --
#!/usr/bin/python3
# -*- coding: utf-8 -*-
# ---
"""
python pwb.py cy/jsub -page:كريس_فروم
python pwb.py cy/jsub -ref:قالب:نتيجة_سباق_الدراجات/بداية
python3 core8/pwb.py cy/jsub -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات

https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Gathering_data_from_Arabic-Wikipedia

"""
# ---
#
# (C) Ibrahem Qasim, 2022
#
# ---

import pywikibot

# ---
from cy.cy5 import *

# ---
import gent




def main2(*args):
    generator = gent.get_gent(listonly=True, *args)
    for numb, pagetitle in enumerate(generator, start=1):
        pywikibot.output(f"page: {numb} : {pagetitle}")
        StartOnePage(pagetitle)


# ---
if __name__ == "__main__":
    main2()
# ---

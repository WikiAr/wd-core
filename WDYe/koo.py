#!/usr/bin/python3
"""

python pwb.py wd/koo -page:مارك_فان_بوميل

python3 core8/pwb.py wd/koo -ns:0 -ref:قالب:كووورة

"""
#
# (C) Ibrahem Qasim, 2022
#
from wd_api import himoAPI_test as himoAPI
from API import himoBOT2

import pywikibot
# ---
import gent
# generator = gent.get_gent(*args)
# ---
#

from pywikibot import textlib

# ---
# ---

done = []


def woo(page):
    # ---
    title = page.title(as_link=False)
    text = page.text
    templates = textlib.extract_templates_and_params(text, True, True)
    # ---
    id = ''
    info = himoBOT2.Get_page_info_from_wikipedia("ar", title)
    qid = info.get("q", "")
    # ---
    for x, y in templates:
        if x.strip() == "كووورة":
            for key in sorted(y):
                if key == "1":
                    id = y[key]
    # ---
    pywikibot.output(f"koora id:{id}")
    # ---
    P31 = himoBOT2.Get_Claim_API(qid, "P31")
    iin = himoBOT2.Get_Property_API(qid, "P8021", titles=title, sites="arwiki")
    # pywikibot.output( "iin:%s" % iin )
    # ---
    pywikibot.output(f"P31:{P31}")
    # ---
    if P31 != "Q5":
        return ''
    # else:
    # pywikibot.output( "P31:%s" % P31 )
    # ---
    if not iin and id not in done:
        himoAPI.Claim_API_string(qid, "P8021", id)
        done.append(id)
        # pywikibot.output( f )


def main(*args):
    generator = gent.get_gent(*args)

    for page in generator:
        woo(page)


# ---
if __name__ == "__main__":
    main()
# ---

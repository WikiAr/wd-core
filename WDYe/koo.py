#!/usr/bin/python3
"""

python pwb.py wd/koo -page:مارك_فان_بوميل

python3 core8/pwb.py wd/koo -ns:0 -ref:قالب:كووورة

"""
#
# (C) Ibrahem Qasim, 2022
#
from himo_api import himoAPI_test as himoAPI
from API import himoBOT2
from wd_api import wd_bot
import pywikibot

# ---
import gent


# ---
#

from pywikibot import textlib

# ---
# ---

done = []


def woo(page):
    # ---
    title = page.title(as_link=False)
    # ---
    text = himoBOT2.GetarPageText(title, sitecode="ar") #from API import himoBOT2
    # ---
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
    P31 = wd_bot.Get_Claim_API(q=qid, p="P31")
    iin = wd_bot.Get_Property_API(q=qid, p="P8021", titles=title, sites="arwiki")
    # pywikibot.output(f"iin:{iin}")
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
    generator = gent.get_gent(listonly=False, *args)

    for page in generator:
        woo(page)


# ---
if __name__ == "__main__":
    main()
# ---

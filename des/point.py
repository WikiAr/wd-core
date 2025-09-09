#!/usr/bin/python3
"""


تسمية  عناصر ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import re
import sys
from newapi import printe
from wd_api import wd_bot
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="bot", www="www")
# ---

# ---
bylangs = False  # False#True
# ---
limits = {1: "1000"}
# ---
items_done = []


def action(json1):
    try:
        total = len(json1)
    except BaseException:
        total = 0
    c = 1
    # ---
    for tab in json1:  # عنصر ويكي بيانات
        printe.output(tab)
        q = tab["item_q"]
        if q not in items_done:
            c += 1
            printe.output(f'action {c}/{total} "{q}"')
            label = tab["label"]
            # ---
            # year =  re.match(r'(\d\d\d\d)', label)
            year = re.sub(r".*(\d+\d+\d+\d+).*", r"\g<1>", label)
            # ---
            if year == label:
                year = ""
            # ---
            if year:
                year1 = year  # .group(1)
                timestr = f"+{year1}-00-00T00:00:00Z"
                # ---
                PP_time = ""
                PP = wd_bot.Get_Property_API(q=q, p="P585")
                if PP and PP[0] and PP[0]["time"]:
                    PP_time = PP[0]["time"]
                    printe.output(f"  * PP:\"{PP[0]['time']}\"")
                # ---
                printe.output(f'  * year1:"{year1}"')
                if PP_time != timestr:
                    WD_API_Bot.Claim_API_time(q, "P585", precision=9, year=year1, strtime=timestr)
                else:
                    printe.output(f" <<lightred>> * time == timestr.{timestr} ")
        else:
            printe.output(" <<lightred>> * q in items_done. " % q)


# ---
Quarry = {
    "y":
        """
SELECT (concat(strafter(str(?item),"/entity/"))  as ?item_q)
 ?label WHERE {
    ?item wdt:P31 ?pp.
    ?pp wdt:P31* wd:Q15275719.
    #OPTIONAL {?item wdt:P641/wdt:P279 wd:Q2215841. }
    #?item wdt:P641/wdt:P279 wd:Q2215841.
    FILTER NOT EXISTS { ?item wdt:P585 ?P585. }
    FILTER NOT EXISTS { ?item wdt:P580 ?P580. }
    #?item rdfs:label ?l . FILTER( REGEX(?l, "(1[89]\u007C20)\\d\\d") )
    ?item rdfs:label ?label . FILTER( REGEX(?label, "(\\d\\d\\d\\d)") )
    #%s
    #?item rdfs:label ?l . FILTER(lang(?l) = "en" && REGEX(?l, "(1[89]\u007C20)\\d\\d") )
}
#LIMIT 2
"""
}


def main():
    # ---
    # python pwb.py des/point -limit:2
    # ---
    taxose = ""
    qya = {}
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg == "-limit":
            printe.output(f"<<lightred>>>>  limit ( {value} )  ")
            limits[1] = value
        # ---
        if arg in Quarry:
            printe.output(f"<<lightred>>>>  use Quarry:{arg} . ")
            qya[arg] = Quarry[arg]
    # ---
    if not qya:
        qya = Quarry
    for number, (key, quuu) in enumerate(qya.items(), start=1):
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            # ---
            if arg in ["P31", "-P31"]:
                printe.output(f"<<lightred>>>>  P31:{value}. ")
                taxose = f"?item wdt:P31/wdt:P279* wd:{value}."
            # ---
            if arg in ["lang", "-lang"]:
                if value == "fr":
                    quuu = quuu.replace('"en"', '"fr"')
                    quuu = quuu.replace('"Category:"', '"Catégorie:"')
                    printe.output("<<lightred>>>> change lang to france. ")
        # ---
        quuu = quuu % taxose
        # ---
        if limits[1]:
            quuu = f"{quuu}\n LIMIT {limits[1]}"
        # ---
        printe.output(f"quuu : {number}/{len(qya)} key:{key}")
        printe.output(quuu)
        # ---
        json1 = wd_bot.sparql_generator_url(quuu)
        action(json1)


# ---
if __name__ == "__main__":
    main()
# ---

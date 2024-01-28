"""

"""

import sys
from pathlib import Path
import pywikibot

# ---
from nep.si3 import (
    Qids_translate,
    space_list_and_other,
    others_list,
    others_list_2,
    Geo_List,
)
from nep import read_json

# ---
Dir = Path(__file__).parent


def read_new_types_file():
    # ---
    # python3 core8/pwb.py nep/si3 read
    # python3 core8/pwb.py nep/si3 read -file:nep/new_types11.json
    # python3 core8/pwb.py nep/si3 read -number:500
    # ---
    file = "tables/new_types.json"
    number = 100
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg in ["-number", "number"]:
            number = int(value)
        if arg in ["-file", "file"]:
            file = value
    # ---
    wd_file = {}
    jsonfile = Dir / file
    # ---
    # space_list_and_other
    # ---
    Known = ["Q5", "Q16521"]
    # ---
    # with codecs.open(jsonfile, "r", encoding="utf-8-sig") as listt:
    # wd_file = json.load(listt)
    # ---
    wd_file = read_json.read_bad_json(jsonfile)
    # wd_file.keys()
    # ---
    PP = [[leen, gf] for gf, leen in wd_file.items()]
    PP.sort(reverse=True)
    # ---Geo_List
    pywikibot.output("===================")
    for yy, xh in PP:
        if (
            yy > number
            and xh not in Qids_translate.keys()
            and xh not in Known
            and xh not in space_list_and_other
            and xh not in others_list
            and xh not in others_list_2
            and xh not in Geo_List
        ):
            # pywikibot.output( '* %d\t \t{{Q|%s}}' % (yy, xh) )
            pywikibot.output(
                "*'%s':{'ar':'{{#invoke:Wikidata2|labelIn|ar|%s}}', 'en':'{{#invoke:Wikidata2|labelIn|en|%s}}' }, # %d"
                % (xh, xh, xh, yy)
            )
    pywikibot.output("===================")
    # ---
    print("done")


# ---
# python3 core8/pwb.py nep/read_np
# ---
if __name__ == "__main__":
    read_new_types_file()

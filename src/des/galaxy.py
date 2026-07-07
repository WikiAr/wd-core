#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
#
"""


python pwb.py des/galaxy

"""


from bots_subs.wd_api import newdesc
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions

# newdesc.mainfromQuarry2( topic , Quarry, translations)

translations = {"Q318": DescraptionsTable.get("galaxy") or Qid_Descraptions.get("Q318") or {}}

for q in translations:
    quarry = f"SELECT ?item WHERE {{ ?item wdt:P31 wd:{q}.}} limit 50000"
    newdesc.mainfromQuarry2(q, quarry, translations)

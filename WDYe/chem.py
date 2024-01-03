"""
#  python pwb.py wd/wikinews
"""

from wd_api import newdesc

# ---
from desc_dicts.descraptions import Qid_Descraptions

# ---
QS = {"Q11173": Qid_Descraptions["Q11173"]}
# ---
for q in QS:
    en = QS[q]["en"]
    quarry = 'SELECT DISTINCT ?item WHERE { '
    quarry = f'?item wdt:P31 wd:{q}. ?item schema:description "{en}"@en . '
    quarry += '} limit 10000'
    newdesc.mainfromQuarry2(q, quarry, QS)
# ---

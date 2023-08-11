"""
#  python pwb.py wd/wikinews
"""
from wd_API import newdesc
# ---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions
# ---
QS = {}
# QS["Q6979593"] = Qid_Descraptions["Q6979593"]    national association football team
QS["Q11173"] = Qid_Descraptions["Q11173"]  # chemical compound
# ---
for q in QS:
    en = QS[q]["en"]
    quarry  = 'SELECT DISTINCT ?item WHERE { '
    quarry  = f'?item wdt:P31 wd:{q}. ?item schema:description "{en}"@en . '
    quarry += '} limit 10000'
    newdesc.mainfromQuarry2(q, quarry, QS)
# ---

#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة تسميات مواضيع طبية

"""
#
# (C) Ibrahem Qasim, 2022
#
#


import re
import time
import pywikibot
# ---
import sys
# ---
import urllib
import urllib.request
import urllib.parse
# ---
from API import himoBOT2
from wd_API import himoAPI_test as himoAPI
# ---
SaveR = {1: False}
# ---
main_table = {}
main_table["Q4167836"] = {
    "كرواتيون": "كروات",
    "يهوديون": "يهود",
    "أرمنيون": "أرمن",
    "أفغانيون": "أفغان",
}
# ---
main_table["Q5"] = {
    "جلاسر": "غلاسر",
}
# ---
allise = {}
qid_table = {}
# ---
for qid in main_table:
    for lab in main_table[qid]:
        # ---
        labe = main_table[qid][lab]
        # ---
        allise[lab] = labe
        allise[labe] = lab
        # ---
        qid_table[lab] = qid
        qid_table[labe] = qid
# ---


def WORK(item, table, type):
    # pywikibot.output( item )
    pywikibot.output(table)
    # pywikibot.output( '<<lightgreen>> item:"%s" ' % item )
    # ---
    arlab = table["label"][0]
    arlab2 = arlab
    alias = table["alias"]
    if type in allise:
        pywikibot.output('<<lightgreen>> type:"%s" in allise:"%s" ' %
                         (type,  allise[type]))
        arlab2 = re.sub(r"^%s " % type, allise[type] + " ", arlab2)
        arlab2 = re.sub(r" %s " % type, " " + allise[type] + " ", arlab2)
    # ---
    if arlab2 != arlab:
        pywikibot.output("arlab2 : %s" % arlab2)
        if SaveR[1]:
            himoAPI.Alias_API(item, [arlab2], "ar", False)
        else:
            sa = pywikibot.input(
                '<<lightyellow>>himoAPI: Add Alias ([y]es, [N]o, [a]ll): for item %s' % item)
            if sa == 'y' or sa == 'a' or sa == '':
                himoAPI.Alias_API(item, [arlab2], "ar", False)
            else:
                pywikibot.output(' himoAPI: wrong answer')


    # ---
Limit = {1: "10"}
# ---
Quaa = '''SELECT ?item ?label ?alias
    WHERE
    {
      #?item wdt:P31 wd:Q4167836. 
      ?item wdt:P31 wd:%s. 
      ?item rdfs:label ?label.
      OPTIONAL { ?item skos:altLabel ?alias FILTER (LANG (?alias) = "ar") }
      FILTER(LANG(?label) = "ar").
      FILTER(CONTAINS(?label, "%s")).
    }
    LIMIT '''
# ---


def WORK_table(qid, tables):
    # qid = qid_table.get( peo , "" )
    for peo in tables:
        qua = Quaa % (qid, peo)
        qua = qua + Limit[1]
        # pywikibot.output( qua )
        sparql = himoBOT2.sparql_generator_url(qua, printq=True)
        # pywikibot.output( sparql )
        # ---
        Table = {}
        for item in sparql:
            q = item['item'].split("/entity/")[1]
            if not q in Table:
                Table[q] = {}
            for tab in item:
                if not tab in Table[q]:
                    Table[q][tab] = []
                if tab != 'item':
                    Table[q][tab].append(item[tab])
        # ---
        num = 0
        for item in Table:
            num += 1
            # if num < 2:
            pywikibot.output('<<lightgreen>> %d/%d item:"%s" ' %
                             (num, len(Table.keys()), item))
            # item['item'] = item['item'].split("/entity/")[1]
            WORK(item, Table[item], peo)
# ---


def main():
    # python pwb.py wd/med mainkey subcats
    # python pwb.py wd/med short subcats
    # python pwb.py wd/med subcats ta:horror
    # python pwb.py wd/med qs:Q5
    # ---
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # pp , qq = "P105" , "Q35409"
    # ---
    table_new = main_table
    val = ""
    val2 = ""
    qnew = ""
    # ---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        # ---#Depth[1]
        if arg == "p":
            val = value
        # ---
        if arg == "q":
            qnew = value
        # ---
        if arg == 'always':
            SaveR[1] = True
            pywikibot.output('<<lightred>> SaveR = True.')
        # ---#limit[1]
        if arg == '-limit' or arg == 'limit':
            Limit[1] = value
            pywikibot.output('<<lightred>> Limit = %s.' % value)
    # ---
    if val != "":
        val2 = allise.get(val, "")
        if qnew == "":
            qnew = qid_table.get(val, "")
    # ---
    if val2 != "" and qnew != "":
        table_new = {}
        table_new[qnew] = {val: val2}
    # ---
    num_peo = 0
    for qid in table_new:
        num_peo += 1
        pywikibot.output('<<lightblue>> %d/%d peo:"%s" ' %
                         (num_peo, len(table_new.keys()), qid))
        WORK_table(qid, table_new[qid])

        # ---
if __name__ == "__main__":
    main()
# ---

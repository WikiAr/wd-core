#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python3 pwb.py dump/arn
python3 pwb.py dump/arn test -off:20000 -done2limit:5000
python3 pwb.py dump/arn test nosave
python3 pwb.py dump/arn test printline
python3 pwb.py dump/arn test limit:5000000 -done2limit:200000
انشاء ملفات dump/ar/%s.txt
"""
#
# (C) Ibrahem Qasim, 2017
#
#
import sys
import os
import bz2
# import gz
import json
import time
import pywikibot
title = u'ويكيبيديا:مشروع_ويكي_بيانات/تقرير_P31/1'
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
if not Dump_Dir.endswith('/'):
    Dump_Dir += '/'
print(f'Dump_Dir: {Dump_Dir}')
Table_no_ab2 = {}
Table_no_ar_lab = {}
done2limit = {1: 500000, 2: 0}
Offset = {1: 0}
Limit = {1: 500000000}

for arg in sys.argv:
    arg, sep, value = arg.partition(u':')
    if arg.startswith('-'):
        arg = arg[1:]
    if arg == u"test":
        done2limit[1] = 15000
        Limit[1] = 15000
    if arg == "done2limit":
        done2limit[2] = int(value)
    if arg == "offset" or arg == "off":
        Offset[1] = int(value)
    if arg == "limit":
        Limit[1] = int(value)
if done2limit[2] != 0:
    done2limit[1] = done2limit[2]


def log_dump():
    hhh = 1000
    file_l = u'ar/%s.txt'
    if 'test' in sys.argv:
        file_l = u'artest/%s.txt'
        hhh = 100
    file_l = Dump_Dir + file_l
    pywikibot.output(f'file_l: {file_l}')
    pywikibot.output('len of Table_no_ab2 : %d' % len(Table_no_ab2))
    for qid, List in Table_no_ab2.items():
        if len(List) > hhh:
            fille = file_l % qid
            oldtext = []
            try:
                listo = codecs.open(fille, u"r", encoding="utf-8").read().split('\n')
                oldtext = [x.strip() for x in listo.split('\n') if x.strip() != '']
            except:
                oldtext = []
            Listn = [o for o in List if not o in oldtext]
            newtex = "\n".join(Listn)
            pywikibot.output('write %d line to file:%s' % (len(Listn), fille))
            with open(fille, 'w') as f:
                f.write(newtex)
            Table_no_ab2[qid] = []


def mainr():
    start = time.time()
    t1 = time.time()
    no_claims = 0
    done2 = 0
    c = 0
    dumpdate = 'latest'
    filename = '/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2'
    if not os.path.isfile(filename):
        pywikibot.output(f'file {filename} <<lightred>> not found')
        return
    f = bz2.open(filename, 'r')
    others = 0
    for line in f:
        line = line.decode('utf-8')
        line = line.strip('\n').strip(',')
        c += 1
        if c < Limit[1]:
            if c > Offset[1]:
                if line.startswith('{') and line.endswith('}'):
                    done2 += 1
                    if "printline" in sys.argv and (c % 1000 == 0 or c == 1):
                        pywikibot.output(line)
                    json1 = json.loads(line)
                    q = json1.get('id', '')
                    ar_desc = json1.get('descriptions', {}).get('ar', False)
                    if not ar_desc:
                        for x in json1.get('claims', {}).get('P31', []):
                            p31d = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id')
                            if p31d in Table_no_ab2:
                                if not q in Table_no_ab2[p31d]:
                                    Table_no_ab2[p31d].append(q)
                            else:
                                Table_no_ab2[p31d] = [q]
                if c % 1000 == 0:
                    dii = time.time()-t1
                    pywikibot.output('c:%d, time:%d' % (c, dii))
                    t1 = time.time()
            else:
                if c % 1000 == 0:
                    dii = time.time()-t1
                    pywikibot.output('Offset c:%d, time:%d' % (c, dii))
                    t1 = time.time()
            if done2 == done2limit[1]:
                done2 = 1
                log_dump()
        else:
            break
    log_dump()


if __name__ == '__main__':
    mainr()

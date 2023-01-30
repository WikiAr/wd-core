#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف لعناصر ويكي بيانات الجديدة

python pwb.py np/si -lang:wikidata -family:wikidata -newpages:1000


"""
#
# (C) Ibrahem Qasim, 2022
#
import json
import codecs
from API.maindir import main_dir
if main_dir == "I:/core/master/": main_dir = "I:/core/core-yemen/"
from API import printe
#---
MainTestTable = {1 : True}
#---
dump = {}
dump['new'] = []
done_list = {}
jsonfile = main_dir + 'np/done.json'
#with open(jsonfile) as listt:
with codecs.open(jsonfile, "r", encoding="utf-8-sig") as listt:
    #try:
        done_list = json.load(listt)
        printe.output( 'find %d items in done list.' % len(done_list["done"]) )
#---
def dump_json_write():
    printe.output( 'dump_json_write Adding %d items: '  % len(dump['new']) )
    with open(jsonfile, 'w') as outfile:
        json.dump(done_list, outfile)
    dump['new'] = []
#---
def done_list_append(item):
    done_list["done"].append(item)
    dump['new'].append(item)
    #printe.output( 'Add %s to done_list.' % item )
#---
def ISRE( item , num , lenth ):
    #---
    #printe.output( '*<<lightred>> >%d/%d ISREISRE "%s" :' % ( num , lenth , item ) )
    #for nn in range(1,1000):
        #if num == nn * 10:
             #dump_json_write()  
    caos = [x * 20 for x in range(1,1000)]
    if num in caos:
         printe.output( '*<<lightred>> >%d/%d ISREISRE "%s" :' % ( num , lenth , item ) )
         dump_json_write()
         
    done_list_append(item)
#---
def FindItem(q):
    if not q in done_list["done"]:
        #try:
            return q
        #except:
            #return False
            #pass
        #return False
                #yield wditem
    else:
        printe.output( '*<<lightred>> item "%s" already in done.json.' % q)
#---
MainTest = True#False#True
def Main_Test():
    printe.output( '<<lightyellow>> Main_Test :')
    num = 0
    qua = range(1,1000)# [ 'Q38236869','Q700','Q300','Q500' ]
    for page in qua:
        item = FindItem('Q%d' % page)
        num += 1
        #---python pwb.py np/d2 33200000
        if item:
            ISRE(item , num, len(qua))
    #dumpjson()    
#---
if __name__ == "__main__":
    Main_Test()
#---
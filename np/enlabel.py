#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python3 pwb.py np/enlabel -lang:wikidata -family:wikidata -newpages:200

python3 pwb.py np/enlabel main2 -newpages:20

python3 pwb.py np/enlabel -family:wikidata -lang:wikidata -usercontribs:Mr._Ibrahem

python3 pwb.py np/enlabel main2 -usercontribs:Michgrig -limit:50

"""
#
# (C) Ibrahem Qasim, 2022
#
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title, arsite.encoding() )
#---
from API import printe
import sys
#---
sys_argv = sys.argv or []
#---
# start of himoBOT2.py file
from API import himoBOT2
#---
# start of himoBOT3.py file
from API import himoBOT3 as himoBOT3wd
himoBOT3wd.log('https://' + 'www.wikidata.org/w/api.php')
# himoBOT3wd.Get_Newpages( sitecode, family, limit = "max", namespace = "0" )
#---
# himoBOT3wd.Get_Newpages( sitecode, family, limit = "max", namespace = "0" )
# himoBOT3wd.Get_UserContribs( user, limit = "max", namespace = "*", ucshow = "" )
#---
from API.ru_st_2_latin import make_en_label
# enlabel = make_en_label(labels, q, Add=False)
#---
def ISRE( q, num, lenth ):
    #---
    printe.output( '-------------------------------------------\n*<<lightyellow>> >%d/%d q:"%s" :' % ( num, lenth, q ) )
    #---
    item = himoBOT2.Get_Item_API_From_Qid( q, sites = "", titles = "", props = "labels" )#claims
    if item:
        #---
        labels = item.get("labels", {})
        if labels.get("en","") == "":
            printe.output("item enlabel == ''")
            make_en_label(labels, q, Add=True)
#---
def mainwithcat(*args):
    printe.output( '*<<lightred>> > mainwithcat:')
    generator = gent.get_gent(*args)
    #---
    counter = 0
    for page in generator:
        counter += 1
        q = page.title(as_link=False)
        ISRE( q, counter, 500 )
    #---
def main2():
    printe.output( '*<<lightred>> > main2:')
    #---
    user = ''
    user_limit = '3000'
    #---
    namespaces = '0'
    newpages = ''
    #---
    list = []
    #---
    for arg in sys_argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == "-limit" or arg == "limit" : 
            user_limit = value
        #---
        if arg == "-newpages" : 
            newpages = value
        #---
        if arg == '-page': list.append(value)
        #---
        # python3 pwb.py np/si3 main2 -ns:0 -usercontribs:Ghuron
        if arg == "-user" or arg == "-usercontribs" : 
            user = value
        #---
        if arg == "-ns" : 
            namespaces = value
    #---
    if newpages != "":
        list = himoBOT3wd.Get_Newpages( "www", "wikidata", limit = newpages, namespace = namespaces )
    #---
    elif user != "":
        list = himoBOT3wd.Get_UserContribs( user, limit = user_limit, namespace = namespaces, ucshow = "new" )
    #---
    num = 0
    printe.output( '*<<lightred>> > main2 :')
    for q in list:
        num += 1
        ISRE( q, num, len(list) ) 
    #---
# python3 pwb.py np/si3 read
#---
if __name__ == "__main__":
    if "main2" in sys_argv:
        main2()
    else:
        mainwithcat()
#---
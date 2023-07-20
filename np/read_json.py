#!/usr/bin/python

"""


"""
#
# (C) Ibrahem Qasim, 2023
#
#

import json as JJson
import re
import time
import codecs
from warnings import warn
from datetime import datetime
#---
from API import printe
#---
try:
    import pywikibot
except:
    pywikibot = False
#---
import sys

#---
import urllib
import urllib.request
import urllib.parse
#---
def printo(s):
    if pywikibot:
        pywikibot.output(s)
    else:
        printe.output(s)
#---
def read_bad_list(file):
    try:
        List = []
        with open(file, "r") as listt:
            done_list7 = JJson.load(listt)
            listt.close()
        #---
        for type in done_list7:
            printe.output( 'find %d cats in done_list7. "%s" , file:"%s"' % (len(done_list7[type]) , type , file) )
            for catee in done_list7[type]:
                catee = catee.strip()
                catee = re.sub(r'"', "" , catee)
                if not catee in List:
                    List.append(catee)
        print('Good JJson "%s"' % file )
        return List
    except Exception as e:
        pywikibot.output( '<<lightred>> Traceback (most recent call last):' )
        warn('Exception:' + str(e), UserWarning)
        pywikibot.output( 'CRITICAL:' )
        #---
        List = []
        with open(file, "r") as listt:
            list2 = listt.read()
            listt.close()
        #---
        listo = list2.split("[")[1].split("]")[0]
        listo = listo.split(",")
        for catee in listo:
            catee = catee.strip()
            catee = re.sub(r'"', "" , catee)
            if not catee in List:
                List.append(catee)
        print('Bad JJson "%s"' % file )
        return List
    #---
    return False
#---
def read_bad_json(file):
    try:
        with open(file, "r") as listt:
            done_list7 = JJson.load(listt)
            listt.close()
        #---
        print('Good JJson "%s"' % file )
        return done_list7
        '''for type in done_list7:
            printe.output( 'find %d cats in done_list7. "%s"' % (len(done_list7[type])  , type) )
            for catee in done_list7[type]:
                catee = catee.strip()
                catee = re.sub(r'"', "" , catee)
                if not catt in List:
                    List.append(catee)'''
    except Exception as e:
        pywikibot.output( '<<lightred>> Traceback (most recent call last):' )
        warn('Exception:' + str(e), UserWarning)
        pywikibot.output( 'CRITICAL:' )
        lala = {}
        with codecs.open(file, "r", encoding="utf-8-sig") as listt2:
            lala = listt2.read()
            listt2.close()
        #---
        fa = str(lala)
        fa = fa.split("{")[1].split("}")[0]
        fa = "{" + fa + "}"
        wd_file = JJson.loads(fa)
        print('Bad JJson "%s"' % file )
        return wd_file
    #---
    return {}
#---
def main(file , Type):
    try:
        if Type == "dict":
            return read_bad_json(file)
        elif Type == "list":
            return read_bad_list(file)
        else:
            print("* unknow type :%s"  % Type)
    except Exception as e:
        pywikibot.output( '<<lightred>> Traceback (most recent call last):' )
        pywikibot.output('* Cant work file:"%s" , Type:"%s"'  % (file , Type ) )
        warn('Exception:' + str(e), UserWarning)
        pywikibot.output( 'CRITICAL:' )
    return False
#---
if __name__ == "__main__":
    main("{}" , "dict")
#---
#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python3 pwb.py np/cs mainwithcat2 -ns:0 -usercontribs:JAnDbot
 
"""
#
# (C) Ibrahem Qasim, 2022
#
import json
import time
from datetime import datetime
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
from API import printe
import sys
#---
sys_argv = sys.argv or []
#---
from API import himoAPI
from API import himoBOT2
from API import himoBOT3 as himoBOT3wd
himoBOT3wd.log('https://' + 'www.wikidata.org/w/api.php')
#---
#---
#from trans import *  
from API.descraptions import DescraptionsTable, Qid_Descraptions
#---
Tras = {
    # 'Q4167836': DescraptionsTable['Wikimedia category'],
    'Q4167836': DescraptionsTable.get('Wikimedia category') or Qid_Descraptions.get('Q4167836') or {}
    }
#---
MainTestTable = {1 : False}
#--- 
def wwdesc( NewDesc , q , i, fixlang , ask = ""):
    printe.output('* cs.py wwdesc "%s" try number:"%d" :' % ( str(q) , i )  )
    queries_list = []
    for x in NewDesc.keys():
        if not x in fixlang:
            queries_list.append(x)
    queries_list.sort()
    #---
    data = { 'descriptions' : NewDesc }
    data3 = json.JSONEncoder().encode( data )
    #---
    dlangs = ','.join(queries_list)
    #summary = ('Bot: - Add descriptions:(%d langs) %s' % ( len(queries_list), str(dlangs) )) #ملخص العمل
    summary = 'Bot: '
    if queries_list:
        summary = summary + '- Add descriptions:(%d langs).' % ( len(queries_list) )
        #summary = summary + ' - /* wbsetdescription-add:%d|%s */ %s.' % ( len(queries_list) , deso , simple )
    #---
    if fixlang:
        for ii in fixlang:
            if not ii in NewDesc.keys():
                fixlang.remove(str(ii))
                printe.output('remove "%s" from fixlang because it\'s not in NewDesc'  % ii )
        fixed = ','.join(fixlang)
        summary = summary + ('- fix descriptions:(%d: %s).' % (len(fixlang) , str(fixed)) ) #ملخص العمل
    printe.output(summary)
    #---
    skipplang = []
    if queries_list != [] or fixlang != []:
        value = ''
        if 'ar' in NewDesc:
            value = NewDesc['ar']["value"]
        else:
            if queries_list:
                try:
                    key = queries_list[1]
                    value = NewDesc[key]["value"] + '@%s' % key
                except:
                    value = ''
        #---
        printe.output('*work_api_desc %s "%s": try "%d",%s:' % ( str(q) , value  , i , menet )  )
        #---
        if 'printdisc' in sys_argv:
            printe.output( data3 )
        #---
        #item.editEntity(data, summary=summary)
        skipp = himoAPI.New_Mult_Des_2(q, data3, summary , True, ask = ask)
        if 'success' in skipp:
            #printe.output(summary)
            printe.output('<<lightgreen>> **%s true. %s' % (q, summary) )
            False , NewDesc
        elif ('using the same description text' in skipp) and ('associated with language code' in skipp):
            skipp = skipp.split('using the same description text')[0].split('associated with language code')[1]
            skipplang = skipp.strip().split(',')
            #---
            NewDesc2 = NewDesc
            if len(skipplang) != 0:
                printe.output( 'skiping languages: "%s"' % str(skipplang) )
                #printe.output(keys)
                for lango in skipplang :
                    if lango != '':
                        del NewDesc2[lango]
            #---
            i += 1
            printe.output("<<lightred>> try %d again with remove skipplang "  % i )
            wwdesc( NewDesc2 , q , i, fixlang, ask = ask)
            #return True , NewDesc2
            #---
        elif 'wikibase-api-invalid-json' in skipp :
            printe.output('<<lightred>> - "wikibase-api-invalid-json" ')
            printe.output(NewDesc)
        else:
            printe.output(skipp)
            #return False , NewDesc
            #return False , NewDesc
    else:
        printe.output( '  *** no addedlangs')
#---
def work_api_desc( NewDesc , q , fixlang ):
    #---
    g = ''
    #---
    if not MainTestTable[1] or "dd" in sys_argv :
        g = ''
    else:
        printe.output( '<<lightyellow>> Without save:')
        printe.output(NewDesc.keys() )
        printe.output(NewDesc)
        return ''
    #---
    langes = NewDesc.keys()
    #---
    lang_to_skip = [ "tg-latn", 'en-gb', 'en-ca']
    #---
    if len(langes) == 1: 
        lang = [ x for x in NewDesc.keys()][0]
        #---
        if lang in lang_to_skip:
            printe.output('work_api_desc:"%s" only en-gb and en-ca, Skipp... ' % q )
            return
        #---
        onedesc = NewDesc[lang]['value']
        printe.output('work_api_desc:"%s" only one desc"%s:%s"' % ( q ,lang, onedesc))
        himoAPI.Des_API( q, onedesc , lang )
    elif len(langes) == 2 and langes[0] in lang_to_skip and langes[1] in lang_to_skip:
        printe.output('work_api_desc:"%s" only en-gb and en-ca, Skipp... ' % q )
        return        
    else:
        #Desc = NewDesc
        #ca = True
        for fix in fixlang:
            if not fix in NewDesc.keys():
                fixlang.remove(str(fix))
        fixlang.sort()
        #---
        wwdesc( NewDesc , q , 1 , fixlang)
#---
def work2(item , topic, translations, num):
    q = item["q"]
    descriptions = item.get("descriptions",{})
    NewDesc = {}
    #---
    for lang in translations[topic].keys():
        if not lang in descriptions.keys():
            NewDesc[lang] = {"language":lang,"value":translations[topic][lang]}
    #---
    if NewDesc != {} :
        printe.output( '<<lightyellow>> **%d: work2:%s  (%s)'  %(num , q , topic))
        work_api_desc( NewDesc , q , [])
    else:
        printe.output(' nothing to add. ')
#---
def mainwithcat2(*args):
    printe.output( '*<<lightred>> > mainwithcat2:')
    #---
    # python3 pwb.py np/cs mainwithcat2 -ns:0 -usercontribs:JAnDbot
    options = {}
    #---
    start = time.time()
    final = time.time()
    #---
    user = ''
    user_limit = '3000'
    #---
    namespaces = '0'
    file = ''
    newpages = ''
    #---
    for arg in sys_argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == "-user" or arg == "-usercontribs" : 
            user = value
    #---
    list = []
    #---
    if user != "":
        list = himoBOT3wd.Get_UserContribs( user , limit = user_limit , namespace = namespaces , ucshow = "new" )
    #---
    num = 0
    printe.output( '*<<lightred>> > mainwithcat2 :')
    for q in list:
        num += 1

        item = himoBOT2.Get_Item_API_From_Qid( q , sites = "" , titles = "", props = "sitelinks" )
        if item:
            #---
            sitelinks = item.get("sitelinks",{})
            cswiki = sitelinks.get("cswiki","")
            #---
            if cswiki.startswith('Kategorie:'): 
                #---
                work2( item , 'Q4167836' , Tras , num )
            #---
        else:
            printe.output( '*<<lightred>> >%d error with item "%s" < :' % ( num , q ) )
    #---
if __name__ == "__main__":
    mainwithcat2()
#---
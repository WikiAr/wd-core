#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

python3 pwb.py np/si3 -usercontribs:Ghuron

إضافة وصف لعناصر ويكي بيانات الجديدة

python3 pwb.py np/si3 -ns:0 -offset:5000 -newpages:10000

python3 pwb.py np/si3 mainwithcat2 -newpages:200 descqs
python3 pwb.py np/si3 mainwithcat2 -newpages:100 ask

python3 pwb.py np/si3 -page:Q112167358
python3 pwb.py np/si3 -page:
python3 pwb.py np/si3 -page:Q113510544
python3 pwb.py np/si3 -page:Q111771063
python3 pwb.py np/si3 -start:Q98512481
python3 pwb.py np/si3 -start:Q97950000
python3 pwb.py np/si3 -start:Q97949000
python3 pwb.py np/si3 -start:Q111771064 err

python3 pwb.py np/si3 -newpages:200

python pwb.py np/si3 -newpages:200
python3 pwb.py np/si3 mainwithcat2 -newpages:200 ask

"""
#
# (C) Ibrahem Qasim, 2022
#
import sys
sys.argv.append('-family:wikidata')
sys.argv.append('-lang:wikidata')
#---
import json
import urllib
import codecs
import pywikibot
#---
from API.maindir import main_dir as main_dir1
if main_dir1 == "I:/core/master/": main_dir1 = "I:/core/core-yemen/"
#---
import gent
# generator = gent.get_gent(*args)
# gent.gent_string2html( title, arsite.encoding() )
#---
# 
#import pwb
import re
import string
import datetime 
# import dateutil.parser
#---
import time
import datetime
from datetime import datetime
#---
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
#---
import urllib
import urllib.request
import urllib.parse
#---
from API import read_json
from API.ru_st_2_latin import make_en_label
# enlabel = make_en_label(labels, q, Add=False)
#---
from API import printe
from API import himoAPI
from API import himoBOT
from API import himoBOT2
from API import himoBOT3 as himoBOT3wd
himoBOT3wd.log('https://' + 'www.wikidata.org/w/api.php')
#---
#---
#from trans import *  
from API.descraptions import DescraptionsTable, Qid_Descraptions
from des.desc import work_one_item
from des.places import placesTable
from des.railway import railway_tables, work_railway
#---
translations_o = { 1 : {}, 2 : {} }
from people.new3 import translations_o
#---
from API.taxones import tax_translationsNationalities, taxone_list, lab_for_p171, labforP105
from API.scientific_article_desc import Scientific_descraptions
#---
from np.np_lists import space_list_and_other, others_list, others_list_2, en_des_to_ar
from np.scientific_article import make_scientific_article
from np.nldesc import Make_space_desc, Make_others_desc
#---
genders = {
    'Q6581097': 'male', 
    'Q2449503': 'male', # transgender male
    'Q6581072': 'female', 
    'Q1052281': 'female', #  transgender female
    }
#---
MainTestTable = {1 : False}
#---
dump = {}
dump['new'] = []
done_list = {}
jsonfile = main_dir1 + 'np/done.json'
#---
Lalo_types = { "n" : {} }
new_types = {}
#---
newpages_d = { 1 : 0 }
offsetbg = { 1 : 0 }

#---
QSlimit = { 1 : 3000 }
#---
for arg in sys.argv:
    #---
    arg, sep, value = arg.partition(':')
    #---
    if arg.startswith('-') : arg = arg[1:]#print('change arg to %s ' % arg )
    #---
    if arg == 'qslimit':
        QSlimit[1] = int(value)
    #---
    if arg.lower() == 'newpages':
        newpages_d[1] = int(value)
    #---
    if arg.lower() == 'offset' or arg.lower() == 'off':
        printe.output( 'offsetbg[1] = int(%s)' % value )
        offsetbg[1] = int(value)
    #---
New_QS = { 1 : [] }
Nationalities_list = list( tax_translationsNationalities.keys() )
Nationalities_list.sort()
tax_translations_lower = {}
#---
for tax_key, tax_lab in taxone_list.items():      # الأصنوفة
    if tax_lab.strip() != '' and tax_key.strip() != '' :
        for natkey in Nationalities_list :            # النوع 
            natar = tax_translationsNationalities[natkey]
            if natkey.strip() != '' and natar.strip() != '' :
                kkey = tax_key.replace('~', natkey)
                tax_translations_lower[kkey.lower()] = tax_lab.replace('~',natar ) 
#---
Qids_translate = {
    'Q13442814 ': Scientific_descraptions,
    'Q21014462' : DescraptionsTable['cell line'], 
    'Q11173' : DescraptionsTable['chemical compound'], 
    # 'Q101352' : DescraptionsTable['family name'], # family name
    'Q3409032' : DescraptionsTable['unisex given name'],
    'Q11879590' : DescraptionsTable['female given name'],
    'Q12308941' : DescraptionsTable['male given name'],
    'Q24046192' : DescraptionsTable['Wikimedia category'],
    'Q4167836' : DescraptionsTable['Wikimedia category'],
    'Q4167410' : DescraptionsTable['Wikimedia disambiguation page'],
    'Q13406463' : DescraptionsTable['Wikimedia list article'],
    'Q11266439' : DescraptionsTable['Wikimedia template'],
    'Q11753321' : DescraptionsTable['Wikimedia template'],
    'Q17633526' : DescraptionsTable['Wikinews article'],
    'Q2467461':  { 'en':"academic department", 'ar' :'قسم أكاديمي'},
    'Q7187':  DescraptionsTable['gene'],
    'Q7889':  DescraptionsTable['video game'],
    'Q8054':  DescraptionsTable['protein'],
    'Q21199':  DescraptionsTable['natural number'],
    'Q24856':  DescraptionsTable['film series'],
    'Q49008':  DescraptionsTable['prime number'], 
    'Q4502142':  DescraptionsTable['visual artwork'],
    'Q6979593':  DescraptionsTable['national association football team'],
    'Q10870555':  DescraptionsTable['report'],
    'Q13100073':  DescraptionsTable['village in China'],
    'Q19389637':  DescraptionsTable['biographical article'],
    
    # space 
    }
#---
for x, taba in Qid_Descraptions.items():
    Qids_translate[x] = taba
#---
for qid1 in others_list:
    if not qid1 in Qids_translate:
        Qids_translate[qid1] = others_list[qid1]
#---
replace_desc = {
    "hu": { 
        "férfi keresztnév" : "férfikeresztnév",
    }
    }
#---
Add_en_labels = { 1 : False }
#---
if "addenlabel" in sys.argv: Add_en_labels[1] = True
#---
Geo_List = list( placesTable.keys() )
#---
def Get_P_API_id(item, P):
    #---
    #q = 'claims' in item and item['claims'][P]['mainsnak']['datavalue']['value']['id'] or False
    list = []
    claims = item.get("claims", {} ) .get( P, {} ) 
    for c in claims:
        #print(c)
        q = c.get('mainsnak', {} ).get('datavalue', {} ).get('value', {} ).get('id', False )
        if q:
            list.append(q)
    #---
    return list
#---
def Get_P_API_time(item, P):
    qlist = []
    #---
    if item:
        claims = item["claims"]
        if P in claims:
            for PP31 in claims[P]:
                vv = PP31.get("mainsnak").get("datavalue").get("value")
                vv = PP31['mainsnak']['datavalue']['value'] or False
                if vv and ( 'time' in vv ):
                    qlist.append( vv )
    #---
    Faso = {}
    #---
    if len(qlist) == 1:
        return qlist[0]
    #---
    elif len(qlist) > 1 :
        sasa = [ x['time'].split('-')[0].split('+0000000')[1] for x in qlist if x['time'].startswith('+0000000')]
        for i in sasa:
            Faso[i] = ''
        if len(Faso.keys() )  == 1:
            return qlist[0]
        else:
            return False
    else:
        return False
#---
def make_scientific_art(item, P31, num):
    #---
    table = make_scientific_article(item, P31, num, TestTable=MainTestTable[1])
    #---
    NewDesc =   table["descriptions"]
    qid =       table["qid"]
    rep_langs = table["fixlang"]
    #---
    work_api_desc( NewDesc, qid, rep_langs)
#---
def wwdesc( NewDesc, q, i, fixlang, ask = ""):
    #---
    printe.output('* si3.py wwdesc "%s" try number:"%d" :' % ( str(q), i )  )
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
        #summary = summary + ' - /* wbsetdescription-add:%d|%s */ %s.' % ( len(queries_list), deso, simple )
    #---
    if fixlang:
        for ii in fixlang:
            if not ii in NewDesc.keys():
                fixlang.remove(str(ii))
                printe.output('remove "%s" from fixlang because it\'s not in NewDesc'  % ii )
        fixed = ','.join(fixlang)
        summary = summary + ('- fix descriptions:(%d: %s).' % (len(fixlang), str(fixed)) ) #ملخص العمل
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
        printe.output('*work_api_desc %s "%s": try "%d",%s:' % ( str(q), value, i, menet )  )
        #---
        if 'printdisc' in sys.argv:
            printe.output( data3 )
        #---
        #item.editEntity(data, summary=summary)
        skipp = himoAPI.New_Mult_Des_2(q, data3, summary, True, ask = ask)
        #---
        if skipp:
            if 'success' in skipp:
                #printe.output(summary)
                printe.output('<<lightgreen>> **%s true. %s' % (q, summary) )
                False, NewDesc
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
                wwdesc( NewDesc2, q, i, fixlang, ask = ask)
                #return True, NewDesc2
                #---
            elif 'wikibase-api-invalid-json' in skipp :
                printe.output('<<lightred>> - "wikibase-api-invalid-json" ')
                printe.output(NewDesc)
            else:
                printe.output(skipp)
                #return False, NewDesc
                #return False, NewDesc
        else:
            printe.output('<<lightred>> - no skipp ')
    else:
        printe.output( '  *** no addedlangs')
#---
def work_qs( q, NewDesc ):
    qslinr = []
    #---
    for lang in NewDesc:
        qslinr.append( '%s|D%s|"%s"' % ( q, lang, NewDesc[lang]['value'] ) ) 
    #---
    for qsline in qslinr:
        if len(New_QS[1]) < QSlimit[1]:
            New_QS[1].append( qsline )
            printe.output( "<<lightyellow>>a %d\t%d:add %s to qlline " % (len(New_QS[1]), QSlimit[1], qsline  )  )
        else:
            printe.output( "<<lightgreen>> Add %d line to quickstatements" % len(New_QS[1]) )
            himoAPI.QS_line( "||".join( New_QS[1] ), user = "Mr.Ibrahembot" )
            New_QS[1] = []
#---
def work_api_desc( NewDesc, q, fixlang ):
    #---
    g = ''
    #---
    if not MainTestTable[1] or "dd" in sys.argv :
        g = ''
    else:
        printe.output( '<<lightyellow>> Without save:')
        printe.output(NewDesc.keys() )
        printe.output(NewDesc)
        return ''
    #---
    langes = list(NewDesc.keys())
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
        printe.output('work_api_desc:"%s" only one desc"%s:%s"' % ( q, lang, onedesc))
        himoAPI.Des_API( q, onedesc, lang )
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
        wwdesc( NewDesc, q, 1, fixlang)
#---
def make_tax_des_new( item ):
    q = item["q"]
    #---
    P171 = Get_P_API_id(item, "P171")
    #---
    if P171 == []: return ''
    #---
    P105 = Get_P_API_id(item, "P105")
    P105ar = ''
    for p in P105:
        if p in labforP105:
            P105ar = labforP105[p]
            break
    #---
    if P105ar == '' : return ''
    #---
    nan = '''SELECT DISTINCT ?item ?P171 ?item105
WHERE {
    BIND(wd:Q111771064 AS ?item)
  VALUES ?P171 { 
  %s
  }
    ?item wdt:P31 wd:Q16521.
    ?item wdt:P171* ?P171.
    ?P171 wdt:P105 wd:Q37517.
    ?item wdt:P105 ?item105.
}''' % ( " ".join( [ 'wd:%s' % x for x in lab_for_p171.keys() ] ) )
    nan = nan.replace("Q111771064", q)
    #---
    if "err" in sys.argv: printe.output(nan)
    #---
    bs = himoBOT.sparql_generator_url(nan)
    #---
    if bs != [] :
        bs = bs[0]
        printe.output("bs:")
        printe.output(bs)
        #---
        #[
            # {'P171': 'http://www.wikidata.org/entity/Q1390', 
            # 'item': 'http://www.wikidata.org/entity/Q111771066', 
            # 'item105': 'http://www.wikidata.org/entity/Q7432'}
        # ]
        itq = bs['item'].split('/entity/')[1]
        if itq == q:
            item105 = bs['item105'].split('/entity/')[1]
            P171 = bs['P171'].split('/entity/')[1]
            #---
            if P171 in lab_for_p171.keys():
                P171ar = lab_for_p171[P171]
                ar_lab = P105ar + ' ' + P171ar
                if "descqs" in sys.argv:
                    work_qs( q, { 'ar' : { 'value' : ar_lab } } )
                else:
                    himoAPI.Des_API( q, ar_lab, 'ar' )
        #---
def work_taxon_desc( item, endesc ):
    #---
    ardesc = tax_translations_lower.get(endesc.lower(), '')#.get("ar", '')
    q = item["q"]
    #printe.output( ' work_taxon_desc:endesc:"%s", ardesc:"%s"' % (endesc, ardesc) )
    printe.output( ' work_taxon_desc:ardesc:"%s"' % ardesc )
    if ardesc != '' :
        #---
        if "descqs" in sys.argv:
            work_qs( q, { 'ar' : { 'value' : ardesc } } )
        else:
            himoAPI.Des_API( q, ardesc, 'ar' )
    else:
        print(' no ardesc for en:%s.' %  endesc )
        make_tax_des_new(item)
#---
def work_new_list( item, p31, ardes ):
    #---
    printe.output( ' work_new_list:' )
    #---
    q = item["q"]
    NewDesc = {}
    #---
    gg = Qids_translate.get(p31) or others_list.get(p31) or placesTable.get(p31) or {}
    #---
    for lang in gg.keys():
        if not lang in item.get("descriptions", {}).keys():
            if gg[lang] != '' :
                NewDesc[lang] = {"language":lang, "value":gg[lang]}
    #---
    orig_desc = item.get("descriptions", {}).get("ar", "")
    #---
    if p31 in others_list or p31 in others_list_2:
        print("Make_others_desc ::::")
        ar_desc = Make_others_desc( 'ar', item, p31, orig_desc )
    else:
        print("Make_space_desc ::::")
        ar_desc = Make_space_desc( 'ar', item, p31, orig_desc )
    #---
    #if ar_desc != "" and ardes != ar_desc :
    if ar_desc != "" :
        NewDesc['ar'] = { "language":'ar', "value": ar_desc }
    #---
    #printe.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )
    if NewDesc != {} :
        printe.output( '<<lightyellow>> ** work_new_list p31:%s' % p31 )
        work_api_desc( NewDesc, q, [])
    else:
        print('work_new_list nothing to add. ')
#---
def work_people(item, topic, num, ardes ):
    q = item["q"]
    #---
    translations = translations_o[2]
    #---
    topic = topic.lower().strip()
    #---
    if topic == '' : return ''
    #---
    years = ''
    #---
    if topic.find("(") != -1:
        hhh = re.match('^(.*?) (\([\d\–-]+\))', topic)
        if hhh :
            topic = hhh.group(1)
            years = ' ' + hhh.group(2)
            print(f"topic:{topic},years:{years}")
    #---
    if en_des_to_ar.get(topic, '') != '':
        ara = en_des_to_ar[topic]
        #---
        if years != '' : ara += ' ' + years
        #---
        himoAPI.Des_API( q, ara , 'ar' )    
        return ""
    #---
    taber = translations.get( topic, {} )
    #---
    printe.output( ' work_people:' )
    #---
    if taber == {}:
        printe.output( ' no table descraptions for topic:%s' % topic )
        return ''
    #---
    printe.output( taber )
    #---
    if topic.startswith("researcher (orcid ") and ( ardes.strip() == "" or ardes.startswith("باحث (orcid ") ):
        arr = topic.replace("researcher (orcid ", "باحث (معرف أورسيد " )
        himoAPI.Des_API( q, arr, 'ar' )
    #---
    p21 = item.get("claims", {}).get("P21", [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", '')
    printe.output( p21 )
    #---
    descriptions = item.get("descriptions", {})
    NewDesc = {}
    #---
    p21_c = genders.get( p21 )
    #---
    if p21_c :
        for lang in taber.keys():
            if taber[lang].get(p21_c):
                if not lang in descriptions.keys():
                    NewDesc[lang] = {"language":lang, "value": taber[lang].get(p21_c) }
                    if years != "" and lang in ["en", "ar", "en-ca", "en-gb"]:
                        NewDesc[lang]["value"] += years
    #---
    if NewDesc != {} :
        printe.output( '<<lightyellow>> **%d: work_people:%s  (%s)'  %(num, q, topic))
        work_api_desc( NewDesc, q, [])
    else:
        print(' work_people nothing to add. ')
#---
def work_qid_desc(item, topic, num):
    printe.output( '<<lightyellow>>  work_qid_desc: ' )
    q = item["q"]
    descriptions = item.get("descriptions", {})
    NewDesc = {}
    addedlangs = [] 
    #---
    for lang in Qids_translate[topic].keys():
        #---
        des_for_lang = replace_desc.get(lang, {})
        #---
        if not lang in descriptions.keys():
            #descriptions[lang] = Qids_translate[topic][lang] 
            NewDesc[lang] = {"language":lang, "value":Qids_translate[topic][lang]}
            addedlangs.append(lang)
        elif descriptions[lang] in des_for_lang:
            orgdisc = descriptions[lang]
            NewDesc[lang] = {"language":lang, "value":des_for_lang[orgdisc]}
    #---
    #printe.output( '<<lightyellow>>  NewDesc' + str(NewDesc) )
    #if addedlangs:
    if NewDesc != {} :
        printe.output( '<<lightyellow>> **%d: work_qid_desc:%s  (%s)'  %(num, q, topic))
        work_api_desc( NewDesc, q, [])
    else:
        print('work_qid_desc nothing to add. ')
#---
def log_new_types(lists):
    #---
    if "nolog" in sys.argv: return ''
    #---
    jsonfils = main_dir1 + 'np/new_types.json'
    #---
    try:
        listo = codecs.open( jsonfils, "r", encoding="utf-8-sig").read()
        if listo == '' : 
            printe.output( 'file: %s == {} ' % jsonfils )
            with codecs.open( jsonfils, "a", encoding="utf-8-sig") as dfsdf:
                dfsdf.write( '{}' ) 
            dfsdf.close()
    except:
        printe.output( '' )
    #---
    if "log2" in sys.argv: jsonfils = main_dir1 + 'np/new_types2.json'
    #---
    if Lalo_types["n"] == {} :
        with codecs.open(jsonfils, "r", encoding="utf-8-sig") as listt:
            try:
                Lalo_types["n"] = json.load(listt)
            except:
                printe.output( 'Cant read %s ' % jsonfils )
                Lalo_types["n"] = read_json.read_bad_json(jsonfils)
        listt.close()
    #---
    for lenth, p31 in lists :
        if p31 in Lalo_types["n"]:
            Lalo_types["n"][p31] += lenth
        else:
            Lalo_types["n"][p31] = lenth
            printe.output( 'log new types Adding %s. '  % p31 )
    #---
    with open( jsonfils, 'w' ) as nfile:
        json.dump( Lalo_types["n"], nfile )
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
def ISRE( qitem, num, lenth, no_donelist = True, P31_list = False ):
    #---
    printe.output( f'--- *<<lightyellow>> >{num}/{lenth}: q:{qitem}' )
    #---
    if num < offsetbg[1] : 
        return ''
    #---
    item = himoBOT2.Get_Item_API_From_Qid( qitem, sites = "", titles = "", props = "claims|descriptions|labels" )#claims
    if item:
        #---
        q = qitem
        #---
        if item.get("q", q) != q :
            q = item.get("q",q)
            print(f"new qid:{q}")
        #---
        if Add_en_labels[1]:
            labels = item.get("labels", {})
            if labels.get("en","") == "":
                printe.output("item enlabel == ''")
                make_en_label(labels, q, Add = Add_en_labels[1])
        #---
        P31_table = []
        #---
        if P31_list and P31_list != [] and type(P31_list) == list :
            P31_table = P31_list
        else:
            P31_table = Get_P_API_id(item, 'P31')
        #---
        descriptions = item.get("descriptions", {})
        endes = descriptions.get("en", "")
        if endes  == "" : endes = descriptions.get("nl", "")
        ardes = descriptions.get("ar", "")
        #---
        if len(P31_table) == 0 :
            printe.output( 'no P31 at item. skip..' )
        #---
        for P31 in P31_table:
            #---
            if P31 and P31 != "" :
                #printe.output( item )
                printe.output( 'q:"%s", P31:"%s", en:"%s", ar:"%s"' % ( q, P31, endes, ardes ) )
                #---d
                if P31 == "Q5" :
                    #printe.output( 'endes "%s"' % endes )
                    work_people( item, endes.lower(), num, ardes )
                    break
                #---
                elif P31 in railway_tables :
                    work_railway( item, P31 )
                    break
                #---
                elif P31 in space_list_and_other or P31 in others_list or P31 in others_list_2 :
                    work_new_list( item, P31, ardes )
                    break
                #---
                elif P31 == "Q16521" :
                    work_taxon_desc( item, endes )
                    break
                #---
                elif P31 in Geo_List and placesTable[P31].get('ar') :
                    work_one_item( placesTable[P31]['ar'], 'ar', { "q": item["q"] }, 0, 1, findlab = True )
                    break
                #---
                elif P31 == 'Q13442814':
                    sc_desc = ['', 'مقالة علمية', 'مقالة بحثية'] 
                    if ardes in sc_desc:
                        if not "workibrahem" in sys.argv:
                            make_scientific_art(item, P31, num)
                    break
                #---
                elif P31 in Qids_translate:
                    work_qid_desc(item, P31, num)
                    break
                #---
                else:
                    if ardes == '' :
                        printe.output( '*<<lightred>> >P31 :%s not in Qids_translate.' % P31 )
                        if not P31 in new_types :
                            new_types[P31] = 0
                        new_types[P31] += 1
                        # log_new_types(P31)
        #---
        #done_list_append(q)
    else:
        printe.output( '*<<lightred>> >%d error with item "%s" < :' % ( num, q ) )
#---
def print_new_types():
    lists = [ [ y, x ] for x, y in new_types.items()]
    #lists = [ [ new_types[x], x ] for x in new_types.keys() ]
    lists.sort( reverse = True )
    #---
    log_new_types(lists)
    #---
    for lenth, p31 in lists :
        #Texts += Line % ( x, y )
        #---
        printe.output( "find:%d : P31:%s" % ( lenth, p31 ) )
    #---
def mainwithcat(*args):
    printe.output( '*<<lightred>> > mainwithcat:')
    #---
    lenth = len(sys.argv)
    printe.output(lenth)
    #if lenth == 0:  
        #args = {'-family:wikidata', '-lang:wikidata', '-ns:0', '-newpages:20000'}
        #args = {'-ns:0 -newpages:20000'}
    printe.output(args)
    # python3 pwb.py np/si3 -usercontribs:LargeDatasetBot
    # python3 pwb.py np/si3 -usercontribs:Mr._Ibrahem
    # python pwb.py np/si3 -usercontribs:Emijrpbot
    # python pwb.py np/si3 -usercontribs:Research_Bot
    # python3 pwb.py np/si3 -ns:0 -offset:5000 -newpages:10000
    # python3 pwb.py np/si3 -ns:0 -page:Q111521953 ask
    # python pwb.py np/si3 -ns:0 -page:Q62076323
    # python pwb.py np/si3 -usercontribs:Succu
    generator = gent.get_gent(*args)
    #---
    counter = 0
    for page in generator:
        counter += 1
        q = page.title(as_link=False)
        ISRE( q, counter, newpages_d[1] )
    #---
    print_new_types()
#---
def mainwithcat2(*args):
    printe.output( '*<<lightred>> > mainwithcat2:')
    #---
    # python pwb.py np/si3 main2 -newpages:10
    # python3 pwb.py np/si3 mainwithcat2 -newpages:1000
    # python3 pwb.py np/si3 mainwithcat2 -newpages:20000
    options = {}
    #---
    start = time.time()
    #---
    user = ''
    user_limit = '3000'
    #---
    namespaces = '0'
    file = ''
    newpages = ''
    #---
    list = []
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == "-limit" or arg == "limit" : 
            user_limit = value
        #---
        if arg == "-newpages" : 
            newpages = value
        #---
        # python3 pwb.py np/si3 main2 -arfile:Q7187
        if arg == "-arfile" : 
            file = 'dump/ar/%s.txt' % value
        #---
        # python3 pwb.py np/si3 main2 -file:dump/artest/Q7187.txt
        # python3 pwb.py np/si3 main2 -file:dump/artest/Q1457376.txt
        if arg == "-file" : 
            file = value
        #---
        # python3 pwb.py np/si3 main2 -artest:Q523
        # python3 pwb.py np/si3 main2 -artest:Q318
        # python3 pwb.py np/si3 main2 -artest:Q13442814
        # python3 pwb.py np/si3 main2 -artest:Q21672098
        # python3 pwb.py np/si3 main2 -artest:Q1516079
        # python3 pwb.py np/si3 main2 -artest:Q427087
        # python3 pwb.py np/si3 main2 -artest:Q79007
        # python3 pwb.py np/si3 main2 -artest:Q7187
        if arg == "-artest" : 
            file = 'dump/artest/%s.txt' % value
        #---
        if arg == '-page': list.append(value)
        #---
        # python3 pwb.py np/si3 mainwithcat2 -ns:0 -usercontribs:Edoderoobot
        # python3 pwb.py np/si3 mainwithcat2 -ns:0 -usercontribs:Ghuron
        if arg == "-user" or arg == "-usercontribs" : 
            user = value
        #---
        if arg == "-ns" : 
            namespaces = value
    #---
    if file != "":
        if not file.startswith(main_dir1) : file = main_dir1 + file
        oco = codecs.open( file, "r", encoding="utf-8").read().split('\n')
        list = [ x.strip() for x in oco if x.strip() != '' ]
    #---
    elif newpages != "":
        list = himoBOT3wd.Get_Newpages( "www", "wikidata", limit = newpages, namespace = namespaces )
    #---
    elif user != "":
        list = himoBOT3wd.Get_UserContribs( user, limit = user_limit, namespace = namespaces, ucshow = "new" )
    #---
    num = 0
    printe.output( '*<<lightred>> > mainwithcat2 :')
    for q in list:
        num += 1
        ISRE( q, num, len(list) ) 
    #---
    print_new_types()
    #---
    final = time.time()
    delta = int(final - start)
    #---
    printe.output( 'si3.py mainwithcat2 done in {} seconds'.format( delta ) )
#---
def main():
    SysArgs = sys.argv
    printe.output(len(SysArgs))
    printe.output( SysArgs )
    #if SysArgs and len(SysArgs) > 1:
    if SysArgs:
        if '-family:wikidata' in SysArgs:
            mainwithcat()
        #elif sys.argv[1] == 'death':
            #args = {'-file:c40/birth.txt'}
        else: 
            WorkNew()
    else:
        printe.output('no sys.argv')
#---
#32500000   اكتمل حتى
#32897048  متبقي حتى
#---
def WorkNew():
    start = 32700000
    ATend = 32500000
    #---
    # python3 pwb.py np/si3 WorkNew list1
    if "list1" in sys.argv:
        start = 77196790
        ATend = 77038417 
    #---
    # python3 pwb.py np/si3 WorkNew  list2
    if "list2" in sys.argv:
        start = 80999999 
        ATend = 80000000 
    #---
    # python3 pwb.py np/si3 WorkNew  list3
    if "list3" in sys.argv:
        start = 79788588 
        ATend = 79000000 
    #---
    # python3 pwb.py np/si3 WorkNew  list4
    if "list4" in sys.argv:
        start = 78411675 
        ATend = 78000000 
    #---
    # python3 pwb.py np/si3 WorkNew  list5
    if "list5" in sys.argv:
        start = 78823351 
        ATend = 78412057
    #---
    for arg in sys.argv:
        #---
        arg, sep, value = arg.partition(':')
        #---
        value = value.replace(", ", "")
        #---
        # python3 pwb.py np/si3 WorkNew start:95682306 to:100000
        # python3 pwb.py np/si3 WorkNew start:95000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:95630660 to:100000
        # python3 pwb.py np/si3 WorkNew start:85000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:75000000 to:100000
        # jsub -N ff python3 ./core/pwb.py ./core/np/si3 WorkNew start:75000000 to:100000

        # python3 pwb.py np/si3 WorkNew start:25000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:25130000 to:100000
        if arg == 'start':
            start = int(value)


      
    for arg in sys.argv:

        arg, sep, value = arg.partition(':')
        value = value.replace(", ", "")
        if arg == 'to':
            ATend = int(start) + int(value)
        #---
        # python3 pwb.py np/si3 WorkNew start:95, 682, 306 end:95, 582, 306 
        if arg == 'end':
            ATend = int(value)
    #---
    #---
    # python3 pwb.py np/si3 WorkNew 
    #---
    #if len(sys.argv) > 1:
        #start = sys.argv[1]
    #---
    #if len(sys.argv) > 2:
        #ATend = sys.argv[2]
    #---
    num   = 0
    #---
    start = int(start)
    end = int(ATend)
    #---
    if end < start:
        list  = range( end, start )
    else:
        list  = range( start, end )
    #---
    lenth = len(list)
    printe.output( '** <<lightyellow>> WorkNew in %d items (start:%d, end:%d)'  % (lenth, start, end) )
    #---
    for q in list:
        qitem  = 'Q%d' % q
        num += 1
        ISRE( qitem, num, lenth )
#---
MainTest = True#False#True
def Main_Test():
    # python pwb.py np/si3 test -page:Q65236227
    # python pwb.py np/si3 test
    printe.output( '<<lightyellow>> Main_Test :')
    num = 0
    MainTestTable[1] = True
    #for qq in ['Q21146082', 'Q21563434', 'Q21563625', 'Q22061800', 'Q22065466']:#, 'Q38822009', 'Q38822019', 'Q38822020']:

    #---
    q = "Q95690374"
    #---
    for arg in sys.argv:
        #---
        arg, sep, value = arg.partition(':')
        #---
        if arg == '-page':
            q = value
    #---
    #ISRE( "Q4116394", num, 0)   # scientific article published in 2018
    #ISRE( "Q20420158", num, 0)   # scientific article published in 2018
    #ISRE( "Q92203555", num, 0)  
    #ISRE( "Q95629862", num, 0)  
    #ISRE( "Q92313024", num, 0)   
    #---
    #ISRE( "Q90006515", num, 0)   
    #---
    #ISRE( "Q75729", num, 0)   
    ISRE( q, num, 0)   
    #---
    #ISRE( "Q92313521", num, 0)   
    #ISRE( "Q92313027", num, 0)   
    #---
    #---
    #ISRE( "Q92283597", num, 0)  
    #ISRE( "Q77038516", num, 0)  
    #---
    #ISRE( "Q42997227", num, 0)   # scientific article published in 1988
    #ISRE( "Q63681354", num, 0)   # scientific article published in 2018
    #ISRE( "Q63957216", num, 0)   # scientific article published in January 1990
    #ISRE( "Q36565264", num, 0)   # scientific article published on 5 September 2006
    #ISRE( "Q31056229", num, 0)   # scientific article published in May 1999
    #---
    '''
    item = FindItem(qq, no_donelist = True)
    num += 1
    #---python pwb.py np/d2 33200000
    if item:
        q = item["q"]
        sa = Get_P_API_time(item, 'P577')
        printe.output(sa)
        #make_scientific_art(item, 'Q13442814', num)
    '''
#---
def read_new_types_file():
    #---
    # python3 pwb.py np/si3 read 
    # python3 pwb.py np/si3 read -file:np/new_types11.json
    # python3 pwb.py np/si3 read -number:500
    #---
    file = 'np/new_types.json'
    number = 100
    #---
    for arg in sys.argv:
        arg, sep, value = arg.partition(':')
        #---
        if arg == "-number" or arg == "number" :  number = int(value)
        if arg == "-file" or arg == "file" :  file = value
    #---
    wd_file = {}
    jsonfile = main_dir1 + file
    #---
    #space_list_and_other
    #---
    Known = [ "Q5", "Q16521" ]
    #---
    # with codecs.open(jsonfile, "r", encoding="utf-8-sig") as listt:
        # wd_file = json.load(listt)
    #---
    wd_file = read_json.read_bad_json(jsonfile)
    Years = wd_file.keys()
    #---
    PP = [ [ leen, gf ] for gf, leen in wd_file.items() ]
    PP.sort( reverse = True )
    #---Geo_List
    printe.output("===================" ) 
    for yy, xh in PP : 
        if yy > number \
        and xh not in Qids_translate.keys() \
        and xh not in Known \
        and xh not in space_list_and_other \
        and xh not in others_list \
        and xh not in others_list_2 \
        and xh not in Geo_List :
            #printe.output( '* %d\t \t{{Q|%s}}' % (yy, xh) )
            printe.output( "*'%s':{'ar':'{{#invoke:Wikidata2|labelIn|ar|%s}}', 'en':'{{#invoke:Wikidata2|labelIn|en|%s}}' }, # %d" % (xh, xh, xh, yy) )
    printe.output("===================" ) 
    #---  
    print('done')
#---
# python3 pwb.py np/si3 read
#---
if __name__ == "__main__":
    if "read" in sys.argv:
        read_new_types_file()
    elif "WorkNew" in sys.argv or "worknew" in sys.argv:
        WorkNew()
    elif "test" in sys.argv:
        Main_Test()
    elif "mainwithcat2" in sys.argv or "main2" in sys.argv:
        mainwithcat2()
    else:
        mainwithcat()
#---
# python3 pwb.py np/si3 main2 -newpages:50
# python3 pwb.py np/si3 mainwithcat2 -newpages:500
# python pwb.py np/si3 -newpages:100
# python3 ./core/pwb.py ./core/np/si3 mainwithcat2 -limit:3000 -ns:0 -usercontribs:Research_Bot
# python3 pwb.py np/si3 mainwithcat2 -limit:6000 -ns:0 -usercontribs:Succu
# python3 pwb.py np/si3 mainwithcat2 -limit:6000 -ns:0 -usercontribs:LargeDatasetBot
# python3 pwb.py np/si3 mainwithcat2 -limit:6000 -ns:0 -usercontribs:Research_Bot
#---
#!/usr/bin/python
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
import sys
sys.argv.append('-family:wikidata')
sys.argv.append('-lang:wikidata')
#---
import json
import codecs
import pywikibot
import re
import os
from pathlib import Path
import string
import time
import urllib
import urllib.request
import urllib.parse
import datetime
from datetime import datetime
#---
from API import printe
#---
Dir = Path(__file__).parent
main_dir1 = Path(__file__).parent.parent + '/'
#---
printe.output( f'<<lightyellow>> main_dir1 = {main_dir1}' )
#---
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")
#---
from np import read_json
from des.ru_st_2_latin import make_en_label
# enlabel = make_en_label(labels, q, Add=False)
#---
from wd_API import himoAPI
from wd_API import wd_bot
from API import himoBOT2
#---
from wd_API import wd_desc
# wd_desc.wwdesc(NewDesc, qid, i, fixlang, ask="", tage='')
# wd_desc.work_api_desc(NewDesc, qid, addedlangs=[], fixlang=[], ask="")
#---
from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions, replace_desc
#---
from des.desc import work_one_item
from des.places import placesTable
from des.railway import railway_tables, work_railway
#---
translations_o = { 1 : {}, 2 : {} }
from people.new3 import translations_o
#---
from desc_dicts.taxones import tax_translationsNationalities, taxone_list, lab_for_p171, labforP105
from desc_dicts.scientific_article_desc import Scientific_descraptions
#---
from np.np_lists import space_list_and_other, others_list, others_list_2, en_des_to_ar
from np.scientific_article import make_scientific_article
from np.nldesc import Make_space_desc, Make_others_desc
#---
if True:
    genders = {
        'Q6581097': 'male', 
        'Q2449503': 'male', # transgender male
        'Q6581072': 'female', 
        'Q1052281': 'female', #  transgender female
        }
    #---
    MainTestTable = {1 : False}
    #---
    Lalo_types = { "n" : {} }
    new_types = {}
    #---
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
        if arg.lower() == 'offset' or arg.lower() == 'off':
            printe.output( f'offsetbg[1] = int({value})' )
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
    Add_en_labels = { 1 : False }
    #---
    if "addenlabel" in sys.argv: Add_en_labels[1] = True
    #---
    Geo_List = list( placesTable.keys() )
#---
def Get_P_API_id(item, P):
    #---
    #q = 'claims' in item and item['claims'][P]['mainsnak']['datavalue']['value']['id'] or False
    lista = []
    claims = item.get("claims", {} ) .get( P, {} ) 
    for c in claims:
        #print(c)
        q = c.get('mainsnak', {} ).get('datavalue', {} ).get('value', {} ).get('id', False )
        if q:
            lista.append(q)
    #---
    return lista
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
def work_qs( q, NewDesc ):
    qslinr = []
    #---
    for lang in NewDesc:
        qslinr.append( f"{q}|D{lang}|\"{NewDesc[lang]['value']}\"" ) 
    #---
    for qsline in qslinr:
        if len(New_QS[1]) < QSlimit[1]:
            New_QS[1].append( qsline )
            printe.output( "<<lightyellow>>a %d\t%d:add %s to qlline " % (len(New_QS[1]), QSlimit[1], qsline  )  )
        else:
            printe.output( f"<<lightgreen>> Add {len(New_QS[1])} line to quickstatements" )
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
            printe.output(f'work_api_desc:"{q}" only en-gb and en-ca, Skipp... ' )
            return
        #---
        onedesc = NewDesc[lang]['value']
        printe.output(f'work_api_desc:"{q}" only one desc"{lang}:{onedesc}"')
        himoAPI.Des_API( q, onedesc, lang )
    elif len(langes) == 2 and langes[0] in lang_to_skip and langes[1] in lang_to_skip:
        printe.output(f'work_api_desc:"{q}" only en-gb and en-ca, Skipp... ' )
        return        
    else:
        #Desc = NewDesc
        #ca = True
        for fix in fixlang:
            if not fix in NewDesc.keys():
                fixlang.remove(str(fix))
        fixlang.sort()
        #---
        wd_desc.wwdesc( NewDesc, q, 1, fixlang)
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
    bs = wd_bot.sparql_generator_url(nan)
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
#---
def work_taxon_desc( item, endesc ):
    #---
    ardesc = tax_translations_lower.get(endesc.lower(), '')#.get("ar", '')
    q = item["q"]
    #printe.output( ' work_taxon_desc:endesc:"%s", ardesc:"%s"' % (endesc, ardesc) )
    printe.output( f' work_taxon_desc:ardesc:"{ardesc}"' )
    if ardesc != '' :
        #---
        if "descqs" in sys.argv:
            work_qs( q, { 'ar' : { 'value' : ardesc } } )
        else:
            himoAPI.Des_API( q, ardesc, 'ar' )
    else:
        print(f' no ardesc for en:{endesc}.' )
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
        printe.output( f'<<lightyellow>> ** work_new_list p31:{p31}' )
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
        hhh = re.match(r'^(.*?) (\([\d\–-]+\))', topic)
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
        printe.output( f' no table descraptions for topic:{topic}' )
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
                printe.output( f'Cant read {jsonfils} ' )
                Lalo_types["n"] = read_json.read_bad_json(jsonfils)
        listt.close()
    #---
    for lenth, p31 in lists :
        if p31 in Lalo_types["n"]:
            Lalo_types["n"][p31] += lenth
        else:
            Lalo_types["n"][p31] = lenth
            printe.output( f'log new types Adding {p31}. ' )
    #---
    with open( jsonfils, 'w' ) as nfile:
        json.dump( Lalo_types["n"], nfile )
    #---
#---
def ISRE( qitem, num, lenth, no_donelist = True, P31_list = False ):
    #---
    printe.output( f'--- *<<lightyellow>> >{num}/{lenth}: q:{qitem}' )
    #---
    if num < offsetbg[1] : 
        return ''
    #---
    item = himoBOT2.Get_Item_API_From_Qid( qitem, sites = "", titles = "", props = "claims|descriptions|labels" )#claims
    #---
    q = qitem
    #---
    if not item:
        printe.output( '*<<lightred>> >%d error with item "%s" < :' % ( num, q ) )
        return
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
        if not P31 or P31 == "" :
            continue
        #---
        #printe.output( item )
        printe.output( f'q:"{q}", P31:"{P31}", en:"{endes}", ar:"{ardes}"' )
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
                if "workibrahem" not in sys.argv:
                    make_scientific_art(item, P31, num)
            break
        #---
        elif P31 in Qids_translate:
            work_qid_desc(item, P31, num)
            break
        #---
        else:
            if ardes == '' :
                printe.output( f'*<<lightred>> >P31 :{P31} not in Qids_translate.' )
                #---
                if not P31 in new_types :   new_types[P31] = 0
                #---
                new_types[P31] += 1
    #---
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
#---
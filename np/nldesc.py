#!/usr/bin/python
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.
# Q13005188 mandal
'''

'''
import re
from API import printe
import sys
# ---
from wd_api import himoAPI
from API import himoBOT2
# ---
# --- == == == == == == == == == == == ==
from desc_dicts.descraptions import Qid_Descraptions
# ---
items2do = 0  # global parameter to print progress
totaledits = 0
lng_canbeused = [
    'en',
    'de',
    'fr',
    'it',
    'es',
    'pt',
    'ca',
    'dk',
    'cs',
    'hr',
    'nl',
    'ro',
    'sh',
    'vi',
    'eo',
    'simple',
    'eu',
    'zea',
    'li',
    'fy',
    'oc',
    'af',
    'nb',
    'no',
    'pl',
    'si',
    'sv',
    'wa',
]
# ---
QSlimit = {
    1: 200
}
sparqler = {
    1: ''
}
Offq = {
    1: 0
}
Off = {
    1: 0
}
limit = {
    1: 0
}
# ---
totallimit = {
    1: 10000
}
# ---
Labels_Csash = {
    'ar': {}
}
# ---
from np.cash import *  # Labels_Csash
from np.np_lists import bldiat, Space_tab, p50s, nationalities, songs_type, others_list, others_list_2, space_list_and_other, qura, Geo_entity
# ---
for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(':')
    # ---
    if arg.startswith('-'):
        arg = arg[1:]
    # ---
    if arg == 'off':
        Off[1] = int(value)
        printe.output('Off[1] = %d' % Off[1])
    # ---
    if arg == 'offq':
        Offq[1] = int(value)
        printe.output('Offq[1] = %d' % Offq[1])
    # ---
    if arg == 'totallimit' or arg == 'all':
        totallimit[1] = int(value)
        printe.output('totallimit[1] = %d' % totallimit[1])
    # ---
    if arg == 'limit':
        limit[1] = int(value)
        printe.output('limit[1] = %d' % limit[1])
    # ---
    if arg == 'qslimit':
        QSlimit[1] = int(value)
        printe.output('QSlimit[1] = %d' % QSlimit[1])
    # ---
    if arg == 'sparql':
        sparqler[1] = value
        printe.output('sparqler[1] = "%s"' % sparqler[1])
# ---
from des.railway import railway_tables, work_railway


def Make_railway_desc(wditem, p31):
    # ---
    return work_railway(wditem, p31)
    # ---


def get_lng_description(language, wikidataitem):
    return wikidataitem.get('descriptions', {}).get(language, '')


def its_a_generalthing(wditem, shortstr, longdescrstr, myclaim, claimstr=''):
    # ---
    pp = wditem.get('claims', {}).get(myclaim, [])
    # ---
    for x in pp:
        LNKitem = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
        if claimstr == '':
            claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    if claimstr == '':
        return shortstr
    # ---
    laste = f'{longdescrstr.strip()} {claimstr}'
    laste = laste.replace('جين في إنسان عاقل', 'جين من أنواع جينات الإنسان العاقل')
    # ---
    printe.output('laste:(%s)' % laste)
    return laste


def get_label_txt(lng, wdi, property, array=0, fallback=False):
    # try:
    if property in wdi.get('claims', {}):
        if (len(wdi.get('claims', {}).get(property, '')) > array):
            lnkProperty = wdi.get('claims', {}).get(property)[array].getTarget()
            propwdi = himoBOT2.Get_Item_API_From_Qid(lnkProperty)  # xzo
            if propwdi:
                if lng in propwdi.get('labels', {}):
                    return propwdi.get('labels', {}).get(lng)
                elif fallback:
                    if lng != 'ar':
                        for fallbacklng in lng_canbeused:
                            if fallbacklng in propwdi.get('labels', {}):
                                return propwdi.get('labels', {}).get(fallbacklng, '')
    return ''


def its_a_headquarted_thing(lng, wdi, thing):
    where = get_label_txt(lng, wdi, 'P159', fallback=True)
    if where != '':
        return f'{thing} {where}'
    return ''


def its_something_in_an_entity(wdi, something):
    prnEntity = ''
    prnCountry = ''
    # 'P131'    #P131
    # 'P17'   #P17
    LNKentity = wdi.get('claims', {}).get('P131', [{}])[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
    if LNKentity != '':
        prnEntity = Get_label(LNKentity)
    # ---
    LNKcountry = wdi.get('claims', {}).get('P17', [{}])[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
    if LNKcountry != '':
        prnCountry = Get_label(LNKcountry)
    # ---
    if prnCountry != '' and prnEntity != '':
        return f'{something} {prnEntity}، {prnCountry}'
    elif prnCountry != '':
        return f'{something} {prnCountry}'
    elif prnEntity != '':
        return f'{something} {prnEntity}'
    # ---
    return ''
    # ---


def Get_label(qid):
    # ---
    lng = 'ar'
    label = ''
    # ---
    if lng not in Labels_Csash:
        Labels_Csash[lng] = {}
    # ---
    if qid in Labels_Csash.get(lng, {}):
        return Labels_Csash[lng][qid]
    # ---
    if qid == '':
        return label
    # ---
    WDI = himoBOT2.Get_Item_API_From_Qid(qid, sites='', titles='', props='labels')
    # ---
    if lng in WDI.get('labels', {}):
        label = WDI.get('labels', {})[lng]
    # ---
    if label != '':
        label = label.replace(" (كوكبة)", '')
        label = label.replace(" (نجم)", '')
        label = label.replace(" (مجرة)", '')
        # label = label.replace("كوكبة ",'')
        Labels_Csash[lng][qid] = label
    # ---
    return label


def get_female_for_p17(contry_lab, type):
    # ---
    if contry_lab.strip() == '':
        return ''
    # ---
    lab = nationalities.get(contry_lab, {}).get(type, '')
    # ---
    if contry_lab not in nationalities:
        printe.output('contry_lab:%s not in nationalities' % contry_lab)
    # ---
    return lab


def its_something_in_a_country(wdi, something):
    # ---
    printe.output('its_something_in_a_country,something:%s' % something)
    # ---
    prnCountry = ''
    # ---
    Claims = wdi.get('claims', {})
    # ---
    if 'P17' in Claims:
        LNKcountry = Claims.get('P17')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    if prnCountry == '' and 'P495' in Claims:
        LNKcountry = Claims.get('P495')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    if prnCountry == '' and 'P131' in Claims:
        LNKcountry = Claims.get('P131')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    printe.output('prnCountry:%s' % prnCountry)
    # ---
    fanee = something.strip()
    # ---
    ande = ' في '
    # ---
    females = [
        'شركة طيران',
        'شركة',
        'منظمة',
    ]
    # ---
    males = [
        'قانون تشريعي',
        'برنامج تلفزيوني',
        'مسلسل تلفزيوني',
        'طاقم موسيقي',
        'حزب سياسي',
        'نادي كرة قدم للهواة',
        'نادي كرة قدم',
    ]
    if fanee in males:
        ande = ' من '
    # ---
    dara = ande.strip() + ' ' + prnCountry.strip()
    # ---
    if something.strip() in males:
        ma = get_female_for_p17(prnCountry.strip(), 'man')
        if ma != '':
            dara = ma
            if something.strip() == 'نادي كرة قدم للهواة':
                something = 'نادي كرة قدم'
    # ---
    elif something.strip() in females:
        f = get_female_for_p17(prnCountry.strip(), 'women')
        if f != '':
            dara = f
    # ---
    if prnCountry != '':
        fanee = something.strip() + ' ' + dara.strip()
    # ---
    return fanee


def its_canton_of_France(wdi):  # Q184188
    # 'P131' = 'P131'
    clai = wdi.get('claims', {})
    current_desc = wdi.get('descriptions', {}).get('ar', '')
    desco = 'كانتون فرنسي'
    if current_desc == '':
        if 'P131' in clai:
            LNKcommunity = clai.get('P131')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
            label = Get_label(LNKcommunity)
            if label != '':
                label = label.replace('، فرنسا', '').replace(' (فرنسا)', '')
                desco = 'كانتون في ' + label + '، فرنسا'
    return desco


def its_disambigue(lng, wdi):
    if (lng in wdi.get('descriptions', {})) or (len(wdi.get('claims', {})) > 1):  # there is already a description, skip this one
        return ''
    return 'Wikimedia-doorverwijspagina'


def its_a_publication(wditem):
    over = uitgever = datumstr = ''
    if ('P921' in wditem.get('claims', {})):
        its_a_generalthing(wditem, '', 'over', 'P921')
    if ('P123' in wditem.get('claims', {})):
        its_a_generalthing(wditem, '', 'van uitgever', 'P123')
    if ('P577' in wditem.get('claims', {})):
        pass
    return 'publicatie'


def its_an_episode(lng, wditem):
    if lng in wditem.get('descriptions', {}):
        return wditem.get('descriptions', {})[lng]
    if 'P179' in wditem.get('claims', {}):  # serie
        LNKseries = wditem.get('claims', {}).get('P179')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        serienaam = Get_label(LNKseries)
        if serienaam != '':
            serienaam = serienaam.replace('، مسلسل', '').replace(' (مسلسل)', '')
            return 'حلقة من سلسلة ' + serienaam
    return ''


def its_a_discography(lng, wditem):
    if 'P175' in wditem.get('claims', {}):
        artistLNK = wditem.get('claims', {}).get('P175')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if artistLNK is not None:
            wdArtist = himoBOT2.Get_Item_API_From_Qid(artistLNK)  # xzo
            if lng in wdArtist.get('labels', {}):
                return 'discografie van ' + wdArtist.get('labels', {}).get(lng, '')
            else:
                if lng != 'ar':
                    for trylng in lng_canbeused:
                        if trylng in wdArtist.get('labels', {}):
                            return 'discografie van ' + wdArtist.get('labels', {}).get(trylng, '')
    return 'discografie'


def action_one_P131_item(lng, oneitem):
    global totaledits
    if (lng in oneitem.get('descriptions', {})):
        nld = oneitem.get('descriptions', {}).get(lng, '')
    else:
        nld = ''
    if (lng in oneitem.get('labels', {})):
        oneitem.get('labels', {}).get(lng, '')
    else:
        pass
    adminname = ''
    isaname = ''
    countryname = ''
    if ('P31' in oneitem.get('claims', {})):
        LNKisa = oneitem.get('claims', {}).get('P31')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if LNKisa is not None:
            isa = himoBOT2.Get_Item_API_From_Qid(LNKisa)  # xzo
            if lng in isa.get('labels', {}):
                isaname = isa.get('labels', {}).get(lng, '')
    if (isaname in ['dorp in China']):
        shortname = 'قرية'
    else:
        shortname = isaname
    if ('P131' in oneitem.get('claims', {})):
        LNKadmin = oneitem.get('claims', {}).get('P131')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if LNKadmin is not None:
            admin = himoBOT2.Get_Item_API_From_Qid(LNKadmin)  # xzo
            if lng in admin.get('labels', {}):
                adminname = admin.get('labels', {}).get(lng, '')
    if ('P17' in oneitem.get('claims', {})):
        LNKcountry = oneitem.get('claims', {}).get('P17')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if LNKcountry is not None:
            country = himoBOT2.Get_Item_API_From_Qid(LNKcountry)  # xzo
            if lng in country.get('labels', {}):
                countryname = country.get('labels', {}).get(lng, '')
    data = {}
    found = False
    if (lng not in oneitem.get('labels', {})):
        if lng != 'ar':
            for plang in lng_canbeused:
                if (plang in oneitem.get('labels', {})) and not found:
                    data.update({
                        'labels': {
                            lng: oneitem.get('labels', {}).get(plang, '')
                        }
                    })
                    found = True
    if (adminname == ''):
        newdescription = '%s' % isaname
    else:
        newdescription = f'{shortname} in {adminname}, {countryname}'
    if (isaname != '') and (nld in ['', 'قرية', 'dorp in China', 'gemeente', 'gemeente in China']):
        data.update({
            'descriptions': {
                lng: newdescription
            }
        })
    # ---
    try:
        oneitem.editEntity(data, summary='nl-description, [[User:Edoderoobot/Set-nl-description|python code]], logfile on https://goo .gl/BezTim')
        totaledits += 1
        return 1
    except ValueError:
        print("ValueError occured on %s", oneitem.title())
    except BaseException:
        print("Undefined error occured on %s-[%s]", oneitem.title(), 'simpleP131')
    else:
        pass  # print("Else:")
    # ---
    return 0


def its_an_audio_drama(wditem):
    if ('P179' in wditem.get('claims', {})):
        return its_a_generalthing(wditem, 'hoorspel', 'hoorspel van', 'P50')
    if ('P50' in wditem.get('claims', {})):
        return its_a_generalthing(wditem, 'hoorspel', 'hoorspel van', 'P50')
    if ('P495' in wditem.get('claims', {})):
        return its_a_generalthing(wditem, 'hoorspel', 'hoorspel uit', 'P495')
    return 'hoorspel'


def its_a_taxon(lng, wditem):
    '''
    read P171/mother taxon until taxo-rang/P105 is <Q19970288/no value> -> that mother taxon is the first part (insect/)
    '''
    if (lng in wditem.get('descriptions', {})):
        return wditem.get('descriptions', {})[lng]
    return 'taxon'


def its_a_composition(lng, wditem):
    '''
    find composer P86
    '''
    if ('P86' in wditem.get('claims', {})):
        composerLNK = wditem.get('claims', {}).get('P86')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if composerLNK is not None:
            composer = himoBOT2.Get_Item_API_From_Qid(composerLNK)  # xzo
            if (lng in composer.get('labels', {})):
                return 'compositie van %s' % composer.get('labels', {}).get(lng, '')
    return 'compositie'


def its_a_tabon_in_thailand(lng, wditem):
    newdescription = ''
    if ('P131' in wditem.get('claims', {})):
        LNKtambon = wditem.get('claims', {}).get('P131')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if LNKtambon is not None:
            WDitemtambon = himoBOT2.Get_Item_API_From_Qid(LNKtambon)  # xzo
            return Get_label_from_item(lng, WDitemtambon)
    return newdescription


def Get_label_from_item(lng, wditem):
    if wditem and isinstance(wditem, dict):
        labels = wditem.get('labels', {})
        # ---
        if lng in labels:
            return labels[lng]
    # ---
    return ''


def its_a_fictional_character(wditem):
    if ('P1441' in wditem.get('claims', {})):
        my_description = its_a_generalthing(wditem, 'personage', 'personage uit', 'P1441')
    elif ('P1080' in wditem.get('claims', {})):
        my_description = its_a_generalthing(wditem, 'personage', 'personage uit', 'P1080')
    else:
        my_description = 'personage'
    return my_description


def its_a_computergame(lng, wditem):
    printe.output(' its_a_computergame ')
    if ('P178' in wditem.get('claims', {})):  # المطور
        LNKdeveloper = wditem.get('claims', {}).get('P178')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if LNKdeveloper is not None:
            WDitemdeveloper = himoBOT2.Get_Item_API_From_Qid(LNKdeveloper)
            developer_name = Get_label_from_item(lng, WDitemdeveloper)
            if (developer_name != ''):
                return 'لعبة فيديو من تطوير %s' % developer_name
    if ('P179' in wditem.get('claims', {})):  # السلسلة
        serieLNK = wditem.get('claims', {}).get('P179')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        if serieLNK is not None:
            WDitemserie = himoBOT2.Get_Item_API_From_Qid(serieLNK)
            seriename = Get_label_from_item(lng, WDitemserie)
            if (seriename != ''):
                # return 'computerspel uit de serie %s' % seriename
                return 'لعبة فيديو من سلسلة %s' % seriename
    return 'لعبة فيديو'


# ---
New_QS = {
    1: []
}


def descqs(q, value, lang):
    if len(New_QS[1]) < QSlimit[1]:
        qsline = f'{q}|D{lang}|"{value}"'
        New_QS[1].append(qsline)
        printe.output("<<lightyellow>>a %d\t%d:add %s to qlline." % (len(New_QS[1]), QSlimit[1], qsline))
    else:
        printe.output("<<lightgreen>> Add %d line to quickstatements" % len(New_QS[1]))
        himoAPI.QS_line("||".join(New_QS[1]), user="Mr.Ibrahembot")
        New_QS[1] = []


def Add_desc(q, value, lang):
    if 'descqs' in sys.argv:
        descqs(q, value, lang)
    else:
        himoAPI.Des_API(q, value, lang, ask='')


def Make_space_desc(lng, wditem, type_of_item, orig_desc, claimstr=''):
    my_description = ''
    # ---
    printe.output("Make_space_desc::")
    # ---
    if type_of_item == 'Q2467461':
        my_description = 'قسم أكاديمي'
    # ---
    elif type_of_item in p50s:
        if orig_desc in ['', 'عمل أدبي', p50s[type_of_item]['ar']]:
            my_description = its_a_p50(type_of_item, wditem, p50s[type_of_item]['ar'], claimstr=claimstr)
    # ---
    elif type_of_item == 'Q7889':  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
        if orig_desc in ['لعبة فيديو', '']:
            my_description = its_a_computergame(lng, wditem)
    # ---
    # Q476028
    elif type_of_item == 'Q476028':  # نادي كرة قدم
        if orig_desc in ['نادي كرة قدم']:
            my_description = its_something_in_a_country(wditem, 'نادي كرة قدم')
    # ---
    elif type_of_item == 'Q14752149':  # amateur football club
        if orig_desc in ['', 'نادي كرة قدم للهواة']:
            my_description = its_something_in_a_country(wditem, 'نادي كرة قدم للهواة')
    # ---
    elif type_of_item == 'Q7278':  # political party
        if orig_desc in ['حزب سياسي', '']:
            my_description = its_something_in_a_country(wditem, 'حزب سياسي')
    # ---
    elif type_of_item == 'Q265158' and orig_desc in ['', 'مراجعة']:
        my_description = its_a_generalthing(wditem, 'مراجعة', 'مراجعة منشورة في', 'P1433')
    # ---
    elif type_of_item == 'Q13433827' and orig_desc in ['', 'مقالة موسوعية']:
        my_description = its_a_generalthing(wditem, 'مقالة موسوعية', 'مقالة في', 'P1433')
    # ---
    elif type_of_item == 'Q191067' and orig_desc in ['مقالة', '']:
        my_description = its_a_generalthing(wditem, '', 'مقالة في ', 'P1433')
    # ---
    elif type_of_item == 'Q96739634':
        if orig_desc in ['', 'حركة فردية']:
            my_description = its_a_generalthing(wditem, 'حركة فردية', 'حركة فردية بواسطة', 'P50')
    # ---
    elif type_of_item == 'Q3305213':  # لوحة فنية بواسطة P170
        if orig_desc in ['لوحة فنية', '']:
            my_description = its_a_generalthing(wditem, 'لوحة فنية', 'لوحة فنية بواسطة', 'P170')
    # ---
    elif type_of_item == 'Q7187':
        if (orig_desc in ['جين', '']):
            my_description = its_a_generalthing(wditem, '', 'جين في ', 'P703')
    # ---
    # جين كاذب
    elif type_of_item == 'Q277338':
        if orig_desc in ['جين كاذب', 'جين', 'speudogen', '']:
            my_description = its_a_generalthing(wditem, '', 'جين كاذب في ', 'P703')  # P1057 #fixed
    # ---
    # بروتين
    elif type_of_item == 'Q8054':
        if (orig_desc in ['بروتين', '']):
            my_description = its_a_generalthing(wditem, '', 'بروتين في ', 'P703')
    # ---
    elif type_of_item == 'Q783866':
        if (orig_desc in ['مكتبة جافا سكريبت', '']):
            my_description = its_a_generalthing(wditem, 'مكتبة جافا سكريبت', 'مكتبة جافا سكريبت من تطوير ', 'P178')
    # ---
    elif type_of_item == 'Q620615':  # تطبيق محمول
        if (orig_desc in ['تطبيق محمول', '']):
            my_description = its_a_generalthing(wditem, '', 'تطبيق محمول من تطوير ', 'P178')
    # ---
    elif type_of_item in Space_tab:
        labr = Space_tab[type_of_item]
        if orig_desc in [labr, '']:
            my_description = its_a_generalthing(wditem, labr, '%s في ' % labr, 'P59')
    # ---
    elif type_of_item == 'Q2831984':  # ألبوم قصص مصورة uit de serie P179
        if orig_desc in ['', 'ألبوم قصص مصورة']:
            my_description = its_a_generalthing(wditem, '', 'ألبوم قصص مصورة من سلسلة ', 'P179')
        if (my_description in ['', 'ألبوم قصص مصورة']):
            my_description = its_a_generalthing(wditem, '', 'ألبوم قصص مصورة من تأليف ', 'P50')
    # ---
    elif type_of_item == 'Q19389637':
        short = 'مقالة سيرة ذاتية'
        if (orig_desc in [short, '']) or (orig_desc.find(short) == 0):
            printe.output("work in Q19389637")
            # my_description ='biografisch artikel',''
            my_description = its_a_generalthing(wditem, short, 'مقالة سيرة ذاتية للمؤلف', 'P50')
            # ---
            if my_description == short:
                my_description = its_a_generalthing(wditem, short, 'مقالة سيرة ذاتية منشورة في', 'P1433')
            # ---
            if my_description == short:
                my_description = its_a_generalthing(wditem, short, 'مقالة سيرة ذاتية عن', 'P921')
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", '', my_description.lower())
    if test.lower() != my_description.lower():
        my_description = ''
        printe.output(f'test:[{test}] != my_description[{my_description}]')
    # ---
    printe.output('Make_space_desc:[%s]' % my_description)
    # ---
    return my_description


def its_a_sports_season(wditem, claimstr=''):
    # ---
    # LNKsport=wditem.get('claims',{}).get('P3450')[0].get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id','')#.getTarget()
    # ---
    myclaim = 'P3450'
    # ---
    pp = wditem.get('claims', {}).get(myclaim, [])
    if claimstr.strip() == '':
        # ---
        for x in pp:
            LNKitem = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
            if claimstr == '':
                claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    # ---
    shortstr = 'موسم رياضي'
    # ---
    if pp == []:
        printe.output("its_a_sports_season item has no %s claims.." % myclaim)
    # ---
    if claimstr == '':
        return shortstr
    # ---
    laste = 'موسم من %s' % claimstr
    # ---
    printe.output("its_a_sports_season:(%s)" % laste)
    # ---
    return laste


def its_songs(type_of_item, wditem, shortstr, claimstr=''):
    # my_description = its_a_generalthing( wditem , da , '%s من أداء ' % da ,'P175')
    myclaim = 'P175'
    # ---
    # songs_type
    # ---
    laste = shortstr
    # ---
    P175 = wditem.get('claims', {}).get(myclaim, [])
    # ---
    if claimstr == '':
        # ---
        for x in P175:
            LNKitem = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
            claimstr = Get_label(LNKitem)
            printe.output(f"claimstr of {LNKitem}=[{claimstr}]")
            if claimstr != '':
                if len(P175) > 1:
                    claimstr += ' وآخرون'
                break
        # ---
        if P175 == []:
            printe.output("its_songs item has no P175 claims..")
    # ---
    claimstr = claimstr.strip()
    # ---
    if claimstr != '':
        laste = f'{shortstr.strip()} من أداء {claimstr}'
    # ---
    sooo = [
        'Q1573906',  # جولة موسيقية
        'Q182832',  # حفلة موسيقية
    ]
    # ---
    if claimstr == '' and type_of_item in sooo:
        # ---
        LNKdirector = wditem.get('claims', {}).get('P57', [])
        # ---
        directorname = ''
        # ---
        for x in LNKdirector:
            LNKitem = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
            directorname = Get_label(LNKitem)
            if directorname != '':
                break
        # ---
        if directorname != '':
            laste = f'{shortstr} من إخراج {directorname}'
    # ---
    printe.output("its_songs:(%s)" % laste)
    # ---
    return laste


def its_a_p50(type_of_item, wditem, shortstr, claimstr=''):
    myclaim = 'P50'
    # ---
    P136 = wditem.get('claims', {}).get('P136', [{}])[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
    if P136 == 'Q8261' and shortstr == 'عمل أدبي':
        shortstr = 'رواية'
    # ---
    P50 = wditem.get('claims', {}).get(myclaim, [])
    # ---
    if claimstr == '':
        # ---
        for x in P50:
            LNKitem = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
            if claimstr == '':
                claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    # ---
    # if claimstr == '': return shortstr
    if claimstr == '':
        return ''
    # ---
    jjj = [
        "كتاب",
        "عمل أدبي",
        "رواية",
        "كتاب هزلي",
        "قصة",
        "قصة قصيرة",
    ]
    # ---
    sus = 'بواسطة'
    # ---
    if shortstr.strip() in jjj:
        sus = 'من تأليف'
    elif shortstr.strip().find("مقالة") != -1:
        sus = 'كتبها'
    # ---
    laste = f'{shortstr.strip()} {sus} {claimstr}'
    if len(P50) > 1:
        laste = f'{shortstr.strip()} {sus} {claimstr} وآخرون'
    # ---
    # laste = laste.replace("كوكبة  ","كوكبة ")
    # ---
    printe.output("its_a_p50:(%s)" % laste)
    return laste


def its_a_thing_located_in_country(wditem, countryname, thing):
    if 'P131' in wditem.get('claims', {}):
        LNKcommunity = wditem.get('claims', {}).get('P131')[0].get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')  # .getTarget()
        label = Get_label(LNKcommunity)
        if label != '':
            return thing + ' في ' + label + '، ' + countryname
        else:
            return thing + ' في ' + countryname
    return thing + ' في ' + countryname


def its_a_film(wditem):
    # ---
    directorname = ''
    # ---
    P57 = wditem.get('claims', {}).get('P57', [])
    # ---
    print("len of P57: %d" % len(P57))
    # ---
    for x in P57:
        q = x.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
        directorname = Get_label(q)
        printe.output(f"directorname of {q}=[{directorname}]")
        if directorname != '':
            if len(P57) > 1:
                directorname += ' وآخرون'
            break
    # ---
    if directorname != '':
        return 'فيلم من إخراج %s' % directorname
    # ---
    return ''


def Make_others_desc(lng, wditem, type_of_item, orig_desc, claimstr=''):
    my_description = ''
    # ---
    # printe.output( "Make others desc:P31:%s" % type_of_item )
    # ---
    if type_of_item == 'Q13417250':  # a
        if orig_desc in ['']:
            my_description = 'مقاطعة في أذربيجان'
    # ---
    elif type_of_item in ['Q1983062', 'Q21191270']:  # حلقة مسلسل تلفزيوني
        my_description = its_an_episode(lng, wditem)
    # ---
    elif type_of_item == 'Q11424':  # film uit P495 (P577)
        if orig_desc in ['', 'فيلم']:
            my_description = its_a_film(wditem)
    # ---
    elif type_of_item in bldiat:
        my_description = its_a_thing_located_in_country(wditem, bldiat[type_of_item], 'بلدية')
        if my_description in ['بلدية', '']:
            my_description = 'بلدية في %s' % bldiat[type_of_item]
    # ---
    # أغاني وألبومات صوتية وما شابهه
    elif type_of_item in songs_type:
        da = songs_type[type_of_item]
        if orig_desc in [da, '']:
            my_description = its_songs(type_of_item, wditem, da, claimstr=claimstr)
    # ---
    elif type_of_item == 'Q79007':
        if orig_desc in ['شارع', '']:
            my_description = its_something_in_an_entity(wditem, 'شارع في')
    # ---
    elif type_of_item in Geo_entity:
        labr = Geo_entity[type_of_item]
        if orig_desc in [labr, '']:
            my_description = its_something_in_an_entity(wditem, '%s في' % labr)
    # ---
    elif type_of_item == 'Q8502':  # a جبل
        if orig_desc in ['جبل', '']:
            my_description = its_something_in_an_entity(wditem, 'جبل في')
    # ---

    elif type_of_item == 'Q484170':  # بلدية في فرنسا
        my_description = its_something_in_a_country(wditem, 'بلدية')
    # ---
    elif (type_of_item == 'Q262166') or (type_of_item == 'Q22865'):  # بلدية في ألمانيا
        my_description = its_something_in_a_country(wditem, 'بلدية')
    # ---
    elif type_of_item == 'Q747074':  # Italian communiity
        my_description = its_something_in_a_country(wditem, 'بلدية')
    # ---
    elif type_of_item == 'Q5398426':  # tv_series
        my_description = its_something_in_a_country(wditem, 'مسلسل تلفزيوني')
    # ---
    elif type_of_item == 'Q45382':
        if orig_desc in ['انقلاب', '']:
            my_description = its_something_in_a_country(wditem, 'انقلاب')
    # ---
    elif type_of_item == 'Q43229':  # organisation
        if orig_desc in ['منظمة', '']:
            my_description = its_something_in_a_country(wditem, 'منظمة')
    # ---
    elif type_of_item == 'Q46970':  # شركة طيران uit P17
        if orig_desc in ['شركة طيران', '']:
            my_description = its_something_in_a_country(wditem, 'شركة طيران')
    # ---
    elif ((type_of_item == 'Q783794') or (type_of_item == 'Q4830453')):
        my_description = its_something_in_a_country(wditem, 'شركة')
    # ---
    elif type_of_item == 'Q532':  # dorp in P17
        if orig_desc in ['قرية', '']:
            my_description = its_something_in_a_country(wditem, 'قرية')
    # ---
    elif type_of_item == 'Q4022':
        if orig_desc in ['نهر', '']:
            my_description = its_something_in_a_country(wditem, 'نهر')
    # ---
    elif type_of_item == 'Q15416':  # برنامج تلفزيوني
        if orig_desc in ['برنامج تلفزيوني', '']:
            my_description = its_something_in_a_country(wditem, 'برنامج تلفزيوني')
    # ---
    elif type_of_item in others_list:
        labr = others_list[type_of_item]['ar']
        if orig_desc in [labr, '']:
            my_description = its_something_in_a_country(wditem, labr)
            if type_of_item in qura and my_description in [qura[type_of_item]['P31'], '']:
                my_description = '{} في {}'.format(qura[type_of_item]['P31'], qura[type_of_item]['P17'])
    # ---
    if my_description == '':
        return my_description
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", '', my_description.lower())
    if test.lower() != my_description.lower():
        my_description = ''
        printe.output(f'test:[{test}] != my_description[{my_description}]')
    # ---
    # printe.output('Make others desc:[%s]' % my_description )
    # ---
    return my_description


# ---
str_descs = {
    'Q1149652': {
        "org": ['', 'district'],
        "desc": 'district in India',
    },
    # ---
    'Q2154519': {
        "org": ['', ''],
        "desc": 'bron van astrofysische röntgenstraling',
    },
    # ---
    'Q67206701': {
        "org": ['', ''],
        "desc": 'ver-liggend infrarood object',
    },
    # ---
    'Q189004': {
        "org": ['', ''],
        "desc": 'onderwijsinstelling',
    },
    # ---
    'Q17633526': {
        "org": ['', ''],
        "desc": 'Wikinews-artikel',
    },
    # ---
    'Q4592255': {
        "org": ['', ''],
        "desc": 'project sub-pagina',
    },
    # ---
    'Q21278897': {
        "org": ['', ''],
        "desc": 'Wiktionary-doorverwijzing',
    },
    # ---
    'Q737498': {
        "org": ['tijdschrift', ''],
        "desc": 'academisch tijdschrift',
    },
    # ---
    'Q24764': {
        "org": ['gemeente', ''],
        "desc": 'Filipijnse gemeente',
    },
    # ---
    'Q70208': {
        "org": ['gemeente', ''],
        "desc": 'Zwitserse gemeente',
    },
    # ---
    'Q203300': {
        "org": ['gemeente', ''],
        "desc": 'gemeente in Liechtenstein',
    },
    # ---
    'Q53764738': {
        "org": ['', ''],
        "desc": 'Chinees karakter',
    },
    # ---
    'Q30612': {
        "org": ['klinisch onderzoek', ''],
        "desc": 'klinisch onderzoek',
    },
    # ---
    'Q2996394': {
        "org": ['x', ''],
        "desc": 'biologisch proces',
    },
    # ---
    'Q14860489': {
        "org": ['y', ''],
        "desc": 'moleculaire functie',
    },
    # ---
    'Q5058355': {
        "org": ['z', ''],
        "desc": 'cellulaire component',
    },
    # ---
    'Q101352': {
        "org": ['', ''],
        "desc": 'achternaam',
    },
    # ---
    'Q4167836': {
        "org": ['', 'categorie', 'Categorie', 'category'],
        "desc": 'Wikimedia-categorie',
    },
    # ---
    'Q13442814': {
        "org": ['artikel', ''],
        "desc": 'wetenschappelijk artikel',
    },
    # ---
    'Q5864': {
        "org": ['geile dwerg', ''],
        "desc": 'gele dwerg',
    },
    # ---
    'Q50231': {
        "org": ['bestuurlijk gebied', 'gebied', ''],
        "desc": 'bestuurlijk gebied in China',
    },
    # ---
    'Q41710': {
        "org": ['', ''],
        "desc": 'etnische groep',
    },
    # ---
    'Q11446': {
        "org": ['', ''],
        "desc": 'schip',
    },
    # ---
    'Q5153359': {
        "org": ['', ''],
        "desc": 'gemeente in Tsjechië',
    },
    # ---
    'Q1131296': {
        "org": ['', ''],
        "desc": 'freguesia in Portugal',
    },
    # ---
    'Q3966183': {
        "org": ['Pokemonwezen', 'Pokémon-wezen', 'Pokemon', 'Pokémon', ''],
        "desc": 'Pokémonwezen',
    },
    # ---
    'Q618779': {
        "org": ['onderscheiding', ''],
        "desc": 'onderscheiding',
    },
    # ---
    'Q197': {
        "org": ['', 'vliegtuig'],
        "desc": 'vliegtuig',
    },
    # ---
    'Q2590631': {
        "org": ['', ''],
        "desc": 'gemeente in Hongarije',
    },
    # ---
    'Q3024240': {
        "org": ['', ''],
        "desc": 'historisch land',
    },
    # ---
    'Q11173': {
        "org": ['chemische stof', 'chemische samenstelling', ''],
        "desc": 'chemische verbinding',
    },
    # ---
    'Q79529': {
        "org": ['chemische samenstelling', 'chemische verbinding'],
        "desc": 'chemische stof',
    },
    # ---
    'Q11266439': {
        "org": ['', 'template', 'sjabloon'],
        "desc": 'Wikimedia-sjabloon',
    },
    # ---
    'Q310890': {
        "org": ['taxon', ''],
        "desc": 'monotypische taxon',
    },
    # ---
    'Q877358': {
        "org": ['resolutie', ''],
        "desc": 'resolutie van de Veiligheidsraad van de Verenigde Naties',
    },
    # ---
    'Q3192808': {
        "org": ['commune', ''],
        "desc": 'commune in Madagascar',
    },
    # ---
    'Q18536594': {
        "org": ['sportevenement', ''],
        "desc": 'sportevenement op de Olympische Spelen',
    },
}


def make_nn(lng, wditem, p31, orig_desc):
    # ---
    desc = ''
    # ---
    if str_descs.get(p31):
        if orig_desc in str_descs[p31]["org"]:
            desc = str_descs[p31]["desc"]
            return desc
    # ---
    if p31 == 'Q18340514':
        desc = 'مقالة عن أحداث في سنة أو فترة زمنية محددة'
    # ---
    elif p31 == 'Q1539532':
        desc = 'موسم نادي رياضي'
    # ---
    if p31 == 'Q207628':
        if orig_desc in ['compositie', '']:
            desc = its_a_composition(lng, wditem)
    # ---
    elif p31 == 'Q273057':
        if orig_desc in ['', 'discografie']:
            desc = its_a_discography(lng, wditem)
    # ---
    elif p31 == 'Q95074':
        if orig_desc in ['personage', '']:
            desc = its_a_fictional_character(wditem)
    # ---
    elif p31 == 'Q3508250':
        if orig_desc in ['', '']:
            desc = its_a_headquarted_thing(lng, wditem, 'syndicat intercommunal in')
    # ---
    elif p31 == 'Q732577':
        if orig_desc in ['publicatie', '']:
            desc = its_a_publication(wditem)
    # ---
    elif p31 == 'Q1077097':
        if orig_desc in ['tambon', '']:
            desc = its_a_tabon_in_thailand(lng, wditem)
    # ---
    elif p31 == 'Q16521':
        if orig_desc in ['', '']:
            desc = its_a_taxon(lng, wditem)
    # ---
    elif p31 == 'Q253019':
        if orig_desc in ['', 'ortsteil', 'plaats in duitsland']:
            desc = its_a_thing_located_in_country(wditem, 'Duitsland', 'ortsteil')
    # ---
    elif p31 == 'Q2635894':
        if orig_desc in ['hoorspel', '']:
            desc = its_an_audio_drama(wditem)
    # ---
    elif p31 == 'Q4167410':
        if orig_desc in ['', 'dp', 'doorverwijzing', 'doorverwijspagina']:
            desc = its_disambigue(lng, wditem)
    # ---
    elif p31 in ['Q515', 'Q5119', 'Q1549591', 'Q3957']:
        desc = its_something_in_a_country(wditem, 'stad')
    # ---
    entities = {
        'Q106259': {
            "org": ['polder', ''],
            "desc": 'polder in',
        },
        'Q106658': {
            "org": ['landkreis', ''],
            "desc": 'Landkreis in',
        },
        'Q126807': {
            "org": ['kleuterschool', 'school', ''],
            "desc": 'kleuterschool in',
        },
        'Q127448': {
            "org": ['gemeente', 'zweedse gemeente'],
            "desc": 'Zweedse gemeente in',
        },
        'Q13005188': {
            "org": ['', 'mandal', 'mandal in India'],
            "desc": 'mandal in',
        },
        'Q166735': {
            "org": ['broekbos', ''],
            "desc": 'broekbos in',
        },
        'Q1690211': {
            "org": ['', ''],
            "desc": 'openbare wasplaats in',
        },
        'Q2042028': {
            "org": ['kloof', ''],
            "desc": 'kloof in',
        },
        'Q26703203': {
            "org": ['stolperstein', ''],
            "desc": 'stolperstein in',
        },
        'Q30198': {
            "org": ['', 'uitstekend landdeel', 'meers', 'moeras'],
            "desc": 'moeras in',
        },
        'Q3184121': {
            "org": ['gemeente', 'gemeente in brazilie', 'gemeente in brazilië', ''],
            "desc": 'gemeente in',
        },
        'Q3947': {
            "org": ['woonhuis', ''],
            "desc": 'woonhuis in',
        },
        'Q41176': {
            "org": ['gebouw', 'bouwwerk', ''],
            "desc": 'gebouw in',
        },
        'Q5084': {
            "org": ['gehucht', ''],
            "desc": 'gehucht in',
        },
        'Q5358913': {
            "org": ['', ''],
            "desc": 'Japanse basisschool in',
        },
        'Q5783996': {
            "org": ['cottage', ''],
            "desc": 'cottage in',
        },
        'Q659103': {
            "org": ['gemeente in Roemenie', 'gemeente in Roemenië', 'gemeente', ''],
            "desc": 'gemeente in',
        },
        'Q7075': {
            "org": ['bibliotheek', ''],
            "desc": 'bibliotheek in',
        },
        'Q735428': {
            "org": ['gemeente', ''],
            "desc": 'gemeente in',
        },
        'Q751876': {
            "org": ['kasteel', ''],
            "desc": 'kasteel in',
        },
        'Q811979': {
            "org": ['bouwwerk', ''],
            "desc": 'bouwwerk in',
        },
        'Q88965416': {
            "org": ['', ''],
            "desc": 'Zweedse schooleenheid in',
        },
        'Q953806': {
            "org": ['bushalte', ''],
            "desc": 'bushalte in',
        },
        'Q9842': {
            "org": ['basisschool', 'basisschool in italië', ''],
            "desc": 'basisschool in ',
        },
    }
    # ---
    if entities.get(p31):
        p31_tab = entities[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_something_in_an_entity(wditem, p31_tab["desc"])
    # ---
    countries = {
        'Q102496': {
            "org": ['parochie', ''],
            "desc": 'parochie',
        },
        'Q11812394': {
            "org": ['', 'theaterbedrijf'],
            "desc": 'theaterbedrijf',
        },
        'Q13141064': {
            "org": ['', 'badmintonner', 'badmintonspeler', ''],
            "desc": 'badmintonspeler',
        },
        'Q14659': {
            "org": ['heraldisch wapen', ''],
            "desc": 'wapen',
        },
        'Q15081032': {
            "org": ['motorfietsmerk', ''],
            "desc": 'motorfietsmerk',
        },
        'Q15991303': {
            "org": ['voetbalcompetitie', ''],
            "desc": 'voetbalcompetitie',
        },
        'Q165': {
            "org": ['zee', ''],
            "desc": 'zee',
        },
        'Q16970': {
            "org": ['kerkgebouw', ''],
            "desc": 'kerkgebouw',
        },
        'Q178561': {
            "org": ['veldslag', ''],
            "desc": 'veldslag',
        },
        'Q180684': {
            "org": ['conflict', ''],
            "desc": 'conflict',
        },
        'Q2065704': {
            "org": ['', 'kantongerecht', 'kantongerecht in noorwegen'],
            "desc": 'kantongerecht',
        },
        'Q23397': {
            "org": ['meer', ''],
            "desc": 'meer',
        },
        'Q23442': {
            "org": ['eiland', ''],
            "desc": 'eiland ',
        },
        'Q23925393': {
            "org": ['douar', ''],
            "desc": 'douar',
        },
        'Q2526255': {
            "org": ['filmregisseur', '', 'regisseur'],
            "desc": 'filmregisseur',
        },
        'Q2912397': {
            "org": ['eendaagse wielerwedstrijd', ''],
            "desc": 'eendaagse wielerwedstrijd ',
        },
        'Q34442': {
            "org": ['weg', 'straat', 'straat in', ''],
            "desc": 'weg',
        },
        'Q34763': {
            "org": ['schiereiland', ''],
            "desc": 'schiereiland ',
        },
        'Q355304': {
            "org": ['', 'watergang'],
            "desc": 'watergang ',
        },
        'Q3914': {
            "org": ['school', ''],
            "desc": 'school',
        },
        'Q55659167': {
            "org": ['', 'natuurlijke waterloop'],
            "desc": 'natuurlijke waterloop',
        },
        'Q57733494': {
            "org": ['', 'badmintoernooi'],
            "desc": 'badmintontoernooi',
        },
        'Q742421': {
            "org": ['', 'theatergezelschap'],
            "desc": 'theatergezelschap',
        },
        'Q985488': {
            "org": ['bewonersgemeenschap', ''],
            "desc": 'bewonersgemeenschap',
        },
    }
    # ---
    if countries.get(p31):
        p31_tab = countries[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_something_in_a_country(wditem, p31_tab["desc"])
    # ---
    genese = {
        'Q1002697': {
            "org": ['periodiek', ''],
            "desc": '',
            "desc_in": 'periodiek over',
            "pid": 'P641',
        },
        'Q1004': {
            "org": ['stripverhaal', ''],
            "desc": 'stripverhaal',
            "desc_in": 'stripverhaal من سلسلة ',
            "pid": 'P179',
        },
        'Q1344': {
            "org": ['opera', ''],
            "desc": 'opera',
            "desc_in": 'opera van ',
            "pid": 'P86',
        },
        'Q14406742': {
            "org": ['stripreeks', ''],
            "desc": 'stripreeks',
            "desc_in": 'stripreeks door ',
            "pid": 'P50',
        },
        'Q178122': {
            "org": ['aria', ''],
            "desc": 'aria',
            "desc_in": 'aria van ',
            "pid": 'P86',
        },
        'Q21014462': {
            "org": ['cellijn', ''],
            "desc": '',
            "desc_in": 'cellijn van een ',
            "pid": 'P703',
        },
        'Q2668072': {
            "org": ['', ''],
            "desc": 'collectie',
            "desc_in": 'collectie uit ',
            "pid": 'P195',
        },
        'Q4502142': {
            "org": ['visueel kunstwerk', ''],
            "desc": 'visueel kunstwerk',
            "desc_in": 'visueel kunstwerk in collectie ',
            "pid": 'P195',
        },
        'Q50386450': {
            "org": ['opera-personage', ''],
            "desc": 'opera-personage',
            "desc_in": 'opera-personage uit ',
            "pid": 'P1441',
        },
        'Q5633421': {
            "org": ['', 'tijdschrift', 'wetenschappelijk tijdschrift'],
            "desc": '',
            "desc_in": 'wetenschappelijk tijdschrift van ',
            "pid": 'P123',
        },
        'Q6451276': {
            "org": ['CSR-rapport', ''],
            "desc": 'CSR-rapport',
            "desc_in": 'CSR-rapport over ',
            "pid": 'P921',
        },
    }
    # ---
    if genese.get(p31):
        p31_tab = genese[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_a_generalthing(wditem, p31_tab["desc"], p31_tab["desc_in"], p31_tab["pid"])
    # ---
    return desc


def action_one_item(lngr, q, item={}, claimstr=''):
    global items2do
    global totaledits
    wditem = himoBOT2.Get_Item_API_From_Qid(q, sites='', titles='', props='')
    items_written = items_found = 0
    lng = 'ar'
    my_description = ''
    orig_desc = get_lng_description(lng, wditem).lower()
    # ---
    if 'org' in sys.argv:
        orig_desc = ''
    # ---
    en_description = get_lng_description('en', wditem)
    printe.output(f"orig_desc:{orig_desc},en_description:{en_description}")
    claims = wditem['claims']
    items2do -= 1
    # ---
    if 'P31' not in claims:
        return
    # ---
    type_ids = claims.get('P31', {})
    # ---
    for type_id in type_ids:
        # ---
        type_of_item = type_id.get('mainsnak', {}).get('datavalue', {}).get('value', {}).get('id', '')
        # ---
        if type_of_item in railway_tables:
            Make_railway_desc(wditem, type_of_item)
            return items_found, items_written
        # ---
        printe.output('Type: [%s]' % type_of_item)
        # ---
        if type_of_item != '':
            if type_of_item == 'Q7604686':
                my_description = "صك قانوني في المملكة المتحدة"
            # ---
            elif type_of_item == 'Q7604693':
                my_description = "قواعد قانونية في أيرلندا الشمالية"
            # ---
            elif type_of_item == 'Q3231690':
                if orig_desc in ['طراز سيارة', '']:
                    my_description = its_a_generalthing(wditem, '', 'طراز سيارة من إنتاج', 'P176', claimstr=claimstr)
                    # ---
            elif type_of_item == 'Q571':
                if orig_desc in ['', 'كتاب']:
                    my_description = its_a_generalthing(wditem, '', 'كتاب من تأليف', 'P50')
            # ---
                '''
          elif type_of_item == 'Q3331189':
            if orig_desc in ['طبعة',''] :
              my_description = its_a_generalthing( wditem , 'طبعة', '' , 'P629' )
              if my_description == 'طبعة' :
                my_description  = ''
          '''
            # ---
            elif type_of_item == 'Q27020041':  # موسم رياضي
                if orig_desc in ['موسم رياضي', '']:
                    my_description = its_a_sports_season(wditem, claimstr=claimstr)
            # ---
            elif type_of_item == 'Q3863':  # كويكب
                if orig_desc in ['']:
                    my_description = 'كويكب'
            # ---
            elif type_of_item == 'Q7889':  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
                if orig_desc in ['لعبة فيديو', '']:
                    my_description = its_a_computergame(lng, wditem)
            # ---
            # ---
            # ---
            # ---
            # ---
            elif type_of_item in space_list_and_other:
                my_description = Make_space_desc(lng, wditem, type_of_item, orig_desc, claimstr=claimstr)
            # ---
            elif type_of_item in others_list or type_of_item in others_list_2:
                my_description = Make_others_desc(lng, wditem, type_of_item, orig_desc, claimstr=claimstr)
            # ---
            elif type_of_item == 'سلالة كلب':  # hondenras
                if orig_desc in ['سلالة', '']:
                    my_description = 'سلالة كلب'
            # ---
            elif type_of_item == 'Q215380':  # muziekband
                if orig_desc in ['طاقم موسيقي', '']:
                    my_description = its_something_in_a_country(wditem, 'طاقم موسيقي')
            # ---
            elif type_of_item == 'Q184188':  # كانتون فرنسي
                my_description = its_canton_of_France(wditem)
            # ---
            elif type_of_item in Qid_Descraptions:
                my_description = Qid_Descraptions[type_of_item].get('ar', '')
            # ---
            elif type_of_item == 'Q7930614':
                if orig_desc in ['قرية', '', 'قرية في تايوان']:
                    my_description = its_something_in_an_entity(wditem, 'قرية في')
                    if my_description in ['']:
                        my_description = 'قرية في تايوان'
            # ---
            elif type_of_item == 'Q56436498 xxx':
                if orig_desc in ['قرية', '', 'قرية في الهند']:
                    my_description = its_something_in_an_entity(wditem, 'قرية في')
                    if (my_description in ['', ' ']):
                        my_description = 'قرية في الهند'
        # ---
        if my_description == 'sds':
            my_description = make_nn(lng, wditem, type_of_item, orig_desc)
        # ---
        my_description = re.sub(r"\s+", " ", my_description)
        my_description = my_description.strip()
        # ---
        if my_description == '':
            printe.output(f'type of item: {type_of_item}, orig_desc: [{orig_desc}], new: [{my_description}]')
            continue
        # ---
        if my_description.find('n/a') != -1:
            continue
        # ---
        if my_description == orig_desc:
            continue
        # ---
        if my_description == "جين في إنسان عاقل":
            my_description = "جين من أنواع جينات الإنسان العاقل"
        # ---
        data = {}
        data.update({
            'descriptions': {
                lng: {
                    'language': lng,
                    'value': my_description
                }
            }
        })
        # ---
        items_written += 1
        # ---
        valuee = data['descriptions'][lng]['value']
        valuee = valuee.replace(',', '،')
        test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", '', valuee.lower())
        # ---
        if test.lower() == valuee.lower():
            Add_desc(q, valuee, data['descriptions'][lng]['language'])
            totaledits += 1
            items_found += 1
            break
        else:
            printe.output(f'test:[{test}] != value[{valuee}]')
        # ---
    # ---
    return items_found, items_written


# ---

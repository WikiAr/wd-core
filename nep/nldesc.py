#!/usr/bin/python3
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.
# Q13005188 mandal
"""

"""

import re
import sys

# ---
from API import printe
from wd_api import himoAPI
from wd_api import wd_bot

# ---
from desc_dicts.descraptions import Qid_Descraptions
from des.railway import railway_tables, work_railway

# ---
from nep.tables.lists import (
    bldiat,
    Space_tab,
    p50s,
    songs_type,
    others_list,
    others_list_2,
    space_list_and_other,
    qura,
    Geo_entity,
)
from nep.tables.str_descs import descs, entities, countries, genese
from nep.bots.helps import (
    get_female_for_p17,
    Get_label,
    get_label_txt,
    Get_label_from_item,
    get_mainsnak,
)
from nep.its import (
    its_a_composition,
    its_a_computergame,
    its_a_discography,
    its_a_fictional_character,
    its_a_film,
    its_a_generalthing,
    its_a_headquarted_thing,
    its_a_p50,
    its_a_publication,
    its_a_sports_season,
    its_a_tabon_in_thailand,
    its_a_taxon,
    its_a_thing_located_in_country,
    its_an_audio_drama,
    its_an_episode,
    its_canton_of_France,
    its_something_in_a_country,
    its_something_in_an_entity,
    its_songs,
)

# ---
items2do = 0  # global parameter to print progress
totaledits = 0
lng_canbeused = [
    "en",
    "de",
    "fr",
    "it",
    "es",
    "pt",
    "ca",
    "dk",
    "cs",
    "hr",
    "nl",
    "ro",
    "sh",
    "vi",
    "eo",
    "simple",
    "eu",
    "zea",
    "li",
    "fy",
    "oc",
    "af",
    "nb",
    "no",
    "pl",
    "si",
    "sv",
    "wa",
]
# ---
sparqler = {1: ""}
Offq = {1: 0}
Off = {1: 0}
limit = {1: 0}
# ---
totallimit = {1: 10000}
# ---
for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg.startswith("-"):
        arg = arg[1:]
    # ---
    if arg == "off":
        Off[1] = int(value)
        printe.output("Off[1] = %d" % Off[1])
    # ---
    if arg == "offq":
        Offq[1] = int(value)
        printe.output("Offq[1] = %d" % Offq[1])
    # ---
    if arg in ["totallimit", "all"]:
        totallimit[1] = int(value)
        printe.output("totallimit[1] = %d" % totallimit[1])
    # ---
    if arg == "limit":
        limit[1] = int(value)
        printe.output("limit[1] = %d" % limit[1])
    # ---
    if arg == "sparql":
        sparqler[1] = value
        printe.output(f'sparqler[1] = "{sparqler[1]}"')
# ---


def Make_railway_desc(wditem, p31):
    # ---
    return work_railway(wditem, p31)


def action_one_P131_item(lng, oneitem):
    global totaledits
    if lng in oneitem.get("descriptions", {}):
        nld = oneitem.get("descriptions", {}).get(lng, "")
    else:
        nld = ""
    if lng in oneitem.get("labels", {}):
        oneitem.get("labels", {}).get(lng, "")
    adminname = ""
    isaname = ""
    countryname = ""
    if "P31" in oneitem.get("claims", {}):
        LNKisa = get_mainsnak(oneitem.get("claims", {}).get("P31")[0])  # .getTarget()
        if LNKisa is not None:
            isa = wd_bot.Get_Item_API_From_Qid(LNKisa)  # xzo
            if lng in isa.get("labels", {}):
                isaname = isa.get("labels", {}).get(lng, "")

    shortname = "قرية" if isaname in ["dorp in China"] else isaname
    if "P131" in oneitem.get("claims", {}):
        LNKadmin = get_mainsnak(
            oneitem.get("claims", {}).get("P131")[0]
        )  # .getTarget()
        if LNKadmin is not None:
            admin = wd_bot.Get_Item_API_From_Qid(LNKadmin)  # xzo
            if lng in admin.get("labels", {}):
                adminname = admin.get("labels", {}).get(lng, "")
    if "P17" in oneitem.get("claims", {}):
        LNKcountry = get_mainsnak(
            oneitem.get("claims", {}).get("P17")[0]
        )  # .getTarget()
        if LNKcountry is not None:
            country = wd_bot.Get_Item_API_From_Qid(LNKcountry)  # xzo
            if lng in country.get("labels", {}):
                countryname = country.get("labels", {}).get(lng, "")
    data = {}
    found = False
    if lng not in oneitem.get("labels", {}):
        if lng != "ar":
            for plang in lng_canbeused:
                if (plang in oneitem.get("labels", {})) and not found:
                    data["labels"] = {lng: oneitem.get("labels", {}).get(plang, "")}
                    found = True
    if not adminname:
        newdescription = f"{isaname}"
    else:
        newdescription = f"{shortname} in {adminname}, {countryname}"
    if (isaname != "") and (
        nld in ["", "قرية", "dorp in China", "gemeente", "gemeente in China"]
    ):
        data["descriptions"] = {lng: newdescription}
    # ---
    try:
        oneitem.editEntity(
            data,
            summary="nl-description, [[User:Edoderoobot/Set-nl-description|python code]], logfile on https://goo .gl/BezTim",
        )
        totaledits += 1
        return 1
    except ValueError:
        print("ValueError occured on %s", oneitem.title())
    except BaseException:
        print("Undefined error occured on %s-[%s]", oneitem.title(), "simpleP131")
    # ---
    return 0


def Add_desc(q, value, lang):
    himoAPI.Des_API(q, value, lang, ask="")


def Make_space_desc(lng, wditem, type_of_item, orig_desc, claimstr=""):
    my_description = ""
    # ---
    printe.output("Make_space_desc::")
    # ---
    if type_of_item == "Q2467461":
        my_description = "قسم أكاديمي"
    # ---
    elif type_of_item in p50s:
        if orig_desc in ["", "عمل أدبي", p50s[type_of_item]["ar"]]:
            my_description = its_a_p50(
                type_of_item, wditem, p50s[type_of_item]["ar"], claimstr=claimstr
            )
    # ---
    elif (
        type_of_item == "Q7889"
    ):  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
        if orig_desc in ["لعبة فيديو", ""]:
            my_description = its_a_computergame(lng, wditem)
    # ---
    # Q476028
    elif type_of_item == "Q476028":  # نادي كرة قدم
        if orig_desc in ["نادي كرة قدم"]:
            my_description = its_something_in_a_country(wditem, "نادي كرة قدم")
    # ---
    elif type_of_item == "Q14752149":  # amateur football club
        if orig_desc in ["", "نادي كرة قدم للهواة"]:
            my_description = its_something_in_a_country(wditem, "نادي كرة قدم للهواة")
    # ---
    elif type_of_item == "Q7278":  # political party
        if orig_desc in ["حزب سياسي", ""]:
            my_description = its_something_in_a_country(wditem, "حزب سياسي")
    # ---
    elif type_of_item == "Q265158" and orig_desc in ["", "مراجعة"]:
        my_description = its_a_generalthing(
            wditem, "مراجعة", "مراجعة منشورة في", "P1433"
        )
    # ---
    elif type_of_item == "Q13433827" and orig_desc in ["", "مقالة موسوعية"]:
        my_description = its_a_generalthing(
            wditem, "مقالة موسوعية", "مقالة في", "P1433"
        )
    # ---
    elif type_of_item == "Q191067" and orig_desc in ["مقالة", ""]:
        my_description = its_a_generalthing(wditem, "", "مقالة في ", "P1433")
    # ---
    elif type_of_item == "Q96739634":
        if orig_desc in ["", "حركة فردية"]:
            my_description = its_a_generalthing(
                wditem, "حركة فردية", "حركة فردية بواسطة", "P50"
            )
    # ---
    elif type_of_item == "Q3305213":  # لوحة فنية بواسطة P170
        if orig_desc in ["لوحة فنية", ""]:
            my_description = its_a_generalthing(
                wditem, "لوحة فنية", "لوحة فنية رسمها", "P170"
            )
    # ---
    elif type_of_item == "Q7187":
        if orig_desc in ["جين", ""]:
            my_description = its_a_generalthing(wditem, "", "جين في ", "P703")
    # ---
    # جين كاذب
    elif type_of_item == "Q277338":
        if orig_desc in ["جين كاذب", "جين", "speudogen", ""]:
            my_description = its_a_generalthing(
                wditem, "", "جين كاذب في ", "P703"
            )  # P1057 #fixed
    # ---
    # بروتين
    elif type_of_item == "Q8054":
        if orig_desc in ["بروتين", ""]:
            my_description = its_a_generalthing(wditem, "", "بروتين في ", "P703")
    # ---
    elif type_of_item == "Q783866":
        if orig_desc in ["مكتبة جافا سكريبت", ""]:
            my_description = its_a_generalthing(
                wditem, "مكتبة جافا سكريبت", "مكتبة جافا سكريبت من تطوير ", "P178"
            )
    # ---
    elif type_of_item == "Q620615":  # تطبيق محمول
        if orig_desc in ["تطبيق محمول", ""]:
            my_description = its_a_generalthing(
                wditem, "", "تطبيق محمول من تطوير ", "P178"
            )
    # ---
    elif type_of_item in Space_tab:
        labr = Space_tab[type_of_item]
        if orig_desc in [labr, ""]:
            my_description = its_a_generalthing(wditem, labr, "%s في " % labr, "P59")
    # ---
    elif type_of_item == "Q2831984":  # ألبوم قصص مصورة uit de serie P179
        if orig_desc in ["", "ألبوم قصص مصورة"]:
            my_description = its_a_generalthing(
                wditem, "", "ألبوم قصص مصورة من سلسلة ", "P179"
            )
        if my_description in ["", "ألبوم قصص مصورة"]:
            my_description = its_a_generalthing(
                wditem, "", "ألبوم قصص مصورة من تأليف ", "P50"
            )
    # ---
    elif type_of_item == "Q19389637":
        short = "مقالة سيرة ذاتية"
        if (orig_desc in [short, ""]) or (orig_desc.find(short) == 0):
            printe.output("work in Q19389637")
            # my_description ='biografisch artikel',''
            my_description = its_a_generalthing(
                wditem, short, "مقالة سيرة ذاتية للمؤلف", "P50"
            )
            # ---
            if my_description == short:
                my_description = its_a_generalthing(
                    wditem, short, "مقالة سيرة ذاتية منشورة في", "P1433"
                )
            # ---
            if my_description == short:
                my_description = its_a_generalthing(
                    wditem, short, "مقالة سيرة ذاتية عن", "P921"
                )
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", my_description.lower())
    if test.lower() != my_description.lower():
        my_description = ""
        printe.output(f"test:[{test}] != my_description[{my_description}]")
    # ---
    printe.output("Make_space_desc:[%s]" % my_description)
    # ---
    return my_description


def Make_others_desc(lng, wditem, type_of_item, orig_desc, claimstr=""):
    my_description = ""
    # ---
    # printe.output( "Make others desc:P31:%s" % type_of_item )
    # ---
    if type_of_item == "Q13417250":  # a
        if orig_desc in [""]:
            my_description = "مقاطعة في أذربيجان"
    # ---
    elif type_of_item in ["Q1983062", "Q21191270"]:  # حلقة مسلسل تلفزيوني
        my_description = its_an_episode(lng, wditem)
    # ---
    elif type_of_item == "Q11424":  # film uit P495 (P577)
        if orig_desc in ["", "فيلم"]:
            my_description = its_a_film(wditem)
    # ---
    elif type_of_item in bldiat:
        my_description = its_a_thing_located_in_country(
            wditem, bldiat[type_of_item], "بلدية"
        )
        if my_description in ["بلدية", ""]:
            my_description = "بلدية في %s" % bldiat[type_of_item]
    # ---
    # أغاني وألبومات صوتية وما شابهه
    elif type_of_item in songs_type:
        da = songs_type[type_of_item]
        if orig_desc in [da, ""]:
            my_description = its_songs(type_of_item, wditem, da, claimstr=claimstr)
    # ---
    elif type_of_item == "Q79007":
        if orig_desc in ["شارع", ""]:
            my_description = its_something_in_an_entity(wditem, "شارع في")
    # ---
    elif type_of_item in Geo_entity:
        labr = Geo_entity[type_of_item]
        if orig_desc in [labr, ""]:
            my_description = its_something_in_an_entity(wditem, "%s في" % labr)
    # ---
    elif type_of_item == "Q8502":  # a جبل
        if orig_desc in ["جبل", ""]:
            my_description = its_something_in_an_entity(wditem, "جبل في")
    # ---

    elif type_of_item == "Q484170":  # بلدية في فرنسا
        my_description = its_something_in_a_country(wditem, "بلدية")
    # ---
    elif (type_of_item == "Q262166") or (type_of_item == "Q22865"):  # بلدية في ألمانيا
        my_description = its_something_in_a_country(wditem, "بلدية")
    # ---
    elif type_of_item == "Q747074":  # Italian communiity
        my_description = its_something_in_a_country(wditem, "بلدية")
    # ---
    elif type_of_item == "Q5398426":  # tv_series
        my_description = its_something_in_a_country(wditem, "مسلسل تلفزيوني")
    # ---
    elif type_of_item == "Q45382":
        if orig_desc in ["انقلاب", ""]:
            my_description = its_something_in_a_country(wditem, "انقلاب")
    # ---
    elif type_of_item == "Q43229":  # organisation
        if orig_desc in ["منظمة", ""]:
            my_description = its_something_in_a_country(wditem, "منظمة")
    # ---
    elif type_of_item == "Q46970":  # شركة طيران uit P17
        if orig_desc in ["شركة طيران", ""]:
            my_description = its_something_in_a_country(wditem, "شركة طيران")
    # ---
    elif (type_of_item == "Q783794") or (type_of_item == "Q4830453"):
        my_description = its_something_in_a_country(wditem, "شركة")
    # ---
    elif type_of_item == "Q532":  # dorp in P17
        if orig_desc in ["قرية", ""]:
            my_description = its_something_in_a_country(wditem, "قرية")
    # ---
    elif type_of_item == "Q4022":
        if orig_desc in ["نهر", ""]:
            my_description = its_something_in_a_country(wditem, "نهر")
    # ---
    elif type_of_item == "Q15416":  # برنامج تلفزيوني
        if orig_desc in ["برنامج تلفزيوني", ""]:
            my_description = its_something_in_a_country(wditem, "برنامج تلفزيوني")
    # ---
    elif type_of_item in others_list:
        labr = others_list[type_of_item]["ar"]
        if orig_desc in [labr, ""]:
            my_description = its_something_in_a_country(wditem, labr)
            if type_of_item in qura and my_description in [
                qura[type_of_item]["P31"],
                "",
            ]:
                my_description = "{} في {}".format(
                    qura[type_of_item]["P31"], qura[type_of_item]["P17"]
                )
    # ---
    if not my_description:
        return my_description
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", my_description.lower())
    if test.lower() != my_description.lower():
        my_description = ""
        printe.output(f"test:[{test}] != my_description[{my_description}]")
    # ---
    # printe.output('Make others desc:[%s]' % my_description )
    # ---
    return my_description


def make_nn(lng, wditem, p31, orig_desc):
    # ---
    desc = ""
    # ---
    if descs.get(p31):
        if orig_desc in descs[p31]["org"]:
            desc = descs[p31]["desc"]
            return desc
    # ---
    if p31 == "Q18340514":
        desc = "مقالة عن أحداث في سنة أو فترة زمنية محددة"
    # ---
    elif p31 == "Q1539532":
        desc = "موسم نادي رياضي"
    # ---
    if p31 == "Q207628":
        if orig_desc in ["compositie", ""]:
            desc = its_a_composition(lng, wditem)
    # ---
    elif p31 == "Q273057":
        if orig_desc in ["", "discografie"]:
            desc = its_a_discography(lng, wditem)
    # ---
    elif p31 == "Q95074":
        if orig_desc in ["personage", ""]:
            desc = its_a_fictional_character(wditem)
    # ---
    elif p31 == "Q3508250":
        if orig_desc in ["", ""]:
            desc = its_a_headquarted_thing(lng, wditem, "syndicat intercommunal in")
    # ---
    elif p31 == "Q732577":
        if orig_desc in ["publicatie", ""]:
            desc = its_a_publication(wditem)
    # ---
    elif p31 == "Q1077097":
        if orig_desc in ["tambon", ""]:
            desc = its_a_tabon_in_thailand(lng, wditem)
    # ---
    elif p31 == "Q16521":
        if orig_desc in ["", ""]:
            desc = its_a_taxon(lng, wditem)
    # ---
    elif p31 == "Q253019":
        if orig_desc in ["", "ortsteil", "plaats in duitsland"]:
            desc = its_a_thing_located_in_country(wditem, "Duitsland", "ortsteil")
    # ---
    elif p31 == "Q2635894":
        if orig_desc in ["hoorspel", ""]:
            desc = its_an_audio_drama(wditem)
    # ---
    elif p31 in ["Q515", "Q5119", "Q1549591", "Q3957"]:
        desc = its_something_in_a_country(wditem, "stad")
    # ---
    if entities.get(p31):
        p31_tab = entities[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_something_in_an_entity(wditem, p31_tab["desc"])
    # ---

    if countries.get(p31):
        p31_tab = countries[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_something_in_a_country(wditem, p31_tab["desc"])
    # ---
    if genese.get(p31):
        p31_tab = genese[p31]
        if orig_desc in p31_tab["org"]:
            desc = its_a_generalthing(
                wditem, p31_tab["desc"], p31_tab["desc_in"], p31_tab["pid"]
            )
    # ---
    return desc


def action_one_item(lngr, q, item={}, claimstr=""):
    global items2do
    global totaledits
    wditem = wd_bot.Get_Item_API_From_Qid(q, sites="", titles="", props="")
    items_written = items_found = 0
    lng = "ar"
    my_description = ""
    orig_desc = wditem.get("descriptions", {}).get(lng, "").lower()
    # ---
    if "org" in sys.argv:
        orig_desc = ""
    # ---
    en_description = wditem.get("descriptions", {}).get("en", "").lower()
    printe.output(f"orig_desc:{orig_desc},en_description:{en_description}")
    claims = wditem["claims"]
    items2do -= 1
    # ---
    if "P31" not in claims:
        return
    # ---
    type_ids = claims.get("P31", {})
    # ---
    for type_id in type_ids:
        # ---
        type_of_item = get_mainsnak(type_id)
        # ---
        if type_of_item in railway_tables:
            Make_railway_desc(wditem, type_of_item)
            return items_found, items_written
        # ---
        printe.output("Type: [%s]" % type_of_item)
        # ---
        if type_of_item:
            if type_of_item == "Q7604686":
                my_description = "صك قانوني في المملكة المتحدة"
            # ---
            elif type_of_item == "Q7604693":
                my_description = "قواعد قانونية في أيرلندا الشمالية"
            # ---
            elif type_of_item == "Q3231690":
                if orig_desc in ["طراز سيارة", ""]:
                    my_description = its_a_generalthing(
                        wditem, "", "طراز سيارة من إنتاج", "P176", claimstr=claimstr
                    )
                    # ---
            elif type_of_item == "Q571":
                if orig_desc in ["", "كتاب"]:
                    my_description = its_a_generalthing(
                        wditem, "", "كتاب من تأليف", "P50"
                    )
                # ---
                """
          elif type_of_item == 'Q3331189':
            if orig_desc in ['طبعة',''] :
              my_description = its_a_generalthing( wditem , 'طبعة', '' , 'P629' )
              if my_description == 'طبعة' :
                my_description  = ''
          """
            # ---
            elif type_of_item == "Q27020041":  # موسم رياضي
                if orig_desc in ["موسم رياضي", ""]:
                    my_description = its_a_sports_season(wditem, claimstr=claimstr)
            # ---
            elif type_of_item == "Q3863":  # كويكب
                if orig_desc in [""]:
                    my_description = "كويكب"
            # ---
            elif (
                type_of_item == "Q7889"
            ):  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
                if orig_desc in ["لعبة فيديو", ""]:
                    my_description = its_a_computergame(lng, wditem)
            # ---
            # ---
            # ---
            # ---
            # ---
            elif type_of_item in space_list_and_other:
                my_description = Make_space_desc(
                    lng, wditem, type_of_item, orig_desc, claimstr=claimstr
                )
            # ---
            elif type_of_item in others_list or type_of_item in others_list_2:
                my_description = Make_others_desc(
                    lng, wditem, type_of_item, orig_desc, claimstr=claimstr
                )
            # ---
            elif type_of_item == "سلالة كلب":  # hondenras
                if orig_desc in ["سلالة", ""]:
                    my_description = "سلالة كلب"
            # ---
            elif type_of_item == "Q215380":  # muziekband
                if orig_desc in ["طاقم موسيقي", ""]:
                    my_description = its_something_in_a_country(wditem, "طاقم موسيقي")
            # ---
            elif type_of_item == "Q184188":  # كانتون فرنسي
                my_description = its_canton_of_France(wditem)
            # ---
            elif type_of_item in Qid_Descraptions:
                my_description = Qid_Descraptions[type_of_item].get("ar", "")
            # ---
            elif type_of_item == "Q7930614":
                if orig_desc in ["قرية", "", "قرية في تايوان"]:
                    my_description = its_something_in_an_entity(wditem, "قرية في")
                    if my_description in [""]:
                        my_description = "قرية في تايوان"
            # ---
            elif type_of_item == "Q56436498 xxx":
                if orig_desc in ["قرية", "", "قرية في الهند"]:
                    my_description = its_something_in_an_entity(wditem, "قرية في")
                    if my_description in ["", " "]:
                        my_description = "قرية في الهند"
        # ---
        if my_description == "sds":
            my_description = make_nn(lng, wditem, type_of_item, orig_desc)
        # ---
        my_description = re.sub(r"\s+", " ", my_description)
        my_description = my_description.strip()
        # ---
        if not my_description:
            printe.output(
                f"type of item: {type_of_item}, orig_desc: [{orig_desc}], new: [{my_description}]"
            )
            continue
        # ---
        if my_description.find("n/a") != -1:
            continue
        # ---
        if my_description == orig_desc:
            continue
        # ---
        if my_description == "جين في إنسان عاقل":
            my_description = "جين من أنواع جينات الإنسان العاقل"
        # ---
        data = {}
        data.update({"descriptions": {lng: {"language": lng, "value": my_description}}})
        # ---
        items_written += 1
        # ---
        valuee = data["descriptions"][lng]["value"]
        valuee = valuee.replace(",", "،")
        test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", valuee.lower())
        # ---
        if test.lower() == valuee.lower():
            Add_desc(q, valuee, data["descriptions"][lng]["language"])
            totaledits += 1
            items_found += 1
            break
        else:
            printe.output(f"test:[{test}] != value[{valuee}]")
        # ---
    # ---
    return items_found, items_written

#!/usr/bin/python3
"""

"""

import re
import sys

# ---
from newapi import printe
from himo_api import himoAPI
from wd_api import wd_bot

# ---
from desc_dicts.descraptions import Qid_Descraptions
from des.railway import railway_tables, work_railway
from nep.space_others import Make_space_desc, Make_others_desc

# ---
from nep.tables.lists import (
    others_list,
    others_list_2,
    space_list_and_other,
)
from nep.tables.str_descs import make_nn
from nep.bots.helps import get_mainsnak
from nep.bots.its import (
    its_a_computergame,
    its_a_generalthing,
    its_a_sports_season,
    its_canton_of_France,
    its_something_in_a_country,
    its_something_in_an_entity,
)

from nep.new_way import P1433_ids, do_P1433_ids, P1433_en_to_qid

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
        LNKadmin = get_mainsnak(oneitem.get("claims", {}).get("P131")[0])  # .getTarget()
        if LNKadmin is not None:
            admin = wd_bot.Get_Item_API_From_Qid(LNKadmin)  # xzo
            if lng in admin.get("labels", {}):
                adminname = admin.get("labels", {}).get(lng, "")
    if "P17" in oneitem.get("claims", {}):
        LNKcountry = get_mainsnak(oneitem.get("claims", {}).get("P17")[0])  # .getTarget()
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
    if (isaname != "") and (nld in ["", "قرية", "dorp in China", "gemeente", "gemeente in China"]):
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
                    my_description = its_a_generalthing(wditem, "", "طراز سيارة من إنتاج", "P176", claimstr=claimstr)
            # ---
            elif type_of_item == "Q571":
                if orig_desc in ["", "كتاب"]:
                    my_description = its_a_generalthing(wditem, "", "كتاب من تأليف", "P50")
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
            elif type_of_item == "Q7889":  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
                if orig_desc in ["لعبة فيديو", ""]:
                    my_description = its_a_computergame(lng, wditem)
            # ---
            # ---
            # ---
            # ---
            # ---
            elif type_of_item in space_list_and_other:
                my_description = Make_space_desc(lng, wditem, type_of_item, orig_desc, claimstr=claimstr)
            # ---
            elif type_of_item in P1433_ids or en_description.lower() in P1433_en_to_qid:
                my_description = do_P1433_ids(wditem, type_of_item, orig_desc)

            # ---
            elif type_of_item in others_list or type_of_item in others_list_2:
                my_description = Make_others_desc(lng, wditem, type_of_item, orig_desc, claimstr=claimstr)
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
            printe.output(f"type of item: {type_of_item}, orig_desc: [{orig_desc}], new: [{my_description}]")
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
    return items_found, items_written

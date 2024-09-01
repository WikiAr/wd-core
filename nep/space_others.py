#!/usr/bin/python3
"""
from nep.space_others import Make_space_desc, Make_others_desc
"""

import re

# ---
from newapi import printe
from nep.new_way import P1433_ids, do_P1433_ids

# ---
from nep.tables.lists import (
    bldiat,
    Space_tab,
    p50s,
    songs_type,
    others_list,
    qura,
    Geo_entity,
)
from nep.bots.its import (
    its_a_computergame,
    its_a_film,
    its_a_generalthing,
    its_a_p50,
    its_a_thing_located_in_country,
    its_an_episode,
    its_something_in_a_country,
    its_something_in_an_entity,
    its_songs,
)


def Make_space_desc(lng, wditem, type_of_item, orig_desc, claimstr=""):
    my_description = ""
    # ---
    if type_of_item == "Q2467461":
        my_description = "قسم أكاديمي"
    # ---
    elif type_of_item in P1433_ids:
        my_description = do_P1433_ids(wditem, type_of_item, orig_desc)
        # ---
    elif type_of_item in p50s:
        if orig_desc in ["", "عمل أدبي", p50s[type_of_item]["ar"]]:
            my_description = its_a_p50(type_of_item, wditem, p50s[type_of_item]["ar"], claimstr=claimstr)
    # ---
    elif type_of_item == "Q7889":  # computerspel  genre=P136   ontwikkelaar=P178  uitgeverij=P123
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
    elif type_of_item == "Q96739634":
        if orig_desc in ["", "حركة فردية"]:
            my_description = its_a_generalthing(wditem, "حركة فردية", "حركة فردية بواسطة", "P50")
    # ---
    elif type_of_item == "Q3305213":  # لوحة فنية بواسطة P170
        if orig_desc in ["لوحة فنية", ""]:
            my_description = its_a_generalthing(wditem, "لوحة فنية", "لوحة فنية رسمها", "P170")
    # ---
    elif type_of_item == "Q7187":
        if orig_desc in ["جين", ""]:
            my_description = its_a_generalthing(wditem, "", "جين في ", "P703")
    # ---
    # جين كاذب
    elif type_of_item == "Q277338":
        if orig_desc in ["جين كاذب", "جين", "speudogen", ""]:
            my_description = its_a_generalthing(wditem, "", "جين كاذب في ", "P703")  # P1057 #fixed
    # ---
    # بروتين
    elif type_of_item == "Q8054":
        if orig_desc in ["بروتين", ""]:
            my_description = its_a_generalthing(wditem, "", "بروتين في ", "P703")
    # ---
    elif type_of_item == "Q783866":
        if orig_desc in ["مكتبة جافا سكريبت", ""]:
            my_description = its_a_generalthing(wditem, "مكتبة جافا سكريبت", "مكتبة جافا سكريبت من تطوير ", "P178")
    # ---
    elif type_of_item == "Q620615":  # تطبيق محمول
        if orig_desc in ["تطبيق محمول", ""]:
            my_description = its_a_generalthing(wditem, "", "تطبيق محمول من تطوير ", "P178")
    # ---
    elif type_of_item in Space_tab:
        labr = Space_tab[type_of_item]
        if orig_desc in [labr, ""]:
            my_description = its_a_generalthing(wditem, labr, "%s في " % labr, "P59")
    # ---
    elif type_of_item == "Q2831984":  # ألبوم قصص مصورة uit de serie P179
        if orig_desc in ["", "ألبوم قصص مصورة"]:
            my_description = its_a_generalthing(wditem, "", "ألبوم قصص مصورة من سلسلة ", "P179")
        if my_description in ["", "ألبوم قصص مصورة"]:
            my_description = its_a_generalthing(wditem, "", "ألبوم قصص مصورة من تأليف ", "P50")
    # ---
    elif type_of_item == "Q19389637":
        short = "مقالة سيرة ذاتية"
        if (orig_desc in [short, ""]) or (orig_desc.find(short) == 0):
            printe.output("work in Q19389637")
            # my_description ='biografisch artikel',''
            my_description = its_a_generalthing(wditem, short, "مقالة سيرة ذاتية للمؤلف", "P50")
            # ---
            if my_description == short:
                my_description = its_a_generalthing(wditem, short, "مقالة سيرة ذاتية منشورة في", "P1433")
            # ---
            if my_description == short:
                my_description = its_a_generalthing(wditem, short, "مقالة سيرة ذاتية عن", "P921")
    # ---
    test = re.sub(r"[abcdefghijklmnopqrstuvwxyz]", "", my_description.lower())
    if test.lower() != my_description.lower():
        my_description = ""
        printe.output(f"test:[{test}] != my_description[{my_description}]")
    # ---
    printe.output("Make space desc:[%s]" % my_description)
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
        my_description = its_a_thing_located_in_country(wditem, bldiat[type_of_item], "بلدية")
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
        my_description = its_something_in_an_entity(wditem, "بلدية في")
    # ---
    elif (type_of_item == "Q262166") or (type_of_item == "Q22865"):  # بلدية في ألمانيا
        my_description = its_something_in_an_entity(wditem, "بلدية في")
    # ---
    elif type_of_item == "Q747074":  # Italian communiity
        my_description = its_something_in_an_entity(wditem, "بلدية في")
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
            my_description = its_something_in_an_entity(wditem, "منظمة في")
    # ---
    elif type_of_item == "Q46970":  # شركة طيران uit P17
        if orig_desc in ["شركة طيران", "شركة", ""]:
            my_description = its_something_in_an_entity(wditem, "شركة طيران في")
    # ---
    elif (type_of_item == "Q783794") or (type_of_item == "Q4830453"):
        my_description = its_something_in_an_entity(wditem, "شركة في")
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
            if type_of_item in qura and my_description in [qura[type_of_item]["P31"], ""]:
                my_description = "{} في {}".format(qura[type_of_item]["P31"], qura[type_of_item]["P17"])
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

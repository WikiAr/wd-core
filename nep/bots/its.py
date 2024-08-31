"""
from nep.bots.its import its_a_composition, its_a_computergame, its_a_discography, its_a_fictional_character, its_a_film, its_a_generalthing, its_a_headquarted_thing, its_a_p50, its_a_publication, its_a_sports_season, its_a_tabon_in_thailand, its_a_taxon, its_a_thing_located_in_country, its_an_audio_drama, its_an_episode, its_canton_of_France, its_something_in_a_country, its_something_in_an_entity, its_songs
"""

from newapi import printe
from wd_api import wd_bot
from nep.bots.helps import (
    get_female_for_p17,
    Get_label,
    get_label_txt,
    Get_label_from_item,
    get_mainsnak,
)

def its_a_generalthing(wditem, shortstr, longdescrstr, myclaim, claimstr=""):
    # ---
    pp = wditem.get("claims", {}).get(myclaim, [])
    # ---
    for x in pp:
        LNKitem = get_mainsnak(x)
        if not claimstr:
            claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    if not claimstr:
        return shortstr
    # ---
    laste = f"{longdescrstr.strip()} {claimstr}"
    laste = laste.replace("جين في إنسان عاقل", "جين من أنواع جينات الإنسان العاقل")
    # ---
    printe.output(f"laste:({laste})")
    return laste


def its_something_in_an_entity(wdi, something):
    # 'P131'    #P131
    # 'P17'   #P17
    # ---
    LNKentity = get_mainsnak(wdi.get("claims", {}).get("P131", [{}])[0])  # .getTarget()
    # ---
    if not LNKentity:
        LNKentity = get_mainsnak(wdi.get("claims", {}).get("P159", [{}])[0])
    prnEntity = Get_label(LNKentity) if LNKentity else ""
    # ---
    LNKcountry = get_mainsnak(wdi.get("claims", {}).get("P17", [{}])[0])  # .getTarget()
    prnCountry = Get_label(LNKcountry) if LNKcountry else ""
    # ---
    if prnCountry and prnEntity:
        return f"{something} {prnEntity}، {prnCountry}"
    elif prnCountry:
        return f"{something} {prnCountry}"
    elif prnEntity:
        return f"{something} {prnEntity}"
    # ---
    return ""


def its_something_in_a_country(wdi, something):
    # ---
    printe.output(f"its_something_in_a_country,something:{something}")
    # ---
    prnCountry = ""
    # ---
    Claims = wdi.get("claims", {})
    # ---
    if "P17" in Claims:
        LNKcountry = get_mainsnak(Claims.get("P17")[0])  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    if prnCountry == "" and "P495" in Claims:
        LNKcountry = get_mainsnak(Claims.get("P495")[0])  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    if prnCountry == "" and "P131" in Claims:
        LNKcountry = get_mainsnak(Claims.get("P131")[0])  # .getTarget()
        prnCountry = Get_label(LNKcountry)
    # ---
    printe.output(f"prnCountry:{prnCountry}")
    # ---
    females = [
        "شركة طيران",
        "شركة",
        "منظمة",
    ]
    # ---
    males = [
        "قانون تشريعي",
        "برنامج تلفزيوني",
        "مسلسل تلفزيوني",
        "طاقم موسيقي",
        "حزب سياسي",
        "نادي كرة قدم للهواة",
        "نادي كرة قدم",
    ]
    ande = " من " if something.strip() in males else " في "
    # ---
    dara = f"{ande.strip()} {prnCountry.strip()}"
    # ---
    if something.strip() in males:
        ma = get_female_for_p17(prnCountry.strip(), "man")
        if ma:
            dara = ma
            if something.strip() == "نادي كرة قدم للهواة":
                something = "نادي كرة قدم"
    # ---
    elif something.strip() in females:
        f = get_female_for_p17(prnCountry.strip(), "women")
        if f:
            dara = f
    # ---
    fanee = ""
    # ---
    if prnCountry:
        fanee = f"{something.strip()} {dara.strip()}"
    # ---
    return fanee


def its_canton_of_France(wdi):  # Q184188
    clai = wdi.get("claims", {})
    current_desc = wdi.get("descriptions", {}).get("ar", "")
    # ---
    if current_desc in ["", "كانتون فرنسي"]:
        if "P131" in clai:
            LNKcommunity = get_mainsnak(clai.get("P131")[0])  # .getTarget()
            label = Get_label(LNKcommunity)
            if label:
                label = label.replace("، فرنسا", "").replace(" (فرنسا)", "")
                desco = f"كانتون في {label}، فرنسا"
                return desco
    return ""


def its_an_episode(lng, wditem):
    if lng in wditem.get("descriptions", {}):
        return wditem.get("descriptions", {})[lng]
    if "P179" in wditem.get("claims", {}):  # serie
        LNKseries = get_mainsnak(wditem.get("claims", {}).get("P179")[0])  # .getTarget()
        serienaam = Get_label(LNKseries)
        if serienaam:
            serienaam = serienaam.replace("، مسلسل", "").replace(" (مسلسل)", "")
            return f"حلقة من سلسلة {serienaam}"
    return ""

def its_a_computergame(lng, wditem):
    printe.output(" its_a_computergame ")
    if "P178" in wditem.get("claims", {}):  # المطور
        LNKdeveloper = get_mainsnak(wditem.get("claims", {}).get("P178")[0])  # .getTarget()
        if LNKdeveloper is not None:
            WDitemdeveloper = wd_bot.Get_Item_API_From_Qid(LNKdeveloper)
            developer_name = Get_label_from_item(lng, WDitemdeveloper)
            if developer_name:
                return f"لعبة فيديو من تطوير {developer_name}"
    if "P179" in wditem.get("claims", {}):  # السلسلة
        serieLNK = get_mainsnak(wditem.get("claims", {}).get("P179")[0])  # .getTarget()
        if serieLNK is not None:
            WDitemserie = wd_bot.Get_Item_API_From_Qid(serieLNK)
            seriename = Get_label_from_item(lng, WDitemserie)
            if seriename:
                # return 'computerspel uit de serie %s' % seriename
                return f"لعبة فيديو من سلسلة {seriename}"
    return ""


def its_a_sports_season(wditem, claimstr=""):
    # ---
    # LNKsport=wditem.get('claims',{}).get('P3450')[0].get('mainsnak',{}).get('datavalue',{}).get('value',{}).get('id','')#.getTarget()
    # ---
    myclaim = "P3450"
    # ---
    pp = wditem.get("claims", {}).get(myclaim, [])
    if not claimstr.strip():
        # ---
        for x in pp:
            LNKitem = get_mainsnak(x)
            if not claimstr:
                claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    # ---
    shortstr = ""# "موسم رياضي"
    # ---
    if not pp:
        printe.output(f"its_a_sports_season item has no {myclaim} claims..")
    # ---
    if not claimstr:
        return shortstr
    # ---
    laste = f"موسم من {claimstr}"
    # ---
    printe.output(f"its_a_sports_season:({laste})")
    # ---
    return laste


def its_songs(type_of_item, wditem, shortstr, claimstr=""):
    # my_description = its_a_generalthing( wditem , da , '%s من أداء ' % da ,'P175')
    myclaim = "P175"
    # ---
    # songs_type
    # ---
    laste = ""# shortstr
    # ---
    P175 = wditem.get("claims", {}).get(myclaim, [])
    # ---
    if not claimstr:
        # ---
        for x in P175:
            LNKitem = get_mainsnak(x)
            claimstr = Get_label(LNKitem)
            printe.output(f"claimstr of {LNKitem}=[{claimstr}]")
            if claimstr:
                if len(P175) > 1:
                    claimstr += " وآخرون"
                break
        # ---
        if not P175:
            printe.output("its_songs item has no P175 claims..")
    # ---
    claimstr = claimstr.strip()
    # ---
    if claimstr:
        laste = f"{shortstr.strip()} من أداء {claimstr}"
    # ---
    sooo = [
        "Q1573906",  # جولة موسيقية
        "Q182832",  # حفلة موسيقية
    ]
    # ---
    if claimstr == "" and type_of_item in sooo:
        # ---
        LNKdirector = wditem.get("claims", {}).get("P57", [])
        # ---
        directorname = ""
        # ---
        for x in LNKdirector:
            LNKitem = get_mainsnak(x)
            directorname = Get_label(LNKitem)
            if directorname:
                break
        # ---
        if directorname:
            laste = f"{shortstr} من إخراج {directorname}"
    # ---
    printe.output(f"its_songs:({laste})")
    # ---
    return laste


def its_a_p50(type_of_item, wditem, shortstr, claimstr=""):
    myclaim = "P50"
    # ---
    P136 = get_mainsnak(wditem.get("claims", {}).get("P136", [{}])[0])
    if P136 == "Q8261" and shortstr == "عمل أدبي":
        shortstr = "رواية"
    # ---
    P50 = wditem.get("claims", {}).get(myclaim, [])
    # ---
    if not claimstr:
        # ---
        for x in P50:
            LNKitem = get_mainsnak(x)
            if not claimstr:
                claimstr = Get_label(LNKitem)
    # ---
    claimstr = claimstr.strip()
    # ---
    # if not claimstr: return shortstr
    if not claimstr:
        return ""
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
    sus = "بواسطة"
    # ---
    if shortstr.strip() in jjj:
        sus = "من تأليف"
    elif shortstr.strip().find("مقالة") != -1:
        sus = "كتبها"
    # ---
    laste = f"{shortstr.strip()} {sus} {claimstr}"
    if len(P50) > 1:
        laste = f"{shortstr.strip()} {sus} {claimstr} وآخرون"
    # ---
    # laste = laste.replace("كوكبة  ","كوكبة ")
    # ---
    printe.output(f"its_a_p50:({laste})")
    return laste


def its_a_thing_located_in_country(wditem, countryname, thing):
    if "P131" in wditem.get("claims", {}):
        LNKcommunity = get_mainsnak(wditem.get("claims", {}).get("P131")[0])  # .getTarget()
        label = Get_label(LNKcommunity)
        if label:
            return f"{thing} في {label}، {countryname}"
        else:
            return f"{thing} في {countryname}"
    return f"{thing} في {countryname}"


def its_a_film(wditem):
    # ---
    directorname = ""
    # ---
    P57 = wditem.get("claims", {}).get("P57", [])
    # ---
    print(f"len of P57: {len(P57)}")
    # ---
    for x in P57:
        q = get_mainsnak(x)
        directorname = Get_label(q)
        printe.output(f"directorname of {q}=[{directorname}]")
        if directorname:
            if len(P57) > 1:
                directorname += " وآخرون"
            break
    # ---
    if directorname:
        return f"فيلم من إخراج {directorname}"
    # ---
    return ""

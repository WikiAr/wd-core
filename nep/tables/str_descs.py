#!/usr/bin/env python3
"""
from nep.tables.str_descs import descs, entities, countries, genese, make_nn
"""


# ---
descs = {
    "Q1149652": {"org": ["", "district"], "desc": "district in India"},
    # ---
    "Q2154519": {"org": ["", ""], "desc": "bron van astrofysische röntgenstraling"},  # 16649
    # ---
    "Q67206701": {"org": ["", ""], "desc": "ver-liggend infrarood object"},  # 10132
    # ---
    "Q189004": {"org": ["", ""], "desc": "onderwijsinstelling"},
    # ---
    "Q17633526": {"org": ["", ""], "desc": "Wikinews-artikel"},
    # ---
    "Q4592255": {"org": ["", ""], "desc": "project sub-pagina"},
    # ---
    "Q21278897": {"org": ["", ""], "desc": "Wiktionary-doorverwijzing"},
    # ---
    "Q737498": {"org": ["tijdschrift", ""], "desc": "academisch tijdschrift"},
    # ---
    "Q24764": {"org": ["gemeente", ""], "desc": "Filipijnse gemeente"},
    # ---
    "Q70208": {"org": ["gemeente", ""], "desc": "Zwitserse gemeente"},
    # ---
    "Q203300": {"org": ["gemeente", ""], "desc": "gemeente in Liechtenstein"},
    # ---
    "Q53764738": {"org": ["", ""], "desc": "Chinees karakter"},
    # ---
    "Q30612": {"org": ["klinisch onderzoek", ""], "desc": "klinisch onderzoek"},
    # ---
    "Q2996394": {"org": ["x", ""], "desc": "biologisch proces"},
    # ---
    "Q14860489": {"org": ["y", ""], "desc": "moleculaire functie"},
    # ---
    "Q5058355": {"org": ["z", ""], "desc": "cellulaire component"},
    # ---
    "Q101352": {"org": ["", ""], "desc": "achternaam"},
    # ---
    "Q4167836": {"org": ["", "categorie", "Categorie", "category"], "desc": "Wikimedia-categorie"},
    # ---
    "Q13442814": {"org": ["artikel", ""], "desc": "wetenschappelijk artikel"},
    # ---
    "Q5864": {"org": ["geile dwerg", ""], "desc": "gele dwerg"},
    # ---
    "Q50231": {"org": ["bestuurlijk gebied", "gebied", ""], "desc": "bestuurlijk gebied in China"},
    # ---
    "Q41710": {"org": ["", ""], "desc": "etnische groep"},
    # ---
    "Q11446": {"org": ["", ""], "desc": "schip"},
    # ---
    "Q5153359": {"org": ["", ""], "desc": "gemeente in Tsjechië"},
    # ---
    "Q1131296": {"org": ["", ""], "desc": "freguesia in Portugal"},
    # ---
    "Q3966183": {"org": ["Pokemonwezen", "Pokémon-wezen", "Pokemon", "Pokémon", ""], "desc": "Pokémonwezen"},
    # ---
    "Q618779": {"org": ["onderscheiding", ""], "desc": "onderscheiding"},
    # ---
    "Q197": {"org": ["", "vliegtuig"], "desc": "vliegtuig"},
    # ---
    "Q2590631": {"org": ["", ""], "desc": "gemeente in Hongarije"},
    # ---
    "Q3024240": {"org": ["", ""], "desc": "historisch land"},
    # ---
    "Q11173": {"org": ["chemische stof", "chemische samenstelling", ""], "desc": "chemische verbinding"},
    # ---
    "Q79529": {"org": ["chemische samenstelling", "chemische verbinding"], "desc": "chemische stof"},
    # ---
    "Q11266439": {"org": ["", "template", "sjabloon"], "desc": "Wikimedia-sjabloon"},
    # ---
    "Q310890": {"org": ["taxon", ""], "desc": "monotypische taxon"},
    # ---
    "Q877358": {"org": ["resolutie", ""], "desc": "resolutie van de Veiligheidsraad van de Verenigde Naties"},
    # ---
    "Q3192808": {"org": ["commune", ""], "desc": "commune in Madagascar"},
    # ---
    "Q18536594": {"org": ["sportevenement", ""], "desc": "sportevenement op de Olympische Spelen"},
}
entities = {
    "Q106259": {"org": ["polder", ""], "desc": "polder in"},
    "Q106658": {"org": ["landkreis", ""], "desc": "Landkreis in"},
    "Q126807": {"org": ["kleuterschool", "school", ""], "desc": "kleuterschool in"},
    "Q127448": {"org": ["gemeente", "zweedse gemeente"], "desc": "Zweedse gemeente in"},
    "Q13005188": {"org": ["", "mandal", "mandal in India"], "desc": "mandal in"},
    "Q166735": {"org": ["broekbos", ""], "desc": "broekbos in"},
    "Q1690211": {"org": ["", ""], "desc": "openbare wasplaats in"},
    "Q2042028": {"org": ["kloof", ""], "desc": "kloof in"},
    "Q26703203": {"org": ["stolperstein", ""], "desc": "stolperstein in"},
    "Q30198": {"org": ["", "uitstekend landdeel", "meers", "moeras"], "desc": "moeras in"},
    "Q3184121": {"org": ["gemeente", "gemeente in brazilie", "gemeente in brazilië", ""], "desc": "gemeente in"},
    "Q3947": {"org": ["woonhuis", ""], "desc": "woonhuis in"},
    "Q41176": {"org": ["gebouw", "bouwwerk", ""], "desc": "gebouw in"},
    "Q5084": {"org": ["gehucht", ""], "desc": "gehucht in"},
    "Q5358913": {"org": ["", ""], "desc": "Japanse basisschool in"},
    "Q5783996": {"org": ["cottage", ""], "desc": "cottage in"},
    "Q659103": {"org": ["gemeente in Roemenie", "gemeente in Roemenië", "gemeente", ""], "desc": "gemeente in"},
    "Q7075": {"org": ["bibliotheek", ""], "desc": "bibliotheek in"},
    "Q735428": {"org": ["gemeente", ""], "desc": "gemeente in"},
    "Q751876": {"org": ["kasteel", ""], "desc": "kasteel in"},
    "Q811979": {"org": ["bouwwerk", ""], "desc": "bouwwerk in"},
    "Q88965416": {"org": ["", ""], "desc": "Zweedse schooleenheid in"},
    "Q953806": {"org": ["bushalte", ""], "desc": "bushalte in"},
    "Q9842": {"org": ["basisschool", "basisschool in italië", ""], "desc": "basisschool in "},
}

countries = {
    "Q102496": {"org": ["parochie", ""], "desc": "parochie"},
    "Q11812394": {"org": ["", "theaterbedrijf"], "desc": "theaterbedrijf"},
    "Q13141064": {"org": ["", "badmintonner", "badmintonspeler", ""], "desc": "badmintonspeler"},
    "Q14659": {"org": ["heraldisch wapen", ""], "desc": "wapen"},
    "Q15081032": {"org": ["motorfietsmerk", ""], "desc": "motorfietsmerk"},
    "Q15991303": {"org": ["voetbalcompetitie", ""], "desc": "voetbalcompetitie"},
    "Q165": {"org": ["zee", ""], "desc": "zee"},
    "Q16970": {"org": ["kerkgebouw", ""], "desc": "kerkgebouw"},
    "Q178561": {"org": ["veldslag", ""], "desc": "veldslag"},
    "Q180684": {"org": ["conflict", ""], "desc": "conflict"},
    "Q2065704": {"org": ["", "kantongerecht", "kantongerecht in noorwegen"], "desc": "kantongerecht"},
    "Q23397": {"org": ["meer", ""], "desc": "meer"},
    "Q23442": {"org": ["eiland", ""], "desc": "eiland "},
    "Q23925393": {"org": ["douar", ""], "desc": "douar"},
    "Q2526255": {"org": ["filmregisseur", "", "regisseur"], "desc": "filmregisseur"},
    "Q2912397": {"org": ["eendaagse wielerwedstrijd", ""], "desc": "eendaagse wielerwedstrijd "},
    "Q34442": {"org": ["weg", "straat", "straat in", ""], "desc": "weg"},
    "Q34763": {"org": ["schiereiland", ""], "desc": "schiereiland "},
    "Q355304": {"org": ["", "watergang"], "desc": "watergang "},
    "Q3914": {"org": ["school", ""], "desc": "school"},
    "Q55659167": {"org": ["", "natuurlijke waterloop"], "desc": "natuurlijke waterloop"},
    "Q57733494": {"org": ["", "badmintoernooi"], "desc": "badmintontoernooi"},
    "Q742421": {"org": ["", "theatergezelschap"], "desc": "theatergezelschap"},
    "Q985488": {"org": ["bewonersgemeenschap", ""], "desc": "bewonersgemeenschap"},
}
# ---
genese = {
    "Q1002697": {"org": ["periodiek", ""], "desc": "", "desc_in": "periodiek over", "pid": "P641"},
    "Q1004": {"org": ["stripverhaal", ""], "desc": "stripverhaal", "desc_in": "stripverhaal من سلسلة ", "pid": "P179"},
    "Q1344": {"org": ["opera", ""], "desc": "opera", "desc_in": "opera van ", "pid": "P86"},
    "Q14406742": {"org": ["stripreeks", ""], "desc": "stripreeks", "desc_in": "stripreeks door ", "pid": "P50"},
    "Q178122": {"org": ["aria", ""], "desc": "aria", "desc_in": "aria van ", "pid": "P86"},
    "Q21014462": {"org": ["cellijn", ""], "desc": "", "desc_in": "cellijn van een ", "pid": "P703"},
    "Q2668072": {"org": ["", ""], "desc": "collectie", "desc_in": "collectie uit ", "pid": "P195"},
    "Q4502142": {"org": ["visueel kunstwerk", ""], "desc": "visueel kunstwerk", "desc_in": "visueel kunstwerk in collectie ", "pid": "P195"},
    "Q50386450": {"org": ["opera-personage", ""], "desc": "opera-personage", "desc_in": "opera-personage uit ", "pid": "P1441"},
    "Q5633421": {"org": ["", "tijdschrift", "wetenschappelijk tijdschrift"], "desc": "", "desc_in": "wetenschappelijk tijdschrift van ", "pid": "P123"},
    "Q6451276": {"org": ["CSR-rapport", ""], "desc": "CSR-rapport", "desc_in": "CSR-rapport over ", "pid": "P921"},
}
# ---
from wd_api import wd_bot

from nep.bots.its import (
    its_a_generalthing,
    its_a_thing_located_in_country,
    its_something_in_a_country,
    its_something_in_an_entity,
)
from nep.bots.helps import (
    get_label_txt,
    Get_label_from_item,
    get_mainsnak,
)

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


def its_an_audio_drama(wditem):
    if "P179" in wditem.get("claims", {}):
        return its_a_generalthing(wditem, "hoorspel", "hoorspel van", "P50")
    if "P50" in wditem.get("claims", {}):
        return its_a_generalthing(wditem, "hoorspel", "hoorspel van", "P50")
    if "P495" in wditem.get("claims", {}):
        return its_a_generalthing(wditem, "hoorspel", "hoorspel uit", "P495")
    return ""


def its_a_taxon(lng, wditem):
    """
    read P171/mother taxon until taxo-rang/P105 is <Q19970288/no value> -> that mother taxon is the first part (insect/)
    """
    if lng in wditem.get("descriptions", {}):
        return wditem.get("descriptions", {})[lng]
    return ""


def its_a_tabon_in_thailand(lng, wditem):
    if "P131" in wditem.get("claims", {}):
        LNKtambon = get_mainsnak(wditem.get("claims", {}).get("P131")[0])  # .getTarget()
        if LNKtambon is not None:
            WDitemtambon = wd_bot.Get_Item_API_From_Qid(LNKtambon)  # xzo
            return Get_label_from_item(lng, WDitemtambon)
    return ""


def its_a_publication(wditem):
    if "P921" in wditem.get("claims", {}):
        its_a_generalthing(wditem, "", "over", "P921")
    if "P123" in wditem.get("claims", {}):
        its_a_generalthing(wditem, "", "van uitgever", "P123")
    if "P577" in wditem.get("claims", {}):
        pass
    return "publicatie"


def its_a_headquarted_thing(lng, wdi, thing):
    where = get_label_txt(lng, wdi, "P159", fallback=True)
    return f"{thing} {where}" if where else ""


def its_a_fictional_character(wditem):
    if "P1441" in wditem.get("claims", {}):
        return its_a_generalthing(wditem, "personage", "personage uit", "P1441")
    elif "P1080" in wditem.get("claims", {}):
        return its_a_generalthing(wditem, "personage", "personage uit", "P1080")
    else:
        return ""


def its_a_discography(lng, wditem):
    if "P175" in wditem.get("claims", {}):
        artistLNK = get_mainsnak(wditem.get("claims", {}).get("P175")[0])  # .getTarget()
        if artistLNK is not None:
            wdArtist = wd_bot.Get_Item_API_From_Qid(artistLNK)  # xzo
            if lng in wdArtist.get("labels", {}):
                return f"discografie van {wdArtist.get('labels', {}).get(lng, '')}"
            if lng != "ar":
                for trylng in lng_canbeused:
                    if trylng in wdArtist.get("labels", {}):
                        return f"discografie van {wdArtist.get('labels', {}).get(trylng, '')}"
    return ""


def its_a_composition(lng, wditem):
    """
    find composer P86
    """
    if "P86" in wditem.get("claims", {}):
        composerLNK = get_mainsnak(wditem.get("claims", {}).get("P86")[0])  # .getTarget()
        if composerLNK is not None:
            composer = wd_bot.Get_Item_API_From_Qid(composerLNK)  # xzo
            if lng in composer.get("labels", {}):
                return f"compositie van {composer.get('labels', {}).get(lng, '')}"
    return ""


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
    elif p31 == "Q3508250":  # 15456
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
            desc = its_a_generalthing(wditem, p31_tab["desc"], p31_tab["desc_in"], p31_tab["pid"])
    # ---
    return desc

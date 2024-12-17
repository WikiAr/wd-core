#!/usr/bin/python3
"""

from people.people_get_topic import get_topic

python3 core8/pwb.py people/people_get_topic

SELECT ?item ?dem WHERE {
  ?item wdt:P31 wd:Q3624078;
    wdt:P1549 ?dem.
  filter (lang(?dem) = "en")
}

"""
import sys
from newapi import printe


qid_to_job = {
    "Q520549": "~ geologist",
}

nat_to_qid = {
    "Afghan": "Q889",
    "Albanian": "Q222",
    "Algerian": "Q262",
    "American": "Q30",
    "Andorran": "Q228",
    "Angolan": "Q916",
    "Argentine": "Q414",
    "Argentinean": "",
    "Armenian": "Q399",
    "Argentinian": "Q414",
    "Australian": "Q408",
    "Austrian": "Q40",
    "Azerbaijani": "Q227",
    "Bahamian": "Q778",
    "Bahraini": "Q398",
    "Bangladeshi": "Q902",
    "Barbadian": "Q244",
    "Belarusian": "Q184",
    "Belgian": "Q31",
    "Belizean": "Q242",
    "Beninese": "Q962",
    "Beninois": "",
    "Bermudan": "",
    "Bermudian": "",
    "Bhutanese": "Q917",
    "Bissau-Guinean": "Q1007",
    "Bolivian": "Q750",
    "Bosnian": "Q225",
    "Botswanan": "Q963",
    "Brazilian": "Q155",
    "British": "Q145",
    "Bruneian": "",
    "Bulgarian": "Q219",
    "Burkinabe": "Q965",
    "Burkinabé": "Q965",
    "Burmese": "Q836",
    "Burundian": "Q967",
    "Cabo Verdean": "Q1011",
    "Cambodian": "Q424",
    "Cameroonian": "Q1009",
    "Canadian": "Q16",
    "Chadian": "Q657",
    "Chilean": "Q298",
    "Chinese": "Q148",
    "Colombian": "Q739",
    "Comoran": "Q970",
    "Comorian": "Q970",
    "Congolese": "Q974",
    "Costa Rican": "Q800",
    "Croatian": "Q224",
    "Cuban": "Q241",
    "Cypriot": "Q229",
    "Czech": "Q213",
    "Danish": "Q756617",
    "Djiboutian": "Q977",
    "Dutch": "Q29999",
    "Ecuadorian": "Q736",
    "Egyptian": "Q79",
    "Emirati": "Q878",
    "Emiri": "Q878",
    "Emirian": "Q878",
    "Equatoguinean": "Q983",
    "Equatorial Guinean": "Q983",
    "Eritrean": "Q986",
    "Estonian": "Q191",
    "Ethiopian": "Q115",
    "Fijian": "Q712",
    "Filipino": "Q928",
    "Finnish": "Q33",
    "French": "Q142",
    "Gabonese": "Q1000",
    "Gambian": "Q1005",
    "Georgian": "Q230",
    "German": "Q183",
    "Ghanaian": "Q117",
    "Greek": "Q41",
    "Greenlandic": "",
    "Grenadian": "Q769",
    "Guatemalan": "Q774",
    "Guinean": "Q1006",
    "Guyanese": "Q734",
    "Haitian": "Q790",
    "Herzegovinian": "Q225",
    "Honduran": "Q783",
    "Hungarian": "Q28",
    "Icelandic": "Q189",
    "I-Kiribati": "Q710",
    "Indian": "Q668",
    "Indonesian": "Q252",
    "Iranian": "Q794",
    "Iraqi": "Q796",
    "Irish": "Q27",
    "Israeli": "Q801",
    "Italian": "Q38",
    "Ivorian": "Q1008",
    "Jamaican": "Q766",
    "Japanese": "Q17",
    "Jordanian": "Q810",
    "Kazakh": "Q232",
    "Kazakhstani": "Q232",
    "Kenyan": "Q114",
    "Kirghiz": "",
    "Kirgiz": "",
    "Kiribati": "",
    "Kosovan": "",
    "Kosovar": "",
    "Kuwaiti": "Q817",
    "Kyrgyz": "Q813",
    "Kyrgyzstani": "Q813",
    "Lao": "Q819",
    "Laotian": "Q819",
    "Latvian": "Q211",
    "Lebanese": "Q822",
    "Liberian": "Q1014",
    "Libyan": "Q1016",
    "Liechtensteiner": "Q347",
    "Lithuanian": "Q37",
    "Luxembourg": "",
    "Luxembourgish": "Q32",
    "Macanese": "",
    "Macedonian": "Q221",
    "Malagasy": "Q1019",
    "Malawian": "Q1020",
    "Malaysian": "Q833",
    "Maldivian": "Q826",
    "Malian": "Q912",
    "Maltese": "Q233",
    "Mauritanian": "Q1025",
    "Mauritian": "Q1027",
    "Mexican": "Q96",
    "Moldovan": "Q217",
    "Monacan": "Q235",
    "Monégasque": "Q235",
    "Mongolian": "Q711",
    "Montenegrin": "Q236",
    "Moroccan": "Q1028",
    "Mosotho": "Q1013",
    "Mozambican": "Q1029",
    "Namibian": "Q1030",
    "Nauruan": "Q697",
    "Nepalese": "Q837",
    "Nepali": "Q837",
    "New Zealand": "Q664",
    "Ni-Vanuatu": "Q686",
    "Nicaraguan": "Q811",
    "Nigerian": "Q1033",
    "Nigerien": "Q1032",
    "North Korean": "Q423",
    "Norwegian": "Q20",
    "Omani": "Q842",
    "Pakistani": "Q843",
    "Palauan": "Q695",
    "Palestinian": "Q219060",
    "Panamanian": "Q804",
    "Papua New Guinean": "Q691",
    "Papuan": "",
    "Paraguayan": "Q733",
    "Peruvian": "Q419",
    "Philippine": "Q928",
    "Polish": "Q36",
    "Portuguese": "Q45",
    "Puerto Rican": "",
    "Qatari": "Q846",
    "Romanian": "Q218",
    "Russian": "Q159",
    "Rwandan": "Q1037",
    "Salvadoran": "Q792",
    "Sammarinese": "Q238",
    "Samoan": "Q683",
    "São Toméan": "Q1039",
    "Saudi": "Q851",
    "Saudi Arabian": "Q851",
    "Senegalese": "Q1041",
    "Serbian": "Q403",
    "Seychellois": "Q1042",
    "Sierra Leonean": "Q1044",
    "Singapore": "",
    "Singaporean": "Q334",
    "Slovak": "Q214",
    "Slovene": "Q215",
    "Slovenian": "Q215",
    "Somali": "Q1045",
    "South African": "Q258",
    "South Korean": "Q884",
    "Spanish": "Q29",
    "Sri Lankan": "Q854",
    "Sudanese": "Q1049",
    "Surinamese": "Q730",
    "Swedish": "Q34",
    "Swiss": "Q39",
    "Syrian": "Q858",
    "Tajikistani": "Q863",
    "Tanzanian": "Q924",
    "Thai": "Q869",
    "Timorese": "",
    "Togolese": "Q945",
    "Tongan": "Q678",
    "Trinidadian": "Q754",
    "Tobagonian": "",
    "Tunisian": "Q948",
    "Turkish": "Q43",
    "Turkmen": "Q874",
    "Tuvaluan": "Q672",
    "Ugandan": "Q1036",
    "UK": "",
    "U.K.": "",
    "Ukrainian": "",
    "Uruguayan": "Q77",
    "US": "",
    "U.S.": "",
    "United States": "",
    "Uzbek": "Q265",
    "Uzbekistani": "Q265",
    "Vanuatuan": "Q686",
    "Vatican": "Q237",
    "Venezuelan": "Q717",
    "Vietnamese": "Q881",
    "Yemeni": "Q805",
    "Zambian": "Q953",
    "Zimbabwean": "Q954",
    "Luxembourgian": "Q32",
    "New Zealander": "Q664",
}

qid_to_p27 = {n: q for q, n in nat_to_qid.items()}


def get_claim_id(item, prop):
    claim = item.get("claims", {}).get(prop, [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")
    return claim


def get_topic(item):
    # ---
    P106 = get_claim_id(item, "P106")
    P27 = get_claim_id(item, "P27")
    # ---
    printe.output(f" P106:{P106}: P27:{P27}")
    # ---
    lab = ""
    # ---
    p106_lab = qid_to_job.get(P106)
    p27_lab = qid_to_p27.get(P27)
    # ---
    if p106_lab and p27_lab:
        lab = p106_lab.replace("~", p27_lab)
        printe.output(f" topic:{lab}")
    # ---
    if not lab:
        return ""
    # ---
    if "returnlab" in sys.argv:
        return lab
    # ---
    printe.output(f"<<yellow>> lab:{lab} add 'returnlab' to sys.argv to use it..!!")
    # ---
    return ""

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
    "Afghan": "",
    "Albanian": "",
    "Algerian": "",
    "American": "",
    "Andorran": "",
    "Angolan": "",
    "Argentine": "",
    "Argentinean": "",
    "Armenian": "",
    "Argentinian": "",
    "Australian": "",
    "Austrian": "",
    "Azerbaijani": "",
    "Bahamian": "",
    "Bahraini": "",
    "Bangladeshi": "",
    "Barbadian": "",
    "Belarusian": "",
    "Belgian": "",
    "Belizean": "",
    "Beninese": "",
    "Beninois": "",
    "Bermudan": "",
    "Bermudian": "",
    "Bhutanese": "",
    "Bissau-Guinean": "",
    "Bolivian": "",
    "Bosnian": "",
    "Botswanan": "",
    "Brazilian": "",
    "British": "",
    "Bruneian": "",
    "Bulgarian": "",
    "Burkinabe": "",
    "Burkinabé": "",
    "Burmese": "",
    "Burundian": "",
    "Cabo Verdean": "",
    "Cambodian": "",
    "Cameroonian": "",
    "Canadian": "",
    "Chadian": "",
    "Chilean": "",
    "Chinese": "",
    "Colombian": "",
    "Comoran": "",
    "Comorian": "",
    "Congolese": "",
    "Costa Rican": "",
    "Croatian": "",
    "Cuban": "",
    "Cypriot": "",
    "Czech": "",
    "Danish": "",
    "Djiboutian": "",
    "Dutch": "",
    "Ecuadorian": "",
    "Egyptian": "",
    "Emirati": "",
    "Emiri": "",
    "Emirian": "",
    "Equatoguinean": "",
    "Equatorial Guinean": "",
    "Eritrean": "",
    "Estonian": "",
    "Ethiopian": "",
    "Fijian": "",
    "Filipino": "",
    "Finnish": "",
    "French": "",
    "Gabonese": "",
    "Gambian": "",
    "Georgian": "",
    "German": "Q183",
    "Ghanaian": "",
    "Greek": "",
    "Greenlandic": "",
    "Grenadian": "",
    "Guatemalan": "",
    "Guinean": "",
    "Guyanese": "",
    "Haitian": "",
    "Herzegovinian": "",
    "Honduran": "",
    "Hungarian": "",
    "Icelandic": "",
    "I-Kiribati": "",
    "Indian": "",
    "Indonesian": "",
    "Iranian": "",
    "Iraqi": "",
    "Irish": "",
    "Israeli": "",
    "Italian": "",
    "Ivorian": "",
    "Jamaican": "",
    "Japanese": "",
    "Jordanian": "",
    "Kazakh": "",
    "Kazakhstani": "",
    "Kenyan": "",
    "Kirghiz": "",
    "Kirgiz": "",
    "Kiribati": "",
    "Kosovan": "",
    "Kosovar": "",
    "Kuwaiti": "",
    "Kyrgyz": "",
    "Kyrgyzstani": "",
    "Lao": "",
    "Laotian": "",
    "Latvian": "",
    "Lebanese": "",
    "Liberian": "",
    "Libyan": "",
    "Liechtensteiner": "",
    "Lithuanian": "",
    "Luxembourg": "",
    "Luxembourgish": "",
    "Macanese": "",
    "Macedonian": "",
    "Malagasy": "",
    "Malawian": "",
    "Malaysian": "",
    "Maldivian": "",
    "Malian": "",
    "Maltese": "",
    "Mauritanian": "",
    "Mauritian": "",
    "Mexican": "",
    "Moldovan": "",
    "Monacan": "",
    "Monégasque": "",
    "Mongolian": "",
    "Montenegrin": "",
    "Moroccan": "",
    "Mosotho": "",
    "Mozambican": "",
    "Namibian": "",
    "Nauruan": "",
    "Nepalese": "",
    "Nepali": "",
    "New Zealand": "",
    "Ni-Vanuatu": "",
    "Nicaraguan": "",
    "Nigerian": "",
    "Nigerien": "",
    "North Korean": "",
    "Norwegian": "",
    "Omani": "",
    "Pakistani": "",
    "Palauan": "",
    "Palestinian": "",
    "Panamanian": "",
    "Papua New Guinean": "",
    "Papuan": "",
    "Paraguayan": "",
    "Peruvian": "",
    "Philippine": "",
    "Polish": "",
    "Portuguese": "",
    "Puerto Rican": "",
    "Qatari": "",
    "Romanian": "",
    "Russian": "",
    "Rwandan": "",
    "Salvadoran": "",
    "Sammarinese": "",
    "Samoan": "",
    "São Toméan": "",
    "Saudi": "",
    "Saudi Arabian": "",
    "Senegalese": "",
    "Serbian": "",
    "Seychellois": "",
    "Sierra Leonean": "",
    "Singapore": "",
    "Singaporean": "",
    "Slovak": "",
    "Slovene": "",
    "Slovenian": "",
    "Somali": "",
    "South African": "",
    "South Korean": "",
    "Spanish": "",
    "Sri Lankan": "",
    "Sudanese": "",
    "Surinamese": "",
    "Swedish": "",
    "Swiss": "",
    "Syrian": "",
    "Tajikistani": "",
    "Tanzanian": "",
    "Thai": "",
    "Timorese": "",
    "Togolese": "",
    "Tongan": "",
    "Trinidadian": "",
    "Tobagonian": "",
    "Tunisian": "",
    "Turkish": "",
    "Turkmen": "",
    "Tuvaluan": "",
    "Ugandan": "",
    "UK": "",
    "U.K.": "",
    "Ukrainian": "",
    "Uruguayan": "",
    "US": "",
    "U.S.": "",
    "United States": "",
    "Uzbek": "",
    "Uzbekistani": "",
    "Vanuatuan": "",
    "Vatican": "",
    "Venezuelan": "",
    "Vietnamese": "",
    "Yemeni": "Q805",
    "Zambian": "",
    "Zimbabwean": "",
    "Luxembourgian": "",
    "New Zealander": "",
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

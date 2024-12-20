#!/usr/bin/python3
"""

from people.people_get_topic import job_to_qid, nat_to_qid
from people.people_get_topic import get_topic
from people.people_get_topic import print_new_jobs

python3 core8/pwb.py people/people_get_topic

SELECT ?item ?dem WHERE {
  ?item wdt:P31 wd:Q3624078;
    wdt:P1549 ?dem.
  filter (lang(?dem) = "en")
}

"""
import sys
from newapi import printe


job_to_qid = {
    # "businessman": "Q43845",
    # "businesswomen": "Q43845",
    "businessman and philanthropist": "",
    "football player": "Q117321337",
    "footballer": "Q117321337",
    "gynaecologist": "Q2640827",
    "archduke": "Q154615",
    "theatre director": "Q3387717",
    "indigenous artist": "",
    "former military officer": "",
    "racing cyclist": "Q2309784",
    "rules footballer": "Q13414980",
    "lyricist": "Q822146",
    "cartoonist": "Q1114448",
    "philanthropist": "Q12362622",
    "pharmacist": "Q105186",
    "archbishop": "Q49476",
    "activist": "Q15253558",
    "actor": "Q33999",
    "actress": "Q21169216",
    "architect": "Q42973",
    "artist": "Q847689",
    "association football player": "Q937857",
    "association football manager": "Q628099",
    "astronomer": "Q11063",
    "athlete": "Q2066131",
    "athletics competitor": "Q11513337",
    "basketball player": "Q3665646",
    "bicycle racer": "Q2309784",
    "botanist": "Q2374149",
    "catholic priest": "Q250867",
    "chemist": "Q593644",
    "choreographer": "Q2490358",
    "comics artist": "Q715301",
    "composer": "Q36834",
    "cyclist": "Q2125610",
    "diplomat": "Q193391",
    "economist": "Q188094",
    "educator": "Q974144",
    "engineer": "Q81096",
    "entomologist": "Q3055126",
    "explorer": "Q11900058",
    "film actor": "Q10800557",
    "film director": "Q2526255",
    "film producer": "Q3282637",
    "historian": "Q201788",
    "illustrator": "Q644687",
    "journalist": "Q1930187",
    "jurist": "Q185351",
    "lawyer": "Q40348",
    "lexicographer": "Q14972848",
    "mathematician": "Q170790",
    "musician": "Q639669",
    "novelist": "Q6625963",
    "painter": "Q1028181",
    "philosopher": "Q4964182",
    "photographer": "Q33231",
    "physician": "Q39631",
    "physicist": "Q169470",
    "pianist": "Q486748",
    "playwright": "Q214917",
    "poet": "Q49757",
    "politician": "Q82955",
    "publisher": "Q2516866",
    "rabbi": "Q133485",
    "rugby union player": "Q14089670",
    "screenwriter": "Q28389",
    "sculptor": "Q1281618",
    "singer": "Q177220",
    "skier": "Q4270517",
    "sociologist": "Q2306091",
    "soldier": "Q4991371",
    "sport cyclist": "Q2309784",
    "swimmer": "Q10843402",
    "tennis player": "Q10833314",
    "translator": "Q333634",
    "writer": "Q36180",
    "art historian": "Q1792450",
    "university teacher": "Q1622272",
    "fencer": "Q13381863",
    "businessperson": "Q43845",
    "children's writer": "Q4853732",
    "papyrologist": "Q16267158",
    "researcher": "Q1650915",
    "sprinter": "Q4009406",
    "military officer": "Q189290",
    "medievalist": "Q3332711",
    "philologist": "Q13418253",
    "physiologist": "Q2055046",
    "political scientist": "Q1238570",
    "psychoanalyst": "Q3410028",
    "psychiatrist": "Q211346",
    "psychologist": "Q212980",
    "racing driver": "Q378622",
    "basketball coach": "Q5137571",
    "violinist": "Q1259917",
    "virologist": "Q15634281",
    "rally driver": "Q10842936",
    "pathologist": "Q3368718",
    "pharmacologist": "Q2114605",
    "rapper": "Q2252262",
    "saxophonist": "Q12800682",
    "scientist": "Q901",
    "singer-songwriter": "Q488205",
    "radiologist": "Q18245236",
    "ethnologist": "Q1371378",
    "handball player": "Q12840545",
    "geographer": "Q901402",
    "geologist": "Q520549",
    "theologian": "Q1234713",
    "volleyball player": "Q15117302",
    "water polo player": "Q17524364",
    "zoologist": "Q350979",
    "archivist": "Q635734",
    "rower": "Q13382576",
    "snowboarder": "Q15709642",
    "speleologist": "Q16742175",
    "spy": "Q9352089",
    "trade unionist": "Q15627169",
    "veterinarian": "Q202883",
    "surgeon": "Q774306",
    "academic": "Q3400985",
    "alpine skier": "Q4144610",
    "cross-country skier": "Q13382608",
    "chess player": "Q10873124",
    "caricaturist": "Q3658608",
    "chef": "Q3499072",
    "boxer": "Q11338576",
    "cartographer": "Q1734662",
    "dermatologist": "Q2447386",
    "biathlete": "Q16029547",
    "ice hockey player": "Q11774891",
    "field hockey player": "Q10843263",
    "geneticist": "Q3126128",
    "guitarist": "Q855091",
    "gymnast": "Q16947675",
    "judoka": "Q6665249",
    "legal historian": "Q2135538",
    "librarian": "Q182436",
    "linguist": "Q14467526",
    "critic": "Q6430706",
    "literary critic": "Q4263842",
    "association football referee": "Q859528",
    "anatomist": "Q10872101",
    "anthropologist": "Q4773904",
    "archaeologist": "Q3621491",
    "archer": "Q13382355",
    "biologist": "Q864503",
    "egyptologist": "Q1350189",
    "film critic": "Q4220892",
    "flying ace": "Q222982",
    "mineralogist": "Q13416354",
    "missionary": "Q219477",
    "motorcycle racer": "Q3014296",
    "musicologist": "Q14915627",
    "mycologist": "Q2487799",
    "naturalist": "Q18805",
    "neurologist": "Q783906",
    "essayist": "Q11774202",
    "engraver": "Q329439",
    "oncologist": "Q16062369",
    "opera singer": "Q2865819",
    "ophthalmologist": "Q12013238",
    "organist": "Q765778",
    "orientalist": "Q1731155",
    "ornithologist": "Q1225716",
}

nat_to_qid = {
    "Afghan": "Q889",
    "Albanian": "Q222",
    "Algerian": "Q262",
    "American": "Q30",
    "Andorran": "Q228",
    "Angolan": "Q916",
    "Argentine": "Q414",
    "Argentinean": "Q414",
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
    "Beninois": "Q962",
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
    "UK": "British",
    "U.K.": "British",
    "Ukrainian": "",
    "Uruguayan": "Q77",
    "US": "Q30",
    "U.S.": "Q30",
    "United States": "Q30",
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

qid_to_p27 = {q: n for n, q in nat_to_qid.items() if n != "" and q != ""}
qid_to_job = {q: n for n, q in job_to_qid.items() if n != "" and q != ""}


def get_claim_id(item, prop):
    claim = item.get("claims", {}).get(prop, [{}])[0].get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "")
    return claim


def get_claim_ids(item, prop):
    claims = item.get("claims", {}).get(prop, [])
    claim_ids = [claim.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id", "") for claim in claims]
    return claim_ids


new_jobs = {}
new_nats = {}


def get_topic(item):
    # ---
    P106_list = get_claim_ids(item, "P106")
    P27_list = get_claim_ids(item, "P27")
    # ---
    p27_lab = ""
    p106_lab = ""
    # ---
    for x in P106_list:
        p106_lab = qid_to_job.get(x)
        if p106_lab:
            break
        else:
            new_jobs.setdefault(x, 0)
            new_jobs[x] += 1
    # ---
    for x in P27_list:
        p27_lab = qid_to_p27.get(x)
        if p27_lab:
            break
        else:
            new_nats.setdefault(x, 0)
            new_nats[x] += 1
    # ---
    lab = ""
    # ---
    if p106_lab and p27_lab:
        # lab = p106_lab.replace("~", p27_lab)
        lab = f"{p27_lab} {p106_lab}"
        printe.output(f" topic:{lab}")
    # ---
    if not lab:
        printe.output(f"{p106_lab=} {p27_lab=}")
        return ""
    # ---
    if "returnlab" in sys.argv:
        return lab
    # ---
    printe.output(f"<<yellow>> lab:{lab} add 'returnlab' to sys.argv to use it..!!")
    # ---
    return ""


def print_new_jobs():
    lists = [[y, x] for x, y in new_jobs.items()]
    lists.sort(reverse=True)
    # ---
    for lenth, qid in lists:
        # ---
        printe.output(f"new_jobs:{lenth} : qid:{qid}")
    # ---
    lists1 = [[y, x] for x, y in new_nats.items()]
    lists1.sort(reverse=True)
    # ---
    for lenth, qid in lists1:
        # ---
        printe.output(f"new_nats:{lenth} : qid:{qid}")
    # ---

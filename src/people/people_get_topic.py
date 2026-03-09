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

import logging
logger = logging.getLogger(__name__)

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
    "Gabonese": "Q1000",
    "Gambian": "Q1005",
    "Guinean": "Q1006",
    "Bissau-Guinean": "Q1007",
    "Ivorian": "Q1008",
    "Cameroonian": "Q1009",
    "Cabo Verdean": "Q1011",
    "Mosotho": "Q1013",
    "Liberian": "Q1014",
    "Libyan": "Q1016",
    "Malagasy": "Q1019",
    "Malawian": "Q1020",
    "Mauritanian": "Q1025",
    "Mauritian": "Q1027",
    "Moroccan": "Q1028",
    "Mozambican": "Q1029",
    "Namibian": "Q1030",
    "Nigerien": "Q1032",
    "Nigerian": "Q1033",
    "Ugandan": "Q1036",
    "Rwandan": "Q1037",
    "São Toméan": "Q1039",
    "Senegalese": "Q1041",
    "Seychellois": "Q1042",
    "Sierra Leonean": "Q1044",
    "Somali": "Q1045",
    "Sudanese": "Q1049",
    "Kenyan": "Q114",
    "Ethiopian": "Q115",
    "Ghanaian": "Q117",
    "French": "Q142",
    "British": "Q145",
    "Chinese": "Q148",
    "Brazilian": "Q155",
    "Russian": "Q159",
    "Canadian": "Q16",
    "Japanese": "Q17",
    "German": "Q183",
    "Belarusian": "Q184",
    "Icelandic": "Q189",
    "Estonian": "Q191",
    "Norwegian": "Q20",
    "Latvian": "Q211",
    "Czech": "Q213",
    "Slovak": "Q214",
    "Slovenian": "Q215",
    "Moldovan": "Q217",
    "Romanian": "Q218",
    "Bulgarian": "Q219",
    "Palestinian": "Q219060",
    "Macedonian": "Q221",
    "Albanian": "Q222",
    "Croatian": "Q224",
    "Bosnian": "Q225",
    "Azerbaijani": "Q227",
    "Andorran": "Q228",
    "Cypriot": "Q229",
    "Georgian": "Q230",
    "Kazakhstani": "Q232",
    "Maltese": "Q233",
    "Monégasque": "Q235",
    "Montenegrin": "Q236",
    "Vatican": "Q237",
    "Sammarinese": "Q238",
    "Cuban": "Q241",
    "Belizean": "Q242",
    "Barbadian": "Q244",
    "Indonesian": "Q252",
    "South African": "Q258",
    "Algerian": "Q262",
    "Uzbek": "Q265",
    "Irish": "Q27",
    "Hungarian": "Q28",
    "Spanish": "Q29",
    "Chilean": "Q298",
    "Dutch": "Q29999",
    "American": "Q30",
    "Belgian": "Q31",
    "Luxembourgian": "Q32",
    "Finnish": "Q33",
    "Singaporean": "Q334",
    "Swedish": "Q34",
    "Liechtensteiner": "Q347",
    "Polish": "Q36",
    "Lithuanian": "Q37",
    "Italian": "Q38",
    "Swiss": "Q39",
    "Bahraini": "Q398",
    "Armenian": "Q399",
    "Austrian": "Q40",
    "Serbian": "Q403",
    "Australian": "Q408",
    "Greek": "Q41",
    "Argentinian": "Q414",
    "Peruvian": "Q419",
    "North Korean": "Q423",
    "Cambodian": "Q424",
    "Turkish": "Q43",
    "Portuguese": "Q45",
    "Chadian": "Q657",
    "New Zealand": "Q664",
    "Indian": "Q668",
    "Tuvaluan": "Q672",
    "Tongan": "Q678",
    "Samoan": "Q683",
    "Vanuatuan": "Q686",
    "Papua New Guinean": "Q691",
    "Palauan": "Q695",
    "Nauruan": "Q697",
    "I-Kiribati": "Q710",
    "Mongolian": "Q711",
    "Fijian": "Q712",
    "Venezuelan": "Q717",
    "Surinamese": "Q730",
    "Paraguayan": "Q733",
    "Guyanese": "Q734",
    "Ecuadorian": "Q736",
    "Colombian": "Q739",
    "Bolivian": "Q750",
    "Trinidadian": "Q754",
    "Danish": "Q756617",
    "Jamaican": "Q766",
    "Grenadian": "Q769",
    "Uruguayan": "Q77",
    "Guatemalan": "Q774",
    "Bahamian": "Q778",
    "Honduran": "Q783",
    "Egyptian": "Q79",
    "Haitian": "Q790",
    "Salvadoran": "Q792",
    "Iranian": "Q794",
    "Iraqi": "Q796",
    "Costa Rican": "Q800",
    "Israeli": "Q801",
    "Panamanian": "Q804",
    "Yemeni": "Q805",
    "Jordanian": "Q810",
    "Nicaraguan": "Q811",
    "Kyrgyz": "Q813",
    "Kuwaiti": "Q817",
    "Laotian": "Q819",
    "Lebanese": "Q822",
    "Maldivian": "Q826",
    "Malaysian": "Q833",
    "Burmese": "Q836",
    "Nepalese": "Q837",
    "Omani": "Q842",
    "Pakistani": "Q843",
    "Qatari": "Q846",
    "Saudi": "Q851",
    "Sri Lankan": "Q854",
    "Syrian": "Q858",
    "Tajikistani": "Q863",
    "Thai": "Q869",
    "Turkmen": "Q874",
    "Emirati": "Q878",
    "Vietnamese": "Q881",
    "South Korean": "Q884",
    "Afghan": "Q889",
    "Bangladeshi": "Q902",
    "Malian": "Q912",
    "Angolan": "Q916",
    "Bhutanese": "Q917",
    "Tanzanian": "Q924",
    "Filipino": "Q928",
    "Togolese": "Q945",
    "Tunisian": "Q948",
    "Zambian": "Q953",
    "Zimbabwean": "Q954",
    "Mexican": "Q96",
    "Beninois": "Q962",
    "Botswanan": "Q963",
    "Burkinabe": "Q965",
    "Burundian": "Q967",
    "Comorian": "Q970",
    "Congolese": "Q974",
    "Djiboutian": "Q977",
    "Equatoguinean": "Q983",
    "Eritrean": "Q986",
    "Bermudian": "",
    "Bruneian": "Q921",
    # "Greenlandic": "",
    "Kiribati": "Q710",
    "Kosovan": "Q1246",
    # "Macanese": "",
    "Puerto Rican": "Q1183",
    "Timorese": "Q574",
    "Ukrainian": "Q212",
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
        logger.info(f" topic:{lab}")
    # ---
    if not lab:
        logger.info(f"{p106_lab=} {p27_lab=}")
        return ""
    # ---
    if "returnlab" in sys.argv:
        return lab
    # ---
    logger.info(f"<<yellow>> lab:{lab} add 'returnlab' to sys.argv to use it..!!")
    # ---
    return ""

def print_new_jobs():
    lists = [[y, x] for x, y in new_jobs.items()]
    lists.sort(reverse=True)
    # ---
    for lenth, qid in lists:
        # ---
        logger.info(f"new_jobs:{lenth} : qid:{qid}")
    # ---
    lists1 = [[y, x] for x, y in new_nats.items()]
    lists1.sort(reverse=True)
    # ---
    for lenth, qid in lists1:
        # ---
        logger.info(f"new_nats:{lenth} : qid:{qid}")
    # ---

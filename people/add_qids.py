#!/usr/bin/python3
"""

python3 core8/pwb.py people/add_qids

SELECT ?item ?dem WHERE {
  ?item wdt:P31 wd:Q3624078;
    wdt:P1549 ?dem.
  filter (lang(?dem) = "en")
}


SELECT
(concat('"',str(?dem),'":"', strafter(str(?item),"/entity/"),'",') as ?333)

WHERE {
  ?item wdt:P31 wd:Q12737077;
    wdt:P3321 ?dem.
  filter (lang(?dem) = "en")
}

"""

from people.people_get_topic import job_to_qid, nat_to_qid

uux = {
    "accountant": "Q326653",
    "actor": "Q33999",
    "advertising installer": "Q109934711",
    "allied health professional": "Q55071047",
    "application programmer": "Q613431",
    "aquaculture cage mooring worker": "Q109985391",
    "attraction operator": "Q109934184",
    "bank teller": "Q806805",
    "bartender": "Q808266",
    "building engineer": "Q21778977",
    "buyer": "Q1308239",
    "chemical engineer": "Q7888586",
    "chemist": "Q593644",
    "civil engineer": "Q13582652",
    "coachman": "Q1221610",
    "crop production worker": "Q110002200",
    "data entry clerk": "Q918751",
    "dentist": "Q27349",
    "driving instructor": "Q678003",
    "economist": "Q188094",
    "education manager": "Q108290311",
    "electrical engineer": "Q1326886",
    "electronic engineer": "Q108140949",
    "environmental engineer": "Q19377727",
    "financial analyst": "Q1416279",
    "firefighter": "Q107711",
    "food preparation assistants": "Q108289055",
    "food preparation assistants": "Q108303218",
    "forestry worker": "Q12335817",
    "freight handler": "Q30921607",
    "general practitioner": "Q6500773",
    "general secretary": "Q6501749",
    "glazier": "Q664283",
    "hairdresser": "Q55187",
    "health professional": "Q11974939",
    "high-school teacher": "Q5758653",
    "hotel manager": "Q1631120",
    "insulation worker": "Q108305396",
    "journalist": "Q1930187",
    "judge": "Q16533",
    "kitchen assistant": "Q1796839",
    "landscape architect": "Q2815948",
    "laundromat attendant": "Q109932790",
    "leaflet distributor": "Q109943861",
    "legal secretary": "Q15403960",
    "legislator": "Q4175034",
    "locker room attendant": "Q109906114",
    "manager": "Q2462658",
    "mathematician": "Q170790",
    "mechanical engineer": "Q1906857",
    "medical specialist": "Q3332438",
    "meteorologist": "Q2310145",
    "meter reader": "Q109936996",
    "music teacher": "Q2675537",
    "newspaper vendor": "Q109943280",
    "official": "Q599151",
    "on foot aquatic resources collector": "Q109985212",
    "peddler": "Q638172",
    "pharmacist": "Q105186",
    "physician": "Q39631",
    "physiotherapist": "Q694748",
    "plasterer": "Q15284879",
    "police officer": "Q361593",
    "printer": "Q175151",
    "prison officer": "Q311396",
    "professional photographer": "Q98084799",
    "psychologist": "Q212980",
    "rail layer": "Q109982660",
    "recycling worker": "Q109937477",
    "road maintenance worker": "Q109983547",
    "road marker": "Q109983376",
    "sewerage cleaner": "Q110148239",
    "shelf filler": "Q109953281",
    "shopkeeper": "Q7501153",
    "singer": "Q177220",
    "software developer": "Q183888",
    "sorter labourer": "Q109937424",
    "special education teacher": "Q1030095",
    "stage magician": "Q15855449",
    "stock clerk": "Q2145570",
    "surveyor": "Q294126",
    "swimming pool attendant": "Q110148099",
    "system administrator": "Q327353",
    "systems analyst": "Q942569",
    "telecommunications engineer": "Q12246069",
    "travel guide": "Q2073907",
    "tribal chief": "Q1259323",
    "vending machine operator": "Q109936724",
    "veterinarian": "Q202883",
    "vineyard worker": "Q110008263",
    "visual artist": "Q3391743",
    "vocational teacher": "Q829057",
    "waiter": "Q157195",
    "wood carrier": "Q109936679",
}

for x, q in job_to_qid.items():
    x2 = x.replace("~", "").strip().lower()

    qid = q if q else uux.get(x, "")

    print(f'    "{x}": "{qid}",')

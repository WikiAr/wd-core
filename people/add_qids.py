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


SELECT DISTINCT
(concat('"',str(?label),'":"', strafter(str(?item),"/entity/"),'",') as ?333)

WHERE {
  values ?label {
    "businessman and philanthropist"@en
    "actor"@en
    }
  ?item wdt:P2521 ?P2521.
  ?item rdfs:label ?label
  filter (lang(?label) = "en")

}

"""

from people.people_get_topic import job_to_qid, nat_to_qid

uux = {
    "academic": "Q3400985",
    "alpine skier": "Q4144610",
    "anatomist": "Q10872101",
    "anthropologist": "Q4773904",
    "archbishop": "Q49476",
    "archer": "Q13382355",
    "archivist": "Q635734",
    "association football referee": "Q859528",
    "astronomer": "Q11063",
    "basketball coach": "Q5137571",
    "basketball player": "Q3665646",
    "biathlete": "Q16029547",
    "biologist": "Q864503",
    "botanist": "Q2374149",
    "boxer": "Q11338576",
    "caricaturist": "Q3658608",
    "cartographer": "Q1734662",
    "chef": "Q3499072",
    "chess player": "Q10873124",
    "choreographer": "Q2490358",
    "comics artist": "Q715301",
    "dermatologist": "Q2447386",
    "diplomat": "Q193391",
    "educator": "Q974144",
    "egyptologist": "Q1350189",
    "engineer": "Q81096",
    "engraver": "Q329439",
    "essayist": "Q11774202",
    "field hockey player": "Q10843263",
    "film actor": "Q10800557",
    "film critic": "Q4220892",
    "film director": "Q2526255",
    "film producer": "Q3282637",
    "flying ace": "Q222982",
    "football player": "Q117321337",
    "geneticist": "Q3126128",
    "geographer": "Q901402",
    "gymnast": "Q16947675",
    "handball player": "Q12840545",
    "historian": "Q201788",
    "illustrator": "Q644687",
    "jurist": "Q185351",
    "lawyer": "Q40348",
    "legal historian": "Q2135538",
    "lexicographer": "Q14972848",
    "literary critic": "Q4263842",
    "medievalist": "Q3332711",
    "military officer": "Q189290",
    "mineralogist": "Q13416354",
    "missionary": "Q219477",
    "motorcycle racer": "Q3014296",
    "musicologist": "Q14915627",
    "mycologist": "Q2487799",
    "neurologist": "Q783906",
    "novelist": "Q6625963",
    "oncologist": "Q16062369",
    "orientalist": "Q1731155",
    "papyrologist": "Q16267158",
    "pathologist": "Q3368718",
    "pharmacologist": "Q2114605",
    "philologist": "Q13418253",
    "physicist": "Q169470",
    "physiologist": "Q2055046",
    "playwright": "Q214917",
    "poet": "Q49757",
    "political scientist": "Q1238570",
    "politician": "Q82955",
    "psychiatrist": "Q211346",
    "psychoanalyst": "Q3410028",
    "rabbi": "Q133485",
    "racing driver": "Q378622",
    "radiologist": "Q18245236",
    "rally driver": "Q10842936",
    "rugby union player": "Q14089670",
    "scientist": "Q901",
    "screenwriter": "Q28389",
    "sculptor": "Q1281618",
    "soldier": "Q4991371",
    "speleologist": "Q16742175",
    "sport cyclist": "Q2309784",
    "sprinter": "Q4009406",
    "spy": "Q9352089",
    "surgeon": "Q774306",
    "tennis player": "Q10833314",
    "theologian": "Q1234713",
    "translator": "Q333634",
    "university teacher": "Q1622272",
    "virologist": "Q15634281",
    "volleyball player": "Q15117302",
    "water polo player": "Q17524364",
    "zoologist": "Q350979",
}

for x, q in job_to_qid.items():
    x2 = x.replace("~", "").strip().lower()

    qid = q if q else uux.get(x, "")

    print(f'    "{x}": "{qid}",')

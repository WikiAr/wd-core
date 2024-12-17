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
}

for x, q in job_to_qid.items():
    x2 = x.replace("~", "").strip().lower()

    qid = q if q else uux.get(x, "")

    print(f'    "{x}": "{qid}",')

#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
# ---
quuu = {}
quuu['species of beetle'] = """
SELECT DISTINCT
?item ?en2 WHERE {
  BIND("espèce de coléoptères"@fr AS ?fr) ?item schema:description ?fr.
  BIND("specie di coleottero"@it AS ?it) ?item schema:description ?it.
  BIND("species of beetle"@en AS ?en) ?item schema:description ?en.
  #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 20000"""
quuu['species of insect'] = """
SELECT DISTINCT
?item ?en2 WHERE {
  BIND("espèce de coléoptères"@fr AS ?fr) ?item schema:description ?fr.
  BIND("specie di coleottero"@it AS ?it) ?item schema:description ?it.
  BIND("species of insect"@en AS ?en) ?item schema:description ?en.
  #OPTIONAL { ?item schema:description ?en2. FILTER((LANG(?en2)) = "en") }
}
LIMIT 20000"""
# ---
# from API.replacement import replacement
# ---
translations = {
    'species of beetle': {
        'it': 'specie di coleotteri',
        'fr': 'espèces de coléoptères',

    },
    'species of insect': {
        'it': 'specie di insetti',
        'fr': "espèces d'insectes",

    },
}
# ---
# start of newdesc.py file

# newdesc.main_from_file(file, topic, translations2)
# newdesc.mainfromQuarry ( topic, Quarry, translations)
# newdesc.mainfromQuarry2( topic, Quarry, translations)
# ---
if __name__ == "__main__":
    for x in translations:
        newdesc.mainfromQuarry(x, quuu[x], translations)
# ---

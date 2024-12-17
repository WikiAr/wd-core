#!/usr/bin/python3
"""


بوت إضافة الوصوف عن الأشخاص في ويكي بيانات

جميع اللغات

https://github.com/emijrp/wikidata/blob/master/human.descriptions.py


"""
#
# (C) Ibrahem Qasim, 2022
#
#
from pathlib import Path
import json

# ---
Dir = Path(__file__).parent
# ---
translationsNationalities = {}
# ---
with open(f"{Dir}/translationsNationalities.json", "r", encoding="utf-8") as f:
    translationsNationalities = json.load(f)
# ---
translationsNationalities["Luxembourgian"] = translationsNationalities["Luxembourg"]
translationsNationalities["New Zealander"] = translationsNationalities["New Zealand"]
# ---
tra = translationsNationalities

if __name__ == "__main__":
    # python3 core8/pwb.py people/Nationalities
    for k in tra.keys():
        print(f'\t"{k}" : "",')

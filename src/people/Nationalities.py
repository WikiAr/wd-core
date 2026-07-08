#!/usr/bin/python3
"""


بوت إضافة الوصوف عن الأشخاص في ويكي بيانات

جميع اللغات

https://github.com/emijrp/wikidata/blob/master/human.descriptions.py


"""

import json
from pathlib import Path

Dir = Path(__file__).parent

TRANSLATIONS_NATIONALITIES = {}

with open(f"{Dir}/translationsNationalities.json", "r", encoding="utf-8") as f:
    TRANSLATIONS_NATIONALITIES = json.load(f)

TRANSLATIONS_NATIONALITIES["Luxembourgian"] = TRANSLATIONS_NATIONALITIES["Luxembourg"]
TRANSLATIONS_NATIONALITIES["New Zealander"] = TRANSLATIONS_NATIONALITIES["New Zealand"]

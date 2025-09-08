import sys
import json
import re
import requests
from tqdm import tqdm
from pathlib import Path

Dir = Path(__file__).parent
dump_path = Dir / "forms"
dump_path.mkdir(exist_ok=True)

file_uthmani = Dir / "quran-uthmani.json"
if file_uthmani.exists():
    # تحميل القرآن من الملف المحلي
    with open(Dir / "quran-uthmani.json", "r", encoding="utf-8") as f:
        quran_data = json.load(f)
else:
    # تحميل القرآن من موقع quran.com
    url = "https://api.alquran.cloud/v1/quran/quran-uthmani"
    response = requests.get(url)
    quran_data = response.json()
    with open(file_uthmani, "w", encoding="utf-8") as f:
        json.dump(quran_data, f, ensure_ascii=False, indent=4)

surahs = quran_data["data"]["surahs"]

words_to_add = {}

for surah in tqdm(surahs):
    for ayah in surah["ayahs"]:
        for word in ayah["text"].split(" "):
            # ---
            if word not in words_to_add:
                words_to_add[word] = []
            # ---
            words_to_add[word].append({
                "sura": surah["number"],
                "sura_name": surah["name"],
                "aya": ayah["numberInSurah"],
                "text": ayah["text"]
            })


def search_in_quran_new(word):
    results = words_to_add.get(word, [])
    return results

# دالة جلب الأشكال من Wikidata


def get_forms_from_lexeme(lexeme_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{lexeme_id}.json"
    headers = {
        "User-Agent": "MyQuranLexemeBot/1.0 (example@example.com)"
    }
    r = requests.get(url, headers=headers)
    data = r.json()

    entity = data["entities"][lexeme_id]
    forms = entity.get("forms", [])
    results = {}
    already_has = 0
    for form in forms:
        form_id = form["id"]
        arabic_value = form.get("representations", {}).get("ar", {}).get("value")

        if not arabic_value:
            continue

        if 'claims' in form and 'P5831' in form['claims']:
            already_has += 1
        else:
            matches = search_in_quran_new(arabic_value)
            if matches:
                results[form_id] = matches[0]
    # print(f"{lexeme_id} \t forms: {len(forms)} \t results: {len(results)} \t already_has: {already_has}")

    return results


def get_arabic_lexemes():
    file = Dir / "all_arabic_by_category.json"
    with open(file, "r", encoding="utf-8") as f:
        data = json.load(f)

    categoryLabels = {
        "Q1084": "اسم",
        "Q24905": "فعل",
        "Q34698": "صفة",
        # "Q1050744": "اسم موصول",
        # "Q111029": "جذر",
        # "Q11563": "عدد",
        # "Q1167104": "ظرف رابط",
        # "Q1401131": "الجملة الاسمية",
        # "Q147276": "اسم علم",
        # "Q161873": "أداة جر لاحقة",
        # "Q184943": "حرف معنى",
        # "Q2146100": "ضمير  استئنافي",
        # "Q2865743": "أداة تعريف",
        # "Q29888377": "عبارة اسمية",
        # "Q34793275": "ضمير إشارة",
        # "Q36224": "ضمير",
        # "Q36484": "حرف ربط",
        # "Q380057": "ظرف",
        # "Q468801": "ضمير شخصي",
        # "Q4833830": "حرف جر",
        # "Q503992": "الاسم الوظيفي",
        # "Q576271": "مُحدِّد",
        # "Q63116": "اسم عدد",
        # "Q65279776": "أداة نفي",
        # "Q83034": "التعجب",
        # "Q9788": "حرف",
    }
    lexemes = []
    for item, tab in data["list"].items():
        if item not in categoryLabels:
            continue
        lexemes.extend(list(tab.keys()))
    return lexemes


def start():
    lexemes = get_arabic_lexemes()
    for lexeme_id in tqdm(lexemes):
        extracted = get_forms_from_lexeme(lexeme_id)
        if extracted:
            with open(dump_path / f"{lexeme_id}.json", "w", encoding="utf-8") as f:
                json.dump(extracted, f, ensure_ascii=False, indent=2)


def test():
    lexeme_id = "L1478647"
    extracted = get_forms_from_lexeme(lexeme_id)

    with open(Dir / "forms_examples.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)

    print("saved forms_examples.json ✅")


if __name__ == "__main__":
    if "test" in sys.argv:
        test()
    else:
        start()

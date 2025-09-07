import json
import requests

# --------------------------
# تحميل القرآن من الملف المحلي
# --------------------------
with open("quran-uthmani.json", "r", encoding="utf-8") as f:
    quran_data = json.load(f)

surahs = quran_data["data"]["surahs"]

# --------------------------
# دالة البحث داخل القرآن
# --------------------------


def search_in_quran(word):
    results = []
    for surah in surahs:
        for ayah in surah["ayahs"]:
            if word in ayah["text"]:
                results.append({
                    "sura": surah["number"],
                    "sura_name": surah["name"],
                    "aya": ayah["numberInSurah"],
                    "text": ayah["text"]
                })
    return results

# --------------------------
# دالة جلب الأشكال من Wikidata
# --------------------------


def get_forms_from_lexeme(lexeme_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{lexeme_id}.json"
    headers = {
        "User-Agent": "MyQuranLexemeBot/1.0 (example@example.com)"
    }
    r = requests.get(url, headers=headers)
    data = r.json()

    entity = data["entities"][lexeme_id]
    forms = entity.get("forms", [])
    results = []

    for form in forms:
        form_id = form["id"]
        arabic_value = form.get("representations", {}).get("ar", {}).get("value")

        if not arabic_value:
            continue

        if 'claims' not in form or 'P5831' not in form['claims']:

            # البحث في القرآن
            matches = search_in_quran(arabic_value)
            if matches:
                verse = matches[0]  # نأخذ أول تطابق
                results.append({
                    "form_id": form_id,
                    "word": arabic_value,
                    "example": verse["text"],
                    "sura": verse["sura"],
                    "sura_name": verse["sura_name"],
                    "aya": verse["aya"]
                })

    return results


# --------------------------
# مثال للتنفيذ
# --------------------------
if __name__ == "__main__":
    lexeme_id = "L1478647"  # ضع هنا رقم اللغيمة
    extracted = get_forms_from_lexeme(lexeme_id)

    with open("forms_examples.json", "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)

    print("تم حفظ النتائج في forms_examples.json ✅")

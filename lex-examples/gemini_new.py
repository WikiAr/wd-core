import sys
import json
import time
import requests
from tqdm import tqdm
from pathlib import Path
from SPARQLWrapper import SPARQLWrapper, JSON

Dir = Path(__file__).parent

dump_path = Dir / "forms"
empty_dump_path = Dir / "no_forms"

dump_path.mkdir(exist_ok=True)
empty_dump_path.mkdir(exist_ok=True)


# تحميل القرآن من موقع quran.com
url = "https://api.alquran.cloud/v1/quran/quran-uthmani"
# ---
session = requests.session()
session.headers.update({"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"})
# ---
response = session.get(url, timeout=10)
quran_data = response.json()

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


def get_forms_from_lexeme(lexeme_id):
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{lexeme_id}.json"
    # ---
    session = requests.session()
    session.headers.update({"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"})
    # ---
    r = session.get(url)
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

    return results, already_has


def get_results(query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    endpoint_url = 'https://query.wikidata.org/sparql'
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    # ---
    data = sparql.query().convert()
    # ---
    # تنسيق النتائج
    result = []

    items = data.get("results", {}).get("bindings", [])
    vars_list = data.get("head", {}).get("vars", [])

    for row in items:
        new_row = {}
        # ---
        for var in vars_list:
            value = row.get(var, {}).get("value", "")
            # ---
            if value.count("/entity/") == 1:
                value = value.split("/").pop()
            # ---
            new_row[var] = value
        # ---
        result.append(new_row)

    return result


def get_arabic_lexemes_new():
    # ---
    sparql_query = """
        SELECT ?item (COUNT(?form) as ?forms)
        WHERE {
            VALUES ?category { wd:Q24905 wd:Q34698 wd:Q1084 } .
            ?item dct:language wd:Q13955.
            ?item wikibase:lexicalCategory ?category.
            ?item wikibase:lemma ?lemma.
            ?item ontolex:lexicalForm ?form .
        }

        GROUP BY ?item
        HAVING (COUNT(?form) > 1)

        order by DESC (COUNT(?form))

    """
    # ---
    data = get_results(sparql_query)
    # ---
    data = {x["item"] : int(x["forms"]) for x in data}
    # ---
    # sort data by forms
    # data = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))
    # ---
    # sort data by item
    data = dict(sorted(data.items(), key=lambda item: item[0]))
    # ---
    return data


no_examples = 0
file_exists = 0
all_already_has = 0

time_parts = time.time()


def print_status():
    global time_parts
    # ---
    in_time = time.time() - time_parts
    time_parts = time.time()
    # ---
    print(f"Time: {in_time:.2f} seconds")
    # ---
    print(f"file_exists: {file_exists:,}")
    print(f"no_examples: {no_examples:,}")
    print(f"forms with examples: {all_already_has:,}")


lexemes = get_arabic_lexemes_new()
# ---
for n, lexeme_id in tqdm(enumerate(lexemes), total=len(lexemes)):
    # ---
    if n % 500 == 0:
        print_status()
    # ---
    file = dump_path / f"{lexeme_id}.json"
    file2 = empty_dump_path / f"{lexeme_id}.json"
    # ---
    if file.exists() or file2.exists():
        file_exists += 1
        continue
    # ---
    extracted, already_has = get_forms_from_lexeme(lexeme_id)
    # ---
    all_already_has += already_has
    # ---
    if not extracted:
        no_examples += 1
        file = file2
    # ---
    with open(file, "w", encoding="utf-8") as f:
        json.dump(extracted, f, ensure_ascii=False, indent=2)
# ---
print("Done.")
print(f"all lexemes: {len(lexemes):,}")
print_status()

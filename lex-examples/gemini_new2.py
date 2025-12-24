import sys
import json
import requests
from tqdm import tqdm
from pathlib import Path
from SPARQLWrapper import SPARQLWrapper, JSON


Dir = Path(__file__).parent
dump_path = Dir / "forms"
dump_path.mkdir(exist_ok=True)


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


def get_forms_from_lexeme(forms):
    # ---
    try:
        forms = json.loads(forms)
    except json.decoder.JSONDecodeError:
        return []
    # ---
    results = {}
    # ---
    for form in forms:
        # ---
        matches = search_in_quran_new(form["word"])
        # ---
        if matches:
            results[form["id"]] = matches[0]
    # ---
    return results


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


def get_arabic_lexemes_new(limit, offset):
    # ---
    sparql_query = """
        SELECT ?item ?category (CONCAT(
                "[",
                GROUP_CONCAT(
                    CONCAT(
                        '{"id":"', STRAFTER(STR(?form), "/entity/"),
                        '", "word":"', STR(?word), '"}'
                    );
                    separator=", "
                ),
                "]"
            ) AS ?forms)
        WHERE {
        VALUES ?category { wd:Q24905 wd:Q34698 wd:Q1084 } .
        ?item a ontolex:LexicalEntry.
        ?item wikibase:lexicalCategory ?category.
        ?item dct:language wd:Q13955.
        ?item ontolex:lexicalForm ?form .
        ?form ontolex:representation ?word .
        }
        GROUP BY ?item ?category
    """
    # ---
    sparql_query += f"\n\n LIMIT {limit} OFFSET {offset}"
    # ---
    data = get_results(sparql_query)
    # ---
    result = {x['item']: x['forms'] for x in data}
    # ---
    return result


def start():
    # ---
    limit = 50
    offset = 0
    # ---
    total_queries = 0
    # ---
    while True:
        # ---
        total_queries += 1
        # ---
        lexemes = get_arabic_lexemes_new(limit, offset)
        # ---
        if not lexemes:
            break
        # ---
        offset += limit
        # ---
        for lexeme_id, forms in tqdm(lexemes.items()):
            extracted = get_forms_from_lexeme(forms)
            if extracted:
                with open(dump_path / f"{lexeme_id}.json", "w", encoding="utf-8") as f:
                    json.dump(extracted, f, ensure_ascii=False, indent=2)
    # ---
    print(f"Done, total_queries: {total_queries}")


if __name__ == "__main__":
    start()

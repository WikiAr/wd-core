import requests
import json
import re


def get_forms_from_wikidata(lexeme_id):
    """
    Retrieves forms of an Arabic lexeme from Wikidata.
    """
    headers = {
        'User-Agent': 'MyWikidataLexemeBot/1.0 (dev.mounir.info@gmail.com)'
    }
    url = f"https://www.wikidata.org/wiki/Special:EntityData/{lexeme_id}.json"
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        lexeme_data = data['entities'][lexeme_id]
        return lexeme_data.get('forms', [])
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for {lexeme_id}: {e}")
        return []


def get_quran_text_from_file(file_path="quran-uthmani.json"):
    """
    Reads the full Arabic text of the Quran from a local JSON file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['data']['surahs']
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file_path}'. Check file format.")
        return []


def search_quran_for_word(word, quran_data):
    """
    Searches for a specific word in the Quran data.
    """
    for surah in quran_data:
        for ayah in surah['ayahs']:
            # Using a word boundary to ensure we match the full word, not a part of it
            # The pattern is: \b + word + \b
            if re.search(r'\b' + re.escape(word) + r'\b', ayah['text']):
                return {
                    "ayah_text": ayah['text'],
                    "surah_name": surah['name'],
                    "ayah_number": ayah['numberInSurah']
                }
    return None


def process_lexeme(lexeme_id, quran_file_path, output_file="output.json"):
    """
    Main function to process the lexeme, find examples, and save to a JSON file.
    """
    forms = get_forms_from_wikidata(lexeme_id)
    if not forms:
        print("No forms found for this lexeme.")
        return

    quran_data = get_quran_text_from_file(quran_file_path)
    if not quran_data:
        print("Could not retrieve Quran data from file.")
        return

    results = []

    for form in forms:
        form_id = form.get('id')
        arabic_value = form.get('representations', {}).get('ar', {}).get('value')

        if not arabic_value:
            continue

        if 'claims' not in form or 'P5831' not in form['claims']:

            quran_example = search_quran_for_word(arabic_value, quran_data)
            if quran_example:
                results.append({
                    "form_id": form_id,
                    "word": arabic_value,
                    "source": "Quran",
                    "example": quran_example["ayah_text"],
                    "surah_name": quran_example["surah_name"],
                    "ayah_number": quran_example["ayah_number"]
                })

    # Save results to a JSON file
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=4)

    print(f"Processing complete. Results saved to {output_file}.")


# Run the script with your desired lexeme ID and the path to your Quran JSON file
lexeme_id_to_process = "L1478647"  # Example for 'ضرب'
quran_json_file = "quran-uthmani.json"
process_lexeme(lexeme_id_to_process, quran_json_file)

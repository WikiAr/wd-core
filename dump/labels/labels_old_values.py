"""
from dump.labels.labels_old_values import make_old_values# make_old_values()
"""
import os
from pathlib import Path
import json
import sys
import codecs
import re
import requests
Session = requests.Session()
dir2 = Path(__file__).parent

file_old_data = f'{dir2}/old_data.json'

if not os.path.isfile(file_old_data):
    print(f'create file_old_data:{file_old_data}..')
    with open(file_old_data, 'w', encoding='utf-8') as f:
        json.dump({}, f)

with open(file_old_data, 'r', encoding='utf-8') as f:
    _old_data = json.load(f)
_old_data = _old_data.get('langs') or _old_data


def GetPageText(title):
    params = {"action": "parse", "prop": "wikitext|sections", "page": title, 'format': 'json', 'utf8': 1}
    # ---
    end_point = 'https://www.wikidata.org/w/api.php?'
    # ---
    json1 = Session.post(end_point, data=params).json()
    # ---
    if not json1 or json1 == {}:
        return ''
    # ---
    text = json1.get("parse", {}).get("wikitext", {}).get("*", "")
    # ---
    if text == "":
        print(f'no text for {title}')
    # ---
    return text


def from_wiki():
    # ---
    print('from_wiki')
    # ---
    title = 'User:Mr. Ibrahem/Language statistics for items'
    # ---
    Old = {}
    # ---
    texts = GetPageText(title)
    # texts = codecs.open(f'{dir2}/te.txt', 'r', encoding='utf-8').read()
    # ---
    texts = texts.replace(',', '')
    # ---
    last_total = 0
    # ---
    # find text like: * Total items:106069526
    io = re.search(r"\* Total items:(\d+)\.", texts)
    if io:
        last_total = int(io.group(1))
    # ---
    Old['last_total'] = last_total
    # ---
    texts = texts.split('|}')[0]
    texts = texts.replace('|}', '')
    for L in texts.split('|-'):
        L = L.strip()
        L = L.replace('\n', '|')
        if L.find('{{#language:') != -1:
            L = re.sub(r'\d+\.\d+\%', '', L)
            L = re.sub(r'\|\|\s*\+\d+\s*', '', L)
            L = re.sub(r'\|\|\s*\-\d+\s*', '', L)
            L = re.sub(r'\s*\{\{\#language\:.*?\}\}\s*', '', L)
            L = re.sub(r'\s*\|\|\s*', '||', L)
            L = re.sub(r'\s*\|\s*', '|', L)
            L = L.replace('||||', '||')
            L = L.replace('||||', '||')
            L = L.replace('||||', '||')
            L = L.replace('||||', '||')
            L = L.strip()
            if 'test' in sys.argv:
                print(L)
            iu = re.search(r"\|(.*?)\|\|(\d*)\|\|(\d*)\|\|(\d*)", L)
            if iu:
                lang = iu.group(1).strip()
                Old[lang] = {'labels': 0, 'descriptions': 0, 'aliases': 0, 'all': 0}

                if iu.group(2):
                    Old[lang]['all'] += int(iu.group(2))
                    Old[lang]['labels'] = int(iu.group(2))

                if iu.group(3):
                    Old[lang]['all'] += int(iu.group(3))
                    Old[lang]['descriptions'] = int(iu.group(3))

                if iu.group(4):
                    Old[lang]['all'] += int(iu.group(4))
                    Old[lang]['aliases'] = int(iu.group(4))

    print(f'get data from page len of old data:{len(Old)}')
    return Old


def make_old_values():
    # ---
    if len(_old_data) > 5 and 'old' in sys.argv:
        print('data in the file..')
        json.dump(_old_data, codecs.open(file_old_data, 'w', 'utf-8'), indent=4)
        return _old_data
    # ---
    print('get data from page')
    # ---
    Old = from_wiki()
    # ---
    json.dump(Old, codecs.open(file_old_data, 'w', 'utf-8'), indent=4)
    # ---
    return Old


if __name__ == "__main__":
    make_old_values()

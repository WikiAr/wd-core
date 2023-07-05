"""
from dump.bots.labels_old_values import make_old_values# make_old_values()
"""
from API import himoBOT2
import os
import json
import sys
import re
dir2 = os.path.dirname(os.path.realpath(__file__))
dir2 = os.path.dirname(dir2)

file = f'{dir2}/new_data.json'
if not os.path.isfile(file):
    # create it
    with open(file, 'w') as f:
        f.write('{}')

_old_data = json.load(open(file))

title = 'User:Mr. Ibrahem/Language statistics for items'

def from_wiki():
    # ---
    Old = {}
    # ---
    texts = himoBOT2.GetPageText(title.replace(' ', '_'), 'www', family='wikidata')
    # ---
    texts = texts.split('|}')[0]
    texts = texts.replace('|}', '')
    texts = texts.replace(',', '')
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
                Old[lang] = {'labels': 0, 'descriptions': 0, 'aliases': 0}

                if iu.group(2):
                    Old[lang]['labels'] = int(iu.group(2))

                if iu.group(3):
                    Old[lang]['descriptions'] = int(iu.group(3))

                if iu.group(4):
                    Old[lang]['aliases'] = int(iu.group(4))
    return Old


def make_old_values():
    # ---
    if len(_old_data) > 5:
        return _old_data
    # ---
    Old = from_wiki()
    # ---
    return Old

if __name__ == "__main__":
    from_wiki()
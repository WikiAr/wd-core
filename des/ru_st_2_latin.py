'''
# ---
from des.ru_st_2_latin import make_en_label
# enlabel = make_en_label(labels, q, Add=False)
# ---
python3 core8/pwb.py des/ru_st_2_latin test

'''
from pywikibot.pagegenerators import WikidataSPARQLPageGenerator
from wd_api import himoAPI
import pywikibot
import sys
# ---
letters_to_latin = {
    "ru": {
        "а": "a",
        "б": "b",
        "д": "d",
        "е": "e",
        "ф": "f",
        "г": "g",
        "и": "i",
        "ю": "ju",
        "к": "k",
        "л": "l",
        "м": "m",
        "н": "n",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "в": "v",
        "й": "y",
        "з": "z",
        "А": "A",
        "Б": "B",
        "Д": "D",
        "Э": "E",
        "Ф": "F",
        "Г": "G",
        "Х": "H",
        "И": "I",
        "Ю": "Ju",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "В": "V",
        "Й": "Y",
        "З": "Z",
        "ж": "zj",
        "э": "e",
        "л": "l",
        " ": " ",
        "?": "?",
        "ш": "sj",
        "ч": "tsj",
        ",": ",",
        "у": "oe",
        "ы": "i",
        "Ы": "I",
        "Щ": "Sjtsj",
        "щ": "sjtsj",
        "х": "ch",
        "У": "Oe",
        "ц": "ts",
        "-": "-",
        "Ж": "Zj",
        "Я": "Ja",
        "я": "ja",
        "Ш": "Sj",
        "Ч": "Tsj",
        "Ё": "Jo",
        "ё": "jo",
        " ": " ",
        "=": "=",
        "/": "/",
        "Ц": "Ts",
        "Е": "E",
        "ь": "",
        ".": ".",
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H",
        "I": "I",
        "J": "J",
        "K": "K",
        "L": "L",
        "M": "M",
        "N": "N",
        "O": "O",
        "P": "P",
        "Q": "Q",
        "R": "R",
        "S": "S",
        "T": "T",
        "U": "U",
        "V": "V",
        "W": "W",
        "X": "X",
        "Y": "Y",
        "Z": "Z",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "0": "0",
        "(": "(",
        ")": ")",
        "$": "$",
        "'": "'",
        "": "",
    },
    "sr": {
        "а": "a",
        "б": "b",
        "в": "v",
        "г": "g",
        "д": "d",
        "ђ": "dj",
        "е": "e",
        "ж": "zj",
        "з": "z",
        "и": "i",
        "ј": "j",
        "к": "k",
        "л": "l",
        "љ": "lj",
        "м": "m",
        "н": "n",
        "њ": "nj",
        "о": "o",
        "п": "p",
        "р": "r",
        "с": "s",
        "т": "t",
        "ћ": "ć",
        "у": "u",
        "ф": "f",
        "х": "h",
        "ц": "c",
        "ч": "č",
        "џ": "dž",
        "ш": "š",
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Ђ": "Dj",
        "Е": "E",
        "Ж": "Zj",
        "З": "Z",
        "И": "I",
        "Ј": "J",
        "К": "K",
        "Л": "L",
        "Љ": "Lj",
        "М": "M",
        "Н": "N",
        "Њ": "Nj",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "Ћ": "Ć",
        "У": "U",
        "Ф": "F",
        "Х": "H",
        "Ц": "C",
        "Ч": "Č",
        "Џ": "Dž",
        "Ш": "Š",
        "a": "a",
        "b": "b",
        "c": "c",
        "d": "d",
        "e": "e",
        "f": "f",
        "g": "g",
        "h": "h",
        "i": "i",
        "j": "j",
        "k": "k",
        "l": "l",
        "m": "m",
        "n": "n",
        "o": "o",
        "p": "p",
        "q": "q",
        "r": "r",
        "s": "s",
        "t": "t",
        "u": "u",
        "v": "v",
        "w": "w",
        "x": "x",
        "y": "y",
        "z": "z",
        "A": "A",
        "B": "B",
        "C": "C",
        "D": "D",
        "E": "E",
        "F": "F",
        "G": "G",
        "H": "H",
        "I": "I",
        "J": "J",
        "K": "K",
        "L": "L",
        "M": "M",
        "N": "N",
        "O": "O",
        "P": "P",
        "Q": "Q",
        "R": "R",
        "S": "S",
        "T": "T",
        "U": "U",
        "V": "V",
        "W": "W",
        "X": "X",
        "Y": "Y",
        "Z": "Z",
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "0": "0",
        "(": "(",
        ")": ")",
        "$": "$",
        "'": "'",
        "-": "-",
        ".": ".",
        "—": "—",
        " ": " ",
        "": "",
    }
}
# ---


def add_new_label(q, enlabel):
    # ---
    if enlabel == "":
        return
    # ---
    labels = {}
    # ---
    labels["en"] = {
        "language": "en",
        "value": enlabel
    }
    # ---
    data = {
        "labels": labels
    }
    # ---
    add = himoAPI.New_Mult_Des(q, data, "Bot: cyrillic2latin-labels", False)


# ---
# abcd = "abcdefghijklmnopqrstuvwxyz".split('')
abcd = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
# ---
liste = {
    'ru': list(set(letters_to_latin['ru'].keys()) - set(letters_to_latin['ru'].values()) - set(abcd)),
    'sr': list(set(letters_to_latin['sr'].keys()) - set(letters_to_latin['sr'].values()) - set(abcd)),
}
# ---


def change_one_lab(text, lang):
    table = letters_to_latin[lang]
    # ---
    new_lab = "".join([table.get(i, i) for i in text])
    # ---
    # if lang ==  'ru': new_lab = new_lab.replace("ь","")
    # ---
    new_lab2 = new_lab.lower()
    # ---
    for x in liste[lang]:
        if x != '' and new_lab2.find(x.lower()) != -1:
            print(f'<<lightred>> new_lab has {x}')
            if table.get(x):
                new_lab = new_lab.replace(x, table.get(x))
    # ---
    print(f'get new lab from org_lab:[{lang}:{text}] : new:{new_lab}')
    # ---
    return new_lab


# ---


def make_en_label(labels, q, Add=False):
    org_lab = ''
    new_lab = ''
    # ---
    # ---
    for lang in ['ru', 'sr']:
        if lang in labels:
            org_lab = labels[lang]
            # ---
            new_lab = change_one_lab(org_lab, lang)
            # ---
            break
    # ---
    if new_lab != "":
        if Add:
            add_new_label(q, new_lab)
    # ---
    return new_lab


# ---


def main():
    # ---
    query = '''SELECT ?item
WHERE {  ?item wdt:P495 wd:Q403.
?item ^schema:about ?article . ?article schema:isPartOf <https://sr.wikipedia.org/>;
}
limit 10'''

  # country of origin=Srbia  #xxxx items
    # ---
    # ---
    generator = WikidataSPARQLPageGenerator(
        query,
        site=pywikibot.Site('wikidata'),
    )
    # ---
    for item in generator:
        # print(item)
        labels = item.labels
        q = item.title(as_link=False)
        if item.exists():
            item.get(get_redirect=True)
            make_en_label(labels, q)


# ---
if __name__ == "__main__":
    if 'test' in sys.argv:
        change_one_lab('Уркальту', 'ru')
    else:
        main()

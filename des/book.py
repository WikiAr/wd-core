#!/usr/bin/python3
"""

إضافة وصف للكتب والقصص


python3 core8/pwb.py des/book optional
python3 core8/pwb.py des/book ask

python pwb.py des/book

"""

#
# (C) Ibrahem Qasim, 2022
#
#
import re
import pywikibot
import sys

from wd_api import wd_desc
from wd_api import wd_bot
from API import printe

# ---
AskSave = {1: True}
"""Qlist['Q19389637'] = {# مقالة سيرة ذاتية
                'ar' : 'مقالة سيرة ذاتية' ,
                'en' : 'biographical article' ,
                'de' : 'biographischer Artikel' ,
                'fr' : 'article biographique' ,
                'nl' : 'biografisch artikel' ,
        }"""
Qlist = {
    "Q49084": {
        "ar": "قصة قصيرة",
        "en": "short story",
        "de": "Kurzgeschichte",
        "fr": "nouvelle",
        "nl": "kort verhaal",
    },
    "Q1318295": {
        "ar": "قصة",
        "en": "story",
        "de": "Erzählung",
        "fr": "récit",
        "nl": "verhaal",
    },
    "novel": {
        "ar": "رواية",
        "en": "novel",
        "de": "Roman",
        "fr": "roman",
        "nl": "roman",
    },
    "Q1760610": {
        "ar": "كتاب هزلي",
        "en": "comic book",
        "de": "Comicbuch",
        "fr": "comic book",
        "nl": "stripboek",
    },
    "Q482994": {
        "ar": "ألبوم",
        "en": "album",
        "fr": "album",
        "nl": "muziekalbum",
    },
}


def action_one_item(Qid, pa, lang, keys):
    item = wd_bot.Get_Item_API_From_Qid(pa["item"])
    if not item:
        return
    # desc = MakeDesc(Qid, auth, lang)
    # Summary= 'Bot: - Add descriptions: '+ lang
    keys = sorted(keys)
    # ---
    if "en" in keys:
        keys.append("en-gb")
        keys.append("en-ca")
    printe.output(f"keys:{str(keys)}")
    # ---
    descriptions = item["descriptions"]
    NewDesc = {}
    addedlangs = []
    # ---
    for lang in keys:
        if lang not in descriptions.keys():
            # ---
            lang2 = lang
            if lang in ("en-ca", "en-gb"):
                lang2 = "en"
            if des := MakeDesc(Qid, pa, lang2):
                NewDesc[lang] = {"language": lang, "value": des}
                dns = ""
                if "endes" in pa:
                    dns = pa["endes"]
                printe.output(f"newar:{des},en:{dns}")
                addedlangs.append(lang)
            else:
                printe.output(f'*no desc for "{lang}"')
        # ---
    if addedlangs:
        qitem = Qid  # item.title(as_link=False)
        if AskSave[1]:
            printe.output(f"================== + {addedlangs}")
            for lan, value in NewDesc.items():
                printe.output(f"""lang:{lan}, value: \"{value['value']}\"""")
            saaa = pywikibot.input("<<lightyellow>> Add as descriptions? ")
            if saaa in ["y", "a", ""]:
                if saaa == "a":
                    AskSave[1] = False
                wd_desc.work_api_desc(NewDesc, qitem)
            else:
                printe.output("* rong answer")
        else:
            wd_desc.work_api_desc(NewDesc, qitem)


# ---
Comma = {
    "an": " y ",
    "ar": "/",
    # "ar": "، و" ,
    "ast": " y ",
    "ca": " i ",
    "de": " und ",
    "es": " y ",
    "ext": " y ",
    "fr": " et ",
    "he": " ו",
    "gl": " e ",
    "it": " e ",
    "nl": " en ",
    "oc": " e ",
    "pt": " e ",
    "ro": " și ",
    "sv": " och ",
    "en": ", ",
}
Comma2 = {"ar": "، و", "en": ", ", "de": ", ", "fr": ", ", "nl": ", "}


def GetQuery(Qid, lang, keys):
    P50 = "P175" if Qid == "Q482994" else "P50"
    # ---
    # sa = ('?item wdt:P136 wd:Q8261 . ?item wdt:P31* wd:Q7725634 .\n')
    sa = f"?item wdt:P31 wd:{Qid} .\n"
    # ---
    if Qid == "novel":
        sa = "?item wdt:P136 wd:Q8261 . ?item wdt:P31 wd:Q7725634 .\n"
    # ---
    ur = f'SELECT ?item (GROUP_CONCAT(DISTINCT(?auth{lang}); separator="{Comma[lang]}") as ?{lang}) '
    # ---
    for lan in keys:
        if lan != lang:
            ur += f'\n(GROUP_CONCAT(DISTINCT(?auth{lan}); separator="{Comma[lan]}") as ?{lan}) '
    # ---
    ur += "WHERE {"
    ur += f"?item wdt:{P50} ?auths .\n"
    ur += sa
    # ---
    for lan in keys:
        if lan != lang:
            ur += f'OPTIONAL {{?auths rdfs:label ?auth{lan} filter (lang(?auth{lan}) = "{lan}")}} .\n'
    # ---
    if sys.argv and "optional" in sys.argv:
        ur += f' OPTIONAL {{ ?auths rdfs:label ?auth{lang} filter (lang(?auth{lang}) = "{lang}") }} .'
    else:
        ur += f' ?auths rdfs:label ?auth{lang} filter (lang(?auth{lang}) = "{lang}") .'
    # ---
    ur += '\nOPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "%s")}' % lang
    ur += "FILTER(!BOUND(?itemDes))  }\n GROUP BY ?item "
    # ---
    # printe.output(ur)
    # ---
    return ur


def Gquery2(json1):
    table = {}
    # table = []
    # for head in json1['head']['vars']:
    for result in json1["results"]["bindings"]:
        q = "item" in result and result["item"]["value"].split("/entity/")[1] or ""
        s = {se: result[se]["value"] for se in result}
        s["item"] = q
        table[q] = s
    return table


# ---
Off = {1: 0}
limit = {1: 0}
# ---
for arg in sys.argv:
    # ---
    arg, _, value = arg.partition(":")
    # ---
    if arg == "limit":
        limit[1] = int(value)
    elif arg == "off":
        Off[1] = int(value)


def wd_sparql_query(query, ddf=False):
    # ---
    New_List = []
    # ---
    qua = query
    # ---
    if not qua:
        return New_List
    # ---
    # if limit[1] != 0 :
    # query = query + " limit " + str( limit[1] )
    # ---
    Keep = True
    offset = Off[1] if Off[1] != 0 else 0
    # ---
    while Keep:
        # ---
        quarry = qua
        # ---
        # if ddf:
        if limit[1] != 0:
            quarry = quarry + "\n limit " + str(limit[1])
        if offset != 0:
            quarry = f"{quarry} offset {str(offset)}"
        # else: Off[1] != 0 :
        # quarry = quarry + " offset " + str( Off[1] )
        # ---
        # printe.output( quarry )
        # ---
        printe.output(f'quarry "{quarry}"')
        # ---
        generator = wd_bot.sparql_generator_url(quarry)
        # ---
        New_List.extend(iter(generator))
        # ---
        offset = int(offset + limit[1])
        # ---
        if not generator or generator == [] or "nokeep" in sys.argv:
            Keep = False
        # ---
        if not ddf or limit[1] == 0:
            Keep = False
    # ---
    return New_List


def WorkWithOneLang(Qid, lang, keys):
    printe.output("*<<lightyellow>> WorkWithOneLang: ")
    # ---
    query = GetQuery(Qid, lang, keys)
    # ---
    # printe.output(query)
    # ---
    PageList = wd_sparql_query(query, ddf=True)
    # ---
    printe.output("* PageList: ")
    SAO = Qlist[Qid][lang]
    # ---
    total = len(PageList)
    # ---
    for num, pa in enumerate(PageList, start=1):
        pa["item"] = pa["item"].split("/entity/")[1]
        printe.output(f"<<lightblue>>> {lang} \"{SAO}\" :{num}/{total} : {pa['item']}")
        action_one_item(Qid, pa, lang, keys)


# ---
by_list = {"ar": "من تأليف", "en": "by", "fr": "de", "de": "von", "nl": "van", "ca": "per", "cs": "od", "la": "ab", "it": "da", "io": "da", "eo": "de", "da": "af", "pl": "przez", "ro": "de", "es": "por", "sv": "av"}


def MakeDesc(Qid, pa, lang):
    # for lang in language:
    # auth
    description = False
    english = ["en-gb", "en-ca"]
    if lang in english:
        lang = "en"
    # ---
    if lang not in by_list:
        printe.output(f'<<lightblue>>> cant find "by" in by_list for lang: "{lang}"')
        return False
    co = "من أداء " if (Qid == "Q482994") and (lang == "ar") else f"{by_list[lang]} "
    # ---
    if (lang in pa) and (pa[lang] != ""):
        if auth := pa[lang]:
            if lang in Qlist[Qid]:
                des = Qlist[Qid][lang]
                d = des  # الوصف
                # d = d + ' '                        # الرابط by
                d = f"{d} {co}"
                d = d + auth  # المؤلف
                # printe.output( 'd' )
                # printe.output( d )
                description = d
    # else:
    # description = False
    # ---
    if description and lang == "ar":
        description = description.replace("/", "، و")
    # ---
    if lang == "ar":
        if description and description != re.sub(r"[abcdefghijklmnobqrstuvwxyz]", "", description):
            printe.output(f'<<lightred>> arabic description test failed "{description}".')
            description = False
    return description


def main():
    # ---
    for arg in sys.argv:
        # ---
        arg, _, value = arg.partition(":")
        # ---
        if arg == "save":
            AskSave[1] = False
    printe.output("start with query")
    # ---
    for Queries, Qid in enumerate(Qlist, start=1):
        keys = Qlist[Qid].keys()
        keys = ["ar"]

        totalqueries = len(Qlist.keys()) * len(Qlist[Qid].keys())
        printe.output(f'*Qid "{Qid}":')
        out = f"<<lightgreen>>  *== Quary:\"{Qlist[Qid]['ar']}\", {Queries}/{totalqueries}. =="
        printe.output(out)
        # printe.output( 'lab: "%s". ' % Qlist[Qid]['ar'] )
        for lang in keys:
            # printe.output( Qlist[Qid][lang] )
            WorkWithOneLang(Qid, lang, keys)


# ---
if __name__ == "__main__":
    main()
# ---

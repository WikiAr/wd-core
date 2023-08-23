#!/usr/bin/python
"""


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import requests
import json
import urllib
import os
import sys

# ---
def print_test(line, color=""):
    colors = {
    "red": "\033[91m%s\033[00m",
    "blue": "\033[94m%s\033[00m"
    }
    if color != "" and colors.get(color):
        line = colors[color] % line
    # ---
    if Ask[1] or Test[1]:
        print(line)
# ---
filepath = str(os.path.abspath(__file__)).replace('\\', '/')
# ---
paths = [
    '/data/project/himo/core1/',
    '/data/project/himowd/wd_core/',
    '/data/project/himowd/.local/lib/python3.7/site-packages',
]
# ---
if filepath.find("/data/project/") == -1 and filepath.find("labstore-secondary-tools-project") == -1:
    paths = [
        'I:/core/wd_core/',
        'I:/core/master/'
    ]
# ---
for x in paths:
    if os.path.isdir(x):
        sys.path.append(x)
# ---
from wikidataintegrator2 import wdi_helpers
from wikidataintegrator2 import wdi_login
# ---
from API import useraccount
# ---
username = useraccount.hiacc
password = useraccount.hipass
login = wdi_login.WDLogin(username, password)
# ---
Test = {1: False}
Ask = {1: False}
# ---
if "ask" in sys.argv:
    Ask[1] = True
if "test" in sys.argv:
    Test[1] = True
# ---
def get_and_load(url):
    # ---
    print_test(url)
    # ---
    html = ''
    try:
        html = urllib.request.urlopen(url).read().strip().decode('utf-8')
    except Exception as e:
        print_test(e)
        html = ''
    # ---
    json1 = {}
    # ---
    if html != "":
        try:
            json1 = json.loads(html)
        except Exception as ee:
            print_test(ee)
            json1 = {}
    # ---
    return json1
# ---
id_types = {"MED", "PMC", "EUROPEPMC", "PAT", "NBK", "HIR", "ETH", "CTX", "CBA", "AGR", "DOI"}
# ---
def get_article_info(ext_id, id_type):
    if not id_type.upper() in id_types:
        print(f"id_type must be in {id_types}")
    # ---
    urls = {}
    # ---
    id_type = id_type.lower()
    # ---
    print_test(f' get_article_info for {id_type}')
    if id_type == "pmc":
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC{}&resulttype=core&format=json'
        #url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:{}&resulttype=core&format=json'
        #url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=PMCID:PMC{}&resulttype=core&format=json'
        urls["europepmc"] = url.format(ext_id)

    elif id_type == "doi":
        #url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:%22{}%22&resulttype=core&format=json"
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:{}&resulttype=core&format=json"
        urls["europepmc"] = url.format(ext_id)

        url2 = "https://api.crossref.org/v1/works/http://dx.doi.org/{}"
        urls["crossref"] = url2.format(ext_id)

    elif id_type != "doi":
        url = 'https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{}%20AND%20SRC:{}&resulttype=core&format=json'
        urls["europepmc"] = url.format(ext_id, id_type)
    else:
        print_test('ValueError')
    # ---
    headers = {
        'User-Agent': 'wikidataintegrator: github.com/SuLab/WikidataIntegrator'
    }
    #response = requests.get(url, headers=headers)
    #response.raise_for_status()
    #d = response.json()
    for source, url in urls.items():
        do = get_and_load(url)
        # if do != '' and do != "Resource not found.":
        # ---
        if type(do) != dict:
            continue
        # ---
        if do.get('hitCount'):
            if do.get('hitCount') != 1:
                continue
            else:
                article = do.get('resultList', {}).get('result', [])
                if len(article) > 0:
                    article = article[0]
                    return source
        else:
            # ---
            message = do.get("message", {})
            if message != {}:
                title = message.get("title", [""])[0]
                print_test(f"title:{title}")
                # ---
                if title.find("افتتاحية") != -1:
                    print("skip افتتاحية")
                    return False
                # ---
                author = message.get("author", [])
                if len(author) == 0:
                    print("no author")
                    return False
            # ---
            # status": "ok"
            status = do.get("status", "")
            if status == "ok":
                print_test("status == ok")
                return source
            # ---
    print('No results')
    return False
# ---
def add(id, typee):
    print_test(f'typee: "{typee}"')
    source = get_article_info(id, typee)
    typee = typee.lower()
    if source:
        qid, a, b, ty = wdi_helpers.PublicationHelper(id, id_type=typee, source=source).get_or_create(login)
        if ty == "old":
            print(f'already in wikidata: <a target="_blank" href="https://www.wikidata.org/wiki/{qid}">{qid}</a>')
            print_test(f'already in wikidata:{qid}', "red")
        elif ty == 'new':
            print(f'Create success: <a target="_blank" href="https://www.wikidata.org/wiki/{qid}">{qid}</a>')
            print_test(f'Create success:{qid}', "blue")
        print_test(f'qid: {qid}')
        print_test(f'a: {a}')
        print_test(f'b: {b}')
        print_test(f'ty: {ty}')
# ---
if __name__ == "__main__":
    br = '</br>'
    #python pwb.py pub type:PMC id:4080339
    print_test('TestMain:' + br)
    typee = "MED"
    if sys.argv:
        #lenth = len(sys.argv)
        #print_test(str(lenth) + str(sys.argv) )
        for arg in sys.argv:
            arg, sep, value = arg.partition(':')
            if arg == 'type' and value != '':
                typee = value
            if arg == 'id' and value != '':
                id = value
    # ---
    if id != "":
        add(id, typee)
    else:
        print("id empty..")
# ---
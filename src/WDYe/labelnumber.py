#!/usr/bin/python3
#
import pywikibot
from pywikibot import pagegenerators as pg

default_language = 'ar'
items2do = 0
itemsdone = 0
missing_dict = {}


def onee_item(wditem):
    global items2do
    items2do -= 1
    if wditem.labels:  # تسميات موجودة
        if 'en' in wditem.labels:  # تسمية انجليزية متوفرة
            numberlabel = wditem.labels['en']  # اسم انجليزي
            ara = 'ar'
            data = {'labels': {ara: numberlabel}}
            wditem.editEntity(data, summary=f'Bot: add ar label: {numberlabel}')
    return 1


def wd_sparql_generator(query):
    wikidatasite = pywikibot.Site('wikidata', 'wikidata')
    generator = pg.WikidataSPARQLPageGenerator(query, site=wikidatasite)
    for wd in generator:
        wd.get(get_redirect=True)
        yield wd


def main():
    global itemsdone
    itemsdone = 0
    max = 10
    print("- بدء المهمة")  # تسميات إنجليزية مجرد أرقام دون تسمية عربية
    query = 'SELECT ?item WHERE { ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en"). BIND( REGEX(STR(?cid22), "^([0-9]*)$") AS ?regexresult ) . FILTER( ?regexresult = true ) . FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .} LIMIT ' + str(max) + ''
    print("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        try:
            onee_item(wditem)
            itemsdone += 1
        except BaseException:
            print(f'{wditem} تخطي')
    print(f'العناصر المكتملة: {itemsdone}')


if __name__ == "__main__":
    main()

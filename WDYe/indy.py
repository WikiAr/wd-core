#!/usr/bin/python3
#
import pywikibot
from pywikibot import pagegenerators as pg

debugedo = True
debugedo = False
debug = False
default_language = 'ar'
items2do = 0
itemsdone = 0
missing_dict = {}


def fixlabel(oldlabel):
    new = oldlabel.replace('٠', '0').replace('١', '1').replace('٢', '2').replace('٣', '3').replace('٤', '4')
    new2 = new.replace('٥', '5').replace('٦', '6').replace('٧', '7').replace('٨', '8').replace('٩', '9')
    return new2


def action_one_item(wditem):
    global items2do
    ara = 'ar'
    items2do -= 1
    if wditem.labels:  # تسميات موجودة
        if ('ar' in wditem.labels):
            oldlabel = wditem.labels['ar']
            newlabel = fixlabel(oldlabel)
            data = {}
            data.update({
                'labels': {
                    ara: newlabel
                }
            })
            wditem.editEntity(data, summary=f'Bot: update Arabic label: {oldlabel} to {newlabel}')
        else:
            pass
    return 1
    return 0


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
    # تسميات إنجليزية مجرد أرقام دون تسمية عربية
    print("- بدء المهمة تسميات بأرقام هندية")
    # query = 'SELECT ?item WHERE { ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en"). BIND( REGEX(STR(?cid22), "^([0-9]*)$") AS ?regexresult ) . FILTER( ?regexresult = true ) . FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .} LIMIT '+str(max)+''
    query = 'SELECT ?item WHERE {  ?item rdfs:label ?cid22. FILTER((LANG(?cid22)) = "en").  ?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar") BIND( REGEX(STR(?itemabel), "^((٠|١|٢|٣|٤|٥|٦|٧|٨|٩)*)$") AS ?regexresult ) .  FILTER( ?regexresult = true ) . } LIMIT ' + str(max) + ''
    print("--- يتم الان تشغيل الاستعلام")
    pigenerator = wd_sparql_generator(query)
    for wditem in pigenerator:
        try:
            action_one_item(wditem)
            itemsdone += 1
            print('العناصر المكتملة: %s' % itemsdone)
        except BaseException:
            print('%s تخطي' % wditem)
    print('العناصر المكتملة: %s' % itemsdone)


if __name__ == "__main__":
    if debugedo:
        print("debug is on")
        site = pywikibot.Site('ar')
        repo = site.data_repository()
        wd = pywikibot.ItemPage(repo, 'Q17979303')
        wd.get(get_redirect=True)
        action_one_item(wd)
    else:
        print("(---------- جاهز للبدء ----------)")
        main()

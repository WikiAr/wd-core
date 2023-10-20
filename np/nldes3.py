#!/usr/bin/python
# (C) Edoderoo/Edoderoobot (meta.wikimedia.org), 2016–2019
# Distributed under the terms of the CC-BY-SA 3.0 licence.
# Q13005188 mandal
r'''
jsub -N aa python3 core8/pwb.py np/nldes3 a3r sparql:Q23038290
python3 core8/pwb.py np/nldes3 allkeys
python3 core8/pwb.py np/nldes3 sparql:Q820655
python3 core8/pwb.py np/nldes3 a3r sparql:Q728937 railway
python3 core8/pwb.py np/nldes3 a3r sparql:Q7604686
python3 core8/pwb.py np/nldes3 a3r sparql:Q27020041
python3 core8/pwb.py np/nldes3 a3r sparql:Q484170 #بلدية في فرنسا
python3 core8/pwb.py np/nldes3 a3r sparql:Q262166 #بلدية في ألمانيا
python3 core8/pwb.py np/nldes3 a3r sparql:Q22865 #بلدية في ألمانيا
python3 core8/pwb.py np/nldes3 a3r sparql:Q3184121 #بلدية في البرازيل
python3 core8/pwb.py np/nldes3 a3r sparql:Q6784672 #بلدية في سلوفاكيا
python3 core8/pwb.py np/nldes3 a3r sparql:Q667509 #بلدية في النمسا
python3 core8/pwb.py np/nldes3 a3r sparql:Q24764  #بلدية في الفلبين
python3 core8/pwb.py np/nldes3 a3r sparql:Q2039348  #بلدية في هولندا
python3 core8/pwb.py np/nldes3 a3r sparql:Q57058  #بلدية في كرواتيا
python3 core8/pwb.py np/nldes3 a3r sparql:Q1054813  #بلدية في اليابان
python3 core8/pwb.py np/nldes3 a3r sparql:Q1758856  #بلدية في مالي
python3 core8/pwb.py np/nldes3 a3r sparql:Q747074  #بلدية إيطالية
python3 core8/pwb.py np/nldes3 a3r sparql:Q493522  #بلدية في بلجيكا
python3 core8/pwb.py np/nldes3 a3r sparql:Q755707  #بلدية في النرويج
python3 core8/pwb.py np/nldes3 a3r sparql:Q1349648  #بلدية في اليونان
python3 core8/pwb.py np/nldes3 a3r sparql:Q127448  #بلدية في السويد
python3 core8/pwb.py np/nldes3 a3r sparql:Q1906268  #بلدية في بلغاريا
python3 core8/pwb.py np/nldes3 a3r sparql:Q856076  #بلدية في فنلندا
python3 core8/pwb.py np/nldes3 a3r sparql:Q378508  #بلدية في أنغولا
# أنواع البلديات
SELECT ?item2 ?item2Label (COUNT(?item) AS ?count) WHERE {
  ?item wdt:P31 ?item2.
  FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = 'ar') }
  ?item2 wdt:P279 wd:Q15284.
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language 'ar,en,bl' .
  }
}
group by ?item2 ?item2Label
# ---
pywikibot\.ItemPage\(repo\,(.*?)\.title\(\)\)
python3 core8/pwb.py np/nldes3 a3r sparql:Q184188      #كانتون فرنسي
python3 core8/pwb.py np/nldes3 a3r sparql:Q7930614     #قرية في تايوان
python3 core8/pwb.py np/nldes3 a3r sparql:Q56436498    #قرية في الهند
python3 core8/pwb.py np/nldes3 a3r sparql:Q1983062     #حلقة
python3 core8/pwb.py np/nldes3 a3r sparql:Q21191270    #حلقة مسلسل تلفزيوني
python3 core8/pwb.py np/nldes3 a3r sparql:Q571         #كتاب
python3 core8/pwb.py np/nldes3 a3r sparql:
python3 core8/pwb.py np/nldes3 a3r sparql:
python3 core8/pwb.py np/nldes3 a3r sparql:
Q842478
#!/usr/local/bin/python
# -*- coding: utf-8 -*-
python3 core8/pwb.py np/nldes3 a3r sparql:Q7366  # أغنية
python3 core8/pwb.py np/nldes3 a3r sparql:Q5398426
python3 core8/pwb.py np/nldes3 a3r sparql:Q13417250   #مقاطعة في أذربيجان
python3 core8/pwb.py np/nldes3 a3r sparql:Q215380
python3 core8/pwb.py np/nldes3 a3r sparql:Q83373   # نجم زائف
python3 core8/pwb.py np/nldes3 a3r sparql:Q13890   # نجم مزدوج
python3 core8/pwb.py np/nldes3 a3r sparql:Q6999    # جرم فلكي
python3 core8/pwb.py np/nldes3 a3r sparql:Q569500  # مركز صحي
python3 core8/pwb.py np/nldes3 a3r sparql:Q54050   # تل
python3 core8/pwb.py np/nldes3 a3r sparql:Q39614   # مقبرة
python3 core8/pwb.py np/nldes3 a3r sparql:Q123705  # حي سكني
python3 core8/pwb.py np/nldes3 a3r sparql:Q12323   # سد
python3 core8/pwb.py np/nldes3 a3r sparql:Q22698   # متنزه
python3 core8/pwb.py np/nldes3 a3r sparql:Q131681  #  خزان مائي
python3 core8/pwb.py np/nldes3 a3r sparql:Q4421    #غابة
python3 core8/pwb.py np/nldes3 a3r sparql:Q180958    #كلية
python3 core8/pwb.py np/nldes3 a3r sparql:Q179700    #تمثال
python3 core8/pwb.py np/nldes3 a3r sparql:Q30022    #مقهى
python3 core8/pwb.py np/nldes3 a3r sparql:Q4989906    #معلم تذكاري
# ---
python3 core8/pwb.py np/nldes3 a3r sparql:Q184188 ask #كانتون فرنسي
python3 core8/pwb.py np/nldes3 a3r sparql:Q783866 ask #
python3 core8/pwb.py np/nldes3 a3r sparql:Q783866 ask #
python3 core8/pwb.py np/nldes3 a3r sparql:Q783866 ask #
python3 core8/pwb.py np/nldes3 a3r sparql:Q783866 ask #
python3 core8/pwb.py np/nldes3 a3r sparql:Q3331189  #طبعة
python3 core8/pwb.py np/nldes3 a3r sparql:Q783866  #مكتبة جافا سكريبت
python3 core8/pwb.py np/nldes3 a3r sparql:Q14752149  #نادي كرة قدم للهواة
python3 core8/pwb.py np/nldes3 a3r sparql:Q476028  #نادي كرة قدم
python3 core8/pwb.py np/nldes3 a3r sparql:Q620615  #تطببيق محمول
python3 core8/pwb.py np/nldes3 a3r sparql:Q2831984   #ألبوم قصص مصورة
python3 core8/pwb.py np/nldes3 a3r sparql:Q7187     # جين
python3 core8/pwb.py np/nldes3 a3r sparql:Q277338     # جين كاذب
python3 core8/pwb.py np/nldes3 a3r sparql:Q19389637     مقالة سيرة ذاتية
python3 core8/pwb.py np/nldes3 a3r sparql:Q3305213  # لوحة فنية بواسطة
python3 core8/pwb.py np/nldes3 a3r sparql:Q7889    # لعبة فيديو
python3 core8/pwb.py np/nldes3 a3r sparql:Q8054     # بروتين
python3 core8/pwb.py np/nldes3 a3r sparql:Q7278     # حزب سياسي
'''
import pywikibot
from pywikibot import pagegenerators as pg
import random
from API import printe
import sys
import re
from datetime import timedelta
# ---
from wd_api import himoAPI
from wd_api import wd_bot
# ---
totaledits = 0
# ---
sparqler = {
    1: ''
}
Offq = {
    1: 0
}
Off = {
    1: 0
}
limit = {
    1: 0
}
# ---
totallimit = {
    1: 10000
}
# ---
from np.nldesc import action_one_item, all_types_list, simple_set_byP131, SPARQLSE, New_QS
# ---


def lastXnewpages(maxp):
    printe.output('Begonnen')
    site = pywikibot.Site('nl')
    mygenerator = pg.NewpagesPageGenerator(site, 0, maxp)
    for onepage in mygenerator:
        if (onepage.exists()):  # avoid speedy deleted
            # print('p:%s' % onepage.title())
            if ('wikibase_item' in onepage.properties()):
                try:
                    wd = onepage.data_item()
                    yield (wd)
                except BaseException:
                    pass
    printe.output('Klaar')


# ---


def testrun():
    repo = pywikibot.Site().data_repository()
    item2get = 'Q92924911'
    x = pywikibot.ItemPage(repo, item2get)
    printe.output('read item')
    if x.exists():
        printe.output('item does exist')
        found, written = action_one_item('nl', x)
        # print('[%s][%s]' % (x.get('descriptions',{})['nl'],''))
    else:
        printe.output('no action!')


# ---


def wd_one_without_description(item):
    base_sparql = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . OPTIONAL {?item schema:description ?itemdescription filter (lang(?itemdescription) = \"nl\").  } FILTER (!BOUND(?itemdescription))}'
    one_sparql = base_sparql % item
    for wditem in wd_sparql_query(one_sparql):
        if (wditem.exists()):
            yield wditem


# ---


def wd_all_without_description():
    base_sparql = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . OPTIONAL {?item schema:description ?itemdescription filter (lang(?itemdescription) = \"nl\").  } FILTER (!BOUND(?itemdescription))}'
    for item in all_types_list:
        wd_one_without_description(item)
        '''
    one_sparql = base_sparql % item
    for wditem in wd_sparql_query(one_sparql):
      if (wditem.exists()):
        yield wditem
    '''


# ---


def wd_all_simple_P131():
    for onesimpleitem in simple_set_byP131:
        query = 'select ?item where {?item wdt:P31 wd:%s}' % onesimpleitem
        printe.output(f'\n\nQuery: {query}\n\n')
        for oneitem in wd_sparql_query(query):
            try:
                if oneitem.exists():
                    yield oneitem
                    # action_one_P131_item()
                else:
                    printe.output(f'Else wd-simple: {oneitem.title()}')
            except BaseException:
                pass
    yield 'Q5'


# ---


def wd_all_countries(spq):
    country_query = 'select ?item where {?item wdt:P31 wd:Q6256}'
    country_generator = wd_sparql_query(country_query)
    for wd_country in country_generator:
        spq_with_country = spq % wd_country
        one_country_generator = wd_sparql_query(spq_with_country)
        for item in one_country_generator:
            if (item.exists()):
                yield item


# ---


def wd_sparql_query(spq, ddf=False):
    # ---
    New_List = []
    # ---
    qua = spq
    # ---
    if qua == '':
        return New_List
    # ---
    Keep = True
    offset = 0
    # ---
    if Off[1] != 0:
        offset = Off[1]
    # ---
    printe.output(f'qua "{qua}"')
    # ---
    while Keep:
        # ---
        quarry = qua
        # ---
        # if ddf:
        if limit[1] != 0:
            quarry = quarry + "\n limit " + str(limit[1])
        if offset != 0:
            quarry = quarry + " offset " + str(offset)
        # ---
        # printe.output( quarry )
        # ---
        printe.output('limit[1]:"%d"\t offset:"%d"' % (limit[1], offset))
        # ---
        generator = wd_bot.sparql_generator_url(quarry, printquary=False, geterror=True)
        # ---
        for x in generator:
            New_List.append(x)
        # ---
        offset = int(offset + limit[1])
        # ---
        if not generator or generator == [] or 'nokeep' in sys.argv:
            Keep = False
        # ---
        # ناتج الاستعلام أقل من تحديد limit
        if len(generator) < limit[1] and 'hhh' in sys.argv:
            Keep = False
        # ---
        #
        if len(New_List) > 1:
            fandi = (len(New_List) / totallimit[1]) * 100
            printe.output('fandi: %d.' % fandi)
            if fandi > 89:
                Keep = False
                printe.output('return New_List..')
        # ---
        if not ddf or limit[1] == 0:
            Keep = False
    # ---
    return New_List


# ---


def wd_user_edits(username, ucsite, totaledits):
    repo = pywikibot.Site('wikidata', 'wikidata').data_repository()
    useredits = pg.UserContributionsGenerator(username, site=ucsite, total=totaledits, namespaces=[0])
    for oneedit in useredits:
        if (oneedit.exists()):
            wd = pywikibot.ItemPage(repo, oneedit.title())
            if (wd.exists()):
                yield wd


# ---


def sparql_nodescription(sparql):
    return 'select distinct ?item where {{%s}filter (!bound(?itemDescription))}' % sparql


# ---


def some_items():
    repo = pywikibot.Site('wikidata', 'wikidata').data_repository()
    do_these = ['Q52504095', 'Q52501574']  # scenografino / dramaturgino
    do_these = ['Q62507873', 'Q62898370']  # null edits
    for one_item in do_these:
        wd = pywikibot.ItemPage(repo, one_item)
        if (wd.exists()):
            yield wd


# ---


def newest_items(repo, site):
    for item in pg.NewPagesPageGenerator(site):
        break
    startno = int(item.title()[1:])
    for itemno in range(startno, 0, -1):
        item = pywikibot.ItemPage(repo, 'Q%d' % itemno)
        yield (item)


# ---


def generator_last_hour():
    timenow = None
    site = pywikibot.Site('wikidata', 'wikidata')
    repo = site.data_repository()
    generator = newest_items(repo, site)
    generator = pg.NewpagesPageGenerator(site)
    for item in generator:
        if timenow is None:
            timenow = item.oldest_revision.timestamp
            endtime = timenow - timedelta(1.0 / 24.0)
            untilltime = endtime - timedelta(0.001)
        if (item.oldest_revision.timestamp > untilltime):
            # print(item.title())
            item = pywikibot.ItemPage(repo, item.title())
            if (item.exists()):
                # print(item.title())
                yield item
        else:
            printe.output(f'Klaar: {item.oldest_revision.timestamp}')
            break


# ---


def wd_all_items():
    startrange = 80999999
    stoprange = 80000000
    startrange = 79788588
    stoprange = 79000000
    startrange = 78823351
    stoprange = 78000000
    startrange = 77196790
    stoprange = 77000000
    # startrange= 50000100
    # stoprange = 50000000
    repo = pywikibot.Site('wikidata', 'wikidata').data_repository()
    for itemno in range(startrange, stoprange):
        # try:
        wd = pywikibot.ItemPage(repo, 'Q%d' % itemno)
        if not wd.isRedirectPage():
            if wd.exists():
                yield wd
        else:
            pass
        itemno -= 1


# ---
'''
query = 'link[nlwiki]'
sparql_query4 = 'SELECT * {{SELECT ?item WHERE { ?wiki0 <http://schema.org/about> ?item . ?wiki0 <http://schema.org/isPartOf> <https://nl.wikipedia.org/> {service wikibase:label{bd:serviceParam wikibase:language 'nl' . }}}} filter (!bound(?itemDescription))}   '
sparql_query3 = 'SELECT * {{SELECT ?item WHERE { ?wiki0 <http://schema.org/about> ?item . ?wiki0 <http://schema.org/isPartOf> <https://nl.wikipedia.org/> }} }   '
#sparql_query = 'SELECT ?item WHERE {{SELECT ?item WHERE {hint:Query hint:optimizer 'None' .{SELECT ?item WHERE {?item wdt:P31 wd:Q4167836 .} LIMIT 275000}OPTIONAL { ?item schema:description ?itemDescription  }filter (!bound(?itemDescription)) }} SERVICE wikibase:label {  bd:serviceParam wikibase:language 'nl' .  }}'
#sparql_query=sparql_nodescription('select ?item where {?item wdt:P31 wd:Q5633421. OPTIONAL { ?item schema:description ?itemDescription  } }')
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q202444 }'
sparql_query3 = 'select ?item where {?item wdt:P31 wd:Q5633421 }'
#
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q13442814 .     ?item wdt:P577 ?published .     filter ((?published > "1800-01-01T00:00:00Z"^^xsd:dateTime) && (?published < "2000-01-01T00:00:00Z"^^xsd:dateTime)) }'
#sparql_query = 'SELECT ?item WHERE {?item wdt:P27 wd:%s . ?item wdt:P31 wd:Q5 . ?item wdt:P106 ?beroep optional { ?item schema:description ?itemDescription . FILTER(lang(?itemDescription)='nl') } .  FILTER (REGEX(STR(?itemDescription), "n[/]a", 'i'))}'
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q207628 . OPTIONAL {?item schema:description ?itemdescription filter (lang(?itemdescription) = \"nl\").  } FILTER (!BOUND(?itemdescription))} '  #church no description
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q207628}'
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q5 . ?item wdt:P106 ?beroep . ?item wdt:P27 wd:%s . {service wikibase:label{bd:serviceParam wikibase:language 'nl' . }} OPTIONAL { ?item schema:description ?d .  FILTER(lang(?d)='nl') } filter (!bound(?d))}'
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q3184121 . ?item wdt:P17 wd:%s}'  #basisschool per land
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q1077097 }'
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q985488}' #bewonersgemeenschap in ?land
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q4830453}' #onderneming
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q21278897}' #doorverwijzing naar wiktionary
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q5084}' #gehucht -> test
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q55488}' #spoorwegstation -> test
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q43229}' #organisatie
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q17329259}' #encyclopedsich artikel
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q207628}' #
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q23397}' #meer
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q1004 }' #stripverhaal
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q14406742 . }' #stripreeks
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q34442 . ?item wdt:P17 ?land}' #weg in land
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q273057}' #discografie
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q486972 . ?item wdt:P17 wd:%s}'  #nederzetting per land
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q101352} ' #achternaam
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q7366}' #lied
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q5. ?item wdt:P106 wd:Q2526255}' #filmregisseur
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q15416}' #televisieprogramma
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q134556}' #single
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q3305213}' #3. schilderij
#sparql_query = 'SELECT ?item where {?item wdt:P31 wd:Q4167410 . ?item wdt:P17 ?land}' #disambiguation-page
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q1539532}' #sportseizoen -> pass
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q737498}' #academisch tijdschrift
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q166735}' #broekbos
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q54050}' #heuvel
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q253019}' #ortsteil
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q7075}' #bibliotheek
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q21014462}' #cel lijn 100.000++
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q5 . ?item wdt:P106 wd:Q1028181 . ?item wdt:P27 ?land}'  #kunstschilders geboren in een land
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q178122}'  #aria
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q3331189}' #2d2 #uitgave van P50
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q1344}'     #3d3 #opera van P86
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q742421}' #theatergezelschap
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q4022}' #rivier
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q180684}' #conflict
##sparql_query = 'select distinct ?item where {?item wdt:P31 wd:Q571 . ?item wdt:P50 ?auth}' #boek met auteur
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q732577 . ?item wdt:P123 ?itsthere}' #badmintonners
#sparql_query = 'select ?item where {  ?item wdt:P31 wd:Q5 .   ?item wdt:P106 wd:Q639669 .   ?item wdt:P27 ?land . }' #zwemmers
#sparql_query = 'select ?item where {  ?item wdt:P31 wd:Q5 .   ?item wdt:P106 ?beroep .   ?item wdt:P27 wd:Q183 . }' #belgen met een beroep
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q5783996}' #cottage
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q3863}'    #كويكب
#sparql_query = 'select ?item where {?item wdt:P31 wd:Q726242}' #LLYR-ster
#sparql_query = 'SELECT * { ?item schema:description 'onderzoeker'@nl . ?item wdt:P27 wd:%s }'
#sparql_query = 'SELECT * { ?item schema:description 'tennisser'@nl . ?item wdt:P27 ?land}' #
#sparql_query = 'SELECT ?item WHERE {?item wdt:P31 wd:Q3947}' #
#sparql_query = 'select ?item ?land where { ?item wdt:P31 wd:Q5. ?item wdt:P106 wd:Q1650915. ?item wdt:P27 ?land.}'
#sparql_query = 'SELECT ?item {?item wdt:P31 wd:Q13442814 . OPTIONAL { ?item schema:description ?d . FILTER(lang(?d)='nl') }  FILTER( !BOUND(?d) )} LIMIT 1000'
#sparql_query='SELECT ?item WHERE { ?item wdt:P31 wd:Q5 . ?item wdt:P106 ?dummy0 . ?wiki0 <http://schema.org/about> ?item . ?wiki0 <http://schema.org/isPartOf> <https://nl.wikipedia.org/> {service wikibase:label{bd:serviceParam wikibase:language 'nl' . }}}'  #claim[31:5] and claim[106] and link[nlwiki]
'''
# ---


def just_get_ar(labe):
    lab = labe.split('@@')
    tab = []
    # ---
    claimstr = ''
    # ---
    for o in lab:
        test = re.sub(r"[abcdefghijklmnopqrstuvwxyz@]", '', o.lower())
        if test.lower() == o.lower() and o != '':
            tab.append(o)
    # ---
    if tab != []:
        claimstr = '، و'.join(tab)
        printe.output(f"just_get_ar:{claimstr}.")
    # ---
    return claimstr
    # ---


def main(debug=False):
    print('main')
    sasa = ''
    pigenerator = None
    # ---
    sasa = SPARQLSE.get(sparqler[1].strip(), '')
    # ---
    if sasa == '':
        printe.output(f'{sparqler[1]} not in SPARQLSE')
        sasa = '''SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = 'ar') } } ''' % sparqler[1]
    # ---
    ssqq = [sasa]
    if sparqler[1].strip() == '' or 'allkeys' in sys.argv:
        ssqq = [SPARQLSE[x] for x in SPARQLSE.keys()]
        printe.output(f'work in all SPARQLSE.keys() len: {len(ssqq)}')
    # ---
    numg = 0
    # ---
    ssqq = random.sample(ssqq, int(len(ssqq)))
    # ---
    for sparql_query in ssqq:
        # ---
        numg += 1
        # ---
        printe.output('-------------------------')
        printe.output("<<lightblue>> query %d from %d :" % (numg, len(ssqq)))
        # ---
        if Offq[1] > 0 and Offq[1] > numg:
            continue
        # ---
        # sparql_query = 'select ?item where {?item wdt:P31 wd:Q3508250}' #
        # site=pywikibot.Site('wikidata','wikidata')
        repo = {}  # site.data_repository()
        items_processed = 0
        if debug:
            printe.output('main-1')
        if (True):
            # pigenerator = wd_all_countries(sparql_query)
            # pigenerator = wd_all_without_description()
            # pigenerator=wd_one_without_description('Q189004')  #onderwijsinstelling
            # pigenerator = wd_all_simple_P131()
            # pigenerator = wd_user_edits('Edoderoobot',site,511111)
            # pigenerator = wd_all_items(1)
            # pigenerator = lastXnewpages(1999999) #max one month of newpages anyways
            # pigenerator = wd_all_items(-1)
            # pigenerator=some_items()
            pigenerator = wd_sparql_query(sparql_query, ddf=True)
        if (pigenerator is None) or (forcehourly):
            printe.output('Force hourly script...')
            pigenerator = generator_last_hour()
        totalreads = 0
        # pigenerator = [ {'item': 'http://www.wikidata.org/entity/Q19019359'} ]
        for wd in pigenerator:
            printe.output("<<lightblue>> ============")
            # printe.output( wd )
            q = wd['item'].split("/entity/")[1]
            totalreads += 1
            if debug:
                printe.output(f'Found: {q}')
            printe.output("p%d/%d q:%s" % (totalreads, len(pigenerator), q))
            # ---
            claimstr = just_get_ar(wd.get('lab', ''))
            # ---
            thisfound, thisone = action_one_item('ar', q, claimstr=claimstr)
            items_processed += thisone
            # if (items_processed>12): break
            # if ((items_processed>maxwrites) and (maxwrites>0)): break
        if New_QS[1] != []:
            himoAPI.QS_line("||".join(New_QS[1]), user='Mr.Ibrahembot')
        printe.output(f'Klaar: {items_processed}')


print(' start np/nldes.py ')
forcehourly = False
# ---
if __name__ == '__main__':
    if 'test' in sys.argv:
        action_one_item('ar', 'Q162210')
    else:
        main()
# ---

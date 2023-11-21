#!/usr/bin/python3
"""

new pages from file

python pwb.py wd/common


"""
#
# (C) Ibrahem Qasim, 2022
#
from wd_api import newdesc

import pywikibot

# import pwb

# ---
# ---
# ---
# import urllib
# import urllib.request
# import urllib.parse
# ---
from desc_dicts.descraptions import DescraptionsTable

queries2 = {
    # 'chemical compound': 'SELECT ?item   WHERE { ?item wdt:P31 wd:Q11173 ;      wdt:P31 ?instance .    ?item schema:description "chemical compound"@en.  }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'family name': 'SELECT ?item WHERE { ?item wdt:P31 wd:Q101352 ;     wdt:P31 ?instance .    ?item schema:description "family name"@en.    }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'female given name': 'SELECT ?item   WHERE { ?item wdt:P31 wd:Q11879590 ;       wdt:P31 ?instance .    ?item schema:description "female given name"@en.  }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'genus of algae': 'SELECT ?item  WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of algae"@en. }   ',
    # 'genus of amphibians': 'SELECT ?item WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of amphibians"@en.    }   ',
    # 'genus of arachnids': 'SELECT ?item  WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of arachnids"@en. }   ',
    # 'genus of birds': 'SELECT ?item  WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of birds"@en. }   ',
    # 'genus of fishes': 'SELECT ?item WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of fishes"@en.    }   ',
    # 'genus of fungi': 'SELECT ?item  WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of fungi"@en. }   ',
    # 'genus of insects': 'SELECT ?item    WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of insects"@en.   }   ',
    # 'genus of mammals': 'SELECT ?item    WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of mammals"@en.   }   ',
    # 'genus of molluscs': 'SELECT ?item   WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of molluscs"@en.  }   ',
    # 'genus of plants': 'SELECT ?item WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of plants"@en.    }   ',
    # 'genus of reptiles': 'SELECT ?item   WHERE   {   ?item wdt:P105 wd:Q34740 .    ?item schema:description "genus of reptiles"@en.  }   ',
    # 'Hebrew calendar year': 'SELECT ?item    WHERE { ?item wdt:P31 wd:Q577 ;    wdt:P31 ?instance .    ?item schema:description "Hebrew calendar year"@en.   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    'Islamic calendar year': 'SELECT ?item WHERE { ?item wdt:P31 wd:Q577 ;   wdt:P31 ?instance .  ?item wdt:P361 wd:Q28892 .   ?item schema:description "Islamic calendar year"@en. FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .} GROUP BY ?item HAVING(COUNT(?instance) = 1)',
    'male given name': 'SELECT ?item  WHERE { ?item wdt:P31 wd:Q12308941 ;       wdt:P31 ?instance .    ?item schema:description "male given name"@en.    FILTER NOT EXISTS {?item rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} . }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'natural number': 'SELECT ?item  WHERE { ?item wdt:P31 wd:Q21199 .     FILTER NOT EXISTS { ?item wdt:P31 wd:Q200227 } .    ?item schema:description "natural number"@en.   OPTIONAL {      ?item schema:description ?itemabel.     FILTER((LANG(?itemabel)) = "ar")    }   FILTER(!BOUND(?itemabel)) }   ',
    # 'village in China': 'SELECT ?item    WHERE   {   ?item wdt:P31 wd:Q13100073 ;      wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .     #?item schema:description "Wikimedia category"@en.    }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000    OFFSET 500000',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000    OFFSET 1000000',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000    OFFSET 1500000',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000    OFFSET 2000000',
    # 'Wikimedia category': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q4167836 ;   wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)    LIMIT 500000    OFFSET 2500000',
    # 'Wikimedia disambiguation page': 'SELECT ?item   WHERE   {   ?item wdt:P31 wd:Q4167410 ;   wdt:P31 ?instance .     ?item schema:description "Wikimedia disambiguation page"@en.  }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'Wikimedia list article': 'SELECT ?item  WHERE   {   ?item wdt:P31 wd:Q13406463 ;      wdt:P31 ?instance .     ?item schema:description "Wikimedia list article"@en.   #OPTIONAL { ?item schema:description ?itemDescription. FILTER(LANG(?itemDescription) = "es").  }  #FILTER (!BOUND(?itemDescription))  }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'Wikimedia template': 'SELECT ?item  WHERE { ?item wdt:P31 wd:Q11266439 ;      wdt:P31 ?instance .   }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'Wikinews article': 'SELECT ?item    WHERE { ?item wdt:P31 wd:Q17633526 ;      wdt:P31 ?instance .     #?item schema:description "Wikinews article"@en.  }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
    # 'year': 'SELECT ?item    WHERE   {   ?item wdt:P31 wd:Q577 ;   wdt:P31 ?instance .     ?item schema:description "year"@en.     OPTIONAL {      ?item schema:description ?itemabel.     FILTER((LANG(?itemabel)) = "ar")    } }   GROUP BY ?item  HAVING(COUNT(?instance) = 1)',
}

SELECT = 'SELECT  ?item  WHERE { ?item '
# GROUP = 'OPTIONAL { ?item schema:description ?des. FILTER((LANG(?des)) = "ar") } FILTER(!BOUND(?des))} GROUP BY ?item HAVING(COUNT(?instance) = 1) Limit 102'
# GROUP = '' 'OPTIONAL { ?item schema:description ?des. FILTER((LANG(?des)) = "ar") } FILTER(!BOUND(?des))} '
GROUP = ' OPTIONAL { ?item schema:description ?des. FILTER((LANG(?des)) = "ar") } FILTER(!BOUND(?des))} '

queries = {
    # ---
    # 'family name': SELECT + ' wdt:P31 wd:Q101352 ; wdt:P31 ?instance .  ?item schema:description "family name"@en.' + GROUP,
    'family name': SELECT + ' wdt:P31 wd:Q101352. FILTER NOT EXISTS { ?item wdt:P31 wd:Q4167410 } ' + GROUP,
    # 'female given name': SELECT + ' wdt:P31 wd:Q11879590 ;  wdt:P31 ?instance .  ?item schema:description "female given name"@en.' + GROUP,
    'female given name': SELECT + ' wdt:P31 wd:Q11879590. FILTER NOT EXISTS { ?item wdt:P31 wd:Q4167410 }' + GROUP,
    'male given name': SELECT + ' wdt:P31 wd:Q12308941 . FILTER NOT EXISTS { ?item wdt:P31 wd:Q4167410 }' + GROUP,
    # ---
    # 'genus of algae': SELECT + 'wdt:P105 wd:Q34740 .  ?item schema:description "genus of algae"@en.' + GROUP,
    # 'genus of amphibians': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of amphibians"@en.' + GROUP,
    # 'genus of arachnids': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of arachnids"@en.' + GROUP,
    # 'genus of birds': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of birds"@en.' + GROUP,
    # 'genus of fishes': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of fishes"@en.' + GROUP,
    # 'genus of fungi': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of fungi"@en.' + GROUP,
    # 'genus of insects': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of insects"@en.' + GROUP,
    # 'genus of mammals': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of mammals"@en.' + GROUP,
    # 'genus of molluscs': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of molluscs"@en.' + GROUP,
    # 'genus of plants': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of plants"@en.' + GROUP,
    # 'genus of reptiles': SELECT + ' wdt:P105 wd:Q34740 . ?item schema:description "genus of reptiles"@en.' + GROUP,
    # ---
    'Hebrew calendar year': SELECT + ' wdt:P31 wd:Q577  . ?item schema:description "Hebrew calendar year"@en.' + GROUP,
    'Islamic calendar year': SELECT + ' wdt:P31 wd:Q577 ; wdt:P31 ?instance . ?item wdt:P361 wd:Q28892 . ?item schema:description "Islamic calendar year"@en.' + GROUP,
    'year': SELECT + ' wdt:P31 wd:Q577 ; wdt:P31 ?instance . ?item schema:description "year"@en.' + GROUP,
    # ---
    'natural number': SELECT + ' wdt:P31 wd:Q21199 . FILTER NOT EXISTS { ?item wdt:P31 wd:Q200227 } . ?item schema:description "natural number"@en.',
    # 'chemical compound': SELECT + ' wdt:P31 wd:Q11173 ; wdt:P31 ?instance .  ?item schema:description "chemical compound"@en.' + GROUP,
    # 'village in China': SELECT + ' wdt:P31 wd:Q13100073 ; wdt:P31 ?instance . ' + GROUP,
    'village in China': SELECT + ' wdt:P31 wd:Q13100073. ' + GROUP,
    # ---
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . #?item schema:description "Wikimedia category"@en.\n' + GROUP,
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . #?item schema:description "Wikimedia category"@en.\n' + GROUP,
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . } GROUP BY ?item HAVING(COUNT(?instance) = 1) LIMIT 500000 OFFSET 500000',
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . } GROUP BY ?item HAVING(COUNT(?instance) = 1) LIMIT 500000 OFFSET 1000000',
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . } GROUP BY ?item HAVING(COUNT(?instance) = 1) LIMIT 500000 OFFSET 1500000',
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . } GROUP BY ?item HAVING(COUNT(?instance) = 1) LIMIT 500000 OFFSET 2000000',
    # 'Wikimedia category': SELECT + ' wdt:P31 wd:Q4167836 ; wdt:P31 ?instance . } GROUP BY ?item HAVING(COUNT(?instance) = 1) LIMIT 500000 OFFSET 2500000',
    # ---
    # 'Wikimedia disambiguation page': SELECT + ' wdt:P31 wd:Q4167410 ; wdt:P31 ?instance . ?item schema:description "Wikimedia disambiguation page"@en.' + GROUP,
    # 'Wikimedia list article': SELECT + ' wdt:P31 wd:Q13406463 ; wdt:P31 ?instance . ?item schema:description "Wikimedia list article"@en.' + GROUP,
    # 'Wikimedia template': SELECT + ' wdt:P31 wd:Q11266439 ; wdt:P31 ?instance . ' + GROUP,
    # 'Wikinews article': SELECT + ' wdt:P31 wd:Q17633526 . \n' + GROUP,
    # 'Wikinews article': 'SELECT DISTINCT  ?item WHERE {  BIND("Wikinews article"@en AS ?year)  ?item schema:description ?year.}'
}

queriestest = {
    # 'Islamic calendar year': SELECT + ' wdt:P31 wd:Q577 ; wdt:P31 ?instance . ?item wdt:P361 wd:Q28892 . ?item schema:description "Islamic calendar year"@en.' + GROUP,
    # 'family name': SELECT + ' wdt:P31 wd:Q101352 ; wdt:P31 ?instance .  ?item schema:description "family name"@en.' + GROUP,
    'family name': SELECT
    + ' wdt:P31 wd:Q101352 ; wdt:P31 ?instance .  OPTIONAL { ?item schema:description ?itemabel. FILTER((LANG(?itemabel)) = "ar") } FILTER(!BOUND(?itemabel))}',
}


def OOutPut(ss):
    pywikibot.output(ss)


# ---
qq = {
    'Hebrew calendar year': SELECT + ' wdt:P31 wd:Q577  . ?item schema:description "Hebrew calendar year"@en.' + GROUP,
}
# ---
# start of newdesc.py file
# newdesc.work22(q , topic, DescraptionsTable)
# newdesc.main_from_file(file , topic , DescraptionsTable)
# newdesc.mainfromQuarry2( topic , Quarry, DescraptionsTable)
# ---
limiTa = ['Wikimedia category', 'Wikimedia disambiguation page']


def main():
    pywikibot.output('*<<lightyellow>> main:')
    queries_list = sorted([x for x in queries.keys()])
    lenth = len(queries_list)
    numb = 0
    for topic in queries_list:
        numb += 1
        if topic in DescraptionsTable:
            pywikibot.output('**<<lightyellow>> %d/%d: topic: %s' % (numb, lenth, topic))
            # ---
            quary = queries[topic]
            Limit = 'Limit 5000'
            # limiTa = [  'Wikimedia category' , 'Wikimedia disambiguation page']
            if topic in limiTa:
                Limit = 'Limit 100'
            # ---
            quary = quary + Limit
            trans2 = {}
            trans2[topic] = DescraptionsTable[topic]
            newdesc.mainfromQuarry2(topic, quary, trans2)
        else:
            pywikibot.output("topic not in DescraptionsTable")
    # ---
    pywikibot.output("Finished successfully")


def Main_Test():
    wikidatasite = pywikibot.Site('wikidata', 'wikidata')
    repo = wikidatasite.data_repository()
    # ---
    pywikibot.output('**<<lightyellow>> test:')
    topic = 'chemical compound'
    q = 'Q27198088'
    item = pywikibot.ItemPage(repo, q)
    item.get()
    tra = {}
    tra[topic] = DescraptionsTable[topic]
    newdesc.work22(q, topic, tra)
    # ---


MainTest = False  # False#True

if __name__ == "__main__":
    if MainTest:
        Main_Test()
    else:
        main()

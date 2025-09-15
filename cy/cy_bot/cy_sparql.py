#!/usr/bin/python3
"""
from .cy_sparql import GetSparql

"""

import re
import sys
import urllib
import urllib.parse
import requests
from datetime import datetime

# ---
# from .cy_helps import printt
# ---
menet = datetime.now().strftime("%Y-%b-%d  %H:%M:%S")

Stage = {"": ""}
# ---


def get_query_results(query):
    # ---
    query = re.sub(r"\n\s+", "\n", query)
    # ---
    fao = urllib.parse.quote(query)
    # ---
    url = f"https://query.wikidata.org/bigdata/namespace/wdq/sparql?format=json&query={fao}"
    # ---
    if "printurl" in sys.argv:
        print(url)
    # ---
    req = False
    # ---
    session = requests.session()
    session.headers.update({"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"})
    # ---
    try:
        req = session.get(url, timeout=10)

    except requests.exceptions.ReadTimeout:
        print(f"ReadTimeout: {url}")

    except Exception as e:
        print("<<lightred>> Traceback (most recent call last):")
        print(f"<<lightred>> Exception:{e}.")
        print("CRITICAL:")
    # ---
    json1 = {}
    if req:
        try:
            json1 = req.json()
        except Exception as e:
            json1 = {}
            # ---
            print("<<lightred>> Traceback (most recent call last):")
            e = str(e)
            if "java.util.concurrent" in e:
                e = "java.util.concurrent"
            print(f"<<lightred>> Exception:{e}.")
            print("CRITICAL:")
    # ---
    return json1


def GetSparql(qid, title):
    old_qu = """SELECT
    ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?p642label ?p585 ?p582 ?p580 ?title
    WHERE {
    SELECT ?item  ?itemlab ?jerseylab ?image  ?p17lab
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image), "/Special:FilePath/"), "|", ?jerseylab, "}}") AS ?jersey_1)
               ?jersey1lab ?image1
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_2)
               ?p642label  ?p585 ?p582 ?p580 ?title
               WHERE {
                 BIND(wd:Q518222 AS ?aa)
                 OPTIONAL {    ?item p:P2417 ?statment.    ?statment ps:P2417 ?aa.    ?statment pq:P2912 ?jersey.    ?jersey wdt:P18 ?image.  }
                 OPTIONAL {    ?item p:P2321 ?statment1.    ?statment1 ps:P2321 ?aa.    ?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
                 OPTIONAL { ?item wdt:P17 ?p17.}
                 OPTIONAL { ?item wdt:P585 ?p585.}
                 OPTIONAL { ?item wdt:P582 ?p582.}
                 OPTIONAL { ?item wdt:P580 ?p580.}
                 ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.
                 ?winner pq:P642 ?P642.
        FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
        FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
                 OPTIONAL { ?sitelink schema:about ?item
                           . ?sitelink schema:isPartOf <https://ar.wikipedia.org/>
                                                          . ?sitelink schema:name ?title }
                 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
                                         ?p17 rdfs:label ?p17lab.
                                         ?item rdfs:label ?itemlab.
                                         ?jersey rdfs:label ?jerseylab.
                                         ?jersey1 rdfs:label ?jersey1lab.
                                         ?P642 rdfs:label ?p642label.
                                        }

    } } """
    # ---
    qu_2019 = """SELECT DISTINCT ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?jersey_3 ?jersey_4 ?p642label ?p585 ?p582 ?p580 ?rankP4323 ?rankP2321 ?rankP4320 ?rankP3494 ?title
    WHERE {     SELECT DISTINCT ?item ?itemlab ?jerseylab ?p17lab ?rankP4323 ?rankP2321 ?rankP4320 ?rankP3494
               ?jersey1lab ?image1 ?image2  ?image3 ?image4
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_1)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image2), "/Special:FilePath/"), "|", ?jersey2lab, "}}") AS ?jersey_2)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image3), "/Special:FilePath/"), "|", ?jersey3lab, "}}") AS ?jersey_3)
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image4), "/Special:FilePath/"), "|", ?jersey4lab, "}}") AS ?jersey_4)
               ?p642label ?p585 ?p582 ?p580 ?title
               WHERE {
                 BIND(wd:Q447532 AS ?aa)
                  ?item wdt:P31 ?a1a.
                 OPTIONAL {  ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.  ?winner pq:P642 ?P642.  }
                  ?item (p:P1346|p:P4323|p:P2321|p:P4320|p:P3494) ?statment0.
                 ?statment0 (ps:P1346|ps:P4323|ps:P2321|ps:P4320|ps:P3494) ?aa.
                 OPTIONAL {  ?item p:P4323 ?statment1 .  ?statment1  ps:P4323 ?aa.
                           OPTIONAL {?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
                           OPTIONAL {?statment1 pq:P1352 ?rankP4323. }
                          }
                 OPTIONAL {  ?item p:P2321 ?statment2 .  ?statment2 ps:P2321 ?aa.
                           OPTIONAL {?statment2 pq:P2912 ?jersey2.    ?jersey2 wdt:P18 ?image2.  }
                           OPTIONAL {?statment2 pq:P1352 ?rankP2321. }
                          }
                 OPTIONAL {  ?item p:P4320 ?statment3 .  ?statment3 ps:P4320 ?aa.
                           OPTIONAL {?statment3 pq:P2912 ?jersey3.    ?jersey3 wdt:P18 ?image3.  }
                           OPTIONAL {?statment3 pq:P1352 ?rankP4320. }
                          }
                 OPTIONAL {  ?item p:P3494 ?statment4 .  ?statment4 ps:P3494 ?aa.
                           OPTIONAL {?statment4 pq:P2912 ?jersey4.    ?jersey4 wdt:P18 ?image4.  }
                           OPTIONAL {?statment4 pq:P1352 ?rankP3494. }
                          }
OPTIONAL { ?item wdt:P17 ?p17.} OPTIONAL { ?item wdt:P585 ?p585.}  OPTIONAL { ?item wdt:P582 ?p582.}  OPTIONAL { ?item wdt:P580 ?p580.}
FILTER NOT EXISTS { ?item wdt:P31 wd:Q20646667. } # plain stage
FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
FILTER NOT EXISTS { ?item wdt:P31 ?P31 . ?P31 wdt:P279 wd:Q18131152 }
FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }
OPTIONAL { ?sitelink schema:about ?item
                           . ?sitelink schema:isPartOf <https://ar.wikipedia.org/>
                                                          . ?sitelink schema:name ?title }
    SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
    ?p17 rdfs:label ?p17lab.
    ?item rdfs:label ?itemlab.
    ?jersey1 rdfs:label ?jersey1lab.
    ?jersey2 rdfs:label ?jersey2lab.
    ?jersey3 rdfs:label ?jersey3lab.
    ?jersey4 rdfs:label ?jersey4lab.
    ?P642 rdfs:label ?p642label.
    }

    } } """
    # ---
    qu_2019 = qu_2019.replace("Q447532", qid)
    qu2 = qu_2019
    # ---
    if title in Stage:
        qu2 = qu2.replace("FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }", "")
        qu2 = qu2.replace("FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }", "")
    # }Limit 10  } """
    # ---
    json1 = get_query_results(qu2)
    # ---
    # for rr in json1.get("head", {}).get("vars", []): HeadVars.append(rr)
    # ---
    bindings = json1.get("results", {}).get("bindings", [])
    # ---
    if len(bindings) > 1:
        return json1
    # ---
    # one result or no result
    if title in Stage:
        return {}
    # ---
    qua3 = qu_2019
    qua3 = qua3.replace("FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }", "")
    qua3 = qua3.replace("FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }", "")
    qua3 = qua3.replace("FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q18131152 }", "")
    qua3 += f"\n#{menet}"
    # ---
    json2 = get_query_results(qua3)
    # ---
    print("try 2")
    # ---
    return json2

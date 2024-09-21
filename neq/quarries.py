#!/usr/bin/env python3
"""

from nep.tables.quarries import SPARQLSE

"""

# ---
import sys
from nep.tables.lists import p50s, Taton_list, Space_tab, others_list, songs_type, space_list_and_other_2
from desc_dicts.descraptions import Qid_Descraptions

p31_only_quarry = "select ?item where {?item wdt:P31 wd:%s}"

main_quarry = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '

main_quarry_with_proerty = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item wdt:%s ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
"""
query = default_query #later, I want to manage this with params
sparql_query = 'SELECT ?item WHERE {   ?item wdt:P31 wd:Q21191270 .   ?item wdt:P179 ?dummy0 . }'
sparql_query = 'select ?item where{{select ?item ?itemLabel ?itemDescription WHERE {   ?item wdt:P31 wd:Q21191270 .   ?item wdt:P179 ?dummy0 . {service wikibase:label{bd:serviceParam wikibase:language "nl" . }}}} filter (!bound(?itemDescription))}'


#sparql_query=sparql_nodescription(sparql_query)
sparql_query='SELECT ?item WHERE { ?item wdt:P31 wd:Q5 . ?item wdt:P106 ?dummy0 . ?wiki0 <http://schema.org/about> ?item . ?wiki0 <http://schema.org/isPartOf> <https://nl.wikipedia.org/> }'  #claim[31:5] and claim[106] and link[nlwiki]

sparql_query = 'select * {{SELECT ?item ?itemDescription WHERE {{ ?item wdt:P31 wd:Q4167836 }  service wikibase:label{bd:serviceParam wikibase:language "nl" . }  }}}'

"""


# ---
def do_qua(qid, prop="", ad="", ar_values=""):
    qua = "SELECT ?item WHERE {\n"
    qua += f" ?item wdt:P31 wd:{qid}. \n"
    # ---
    if prop:
        qua += f" ?item {prop} ?constellation. \n"
        # ---
        if "a2r" in sys.argv:
            qua += ' ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") \n'
    # ---
    if ad:
        qua += f" {ad} \n"
    # ---
    if ar_values:
        qua += "?item schema:description ?itemar \n"
        qua += f"values ?itemar {{{ar_values}}} \n"
    else:
        qua += 'FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } \n'
    # ---
    qua += "}"
    # ---
    return qua


# ---
# SPARQLSE = {tt: main_quarry % tt for tt in Qid_Descraptions}
SPARQLSE = {tt: do_qua(tt) for tt in Qid_Descraptions}


for p50 in p50s:
    SPARQLSE[f"{p50}dfd"] = do_qua(p50, prop="wdt:P50")

    SPARQLSE[p50] = (
        """
        SELECT DISTINCT
            ?item
            (GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
        WHERE {
            ?item wdt:P31 wd:%s .
            ?item wdt:P50 ?pp.
            ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
            FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
            }
            GROUP BY ?item """
        % p50
    )

# ---
# رواية
SPARQLSE[
    "Q7725634"
] = """SELECT DISTINCT
    ?item
    (GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
    WHERE {
    ?item wdt:P136 wd:Q8261 . ?item wdt:P31 wd:Q7725634 .
    ?item wdt:P50 ?pp.
    ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
    FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
    }
    GROUP BY ?item """
# ---
for scdw in others_list:
    prop = "(wdt:P17|wdt:P131)"
    # ---
    if scdw in songs_type:
        prop = "wdt:P175"
    # ---
    if scdw not in SPARQLSE:
        SPARQLSE[scdw] = do_qua(scdw, prop=prop)
# ---

# مقالة سيرة ذاتية
# .
SPARQLSE["Q19389637"] = SPARQLSE[scdw] = do_qua("Q19389637", prop="wdt:P1433", ad="?item wdt:P361 wd:Q590208")

# biografisch artikel
# ---Q19389637#Q2831984

# كتاب
SPARQLSE["Q571"] = SPARQLSE[scdw] = do_qua("Q571", prop="wdt:P50", ad="")
# ---

# مجرة
SPARQLSE["Q318"] = do_qua("Q318", prop="wdt:P59", ad="?constellation wdt:P31 wd:Q8928.")

# ---
SPARQLSE[
    "Q318"
] = """SELECT DISTINCT ?item
WITH
{
SELECT ?item { ?item wdt:P31 wd:Q101352 } ORDER BY DESC(xsd:integer(SUBSTR(STR(?item),33))) LIMIT 30000
}  AS %a
WITH
{
SELECT ?item (COUNT(?l) as ?ls) (SAMPLE(?l) as ?l1)  {
INCLUDE %a
?item schema:description ?l } GROUP BY ?item HAVING( ?ls < 10)
}  as %b
WHERE
{
INCLUDE %b
OPTIONAL { ?item rdfs:label ?l5 . FILTER(lang(?l5)="en") }
}
ORDER BY DESC(xsd:integer(SUBSTR(STR(?item),33)))"""
# ---
# كسوف نجم ثنائي
SPARQLSE["Q1457376"] = do_qua("Q1457376", prop="wdt:P59", ad="?constellation wdt:P31 wd:Q8928.")
# ---s

# جين
SPARQLSE["Q7187"] = do_qua("Q7187", prop="wdt:P703", ad="?constellation wdt:P31 wd:Q16521.")

if "yuy" in sys.argv:
    SPARQLSE[
        "Q7187"
    ] = """SELECT ?item WHERE { ?item wdt:P31 wd:Q7187 .  ?item wdt:P703 wd:Q15978631.
    FILTER NOT EXISTS { ?item schema:description ?d . FILTER(lang(?d)="ar") }
    } """
# ---Q8054

# بروتين
SPARQLSE["Q8054"] = do_qua("Q8054", prop="(wdt:P702|wdt:P703)", ad="FILTER NOT EXISTS {?item wdt:P31 wd:Q11173}")

if "yuy" in sys.argv:
    SPARQLSE[
        "Q8054"
    ] = """SELECT ?item WHERE { ?item wdt:P31 wd:Q8054 .
?item (wdt:P702|wdt:P703) ?constellation.
?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
FILTER NOT EXISTS {?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
FILTER NOT EXISTS {?item wdt:P31 wd:Q11173}  .
} """
# ---
# حلقة
# Q21191270#Q1983062
SPARQLSE["Q21191270"] = do_qua("Q21191270", prop="wdt:P179", ad="")

SPARQLSE["Q1983062"] = do_qua("Q1983062", prop="wdt:P179", ad="")

SPARQLSE["Q44559"] = do_qua("Q44559", prop="", ad="")
# جبل
SPARQLSE["Q8502"] = do_qua("Q8502", prop="wdt:P17", ad="")

# ---
SPARQLSE["Q45382"] = do_qua("Q45382", prop="wdt:P17", ad="")
# ---
for sw in Taton_list:
    if sw not in SPARQLSE:
        # ---
        SPARQLSE[sw] = main_quarry % sw
        # ---
        const = space_list_and_other_2.get(sw, {}).get("P", "")
        # ---
        if "a2r" in sys.argv and const:
            gtg = "SELECT ?item WHERE {"

            gtg += f"""
                ?item wdt:P31 wd:{sw}.
                ?item wdt:{const} ?const.
                """

            gtg += """
                FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
                ?const rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
                }
            """
            SPARQLSE[sw] = gtg

# ---
for st in Space_tab:
    if st not in SPARQLSE:
        # if SPARQLSE.get( st , '' ) == '' :
        SPARQLSE[st] = do_qua(st, prop="wdt:P59", ad="?constellation wdt:P31 wd:Q8928. # كوكبة")

# ---
# Q11424  فيلم
SPARQLSE["Q11424"] = do_qua("Q11424", prop="wdt:P57", ad="")
# ---


# موسم رياضي
SPARQLSE[
    "Q27020041"
] = """SELECT DISTINCT
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P31 wd:Q27020041 .
  ?item wdt:P3450 ?pp.
  ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item
"""

# طراز سيارة
SPARQLSE[
    "Q3231690"
] = """SELECT DISTINCT
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P31 wd:Q3231690 .
  ?item wdt:P176 ?pp.
  ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item
"""
if "optional" in sys.argv:
    SPARQLSE["Q3231690"] = SPARQLSE["Q3231690"].replace(
        '?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .',
        'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}',
    )
# ---
SPARQLSE["Q3331189"] = do_qua("Q3331189", prop="wdt:P629", ad="")

# ---
SPARQLSE["Q7889"] = do_qua("Q7889", prop="(wdt:P178|wdt:P179)", ad="")
# أغنية
SPARQLSE["Q7366"] = do_qua("Q7366", prop="wdt:P175", ad="")


from nep.new_way import P1433_ids

# ---
for qid, va in P1433_ids.items():
    prop = "|".join([f"wdt:{p['p']}" for p in va["props"]])
    prop = f"({prop})"
    # ---
    ar_values = ""
    # ---
    if "doar" in sys.argv:
        ar_values = " ".join([f'"{ar}"@ar' for ar in va["false_labs"] if ar])
    # ---
    if qid not in SPARQLSE:
        qua = do_qua(qid, prop=prop, ad="", ar_values=ar_values.strip())
        SPARQLSE[qid] = qua
    # ---
    # if "doar" in sys.argv: print(f"python3 core8/pwb.py neq/nldes3 a2r sparql:{qid} all:1000 doar")


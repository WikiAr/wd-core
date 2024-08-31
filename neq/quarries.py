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
SPARQLSE = {tt: main_quarry % tt for tt in Qid_Descraptions}
# ---
# حركة فردية
for p50 in p50s:
    # ---
    SPARQLSE[
        f"{p50}dfd"
    ] = f"""
        SELECT ?item WHERE {{ ?item wdt:P31 wd:{p50} . ?item wdt:P50 ?auth. ?auth rdfs:label ?authar. FILTER((LANG(?authar)) = "ar") . FILTER NOT EXISTS {{ ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }} }}
        """

    # ---
    SPARQLSE[p50] = (
        """SELECT DISTINCT
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
    if "optional" in sys.argv:
        SPARQLSE[p50] = SPARQLSE[p50].replace(
            '?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .',
            'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}',
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
        SPARQLSE[scdw] = "SELECT ?item WHERE {" + f"?item wdt:P31 wd:{scdw}. ?item {prop} ?constellation." + ' FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
        # ---
        if "a2r" in sys.argv:
            SPARQLSE[scdw] = "SELECT ?item WHERE {" + f"?item wdt:P31 wd:{scdw}. ?item {prop} ?constellation." + ' ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
        # ---
        if "a3r" in sys.argv:
            SPARQLSE[scdw] = "SELECT ?item WHERE { ?item wdt:P31 wd:" + scdw + ' . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
# ---


# مقالة سيرة ذاتية
SPARQLSE["Q19389637"] = p31_only_quarry % "Q19389637"  # biografisch artikel

if "Q665807" in sys.argv:
    SPARQLSE["Q19389637"] = "select ?item where {?item wdt:P31 wd:Q19389637 . ?item wdt:P1433 wd:Q665807. } "  # biografisch artikel

elif "noQ665807" in sys.argv:
    SPARQLSE[
        "Q19389637"
    ] = """
        SELECT DISTINCT ?item WHERE {
        ?item wdt:P31 wd:Q8502; wdt:P17 ?dummy0.
        FILTER NOT EXISTS { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
        }

        """

# biografisch artikel
# ---Q19389637#Q2831984

# كتاب
SPARQLSE[
    "Q571"
] = """SELECT ?item WHERE
    { ?item wdt:P31 wd:Q571 .
    ?item wdt:P50 ?auth.
    ?auth rdfs:label ?authar. FILTER((LANG(?authar)) = "ar") .
    FILTER NOT EXISTS { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
    }
    """
# ---

# مجرة
SPARQLSE["Q318"] = "SELECT ?item WHERE { ?item wdt:P31 wd:Q318 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928.} "  # galaxyx
if "a2r" in sys.argv:
    SPARQLSE["Q318"] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q318 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
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
SPARQLSE["Q1457376"] = "SELECT ?item WHERE {?item wdt:P31 wd:Q1457376 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928.} "
if "a2r" in sys.argv:
    SPARQLSE["Q1457376"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q1457376 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
# ---Q7187


# جين
SPARQLSE["Q7187"] = "SELECT ?item WHERE {?item wdt:P31 wd:Q7187 . ?item  wdt:P703 ?constellation. ?constellation wdt:P31 wd:Q16521.} "
if "a2r" in sys.argv:
    SPARQLSE["Q7187"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q7187 . ?item  wdt:P703 ?constellation. ?constellation wdt:P31 wd:Q16521. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
if "yuy" in sys.argv:
    SPARQLSE[
        "Q7187"
    ] = """SELECT ?item WHERE { ?item wdt:P31 wd:Q7187 .  ?item wdt:P703 wd:Q15978631.
    FILTER NOT EXISTS { ?item schema:description ?d . FILTER(lang(?d)="ar") }
    } """
# ---Q8054


# بروتين
SPARQLSE["Q8054"] = "SELECT ?item WHERE {?item wdt:P31 wd:Q8054 . ?item  (wdt:P702|wdt:P703) ?constellation.  FILTER NOT EXISTS {?item wdt:P31 wd:Q11173} } "
if "a2r" in sys.argv:
    SPARQLSE["Q8054"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q8054 . ?item (wdt:P702|wdt:P703) ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS {?item wdt:P31 wd:Q11173} } '
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
SPARQLSE[
    "Q21191270"
] = """SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q21191270.
    ?item wdt:P179 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
"""
SPARQLSE[
    "Q1983062"
] = """SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q1983062.
    ?item wdt:P179 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
"""
# ---


#
SPARQLSE[
    "Q44559"
] = """SELECT ?item WHERE {
  ?item wdt:P31 wd:Q44559.
FILTER NOT EXISTS {?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---


# جبل
SPARQLSE[
    "Q8502"
] = """SELECT ?item WHERE {
  ?item wdt:P31 wd:Q8502; wdt:P17 ?dummy0.
FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---

SPARQLSE[
    "Q45382"
] = """SELECT ?item WHERE {
?item wdt:P31 wd:Q45382; wdt:P17 ?dummy0.
FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---
for sw in Taton_list:
    if sw not in SPARQLSE:
        # if sw not in SPARQLSE:
        # SPARQLSE[sw] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % sw
        # ---
        # SPARQLSE[sw] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % sw
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

        if "a3r" in sys.argv:
            gtg = "SELECT ?item WHERE { ?item wdt:P31 wd:" + sw + '. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
            SPARQLSE[sw] = gtg
# ---
for st in Space_tab:
    if st not in SPARQLSE:
        # if SPARQLSE.get( st , '' ) == '' :
        SPARQLSE[st] = (
            """
SELECT ?item WHERE {
    ?item wdt:P31 wd:%s .
    FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }

    ?item wdt:P59 ?constellation.
    ?constellation wdt:P31 wd:Q8928. # كوكبة
} """
            % st
        )
        # ---
        if "a2r" in sys.argv:
            SPARQLSE[st] = (
                """
SELECT ?item WHERE {
    ?item wdt:P31 wd:%s .
    FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }

    ?item wdt:P59 ?constellation.
    ?constellation wdt:P31 wd:Q8928. # كوكبة
    ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
} """
                % st
            )
        # ---
        if "a3r" in sys.argv:
            SPARQLSE[st] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % st
# ---
# Q11424  فيلم
SPARQLSE["Q11424"] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item wdt:P57 ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % "Q11424"
# ---
if "a2r" in sys.argv:
    SPARQLSE["Q11424"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . ?item wdt:P57 ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % "Q11424"
# ---
if "a3r" in sys.argv:
    SPARQLSE["Q11424"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % "Q11424"
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
if "optional" in sys.argv:
    SPARQLSE["Q27020041"] = SPARQLSE["Q27020041"].replace(
        '?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .',
        'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}',
    )
# ---

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
# for cf in Geo_entity :
# SPARQLSE[cf] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item  wdt:P17 ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } }' % cf
# if "a2r" in sys.argv:
# SPARQLSE[cf] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . ?item  wdt:P17 ?constellation.  ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")  FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } }'  % cf
# ---
# if "a3r" in sys.argv:
# SPARQLSE[cf] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '  % cf
# ---
# SPARQLSE['Q3331189'] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q3331189 . ?item  wdt:P629 ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
SPARQLSE["Q3331189"] = main_quarry_with_proerty % ("Q3331189", "P629")
if "a2r" in sys.argv:
    SPARQLSE["Q3331189"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q3331189. ?item  wdt:P629 ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} '
if "a3r" in sys.argv:
    SPARQLSE["Q3331189"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % "Q3331189"

# ---
SPARQLSE["Q7889"] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item  (wdt:P178|wdt:P179) ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % "Q7889"
if "a2r" in sys.argv:
    SPARQLSE["Q7889"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . ?item (wdt:P178|wdt:P179) ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % "Q7889"
if "a3r" in sys.argv:
    SPARQLSE["Q7889"] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % "Q7889"

# أغنية
SPARQLSE[
    "Q7366"
] = """SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q7366.
    ?item wdt:P175 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
"""
# ---
# البلديات
SPARQLSE[
    "Q7366"
] = """SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q7366.
    ?item wdt:P175 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
"""
# ---

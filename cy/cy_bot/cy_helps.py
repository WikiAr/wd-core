"""
from .cy_helps import printt, CheckTempalteInPageText, printo, print_test2, ec_de_code, TEST, GetSectionNew3, make_dada

"""
import sys
import urllib.parse
import re

br = "<br>"
# ---
qu_2018 = """SELECT
?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?jersey_3 ?jersey_4 ?p642label ?p585 ?p582 ?p580 ?title
WHERE {
SELECT ?item  ?itemlab ?jerseylab ?p17lab
           ?jersey1lab ?image1 ?image2  ?image3 ?image4
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_1)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image2), "/Special:FilePath/"), "|", ?jersey2lab, "}}") AS ?jersey_2)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image3), "/Special:FilePath/"), "|", ?jersey3lab, "}}") AS ?jersey_3)
           (CONCAT("{{JOJOJO|", STRAFTER(STR(?image4), "/Special:FilePath/"), "|", ?jersey4lab, "}}") AS ?jersey_4)
           ?p642label ?p585 ?p582 ?p580 ?title
           WHERE {
             BIND(wd:Q447532 AS ?aa)
             ?item wdt:P1346 ?aa.  ?item p:P1346 ?winner.  ?winner ps:P1346 ?aa.  ?winner pq:P642 ?P642.
             OPTIONAL {  ?item p:P4323 ?statment1.    ?statment1 ps:P4323 ?aa.    ?statment1 pq:P2912 ?jersey1.    ?jersey1 wdt:P18 ?image1.  }
             OPTIONAL {  ?item p:P2321 ?statment2.    ?statment2 ps:P2321 ?aa.    ?statment2 pq:P2912 ?jersey2.    ?jersey2 wdt:P18 ?image2.  }
             OPTIONAL {  ?item p:P4320 ?statment3.    ?statment3 ps:P4320 ?aa.    ?statment3 pq:P2912 ?jersey3.    ?jersey3 wdt:P18 ?image3.  }
             OPTIONAL {  ?item p:P3494 ?statment4.    ?statment4 ps:P3494 ?aa.    ?statment4 pq:P2912 ?jersey4.    ?jersey4 wdt:P18 ?image4.  }

             OPTIONAL { ?item wdt:P17 ?p17.}
             OPTIONAL { ?item wdt:P585 ?p585.}
             OPTIONAL { ?item wdt:P582 ?p582.}
             OPTIONAL { ?item wdt:P580 ?p580.}
    FILTER NOT EXISTS { ?item wdt:P2417 ?P2417 }
    FILTER NOT EXISTS { ?item wdt:P31/wdt:P279* wd:Q53534649 }
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
q22u = """SELECT
    ?item ?p17lab ?itemlab ?jersey_1 ?jersey_2 ?p642label ?p585 ?p582 ?p580
    WHERE {
    SELECT ?item  ?itemlab ?jerseylab ?image  ?p17lab
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image), "/Special:FilePath/"), "|", ?jerseylab, "}}") AS ?jersey_1)
               ?jersey1lab ?image1
               (CONCAT("{{JOJOJO|", STRAFTER(STR(?image1), "/Special:FilePath/"), "|", ?jersey1lab, "}}") AS ?jersey_2)
               ?p642label  ?p585 ?p582 ?p580
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
                 SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en,fr".
                                         ?p17 rdfs:label ?p17lab.
                                         ?item rdfs:label ?itemlab.
                                         ?jersey rdfs:label ?jerseylab.
                                         ?jersey1 rdfs:label ?jersey1lab.
                                         ?P642 rdfs:label ?p642label.
                                        }

    }   } """
# ---
TEST = {1: False, 2: False}
# ---
if "test" in sys.argv:
    TEST[1] = True
# ---
if "test2" in sys.argv:
    TEST[2] = True


def ec_de_code(tt, type):
    fao = tt
    if type == "encode":
        fao = urllib.parse.quote(tt)
    elif type == "decode":
        fao = urllib.parse.unquote(tt)
    return fao


def make_dada(NewText, MainTitle):
    url = "https://" + "ar.wikipedia.org/w/index.php?title=" + ec_de_code(MainTitle, "decode") + "&action=submit"
    t = f"<form id='editform' name='editform' method='POST' action='{url}'>"
    t += f"<textarea id='wikitext-new' class='form-control' name='wpTextbox1'>{NewText}</textarea>"
    t += """
<input type='hidden' name='wpSummary' value='تحديث نتائج اللاعب'/>
<input id='btn-saveandreturn' type='submit' class='btn' name='wpDiff' value='Save &amp; Return' title='Open the edit interface in a new tab/window, then quietly return to the main page.'/>
<input id='wpPreview' type='submit' class='btn-lg' tabindex='5' title='[p]' accesskey='p' name='wpPreview' value='Preview changes'/>
<input id='wpDiff' type='submit' class='btn-lg' tabindex='7' name='wpDiff' value='show changes' accesskey='v' title='show changes.'/>
</form>"""
    return t


def print_test2(s):
    if TEST[2]:
        # pywikibot.output(s)
        print(s)


def printt(s):
    SS = False
    if SS or "test" in sys.argv or "test2" in sys.argv:
        # pywikibot.output(s)
        print(s)


def printo(s):
    # ---
    if "test" in sys.argv or "test2" in sys.argv or "ask" in sys.argv:
        print(s)
        return
    # ---
    try:
        print(ec_de_code(s, "encode"))
    except BaseException:
        print("")
        if "workibrahem" in sys.argv:
            print(s)


def CheckTempalteInPageText(text):
    printt("**CheckTempalteInPageText: <br>")
    if text:
        # ---
        # \{\{template_tesult(\|id\=Q\d+|)\}\}
        Topname = r"نتيجة سباق الدراجات\/بداية"
        Top = r"\{\{" + Topname + r"\}\}"
        # ---
        Check_Top = re.sub(Top, "", text)
        Top2 = r"\{\{" + Topname + r"\s*\|\s*id\s*\=\s*Q\d+\s*\}\}"
        Check_Top2 = re.sub(Top2, "", text)
        Top3 = r"\{\{" + Topname + r"\s*?.*?\}\}"
        Check_Top3 = re.sub(Top3, "", text)
        Bottom = r"\{\{نتيجة سباق الدراجات\/نهاية\}\}"
        Check_Bottom = re.sub(Bottom, "", text)
        # ---
        if (text == Check_Top) and (text == Check_Top2) and (text == Check_Top3):
            po = "لا يمكن إيجاد " + "{{نتيجة سباق الدراجات/بداية " + "في الصفحة. "
            printo(po)
            return False
        elif text == Check_Bottom:
            oo = "لا يمكن إيجاد " + "{{نتيجة سباق الدراجات/نهاية}} " + "في الصفحة. "
            printo(oo)
            return False
        else:
            printt(" * Tempaltes Already there.<br>")
            return True
    else:
        printt(" * no text.<br>")


def GetSectionNew3(text):
    printt("**GetSectionNew3: ")
    text = text
    text2 = text
    FirsPart = ""
    # temp1 = '{{نتيجة سباق الدراجات/بداية|wikidatalist=t}}'
    # temptop = '{{نتيجة سباق الدراجات/بداية}}'
    # ---
    Frist = re.compile(r"\{\{نتيجة سباق الدراجات\/بداية\s*?.*?\}\}")
    if Fristsss := Frist.findall(text2):
        printt("Section: ")
        FirsPart = Fristsss[0]
        printt(FirsPart)
    # ---
    if FirsPart:
        text2 = text2.split(FirsPart)[1]
        text2 = FirsPart + text2
    # ---
    text2 = text2.split("{{نتيجة سباق الدراجات/نهاية}}")[0]
    text2 = text2 + "{{نتيجة سباق الدراجات/نهاية}}"
    # ---
    return text2, FirsPart
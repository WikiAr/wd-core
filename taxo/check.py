#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة وصف للكائنات بناءاً على استعلام جديد


"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import pywikibot
import json
import codecs
import sys
#---
# start of himoBOT.py file
from API import himoBOT
#---
arabic={
   "Q7377":{
            'ar': "من الثدييات",
            'ca': "de mamífers",
            'en': "of mammals",
            'es': "de mamíferos",
            'fr': "de mammifères",
            'gl': "de mamíferos",
            'id': "mamalia",
            'ro': "de mamifere",
            'sq': "e gjitarëve",
        },
   "Q10811":{
            'ar': "من الزواحف",
            'ca': "de rèptils",
            'en': "of reptiles",
            'es': "de reptiles",
            'fr': "de reptiles",
            'id': "reptilia",
            'ro': "de reptile",
            'sq': "e zvarranikëve",
        },
   "Q1358":{
            'ar': "من العنكبوتيات",
            'ca': "d'aràcnids",
            'en': "of arachnids",
            'es': "de arañas",
            'fr': "d'araignées",
            'id': "arachnida",
            'it': "di ragni",
            'ro': "de arahnide",
        },
   "Q5113":{
            'ar': "من الطيور",
            'ca': "d'ocells",
            'en': "of birds",
            'es': "de aves",
            'fr': "d'oiseaux",
            'gl': "de aves",
            'id': "burung",
            'it': "di uccelli",
            'ro': "de păsări",
            'sq': "e zogjve",
        },
   "Q10908":{
            'ar': "من البرمائيات",
            'en': "of amphibians",
            'es': "de anfibios",
            'fr': "d'amphibiens",
            'id': "amfibi",
            'it': "di anfibi",
            'ro': "de amfibieni",
            'ru': "род амфибий",
            'sq': "e amfibeve",
        },
   "Q152":{
            'ar': "من الأسماك",
            'en': "of fishes",
            'es': "de peces",
            'fr': "de poissons",
            'id': "ikan",
            'it': "di pesci",
            'pt': "de peixes",
            'pt-br': "de peixes",
            'ro': "de pești",
            'sq': "e peshqëve",
        },#{ "ar": "من الأسماك","en": "of fish" },
   "Q756":{
            'ar': "من النباتات",
            'ca': "de plantes",
            'en': "of plants",
            'es': "de plantas",
            'fr': "de plantes",
            'gl': "de plantas",
            'id': "tumbuh-tumbuhan",
            'pt': "de plantas",
            'nl': "van planten",
            'pt-br': "de plantas",
            'ro': "de plante",
            'sq': "e bimëve",
        },
   "Q764":{
            'ar': "من الفطريات",
            'en': "of fungi",
            'es': "de hongos",
            'fr': "de champignons",
            'gl': "de fungos",
            'id': "fungi",
            'it': "di funghi",
            'pt': "de fungos",
            'pt-br': "de fungos",
            'sq': "e kërpudhave",
        },
   'Q25326': { # نوع:"" , جنس:"".
            'ar': "من الرخويات",
            'ca': "de mol·luscs",
            'en': "of molluscs",
            'es': "de moluscos",
            'fr': "de mollusques",
            'gl': "de moluscos",
            'he': "סוג של רכיכה",
            'id': "moluska",
            'it': "di molluschi",
            'ro': "de moluște",
            'sq': "e molusqeve",
        }, 
    "Q127282":{
    "ar": "من شعاعيات الزعانف"
    , "en": "of actinopterygii"
    },  #   10000   ,#spe  ,#genus   ,#variety   ,#
    "Q831482":{
    "ar": "من حزازيات حقيقية"
    , "en": "of bryopsida"
    },    #   10000 ,#spe  ,#genus   ,#variety   ,#
    "Q133571":{
    "ar": "من اللقنورانية"
    , "en": "of lecanoromycetes"
    }, #   10000    ,#spe  ,#genus   ,#variety   ,#
    "Q167367":{
    "ar": "من ألفية الأرجل"
    , "en": "of diplopoda"
    },  #   10000   ,#spe  ,#genus   ,#variety   ,#
    "Q25368":{
    "ar": "من ذوات الصدفتين"
    , "en": "of bivalvia"
    },   #   10000  ,#spe  ,#genus   ,#variety   ,#
    "Q134677":{
    "ar": "من السراخس الكنباثية"
    , "en": "of equisetopsida"
    }, #   10000    ,#spe  ,#genus   ,#variety   ,#
    "Q182978":{
    "ar": "من لينات الدرقة"
    , "en": "of malacostraca"
    },   #   10000  ,#spe  ,#genus   ,#variety   ,#
    "Q4867740":{
    "ar": "من بطنيات القدم"
    , "en": "of gastropoda"
    },    #   10000 ,#spe  ,#genus   ,#variety   ,#
    "Q18952":{
    "ar": "من كثيرات الأشعار"
    , "en": "of polychaeta"
    },    #   10000 ,#spe  ,#genus   ,#variety   ,#
    "Q373615":{
    "ar": "من السراخس الرقيقة المباغ"
    , "en": "of leptosporangiate fern"
    },    #   10000 ,#spe:34558  ,#genus   ,#variety   ,#
    "Q132662":{
    "ar": "من فكيات الأرجل"
    , "en": "of maxillopoda"
    },    #   10000 ,#spe  ,#genus   ,#variety   ,#
    "Q27720":{
    "ar": "من الغاريقونانية"
    , "en": "of agaricomycetes"
    }, #   10000    ,#spe  ,#genus   ,#variety   ,#
    "Q132159":{
    "ar": "من الدرينانية"
    , "en": "of dothideomycetes"
    },  #   9594    ,#spe  ,#genus   ,#variety   ,#
    "Q28524":{
    "ar": "من الزهريات الشعاعية"
    , "en": "of anthozoa"
    },   #   9166   ,#spe  ,#genus   ,#variety   ,#
    "Q133607":{
    "ar": "من السوردارانية"
    , "en": "of sordariomycetes"
    },    #   8873  ,#spe  ,#genus   ,#variety   ,#
    "Q276412":{
    "ar": "من الصدفيات"
    , "en": "of ostracoda"
    },  #   7296    ,#spe  ,#genus   ,#variety   ,#
    "Q132006":{
    "ar": "من شقرانانية"
    , "en": "of pucciniomycetes"
    },   #   6462   ,#spe  ,#genus   ,#variety   ,#
    }

#---
def logme(item, json):
    cap = [ '\n\t\t\t"%s": "%s",' % (json[x]['des'][0] , json[x]['count'][0]) for x in json.keys()]
    lllll = '%s' % ','.join(cap)
    with codecs.open("taxo/checklist.py", "a", encoding="utf-8") as logfile:
        #fao = json.JSONEncoder().encode(arabic[item])
        xaxa = '\t"%s": {%s\n\t\t},\n' %  (item, lllll)
        pywikibot.output(xaxa)
        logfile.write(xaxa)
        logfile.close()
#---
qoqo = '''SELECT 
?des (COUNT(?des) AS ?count)
WHERE {
  BIND(wd:%s AS ?mama)
  ?item wdt:P105 ?P105.  ?P105 rdfs:label ?des. FILTER((LANG(?des)) = "ar")  # احصاء المرتبة التصنيفية
  ?item wdt:P31 wd:Q16521. ?item wdt:P171* ?mama. 
  }

GROUP BY ?des ?lang ?P105ar
ORDER BY DESC(?count)
limit 100'''
arabic3 = {"Q132006":{"ar": "من شقرانانية", "en": "of pucciniomycetes"}}
def change():
    print('check_quarry:')
    for item in arabic.keys():
        try:
            #---
            json = himoBOT.sparql_generator_url2(qoqo % item)
            lenth = len(json.keys())
            print('lenth : %d. %s' % (lenth , item) )
            #pywikibot.output(json)
            logme(item, json )
            #---
        except:
            pass
#---
if __name__ == "__main__":  
     change()
#---
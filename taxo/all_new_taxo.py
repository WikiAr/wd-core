#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

 
"""
#
# (C) Ibrahem Qasim, 2022
#
#

'''
SELECT 
?des ?lang
(COUNT(?des) AS ?count)
WHERE {
  BIND(wd:Q132006 AS ?mama)
  #?item schema:description ?des .  filter(lang(?des) = "en")     # إحصاء الأوصاف
  ?item schema:description ?des .BIND(lang(?des) AS ?lang)     # إحصاء الأوصاف
  #?item wdt:P105 ?P105.  ?P105 rdfs:label ?des. FILTER((LANG(?des)) = "ar")  # احصاء المرتبة التصنيفية
  ?item wdt:P31 wd:Q16521. ?item wdt:P171* ?mama. 
  #SERVICE wikibase:label { bd:serviceParam wikibase:language "en" }    
  }

GROUP BY ?des ?lang
ORDER BY DESC(?count)
limit 100
'''

#---
'''
# استعلام عدد استخدامات عنصر حسب المرتبة التصنيفية
SELECT ?P105Label  (count(?item) as ?ct)
WHERE {
  ?item wdt:P31 wd:Q16521 ;
        wdt:P171* wd:Q831482 ;
        wdt:P105 ?P105 ;
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en" }
}
GROUP BY ?P105Label
ORDER BY DESC(?ct)
'''

Arabic={
   "Q47253":{
        'ar': "من الديدان",
        #'ca': "de ",
        #'nl': "van ",
        'en': "of worms",
        #'nl': "van ",
        #'es': "de ",
        #'fr': "de ",
        #'gl': "de ",
        #'id': "",
        #'ro': "de ",
        #'sq': "e ",
        },
   "Q808":{
        'ar': "من الفيروسات",
        #'ca': "de ",
        'nl': "van algen",
        'en': "of virus",
        'nl': "van virussen",
        #'es': "de ",
        #'fr': "de ",
        #'gl': "de ",
        #'id': "",
        #'ro': "de ",
        #'sq': "e ",
        },
   "Q37868":{
        'ar': "من الطحالب",
        'ca': "de mamífers",
        'nl': "van algen",
        'en': "of algae",
        'es': "de algas",
        'fr': "de mammifères",
        'gl': "de algas",
        'id': "alga",
        'ro': "de alge",
        'sq': "e algave",
        },
   "Q7377":{
        'ar': "من الثدييات",
        'ca': "de mamífers",
        'en': "of mammals",
        'nl': "van zoogdieren",
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
        'en': "van reptielen",
        'es': "de reptiles",
        'fr': "de reptiles",
        'id': "reptilia",
        'ro': "de reptile",
        'sq': "e zvarranikëve",
        },
   "Q1390":{#/
        'ar': "من الحشرات",
        'an': "d'insecto",
        'gl': 'de insecto',
        'ca': "d'insectes",
        'nl': "van insecten",
        'en': "of insects",
        'es': "de insectos",
        'fr': "d'insectes",
        'id': "serangga",
        'it': "di insetti",
        'pt': "de insetos",
        'pt-br': "de insetos",
        'ro': "de insecte",
        'ru': "род насекомых",
        'sq': "e insekteve",
        },#/
   "Q1358":{
        'ar': "من العنكبوتيات",
        'ca': "d'aràcnids",
        #'de': "der Gattung Caeculisoma",
        'en': "of arachnids",
        'nl': "van spinachtigen",
        'es': "de arañas",
        'fr': "d'araignées",
        'id': "arachnida",
        'it': "di ragni",
        'ro': "de arahnide",
        },
   "Q5113":{#/
        'ar': "من الطيور",
        'ca': "d'ocells",
        'nl': "van vogels",
        'en': "of birds",
        'es': "de aves",
        'fr': "d'oiseaux",
        'gl': "de aves",
        'id': "burung",
        'it': "di uccelli",
        'ro': "de păsări",
        'sq': "e zogjve",
        },
   "Q10908":{#/
        'ar': "من البرمائيات",
        'en': "of amphibians",
        'nl': "van amfibieën",
        'es': "de anfibios",
        'fr': "d'amphibiens",
        'id': "amfibi",
        'it': "di anfibi",
        'ro': "de amfibieni",
        'ru': "род амфибий",
        'sq': "e amfibeve",
        },
   "Q152":{#/
        'ar': "من الأسماك",
        'en': "of fishes",
        'nl': "van vissen",
        'es': "de peces",
        'fr': "de poissons",
        'id': "ikan",
        'it': "di pesci",
        'pt': "de peixes",
        'pt-br': "de peixes",
        'ro': "de pești",
        'sq': "e peshqëve",
        },
   "Q756":{#/
        'ar': "من النباتات",
        'ca': "de plantes",
        'en': "of plants",
        'es': "de plantas",
        'fr': "de plantes",
        'gl': "de plantas",
        'it': "di cactus",
        'id': "tumbuh-tumbuhan",
        'pt': "de plantas",
        'nl': "van planten",
        'pt-br': "de plantas",
        'ro': "de plante",
        'sq': "e bimëve",
        },
   "Q764":{#/
        'ar': "من الفطريات",
        'en': "of fungus",
        'es': "de hongos",
        'fr': "de champignons",
        'gl': "de fungos",
        'nl': "van schimmels",
        'id': "fungi",
        'it': "di funghi",
        'pt': "de fungos",
        'pt-br': "de fungos",
        'sq': "e kërpudhave",
        },
   'Q25326': {#/
        'ar': "من الرخويات",
        'ca': "de mol·luscs",
        'en': "of molluscs",
        'nl': "van weekdieren",
        'es': "de moluscos",
        'fr': "de mollusques",
        'gl': "de moluscos",
        'he': "סוג של רכיכה",
        'id': "moluska",
        'it': "di molluschi",
        'ro': "de moluște",
        'sq': "e molusqeve",
        },
   "Q25364":{
        'ar': "من القشريات",
        #'ca': "de ",
        #'nl': "van ",
        'en': "of crustaceans",
        'nl': "van kreeftachtigen",
        'es': "de crustáceos",
        'fr': "de crustacés",
        #'gl': "de ",
        #'id': "",
        #'ro': "de ",
        #'sq': "e ",
        },
   "":{
        "ar": "من المفصليات"
        , "en": "of arthropods"
        },
   "Q25368":{    #   10000
        "ar": "من ذوات الصدفتين"
        , "en": "of bivalvia"
        },
   "Q134677":{    #   10000
        "ar": "من السراخس الكنباثية"
        , "en": "of equisetopsida"
        },
   "Q182978":{    #   10000
        "ar": "من لينات الدرقة"
        , "en": "of malacostraca"
        },
   "Q4867740":{    #   10000
        "ar": "من بطنيات القدم"
        , "en": "of gastropoda"
        },
   "Q18952":{    #   10000
        "ar": "من كثيرات الأشعار"
        , "en": "of polychaeta"
        },
   "Q28319":{    #   
        "ar": "من حرشفيات الأجنحة"
        , "en": "of lepidoptera"
        },
   "Q25441":{   
        "ar": "من اللاسعات",
        #'ca': "de ",
        #'nl': "van ",
        'en': "of cnidarian",
        'nl': "van neteldieren",
        'es': "de cnidaria",
        'fr': "de cnidaria",
        'it': "di coralli",
        #'gl': "de ",
        #'id': "",
        #'ro': "de ",
        #'sq': "e ",
        },

   }
#---
a = {
   "Q831482":{  #32579 #   نباتات 
        "ar": "من الحزازيات الحقيقية"
        , "en": "of bryopsida"
       },
   "Q276412":{  #   7296 #القشريات
       "ar": "من الصدفيات"
       , "en": "of ostracoda"
       },
   "Q132662":{    #   10000	#قشريات
        "ar": "من فكيات الأرجل"
        , "en": "of maxillopoda"
        },
   "Q133571":{    #   10000#	فطريات
        "ar": "من اللقنورانيات"
        , "en": "of lecanoromycetes"
        },
   "Q132006":{   #   6462
       "ar": "من الشقرانانيات"
       , "en": "of pucciniomycetes"
       },
   "Q133607":{    #   8873 
       "ar": "من السوردارانيات"
       , "en": "of sordariomycetes"
       },
   "Q28524":{   #   9166		# القراصات		#لاسعات
        "ar": "من الزهريات الشعاعية"
        , "en": "of anthozoa"
        },
   "Q27720":{    #   10000
        "ar": "من الغاريقونانيات",
        "en": "of agaricomycetes"
        },
   "Q373615":{    #   10000
        "ar": "من السراخس الرقيقة المباغ"
        , "en": "of leptosporangiate fern"
        },
   "Q167367":{    #   10000
        "ar": "من ألفيات الأرجل"
        , "en": "of diplopoda"
        },
    }
#---
arabic = {}
for x in Arabic:
	arabic[x] = Arabic[x]
#---
# arabic['Q167367'] = arabic[""]#مفصليات
#
arabic['Q28524'] = arabic["Q25441"]#لاسعات

arabic['Q132662'] = arabic["Q25364"]#قشريات
arabic['Q831482'] = arabic["Q756"]#نباتات
arabic['Q373615'] = arabic["Q756"]#نباتات
arabic['Q276412'] = arabic["Q25364"]#قشريات
arabic['Q127282'] = arabic["Q152"]

arabic['Q132159'] = arabic["Q764"] #فطريات  #{ "ar": "من الدرينانية", "en": "of dothideomycetes"
arabic['Q133571'] = arabic["Q764"]
arabic['Q132006'] = arabic["Q764"]
arabic['Q133607'] = arabic["Q764"]
arabic['Q27720'] = arabic["Q764"]

#---
arabic2={
    "Q17156":{"ar": "من اللافصيميات", "en": "of Adenophorea"},  #   6314
    "Q623286":{"ar": "من داخليات الفك", "en": "of Entognatha"}, #   5721
    "Q212798":{"ar": "من المهتزات", "en": "of Turbellaria"},    #   5705
    "Q181989":{"ar": "من الأبابيات", "en": "of Hydrozoa"},  #   4667
    "Q190701":{"ar": "من قافزات الذيل", "en": "of Springtail"}, #   4396
    "Q133551":{"ar": "من الملاسانيات", "en": "of Leotiomycetes"},   #   4066
    "Q207547":{"ar": "من المثقوبات", "en": "of Trematode"}, #   3812
    "Q43447":{"ar": "من أم أربعة وأربعين", "en": "of Chilopoda"},   #   3643
    "Q190090":{"ar": "من الكيسيات", "en": "of Ascidiacea"}, #   3196
    "Q132180":{"ar": "من العوفنيات", "en": "of Eurotiomycetes"},    #   2937
    "Q134668":{"ar": "من متقلبات غاما", "en": "of Gammaproteobacteria"},    #   2605
    "Q839350":{"ar": "من السرجيات", "en": "of Clitellata"}, #   2601
    "Q17157":{"ar": "من السيسيرنينتيات", "en": "of Secernentea"},   #   2513
    "Q184573":{"ar": "من الطحالب البنية", "en": "of Phaeophyceae"}, #   2428
    "Q25349":{"ar": "من نجوم البحر", "en": "of starfish"},  #   2422
    "Q8316":{"ar": "من ثنائيات الفلقة", "en": "of Dicotyledones"},  #   2316
    "Q127470":{"ar": "من خيار البحر", "en": "of sea cucumber"}, #   2217
    "Q1149748":{"ar": "من حزازيات ذئبية", "en": "of Lycopodiopsida"},   #   2156
    "Q25371":{"ar": "من الأسماك الغضروفية", "en": "of Chondrichthyes"}, #   2075
    "Q306579":{"ar": "من متقلبات ألفا", "en": "of Alphaproteobacteria"},    #   1962
    "Q194257":{"ar": "من صفيحيات الخياشيم الغضروفية", "en": "of Elasmobranchii"},   #   1955
    "Q1329304":{"ar": "من الصنوبرانيات", "en": "of Pinopsida"}, #   1901
    "Q149128":{"ar": "من العصيات", "en": "of Bacilli"}, #   1797
    "Q193006":{"ar": "من قليلات الأشواك", "en": "of Oligochaeta"},  #   1786
    "Q159715":{"ar": "من الديدان الشريطية", "en": "of Cestoda"},    #   1726
    "Q128257":{"ar": "من رأسيات القدم", "en": "of Cephalopoda"},    #   1682
    "Q19106":{"ar": "من عناكب البحر", "en": "of Pycnogonida"},  #   1589
    "Q83483":{"ar": "من القنفذ البحري", "en": "of sea urchin"}, #   1432
    "Q188906":{"ar": "من عديدة الأصداف", "en": "of chiton"},    #   1275
    "Q843232":{"ar": "من فنجانيانيات", "en": "of Pezizomycetes"},   #   1266
    "Q1151744":{"ar": "من الطحالب المترابطة", "en": "of Zygnematophyceae"}, #   1234
    "Q3178797":{"ar": "من المخروطانيات", "en": "of Conoidasida"},   #   1165
    "Q132809":{"ar": "من المطثيات", "en": "of Clostridia"}, #   1145
    "Q136674":{"ar": "من متقلبات بيتا", "en": "of Betaproteobacteria"}, #   1084
    "Q188360":{"ar": "من غلصميات الأرجل", "en": "of Branchiopoda"}, #   1064
    "Q1069627":{"ar": "من السكيرانية", "en": "of Saccharomycetes"}, #   939
    "Q271631":{"ar": "من أوليات الذنب", "en": "of Protura"},    #   929
    "Q1096274":{"ar": "من الحزازيات الإسويطية", "en": "of Isoetopsida"},    #   890
    "Q209924":{"ar": "من الإسفنجيات الجيرية", "en": "of calcareous sponge"},    #   863
    "Q147868":{"ar": "من المرشانتاناوت", "en": "of Marchantiopsida"},   #   764
    "Q238314":{"ar": "من الأصداف النابية", "en": "of Scaphopoda"},  #   684
    "Q132763":{"ar": "من السوادانية", "en": "of Ustilaginomycetes"},    #   663
    "Q642852":{"ar": "من حزازيات يشعورية", "en": "of Polytrichopsida"}, #   629
    "Q275657":{"ar": "من مخاطيات الأبواغ", "en": "of Myxosporea"},  #   596
    "Q132609":{"ar": "من الأشنيات الخضراء", "en": "of Chlorophyceae"},  #   546
    "Q1137709":{"ar": "من أصيصيانية", "en": "of Chytridiomycetes"}, #   536
    "Q136846":{"ar": "من الزملولانية", "en": "of Exobasidiomycetes"},   #   448
    "Q1422487":{"ar": "من حزازيات سبخية", "en": "of Sphagnopsida"}, #   447
    "Q5605610":{"ar": "من السيكادانية", "en": "of Cycadopsida"},    #   441
    "Q307535":{"ar": "من متقلبات دلتا", "en": "of Deltaproteobacteria"},    #   416
    "Q221563":{"ar": "من ثنائيات الذنب", "en": "of Diplura"},   #   392
    "Q12207651":{"ar": "من الحزازيات القرناء", "en": "of Anthocerotopsida"},    #   389
    "Q272388":{"ar": "من الفنجانيات", "en": "of Scyphozoa"},    #   352
    "Q1054206":{"ar": "من الملحاوات العصوية", "en": "of Halobacteria"}, #   313
    "Q13389544":{"ar": "من الكببيانية", "en": "of Glomeromycetes"}, #   298
    "Q223597":{"ar": "من الطلائعيات البيضية", "en": "of Oomycetes"},    #   285
    "Q131796":{"ar": "من الرخصيات", "en": "of Mollicutes"}, #   277
    "Q146300":{"ar": "من الأنبوبيات", "en": "of Tubulinea"},    #   258
    "Q3730841":{"ar": "من العصوانيات", "en": "of Bacteroidia"}, #   246
    "Q132016":{"ar": "من الأشنيات الأولفانية", "en": "of Ulvophyceae"}, #   244
    "Q1763065":{"ar": "من الطحالب الذهبية", "en": "of Chrysophyceae"},  #   229
    "Q160830":{"ar": "من لحميات الزعانف", "en": "of Sarcopterygii"},    #   220
    "Q131630":{"ar": "من ذوات منشأ الحركة", "en": "of Kinetoplastea"},  #   193
    "Q1011212":{"ar": "من الجنتوانية", "en": "of Gnetopsida"},  #   188
    "Q136797":{"ar": "من متقلبات إيبسيلونية", "en": "of Epsilonproteobacteria"},    #   154
    "Q12673556":{"ar": "من البكتيريا الملتوية", "en": "of Spirochaetes"},   #   144
    "Q589697":{"ar": "من دودة البلوط", "en": "of Enteropneusta"},   #   136
    "Q1953103":{"ar": "من المستحراوات المتقلبة", "en": "of Thermoprotei"},  #   132
    "Q1051432":{"ar": "من الميثاناوات الجرثومية", "en": "of Methanomicrobia"},  #   128
    "Q488032":{"ar": "من مخفيات النبت", "en": "of Cryptophyceae"},  #   121
    "Q135200":{"ar": "من المخندقانيات", "en": "of Taphrinomycetes"},    #   105
    "Q244147":{"ar": "من المؤتلفات", "en": "of Symphyla"},  #   105
    "Q610887":{"ar": "من الثاليات", "en": "of Thaliacea"},  #   104
    "Q189069":{"ar": "من مندمجات الأقواس", "en": "of synapsid"},    #   99
    "Q10431061":{"ar": "من الأروميانية", "en": "of Blastocladiomycetes"},   #   91
    "Q273179":{"ar": "من المكعبيات", "en": "of Box jellyfish"}, #   87
    "Q162678":{"ar": "من الدياتوم", "en": "of Diatomea"},   #   84
    "Q28960":{"ar": "من اليرقانيات", "en": "of Appendicularia"},    #   83
    "Q10584811":{"ar": "من البويغيات المكروية", "en": "of Microsporea"},    #   66
    "Q510333":{"ar": "من البيركولوزوا", "en": "of Heterolobosea"},  #   58
    "Q1208690":{"ar": "من الطحالب الكارية", "en": "of Charophyceae"},   #   56
    "Q138088":{"ar": "من حلميات الأسنان", "en": "of Thelodonti"},   #   54
    "Q1135978":{"ar": "من المستحراوات المكورة", "en": "of Thermococci"},    #   53
    "Q19436":{"ar": "من عريضات الأجنحة", "en": "of Eurypterid"},    #   45
    "Q490800":{"ar": "من متشعبات الأرجل", "en": "of Remipedia"},    #   45
    "Q19430":{"ar": "من سيفيات الذيل", "en": "of Xiphosura"},   #   37
    "Q10596701":{"ar": "من السويطيانية", "en": "of Neocallimastigomycetes"},    #   33
    "Q865046":{"ar": "من الفصيات", "en": "of Lobosea"}, #   22
    "Q20388475":{"ar": "من البفلوفيانية", "en": "of Pavlovophyceae"},   #   21
    "Q648056":{"ar": "من الفطريات الناقصة", "en": "of Fungi imperfecti"},   #   20
    "Q586245":{"ar": "من مخروطيات الأسنان", "en": "of Conodont"},   #   19
    "Q132649":{"ar": "من رأسيات الدرقة", "en": "of Cephalocarida"}, #   19
    "Q425920":{"ar": "من الطفيليات الدموية الحيوانية", "en": "of Haematozoa"},  #   18
    "Q1349847":{"ar": "من السحناوات", "en": "of Thermomicrobia"},   #   17
    "Q188549":{"ar": "من الجلكانيات", "en": "of Hyperoartia"},  #   17
    "Q943568":{"ar": "من العتيقاوات الكروية", "en": "of Archaeoglobi"}, #   13
    "Q3452046":{"ar": "من الجبائل", "en": "of Sarcodina"},  #   12
    "Q240433":{"ar": "من السوطيات", "en": "of Mastigophora"},   #   12
    "Q332403":{"ar": "من الجرابتوليت", "en": "of Graptolithinia"},  #   8
    "Q2563582":{"ar": "من المتكيسات الرئوية", "en": "of Pneumocystidomycetes"}, #   8
    "Q21447558":{"ar": "من البويغيات المتشنكوفيلية", "en": "of Metchnikovellea"},   #   7
    "Q20635347":{"ar": "من الملتوياوات", "en": "of Spirochaetia"},  #   7
    "Q3329480":{"ar": "من متقلبات زيتا", "en": "of Zetaproteobacteria"},    #   5
    "Q6074541":{"ar": "من الفطريات الطحلبية", "en": "of Phycomycetes"}, #   5
    "Q15129670":{"ar": "من العرفيات القرصية", "en": "of Cristidiscoidea"},  #   5
    "Q851400":{"ar": "من السيستويديات", "en": "of Cystoids"},   #   3
    "Q19962619":{"ar": "من الزرقاويات", "en": "of Glaucocystophyceae"}, #   3
    "Q1566901":{"ar": "من البلاستويديات", "en": "of Blastoid"}, #   3
    "Q15129663":{"ar": "من الأعراف القرصية", "en": "of Cristidiscoidia"},   #   2
    "Q867927":{"ar": "من الميثاناوات النارية", "en": "of Methanopyri"}, #   1
    "Q811147":{"ar": "من الكرات النافحة", "en": "of Gasteroid fungi"},  #   1
    "Q22933896":{"ar": "من الميدوزات الفنجانية", "en": "of Scyphomedusae"}, #   1
    "Q74083":{"ar": "من الأسماك المدرعة", "en": "of Ostracoderm"},  #   1
    "Q28805588":{"ar": "من العفنانيات", "en": "of Mucoromycetes"},  #   1
    "Q21025810":{"ar": "من الأشنيات الخضراء المتشجرة", "en": "of Chlorodendrophyceae"}, #   1
    "Q12967693":{"ar": "من السراخس الماراتية", "en": "of Marattiopsida"},   #   1
    "Q11937877":{"ar": "من القشريات المتعددة", "en": "of Multicrustacea"},  #   1
    }
#---
gens = {
    'Q7432' : { #1918849
            "ar": "نوع",
            "an": "especie",
            "en": "species",
            "ca": "espècie",
            "es": "especie",
            "de": "Art",
            "fr": "espèce",
            "gl": "especie",
            "id": "spesies",
            "it": "specie",
            "pt": "espécie",
            "pt-br": "espécie",
            "ro": "specie",
            'sq': 'specie',
            'nl': 'soort',
            'pt-br': 'espécie',
            'pt': 'espécie',
        }, 
    'Q34740' : {#206899
            "ar": "جنس",
            "en": "genus",
            'ca': 'gènere',
            'fr': 'genre',
            'es': 'género',
            'gl': 'xénero', 
            'nl': 'geslacht',
            'ro': 'gen',
            'sq': 'gjini',
            'it': 'genere',
            'id': 'genus',
            'pt-br': 'gênero',
            'pt': 'género',
        },
    'Q68947' : {#63166
            "ar": "نويع",
            "en": "subspecies",
            'ca': '',
            'fr': '',
            'es': '',
            'gl': '', 
            'nl': '',
            'ro': '',
            'sq': '',
            'it': '',
            'id': '',
            'pt-br': '',
            'pt': '',
        },
    'Q767728' : {#15739
            "ar": "ضرب",
            "es": "variedad",
            "en": "variety",
            'fr': 'variété',
            'de': 'Varietät',
            'nl': 'variëteit', 
            'de': 'Varietät', 
            #'ro': '',
            #'sq': '',
            'it': 'varietà',
        },
    "Q35409" : {#18520
            "en": "family",
            "nl": "familie",    
            "ar": "فصيلة",
            'fr': 'famille',
            'es': 'familia',
            'cy': 'teulu',
            'de': 'Familie',
            'nl': 'familie', 
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'famiglia',
        },
    "Q36602" : {#3061
            "en": "order",
            "es": "orden",
            "nl": "orde",   
            "ar": "رتبة" ,
            'fr': 'ordre',
            'de': 'Ordnung',
            #'nl': '', 
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'ordine',
        },
    "Q3181348" : {#3353
            "en": "section",
            "nl": "sectie",    
            "ar": "قسم" ,
            #'fr': '',
            'de': 'Sektion',
            #'nl': '', 
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            #'it': '',
        },
    "Q2455704" : {#9863
            "en": "subfamily",
            "nl": "onderfamilie",   
            "ar": "فُصيلة",
            'fr': 'sous-famille',
            'de': 'Unterfamilie',
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'sottofamiglia',
        },
    "Q3238261" : {#5677
            "en": "subgenus",
            "nl": "ondergeslacht",  
            "ar": "جُنيس",
            #'fr': 'sous-genre',
            'de': 'Untergattung',
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'sottogenere',
        },
    "Q2136103" : {#2346
            "en": "superfamily",
            "nl": "superfamilie",   
            "ar": "فصيلة عليا" ,
            #'fr': '',
            'de': 'Überfamilie',
            #'nl': '', 
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'superfamiglia',
        },
    "Q227936" : {#6801
            "en": "tribe",
            "nl": "geslachtengroep",    
            "ar": "قبيلة عليا",
            'es': 'subfamili',
            #'fr': '',
            'de': 'Tribus',
            #'nl': '', 
            #'gl': '', 
            #'ro': '',
            #'sq': '',
            'it': 'tribù',
        },
    }
#---
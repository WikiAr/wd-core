#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
'''
"Q1500350" : {"ar" : "بلدة مدينة في الصين" }, #    10527
"Q50231" : {"ar" : "التقسيم الإداري في الصين" }, # 13842
"Q192287" : {"ar" : "كيان إداري إقليمي في روسيا" }, #  16536
"Q1529096" : {"ar" : "قرية تركية" }, # 17578
"Q634099" : {"ar" : "بلدة ريفية روسية" }, #    19125
"Q735428" : {"ar" : "قرية في الصين" }, #   20848
"Q21672098" : {"ar" : "قرية أوكرانية" }, # 26422
"Q23925393" : {"ar" : "دوار مغربي" }, #    32023
"Q484170" : {"ar" : "بلدية في فرنسا" }, #  40170
"Q3558970" : {"ar" : "قرية في بولندا" }, # 56111
"Q13220204" : {"ar" : "المستوى الثاني من التقسيم الإداري" }, # 10141
"Q2389082" : {"ar" : "جماعة قروية فيتنامية" }, #   10001

'''
#
# ---
# (.*)\t(.*)
# , "$1" : {"ar" : "$2" }
# ---
faft = {
    "Q5633421": {"ar": "دورية علمية"},
    "Q5": {"ar": "إنسان"},
    "Q318": {"ar": "مجرة"},  # 2088509
    "Q523": {"ar": "نجم"},  # 3257793
    "Q1931185": {"ar": " مصدر راديو فلكي"},  # 351376
    "Q3863": {"ar": "كويكب"},
    "Q6243": {"ar": "نجم متغير"},
    "Q7187": {"ar": "جين"},
    "Q7366": {"ar": "أغنية"},
    "Q7889": {"ar": "لعبة فيديو"},
    "Q9842": {"ar": "مدرسة ابتدائية"},
    "Q13632": {"ar": "سديم كوكبي"},
    "Q16521": {"ar": "أصنوفة"},
    "Q30612": {"ar": "تجربة سريرية"},
    "Q95074": {"ar": "شخصية خيالية"},
    # "Q101352" : {"ar" : "اسم العائلة" }, # family name
    "Q115518": {"ar": "مجرة ذات سطوع سطحي منخفض"},
    "Q130019": {"ar": "نجم كربوني"},
    "Q134556": {"ar": "أغنية منفردة"},
    "Q178122": {"ar": "الآريا"},
    "Q191067": {"ar": "مقالة"},
    "Q202444": {"ar": "الاسم الأول"},
    "Q204194": {"ar": "سديم مظلم"},
    "Q207628": {"ar": "تأليف موسيقي"},
    "Q215380": {"ar": "طاقم موسيقي"},
    "Q222910": {"ar": "ألبوم تجميعي"},
    "Q277338": {"ar": "جين كاذب"},
    "Q620615": {"ar": "تطبيق محمول"},
    "Q737498": {"ar": "دورية أكاديمية"},
    "Q486972": {"ar": "مستوطنة"},
    "Q482994": {"ar": "ألبوم"},
    "Q732577": {"ar": "منشور"},
    "Q1149652": {"ar": "مقاطعة في الهند"},
    "Q1332364": {"ar": "متغير بيضاوي دوار"},
    "Q1348589": {"ar": "فوهة قمرية"},
    "Q1457376": {"ar": "كسوف نجم ثنائي"},
    "Q4502142": {"ar": "عمل فني مرئي"},
    "Q15917122": {"ar": "نجم متغير دوار"},
    "Q19389637": {"ar": "مقالة سيرة ذاتية"},
    "Q21014462": {"ar": "خط خلية"},
    "Q23925393": {"ar": "دوار مغربي"},
    "Q53764738": {"ar": "مقطع صيني"},
    "Q71963409": {"ar": "تجمع مجري مدمج"},

    "Q20741022": {"ar": "digital camera model"},
    "Q253019": {"ar": "Ortsteil"},
    "Q1153690": {"ar": "long period variable"},
    "Q1690211": {"ar": "lavoir"},
    "Q2065704": {"ar": "district court"},
    "Q2247863": {"ar": "high proper-motion star"},
    "Q7302866": {"ar": "audio track"},
    "Q13005188": {"ar": "mandal"},
    "Q21278897": {"ar": "Wiktionary redirect"},
    "Q21573182": {"ar": "Naturdenkmal in Germany"},
    "Q26703203": {"ar": "stumbling stone"},
    "Q50386450": {"ar": "operatic character"},
    "Q66619666": {"ar": "Red Giant Branch star"},
    "Q67206691": {"ar": "infrared source"},
    "Q72802508": {"ar": "emission-line galaxy"},
    "Q72803622": {"ar": "emission-line star"},
    "Q88965416": {"ar": "school unit"},
}
# ---
asdasd = '''
SELECT ?item ?placear WHERE {
  ?item wdt:P279* wd:Q2221906.
?item rdfs:label ?placear.FILTER((LANG(?placear)) = "ar")
  FILTER(NOT EXISTS {?item wdt:P17 ?df.})
}
LIMIT 1000
'''
# ---
yuxxx = '''

SELECT
#?value ?valueLabel ?ct
(CONCAT('    \"', STRAFTER(STR(?value), "/entity/"), '" : {"ar" : "') AS ?qq)
?valueLabel
(CONCAT('" },#') AS ?vf)
?ct
WHERE { {
    SELECT ?value (COUNT(*) AS ?ct) (SAMPLE(?item) AS ?sampleitem) WHERE {
      ?item wdt:P31 ?value.
      ?value (wdt:P279*) wd:Q2221906.
    }
    GROUP BY ?value
    ORDER BY DESC (?ct)
    LIMIT 500
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". }
}
ORDER BY DESC (?ct) (?value)


SELECT
#?value ?valueLabel ?ct
(CONCAT('    \"', STRAFTER(STR(?value), "/entity/"), '" : {"ar" : "') AS ?qq)
?valueLabel
(CONCAT('" },#') AS ?vf)
?ct
WHERE { {
    SELECT ?value (COUNT(*) AS ?ct) (SAMPLE(?item) AS ?sampleitem) WHERE {
      ?item wdt:P31 ?value.

      ?item (wdt:P131|wdt:P17) ?sd.
    }
    GROUP BY ?value
    ORDER BY DESC (?ct)
    LIMIT 500
  }
  SERVICE wikibase:label { bd:serviceParam wikibase:language "ar,en". }
}
ORDER BY DESC (?ct) (?value)

'''
# ---
placesTable = {
    "Q108325": {'ar': 'مصلى كنسي'},
    "Q1093829": {'ar': 'مدينة'},
    "Q1115575": {'ar': 'أبرشية مدنية'},
    "Q1154710": {'ar': 'أستاد كرة قدم'},
    "Q1197120": {'ar': 'بركان خامد'},
    "Q1200524": {'ar': 'بركان مركب'},
    "Q12280": {'ar': 'جسر'},
    "Q123705": {'ar': 'حي سكني'},
    "Q12518": {'ar': 'برج'},
    "Q126807": {'ar': 'روضة أطفال'},
    "Q1303167": {'ar': 'حظيرة'},
    "Q1329623": {'ar': 'مركز ثقافي'},
    "Q1330974": {'ar': 'بركان نشط'},
    "Q149566": {'ar': 'مدرسة متوسطة'},
    "Q1500350": {'ar': 'بلدة مدينة'},
    "Q1516079": {'ar': 'مجموعة تراث ثقافي'},
    "Q1529096": {'ar': 'قرية'},
    "Q159334": {'ar': 'مدرسة ثانوية'},
    "Q16917": {'ar': 'مستشفى'},
    "Q169358": {'ar': 'بركان طبقي'},
    "Q17018380": {'ar': 'خليج'},
    "Q173387": {'ar': 'قبر'},
    "Q17343829": {'ar': 'مجتمع غير مدمج'},
    "Q174782": {'ar': 'ميدان'},
    "Q1774898": {'ar': 'عيادة'},
    "Q1806785": {'ar': 'مخروط رماد'},
    "Q190250": {'ar': 'تل مركزي'},
    "Q193457": {'ar': 'بركان طيني'},
    "Q19855165": {'ar': 'مدرسة ريفية'},
    "Q212057": {'ar': 'بركان درعي'},
    "Q212198": {'ar': 'حانة'},
    "Q2143039": {'ar': 'بركان تصدعي'},
    "Q21672098": {'ar': 'قرية'},
    "Q2225692": {'ar': 'منطقة سكنية'},
    "Q2389082": {'ar': 'جماعة قروية'},
    "Q23925393": {'ar': 'دوار'},
    "Q24354": {'ar': 'مسرح'},
    "Q256020": {'ar': 'استراحة'},
    "Q27686": {'ar': 'فندق'},
    "Q28564": {'ar': 'مكتبة عامة'},
    "Q2977": {'ar': 'كاتدرائية'},
    "Q3116906": {'ar': 'قمة جبلية شاهقة'},
    "Q3257686": {'ar': 'محلية'},
    "Q3266850": {'ar': 'كيمونة'},
    "Q332614": {'ar': 'بركان هائل'},
    "Q34442": {'ar': 'طريق'},
    "Q34763": {'ar': 'شبه جزيرة'},
    "Q3558970": {'ar': 'قرية'},
    "Q3914": {'ar': 'مدرسة'},
    "Q3947": {'ar': 'منزل'},
    "Q3950": {'ar': 'فيلا'},
    "Q3957": {'ar': 'بلدة'},
    "Q41253": {'ar': 'سينما'},
    "Q43229": {'ar': 'منظمة'},
    "Q44613": {'ar': 'دير'},
    "Q459297": {'ar': 'قناة ري'},
    "Q478788": {'ar': 'بركان بارد'},
    "Q483110": {'ar': 'ملعب'},
    "Q484170": {'ar': 'بلدية'},
    "Q489357": {'ar': 'حظيرة'},
    "Q5084": {'ar': 'نجع'},
    "Q5154047": {'ar': 'كيمونة'},
    "Q526644": {'ar': 'قبة بانكيك'},
    "Q55659167": {'ar': 'مجرى ماء طبيعي'},
    "Q56436498": {'ar': 'قرية'},
    "Q5783996": {'ar': 'كوخ'},
    "Q61443690": {'ar': 'فرع مكتب بريد'},
    "Q62447": {'ar': 'منشأة جوية'},
    "Q634099": {'ar': 'بلدة ريفية'},
    "Q641226": {'ar': 'صالة'},
    "Q67383935": {'ar': 'مدرسة مختلطة'},
    "Q674775": {'ar': 'بركان غائص'},
    "Q7075": {'ar': 'مكتبة'},
    "Q735428": {'ar': 'قرية'},
    "Q771409": {'ar': 'بركان تحت جليدي'},
    "Q811979": {'ar': 'هيكل معماري'},
    "Q839954": {'ar': 'موقع أثري'},
    "Q842402": {'ar': 'معبد هندوسي'},
    "Q842478": {'ar': 'متحف'},
    "Q847017": {'ar': 'ناد رياضي'},
    "Q918230": {'ar': 'فيلا رومانية'},
    "Q928830": {'ar': 'محطة مترو'},
    "Q9826": {'ar': 'ثانوية عامة'},
    "Q9842": {'ar': 'مدرسة ابتدائية'},
    "Q995054": {'ar': 'درع ناري رسوبي'},
    "Q102496": {"ar": "رعية", "en": "parish"},
    "Q1048525": {"ar": "ملعب غولف", "en": "golf course"},
    "Q1054581": {"ar": "منطقة عازلة", "en": "Buffer zone"},
    "Q1172599": {"ar": "بوغاز", "en": "inlet"},
    "Q1174791": {"ar": "جرف", "en": "escarpment"},
    "Q1210950": {"ar": "قناة بحرية", "en": "channel"},
    "Q1210950": {"ar": "قناة بحرية", "en": "channel"},
    "Q1210950": {"ar": "قناة بحرية", "en": "channel"},
    "Q1226252": {"ar": "جزيرة متصلة", "en": "tied island"},
    "Q12284": {"ar": "قناة", "en": "canal"},
    "Q12284": {"ar": "قناة", "en": "canal"},
    "Q12284": {"ar": "قناة", "en": "canal"},
    "Q12323": {"ar": "سد", "en": "dam"},
    "Q124714": {"ar": "ينبوع", "en": "spring"},
    "Q12516": {"ar": "هرم", "en": "pyramid"},
    "Q1265665": {"ar": "بركة سمك", "en": "fish pond"},
    "Q131681": {"ar": "خزان مائي", "en": "reservoir"},
    "Q1324633": {"ar": "قاعدة بحرية", "en": "naval base"},
    "Q133215": {"ar": "كازينو", "en": "casino"},
    "Q134851": {"ar": "منحدر قاري", "en": "continental shelf"},
    "Q1368970": {"ar": "مخروط بركاني", "en": "volcanic cone"},
    "Q151957": {"ar": "جيوت", "en": "guyot"},
    "Q152005": {"ar": "حاجز مائي", "en": "drainage divide"},
    "Q159719": {"ar": "محطة طاقة", "en": "power station"},
    "Q159954": {"ar": "كالديرا", "en": "caldera"},
    "Q160091": {"ar": "سهل", "en": "plain"},
    "Q1620908": {"ar": "منطقة تاريخية", "en": "historical region"},
    "Q165": {"ar": "بحر", "en": "sea"},
    "Q16560": {"ar": "قصر", "en": "palace"},
    "Q166620": {"ar": "مستجمع مائي", "en": "drainage basin"},
    "Q166735": {"ar": "مستنقع", "en": "swamp"},
    "Q16887036": {"en": "gap"},
    "Q16970": {"ar": "كنيسة", "en": "church"},
    "Q179049": {"ar": "محمية طبيعية", "en": "nature reserve"},
    "Q184356": {"ar": "مقراب راديوي", "en": "radio telescope"},
    "Q184358": {"ar": "شعاب", "en": "reef"},
    "Q185113": {"ar": "رأس", "en": "cape"},
    "Q185187": {"ar": "طاحونة مائية", "en": "watermill"},
    "Q187223": {"ar": "بحيرة شاطئة", "en": "lagoon"},
    "Q187971": {"ar": "وادي", "en": "wadi"},
    "Q187971": {"ar": "وادي", "en": "wadi"},
    "Q188989": {"ar": "زراعة مائية", "en": "aquaculture"},
    "Q189004": {"ar": "كلية", "en": "college"},
    "Q190107": {"ar": "محطة رصد جوي", "en": "weather station"},
    "Q190928": {"ar": "حوض بناء سفن", "en": "shipyard"},
    "Q190928": {"ar": "حوض بناء سفن", "en": "shipyard"},
    "Q194408": {"ar": "نوناتاك", "en": "nunatak"},
    "Q194408": {"ar": "نوناتاك", "en": "nunatak"},
    "Q2042028": {"ar": "إفجيج", "en": "ravine"},
    "Q207326": {"ar": "قمة جبل", "en": "summit"},
    "Q214252": {"ar": "إسطبل", "en": "stable"},
    "Q22687": {"ar": "بَنْك", "en": "bank"},
    "Q22715": {"ar": "كرم", "en": "vineyard"},
    "Q22715": {"ar": "كرم", "en": "vineyard"},
    "Q23397": {"ar": "بحيرة", "en": "lake"},
    "Q23413": {"ar": "قلعة", "en": "castle"},
    "Q23442": {"ar": "جزيرة", "en": "island"},
    "Q244326": {"ar": "ملاحات", "en": "salt evaporation pond"},
    "Q245016": {"ar": "قاعدة عسكرية", "en": "military base"},
    "Q245016": {"ar": "قاعدة عسكرية", "en": "military base"},
    "Q24529780": {"ar": "نقطة", "en": "point"},
    "Q25391": {"ar": "كثيب", "en": "dune"},
    "Q283202": {"ar": "مرفأ", "en": "harbor"},
    "Q28337": {"ar": "مياه ضحلة", "en": "shoal"},
    "Q29701762": {"ar": "مستوطنة", "en": "human settlement"},
    "Q3011536": {"ar": "فاصل", "en": "Separator"},
    "Q30198": {"ar": "هور", "en": "marsh"},
    "Q31615": {"ar": "جون", "en": "cove"},
    "Q3253281": {"ar": "بركة", "en": "pond"},
    "Q3294251": {"ar": "أكمة أوراسية", "en": "hillock"},
    "Q329683": {"ar": "منطقة صناعية", "en": "industrial park"},
    "Q33506": {"ar": "متحف", "en": "museum"},
    "Q34038": {"ar": "شلال", "en": "waterfall"},
    "Q34038": {"ar": "شلال", "en": "waterfall"},
    "Q35509": {"ar": "كهف", "en": "cave"},
    "Q355304": {"ar": "مجرى مائي", "en": "watercourse"},
    "Q35666": {"ar": "مثلجة", "en": "glacier"},
    "Q35666": {"ar": "مثلجة", "en": "glacier"},
    "Q3918": {"ar": "جامعة", "en": "university"},
    "Q39594": {"ar": "خليج", "en": "bay"},
    "Q39594": {"ar": "خليج", "en": "bay"},
    "Q39715": {"ar": "منارة", "en": "lighthouse"},
    "Q39816": {"ar": "واد", "en": "valley"},
    "Q40080": {"ar": "شاطئ", "en": "beach"},
    "Q4022": {"ar": "نهر", "en": "river"},
    "Q41176": {"ar": "مبنى", "en": "building"},
    "Q43262": {"ar": "تندرا", "en": "tundra"},
    "Q4421": {"ar": "غابة", "en": "forest"},
    "Q44377": {"ar": "نفق", "en": "tunnel"},
    "Q45776": {"ar": "خلل", "en": "fjord"},
    "Q45776": {"ar": "خلل", "en": "fjord"},
    "Q46124": {"ar": "مصحة", "en": "sanatorium"},
    "Q468756": {"ar": "ضفة", "en": "bank"},
    "Q47053": {"ar": "خور", "en": "estuary"},
    "Q474": {"ar": "قناة", "en": "aqueduct"},
    "Q47521": {"ar": "جدول مائي", "en": "stream"},
    "Q47521": {"ar": "جدول مائي", "en": "stream"},
    "Q486972": {"ar": "مستوطنة", "en": "human settlement"},
    "Q491713": {"de": "Sund", "en": "sound"},
    "Q494829": {"ar": "موقف حافلات", "en": "bus station"},
    "Q502074": {"ar": "مطار مروحيات", "en": "heliport"},
    "Q503269": {"ar": "جبل بحري", "en": "seamount"},
    "Q503269": {"ar": "جبل بحري", "en": "seamount"},
    "Q5107": {"ar": "قارة", "en": "continent"},
    "Q54050": {"ar": "تل", "en": "hill"},
    "Q587682": {"ar": "بئر نفط", "en": "oil well"},
    "Q623319": {"ar": "مائدة صحراوية", "en": "mesa"},
    "Q62832": {"ar": "مرصد", "en": "observatory"},
    "Q637600": {"ar": "سبخة", "en": "sabkha"},
    "Q6501349": {"ar": "موقف سيارات", "en": "parking lot"},
    "Q697295": {"ar": "مزار", "en": "shrine"},
    "Q740445": {"ar": "نتوء جبلي", "en": "ridge"},
    "Q7777019": {"ar": "مرج", "en": "meadow"},
    "Q79007": {"ar": "شارع", "en": "street"},
    "Q8072": {"ar": "بركان", "en": "volcano"},
    "Q81235": {"ar": "آلة صراف آلي", "en": "automated teller machine"},
    "Q82794": {"ar": "منطقة", "en": "geographic region"},
    "Q83471": {"ar": "سخان", "en": "geyser"},
    "Q8502": {"ar": "جبل", "en": "mountain"},
    "Q878077": {"ar": "غطاء جليدي", "en": "ice cap"},
    "Q879641": {"ar": "أراضي أشجار قمئية", "en": "shrubland"},
    "Q93352": {"ar": "ساحل", "en": "coast"},
    "Q9430": {"ar": "محيط", "en": "ocean"},
    "Q963729": {"ar": "أخدود غائص", "en": "submarine canyon"},
    "Q569500": {"ar": "مركز صحي", "en": ""},
    "Q39614": {"ar": "مقبرة", "en": "cemetery"},
}
# ---
placesTable["Q8054"] = {"ar": "بروتين"}
# ---
placesTable["Q207524"] = {"ar": "جزيرة صغيرة", "en": "islet"}
placesTable["Q22698"] = {"ar": "متنزه", "en": "park"}
# placesTable["Q34795826"] = { "ar" : "" , "en" : "moor" }
placesTable["Q211748"] = {"ar": "حقل نفط", "en": "oilfield"}

placesTable["Q1248784"] = {"ar": "مطار", "en": "airport"}
# placesTable["Q591942"] = { "ar" : "فرع" , "en" : "distributary" }
placesTable["Q105190"] = {"ar": "سد مائي", "en": "levee"}
placesTable["Q532"] = {"ar": "قرية", "en": "village"}
placesTable["Q820477"] = {"ar": "منجم", "en": "mine"}

placesTable["Q46831"] = {"ar": "سلسلة جبلية", "en": "mountains"}
placesTable["Q150784"] = {"ar": "أخدود", "en": "canyon"}
placesTable["Q27590"] = {"ar": "براح", "en": "heath"}
placesTable["Q37901"] = {"ar": "مضيق", "en": "strait"}
placesTable["Q107679"] = {"ar": "جرف", "en": "cliff"}
placesTable["Q170321"] = {"ar": "منطقة رطبة", "en": "wetland"}
placesTable["Q75520"] = {"ar": "هضبة", "en": "plateau"}
placesTable["Q2935978"] = {"ar": "قناة ري", "en": "irrigation canal"}
placesTable["Q190429"] = {"ar": "منخفض", "en": "depression"}
placesTable["Q44782"] = {"ar": "ميناء", "en": "port"}
# placesTable[""] = { "ar" : "" , "en" : "" }
# placesTable[""] = { "ar" : "" , "en" : "" }
# placesTable[""] = { "ar" : "" , "en" : "" }
# placesTable[""] = { "ar" : "" , "en" : "" }
placesTable["Q34379419"] = {"ar": "منطقة رملية", "en": "sand area"}
# ---


# ---

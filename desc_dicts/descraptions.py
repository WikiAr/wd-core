#!/usr/bin/python3
r"""

likeapi.descraptions

"([\w\s]+)"(\s*\:\s*{\s*"ar"\s*\:\s*"[\w\s]+")\s*\}\s*\,\s*\#(Q\d+)
"$3"$2, "en":"$1"},

new pages from file

python3 core8/pwb.py API/descraptions
python3 core8/pwb.py update/update


SELECT ?P31 (count(*) as ?d)
WHERE {
  VALUES ?P31 { wd:Q10870555 wd:Q1457376 wd:Q39614 wd:Q19389637 wd:Q15917122 wd:Q4502142
                              wd:Q1332364
                              wd:Q204194
                              wd:Q130019
                              wd:Q523
                              wd:Q6243
                              wd:Q6979593
                              wd:Q6979593
                              wd:Q24856
                              wd:Q4167836
                              wd:Q11173
                              wd:Q101352
                              wd:Q11879590
                              wd:Q3409032
                              wd:Q21199
                              wd:Q12308941
                              wd:Q13442814
                              wd:Q13100073
                              wd:Q4167836
              }
  ?item wdt:P31 ?P31. }
group by ?P31

"""

# ---
# from desc_dicts.descraptions import DescraptionsTable, Qid_Descraptions, Space_Descraptions, Taxon_Descraptions
from desc_dicts.scientific_article_desc import Scientific_descraptions
from desc_dicts.descraptions_dict import many_lang_qid_desc

# ---
DescraptionsTable = {
    "scientific article": Scientific_descraptions,
    "scholarly article": Scientific_descraptions,
}
# ---
Qid_Desc = {
    # "Q29654788" :  {"ar":"محرف الترميز الموحد","en":"Unicode character"},# 129373
    # "Q93184" :     {"ar":"رسم",                "en":"drawing"},# 92480
    # "Q2319498": {"ar": "معالم", "en": "landmark"},  # 13445
    # "Q47461344" :   {"ar":"عمل مكتوب",          "en":"written work"},# 16142
    "Q13424466": {"ar": "ميناء طبيعي", "en": "natural harbor"},
    "Q13433827": {"ar": "مقالة موسوعية", "en": "encyclopedia article"},  # 209000
    "Q18918145": {"ar": "مقالة أكاديمية", "en": "academic journal article"},  # 8407
    "Q2668072": {"ar": "مجموعة", "en": "collection"},  # 155928
    "Q23038290": {"ar": "أصنوفة أحفورية", "en": "fossil taxon"},  # 110830
    "Q1580166": {"ar": "مدخلة قاموس", "en": "dictionary entry"},  # 57490
    "Q11060274": {"ar": "طباعة فنية", "en": "print"},  # 40547
    "Q220659": {"ar": "قطع أثرية", "en": "archaeological artifact"},  # 29283
    # "Q860861": {"ar": "منحوتة", "en": "sculpture"},  # 22091
    "Q1539532": {"ar": "موسم نادي رياضي", "en": "sports season of a sports club"},  # 20501
    "Q30612": {"ar": "تجربة سريرية", "en": "clinical trial"},  # 339121
    "Q152450": {"ar": "انتخابات محلية", "en": "municipal election"},  # 14289
    "Q15632617": {"ar": "إنسان خيالي", "en": "fictional human"},  # 13940
    "Q838948": {"ar": "عمل فني", "en": "work of art"},  # 12626
    "Q2065736": {"ar": "ممتلكات ثقافية", "en": "cultural property"},  # 11435
    "Q2795484": {"ar": "تشريع تنفيذي", "en": "implementing regulation"},  # 10161
    "Q1298239": {"ar": "مرسوم تنفيذي", "en": "decree"},  # 9482
    "Q9052846": {"ar": "مرسوم تنفيذي", "en": "decree"},  # 7949
    "Q2020153": {"ar": "مؤتمر علمي", "en": "academic conference"},  # 8925
    "Q667276": {"ar": "معرض فني", "en": "art exhibition"},  # 8483
    "Q3917681": {"ar": "سفارة", "en": "embassy"},  # 8363
    "Q3658341": {"ar": "شخصية أدبية", "en": "literary character"},  # 8320
    "Q2085381": {"ar": "دار نشر", "en": "publisher"},  # 8318
    "Q654772": {"ar": "نزل الشباب", "en": "hostel"},  # 8076
    "Q852190": {"ar": "حطام سفينة", "en": "shipwreck"},  # 8022
    "Q420927": {"ar": "مركب بروتيني", "en": "protein complex"},  # 7621
    "Q29642950": {"ar": "مكتبة برمجية بايثون", "en": "Python library"},  # 7437
    "Q1980247": {"ar": "باب كتاب", "en": "chapter"},  # 7003
    "Q189118": {"ar": "نوع خلية", "en": "cell type"},  # 6946
    "Q40231": {"ar": "انتخابات", "en": "election"},  # 6680
    "Q2188189": {"ar": "عمل موسيقي", "en": "musical work"},  # 6391
    # "Q953806": {"ar": "محطة حافلات", "en": "bus stop"},  # 6231
    "Q105774620": {"ar": "قانون برلمان المملكة المتحدة", "en": "Public General Act of the Parliament of the United Kingdom"},
    "Q7604693": {"ar": "القواعد القانونية لأيرلندا الشمالية", "en": "Statutory Rules of Northern Ireland"},  # 13624
    "Q427087": {"ar": "حمض نووي ريبوزي غير مشفر", "en": "non-coding RNA"},  # 698
    "Q18340514": {"ar": "مقالة عن أحداث في سنة أو فترة زمنية محددة", "en": "events in a specific year or time period"},
    "Q7604686": {"ar": "صك قانوني في المملكة المتحدة", "en": "UK Statutory Instrument"},
    "Q820655": {"ar": "قانون تشريعي", "en": "statute"},  # python3 core8/pwb.py np/nldes3 sparql:Q820655
    "Q207694": {"ar": "متحف فني", "en": "art museum"},
    "Q27032363": {"ar": "أرشيف صور", "en": "photo archive"},
    "Q7187": {"ar": "جين", "en": "gene"},
    "Q8054": {"ar": "بروتين", "en": "protein"},
    "Q19389637": {"ar": "مقالة سيرة ذاتية", "en": "biographical article"},
    "Q21014462": {"ar": "خط خلية", "en": "cell line"},
    "Q49008": {"ar": "عدد أولي", "en": "prime number"},
    "Q7889": {"ar": "لعبة فيديو", "en": "video game"},
    "Q10870555": {"ar": "تقرير", "en": "report"},
    "Q4502142": {"ar": "عمل فني مرئي", "en": "visual artwork"},
}
# ---
Qid_Descraptions = {}  # مستخدم في عدة بوتات
# ---
for qid, labs in Qid_Desc.items():
    Qid_Descraptions[qid] = {"ar": labs["ar"]}
    DescraptionsTable[labs["en"]] = {"ar": labs["ar"]}
# ---
# many_lang_qid_desc = {}
# ---
many_lang_qid_desc["Q13442814"] = Scientific_descraptions  # scientific article
# ---
# merge 2 dictionaries
# ---
for q2, labse in many_lang_qid_desc.items():
    Qid_Descraptions[q2] = labse
    # if labse.get("uk", '') != '':
    # en = labse.get("en", '')
    # uk = labse.get("uk", '')
    # pkrint(f'*{en}\t{uk}')
    if labse.get("en", "") != "":
        DescraptionsTable[labse["en"]] = labse
# ---
# 'Q7278',   #حزب سياسي
Space_Desc = {
    "Q44559": {"ar": "كوكب خارج المجموعة الشمسية", "en": "extrasolar planet"},
    "Q13890": {"ar": "نجم مزدوج", "en": "double star"},
    "Q83373": {"ar": "نجم زائف", "en": "quasar"},
    "Q46587": {"ar": "نواة مجرة نشطة", "en": "active galactic nucleus"},
    "Q6999": {"ar": "جرم فلكي", "en": "astronomical object"},
    "Q13632": {"ar": "سديم كوكبي", "en": "planetary nebula"},
    "Q1931185": {"ar": "مصدر راديو فلكي", "en": "astronomical radio source"},
    "Q71963409": {"ar": "تجمع مجري مدمج", "en": "compact group of galaxies"},
    "Q67206691": {"ar": "مصدر أشعة تحت حمراء", "en": "infrared source"},
    "Q3863": {"ar": "كويكب", "en": "asteroid"},
    "Q1153690": {"ar": "نجم متغير طويل", "en": "long period variable"},
    "Q168845": {"ar": "عنقود نجمي", "en": "star cluster"},
    "Q1457376": {"ar": "كسوف نجم ثنائي", "en": "eclipsing binary star"},  # 288516 pages
    "Q15917122": {"ar": "نجم متغير دوار", "en": "rotating variable star"},
    "Q1332364": {"ar": "متغير بيضاوي دوار", "en": "rotating ellipsoidal variable"},
    "Q204194": {"ar": "سديم مظلم", "en": "dark nebula"},
    "Q130019": {"ar": "نجم كربوني", "en": "carbon star"},
    "Q523": {"ar": "نجم", "en": "star", "nl": "ster", "sl": "zvezda"},
    "Q6243": {"ar": "نجم متغير", "en": "variable star"},
    "Q115518": {"ar": "مجرة ذات سطوع سطحي منخفض", "en": "low-surface-brightness galaxy"},
    "Q318": {
        "ar": "مجرة",
        "nl": "sterrenstelsel",
        "be": "галактыка",
        "be-tarask": "галяктыка",
        "en": "galaxy",
        "sl": "galaksija",
        "id": "galaksi",
        "ne": "आकासगङ्गा",
        # "de": "Galaxie im Sternbild Jagdhunde",
        "es": "galaxia",
        # "it": "galassia nella costellazione dei Cani da Caccia",
        "fr": "galaxie",
        "ru": "галактика",
        "pt": "galáxia",
        "eo": "galaksio",
        "gl": "galaxia",
        "ca": "galàxia",
        "ast": "galaxa",
        "ga": "réaltra",
        "hr": "galaktika",
    },
}
# ---
Space_Descraptions = {}
# ---
for k, val in Space_Desc.items():
    if len(val.keys()) > 2:
        Space_Descraptions[k] = val
    else:
        Space_Descraptions[k] = {"ar": val["ar"]}
# ---
# enlab:primary school, q:Q9842
# enlab:taxon, q:Q16521
# ---
# Space_Descraptions["Q726242"] = { "ar":"نجم","en":"RR Lyrae variable" }
# Space_Descraptions["Q2247863"] = { "ar":"نجم", "en":"high proper-motion star" }
# Space_Descraptions["Q66619666"] = { "ar":"نجم","en":"Red Giant Branch star" }
# Space_Descraptions["Q72803622"] = { "ar":"نجم","en":"emission-line star" }
# ---
for xd in Space_Descraptions:
    DescraptionsTable[xd] = Space_Descraptions[xd]
# ---
Taxon_Descraptions = {
    "species of insect": {
        "ar": "نوع من الحشرات",
        "an": "especie d'insecto",
        "bg": "вид насекомо",
        "bn": "কীটপতঙ্গের প্রজাতি",
        "ca": "espècie d'insecte",
        "en": "species of insect",
        "fr": "espèce d'insectes",
        "it": "specie di insetti",
        "es": "especie de insecto",
        "gl": "especie de insecto",
        "hy": "միջատների տեսակ",
        "id": "spesies serangga",
        "nb": "insektart",
        "nn": "insektart",
        "pt": "espécie de inseto",
        "pt-br": "espécie de inseto",
        "ro": "specie de insecte",
        "ru": "вид насекомых",
        "sq": "specie e insekteve",
        "ta": "பூச்சி இனம்",
    },
    "species of beetle": {
        "ar": "نوع من الحشرات",
        "en": "species of beetle",
        "fr": "espèce de coléoptères",
        "it": "specie di coleotteri",
    },
    "genus of algae": {
        "ar": "جنس من الطحالب",
        "bn": "শৈবালের গণ",
        "en": "genus of algae",
        "es": "género de algas",
        "gl": "xénero de algas",
        "he": "סוג של אצה",
        "id": "genus alga",
        "nb": "algeslekt",
        "nn": "algeslekt",
        "ro": "gen de alge",
        "sq": "gjini e algave",
    },
    "genus of amphibians": {
        "ar": "جنس من البرمائيات",
        "bn": "উভচর প্রাণীর গণ",
        "en": "genus of amphibians",
        "es": "género de anfibios",
        "fr": "genre d'amphibiens",
        "he": "סוג של דו־חיים",
        "id": "genus amfibi",
        "it": "genere di anfibi",
        "nb": "amfibieslekt",
        "nn": "amfibieslekt",
        "ro": "gen de amfibieni",
        "ru": "род амфибий",
        "sq": "gjini e amfibeve",
    },
    "genus of arachnids": {
        "ar": "جنس من العنكبوتيات",
        "bn": "আর‍্যাকনিডের গণ",
        "ca": "gènere d'aràcnids",
        "en": "genus of arachnids",
        "es": "género de arañas",
        "fr": "genre d'araignées",
        "he": "סוג של עכביש",
        "id": "genus arachnida",
        "it": "genere di ragni",
        "nb": "edderkoppslekt",
        "nn": "edderkoppslekt",
        "ro": "gen de arahnide",
    },
    "genus of birds": {
        "ar": "جنس من الطيور",
        "bn": "পাখির গণ",
        "ca": "gènere d'ocells",
        "en": "genus of birds",
        "es": "género de aves",
        "fr": "genre d'oiseaux",
        "gl": "xénero de aves",
        "he": "סוג של ציפור",
        "id": "genus burung",
        "it": "genere di uccelli",
        "ro": "gen de păsări",
        "sq": "gjini e zogjve",
    },
    "genus of fishes": {
        "ar": "جنس من الأسماك",
        "bn": "মাছের গণ",
        "en": "genus of fishes",
        "es": "género de peces",
        "fr": "genre de poissons",
        "he": "סוג של דג",
        "id": "genus ikan",
        "it": "genere di pesci",
        "nb": "fiskeslekt",
        "nn": "fiskeslekt",
        "pt": "género de peixes",
        "pt-br": "gênero de peixes",
        "ro": "gen de pești",
        "sq": "gjini e peshqëve",
    },
    "genus of fungi": {
        "ar": "جنس من الفطريات",
        "bn": "চত্রাকের গণ",
        "en": "genus of fungi",
        "es": "género de hongos",
        "fr": "genre de champignons",
        "gl": "xénero de fungos",
        "he": "סוג של פטריה",
        "id": "genus fungi",
        "it": "genere di funghi",
        "nb": "soppslekt",
        "nn": "soppslekt",
        "pt": "género de fungos",
        "pt-br": "gênero de fungos",
        # "ro":"gen de fungi",# or 'gen de ciuperci'
        "sq": "gjini e kërpudhave",
    },
    "genus of insects": {
        "ar": "جنس من الحشرات",
        "bn": "কীটপতঙ্গের গণ",
        "ca": "gènere d'insectes",
        "en": "genus of insects",
        "es": "género de insectos",
        "fr": "genre d'insectes",
        "he": "סוג של חרק",
        "id": "genus serangga",
        "it": "genere di insetti",
        "nb": "insektslekt",
        "nn": "insektslekt",
        "pt": "género de insetos",
        "pt-br": "gênero de insetos",
        "ro": "gen de insecte",
        "ru": "род насекомых",
        "sq": "gjini e insekteve",
    },
    "genus of mammals": {
        "ar": "جنس من الثدييات",
        "bn": "স্তন্যপায়ীর গণ",
        "ca": "gènere de mamífers",
        "en": "genus of mammals",
        "es": "género de mamíferos",
        "fr": "genre de mammifères",
        "gl": "xénero de mamíferos",
        "he": "סוג של יונק",
        "id": "genus mamalia",
        "nb": "pattedyrslekt",
        "nn": "pattedyrslekt",
        "ro": "gen de mamifere",
        "sq": "gjini e gjitarëve",
    },
    "genus of molluscs": {
        "ar": "جنس من الرخويات",
        "bn": "মলাস্কার গণ",
        "ca": "gènere de mol·luscs",
        "en": "genus of molluscs",
        "es": "género de moluscos",
        "fr": "genre de mollusques",
        "gl": "xénero de moluscos",
        "he": "סוג של רכיכה",
        "id": "genus moluska",
        "it": "genere di molluschi",
        "nb": "bløtdyrslekt",
        "nn": "blautdyrslekt",
        "ro": "gen de moluște",
        "sq": "gjini e molusqeve",
    },
    "genus of plants": {
        "ar": "جنس من النباتات",
        "ca": "gènere de plantes",
        "bn": "উদ্ভিদের গণ",
        "en": "genus of plants",
        "es": "género de plantas",
        "fr": "genre de plantes",
        "gl": "xénero de plantas",
        "he": "סוג של צמח",
        "id": "genus tumbuh-tumbuhan",
        "nb": "planteslekt",
        "nn": "planteslekt",
        "pt": "género de plantas",
        "pt-br": "gênero de plantas",
        "ro": "gen de plante",
        "sq": "gjini e bimëve",
    },
    "genus of reptiles": {
        "ar": "جنس من الزواحف",
        "bn": "সরীসৃপের গণ",
        "ca": "gènere de rèptils",
        "en": "genus of reptiles",
        "es": "género de reptiles",
        "fr": "genre de reptiles",
        "he": "סוג של זוחל",
        "id": "genus reptilia",
        "nb": "krypdyrslekt",
        "nn": "krypdyrslekt",
        "ro": "gen de reptile",
        "sq": "e zvarranikëve",
    },
}
# ---
replace_desc = {
    "hr": {
        "kategorija na Wikimediji": "kategorija u wikimediju",
        "popis na Wikimediji": "popis u wikimediju",
        "predložak Wikimedija": "predložak za wikimedije",
        "predložak na Wikimediji": "predložak za wikimedije",
        "razdvojbena stranica na Wikimediji": "razdvojbena stranica u wikimediju",
    },
    "hu": {
        "férfi keresztnév": "férfikeresztnév",
    },
    "sl": {
        "kategorija Wikimedije": "kategorija Wikimedie",
        "razločitvena stran Wikimedije": "razločitvena stran Wikimedie",
        "seznam Wikimedije": "seznam Wikimedie",
    },
}
# ---
if __name__ == "__main__":
    # python3 core8/pwb.py desc_dicts/descraptions
    u1 = ""
    u2 = ""
    for taba in DescraptionsTable.values():
        en_d = taba.get("en", "")
        sl_d = taba.get("sl", "")
        line = f"\n|-\n| {en_d} || {sl_d}"
        if "sl" in taba:
            u1 += line
        elif len(taba) > 2:
            u2 += line
    # ---
    # print(u1)
    # print(u2)
    # ---
# ---

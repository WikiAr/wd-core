#!/usr/bin/python
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
# ---
DescraptionsTable = {
    "scientific article": Scientific_descraptions,
}
# ---
Qid_Desc = {
    "Q13424466": {"ar": "ميناء طبيعي", "en": "natural harbor"},
    "Q13433827": {"ar": "مقالة موسوعية", "en": "encyclopedia article"},  # 209000
    "Q18918145": {"ar": "مقالة أكاديمية", "en": "academic journal article"},  # 8407
    "Q2668072": {"ar": "مجموعة", "en": "collection"},  # 155928
    # "Q29654788" :  {"ar":"محرف الترميز الموحد","en":"Unicode character"},# 129373
    "Q23038290": {"ar": "أصنوفة أحفورية", "en": "fossil taxon"},  # 110830
    # "Q93184" :     {"ar":"رسم",                "en":"drawing"},# 92480
    "Q1580166": {"ar": "مدخلة قاموس", "en": "dictionary entry"},  # 57490
    "Q11060274": {"ar": "طباعة فنية", "en": "print"},  # 40547
    "Q220659": {"ar": "قطع أثرية", "en": "archaeological artifact"},  # 29283
    "Q860861": {"ar": "منحوتة", "en": "sculpture"},  # 22091
    "Q1539532": {"ar": "موسم نادي رياضي", "en": "sports season of a sports club"},  # 20501
    # "Q47461344" :   {"ar":"عمل مكتوب",          "en":"written work"},# 16142
    "Q30612": {"ar": "تجربة سريرية", "en": "clinical trial"},  # 339121
    "Q152450": {"ar": "انتخابات محلية", "en": "municipal election"},  # 14289
    "Q15632617": {"ar": "إنسان خيالي", "en": "fictional human"},  # 13940
    "Q2319498": {"ar": "معالم", "en": "landmark"},  # 13445
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
    "Q953806": {"ar": "محطة حافلات", "en": "bus stop"},  # 6231
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
tiny_wrwr = {
    'Q1260524': {'ar': 'وقت من اليوم', 'en': ''},         # 68707
    'Q5633421': {'ar': 'دورية علمية', 'en': ''},          # 55353
    'Q76130167': {'ar': 'مبنى بحثي', 'en': ''},           # 27575
    'Q4830453': {'ar': 'عمل تجاري', 'en': ''},            # 22758
    'Q6881511': {'ar': 'مقاولة', 'en': ''},           # 20179
    'Q2154519': {'ar': '', 'en': ''},         # 16649
    'Q3508250': {'ar': '', 'en': ''},         # 15456
    'Q3305213': {'ar': 'لوحة فنية', 'en': ''},            # 15075
    'Q67206701': {'ar': '', 'en': ''},            # 10132
    'Q3331189': {'ar': 'طبعة', 'en': ''},         # 8717
    'Q1190417': {'ar': '', 'en': ''},         # 7953
    'Q891723': {'ar': 'شركة عمومية محدودة', 'en': ''},            # 7625
    'Q5883980': {'ar': 'ضحايا المحرقة', 'en': ''},            # 7619

    'Q7366': {'ar': 'أغنية', 'en': 'song'},           # 7374
    'Q134556': {'ar': 'أغنية منفردة', 'en': ''},          # 2783

    'Q7725634': {'ar': 'عمل أدبي', 'en': ''},         # 6726
    'Q21191270': {'ar': 'حلقة مسلسل تلفزيوني', 'en': ''},         # 6667
    'Q202444': {'ar': 'الاسم الأول', 'en': ''},           # 6504
    'Q23058136': {'ar': '', 'en': ''},            # 6069
    'Q571': {'ar': 'كتاب', 'en': ''},         # 5095
    'Q11424': {'ar': 'فيلم', 'en': ''},           # 5011
    'Q24862': {'ar': 'فيلم قصير', 'en': ''},           # 5011
    'Q27555384': {'ar': '', 'en': ''},            # 4966
    'Q20747295': {'ar': 'جين يشفر بروتين', 'en': ''},         # 4818
    'Q15261477': {'ar': 'انتخابات محلية', 'en': ''},          # 4796
    'Q55850593': {'ar': '', 'en': ''},            # 4575
    'Q18674739': {'ar': '', 'en': ''},            # 4387
    'Q88163834': {'ar': '', 'en': ''},            # 4386
    'Q721747': {'ar': 'لافتة تاريخية', 'en': ''},         # 4213
    'Q263478': {'ar': 'درجة موسيقية', 'en': ''},          # 3945
    'Q33283984': {'ar': '', 'en': ''},            # 3904
    'Q15623926': {'ar': '', 'en': ''},            # 3772
    'Q26817508': {'ar': '', 'en': ''},            # 3515
    'Q674925': {'ar': 'خلية جذعية مستحثة', 'en': ''},         # 3382
    'Q27671617': {'ar': '', 'en': ''},            # 3290
    'Q3241045': {'ar': 'تفشي مرض', 'en': ''},         # 3226
    'Q4164871': {'ar': 'منصب', 'en': ''},         # 2965
    'Q3508373': {'ar': '', 'en': ''},         # 2960
    'Q22809413': {'ar': '', 'en': ''},            # 2928
    'Q60169073': {'ar': '', 'en': ''},            # 2793
    'Q482994': {'ar': 'ألبوم', 'en': ''},         # 2771
    'Q230752': {'ar': 'أوديتوريوم', 'en': ''},            # 2713
    'Q96048686': {'ar': '', 'en': ''},            # 2640
    'Q204107': {'ar': 'مجموعات وعناقيد المجرات', 'en': ''},           # 2579
    'Q93184': {'ar': 'رسم', 'en': ''},            # 2565
    'Q272447': {'ar': 'سحابة جزيئية', 'en': ''},          # 2367
    'Q2175765': {'ar': '', 'en': ''},         # 2134
    'Q11282': {'ar': 'منطقة هيدروجين II', 'en': ''},          # 2112
    'Q125191': {'ar': 'صورة', 'en': ''},          # 2072
    'Q18611609': {'ar': '', 'en': ''},            # 2040
    'Q2309609': {'ar': '', 'en': ''},         # 2002
    'Q26703203': {'ar': '', 'en': ''},            # 1963
    'Q210272': {'ar': 'التراث الثقافي', 'en': ''},            # 1963
    'Q61610698': {'ar': '', 'en': ''},            # 1958
    'Q5003624': {'ar': 'نصب تذكاري', 'en': ''},           # 1861
    'Q15416': {'ar': 'برنامج تلفزيون', 'en': ''},         # 1856
    'Q221722': {'ar': 'مرافق منفصلة للدراجات', 'en': ''},         # 1833
    'Q575759': {'ar': 'نصب الحرب', 'en': ''},         # 1780
    'Q215380': {'ar': 'طاقم موسيقي', 'en': ''},           # 1754
    'Q618779': {'ar': 'جائزة', 'en': ''},         # 1746
    'Q726': {'ar': 'حصان', 'en': ''},         # 1690
    'Q253019': {'ar': '', 'en': ''},          # 1688
    'Q497654': {'ar': 'أجسام نجمية فتية', 'en': ''},          # 1612
    'Q71798532': {'ar': '', 'en': ''},            # 1591
    'Q5358913': {'ar': '', 'en': ''},         # 1522
    'Q1518285': {'ar': '', 'en': ''},         # 1486
    'Q47461344': {'ar': 'عمل مكتوب', 'en': ''},           # 1483
    'Q694045': {'ar': 'تشريع مفوض', 'en': ''},            # 1475
    'Q637866': {'ar': 'عرض الكتب', 'en': ''},         # 1473
    'Q1572600': {'ar': '', 'en': ''},         # 1455
    'Q95997873': {'ar': '', 'en': ''},            # 1439
    'Q735160': {'ar': '', 'en': ''},          # 1431
    'Q386724': {'ar': 'عمل', 'en': ''},           # 1376
    'Q72803426': {'ar': '', 'en': ''},            # 1348
    'Q5398426': {'ar': 'مسلسل تلفزيوني', 'en': ''},           # 1334
    'Q1148359': {'ar': 'أدب رمادي', 'en': ''},            # 1267
    'Q1363750': {'ar': 'كرسي', 'en': ''},         # 1228
    'Q27555319': {'ar': '', 'en': ''},            # 1218
    'Q744691': {'ar': 'نجوم الأعجوبة', 'en': ''},         # 1214
    'Q429785': {'ar': 'ملصق', 'en': ''},          # 1164
    'Q1151284': {'ar': 'المجرة العنقودية الالمع', 'en': ''},          # 1149
    'Q39911916': {'ar': 'إعلان', 'en': ''},           # 1134
    'Q49084': {'ar': 'قصة قصيرة', 'en': ''},          # 1132
    'Q27554370': {'ar': '', 'en': ''},            # 1112
    'Q87167': {'ar': 'مخطوط', 'en': ''},          # 1100
    'Q21481766': {'ar': '', 'en': ''},            # 1073
    'Q18663566': {'ar': '', 'en': ''},            # 1052
    'Q5707594': {'ar': 'مقالة إخبارية', 'en': ''},            # 1036
    'Q72802977': {'ar': '', 'en': ''},            # 1029
    'Q273057': {'ar': 'ديسكوغرافيا', 'en': ''},           # 1023
    'Q71965429': {'ar': '', 'en': ''},            # 985
    'Q72803170': {'ar': '', 'en': ''},            # 981
    'Q1491746': {'ar': 'تجمع مجري', 'en': ''},            # 973
    'Q11276': {'ar': 'عنقود مغلق', 'en': ''},         # 956
    'Q59191021': {'ar': '', 'en': ''},            # 935
    'Q5871': {'ar': 'قزم أبيض', 'en': ''},            # 916
    'Q60474998': {'ar': '', 'en': ''},            # 910
    'Q464980': {'ar': 'معرض', 'en': ''},          # 910
    'Q35127': {'ar': 'موقع ويب', 'en': ''},           # 909
    'Q7302866': {'ar': '', 'en': ''},         # 898
    'Q71965638': {'ar': '', 'en': ''},            # 894
    'Q4504495': {'ar': 'حفل توزيع جوائز', 'en': ''},          # 893
    'Q2557101': {'ar': 'منطقة خط أنبعاثات نووي منخفض التأين', 'en': ''},          # 879
    'Q96311006': {'ar': '', 'en': ''},            # 878
    'Q483453': {'ar': 'نافورة', 'en': ''},            # 871
    'Q207628': {'ar': 'تأليف موسيقي', 'en': ''},          # 870
    'Q24452': {'ar': '', 'en': ''},           # 851
    'Q506240': {'ar': 'فيلم تلفزيوني', 'en': ''},         # 850
    'Q22247': {'ar': 'انفجار أشعة غاما', 'en': ''},           # 848
    'Q3937': {'ar': 'مستعر أعظم', 'en': ''},          # 839
    'Q191067': {'ar': 'مقالة', 'en': ''},         # 826
    'Q188593': {'ar': 'متغير قيفاوي', 'en': ''},          # 823
    'Q695992': {'ar': '', 'en': ''},          # 821
    'Q18593264': {'ar': 'عنصر مجموعة أو معرض', 'en': ''},         # 801
    'Q20006438': {'ar': 'زمالة', 'en': ''},           # 798
    'Q1993624': {'ar': '', 'en': ''},         # 791
    'Q22808320': {'ar': '', 'en': ''},            # 782
    'Q71798788': {'ar': '', 'en': ''},            # 780
    'Q28640': {'ar': 'مهنة', 'en': ''},           # 780
    'Q1498804': {'ar': '', 'en': ''},         # 765
    'Q732577': {'ar': 'منشور', 'en': ''},         # 762
    'Q1302249': {'ar': '', 'en': ''},         # 746
    'Q175331': {'ar': 'تظاهر', 'en': ''},         # 731
    'Q13406554': {'ar': 'منافسة رياضية', 'en': ''},           # 717
    'Q11032': {'ar': 'صحيفة', 'en': ''},          # 710
    'Q188509': {'ar': 'ضاحية', 'en': ''},         # 709
    'Q783794': {'ar': 'شركة', 'en': ''},          # 708
    'Q877290': {'ar': '', 'en': ''},          # 696
    'Q585956': {'ar': '', 'en': ''},          # 694
    'Q1142192': {'ar': 'نجم متميز كيميائيا', 'en': ''},           # 691
    'Q1269627': {'ar': 'تعديل (قانون)', 'en': ''},            # 689
    'Q1054444': {'ar': 'سحب بين النجوم', 'en': ''},           # 683
    'Q67201574': {'ar': '', 'en': ''},            # 681
    'Q691269': {'ar': '', 'en': ''},          # 672
    'Q10451997': {'ar': '', 'en': ''},            # 659
    'Q41298': {'ar': 'مجلة', 'en': ''},           # 646
    'Q46135307': {'ar': 'بلد في منافسة رياضية', 'en': ''},            # 641
    'Q217012': {'ar': 'مجرة راديوية', 'en': ''},          # 639
    'Q18761202': {'ar': '', 'en': ''},            # 637
    'Q67206785': {'ar': '', 'en': ''},            # 636
    'Q1002697': {'ar': 'دورية', 'en': ''},            # 635
    'Q80793': {'ar': 'مزولة', 'en': ''},          # 633
    'Q18760306': {'ar': '', 'en': ''},            # 624
    'Q1266946': {'ar': 'أطروحة', 'en': ''},           # 600
    'Q208569': {'ar': 'ألبوم إستديو', 'en': ''},          # 597
    'Q84999152': {'ar': '', 'en': ''},            # 571
    'Q55521176': {'ar': '', 'en': ''},            # 570
    'Q89181747': {'ar': '', 'en': ''},            # 569
    'Q341': {'ar': 'برمجيات حرة', 'en': ''},          # 569
    'Q42948': {'ar': 'جدار', 'en': ''},           # 567
    'Q381885': {'ar': 'قبر', 'en': ''},           # 557
    'Q34379': {'ar': 'آلة موسيقية', 'en': ''},            # 555
    'Q101600': {'ar': 'قزم بني', 'en': ''},           # 550
    'Q277759': {'ar': 'سلسلة كتب', 'en': ''},         # 545
    'Q3661265': {'ar': '', 'en': ''},         # 540
    'Q56085099': {'ar': '', 'en': ''},            # 533
    'Q737498': {'ar': 'دورية أكاديمية', 'en': ''},            # 524
    'Q57408632': {'ar': '', 'en': ''},            # 520
    'Q16510064': {'ar': 'حدث رياضي', 'en': ''},           # 516
    'Q291177': {'ar': '', 'en': ''},          # 514
    'Q180846': {'ar': 'سوبرماركت', 'en': ''},         # 511
    'Q797765': {'ar': '', 'en': ''},          # 508
    'Q8362': {'ar': 'منمنمة', 'en': ''},          # 506
    'Q5527082': {'ar': '', 'en': ''},         # 505
}
# ---
for ps in tiny_wrwr.keys():
    if ps in Qid_Desc:
        print(ps)
# ---
Qid_Descraptions = {}  # مستخدم في عدة بوتات
# ---
for qid, labs in Qid_Desc.items():
    Qid_Descraptions[qid] = {"ar": labs['ar']}
    DescraptionsTable[labs['en']] = {"ar": labs['ar']}
# ---
many_lang_qid_desc = {
    "Q13442814": Scientific_descraptions,  # scientific article
    "Q11173": {
        "af": "chemiese verbinding",
        "an": "compuesto quimico",
        "ru": "химическое соединение",
        "ar": "مركب كيميائي",
        "ast": "compuestu químicu",
        "bn": "রাসায়নিক যৌগ",
        "ca": "compost químic",
        "cs": "chemická sloučenina",
        "da": "kemisk forbindelse",
        "de": "chemische Verbindung",

        "en": "chemical compound",
        "sl": "kemična spojina",
        "eo": "kemia kombinaĵo",
        "es": "compuesto químico",
        "eu": "konposatu kimiko",
        "fi": "kemiallinen yhdiste",
        "fr": "composé chimique",
        "gl": "composto químico",
        "he": "תרכובת",
        "hy": "քիմիական միացություն",
        "id": "senyawa kimia",
        "it": "composto chimico",
        "la": "compositum chemicum",
        "lb": "chemesch Verbindung",
        "lv": "ķīmisks savienojums",
        "nb": "kjemisk forbindelse",
        "nl": "chemische verbinding",
        "nn": "kjemisk sambinding",
        "oc": "component quimic",
        "pl": "związek chemiczny",
        "pt": "composto químico",
        "pt-br": "composto químico",
        "ro": "compus chimic",
        "sk": "chemická zlúčenina",
        "sq": "komponim kimik",
        "tg-cyrl": "пайвастагии химиявӣ",
        "tg-latn": "payvastagii khimiyaviy",
    },
    "Q6979593": {  # national association football team
        "ar": "منتخب كرة قدم وطني",
        "sl": "nacionalna nogometna reprezentanca",
        "en": "national association football team",
        "nl": "nationaal voetbalteam",
        "tg-cyrl": "ассотсиатсияи миилии бошгоҳи футбол",
        "tg-latn": "assotsiatsiyoi millie boshgohe futbol",
    },
    "Q24856": {  # film series
        "ar": "سلسلة أفلام",
        "sl": "filmska serija",
        "en": "film series",
        "tg-cyrl": "силсилаи филмҳо",
        "tg-latn": "silsilai filmho",
    },
    "Q15184295": {  # Wikimedia module
        "ar": "وحدة ويكيميديا",
        "en": "Wikimedia module",
        "fr": "Module Wikimedia",
        "sl": "modul Wikimedie",
        "nl": "Wikimedia-module",
        "he": "יחידה של ויקימדיה",
        "ilo": "Modulo ti lua",
        "vi": "mô đun Lua",
        "ko": "위키미디어 루아 모듈",
        "bg": "Уикимедия модул",
        "pl": "moduł Lua",
        "tg-cyrl": "модули Викимедиа",
        "tg-latn": "moduli Vikimediya",
    },
    "Q1013520000000000000000000000000000": {  # family name # Q1013520
        "af": "van",
        "an": "apelliu",
        "ar": "اسم العائلة",
        "ast": "apellíu",
        "az": "soyadı",
        "bar": "Schreibnam",
        "be": "прозвішча",
        "be-tarask": "прозьвішча",
        "bg": "презиме",
        "bn": "পারিবারিক নাম",
        "br": "anv-tiegezh",
        "bs": "prezime",
        "ca": "cognom",
        "crh": "soyadı",
        "cs": "příjmení",
        "csb": "nôzwëskò",
        "cv": "хушамат",
        "cy": "cyfenw",
        "da": "efternavn",
        "de": "Familienname",


        "el": "επώνυμο",
        "en": "family name",

        "en-gb": "surname",
        "eo": "familia nomo",
        "es": "apellido",
        "et": "perekonnanimi",
        "eu": "abizen",
        "fa": "نام خانوادگی",
        "fi": "sukunimi",
        "fit": "sukunimi",
        "fo": "ættarnavn",
        "fr": "nom de famille",
        "fy": "efternamme",
        "ga": "sloinne",
        "gan": "姓氏箋釋",
        "gan-hans": "姓氏笺释",
        "gan-hant": "姓氏箋釋",
        "gd": "sloinneadh",
        "gl": "apelido",
        "gsw": "Familiename",
        "gu": "અટક",
        "gv": "sliennoo",
        "he": "שם משפחה",
        "hi": "उपनाम",
        "hr": "prezime",
        "hu": "vezetéknév",
        "hy": "ազգանուն",
        "id": "nama keluarga",
        "ig": "ahà nnà",
        "io": "surnomo",
        "is": "eftirnafn",
        "it": "cognome",
        "ja": "姓",
        "jut": "efternavn",
        "jv": "jeneng pancer",
        "ka": "გვარი",
        "kk": "тек, ата-тек, әулет есім",
        "kk-cyrl": "тек, ата-тек, әулет есім",
        "kk-latn": "tek, ata-tek, äwlet esim",
        "kk-kz": "тек, ата-тек, әулет есім",
        "kk-tr": "tek, ata-tek, äwlet esim",
        "ko": "성씨",
        "ksh": "Nohnahme",
        "kw": "hanow",
        "la": "nomen gentilicium",
        "lad": "alkunya",
        "lb": "Familljennumm",
        "lt": "pavardė",
        "lv": "uzvārds",
        "lzh": "姓氏",
        "mhr": "тукымлӱм",
        "mi": "ingoa whānau",
        "min": "namo asli",
        "mk": "презиме",
        "mn": "овог нэр",
        "ms": "nama keluarga",
        "mt": "kunjom",
        "nb": "etternavn",
        "nds": "Familiennaam",
        "ne": "थर",
        "new": "उपनां",
        "nl": "achternaam",
        "nn": "etternamn",
        "oc": "nom d’ostal",
        "or": "ସାଙ୍ଗିଆ",
        "os": "мыггаг",
        "pl": "nazwisko",
        "pms": "cognòm",
        "pt": "sobrenome",
        "pt-br": "nome de familia",
        "ro": "nume de familie",
        "ru": "фамилия",
        "rue": "прузвище",
        "sco": "faimily name",
        "se": "goargu",
        "sh": "prezime",
        "sje": "maŋŋepnamma",
        "sk": "priezvisko",
        "sl": "priimek",
        "sma": "fuelhkienomme",
        "smj": "maŋepnamma",
        "sn": "Mazita eMhuri",
        "sq": "mbiemër",
        "sr": "презиме",
        "sr-ec": "презиме",
        "sr-el": "prezime",
        "sv": "efternamn",
        "sw": "jina la ukoo",
        "ta": "குடும்பப் பெயர்",
        "te": "ఇంటి పేర్లు",
        "th": "นามสกุล",
        "tl": "apelyido",
        # "tr":"soyadı",
        "tr": "soyadı",  # Topic:V9p2mhq3iro7lp6y
        "uk": "прізвище",
        "uz": "familiya",
        "vi": "họ",
        "wa": "no d’ famile",
        "war": "apelyidu",
        "xh": "ifani",
        "yi": "פֿאַמיליע נאָמען",
        "yue": "姓",
        "zh": "姓氏",
        "zh-cn": "姓氏",
        "zh-hans": "姓氏",
        "zh-hant": "姓氏",
        "zh-hk": "姓氏",
        "zh-mo": "姓氏",
        "zh-my": "姓氏",
        "zh-sg": "姓氏",
        "zh-tw": "姓氏",
        "zu": "isibongo",
        "tg-cyrl": "насаб",
        "tg-latn": "nasab",
    },
    "Q11879590": {  # female given name
        "af": "vroulike voornaam",
        "ar": "أسم مؤنث معطى",
        "ast": "nome femenín",
        "bar": "Weiwanam",
        "be": "жаночае асабістае імя",
        "bg": "женско собствено име",
        "bn": "প্রদত্ত মহিলা নাম",
        "br": "anv merc’hed",
        "bs": "žensko ime",
        "ca": "prenom femení",
        "ce": "зудчун шен цӀе",
        "cs": "ženské křestní jméno",
        "cy": "enw personol benywaidd",
        "da": "pigenavn",
        "de": "weiblicher Vorname",


        "el": "γυναικείο όνομα",
        "en": "female given name",
        "eo": "virina persona nomo",
        "es": "nombre femenino",
        "et": "naisenimi",
        "eu": "emakumezko izena",
        "fa": "نام‌های زنانه",
        "fi": "naisen etunimi",
        "fr": "prénom féminin",
        "gl": "nome feminino",
        "he": "שם פרטי של אישה",
        "hr": "žensko ime",
        "hsb": "žonjace předmjeno",
        "hu": "női keresztnév",
        "hy": "իգական անձնանուն",
        "id": "nama perempuan feminin",
        "is": "kvenmannsnafn",
        "it": "prenome femminile",
        "ja": "女性の名前",
        "ko": "여성의 이름",
        "la": "praenomen femininum",
        "lb": "weibleche Virnumm",
        "lt": "moteriškas vardas",
        "lv": "sieviešu personvārds",
        "mk": "женско лично име",
        "nb": "kvinnenavn",
        "ne": "स्त्रीलिङ्गी नाम",
        "nl": "vrouwelijke voornaam",
        "nn": "kvinnenamn",
        "pl": "imię żeńskie",
        "pt": "nome próprio feminino",
        "pt-br": "nome próprio feminino",
        "ro": "prenume feminin",
        "ru": "женское личное имя",
        "scn": "nomu di battìu fimmininu",
        "sco": "female gien name",
        "sk": "ženské krstné meno",
        "sl": "žensko osebno ime",
        "sq": "emër femëror",
        "sr": "женско лично име",
        "sr-ec": "женско лично име",
        "sr-el": "žensko lično ime",
        "sv": "kvinnonamn",
        "sw": "jina la mwanamke",
        "ta": "பெண்களுக்கு சூட்டிய பெயர்",
        "tg": "номи шахсии занона",
        "th": "ชื่อผู้หญิง",
        # "tr":"kadın ismidir",
        "tr": "kadın adı",  # Topic:V9p2mhq3iro7lp6y
        "uk": "жіноче особове ім’я",
        "yue": "女性人名",
        "zh": "女性人名",
        "zh-cn": "女性人名 ",
        "zh-hans": "女性人名",
        "zh-hant": "女性人名",
        "zh-hk": "女性人名",
        "zh-mo": "女性人名",
        "zh-my": "女性人名",
        "zh-sg": "女性人名",
        "zh-tw": "女性人名",
        "tg-cyrl": "номи занона",
        "tg-latn": "nomi zanona",
    },
    "Q3409032": {  # unisex given name
        "tr": "ön ad",  # Topic:Vavf6jigl4dwgkc4
        "ar": "اسم شخصي محايد",
        "be": "унісекс-імя",
        "bs": "muško i žensko ime",
        "ca": "prenom ambigu",
        "cs": "obourodé jméno",
        "de": "geschlechtsneutraler Vorname",


        "el": "ανδρικό ή γυναικείο όνομα",
        "en": "unisex given name",
        "eo": "seksneŭtra persona nomo",
        "es": "nombre ambiguo",
        "eu": "izen unisex",
        "fr": "prénom épicène",
        "gsw": "gschlächtsneutrale Vorname",
        "hu": "unisex név",
        "hy": "երկսեռ անձնանուն",
        "it": "prenome sia maschile che femminile",
        "ja": "男女両用の名前",
        "ko": "남녀공통 이름",
        "mk": "бесполово име",
        "nb": "kjønnsnøytralt navn",
        "ne": "स्त्री र पुरूष दुबैले प्रयोग गर्ने नाम",
        "nl": "genderneutrale voornaam",
        "pl": "imię uniseksowe",
        "pt": "nome unissex",
        "ru": "унисекс-имя",
        "scn": "nomu di battìu masculinu e fimmininu",
        "sco": "unisex name",
        "sl": "obojespolno osebno ime",
        "sr": "унисекс име",
        "sr-ec": "унисекс име",
        "sr-el": "uniseks ime",
        "sv": "könsneutralt namn",
        "uk": "унісекс ім’я",
        "vi": "tên trung tính",
        "zh": "中性人名",
    },
    "Q50823455": {
        "ar": "سنة في التقويم العبري",
        "bn": "হিব্রু পঞ্জিকার বছর",
        "ca": "any de calendari hebreu",
        "sl": "hebrejsko koledarsko leto",
        "en": "Hebrew calendar year",
        "es": "año del calendario hebreo",
        "fa": "سال در گاه‌شماری عبری",
        "fr": "année hébraïque",
        "he": "שנה עברית",
        "hy": "Հրեական օրացույցի տարեթիվ",
        "id": "tahun kalendar Ibrani",
        "nb": "hebraisk kalenderår",
        "nn": "hebraisk kalenderår",
        "ru": "год еврейского календаря",
        "sq": "vit i kalendarik hebraik",
        "tg-cyrl": "тақвими солшумории ибрӣ",
        "tg-latn": "taqvimi solshumorii hibri",
    },
    "Q4146861": {
        "ar": "سنة في التقويم الهجري",
        "bn": "ইসলামী পঞ্জিকার বছর",
        "sl": "islamsko koledarsko leto",
        "en": "Islamic calendar year",
        "es": "año del calendario musulmán",
        "he": "שנה בלוח השנה המוסלמי",
        "id": "tahun kalendar Islam",
        "nb": "islamsk kalenderår",
        "nn": "islamsk kalenderår",
        "sq": "vit i kalendarik islamik",
    },
    "Q12308941": {
        "af": "manlike voornaam",
        "ar": "أسم مذكر معطى",
        "ast": "nome masculín",
        "bar": "Mannanam",
        "be": "мужчынскае асабістае імя",
        "be-tarask": "мужчынскае асабістае імя",
        "bg": "мъжко собствено име",
        "bn": "প্রদত্ত পুরুষ নাম",
        "br": "anv paotr",
        "bs": "muško ime",
        "ca": "prenom masculí",
        "ce": "стеган шен цӀе",
        "cs": "mužské křestní jméno",
        "cy": "enw personol gwrywaidd",
        "da": "drengenavn",
        "de": "männlicher Vorname",


        "el": "ανδρικό όνομα",
        "en": "male given name",
        "eo": "vira persona nomo",
        "es": "nombre masculino",
        "et": "mehenimi",
        "eu": "gizonezko izena",
        "fa": "نام کوچک مردانه",
        "fi": "miehen etunimi",
        "fr": "prénom masculin",
        "fy": "Jongesnamme",
        "gl": "nome masculino",
        "gsw": "männlige Vorname",
        "he": "שם פרטי של גבר",
        "hr": "muško ime",
        # "hu":"férfi keresztnév",
        "hu": "férfikeresztnév",
        "hy": "արական անձնանուն",
        "id": "nama pemberian maskulin",
        "is": "mannsnafn",
        "it": "prenome maschile",
        "ja": "男性の名前",
        "ka": "მამაკაცის საკუთარი სახელი",
        "ko": "남성의 이름",
        "la": "praenomen masculinum",
        "lb": "männleche Virnumm",
        "lt": "vyriškas vardas",
        "lv": "vīriešu personvārds",
        "mk": "машко лично име",
        "nb": "mannsnavn",
        "ne": "पुलिङ्गी नाम",
        "nl": "mannelijke voornaam",
        "nn": "mannsnamn",
        "or": "ପୁରୁଷଙ୍କ ନାମ",
        "pl": "imię męskie",
        "pt": "nome próprio masculino",
        "pt-br": "nome próprio masculino",
        "ro": "prenume masculin",
        "ru": "мужское личное имя",
        "scn": "nomu di battìu masculinu",
        "sco": "male first name",
        "sk": "mužské meno",
        "sl": "moško osebno ime",
        "sq": "emër mashkullor",
        "sr": "мушко лично име",
        "sr-el": "muško lično ime",
        "sr-ec": "мушко лично име",
        "sv": "mansnamn",
        "sw": "jina la mwanaume",
        "ta": "ஆண்களுக்கு சூட்டிய பெயர்",
        "tg": "номи мардона",
        "th": "ชื่อผู้ชาย",
        # "tr":"erkek ismidir",
        "tr": "erkek adı",  # Topic:V9p2mhq3iro7lp6y
        "uk": "чоловіче особове ім’я",
        "ur": "مردانہ ذاتی نام",
        "yue": "男性人名",
        "zh": "男性人名",
        "zh-cn": "男性人名",
        "zh-hans": "男性名",
        "zh-hant": "男性人名",
        "zh-hk": "男性人名",
        "zh-mo": "男性人名",
        "zh-my": "男性人名",
        "zh-sg": "男性人名",
        "zh-tw": "男性人名",
        "tg-cyrl": "номи мардона",
        "tg-latn": "nomi mardona",
    },
    "Q21199": {  # natural number
        "af": "natuurlike getal",
        "als": "natürlige Zahle",
        "sl": "naravno število",
        "an": "numero natural",
        "ar": "عدد طبيعي",
        "bn": "প্রাকৃতিক সংখ্যা",
        "ca": "nombre natural",
        "en": "natural number",
        "eo": "natura nombro",
        "es": "número natural",
        "he": "מספר טבעי",
        "hi": "प्राकृतिक संख्या",
        "hy": "Բնական թիվ",
        "ia": "numero natural",
        "id": "bilangan asli",  # angka alami[[Topic:Vrehx2184pi27t0o]]
        "ka": "ნატურალური რიცხვი",
        "kn": "ಸ್ವಾಭಾವಿಕ ಸಂಖ್ಯೆ",
        "it": "numero naturale",
        "la": "numerus naturalis",
        "mwl": "númaro natural",
        "nb": "naturlig tall",
        "nn": "naturleg tal",
        "pms": "nùmer natural",
        "pt": "número natural",
        "ro": "număr natural",
        "scn": "nùmmuru naturali",
        "sco": "naitural nummer",
        "sc": "nùmeru naturale",
        "szl": "naturalno nůmera",
        "ru": "натуральное число",
        "sq": "numër natyror",
        "uk": "натуральне число",
        "tg-cyrl": "рақами натуралӣ",
        "tg-latn": "raqami naturaliy",
    },
    "Q13100073": {
        "an": "pueblo d'a Republica Popular de China",  # o 'pueblo de China'
        "ar": "قرية في الصين",
        "bn": "চীনের একটি গ্রাম",
        "ca": "poble de la Xina",
        "de": "Dorf in China",
        "el": "οικισμός της Λαϊκής Δημοκρατίας της Κίνας",
        "en": "village in China",
        "sl": "vas na Kitajskem",
        "eo": "vilaĝo en Ĉinujo",
        "es": "aldea de la República Popular China",
        "fi": "kylä Kiinassa",
        "fr": "village chinois",
        "he": "כפר ברפובליקה העממית של סין",
        "hy": "գյուղ Չինաստանում",
        "id": "desa di Tiongkok",
        "it": "villaggio cinese",
        "nb": "landsby i Kina",
        "nn": "landsby i Kina",
        "nl": "dorp in China",
        "oc": "vilatge chinés",
        "pt-br": "vila chinesa",
        "ro": "sat din China",
        "ru": "деревня КНР",
        "sq": "fshat në Kinë",
        "tg-cyrl": "русто дар Чин",
        "tg-latn": "rusto dar Xitoy",
    },
    "Q4167836": {  # Wikimedia category
        "ace": "kawan Wikimèdia",
        "af": "Wikimedia-kategorie",
        "an": "categoría de Wikimedia",
        "ar": "تصنيف ويكيميديا",
        # "arz":"ويكيبيديا:تصنيف",
        "ast": "categoría de Wikimedia",
        "ba": "Викимедиа категорияһы",
        "bar": "Wikimedia-Kategorie",
        "be": "катэгорыя ў праекце Вікімедыя",
        "be-tarask": "катэгорыя ў праекце Вікімэдыя",
        "bg": "категория на Уикимедия",
        "bho": "विकिपीडिया:श्रेणी",
        "bjn": "tumbung Wikimedia",
        "bn": "উইকিমিডিয়া বিষয়শ্রেণী",
        "br": "pajenn rummata eus Wikimedia",
        "bs": "kategorija na Wikimediji",
        "bug": "kategori Wikimedia",
        "ca": "categoria de Wikimedia",
        # "ce":"Викимедиа проектан категореш",
        # "ceb":"Wikimedia:Kategorisasyon",
        "ckb": "پۆلی ویکیمیدیا",
        "cs": "kategorie na projektech Wikimedia",
        "cy": "tudalen categori Wikimedia",
        "da": "Wikimedia-kategori",
        "de-at": "Wikimedia-Kategorie",
        "de-ch": "Wikimedia-Kategorie",
        "de": "Wikimedia-Kategorie",
        "el": "κατηγορία εγχειρημάτων Wikimedia",
        "en": "Wikimedia category",
        "eo": "kategorio en Vikimedio",
        "es": "categoría de Wikimedia",
        "et": "Wikimedia kategooria",
        "eu": "Wikimediako kategoria",
        "fa": "ردهٔ ویکی‌پدیا",
        "fi": "Wikimedia-luokka",
        "fr": "page de catégorie de Wikimedia",
        "fy": "Wikimedia-kategory",
        "gl": "categoría de Wikimedia",
        "gsw": "Wikimedia-Kategorie",
        "gu": "વિકિપીડિયા શ્રેણી",
        "he": "קטגוריה במיזמי ויקימדיה",
        "hi": "विकिमीडिया श्रेणी",
        "hr": "kategorija na Wikimediji",
        "hu": "Wikimédia-kategória",
        "hy": "Վիքիմեդիայի նախագծի կատեգորիա",
        "id": "kategori Wikimedia",
        "ilo": "kategoria ti Wikimedia",
        "it": "categoria di un progetto Wikimedia",
        "ja": "ウィキメディアのカテゴリ",
        "ko": "위키미디어 분류",
        "ky": "Wikimedia категориясы",
        "lb": "Wikimedia-Kategorie",
        "li": "Wikimedia-categorie",
        "lv": "Wikimedia projekta kategorija",
        "mk": "Викимедиина категорија",
        "nap": "categurìa 'e nu pruggette Wikimedia",
        "nb": "Wikimedia-kategori",
        "nds": "Wikimedia-Kategorie",
        "nl": "Wikimedia-categorie",
        "nn": "Wikimedia-kategori",
        "pl": "kategoria w projekcie Wikimedia",
        "pt": "categoria de um projeto da Wikimedia",
        "pt-br": "categoria de um projeto da Wikimedia",
        "ro": "categorie a unui proiect Wikimedia",
        "ru": "категория в проекте Викимедиа",
        "sco": "Wikimedia category",
        "se": "Wikimedia-kategoriija",
        "sk": "kategória projektov Wikimedia",
        "sl": "kategorija Wikimedie",  # kategorija Wikimedije  [[wd:Topic:Xjpu4y312bxi699q]]
        "sq": "kategori e Wikimedias",
        "sr": "категорија на Викимедији",
        "sv": "Wikimedia-kategori",
        "tg": "гурӯҳи Викимедиа",
        "tg-cyrl": "гурӯҳи Викимедиа",
        "tg-latn": "guruhi Vikimedia",
        "tr": "Vikimedya kategorisi",
        "uk": "категорія проєкту Вікімедіа",  # категорія в проекті Вікімедіа [[Topic:Xdnbrl1aqt1lou5u]]
        "sw": "jamii ya Wikimedia",
        "yi": "וויקימעדיע קאַטעגאָריע",
        "vi": "thể loại Wikimedia",
        "yo": "ẹ̀ka Wikimedia",
        "yue": "維基媒體分類",
        "zea": "Wikimedia-categorie",
        "zh": "维基媒体分类",
        "zh-cn": "维基媒体分类",
        "zh-hans": "维基媒体分类",
        "zh-hant": "維基媒體分類",
        "zh-hk": "維基媒體分類",
        "zh-mo": "維基媒體分類",
        "zh-my": "维基媒体分类",
        "zh-sg": "维基媒体分类",
        "zh-tw": "維基媒體分類",
    },
    "Q4167410": {  # Wikimedia disambiguation page
        "ast": "páxina de dixebra de Wikimedia",
        "an": "pachina de desambigación",
        "ar": "صفحة توضيح لويكيميديا",
        "bg": "Уикимедия пояснителна страница",
        "bn": "উইকিমিডিয়ার দ্ব্যর্থতা নিরসন পাতা",
        "bs": "čvor stranica na Wikimediji",
        "ca": "pàgina de desambiguació de Wikimedia",
        "ckb": "پەڕەی ڕوونکردنەوەی ویکیمیدیا",
        "cs": "rozcestník na projektech Wikimedia",
        "da": "Wikimedia-flertydigside",
        "de": "Wikimedia-Begriffsklärungsseite",
        "de-at": "Wikimedia-Begriffsklärungsseite",
        "de-ch": "Wikimedia-Begriffsklärungsseite",
        "el": "σελίδα αποσαφήνισης",
        "en": "Wikimedia disambiguation page",
        "eo": "Vikimedia apartigilo",
        "es": "página de desambiguación de Wikimedia",
        "et": "Wikimedia täpsustuslehekülg",
        "eu": "Wikimediako argipen orri",
        # "fa":"یک صفحهٔ ابهام‌زدایی در ویکی‌پدیا",
        "fa": "یک صفحهٔ ابهام‌زدایی در ویکی‌مدیا",
        "fi": "Wikimedia-täsmennyssivu",
        "fr": "page d'homonymie de Wikimedia",
        "fy": "Wikimedia-betsjuttingsside",
        "gl": "páxina de homónimos de Wikimedia",
        "gsw": "Wikimedia-Begriffsklärigssite",
        "gu": "સ્પષ્ટતા પાનું",
        "he": "דף פירושונים",
        "hi": "बहुविकल्पी पृष्ठ",
        "hr": "razdvojbena stranica na Wikimediji",
        "hu": "Wikimédia-egyértelműsítőlap",
        "hy": "Վիքիմեդիայի նախագծի բազմիմաստության փարատման էջ",
        "id": "halaman disambiguasi Wikimedia",
        "is": "aðgreiningarsíða á Wikipediu",
        "it": "pagina di disambiguazione di un progetto Wikimedia",
        "ja": "ウィキメディアの曖昧さ回避ページ",
        "ka": "მრავალმნიშვნელოვანი",
        "ko": "위키미디어 동음이의어 문서",
        "lb": "Wikimedia-Homonymiesäit",
        "li": "Wikimedia-verdudelikingspazjena",
        "lv": "Wikimedia projekta nozīmju atdalīšanas lapa",
        "min": "laman disambiguasi",
        "mk": "појаснителна страница",
        "ms": "laman nyahkekaburan",
        "nb": "Wikimedia-pekerside",
        "nds": "Sied för en mehrdüdig Begreep op Wikimedia",
        "nl": "Wikimedia-doorverwijspagina",
        "nn": "Wikimedia-fleirtydingsside",
        "or": "ବହୁବିକଳ୍ପ ପୃଷ୍ଠା",
        "pl": "strona ujednoznaczniająca w projekcie Wikimedia",
        "pt": "página de desambiguação da Wikimedia",
        "ro": "pagină de dezambiguizare Wikimedia",
        "ru": "страница значений в проекте Викимедиа",
        "sco": "Wikimedia disambiguation page",
        "sk": "rozlišovacia stránka",
        "sl": "razločitvena stran Wikimedie",  # razločitvena stran Wikimedije [[wd:Topic:Xjpu4y312bxi699q]]
        "sq": "faqe kthjelluese e Wikimedias",
        "sr": "вишезначна одредница на Викимедији",
        "sv": "Wikimedia-förgreningssida",
        "tg": "саҳифаи маъноҳои Викимедиа",
        "tg-cyrl": "саҳифаи ибҳомзудоӣ",
        "tg-latn": "sahifai ibhomzudoi",
        "tr": "Wikimedia anlam ayrımı sayfası",
        "tt": "Мәгънәләр бите Викимедиа проектында",
        "tt-cyrl": "Мәгънәләр бите Викимедиа проектында",
        "tt-latn": "Mäğnälär bite Wikimedia proyektında",
        # "uk":"сторінка значень в проекті Вікімедіа",сторінка-список в проекті Вікімедіа
        # "uk":"сторінка-список у проекті Вікімедіа",
        # "uk":"сторінка значень у проекті Вікімедіа",
        "uk": "сторінка значень у проєкті Вікімедіа",
        "vi": "trang định hướng Wikimedia",
        "yo": "ojúewé ìṣojútùú Wikimedia",
        "yue": "維基媒體搞清楚頁",
        "zea": "Wikimedia-deurverwiespagina",
        "zh": "维基媒体消歧义页",
        "zh-cn": "维基媒体消歧义页",
        "zh-hans": "维基媒体消歧义页",
        "zh-hant": "維基媒體消歧義頁",
        "zh-hk": "維基媒體消歧義頁",
        "zh-mo": "維基媒體消歧義頁",
        "zh-my": "维基媒体消歧义页",
        "zh-sg": "维基媒体消歧义页",
        "zh-tw": "維基媒體消歧義頁",
    },
    "Q13406463": {  # Wikimedia list article
        "ace": "teunuléh dapeuta Wikimèdia",
        "af": "Wikimedia lysartikel",
        "an": "articlo de lista de Wikimedia",
        "ar": "قائمة ويكيميديا",
        "as": "ৱিকিপিডিয়া:ৰচনাশৈলীৰ হাতপুথি",
        "ast": "artículu de llista de Wikimedia",
        "ba": "Wikimedia-Listn",
        "be": "спіс артыкулаў у адным з праектаў Вікімедыя",  # [[Topic:Wk7s8mkiocfk2axa]]
        "bn": "উইকিমিডিয়ার তালিকা নিবন্ধ",
        "bs": "spisak na Wikimediji",
        "ca": "article de llista de Wikimedia",
        "cs": "seznam na projektech Wikimedia",
        "da": "Wikimedia liste",
        "de": "Wikimedia-Liste",
        "de-at": "Wikimedia-Liste",
        "de-ch": "Wikimedia-Liste",
        "el": "κατάλογος εγχειρήματος Wikimedia",
        "en": "Wikimedia list article",
        "eo": "listartikolo en Vikimedio",
        "es": "artículo de lista de Wikimedia",
        "eu": "Wikimediako zerrenda artikulua",
        "fi": "Wikimedia-luetteloartikkeli",
        "fr": "page de liste de Wikimedia",
        "fy": "Wikimedia-list",
        "gl": "artigo de listas da Wikimedia",
        "he": "רשימת ערכים",
        "hr": "popis na Wikimediji",
        "hy": "Վիքիմեդիայի նախագծի ցանկ",
        "id": "artikel daftar Wikimedia",
        "ia": "lista de un projecto de Wikimedia",
        "it": "lista di un progetto Wikimedia",
        "ja": "ウィキメディアの一覧記事",
        "ko": "위키미디어 목록 항목",
        "lb": "Wikimedia-Lëschtenartikel",
        "li": "Wikimedia-lies",
        "mk": "список на статии на Викимедија",
        "ms": "rencana senarai Wikimedia",
        "nb": "Wikimedia-listeartikkel",
        "nl": "Wikimedia-lijst",
        "nn": "Wikimedia-listeartikkel",
        "oc": "lista d'un projècte Wikimèdia",
        "pl": "lista w projekcie Wikimedia",
        "ro": "articol-listă în cadrul unui proiect Wikimedia",
        "ru": "статья-список в проекте Викимедиа",
        "sco": "Wikimedia leet airticle",
        "si": "විකිමීඩියා ලැයිස්තු ලිපිය",
        "sk": "zoznamový článok projektov Wikimedia",
        "sl": "seznam Wikimedie",  # seznam Wikimedije [[wd:Topic:Xjpu4y312bxi699q]]
        "sq": "artikull-listë e Wikimedias",
        "sr": "списак на Викимедији",
        "sv": "Wikimedia-listartikel",
        "ta": "விக்கிப்பீடியா:பட்டியலிடல்",
        "tg": "саҳифаи феҳристӣ",
        "tg-cyrl": "саҳифаи феҳристӣ",
        "tg-latn": "sahifai fehristiy",
        "th": "บทความรายชื่อวิกิมีเดีย",
        "tr": "Vikimedya liste maddesi",
        "uk": "стаття-список у проєкті Вікімедіа",  # сторінка-список у проекті Вікімедіа [[Topic:Xdnbrl1aqt1lou5u]]
        "vi": "bài viết danh sách Wikimedia",
        "yi": "וויקימעדיע ליסטע",
        "yo": "ojúewé àtojọ Wikimedia",
        "zea": "Wikimedia-lieste",
        "zh": "维基媒体列表条目",
        "zh-cn": "维基媒体列表条目",
        "zh-hans": "维基媒体列表条目",
        "zh-hant": "維基媒體列表條目",
        "zh-hk": "維基媒體列表條目",
        "zh-mo": "維基媒體列表條目",
        "zh-my": "维基媒体列表条目",
        "zh-sg": "维基媒体列表条目",
        "zh-tw": "維基媒體列表條目"
    },
    "Q11266439": {  # Wikimedia template#Q11753321
        "an": "plantilla de Wikimedia",
        "ar": "قالب ويكيميديا",
        "ast": "plantía de proyectu",
        "ba": "Викимедиа ҡалыбы",
        "bar": "Wikimedia-Vorlog",
        "be": "шаблон праекта Вікімедыя",
        "be-tarask": "шаблён праекту Вікімэдыя",
        "bg": "Уикимедия шаблон",
        "bn": "উইকিমিডিয়া টেমপ্লেট",
        "bs": "šablon Wikimedia",
        "ca": "plantilla de Wikimedia",
        "ce": "Викимедин проектан кеп",
        "cs": "šablona na projektech Wikimedia",
        "cy": "nodyn Wikimedia",
        "da": "Wikimedia-skabelon",
        "de": "Wikimedia-Vorlage",
        "el": "Πρότυπο εγχειρήματος Wikimedia",
        "en": "Wikimedia template",
        "sl": "predloga Wikimedie",
        "eo": "Vikimedia ŝablono",
        "es": "plantilla de Wikimedia",
        "et": "Wikimedia mall",
        "eu": "Wikimediako txantiloia",
        "fa": "الگوی ویکی‌مدیا",
        "fi": "Wikimedia-malline",
        "fo": "fyrimynd Wikimedia",
        "fr": "modèle de Wikimedia",
        "frr": "Wikimedia-föörlaag",
        "fy": "Wikimedia-berjocht",
        "gl": "modelo da Wikimedia",
        "gsw": "Wikimedia-Vorlage",
        "gu": "વિકિપીડિયા ઢાંચો",
        "he": "תבנית של ויקימדיה",
        "hu": "Wikimédia-sablon",
        "hy": "Վիքիմեդիայի նախագծի կաղապար",
        "id": "templat Wikimedia",
        "ilo": "plantilia ti Wikimedia",
        "it": "template di un progetto Wikimedia",
        "ja": "ウィキメディアのテンプレート",
        "jv": "cithakan Wikimedia",
        "ka": "ვიკიმედიის თარგი",
        "ko": "위키미디어 틀",
        "ku-latn": "şablona Wîkîmediyayê",
        "la": "formula Vicimediorum",
        "lb": "Wikimedia-Schabloun",
        "li": "Wikimedia-sjabloon",
        "lt": "Vikimedijos šablonas",
        "lv": "Wikimedia projekta veidne",
        "mk": "шаблон на Викимедија",
        "ml": "വിക്കിമീഡിയ ഫലകം",
        "mr": "विकिपीडिया:साचा",
        "ms": "Templat Wikimedia",
        "nb": "Wikimedia-mal",
        "nds": "Wikimedia-Vörlaag",
        "nds-nl": "Wikimedia-mal",
        "nl": "Wikimedia-sjabloon",
        "nn": "Wikimedia-mal",
        "oc": "modèl de Wikimèdia",
        "or": "ଉଇକିମିଡ଼ିଆ ଛାଞ୍ଚ",
        "pam": "Ulmang pang-Wikimedia",
        "pl": "szablon w projekcie Wikimedia",
        "ps": "ويکيمېډيا کينډۍ",
        "pt": "predefinição da Wikimedia",
        "pt-br": "predefinição da Wikimedia",
        "ro": "format Wikimedia",
        "ru": "шаблон проекта Викимедиа",
        "sco": "Wikimedia template",
        "se": "Wikimedia-málle",
        "sk": "šablóna projektov Wikimedia",
        "sq": "stampë e Wikimedias",
        "sr": "Викимедијин шаблон",
        "sr-ec": "Викимедијин шаблон",
        "stq": "Wikimedia-Foarloage",
        "sv": "Wikimedia-mall",
        "sw": "kigezo cha Wikimedia",
        "ta": "விக்கிமீடியா வார்ப்புரு",
        "te": "వికీమీడియా మూస",
        "tg": "шаблони лоиҳаи Викимедиа",
        "tg-cyrl": "шаблони Викимедиа",
        "tg-latn": "shabloni Vikimedia",
        "th": "หน้าแม่แบบวิกิมีเดีย",
        "tl": "Padrong pang-Wikimedia",
        "tr": "Vikimedya şablonu",
        "uk": "шаблон проєкту Вікімедіа",  # шаблон проекту Вікімедіа[[Topic:Xdnbrl1aqt1lou5u]]
        "vi": "bản mẫu Wikimedia",
        "yo": "àdàkọ Wikimedia",
        "yue": "維基媒體模",
        "zea": "Wikimedia-sjabloon",
        "zh": "维基媒体模板",
        "zh-cn": "维基媒体模板",
        "zh-hans": "维基媒体模板",
        "zh-hant": "維基媒體模板",
        "zh-hk": "維基媒體模板",
        "zh-tw": "維基媒體模板",
    },
    "Q17633526": {
        "an": "articlo de Wikinews",
        "ar": "مقالة ويكي أخبار",
        "bar": "Artike bei Wikinews",
        "bn": "উইকিসংবাদের নিবন্ধ",
        "bs": "Wikinews članak",
        "ca": "article de Viquinotícies",
        "cs": "článek na Wikizprávách",
        "da": "Wikinews-artikel",
        "de": "Artikel bei Wikinews",
        "el": "Άρθρο των Βικινέων",
        "sl": "članek Wikinovic",
        "en": "Wikinews article",
        "eo": "artikolo de Vikinovaĵoj",
        "es": "artículo de Wikinoticias",
        "eu": "Wikialbisteakeko artikulua",
        "fi": "Wikiuutisten artikkeli",
        "fr": "article de Wikinews",
        "fy": "Wikinews-artikel",
        "he": "כתבה בוויקיחדשות",
        "hu": "Wikihírek-cikk",
        "hy": "Վիքիլուրերի հոդված",
        "id": "artikel Wikinews",
        "it": "articolo di Wikinotizie",
        "ja": "ウィキニュースの記事",
        "ko": "위키뉴스 기사",
        "ku-latn": "gotara li ser Wîkînûçeyê",
        "li": "Wikinews-artikel",
        "lt": "Vikinaujienų straipsnis",
        "mk": "напис на Викивести",
        "nb": "Wikinytt-artikkel",
        "nl": "Wikinieuws-artikel",
        "nn": "Wikinytt-artikkel",
        "or": "ଉଇକି ସୂଚନା ପତ୍ରିକା",
        "pl": "artykuł w Wikinews",
        "ps": "د ويکيخبرونو ليکنه",
        "pt": "artigo do Wikinotícias",
        "ro": "articol în Wikiștiri",
        "ru": "статья Викиновостей",
        "sq": "artikull i Wikinews",
        "sr": "чланак са Викивести",
        "sv": "Wikinews-artikel",
        "te": "వికీవార్త వ్యాసం",
        "tg": "саҳифаи Викиахбор",
        "tg-cyrl": "мақолаи Викиахбор",
        "tg-latn": "maqolai Vikimedia",
        "th": "เนื้อหาวิกิข่าว",
        "tr": "Vikihaber maddesi",
        "uk": "стаття Вікіновин",
        "zea": "Wikinews-artikel",
        "zh": "維基新聞新聞稿",
        "zh-cn": "维基新闻新闻稿",
        "zh-hans": "维基新闻新闻稿",
        "zh-hant": "維基新聞新聞稿",
        "zh-hk": "維基新聞新聞稿",
        "zh-mo": "維基新聞新聞稿",
        "zh-my": "维基新闻新闻稿",
        "zh-sg": "维基新闻新闻稿",
        "zh-tw": "維基新聞新聞稿",
    },
    "Q577": {
        "af": "jaar",
        "an": "anyo",
        "ar": "سنة",
        "ast": "añu",
        "be": "год",
        "be-tarask": "год",
        "bg": "година",
        "bn": "বছর",
        "br": "bloavezh",
        "bs": "godina",
        "ca": "any",
        "cs": "rok",
        "da": "år",
        "de": "Jahr",
        "el": "έτος",
        "en": "year",
        "eo": "jaro",
        "es": "año",
        "fi": "vuosi",
        "fr": "année",
        "fy": "jier",
        "gl": "ano",
        "gsw": "joor",
        "he": "שנה",
        "hr": "Godina",
        "ht": "Lane",
        "hu": "Év",
        "hy": "տարեթիվ",
        "ia": "anno",
        "id": "tahun",
        "ilo": "tawen",
        "is": "ár",
        "it": "anno",
        "ja": "年",
        "ka": "წელი",
        "ko": "연도",
        "ku": "Sal",
        "la": "annus",
        "lt": "Metai",
        "lv": "gads",
        "mhr": "Идалык",
        "min": "taun",
        "mk": "година",
        "ms": "Tahun",
        "nan": "nî",
        "nb": "år",
        "nds": "Johr",
        "nl": "jaar",
        "nn": "år",
        "or": "ବର୍ଷ",
        "pl": "rok",
        "pt": "ano",
        "ro": "an",
        "ru": "год",
        "sh": "godina",
        "sk": "Rok",
        "sl": "Leto",
        # "sq":"vit", or viti?
        "sr": "Година",
        "srn": "Yari",
        "sv": "år",
        "th": "ปี",
        "tl": "taon",
        "tr": "yıl",
        "uk": "рік",
        "vi": "năm",
        "war": "Tuig",
        "yi": "יאר",
        "yue": "年",
        "zh": "年",
        "zh-hans": "年份",
        "zh-hant": "年份",
        "tg-cyrl": "сол",
        "tg-latn": "sol",
    },
}
# ---
# merge 2 dictionaries
# ---
for q2, labse in many_lang_qid_desc.items():
    Qid_Descraptions[q2] = labse
    # if labse.get("uk", '') != '':
    # en = labse.get("en", '')
    # uk = labse.get("uk", '')
    # pkrint(f'*{en}\t{uk}')
    if labse.get("en", '') != '':
        DescraptionsTable[labse['en']] = labse
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

    "Q318": {"ar": "مجرة",
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
             "ga": "réaltra"
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
    u1 = ''
    u2 = ''
    for x, taba in DescraptionsTable.items():
        en_d = taba.get('en', '')
        sl_d = taba.get('sl', '')
        line = f'\n|-\n| {en_d} || {sl_d}'
        if "sl" in taba:
            u1 += line
        elif len(taba) > 2:
            u2 += line
    # ---
    print(u1)
    print(u2)
    # ---
# ---

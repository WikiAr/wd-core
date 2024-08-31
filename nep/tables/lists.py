"""
This module defines mappings and SPARQL queries for various entities.
It is used for [describe the purpose] in the context of [describe the context].

from nep.tables.lists import p50s, space_list_and_other, Taton_list, Space_tab, others_list_2, others_list, Geo_entity, bldiat, qura, songs_type, space_list_and_other_2, Taton_list

in si3.py :
from nep.tables.lists import space_list_and_other, others_list, Space_tab, others_list_2
'Q43305660':	{	'ar':'براءة اختراع أمريكية', 'en':'United States Patent' }, # 341036
'Q191067':		{	'ar':'مقالة', 'en':'article' }, # 271264
'Q47461344':	{	'ar':'عمل مكتوب', 'en':'written work' }, # 129452
'Q101352':		{	'ar':'اسم عائلة', 'en':'family name' }, # 126817
'Q105543609':	{	'ar':'عمل/مؤلف موسيقي', 'en':'musical work/composition' }, # 103157
'Q1907875':		{	'ar':'أطروحة الماجستير', 'en':'master's thesis' }, # 102627
'Q18593264':	{	'ar':'عنصر مجموعة أو معرض', 'en':'item of collection or exhibition' }, # 82828
'Q37038':		{	'ar':'إعلان', 'en':'advertising' }, # 68972
'Q22669850':	{	'ar':'تخطيط', 'en':'calligraphic work' }, # 62917
#'Q732577':		{	'ar':'منشور', 'en':'publication' }, # 56024
'Q61855877':	{	'ar':'حلقة بودكاست', 'en':'podcast episode' }, # 49335
'Q1298668':		{	'ar':'مشروع بحثي', 'en':'research project' }, # 46027
'Q20541692':	{	'ar':'مستوطنة في غاليسيا، إسبانيا', 'en':'settlement in Galicia, Spain' }, # 44303
'Q5707594':		{	'ar':'مقالة إخبارية', 'en':'news article' }, # 43411
'Q86442081':	{	'ar':'إدارة بلدية في فرنسا', 'en':'administration municipale en France' }, # 39149
#'Q17315159':	{	'ar':'مباراة منتخب كرة قدم وطني ضد منتخب وطني آخر', 'en':'international association football match' }, # 27192
#'Q294414':		{	'ar':'منصب عام', 'en':'public office' }, # 24185
'Q65618976':	{	'ar':'هيروغليفية مصرية', 'en':'Egyptian hieroglyph' }, # 23477
#'Q125191':		{	'ar':'صورة', 'en':'photograph' }, # 21894
#'Q281460':		{	'ar':'الأرغن ذو الأنابيب', 'en':'pipe organ' }, # 21129
#'Q11446':		{	'ar':'سفينة', 'en':'ship' }, # 21000
'Q2311958':		{	'ar':'كانتون', 'en':'canton' }, # 19714
'Q18131152':	{	'ar':'مرحلة', 'en':'round' }, # 19634
'Q1697305':		{	'ar':'دالة', 'en':'narrative motif' }, # 19033
'Q93184':		{	'ar':'رسم', 'en':'drawing' }, # 18784
'Q163740':		{	'ar':'منظمة غير ربحية', 'en':'nonprofit organization' }, # 18634
"""

# ---
from desc_dicts.descraptions import Space_Descraptions

# ---
en_des_to_ar_no_lower = {
    "Royal Dutch East indies Army personel": "أفراد جيش جزر الهند الشرقية الملكية الهولندية",
    "duits beeldend kunstenaar": "فنان تشكيلي ألماني",
    "politician from Trinidad and Tobago": "سياسي من ترينيداد وتوباغو",
}
# ---
en_des_to_ar = {x.lower(): z for x, z in en_des_to_ar_no_lower.items()}
# ---
Space_tab = {
    "Q18611609": "كوكب غير مؤكد خارج المجموعة الشمسية",  # unconfirmed exoplanet # 20689
    "Q13890": "نجم مزدوج",
    "Q6999": "جرم فلكي",
    "Q83373": "نجم زائف",
    "Q2247863": "نجم",
    "Q1153690": "نجم متغير طويل",
    "Q115518": "مجرة ذات سطوع سطحي منخفض",
    "Q130019": "نجم كربوني",
    "Q1332364": "متغير بيضاوي دوار",
    "Q13632": "سديم كوكبي",
    "Q1457376": "كسوف نجم ثنائي",
    "Q15917122": "نجم متغير دوار",
    "Q168845": "عنقود نجمي",
    "Q1931185": "مصدر راديو فلكي",
    "Q204194": "سديم مظلم",
    "Q318": "مجرة",
    "Q44559": "كوكب خارج المجموعة الشمسية",
    "Q46587": "نواة مجرة نشطة",
    "Q523": "نجم",
    "Q6243": "نجم متغير",
    "Q66619666": "نجم",
    "Q67206691": "مصدر أشعة تحت حمراء",
    "Q71963409": "تجمع مجري مدمج",
    "Q726242": "نجم",
    "Q72803622": "نجم",
}
# ---
for q in Space_Descraptions:
    Space_tab[q] = Space_Descraptions[q]["ar"]
# ---
"""
query = default_query #later, I want to manage this with params
sparql_query = 'SELECT ?item WHERE {   ?item wdt:P31 wd:Q21191270 .   ?item wdt:P179 ?dummy0 . }'
sparql_query = 'select ?item where{{select ?item ?itemLabel ?itemDescription WHERE {   ?item wdt:P31 wd:Q21191270 .   ?item wdt:P179 ?dummy0 . {service wikibase:label{bd:serviceParam wikibase:language "nl" . }}}} filter (!bound(?itemDescription))}'


sparql_query='SELECT ?item WHERE { ?item wdt:P31 wd:Q5 . ?item wdt:P106 ?dummy0 . ?wiki0 <http://schema.org/about> ?item . ?wiki0 <http://schema.org/isPartOf> <https://nl.wikipedia.org/> }'  #claim[31:5] and claim[106] and link[nlwiki]

sparql_query = 'select * {{SELECT ?item ?itemDescription WHERE {{ ?item wdt:P31 wd:Q4167836 }  service wikibase:label{bd:serviceParam wikibase:language "nl" . }  }}}'

"""
# ---
all_types_list = [
    "Q571",  # boek
    "Q134556",  # single
    "Q16970",  # kerkgebouw
    "Q34763",  # schiereiland
    "Q95074",  # personage
    "Q2912397",
    "Q23442",  # eendaagse wielerwedstrijd  # eiland
    "Q23397",  # meer
    "Q102496",  # parochie
    "Q273057",  # discografie
    "Q207628",  # compositie
]
# ---
simple_set_byP131 = [
    "Q24764",
    "Q70208",
    "Q127448",
    "Q203300",
    "Q262166",
    "Q262166",
    "Q378508",
    "Q484170",
    "Q493522",
    "Q612229",
    "Q640364",
    "Q659103",
    "Q667509",
    "Q747074",
    "Q755707",
    "Q856076",
    "Q856079",
    "Q955655",
    "Q1054813",
    "Q13218690",
    "Q15127838",
    "Q2261863",
    "Q494721",  # steden
    "Q1363145",
    "Q1500350",
    "Q1500352",
    "Q1530824",
    "Q1840161",
    "Q2661988",
    "Q2590631",
    "Q2460358",
    "Q1849719",
    "Q2989398",
    "Q3327873",
    "Q3685462",
    "Q5154047",
    "Q6784672",
    "Q16739079",
    "Q20538317",
    "Q23925393",  # marokkaanse douar
    "Q23012917",
    "Q2225692",
    "Q4174776",
    "Q13100073",
    "Q23827464",
    "Q3558970",
    "Q15630849",
    "Q21672098",  # dorpen
    "Q188509",  # buitenwijk
    "Q9842",  # basisschool
    "Q3914",  # school
    "Q355304",  # watergang
    "Q54050",  # heuvel
    "Q166735",  # broekbos
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
]
# ---
Geo_entity = {
    "Q4989906": "معلم تذكاري",
    "Q13424466": "ميناء طبيعي",
    "Q30022": "مقهى",
    "Q179700": "تمثال",
    "Q180958": "كلية",
    "Q54050": "تل",
    "Q11755880": "مبنى سكني",  # residential building
    "Q569500": "مركز صحي",
    "Q39614": "مقبرة",
    "Q123705": "حي سكني",
    "Q12323": "سد",
    "Q22698": "متنزه",
    "Q131681": "خزان مائي",
    "Q4421": "غابة",
}
# ---
p50s = {
    "Q571": {"ar": "كتاب", "P": "P50"},
    "Q7725634": {"ar": "عمل أدبي", "P": "P50"},  # رواية
    "Q1760610": {"ar": "كتاب هزلي", "P": "P50"},
    "Q1318295": {"ar": "قصة", "P": "P50"},
    "Q49084": {"ar": "قصة قصيرة", "P": "P50"},
    "Q96739634": {"ar": "حركة فردية", "P": "P50"},
    "Q18918145": {"ar": "مقالة أكاديمية", "P": "P50"},
    "Q187685": {"ar": "أطروحة أكاديمية", "P": "P50"},
    # 'Q19389637': "مقالة سيرة ذاتية",
    # 'Q571': "كتاب",
    # 'Q2831984': 'ألبوم قصص مصورة',
}
# ---


# حركة فردية
# ---
# رواية
# ---
space_list_and_other = {
    # ---
    # 'Q72802508',#emission-line galaxy
    # ---
    "Q96739634": "حركة فردية",
    "Q3331189": "طبعة",
    "Q7187": "جين",
    "Q2467461": "قسم أكاديمي",
    "Q277338": "جين كاذب",
    "Q14752149": "نادي كرة قدم للهواة",
    "Q476028": "نادي كرة قدم",
    "Q620615": "تطببيق محمول",
    "Q783866": "مكتبة جافا سكريبت",  # 17241
    "Q2831984": "ألبوم قصص مصورة",
    "Q19389637": "مقالة سيرة ذاتية",
    "Q3305213": "لوحة فنية",
    "Q7889": "لعبة فيديو",
    "Q8054": "بروتين",
    "Q265158": "مراجعة",
    "Q18918145": "مقالة أكاديمية",
    "Q13433827": "مقالة موسوعية",
    # ---
    "Q7278": "حزب سياسي",
}
Taton_list = {kj: space_list_and_other[kj] for kj in space_list_and_other}
# ---
# p50s جاهزة في SPARQLSE
for dd in p50s:
    space_list_and_other[dd] = p50s[dd]["ar"]
# ---
# Space_tab جاهزة في SPARQLSE
for sss in Space_tab:
    # space_list_and_other.append(sss)
    space_list_and_other[sss] = Space_tab[sss]
# ---
others_list_2 = [
    "Q820655",  # قانون تشريعي
    "Q21191270",  # حلقة مسلسل تلفزيوني
    "Q1983062",  # حلقة
    "Q45382",  # انقلاب
    "Q7366",  # أغنية
    "Q134556",  # أغنية منفردة
    "Q11424",  # فيلم
    "Q24862",  # فيلم قصير
    "Q3231690",  # طراز سيارة
]
# ---
others_list = {
    # ---
    "Q43229": {"ar": "منظمة"},
    "Q728937": {"ar": "خط سكة حديد"},
    "Q46970": {"ar": "شركة طيران"},
    "Q4830453": {"ar": "شركة"},
    "Q783794": {"ar": "شركة"},
    # ---
    "Q4022": {
        "ar": "نهر",
    },
    "Q215380": {
        "ar": "طاقم موسيقي",
    },
    "Q8502": {
        "ar": "جبل",
    },
    "Q532": {
        "ar": "قرية",
        # "en":"village",
    },
    "Q54050": {
        "ar": "تل",
        # "en":"village",
    },
    "Q79007": {
        "ar": "شارع",
        # "en":"street",
    },
    "Q12280": {"ar": "جسر"},
    "Q39614": {
        "ar": "مقبرة",
        # "nl": "begraafplaats",
        # "en":"cemetery",
        # "en-ca":"cemetery",
        # "en-gb":"cemetery",
    },
    # ---
    "Q5398426": {"ar": "مسلسل تلفزيوني", "en": ""},
    "Q27020041": {"ar": "موسم رياضي", "en": ""},  # 1987
    # 'Q1983062':{"ar":"حلقة", "en":"" },
    # 'Q21191270':{"ar":"حلقة مسلسل تلفزيوني", "en":"" },
    # 'Q15416':{"ar":"برنامج تلفزيوني", "en":"" },
    # 'Q11424':{"ar":"فيلم", "en":"" },
}
# ---
for geo in Geo_entity:
    others_list[geo] = {"ar": Geo_entity[geo], "en": ""}
# ---
bldiat = {
    "Q484170": "فرنسا",  # a 37477
    "Q262166": "ألمانيا",  # a 7941
    "Q3184121": "البرازيل",  # a 5260
    "Q6784672": "سلوفاكيا",  # a 2864
    "Q667509": "النمسا",  # a 2335
    "Q24764": "الفلبين",  # a 1486
    "Q2039348": "هولندا",  # a 892
    "Q57058": "كرواتيا",  # a 880
    "Q1054813": "اليابان",  # a 691
    "Q1758856": "مالي",  # a 667
    "Q747074": "إيطاليا",  # a 594
    "Q493522": "بلجيكا ",  # a 573
    "Q755707": "النرويج",  # a 337
    "Q1349648": "اليونان",  # a 333
    "Q127448": "السويد",  # a 286
    "Q1906268": "بلغاريا",  # a 264
    "Q856076": "فنلندا ",  # a 219
    "Q378508": "أنغولا",  # a 158
}
# ---
for vv in bldiat:
    others_list[vv] = {"ar": f"بلدية في {bldiat[vv]}" ""}
# ---
qura = {
    "Q21672098": {"P17": "أوكرانيا", "P31": "قرية"},
    "Q1529096": {"P17": "تركيا", "P31": "قرية"},
    "Q3558970": {"P17": "بولندا", "P31": "قرية"},
    "Q56436498": {"P17": "الهند", "P31": "قرية"},  # 56802
    "Q484170": {"P17": "فرنسا", "P31": "بلدية"},
    "Q262166": {"P17": "ألمانيا", "P31": "بلدية"},
    "Q747074": {"P17": "ألمانيا", "P31": "بلدية"},
    "Q22865": {"P17": "ألمانيا", "P31": "بلدية"},
    "Q13417250": {"P17": "أذربيجان", "P31": "بلدية"},
    # ---
}
# ---
"""





"""
# ---
for q in qura:
    # labs = '%s في %s' % ( qura[q]['P31'] , qura[q]['P17'] )
    others_list[q] = {"ar": qura[q]["P31"], "en": ""}
# ---


# ---
songs_type = {
    "Q7366": "أغنية",
    "Q482994": "ألبوم",
    "Q134556": "أغنية",  # أغنية منفردة
    "Q7302866": "مقطع صوتي",
    "Q1573906": "جولة موسيقية",
    "Q182832": "حفلة موسيقية",
}
# ---
for son in songs_type:
    others_list[son] = {"ar": songs_type[son], "en": ""}
# ---


# مقالة سيرة ذاتية

# biografisch artikel
# ---Q19389637#Q2831984

# كتاب
# ---

# مجرة
# ---


# كسوف نجم ثنائي

# ---Q7187


# جين

# ---Q8054


# بروتين

# ---
# حلقة
# Q21191270#Q1983062

# ---


# ---


# جبل

# ---


# ---
"""



















"""
# ---
space_list_and_other_2 = {
    "Q96739634": {"ar": "حركة فردية", "P": "P50"},
    "Q3331189": {"ar": "طبعة", "P": "P629"},
    "Q7187": {"ar": "جين", "P": "P703"},
    "Q2467461": {"ar": "قسم أكاديمي", "P": ""},
    "Q277338": {"ar": "جين كاذب", "P": "P703"},
    "Q14752149": {"ar": "نادي كرة قدم للهواة", "P": ""},
    "Q476028": {"ar": "نادي كرة قدم", "P": ""},
    "Q620615": {"ar": "تطببيق محمول", "P": ""},
    "Q783866": {"ar": "مكتبة جافا سكريبت", "P": "P178"},  # 17241
    "Q2831984": {"ar": "ألبوم قصص مصورة", "P": ""},
    "Q19389637": {"ar": "مقالة سيرة ذاتية", "P": ""},
    "Q3305213": {"ar": "لوحة فنية", "P": ""},
    "Q7889": {"ar": "لعبة فيديو", "P": ""},
    "Q8054": {"ar": "بروتين", "P": ""},
    # ---
    "Q7278": {"ar": "حزب سياسي", "P": ""},
}
# ---
# Q11424  فيلم


# موسم رياضي
# ---

# طراز سيارة
# ---x

# أغنية
# ---
# ---

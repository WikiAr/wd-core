#!/usr/bin/env python3
'''
from nep.tables.lists import *

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
'''

# ---
import sys
from desc_dicts.descraptions import Qid_Descraptions, Space_Descraptions

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
    'Q18611609': 'كوكب غير مؤكد خارج المجموعة الشمسية',  # unconfirmed exoplanet # 20689
    'Q13890': 'نجم مزدوج',
    'Q6999': 'جرم فلكي',
    'Q83373': 'نجم زائف',
    'Q2247863': 'نجم',
    'Q1153690': 'نجم متغير طويل',
    'Q115518': 'مجرة ذات سطوع سطحي منخفض',
    'Q130019': 'نجم كربوني',
    'Q1332364': 'متغير بيضاوي دوار',
    'Q13632': 'سديم كوكبي',
    'Q1457376': 'كسوف نجم ثنائي',
    'Q15917122': 'نجم متغير دوار',
    'Q168845': 'عنقود نجمي',
    'Q1931185': 'مصدر راديو فلكي',
    'Q204194': 'سديم مظلم',
    'Q318': 'مجرة',
    'Q44559': 'كوكب خارج المجموعة الشمسية',
    'Q46587': 'نواة مجرة نشطة',
    'Q523': 'نجم',
    'Q6243': 'نجم متغير',
    'Q66619666': 'نجم',
    'Q67206691': 'مصدر أشعة تحت حمراء',
    'Q71963409': 'تجمع مجري مدمج',
    'Q726242': 'نجم',
    'Q72803622': 'نجم',
}
# ---
for q in Space_Descraptions:
    Space_tab[q] = Space_Descraptions[q]["ar"]
# ---
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
nationalities = {
    "آيسلندا": {"man": "أيسلندي", "women": "أيسلندية"},
    "آيسلندا": {"man": "آيسلندي", "women": "آيسلندية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "الدولة الأموية": {"man": "أموي", "women": "أموية"},
    "الدولة العثمانية": {"man": "عثماني", "women": "عثمانية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "مقدونيا الشمالية": {"man": "شمال مقدوني", "women": "شمال مقدونية"},
    "شمال مقدونيا": {"man": "شمال مقدوني", "women": "شمال مقدونية"},
    "مقدونيا القديمة": {"man": "مقدوني قديم", "women": "مقدونية قديمة"},
    "مقدونيا": {"man": "مقدوني", "women": "مقدونية"},
    "مقدونيا": {"man": "مقدوني", "women": "مقدونية"},
    "تركمان": {"man": "تركماني", "women": "تركمانية"},
    "تركمانستان": {"man": "تركماني", "women": "تركمانية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "ميانمار": {"man": "ميانماري", "women": "ميانمارية"},
    "الإمبراطورية الرومانية المقدسة": {"man": "روماني مقدس", "women": "رومانية مقدسة"},
    "الإمبراطورية البيزنطية": {"man": "بيزنطي", "women": "بيزنطية"},
    "الإمبراطورية الساسانية": {"man": "ساساني", "women": "ساسانية"},
    "روما القديمة": {"man": "رومي قديم", "women": "رومية قديمة"},
    "رومانيا القديمة": {"man": "روماني قديم", "women": "رومانية قديمة"},
    "اليونان القديمة": {"man": "يوناني قديم", "women": "يونانية قديمة"},
    "الإمبراطورية النمساوية المجرية": {"man": "نمساوي مجري", "women": "نمساوية مجرية"},
    "الولايات المتحدة": {"man": "أمريكي", "women": "أمريكية"},
    "غوام": {"man": "غوامي", "women": "غوامية"},
    "ساموا الأمريكية": {"man": "ساموي أمريكي", "women": "ساموية أمريكية"},
    "بورتوريكو": {"man": "بورتوريكي", "women": "بورتوريكية"},
    "جزر سليمان": {"man": "سليماني", "women": "سليمانية"},
    "جزر القمر": {"man": "قمري", "women": "قمرية"},
    "جزر القمر": {"man": "قمري", "women": "قمرية"},
    "تشيكوسلوفاكيا": {"man": "تشيكوسلوفاكي", "women": "تشيكوسلوفاكية"},
    "الرأس الأخضر": {"man": "رأس أخضري", "women": "رأس أخضرية"},
    "جزر الأنتيل": {"man": "أنتيلي", "women": "أنتيلية"},
    "البنغال": {"man": "بنغالي", "women": "بنغالية"},
    "بوهيميا": {"man": "بوهيمي", "women": "بوهيمية"},
    "جمهورية أفريقيا الوسطى": {"man": "أفريقي أوسطي", "women": "وسط أفريقية"},
    "القرم": {"man": "قرمي", "women": "قرمية"},
    "غينيا الاستوائية": {"man": "غيني استوائي", "women": "غينية استوائية"},
    "جزر فارو": {"man": "فاروي", "women": "فاروية"},
    "غويانا الفرنسية": {"man": "غوياني فرنسي", "women": "غويانية فرنسية"},
    "قيرغيز": {"man": "قيرغيزي", "women": "قيرغيزية"},
    "مورافيا": {"man": "مورافي", "women": "مورافية"},
    "دول الشمال": {"man": "نوردي", "women": "نوردية"},
    "أوسيتيا الجنوبية": {"man": "أوسيتي", "women": "أوسيتية"},
    "جنوب شرق آسيا": {"man": "آسيوي جنوب شرقي", "women": "آسيوية جنوب شرقية"},
    "أوروبا الجنوبية": {"man": "أوروبي جنوبي", "women": "أوروبية جنوبية"},
    "جنوب غرب آسيا": {"man": "جنوب غرب آسيوي", "women": "جنوب غربي آسيوية"},
    "ترينيداد وتوباغو": {"man": "ترنيدادي", "women": "ترنيدادية"},
    "الهند الغربية": {"man": "هندي غربي", "women": "هندية غربية"},
    "يوروبا": {"man": "يوروبي", "women": "يوروبية"},
    "الأبالاش": {"man": "أبلاشي", "women": "أبلاشية"},
    "أسترالاسيا": {"man": "أسترالاسي", "women": "أسترالاسية"},
    "آسيا الوسطى": {"man": "آسيوي أوسطي", "women": "آسيوية أوسطية"},
    "الشيشان": {"man": "شيشاني", "women": "شيشانية"},
    "تايبيه الصينية": {"man": "تايبي صيني", "women": "تايبيه صينية"},
    "شرق آسيا": {"man": "آسيوي شرقي", "women": "آسيوية شرقية"},
    "ولايات ميكرونيسيا المتحدة": {"man": "ميكرونيزي", "women": "ميكرونيزية"},
    "غوادلوب": {"man": "غواديلوبي", "women": "غواديلوبية"},
    "قبرص الشمالية": {"man": "قبرصي شمالي", "women": "قبرصية شمالية"},
    "ناورو": {"man": "ناوروني", "women": "ناورونية"},
    "غامبيا": {"man": "غامبي", "women": "غامبية"},
    "الاتحاد السوفيتي": {"man": "سوفيتي", "women": "سوفيتية"},
    "غرب آسيا": {"man": "آسيوي غربي", "women": "آسيوية غربية"},
    "الصحراء الغربية": {"man": "صحراوي", "women": "صحراوية"},
    "ماكاو": {"man": "ماكاوي", "women": "ماكاوية"},
    "زائير": {"man": "زائيري", "women": "زائيرية"},
    "المملكة المتحدة": {"man": "بريطاني", "women": "بريطانية"},
    "جورجيا": {"man": "جورجي", "women": "جورجية"},
    "الشرق الأوسط": {"man": "شرق أوسطي", "women": "شرقية أوسطية"},
    "الأوروغواي": {"man": "أوروغواياني", "women": "أوروغوايانية"},
    "جبل طارق": {"man": "جبل طارقي", "women": "جبل طارقية"},
    "رومانيا القديمة": {"man": "روماني قديم", "women": "رومانية قديمة"},
    "رودسيا": {"man": "رودوسي", "women": "رودوسية"},
    "جزر مارشال": {"man": "مارشالي", "women": "مارشالية"},
    "الصين": {"man": "صيني", "women": "صينية"},
    "أيرلندا الشمالية": {"man": "أيرلندي شمالي", "women": "أيرلندية شمالية"},
    "أيرلندا الشمالية": {"man": "أيرلندي شمالي", "women": "أيرلندية شمالية"},
    "أيرلندا": {"man": "أيرلندي", "women": "أيرلندية"},
    "جمهورية أيرلندا": {"man": "أيرلندي", "women": "أيرلندية"},
    "اسكتلندا": {"man": "اسكتلندي", "women": "اسكتلندية"},
    "إنجلترا": {"man": "إنجليزي", "women": "إنجليزية"},
    "ويلز": {"man": "ويلزي", "women": "ويلزية"},
    "أبخازيا": {"man": "أبخازي", "women": "أبخازية"},
    "أفغانستان": {"man": "أفغاني", "women": "أفغانية"},
    "أفريقيا": {"man": "أفريقي", "women": "أفريقية"},
    "ألبانيا": {"man": "ألباني", "women": "ألبانية"},
    "الجزائر": {"man": "جزائري", "women": "جزائرية"},
    "مصر القديمة": {"man": "مصري قديم", "women": "مصرية قديمة"},
    "إغريق": {"man": "إغريقي", "women": "إغريقية"},
    "الأندلس": {"man": "أندلسي", "women": "أندلسية"},
    "أندورا": {"man": "أندوري", "women": "أندورية"},
    "أنغولا": {"man": "أنغولي", "women": "أنغولية"},
    "الأرجنتين": {"man": "أرجنتيني", "women": "أرجنتينية"},
    "أرمينيا": {"man": "أرميني", "women": "أرمينية"},
    "آسيا": {"man": "آسيوي", "women": "آسيوية"},
    "أستراليا": {"man": "أسترالي", "women": "أسترالية"},
    "النمسا": {"man": "نمساوي", "women": "نمساوية"},
    "أذربيجان": {"man": "أذربيجاني", "women": "أذربيجانية"},
    "باهاماس": {"man": "باهاماسي", "women": "باهاماسية"},
    "البحرين": {"man": "بحريني", "women": "بحرينية"},
    "بنغلاديش": {"man": "بنغلاديشي", "women": "بنغلاديشية"},
    "باربادوس": {"man": "باربادوسي", "women": "باربادوسية"},
    "روسيا البيضاء": {"man": "بيلاروسي", "women": "بيلاروسية"},
    "بلجيكا": {"man": "بلجيكي", "women": "بلجيكية"},
    "بليز": {"man": "بليزي", "women": "بليزية"},
    "بنين": {"man": "بنيني", "women": "بنينية"},
    "بوتان": {"man": "بوتاني", "women": "بوتانية"},
    "بوليفيا": {"man": "بوليفي", "women": "بوليفية"},
    "البوسنة والهرسك": {"man": "بوسني", "women": "بوسنية"},
    "بوتسوانا": {"man": "بوتسواني", "women": "بوتسوانية"},
    "البرازيل": {"man": "برازيلي", "women": "برازيلية"},
    "بلغاريا": {"man": "بلغاري", "women": "بلغارية"},
    "بوركينا فاسو": {"man": "بوركينابي", "women": "بوركينابية"},
    "بوروندي": {"man": "بوروندي", "women": "بوروندية"},
    "كمبوديا": {"man": "كمبودي", "women": "كمبودية"},
    "الكاميرون": {"man": "كاميروني", "women": "كاميرونية"},
    "كندا": {"man": "كندي", "women": "كندية"},
    "الكاريبي": {"man": "كاريبي", "women": "كاريبية"},
    "تشاد": {"man": "تشادي", "women": "تشادية"},
    "تشيلي": {"man": "تشيلي", "women": "تشيلية"},
    "كولومبيا": {"man": "كولومبي", "women": "كولومبية"},
    "كوستاريكا": {"man": "كوستاريكي", "women": "كوستاريكية"},
    "كرواتيا": {"man": "كرواتي", "women": "كرواتية"},
    "كوبا": {"man": "كوبي", "women": "كوبية"},
    "قبرص": {"man": "قبرصي", "women": "قبرصية"},
    "التشيك": {"man": "تشيكي", "women": "تشيكية"},
    "الدنمارك": {"man": "دنماركي", "women": "دنماركية"},
    "جيبوتي": {"man": "جيبوتي", "women": "جيبوتية"},
    "جمهورية الدومنيكان": {"man": "دومينيكاني", "women": "دومينيكانية"},
    "جمهورية الدومينيكان": {"man": "دومينيكاني", "women": "دومينيكانية"},
    "تيمور الشرقية": {"man": "تيموري شرقي", "women": "تيمورية شرقية"},
    "الإكوادور": {"man": "إكوادوري", "women": "إكوادورية"},
    "مصر": {"man": "مصري", "women": "مصرية"},
    "السلفادور": {"man": "سلفادوري", "women": "سلفادورية"},
    "إريتريا": {"man": "إريتري", "women": "إريترية"},
    "إستونيا": {"man": "إستوني", "women": "إستونية"},
    "إسواتيني": {"man": "إسواتيني", "women": "إسواتينية"},
    "إثيوبيا": {"man": "إثيوبي", "women": "إثيوبية"},
    "أوروبا": {"man": "أوروبي", "women": "أوروبية"},
    "فيجي": {"man": "فيجي", "women": "فيجية"},
    "فنلندا": {"man": "فنلندي", "women": "فنلندية"},
    "فرنسا": {"man": "فرنسي", "women": "فرنسية"},
    "الغابون": {"man": "غابوني", "women": "غابونية"},
    "ألمانيا": {"man": "ألماني", "women": "ألمانية"},
    "غانا": {"man": "غاني", "women": "غانية"},
    "اليونان": {"man": "يوناني", "women": "يونانية"},
    "جرينلاند": {"man": "جرينلاندي", "women": "جرينلاندية"},
    "غرينادا": {"man": "غرينادي", "women": "غرينادية"},
    "غواتيمالا": {"man": "غواتيمالي", "women": "غواتيمالية"},
    "غينيا": {"man": "غيني", "women": "غينية"},
    "بابوا غينيا الجديدة": {"man": "غيني", "women": "غينية"},
    "غينيا بيساو": {"man": "غيني بيساوي", "women": "غينية بيساوية"},
    "غيانا": {"man": "غياني", "women": "غيانية"},
    "هايتي": {"man": "هايتي", "women": "هايتية"},
    "هندوراس": {"man": "هندوراسي", "women": "هندوراسية"},
    "هونغ كونغ": {"man": "هونغ كونغي", "women": "هونغ كونغية"},
    "المجر": {"man": "مجري", "women": "مجرية"},
    "الهند": {"man": "هندي", "women": "هندية"},
    "إندونيسيا": {"man": "إندونيسي", "women": "إندونيسية"},
    "إيران": {"man": "إيراني", "women": "إيرانية"},
    "العراق": {"man": "عراقي", "women": "عراقية"},
    "إسرائيل": {"man": "إسرائيلي", "women": "إسرائيلية"},
    "جزر فيرجن البريطانية": {"man": "فيرجني", "women": "فيرجنية"},
    "برمودا": {"man": "برمودي", "women": "برمودية"},
    "موناكو": {"man": "موناكي", "women": "موناكية"},
    "بروناي": {"man": "بروني", "women": "برونية"},
    "كاليدونيا الجديدة": {"man": "كاليدوني", "women": "كاليدونية"},
    "إيطاليا": {"man": "إيطالي", "women": "إيطالية"},
    "ساحل العاج": {"man": "إفواري", "women": "إفوارية"},
    "جامايكا": {"man": "جامايكي", "women": "جامايكية"},
    "اليابان": {"man": "ياباني", "women": "يابانية"},
    "الأردن": {"man": "أردني", "women": "أردنية"},
    "يهود": {"man": "يهودي", "women": "يهودية"},
    "كازاخستان": {"man": "كازاخستاني", "women": "كازاخستانية"},
    "كينيا": {"man": "كيني", "women": "كينية"},
    "كيريباتي": {"man": "كيريباتي", "women": "كيريباتية"},
    "كوريا": {"man": "كوري", "women": "كورية"},
    "كوسوفو": {"man": "كوسوفي", "women": "كوسوفية"},
    "الكويت": {"man": "كويتي", "women": "كويتية"},
    "قيرغيزستان": {"man": "قيرغيزستاني", "women": "قيرغيزستانية"},
    "بروسيا": {"man": "بروسي", "women": "بروسية"},
    "لاوس": {"man": "لاوسي", "women": "لاوسية"},
    "لاتفيا": {"man": "لاتيفي", "women": "لاتيفية"},
    "لبنان": {"man": "لبناني", "women": "لبنانية"},
    "ليسوتو": {"man": "ليسوثوي", "women": "ليسوثوية"},
    "ليبيريا": {"man": "ليبيري", "women": "ليبيرية"},
    "ليبيا": {"man": "ليبي", "women": "ليبية"},
    "ليختنشتاين": {"man": "ليختنشتاني", "women": "ليختنشتانية"},
    "ليتوانيا": {"man": "ليتواني", "women": "ليتوانية"},
    "لوكسمبورغ": {"man": "لوكسمبورغي", "women": "لوكسمبورغية"},
    "مدغشقر": {"man": "مدغشقري", "women": "مدغشقرية"},
    "مالاوي": {"man": "ملاوي", "women": "ملاوية"},
    "ماليزيا": {"man": "ماليزي", "women": "ماليزية"},
    "جزر المالديف": {"man": "مالديفي", "women": "مالديفية"},
    "مالي": {"man": "مالي", "women": "مالية"},
    "مالطا": {"man": "مالطي", "women": "مالطية"},
    "موريتانيا": {"man": "موريتاني", "women": "موريتانية"},
    "موريشيوس": {"man": "موريشيوسي", "women": "موريشيوسية"},
    "المكسيك": {"man": "مكسيكي", "women": "مكسيكية"},
    "مولدوفا": {"man": "مولدوفي", "women": "مولدوفية"},
    "منغوليا": {"man": "منغولي", "women": "منغولية"},
    "الجبل الأسود": {"man": "مونتينيغري", "women": "مونتينيغرية"},
    "المغرب": {"man": "مغربي", "women": "مغربية"},
    "موزمبيق": {"man": "موزمبيقي", "women": "موزمبيقية"},
    "ناميبيا": {"man": "ناميبي", "women": "ناميبية"},
    "نيبال": {"man": "نيبالي", "women": "نيبالية"},
    "هولندا": {"man": "هولندي", "women": "هولندية"},
    "نيوزيلندا": {"man": "نيوزيلندي", "women": "نيوزيلندية"},
    "نيكاراغوا": {"man": "نيكاراغوي", "women": "نيكاراغوية"},
    "النيجر": {"man": "نيجري", "women": "نيجرية"},
    "نيجيريا": {"man": "نيجيري", "women": "نيجيرية"},
    "كوريا الشمالية": {"man": "كوري شمالي", "women": "كورية شمالية"},
    "النرويج": {"man": "نرويجي", "women": "نرويجية"},
    "أوقيانوسيا": {"man": "أوقيانوسي", "women": "أوقيانوسية"},
    "عمان": {"man": "عماني", "women": "عمانية"},
    "باكستان": {"man": "باكستاني", "women": "باكستانية"},
    "بالاو": {"man": "بالاوي", "women": "بالاوية"},
    "فلسطين": {"man": "فلسطيني", "women": "فلسطينية"},
    "بنما": {"man": "بنمي", "women": "بنمية"},
    "باراغواي": {"man": "باراغواياني", "women": "باراغوايانية"},
    "بيرو": {"man": "بيروفي", "women": "بيروفية"},
    "الفلبين": {"man": "فلبيني", "women": "فلبينية"},
    "بولندا": {"man": "بولندي", "women": "بولندية"},
    "البرتغال": {"man": "برتغالي", "women": "برتغالية"},
    "قطر": {"man": "قطري", "women": "قطرية"},
    "جمهورية الكونغو": {"man": "كونغولي", "women": "كونغولية"},
    "جمهورية الكونغو الديمقراطية": {"man": "كونغولي ديمقراطي", "women": "كونغولية ديمقراطية"},
    "رومانيا": {"man": "روماني", "women": "رومانية"},
    "روسيا": {"man": "روسي", "women": "روسية"},
    "رواندا": {"man": "رواندي", "women": "رواندية"},
    "ساموا": {"man": "ساموي", "women": "ساموية"},
    "السعودية": {"man": "سعودي", "women": "سعودية"},
    "السنغال": {"man": "سنغالي", "women": "سنغالية"},
    "صربيا": {"man": "صربي", "women": "صربية"},
    "سيشل": {"man": "سيشلي", "women": "سيشلية"},
    "سيراليون": {"man": "سيراليوني", "women": "سيراليونية"},
    "سنغافورة": {"man": "سنغافوري", "women": "سنغافورية"},
    "سلوفاكيا": {"man": "سلوفاكي", "women": "سلوفاكية"},
    "سلوفينيا": {"man": "سلوفيني", "women": "سلوفينية"},
    "الصومال": {"man": "صومالي", "women": "صومالية"},
    "جنوب أفريقيا": {"man": "جنوب أفريقي", "women": "جنوب أفريقية"},
    "كوريا الجنوبية": {"man": "كوري جنوبي", "women": "كورية جنوبية"},
    "جنوب السودان": {"man": "جنوب سوداني", "women": "جنوبية سودانية"},
    "إسبانيا": {"man": "إسباني", "women": "إسبانية"},
    "سريلانكا": {"man": "سريلانكي", "women": "سريلانكية"},
    "السودان": {"man": "سوداني", "women": "سودانية"},
    "سورينام": {"man": "سورينامي", "women": "سورينامية"},
    "سوازيلاند": {"man": "سوازيلندي", "women": "سوازيلندية"},
    "السويد": {"man": "سويدي", "women": "سويدية"},
    "سويسرا": {"man": "سويسري", "women": "سويسرية"},
    "سوريا": {"man": "سوري", "women": "سورية"},
    "ساو تومي": {"man": "ساوتومي", "women": "ساوتومية"},
    "تايوان": {"man": "تايواني", "women": "تايوانية"},
    "طاجيكستان": {"man": "طاجيكي", "women": "طاجيكستانية"},
    "تنزانيا": {"man": "تنزاني", "women": "تنزانية"},
    "تايلاند": {"man": "تايلاندي", "women": "تايلاندية"},
    "توغو": {"man": "توغولي", "women": "توغولية"},
    "تونغا": {"man": "تونغاني", "women": "تونغانية"},
    "تونس": {"man": "تونسي", "women": "تونسية"},
    "تركيا": {"man": "تركي", "women": "تركية"},
    "توفالو": {"man": "توفالي", "women": "توفالية"},
    "المملكة المتحدة": {"man": "بريطاني", "women": "بريطانية"},
    "أوغندا": {"man": "أوغندي", "women": "أوغندية"},
    "أوكرانيا": {"man": "أوكراني", "women": "أوكرانية"},
    "الإمارات": {"man": "إماراتي", "women": "إماراتية"},
    "أوزبكستان": {"man": "أوزبكستاني", "women": "أوزبكستانية"},
    "فانواتو": {"man": "فانواتي", "women": "فانواتية"},
    "الفاتيكان": {"man": "فاتيكاني", "women": "فاتيكانية"},
    "فنزويلا": {"man": "فنزويلي", "women": "فنزويلية"},
    "فيتنام": {"man": "فيتنامي", "women": "فيتنامية"},
    "اليمن": {"man": "يمني", "women": "يمنية"},
    "يوغوسلافيا": {"man": "يوغوسلافي", "women": "يوغوسلافية"},
    "زامبيا": {"man": "زامبي", "women": "زامبية"},
    "زيمبابوي": {"man": "زيمبابوي", "women": "زيمبابوية"},
    "أمريكا الوسطى": {"man": "أمريكي أوسطي", "women": "أمريكية أوسطية"},
    "أمريكا الشمالية": {"man": "أمريكي شمالي", "women": "أمريكية شمالية"},
    "أمريكا الجنوبية": {"man": "أمريكي جنوبي", "women": "أمريكية جنوبية"},
    "فيكتوريا (أستراليا)": {"man": "فيكتوري", "women": "فيكتورية"},
}
# ---
all_types_list = [
    'Q571',  # boek
    'Q134556',  # single
    'Q16970',  # kerkgebouw
    'Q34763',  # schiereiland
    'Q95074',  # personage
    'Q2912397' 'Q23442',  # eendaagse wielerwedstrijd  # eiland
    'Q23397',  # meer
    'Q102496',  # parochie
    'Q273057',  # discografie
    'Q207628',  # compositie
]
# ---
simple_set_byP131 = [
    'Q24764',
    'Q70208',
    'Q127448',
    'Q203300',
    'Q262166',
    'Q262166',
    'Q378508',
    'Q484170',
    'Q493522',
    'Q612229',
    'Q640364',
    'Q659103',
    'Q667509',
    'Q747074',
    'Q755707',
    'Q856076',
    'Q856079',
    'Q955655',
    'Q1054813',
    'Q13218690',
    'Q15127838',
    'Q2261863',
    'Q494721',  # steden
    'Q1363145',
    'Q1500350',
    'Q1500352',
    'Q1530824',
    'Q1840161',
    'Q2661988',
    'Q2590631',
    'Q2460358',
    'Q1849719',
    'Q2989398',
    'Q3327873',
    'Q3685462',
    'Q5154047',
    'Q6784672',
    'Q16739079',
    'Q20538317',
    'Q23925393',  # marokkaanse douar
    'Q23012917',
    'Q2225692',
    'Q4174776',
    'Q13100073',
    'Q23827464',
    'Q3558970',
    'Q15630849',
    'Q21672098',  # dorpen
    'Q188509',  # buitenwijk
    'Q9842',  # basisschool
    'Q3914',  # school
    'Q355304',  # watergang
    'Q54050',  # heuvel
    'Q166735',  # broekbos
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
    '',
]
# ---
Geo_entity = {
    'Q4989906': 'معلم تذكاري',
    'Q13424466': 'ميناء طبيعي',
    'Q30022': 'مقهى',
    'Q179700': 'تمثال',
    'Q180958': 'كلية',
    'Q54050': 'تل',
    'Q11755880': 'مبنى سكني',  # residential building
    'Q569500': 'مركز صحي',
    'Q39614': 'مقبرة',
    'Q123705': 'حي سكني',
    'Q12323': 'سد',
    'Q22698': 'متنزه',
    'Q131681': 'خزان مائي',
    'Q4421': 'غابة',
}
# ---
p50s = {
    'Q571': {'ar': "كتاب", 'P': 'P50'},
    'Q7725634': {'ar': "عمل أدبي", 'P': 'P50'},  # رواية
    'Q1760610': {'ar': "كتاب هزلي", 'P': 'P50'},
    'Q1318295': {'ar': "قصة", 'P': 'P50'},
    'Q49084': {'ar': "قصة قصيرة", 'P': 'P50'},
    'Q96739634': {'ar': "حركة فردية", 'P': 'P50'},
    'Q18918145': {'ar': "مقالة أكاديمية", 'P': 'P50'},
    'Q187685': {'ar': "أطروحة أكاديمية", 'P': 'P50'},
    # 'Q19389637': "مقالة سيرة ذاتية",
    # 'Q571': "كتاب",
    # 'Q2831984': 'ألبوم قصص مصورة',
}
SPARQLSE = {tt: main_quarry % tt for tt in Qid_Descraptions}
# ---
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q571 #كتاب
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q7725634 #رواية
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q1760610 #كتاب هزلي
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q1318295 #قصة
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q49084 #قصة قصيرة
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q187685 #أطروحة أكاديمية
# python3 core8/pwb.py nep/nldes3 limit:2000 sparql:Q96739634 #حركة فردية
# حركة فردية
for p50 in p50s:
    # ---
    SPARQLSE['dfd'] = (
        '''SELECT ?item WHERE
        { ?item wdt:P31 wd:%s .
        ?item wdt:P50 ?auth.
        ?auth rdfs:label ?authar. FILTER((LANG(?authar)) = "ar") .
        FILTER NOT EXISTS { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
        }
        '''
        % p50
    )
    # ---
    SPARQLSE[p50] = (
        '''SELECT DISTINCT
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P31 wd:%s .
  ?item wdt:P50 ?pp.
  ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item '''
        % p50
    )
    # ---
    if 'optional' in sys.argv:
        SPARQLSE[p50] = SPARQLSE[p50].replace('?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .', 'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}')
# ---
# رواية
SPARQLSE[
    'Q7725634'
] = '''SELECT DISTINCT
?item
(GROUP_CONCAT(DISTINCT(STR(?labe)); separator="@@") as ?lab)
WHERE {
  ?item wdt:P136 wd:Q8261 . ?item wdt:P31 wd:Q7725634 .
  ?item wdt:P50 ?pp.
  ?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .
  FILTER(NOT EXISTS {?item schema:description ?des.FILTER((LANG(?des)) = "ar")})
}
GROUP BY ?item '''
# ---
space_list_and_other = {
    # ---
    # 'Q72802508',#emission-line galaxy
    # ---
    'Q96739634': "حركة فردية",
    'Q3331189': "طبعة",
    'Q7187': "جين",
    'Q2467461': "قسم أكاديمي",
    'Q277338': "جين كاذب",
    'Q14752149': "نادي كرة قدم للهواة",
    'Q476028': "نادي كرة قدم",
    'Q620615': "تطببيق محمول",
    'Q783866': 'مكتبة جافا سكريبت',  # 17241
    'Q2831984': "ألبوم قصص مصورة",
    'Q19389637': "مقالة سيرة ذاتية",
    'Q3305213': "لوحة فنية",
    'Q7889': "لعبة فيديو",
    'Q8054': "بروتين",
    'Q265158': "مراجعة",
    'Q18918145': "مقالة أكاديمية",
    'Q13433827': "مقالة موسوعية",
    # ---
    'Q7278': "حزب سياسي",
}
Taton_list = {kj: space_list_and_other[kj] for kj in space_list_and_other}
# ---
# p50s جاهزة في SPARQLSE
for dd in p50s:
    space_list_and_other[dd] = p50s[dd]['ar']
# ---
# Space_tab جاهزة في SPARQLSE
for sss in Space_tab:
    # space_list_and_other.append(sss)
    space_list_and_other[sss] = Space_tab[sss]
# ---
others_list_2 = [
    'Q820655',  # قانون تشريعي
    'Q21191270',  # حلقة مسلسل تلفزيوني
    'Q1983062',  # حلقة
    'Q45382',  # انقلاب
    'Q7366',  # أغنية
    'Q134556',  # أغنية منفردة
    'Q11424',  # فيلم
    'Q24862',  # فيلم قصير
    'Q3231690',  # طراز سيارة
]
# ---
others_list = {
    # ---
    'Q43229': {"ar": 'منظمة'},
    'Q820655': {"ar": 'قانون تشريعي'},  # python3 core8/pwb.py nep/nldes3 sparql:Q820655
    'Q728937': {"ar": 'خط سكة حديد'},
    'Q46970': {"ar": 'شركة طيران'},
    'Q4830453': {"ar": 'شركة'},
    'Q783794': {"ar": 'شركة'},
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
    'Q5398426': {"ar": "مسلسل تلفزيوني", "en": ""},
    'Q27020041': {'ar': 'موسم رياضي', 'en': ''},  # 1987
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
    others_list[vv] = {"ar": f'بلدية في {bldiat[vv]}' ""}
# ---
qura = {
    "Q21672098": {'P17': "أوكرانيا", 'P31': 'قرية'},
    "Q1529096": {'P17': "تركيا", 'P31': 'قرية'},
    "Q3558970": {'P17': "بولندا", 'P31': 'قرية'},
    "Q56436498": {'P17': "الهند", 'P31': 'قرية'},  # 56802
    "Q484170": {'P17': "فرنسا", 'P31': 'بلدية'},
    "Q262166": {'P17': "ألمانيا", 'P31': 'بلدية'},
    "Q22865": {'P17': "ألمانيا", 'P31': 'بلدية'},
    "Q747074": {'P17': "ألمانيا", 'P31': 'بلدية'},
    "Q22865": {'P17': "إيطاليا", 'P31': 'بلدية'},
    "Q13417250": {'P17': "أذربيجان", 'P31': 'بلدية'},
    # ---
}
# ---
'''

python3 core8/pwb.py nep/nldes3 a3r sparql:Q1529096
python3 core8/pwb.py nep/nldes3 a3r sparql:Q3558970
python3 core8/pwb.py nep/nldes3 a3r sparql:Q56436498  #قرية هندية

'''
# ---
for q in qura:
    # labs = '%s في %s' % ( qura[q]['P31'] , qura[q]['P17'] )
    others_list[q] = {"ar": qura[q]['P31'], "en": ""}
# ---
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q7366 #أغنية
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q482994 #ألبوم
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q134556 #منفردة
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q7302866 #مقطع
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q1573906 #جولة
# python3 core8/pwb.py nep/nldes3 a3r sparql:Q182832 #حفلة
# ---
songs_type = {
    'Q7366': 'أغنية',
    'Q482994': 'ألبوم',
    'Q134556': 'أغنية',  # أغنية منفردة
    'Q7302866': 'مقطع صوتي',
    'Q1573906': 'جولة موسيقية',
    'Q182832': 'حفلة موسيقية',
}
# ---
for son in songs_type:
    others_list[son] = {"ar": songs_type[son], "en": ""}
# ---
for scdw in others_list:
    prop = '(wdt:P17|wdt:P131)'
    # ---
    if scdw in songs_type:
        prop = 'wdt:P175'
    # ---
    if scdw not in SPARQLSE:
        SPARQLSE[scdw] = 'SELECT ?item WHERE {' + f'?item wdt:P31 wd:{scdw}. ?item {prop} ?constellation.' + ' FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
        # ---
        if "a2r" in sys.argv:
            SPARQLSE[scdw] = 'SELECT ?item WHERE {' + f'?item wdt:P31 wd:{scdw}. ?item {prop} ?constellation.' + ' ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
        # ---
        if "a3r" in sys.argv:
            SPARQLSE[scdw] = 'SELECT ?item WHERE { ?item wdt:P31 wd:' + scdw + ' . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q44559
# python3 core8/pwb.py nep/nldes3 sparql:Q19389637
# مقالة سيرة ذاتية
SPARQLSE['Q19389637'] = 'select ?item where {?item wdt:P31 wd:Q19389637}'  # biografisch artikel
if "Q665807" in sys.argv:
    SPARQLSE['Q19389637'] = 'select ?item where {?item wdt:P31 wd:Q19389637 . ?item wdt:P1433 wd:Q665807. } '  # biografisch artikel
elif "noQ665807" in sys.argv:
    SPARQLSE[
        'Q19389637'
    ] = '''SELECT DISTINCT ?item WHERE {
  ?item wdt:P31 wd:Q8502; wdt:P17 ?dummy0.
FILTER NOT EXISTS { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
}

'''

# biografisch artikel
# ---Q19389637#Q2831984
# python3 core8/pwb.py nep/nldes3 sparql:Q571
# كتاب
SPARQLSE[
    'Q571'
] = '''SELECT ?item WHERE
    { ?item wdt:P31 wd:Q571 .
    ?item wdt:P50 ?auth.
    ?auth rdfs:label ?authar. FILTER((LANG(?authar)) = "ar") .
    FILTER NOT EXISTS { ?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
    }
    '''
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q318
# مجرة
SPARQLSE['Q318'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q318 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928.} '  # galaxyx
if "a2r" in sys.argv:
    SPARQLSE['Q318'] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q318 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
# ---
SPARQLSE[
    'Q318'
] = '''SELECT DISTINCT ?item
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
ORDER BY DESC(xsd:integer(SUBSTR(STR(?item),33)))'''
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q1457376
# python3 core8/pwb.py nep/nldes3 sparql:Q1457376 a2r
# كسوف نجم ثنائي
SPARQLSE['Q1457376'] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q1457376 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928.} '
if "a2r" in sys.argv:
    SPARQLSE['Q1457376'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q1457376 . ?item  wdt:P59 ?constellation. ?constellation wdt:P31 wd:Q8928. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
# ---Q7187
# python3 core8/pwb.py nep/nldes3 sparql:Q7187 yuy
# python3 core8/pwb.py nep/nldes3 sparql:Q7187 limit:20000
# python3 core8/pwb.py nep/nldes3 sparql:Q7187 yuy nokeep descqs
# جين
SPARQLSE['Q7187'] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q7187 . ?item  wdt:P703 ?constellation. ?constellation wdt:P31 wd:Q16521.} '
if "a2r" in sys.argv:
    SPARQLSE['Q7187'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q7187 . ?item  wdt:P703 ?constellation. ?constellation wdt:P31 wd:Q16521. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") } '
if "yuy" in sys.argv:
    SPARQLSE[
        'Q7187'
    ] = '''SELECT ?item WHERE { ?item wdt:P31 wd:Q7187 .  ?item wdt:P703 wd:Q15978631.
    FILTER NOT EXISTS { ?item schema:description ?d . FILTER(lang(?d)="ar") }
    } '''
# ---Q8054
# python3 core8/pwb.py nep/nldes3 sparql:Q8054
# python3 core8/pwb.py nep/nldes3 sparql:Q8054 descqs limit:10000
# python3 core8/pwb.py nep/nldes3 sparql:Q8054 a2r descqs nokeep limit:500
# python3 core8/pwb.py nep/nldes3 sparql:Q8054 yuy descqs nokeep limit:500
# بروتين
SPARQLSE['Q8054'] = 'SELECT ?item WHERE {?item wdt:P31 wd:Q8054 . ?item  (wdt:P702|wdt:P703) ?constellation.  FILTER NOT EXISTS {?item wdt:P31 wd:Q11173} } '
if "a2r" in sys.argv:
    SPARQLSE['Q8054'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q8054 . ?item (wdt:P702|wdt:P703) ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS {?item wdt:P31 wd:Q11173} } '
if "yuy" in sys.argv:
    SPARQLSE[
        'Q8054'
    ] = '''SELECT ?item WHERE { ?item wdt:P31 wd:Q8054 .
?item (wdt:P702|wdt:P703) ?constellation.
?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
FILTER NOT EXISTS {?item rdfs:label ?itemar. FILTER((LANG(?itemar)) = "ar") }
FILTER NOT EXISTS {?item wdt:P31 wd:Q11173}  .
} '''
# ---
# حلقة
# Q21191270#Q1983062
SPARQLSE[
    'Q21191270'
] = '''SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q21191270.
    ?item wdt:P179 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
'''
SPARQLSE[
    'Q1983062'
] = '''SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q1983062.
    ?item wdt:P179 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
'''
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q44559
# python3 core8/pwb.py nep/nldes3 sparql:Q44559 nokeep limit:500
#
SPARQLSE[
    'Q44559'
] = """SELECT ?item WHERE {
  ?item wdt:P31 wd:Q44559.
FILTER NOT EXISTS {?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q8502
# python3 core8/pwb.py nep/nldes3 sparql:Q8502 nokeep limit:500
# جبل
SPARQLSE[
    'Q8502'
] = """SELECT ?item WHERE {
  ?item wdt:P31 wd:Q8502; wdt:P17 ?dummy0.
FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q45382
SPARQLSE[
    'Q45382'
] = """SELECT ?item WHERE {
?item wdt:P31 wd:Q45382; wdt:P17 ?dummy0.
FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
}
"""
# ---
'''
python3 core8/pwb.py nep/nldes3 a2r sparql:Q1153690
python3 core8/pwb.py nep/nldes3 a2r sparql:Q115518
python3 core8/pwb.py nep/nldes3 a2r sparql:Q130019
python3 core8/pwb.py nep/nldes3 a2r sparql:Q1332364
python3 core8/pwb.py nep/nldes3 a2r sparql:Q13632
python3 core8/pwb.py nep/nldes3 a2r sparql:Q1457376
python3 core8/pwb.py nep/nldes3 a2r sparql:Q15917122
python3 core8/pwb.py nep/nldes3 a2r sparql:Q204194
python3 core8/pwb.py nep/nldes3 a2r sparql:Q2247863
python3 core8/pwb.py nep/nldes3 a2r sparql:Q318
python3 core8/pwb.py nep/nldes3 a2r sparql:Q44559
python3 core8/pwb.py nep/nldes3 a2r sparql:Q523
python3 core8/pwb.py nep/nldes3 a2r sparql:Q6243
python3 core8/pwb.py nep/nldes3 a2r sparql:Q66619666
python3 core8/pwb.py nep/nldes3 a2r sparql:Q67206691
python3 core8/pwb.py nep/nldes3 a2r sparql:Q71963409
python3 core8/pwb.py nep/nldes3 a2r sparql:Q726242
python3 core8/pwb.py nep/nldes3 a2r sparql:Q72802508
python3 core8/pwb.py nep/nldes3 a2r sparql:Q72803622
'''
# ---
space_list_and_other_2 = {
    'Q96739634': {'ar': "حركة فردية", 'P': 'P50'},
    'Q3331189': {'ar': "طبعة", 'P': 'P629'},
    'Q7187': {'ar': "جين", 'P': 'P703'},
    'Q2467461': {'ar': "قسم أكاديمي", 'P': ''},
    'Q277338': {'ar': "جين كاذب", 'P': 'P703'},
    'Q14752149': {'ar': "نادي كرة قدم للهواة", 'P': ''},
    'Q476028': {'ar': "نادي كرة قدم", 'P': ''},
    'Q620615': {'ar': "تطببيق محمول", 'P': ''},
    'Q783866': {'ar': 'مكتبة جافا سكريبت', 'P': 'P178'},  # 17241
    'Q2831984': {'ar': "ألبوم قصص مصورة", 'P': ''},
    'Q19389637': {'ar': "مقالة سيرة ذاتية", 'P': ''},
    'Q3305213': {'ar': "لوحة فنية", 'P': ''},
    'Q7889': {'ar': "لعبة فيديو", 'P': ''},
    'Q8054': {'ar': "بروتين", 'P': ''},
    # ---
    'Q7278': {'ar': "حزب سياسي", 'P': ''},
}
# ---
for sw in Taton_list:
    if sw not in SPARQLSE:
        # if not sw in SPARQLSE :
        # SPARQLSE[sw] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % sw
        # ---
        # SPARQLSE[sw] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % sw
        # ---
        SPARQLSE[sw] = main_quarry % sw
        # ---
        const = space_list_and_other_2.get(sw, {}).get('P', '')
        # ---
        if "a2r" in sys.argv and const != '':
            gtg = 'SELECT ?item WHERE {'

            gtg += f'''
                ?item wdt:P31 wd:{sw}.
                ?item wdt:{const} ?const.
                '''

            gtg += '''
                FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }
                ?const rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
                }
            '''
            SPARQLSE[sw] = gtg

        if "a3r" in sys.argv:
            gtg = 'SELECT ?item WHERE { ?item wdt:P31 wd:' + sw + '. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } '
            SPARQLSE[sw] = gtg
# ---
for st in Space_tab:
    if st not in SPARQLSE:
        # if SPARQLSE.get( st , '' ) == '' :
        SPARQLSE[st] = (
            '''
SELECT ?item WHERE {
    ?item wdt:P31 wd:%s .
    FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }

    ?item wdt:P59 ?constellation.
    ?constellation wdt:P31 wd:Q8928. # كوكبة
} '''
            % st
        )
        # ---
        if "a2r" in sys.argv:
            SPARQLSE[st] = (
                '''
SELECT ?item WHERE {
    ?item wdt:P31 wd:%s .
    FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }

    ?item wdt:P59 ?constellation.
    ?constellation wdt:P31 wd:Q8928. # كوكبة
    ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
} '''
                % st
            )
        # ---
        if "a3r" in sys.argv:
            SPARQLSE[st] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % st
# ---
# Q11424  فيلم
SPARQLSE['Q11424'] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item wdt:P57 ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % 'Q11424'
# ---
if "a2r" in sys.argv:
    SPARQLSE['Q11424'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . ?item wdt:P57 ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % 'Q11424'
# ---
if "a3r" in sys.argv:
    SPARQLSE['Q11424'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % 'Q11424'
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q27020041
# python3 core8/pwb.py nep/nldes3 sparql:Q27020041 nokeep limit:500
# موسم رياضي
SPARQLSE[
    'Q27020041'
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
if 'optional' in sys.argv:
    SPARQLSE['Q27020041'] = SPARQLSE['Q27020041'].replace('?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .', 'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}')
# ---
# python3 core8/pwb.py nep/nldes3 sparql:Q3231690
# طراز سيارة
SPARQLSE[
    'Q3231690'
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
if 'optional' in sys.argv:
    SPARQLSE['Q3231690'] = SPARQLSE['Q3231690'].replace('?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .', 'optional{?pp rdfs:label ?labe . FILTER((LANG(?labe)) = "ar") .}')
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
SPARQLSE['Q3331189'] = main_quarry_with_proerty % ('Q3331189', 'P629')
if "a2r" in sys.argv:
    SPARQLSE['Q3331189'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:Q3331189. ?item  wdt:P629 ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} '
if "a3r" in sys.argv:
    SPARQLSE['Q3331189'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % 'Q3331189'

# ---
SPARQLSE['Q7889'] = 'SELECT ?item WHERE {?item wdt:P31 wd:%s . ?item  (wdt:P178|wdt:P179) ?constellation. FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % 'Q7889'
if "a2r" in sys.argv:
    SPARQLSE['Q7889'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . ?item (wdt:P178|wdt:P179) ?constellation. ?constellation rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar") FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") }} ' % 'Q7889'
if "a3r" in sys.argv:
    SPARQLSE['Q7889'] = 'SELECT ?item WHERE { ?item wdt:P31 wd:%s . FILTER NOT EXISTS { ?item schema:description ?itemar. FILTER((LANG(?itemar)) = "ar") } } ' % 'Q7889'
# ---python3 core8/pwb.py nep/nldes3 a3r sparql:Q7366
# أغنية
SPARQLSE[
    'Q7366'
] = '''SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q7366.
    ?item wdt:P175 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
'''
# ---
# البلديات
SPARQLSE[
    'Q7366'
] = '''SELECT ?item WHERE
{
    ?item wdt:P31 wd:Q7366.
    ?item wdt:P175 ?eps. ?eps rdfs:label ?a2r. FILTER((LANG(?a2r)) = "ar")
    FILTER NOT EXISTS {?item rdfs:label ?item_ar. FILTER((LANG(?item_ar)) = "ar") }
}
'''
# ---

#!/usr/bin/python3
"""

بوت إضافة الوصوف عن الأشخاص في ويكي بيانات

جميع اللغات

https://github.com/emijrp/wikidata/blob/master/human.descriptions.py

~ lithographer
~ Esperantist
~ ski jumper
~ troubadour
~ bishop

"""

#
# (C) Ibrahem Qasim, 2022
#
#
from pathlib import Path
import json

# ---
Dir = Path(__file__).parent
# ---
translationsOccupations = {}
tra_occ_2 = {
    "~ lyricist": {
        "ar": {"male": "شاعر غنائي ~", "female": "شاعرة غنائية ~"},
        "en": {"male": "~ lyricist", "female": "~ lyricist"},
    },
    "~ imam": {
        "ar": {"male": "إمام ~", "female": ""},
        "en": {"male": "~ imam", "female": ""},
    },
    "~ art historian": {
        "ar": {"male": "مؤرخ فن ~", "female": "مؤرخة فن ~"},
        "bn": {"male": "~ শিল্প ইতিহাসবিদ", "female": "~ শিল্প ইতিহাসবিদ"},
        "ca": {"male": "historiador de l'art ~", "female": "historiadora de l'art ~"},
        "en": {"male": "~ art historian", "female": "~ art historian"},
        "es": {"male": "historiador del arte ~", "female": "historiadora del arte ~"},
        "et": {"male": "~ kunstiajaloolane", "female": "~ kunstiajaloolane"},
        "fr": {"male": "historien de l'art ~", "female": "historienne de l'art ~"},
        "gl": {"male": "historiador da arte ~", "female": "historiadora da arte ~"},
        "he": {"male": "היסטוריון אמנות ~", "female": "היסטוריונית אמנות ~"},
        "ro": {"male": "istoric al artei ~", "female": "istorică ~ a artei"},
        "sq": {"male": "historian ~ i artit", "female": "historiane ~ e artit"},
    },
    "~ university teacher": {
        "ar": {"male": "أستاذ جامعي ~", "female": "أستاذة جامعية ~"},
        "bn": {"male": "~ বিশ্ববিদ্যালয়ের শিক্ষক", "female": "~ বিশ্ববিদ্যালয়ের শিক্ষিকা"},
        "ca": {"male": "professor d'universitat ~", "female": "professora d'universitat ~"},
        "en": {"male": "~ university teacher", "female": "~ university teacher"},
        "es": {"male": "profesor universitario ~", "female": "profesora universitaria ~"},
        "et": {"male": "~ ülikooli õppejõud", "female": "~ ülikooli õppejõud"},
        "fr": {"male": "professeur d'université ~", "female": "professeure d'université ~"},
        "gl": {"male": "profesor universitario ~", "female": "profesora universitaria ~"},
        "he": {"male": "מרצה באוניברסיטה ~", "female": "מרצה באוניברסיטה ~"},
        "ro": {"male": "profesor universitar ~", "female": "profesoară universitară ~"},
        "sq": {"male": "profesor universitar ~", "female": "profesore universitare ~"},
    },
    "~ fencer": {
        "ar": {"male": "مسايف ~", "female": "مسايفة ~"},
        "bn": {"male": "~ অসিক্রীড়াবিদ", "female": "~ অসিক্রীড়াবিদ"},
        "ca": {"male": "tirador d'esgrima ~", "female": "tiradora d'esgrima ~"},
        "en": {"male": "~ fencer", "female": "~ fencer"},
        "es": {"male": "esgrimista ~", "female": "esgrimista ~"},
        "et": {"male": "~ vehkleja", "female": "~ vehkleja"},
        "fr": {"male": "escrimeur ~", "female": "escrimeuse ~"},
        "gl": {"male": "esgrimista ~", "female": "esgrimista ~"},
        "he": {"male": "סייף ~", "female": "סייפת ~"},
        "ro": {"male": "scrimer ~", "female": "scrimeră ~"},
        "sq": {"male": "skermist ~", "female": "skermiste ~"},
    },
    "~ businessperson": {
        "ar": {"male": "رائد أعمال ~", "female": "رائدة أعمال ~"},
        "bn": {"male": "~ ব্যবসায়ী", "female": "~ ব্যবসায়ী"},
        "ca": {"male": "empresari ~", "female": "empresària ~"},
        "en": {"male": "~ businessperson", "female": "~ businessperson"},
        "es": {"male": "empresario ~", "female": "empresaria ~"},
        "et": {"male": "~ ärimees", "female": "~ ärinaine"},
        "fr": {"male": "homme d'affaires ~", "female": "femme d'affaires ~"},
        "gl": {"male": "empresario ~", "female": "empresaria ~"},
        "he": {"male": "איש עסקים ~", "female": "אשת עסקים ~"},
        "ro": {"male": "om de afaceri ~", "female": "femeie de afaceri ~"},
        "sq": {"male": "biznesmen ~", "female": "biznesmene ~"},
    },
    "~ children's writer": {
        "ar": {"male": "كاتب أدب أطفال ~", "female": "كاتبة أدب أطفال ~"},
        "bn": {"male": "~ শিশু সাহিত্যিক", "female": "~ শিশু সাহিত্যিক"},
        "ca": {"male": "escriptor de literatura infantil ~", "female": "escriptora de literatura infantil ~"},
        "en": {"male": "~ children's writer", "female": "~ children's writer"},
        "es": {"male": "escritor de literatura infantil ~", "female": "escritora de literatura infantil ~"},
        "et": {"male": "~ lastekirjanik", "female": "~ lastekirjanik"},
        "fr": {"male": "auteur de littérature d'enfance ~", "female": "auteure de littérature d'enfance ~"},
        "gl": {"male": "escritor de literatura infantil ~", "female": "escritora de literatura infantil ~"},
        "he": {"male": "סופר ילדים ~", "female": "סופרת ילדים ~"},
        "ro": {"male": "scriitor de literatură pentru copii ~", "female": "scriitoare de literatură pentru copii ~"},
        "sq": {"male": "shkrimtar për fëmijë ~", "female": "shkrimtare për fëmijë ~"},
    },
}
# ---
with open(f"{Dir}/translationsOccupations.json", "r", encoding="utf-8") as f:
    translationsOccupations = json.load(f)
# ---
translationsOccupations.update(tra_occ_2)
# ---
translationsOccupations_new = {
    "~ Indigenous artist": {
        "ar": {"male": "فنان سكان أصليون ~", "female": "فنانة سكان أصليون ~"},
        "en": {"male": "~ Indigenous artist", "female": "~ Indigenous artist"},
    },
    "~ papyrologist": {
        "ar": {"male": "عالم برديات ~", "female": "عالمة برديات ~"},
        "en": {"male": "~ papyrologist", "female": "~ papyrologist"},
    },
    "~ former military officer": {
        "ar": {"male": "ضابط عسكري سابق ~", "female": "ضابطة عسكرية سابقة ~"},
        "en": {"male": "~ former military officer", "female": "~ former military officer"},
    },
    "~ researcher": {
        "ar": {"male": "باحث ~", "female": "باحثة ~"},
        "en": {"male": "~ researcher", "female": "~ researcher"},
    },
    "~ sprinter": {
        "ar": {"male": "عداء سريع ~", "female": "عدائة سريعة ~"},
        "en": {"male": "~ sprinter", "female": "~ sprinter"},
    },
    "~ military officer": {
        "ar": {"male": "ضابط عسكري ~", "female": "ضابطة عسكرية ~"},
        "en": {"male": "~ military officer", "female": "~ military officer"},
    },
    "~ medievalist": {
        "ar": {"male": "مختص في الدراسات القروسطية ~", "female": "مختصة في الدراسات القروسطية ~"},
        "en": {"male": "~ medievalist", "female": "~ medievalist"},
        "es": {"male": "medievalista ~", "female": "medievalista ~"},
    },
    "~ philologist": {
        "ar": {"male": "فقيه لغة ~", "female": "فقيهة لغة ~"},
        "en": {"male": "~ philologist", "female": "~ philologist"},
        "es": {"male": "filólogo ~", "female": "filóloga ~"},
    },
    "~ physiologist": {
        "ar": {"male": "عالم وظائف الأعضاء ~", "female": "عالمة وظائف الأعضاء ~"},
        "en": {"male": "~ physiologist", "female": "~ physiologist"},
        "es": {"male": "fisiólogo ~", "female": "fisióloga ~"},
    },
    "~ political scientist": {
        "ar": {"male": "عالم سياسة ~", "female": "عالمة سياسة ~"},
        "en": {"male": "~ political scientist", "female": "~ political scientist"},
        "es": {"male": "politólogo ~", "female": "politóloga ~"},
    },
    "~ psychoanalyst": {
        "ar": {"male": "معالج نفسي ~", "female": "معالجة نفسية ~"},
        "en": {"male": "~ psychoanalyst", "female": "~ psychoanalyst"},
        "es": {"male": "psicoanalista ~", "female": "psicoanalista ~"},
    },
    "~ psychiatrist": {
        "ar": {"male": "طبيب نفسي ~", "female": "طبيبة نفسية ~"},
        "en": {"male": "~ psychiatrist", "female": "~ psychiatrist"},
        "es": {"male": "psiquiatra ~", "female": "psiquiatra ~"},
    },
    "~ psychologist": {
        "ar": {"male": "عالم نفس ~", "female": "عالمة نفس ~"},
        "en": {"male": "~ psychologist", "female": "~ psychologist"},
        "es": {"male": "psicólogo ~", "female": "psicóloga ~"},
    },
    "~ racing driver": {
        "ar": {"male": "سائق سباق ~", "female": "سائقة سباق ~"},
        "en": {"male": "~ racing driver", "female": "~ racing driver"},
        "es": {"male": "piloto de automovilismo ~", "female": "piloto de automovilismo ~"},
    },
    "~ basketball coach": {
        "ar": {"male": "مدرب كرة سلة ~", "female": "مدربة كرة سلة ~"},
        "en": {"male": "~ basketball coach", "female": "~ basketball coach"},
        "es": {"male": "entrenador de baloncesto ~", "female": "entrenadora de baloncesto ~"},
    },
    "~ violinist": {
        "ar": {"male": "عازف كمان ~", "female": "عازفة كمان ~"},
        "en": {"male": "~ violinist", "female": "~ violinist"},
        "es": {"male": "violinista ~", "female": "violinista ~"},
    },
    "~ virologist": {
        "ar": {"male": "عالم فيروسات ~", "female": "عالمة فيروسات ~"},
        "en": {"male": "~ virologist", "female": "~ virologist"},
        "es": {"male": "virólogo ~", "female": "viróloga ~"},
    },
    "~ rally driver": {
        "ar": {"male": "سائق رالي ~", "female": "سائقة رالي ~"},
        "en": {"male": "~ rally driver", "female": "~ rally driver"},
        "es": {"male": "piloto de rally ~", "female": "piloto de rally ~"},
    },
    "~ bishop": {
        # 'ar': { 'male': 'أسقف ~', 'female': 'أسقف ~' },
        "en": {"male": "~ bishop", "female": "~ bishop"},
        "es": {"male": "obispo ~", "female": "obispo ~"},
    },
    "~ pathologist": {
        "ar": {"male": "عالم أمراض ~", "female": "عالمة أمراض ~"},
        "en": {"male": "~ pathologist", "female": "~ pathologist"},
        "es": {"male": "patólogo ~", "female": "patóloga ~"},
    },
    "~ pharmacologist": {
        "ar": {"male": "عالم صيدلية ~", "female": "عالمة صيدلية ~"},
        "en": {"male": "~ pharmacologist", "female": "~ pharmacologist"},
        "es": {"male": "farmacólogo ~", "female": "farmacóloga ~"},
    },
    "~ rapper": {
        "ar": {"male": "رابر ~", "female": "مغنية راب ~"},
        "en": {"male": "~ rapper", "female": "~ rapper"},
        "es": {"male": "rapero ~", "female": "rapera ~"},
    },
    "~ saxophonist": {
        "ar": {"male": "عازف ساكسفون ~", "female": "عازفة ساكسفون ~"},
        "en": {"male": "~ saxophonist", "female": "~ saxophonist"},
        "es": {"male": "saxofonista ~", "female": "saxofonista ~"},
    },
    "~ scientist": {
        "ar": {"male": "عالم ~", "female": "عالمة ~"},
        "en": {"male": "~ scientist", "female": "~ scientist"},
        "es": {"male": "científico ~", "female": "científica ~"},
    },
    "~ singer-songwriter": {
        "ar": {"male": "مغن مؤلف ~", "female": "مغنية ومؤلفة ~"},
        "en": {"male": "~ singer-songwriter", "female": "~ singer-songwriter"},
        "es": {"male": "cantautor ~", "female": "cantautora ~"},
    },
    "~ radiologist": {
        "ar": {"male": "أخصائي أشعة ~", "female": "أخصائية أشعة ~"},
        "en": {"male": "~ radiologist", "female": "~ radiologist"},
        "es": {"male": "radiólogo ~", "female": "radióloga ~"},
    },
    "~ theatre director": {
        "ar": {"male": "مخرج مسرح ~", "female": "مخرجة مسرح ~"},
        "en": {"male": "~ theatre director", "female": "~ theatre director"},
        "es": {"male": "director de teatro ~", "female": "directora de teatro ~"},
    },
    "~ ski jumper": {
        "en": {"male": "~ ski jumper", "female": "~ ski jumper"},
        "es": {"male": "saltador de esquí ~", "female": "saltadora de esquí ~"},
    },
    "~ ethnologist": {
        "ar": {"male": "عالم أثنولوجيا ~", "female": "عالمة أثنولوجيا ~"},
        "en": {"male": "~ ethnologist", "female": "~ ethnologist"},
        "es": {"male": "etnólogo ~", "female": "etnóloga ~"},
    },
    "~ Esperantist": {
        "en": {"male": "~ Esperantist", "female": "~ Esperantist"},
        "es": {"male": "esperantista ~", "female": "esperantista ~"},
    },
    "~ lithographer": {
        "en": {"male": "~ lithographer", "female": "~ lithographer"},
        "es": {"male": "litógrafo ~", "female": "litógrafa ~"},
    },
    "~ handball player": {
        "ar": {"male": "لاعب كرة يد ~", "female": "لاعبة كرة يد ~"},
        "en": {"male": "~ handball player", "female": "~ handball player"},
        "es": {"male": "balonmanista ~", "female": "balonmanista ~"},
    },
    "~ geographer": {
        "ar": {"male": "جغرافي ~", "female": "جغرافية ~"},
        "en": {"male": "~ geographer", "female": "~ geographer"},
        "es": {"male": "geógrafo ~", "female": "geógrafa ~"},
    },
    "~ geologist": {
        "ar": {"male": "جيولوجي ~", "female": "جيولوجية ~"},
        "en": {"male": "~ geologist", "female": "~ geologist"},
        "es": {"male": "geólogo ~", "female": "geóloga ~"},
    },
    "~ theologian": {
        "ar": {"male": "عالم عقيدة ~", "female": "عالمة عقيدة ~"},
        "en": {"male": "~ theologian", "female": "~ theologian"},
        "es": {"male": "teólogo ~", "female": "teóloga ~"},
    },
    "~ volleyball player": {
        "ar": {"male": "لاعب كرة طائرة ~", "female": "لاعبة كرة طائرة ~"},
        "en": {"male": "~ volleyball player", "female": "~ volleyball player"},
        "es": {"male": "jugador de voleibol ~", "female": "jugadora de voleibol ~"},
    },
    "~ water polo player": {
        "ar": {"male": "لاعب كرة ماء ~", "female": "لاعبة كرة ماء ~"},
        "en": {"male": "~ water polo player", "female": "~ water polo player"},
        "es": {"male": "jugador de waterpolo ~", "female": "jugadora de waterpolo ~"},
    },
    "~ zoologist": {
        "ar": {"male": "عالم حيوانات ~", "female": "عالمة حيوانات ~"},
        "en": {"male": "~ zoologist", "female": "~ zoologist"},
        "es": {"male": "zoólogo ~", "female": "zoóloga ~"},
    },
    "~ archivist": {
        "ar": {"male": "أمين أرشيف ~", "female": "أمينة أرشيف ~"},
        "en": {"male": "~ archivist", "female": "~ archivist"},
        "es": {"male": "archivero ~", "female": "archivera ~"},
    },
    "~ rower": {
        "ar": {"male": "مجدف ~", "female": "مجدفة ~"},
        "en": {"male": "~ rower", "female": "~ rower"},
        "es": {"male": "remero ~", "female": "remera ~"},
    },
    "~ snowboarder": {
        "ar": {"male": "متزلج ثلجي ~", "female": "متزلجة ثلجية ~"},
        "en": {"male": "~ snowboarder", "female": "~ snowboarder"},
        "es": {"male": "snowboarder ~", "female": "snowboarder ~"},
    },
    "~ speleologist": {
        "ar": {"male": "عالم كهوف ~", "female": "عالمة كهوف ~"},
        "en": {"male": "~ speleologist", "female": "~ speleologist"},
        "es": {"male": "espeleólogo ~", "female": "espeleóloga ~"},
    },
    "~ spy": {
        "ar": {"male": "جاسوس ~", "female": "جاسوسة ~"},
        "en": {"male": "~ spy", "female": "~ spy"},
        "es": {"male": "espía ~", "female": "espía ~"},
    },
    "~ trade unionist": {
        "ar": {"male": "نقابي ~", "female": "نقابية ~"},
        "en": {"male": "~ trade unionist", "female": "~ trade unionist"},
        "es": {"male": "sindicalista ~", "female": "sindicalista ~"},
    },
    "~ troubadour": {
        "en": {"male": "~ troubadour", "female": "~ troubadour"},
        "es": {"male": "trovador ~", "female": "trovadora ~"},
    },
    "~ veterinarian": {
        "ar": {"male": "طبيب بيطري ~", "female": "طبيبة بيطرية ~"},
        "en": {"male": "~ veterinarian", "female": "~ veterinarian"},
        "es": {"male": "veterinario ~", "female": "veterinaria ~"},
    },
    "~ surgeon": {
        "ar": {"male": "جراح ~", "female": "جراحة ~"},
        "en": {"male": "~ surgeon", "female": "~ surgeon"},
        "es": {"male": "cirujano ~", "female": "cirujana ~"},
    },
    "~ academic": {
        "ar": {"male": "أكاديمي ~", "female": "أكاديمية ~"},
        "en": {"male": "~ academic", "female": "~ academic"},
        "es": {"male": "académico ~", "female": "académica ~"},
    },
    "~ archduke": {
        "ar": {"male": "أرشيدوق ~", "female": "أرشيدوقة ~"},
        "en": {"male": "~ archduke", "female": "~ archduke"},
    },
    "~ alpine skier": {
        "ar": {"male": "متزحلق منحدرات ثلجية ~", "female": "متزحلقة منحدرات ثلجية ~"},
        "en": {"male": "~ alpine skier", "female": "~ alpine skier"},
        "es": {"male": "esquiador alpino ~", "female": "esquiadora alpina ~"},
    },
    "~ cross-country skier": {
        "ar": {"male": "متزلج ريفي ~", "female": "متزلجة ريفية ~"},
        "en": {"male": "~ cross-country skier", "female": "~ cross-country skier"},
        "es": {"male": "esquiador de fondo ~", "female": "esquiadora de fondo ~"},
    },
    "~ chess player": {
        "ar": {"male": "لاعب شطرنج ~", "female": "لاعبة شطرنج ~"},
        "en": {"male": "~ chess player", "female": "~ chess player"},
        "es": {"male": "ajedrecista ~", "female": "ajedrecista ~"},
    },
    "~ caricaturist": {
        "ar": {"male": "رسام كاريكاتير ~", "female": "رسامة كاريكاتير ~"},
        "en": {"male": "~ caricaturist", "female": "~ caricaturist"},
        "es": {"male": "caricaturista ~", "female": "caricaturista ~"},
    },
    "~ chef": {
        "ar": {"male": "طباخ ~", "female": "طباخة ~"},
        "en": {"male": "~ chef", "female": "~ chef"},
        "es": {"male": "chef ~", "female": "chef ~"},
    },
    "~ boxer": {
        "ar": {"male": "ملاكم ~", "female": "ملاكمة ~"},
        "en": {"male": "~ boxer", "female": "~ boxer"},
        "es": {"male": "boxeador ~", "female": "boxeadora ~"},
    },
    "~ cartographer": {
        "ar": {"male": "عالم خرائط ~", "female": "عالمة خرائط ~"},
        "en": {"male": "~ cartographer", "female": "~ cartographer"},
        "es": {"male": "cartógrafo ~", "female": "cartógrafa ~"},
    },
    "~ dermatologist": {
        "ar": {"male": "طبيب أمراض جلدية ~", "female": "طبيبة أمراض جلدية ~"},
        "en": {"male": "~ dermatologist", "female": "~ dermatologist"},
        "es": {"male": "dermatólogo ~", "female": "dermatóloga ~"},
    },
    "~ biathlete": {
        "ar": {"male": "لاعب بياثلون ~", "female": "لاعبة بياثلون ~"},
        "en": {"male": "~ biathlete", "female": "~ biathlete"},
        "es": {"male": "biatleta ~", "female": "biatleta ~"},
    },
    "~ ice hockey player": {
        "ar": {"male": "لاعب هوكي الجليد ~", "female": "لاعبة هوكي الجليد ~"},
        "en": {"male": "~ ice hockey player", "female": "~ ice hockey player"},
        "es": {"male": "jugador de hockey sobre hielo ~", "female": "jugadora de hockey sobre hielo ~"},
    },
    "~ field hockey player": {
        "ar": {"male": "لاعب هوكي الحقل ~", "female": "لاعبة هوكي الحقل ~"},
        "en": {"male": "~ field hockey player", "female": "~ field hockey player"},
        "es": {"male": "jugador de hockey sobre hierba ~", "female": "jugadora de hockey sobre hierba ~"},
    },
    "~ geneticist": {
        "ar": {"male": "عالم وراثة ~", "female": "عالمة وراثة ~"},
        "en": {"male": "~ geneticist", "female": "~ geneticist"},
        "es": {"male": "genetista ~", "female": "genetista ~"},
    },
    "~ guitarist": {
        "ar": {"male": "عازف قيثارة ~", "female": "عازفة قيثارة ~"},
        "en": {"male": "~ guitarist", "female": "~ guitarist"},
        "es": {"male": "guitarrista ~", "female": "guitarrista ~"},
    },
    "~ gymnast": {
        "ar": {"male": "لاعب جمباز ~", "female": "لاعبة جمباز ~"},
        "en": {"male": "~ gymnast", "female": "~ gymnast"},
        "es": {"male": "gimnasta ~", "female": "gimnasta ~"},
    },
    "~ gynaecologist": {
        "ar": {"male": "أخصائي أمراض نسائية ~", "female": "أخصائية أمراض نسائية ~"},
        "en": {"male": "~ gynaecologist", "female": "~ gynaecologist"},
        "es": {"male": "ginecólogo ~", "female": "ginecóloga ~"},
    },
    "~ judoka": {
        "ar": {"male": "لاعب جودو ~", "female": "لاعبة جودو ~"},
        "en": {"male": "~ judoka", "female": "~ judoka"},
        "es": {"male": "yudoca ~", "female": "yudoca ~"},
    },
    "~ legal historian": {
        "ar": {"male": "مؤرخ قانون ~", "female": "مؤرخة قانون ~"},
        "en": {"male": "~ legal historian", "female": "~ legal historian"},
        "es": {"male": "historiador del derecho ~", "female": "historiadora del derecho ~"},
    },
    "~ librarian": {
        "ar": {"male": "أمين مكتبة ~", "female": "أمينة مكتبة ~"},
        "en": {"male": "~ librarian", "female": "~ librarian"},
        "es": {"male": "bibliotecario ~", "female": "bibliotecaria ~"},
    },
    "~ linguist": {
        "ar": {"male": "لغوي ~", "female": "لغوية ~"},
        "en": {"male": "~ linguist", "female": "~ linguist"},
        "es": {"male": "lingüista ~", "female": "lingüista ~"},
    },
    "~ literary critic": {
        "ar": {"male": "ناقد أدبي ~", "female": "ناقدة أدبية ~"},
        "en": {"male": "~ literary critic", "female": "~ literary critic"},
        "es": {"male": "crítico literario ~", "female": "crítica literaria ~"},
    },
    "~ association football referee": {
        "ar": {"male": "حكم كرة قدم ~", "female": "حكمة كرة قدم ~"},
        "en": {"male": "~ association football referee", "female": "~ association football referee"},
        "es": {"male": "árbitro de fútbol ~", "female": "árbitra de fútbol ~"},
    },
    "~ anatomist": {
        "ar": {"male": "عالم تشريح ~", "female": "عالمة تشريح ~"},
        "en": {"male": "~ anatomist", "female": "~ anatomist"},
        "es": {"male": "anatomista ~", "female": "anatomista ~"},
    },
    "~ anthropologist": {
        "ar": {"male": "عالم أنثروبولوجيا ~", "female": "عالمة أنثروبولوجيا ~"},
        "en": {"male": "~ anthropologist", "female": "~ anthropologist"},
        "es": {"male": "antropólogo ~", "female": "antropóloga ~"},
    },
    "~ archaeologist": {
        "ar": {"male": "عالم آثار ~", "female": "عالمة آثار ~"},
        "en": {"male": "~ archaeologist", "female": "~ archaeologist"},
        "es": {"male": "arqueólogo ~", "female": "arqueóloga ~"},
    },
    "~ archer": {
        "ar": {"male": "نبال ~", "female": "نبالة ~"},
        "en": {"male": "~ archer", "female": "~ archer"},
        "es": {"male": "arquero ~", "female": "arquera ~"},
    },
    "~ biologist": {
        "ar": {"male": "عالم أحياء ~", "female": "عالمة أحياء ~"},
        "en": {"male": "~ biologist", "female": "~ biologist"},
        "es": {"male": "biólogo ~", "female": "bióloga ~"},
    },
    "~ egyptologist": {
        "ar": {"male": "عالم مصريات ~", "female": "عالمة مصريات ~"},
        "en": {"male": "~ egyptologist", "female": "~ egyptologist"},
        "es": {"male": "egiptólogo ~", "female": "egiptóloga ~"},
    },
    "~ film critic": {
        "ar": {"male": "ناقد أفلام ~", "female": "ناقدة أفلام ~"},
        "en": {"male": "~ film critic", "female": "~ film critic"},
        "es": {"male": "crítico de cine ~", "female": "crítica de cine ~"},
    },
    "~ flying ace": {
        "ar": {"male": "طيار عسكري ~", "female": "قائدة طيارة عسكرية ~"},
        "en": {"male": "~ flying ace", "female": "~ flying ace"},
        "es": {"male": "as de la aviación ~", "female": "as de la aviación ~"},
    },
    "~ mineralogist": {
        "ar": {"male": "عالم معادن ~", "female": "عالمة معادن ~"},
        "en": {"male": "~ mineralogist", "female": "~ mineralogist"},
        "es": {"male": "mineralogista ~", "female": "mineralogista ~"},
    },
    "~ missionary": {
        "ar": {"male": "مبشر ~", "female": "مبشرة ~"},
        "en": {"male": "~ missionary", "female": "~ missionary"},
        "es": {"male": "misionero ~", "female": "misionera ~"},
    },
    "~ motorcycle racer": {
        "ar": {"male": "متسابق دراجات نارية ~", "female": "متسابقة دراجات نارية ~"},
        "en": {"male": "~ motorcycle racer", "female": "~ motorcycle racer"},
        "es": {"male": "piloto de motociclismo ~", "female": "piloto de motociclismo ~"},
    },
    "~ musicologist": {
        "ar": {"male": "عالم موسيقي ~", "female": "عالمة موسيقي ~"},
        "en": {"male": "~ musicologist", "female": "~ musicologist"},
        "es": {"male": "musicólogo ~", "female": "musicóloga ~"},
    },
    "~ mycologist": {
        "ar": {"male": "أخصائي فطريات ~", "female": "أخصائية فطريات ~"},
        "en": {"male": "~ mycologist", "female": "~ mycologist"},
        "es": {"male": "micólogo ~", "female": "micóloga ~"},
    },
    "~ naturalist": {
        "ar": {"male": "عالم طبيعة ~", "female": "عالمة طبيعة ~"},
        "en": {"male": "~ naturalist", "female": "~ naturalist"},
        "es": {"male": "naturalista ~", "female": "naturalista ~"},
    },
    "~ neurologist": {
        "ar": {"male": "طبيب أعصاب ~", "female": "طبيبة أعصاب ~"},
        "en": {"male": "~ neurologist", "female": "~ neurologist"},
        "es": {"male": "neurólogo ~", "female": "neuróloga ~"},
    },
    "~ essayist": {
        "ar": {"male": "كاتب مقالات ~", "female": "كاتبة مقالات ~"},
        "en": {"male": "~ essayist", "female": "~ essayist"},
        "es": {"male": "ensayista ~", "female": "ensayista ~"},
    },
    "~ engraver": {
        "ar": {"male": "نقاش ~", "female": "نقاشة ~"},
        "en": {"male": "~ engraver", "female": "~ engraver"},
        "es": {"male": "grabador ~", "female": "grabadora ~"},
    },
    "~ oncologist": {
        "ar": {"male": "طبيب أورام ~", "female": "طبيبة أورام ~"},
        "en": {"male": "~ oncologist", "female": "~ oncologist"},
        "es": {"male": "oncólogo ~", "female": "oncóloga ~"},
    },
    "~ opera singer": {
        "ar": {"male": "فنان أوبرا ~", "female": "فنانة أوبرا ~"},
        "en": {"male": "~ opera singer", "female": "~ opera singer"},
        "es": {"male": "cantante de ópera ~", "female": "cantante de ópera ~"},
    },
    "~ ophthalmologist": {
        "ar": {"male": "طبيب عيون ~", "female": "طبيبة عيون ~"},
        "en": {"male": "~ ophthalmologist", "female": "~ ophthalmologist"},
        "es": {"male": "oftalmólogo ~", "female": "oftalmóloga ~"},
    },
    "~ organist": {
        "ar": {"male": "عازف أورغن ~", "female": "عازفة أورغن ~"},
        "en": {"male": "~ organist", "female": "~ organist"},
        "es": {"male": "organista ~", "female": "organista ~"},
    },
    "~ orientalist": {
        "ar": {"male": "مستشرق ~", "female": "مستشرقة ~"},
        "en": {"male": "~ orientalist", "female": "~ orientalist"},
        "es": {"male": "orientalista ~", "female": "orientalista ~"},
    },
    "~ ornithologist": {
        "ar": {"male": "عالم طيور ~", "female": "عالمة طيور ~"},
        "en": {"male": "~ ornithologist", "female": "~ ornithologist"},
        "es": {"male": "ornitólogo ~", "female": "ornitóloga ~"},
    },
}
# ---
translations_all = {**translationsOccupations, **translationsOccupations}
# ---
# for x in translationsOccupations:
# if "ar" not in translationsOccupations[x]:
# print( x )
# ---
for x, yy in translationsOccupations_new.items():
    if "ar" in yy:
        translationsOccupations[x] = yy
    translations_all[x] = yy
# ---
"""
from stub.list import tempse_all
# ---
arl = {}
for x in tempse_all:
    arl[x.strip().lower()] = tempse_all[x]["ar"]
# ---
for x in New_Keys_occ:
    if "ar" not in translationsOccupations[x]:
        x2 = x.replace("~","").strip().lower()
        ar2 = arl.get(x2)
        if ar2:
            print( "        '%s': {" % x )
            print("            'ar': { 'male': '%s ~', 'female': '%s ~' },\n" % ( ar2 , ar2 ) )
# ---
"""

# ---
for yy in translationsOccupations.values():
    if "ar" in yy and yy["ar"]["male"] == yy["ar"]["female"]:
        print(f" male:{yy['ar']['male']} == female")
# ---

# ---

if __name__ == "__main__":
    # python3 core8/pwb.py people/occupationsall
    for k in translationsOccupations.keys():
        print(f'\t"{k}" : "",')

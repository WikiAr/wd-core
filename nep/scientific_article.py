#!/usr/bin/python3
"""

from nep.scientific_article import make_scientific_article

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import dateutil.parser

# ---
from nep.bots.helps import Get_P_API_time
from API import printe
from desc_dicts.scientific_article_desc import Scientific_descraptions
# ---
Desc_Just_year = {
    "zh": "%s年学术文章",  # 年论文
    # ---
    "zh-hant": "%s年學術文章",  # 年論文
    # ---
    "ja": "%s年の論文",
    "ko": "%s년 논문",
    "nan": "%s nî lūn-bûn",
}
# ---
Desc_Just_year["yue"] = Desc_Just_year["zh-hant"]
# ---
Desc_Just_year["zh-hans"] = Desc_Just_year["zh"]
Desc_Just_year["wuu"] = Desc_Just_year["zh"]
# ---
"""
# ---
"zh":"%s年论文",
"zh-hans":"%s年论文",
"zh-cn":"%s年论文",
"zh-sg":"%s年论文",
"zh-my":"%s年论文",
"wuu":"%s年论文",
# ---
"zh-hant":"%s年學術文章",#年論文
"zh-hk":"%s年論文",
"zh-mo":"%s年論文",
"zh-tw":"%s年論文",
"yue":"%s年論文",
# ---
"""
# ---
pubtxt = {
    "ar": "نشرت في",
    "de": "veröffentlicht",
    "da": "udgivet",
    "en": "published on",
    "fr": "publié",
    "it": "pubblicato il",
    "nl": "gepubliceerd op",
    "pt": "publicado na",
    "sr": "објављен",
    "sv": "publicerad på",
    "tr": "günü yayınlanan",
    "ca": "publicat el",
    "cs": "publikovaný v roce",
    "sk": "publikovaný",
}
# ---
Month_Table = {
    "ar": {
        "1": "يناير",
        "2": "فبراير",
        "3": "مارس",
        "4": "أبريل",
        "5": "مايو",
        "6": "يونيو",
        "7": "يوليو",
        "8": "أغسطس",
        "9": "سبتمبر",
        "10": "أكتوبر",
        "11": "نوفمبر",
        "12": "ديسمبر",
    },
    "en": {
        "1": "January",
        "2": "February",
        "3": "March",
        "4": "April",
        "5": "May",
        "6": "June",
        "7": "July",
        "8": "August",
        "9": "September",
        "10": "October",
        "11": "November",
        "12": "December",
    },
    "bn": {
        "1": "জানুয়ারি",
        "2": "ফেব্রুয়ারি",
        "3": "মার্চ",
        "4": "এপ্রিল",
        "5": "মে",
        "6": "জুন",
        "7": "জুলাই",
        "8": "আগস্ট",
        "9": "সেপ্টেম্বর",
        "10": "অক্টোবর",
        "11": "নভেম্বর",
        "12": "ডিসেম্বর",
    },
    "da": {  # Danish description : [[Topic:Van4tumqajysbq2g]]
        "1": "januar",
        "2": "februar",
        "3": "marts",
        "4": "april",
        "5": "maj",
        "6": "juni",
        "7": "juli",
        "8": "august",
        "9": "september",
        "10": "oktober",
        "11": "november",
        "12": "december",
    },
    "uk": {
        "1": "в січні",
        "2": "в лютому",
        "3": "в березні",
        "4": "у квітні",
        "5": "в травні",
        "6": "в червні",
        "7": "в липні",
        "8": "в серпні",
        "9": "у вересні",
        "10": "в жовтні",
        "11": "в листопаді",
        "12": "в грудні",
    },
}
# ---
format_l = {
    "da": "videnskabelig artikel udgivet %s",
    # 'ar' : "مقالة علمية نشرت في %s",
    "ar": "مقالة بحثية نشرت في %s",
    "uk": "наукова стаття, опублікована %s",
    "en": "scientific article published in %s",
    "es": "artículo científico publicado en %s",
    "bn": "%s-এ প্রকাশিত বৈজ্ঞানিক নিবন্ধ",
}
JustYear = [
    "zh",
    "zh-hans",
    "zh-cn",
    "zh-sg",
    "zh-my",
    "wuu",
    "zh-hant",
    "zh-hk",
    "zh-mo",
    "zh-tw",
    "yue",
    "ja",
    "ko",
    "nan",
]


def bnyear(date):
    digits = {
        "0": "০",
        "1": "১",
        "2": "২",
        "3": "৩",
        "4": "৪",
        "5": "৫",
        "6": "৬",
        "7": "৭",
        "8": "৮",
        "9": "৯",
    }
    date = str(date)
    for k, v in digits.items():
        date = re.sub(k, v, date)
    return date


def Monthname(lang, month):
    if month not in ["10", "11", "12"]:
        month = re.sub(r"0", "", month)
    # ---
    # if lang == "bn":
    # return month
    # ---
    if lang in Month_Table and month in Month_Table[lang]:
        # printe.output(Month_Table[lang][month])
        return Month_Table[lang][month]
    # else:
    # printe.output( 'Monthname' )
    # ---
    return False


def Make_uk_desc(desc):
    return desc


def fixdate(date):
    table = {"year": "", "month": "", "day": ""}
    date = re.sub(r"\+0000000", "+", date)
    # date = date.split('T')[0]
    # printe.output(date)
    try:
        date1 = date.split("T")[0].split("+")[1]
        # printe.output(date1)
        date1 = dateutil.parser.parse(date1)
        table["year"], table["month"], table["day"] = (
            str(date1.year),
            str(date1.month),
            str(date1.day),
        )
    except BaseException:
        try:
            date1 = date.split("T")[0].split("+")[1]
            # printe.output(date1)
            year, sep, mo = date1.partition("-")
            month, sep2, day = mo.partition("-")
            table["year"], table["month"], table["day"] = year, month, day
        except BaseException:
            printe.output(date)
            printe.output("<<lightred>> fixdate ??:")
    # printe.output(table)
    return table


def make_scientific_desc(lang, date, precision):
    # year, sep, mo = date.partition('-')
    # month, sep2, day = mo.partition('-')
    # date = date.split('Z')[0].split('+')[1]
    # date = dateutil.parser.parse(date)
    # year , month , day = str(date.year) ,str(date.month) , str(date.day)
    year, month, day = date["year"], date["month"], date["day"]
    # _Year , _Day = year, day
    Correctdate = True
    Full_Date = False
    date2 = year
    desc = ""
    # ---
    if month not in ["10", "11", "12"]:
        month = re.sub(r"0", "", month)
    # ---
    if day == "01":
        day = "1"
    # ---
    # إذا لم يوجد في التاريخ سنة
    if re.sub(r"\d\d\d\d", "", year) != "":
        Correctdate = False
        printe.output(f"<<lightred>> year:{year}, month:{month}, day:{day}")
        printe.output("<<lightred>> unCorrect date:")
    if Month_name := Monthname(lang, month):
        # printe.output( 'year:%s, month:%s, day:%s' % (year , month, day)   )
        precision = int(precision)
        # ---
        if lang == "uk":
            if day == "01" or day == "1" or precision == 10 or precision == 11:
                date2 = f"{Month_name} {year}"
                # printe.output( 'uk date2:"%s"' % date2 )
        elif day == "01" or day == "1" or precision == 10:
            date2 = f"{Month_name} {year}"
        elif precision == 11:
            date2 = f"{day} {Month_name} {year}"
            if lang == "da":
                date2 = f"{day}. {Month_name} {year}"
            Full_Date = True
    # ---
    # إضافة وصف مع التاريخ
    # if Correctdate:
    if Correctdate and lang in JustYear and lang in Desc_Just_year:
        # ---
        # السنة فقط للغات الصينية وما شابهها
        # desc = year + '' + Desc_Just_year[lang]    #بدون فاصلة
        desc = Desc_Just_year[lang] % str(year)
    # ---
    # إضافة وصف مطول
    elif date2 and lang in format_l:
        desc = format_l[lang] % str(date2)
        # ---
        # تعديل الوصف الإنجليزي عند وجود تاريخ كامل
        if Full_Date and lang in ["en", "en-gb", "en-ca"]:
            desc = f"scientific article published on {str(date2)}"
    # ---
    # إضافة وصف عادي
    elif year and lang in Desc_Just_year:
        desc = Desc_Just_year[lang] % year
    # ---
    # إضافة وصف عادي
    elif lang in Scientific_descraptions:
        desc = Scientific_descraptions[lang]
    # ---
    if Correctdate and lang == "bn":
        # _Year , _Day = bnyear(year), bnyear(day)
        # تعديل التاريخ للغة bn
        desc = bnyear(desc)
    # ---
    # wikidata.org/w/index.php?title=Topic:Unt80qci751n0t84
    # وصف uk لسنة دون أشهر
    if lang == "uk" and desc == f"наукова стаття, опублікована {year}":
        desc = "наукова стаття"
        if year.startswith("1"):
            desc = f"наукова стаття, опублікована в {year}"
        elif year.startswith("2"):
            desc = f"наукова стаття, опублікована у {year}"
            # printe.output( 'uk date2:"%s"' % date2 )
    # ---
    # if lang == "uk":
    # _Year , _Day = bnyear(year), bnyear(day)
    # تعديل التاريخ للغة bn
    # printe.output(desc)#
    # desc = Make_uk_desc(desc)
    # printe.output(desc)#
    # return fafa
    # ---

    # ---
    # printe.output(desc)#
    return desc


def make_scientific_article(item, p31, num, TestTable=False):
    # ---
    tablem = {"descriptions": {}, "qid": "", "fixlang": []}
    # ---
    q = item["q"]
    printe.output("<<lightyellow>> **%d: make_scientific_article: %s" % (num, q))
    # ---
    if p31 != "Q13442814":
        printe.output(
            "<<lightred>> make_scientific_article: can't make desc p31 != Q13442814"
        )
        return tablem
    # ---
    precision = ""
    item_descriptions = item.get("descriptions", {})
    # printe.output( item_descriptions )
    P577 = Get_P_API_time(item, "P577")
    pubdate = {}
    if P577:
        pubdate = fixdate(P577["time"])
        # pubdate = P577['time'].split('Z')[0].split('+0000000')[1]
        # pubdate = dateutil.parser.parse(pubdate)
        #
        if "precision" in P577:
            precision = P577["precision"]
    else:
        print(" no P577. ")
        return tablem
    # ---
    # printe.output('pubdate : ' + str(pubdate) )
    translations = {}
    # ---
    for lang in Scientific_descraptions.keys():
        if desc := make_scientific_desc(lang, pubdate, precision):
            translations[lang] = desc
    # ---
    if TestTable:
        printe.output(f'<<lightgreen>> {translations["en"]}:{translations["da"]}')
        printe.output(translations["en"])
        printe.output(translations["da"])
        printe.output(translations["ar"])
    # ---
    NewDesc = {}
    addedlangs = []
    replacelang = []
    for lang, lang_e in translations.items():
        # ---
        ses_desc = Scientific_descraptions.get(lang, "")
        # ---
        item_desc = item_descriptions.get(lang, "")
        # ---
        ar_descs = ["مقالة علمية", "مقالة بحثية"]
        # ---
        if lang not in item_descriptions.keys():
            NewDesc[lang] = {"language": lang, "value": lang_e}
            addedlangs.append(lang)
        # ---
        elif item_desc == ses_desc or (
            lang == "ar" and item_desc in ar_descs
        ):  # or (lang == "bn"  and ):  # to fix bn descraptions
            if lang_e != item_desc:
                printe.output(f'<<lightyellow>> replace desc "{item_desc}"@{lang}.')
                NewDesc[lang] = {"language": lang, "value": lang_e}
                # if lang == "bn":
                # replacelang.append(lang)
                # else:
                addedlangs.append(lang)
        # ---
        # fix some error
        elif pubdate["month"] == "11" and lang in Month_Table:
            if item_desc.find(Month_Table[lang]["12"]) != -1:
                printe.output(f'<<lightyellow>> find error desc "{item_desc}"@{lang}.')
                NewDesc[lang] = {"language": lang, "value": lang_e}
                replacelang.append(lang)
    # ---
    # printe.output( '<<lightyellow>> make_scientific_article' + str(NewDesc) )
    if addedlangs or replacelang:
        # printe.output( '<<lightyellow>> **%d: make_scientific_article: %s  %s'  %(num , item["q"] , p31))
        tablem["descriptions"] = NewDesc
        tablem["qid"] = q
        tablem["fixlang"] = replacelang
    else:
        print("make_scientific_article nothing to add. ")

    return tablem


#!/usr/bin/python3
"""
from .do_text import make_new_text, do_One_Page

"""

import re

# ---
from .cy_regs import make_data
from .cy_helps import printt, print_test2, GetSectionNew3, printo, TEST, CheckTempalteInPageText
from .cy_sparql import GetSparql

# ---
remove_date = {}
Work_with_Year = {}
Len_of_results = {}
Len_of_valid_results = {}
new_lines = {}
# ---
states = {}
lines = {}
# ---
HeadVars = ["imagejersey"]
JOJOJO = "نتيجة سباق الدراجات/جيرسي"


Skip_items = ["Q4115189"]

NoAppend = ["p585", "p582", "p580"]
# ---
ranks_label = {
    "P4323": "المرتبة %s في تصنيف أفضل شاب",
    "P2321": "المرتبة %s في التصنيف العام",
    "P4320": "المرتبة %s في تصنيف الجبال",
    "P3494": "المرتبة %s في تصنيف النقاط",
}
# ---

Work_with_Stage = {}


def template_params(text, title):
    # ---
    Frist = re.compile(r"\{\{نتيجة سباق الدراجات\/بداية\s*?.*?\}\}")
    # ---
    pas = Frist.findall(text)
    # ---
    if not pas:
        return False, False
    # ---
    params = str(pas[0])
    params = re.sub(r"\s*\=\s*", "=", params)
    params = re.sub(r"\s*\|\s*", "|", params)
    if do := re.search(r".*\|تاريخ\=(\d+)(\}\}|\|)", text):
        Work_with_Year[title] = int(do.group(1))
        print_test2(f"Work_with_Year:{do.group(1)}")
    # ---
    if re.sub(r"مراحل\s*\=\s*نعم", "", params) != params:
        printt("Work with Stage")
        Work_with_Stage[title] = True
    # ---
    if re.sub(r".*id\s*\=\s*(Q\d+).*", r"\g<1>", params) != params:
        printt("** found currect line")
        Qid = re.sub(r".*id\=(Q\d+).*", r"\g<1>", params)
        printt(f"id: {Qid}")
        return Qid, True
    # ---
    return False, False


def findflag(race, flag):
    flage = {
        "إيطاليا": "{{رمز علم|إيطاليا}}",
        "جيرو ديل ترينتينو": "{{رمز علم|إيطاليا}}",
        "the Alps": "{{رمز علم|إيطاليا}}",
        "France": "{{رمز علم|فرنسا}}",
        "فرنسا": "{{رمز علم|فرنسا}}",
        "إسبانيا": "{{رمز علم|إسبانيا}}",
        "دونكيرك": "{{رمز علم|بلجيكا}}",
        "غنت-وفلجم": "{{رمز علم|بلجيكا}}",
        "Gent–Wevelgem": "{{رمز علم|بلجيكا}}",
        "Norway": "{{رمز علم|النرويج}}",
        "النرويج": "{{رمز علم|النرويج}}",
        "كريثيديا دو دوفين": "{{رمز علم|سويسرا}}",
        "du Dauphiné": "{{رمز علم|سويسرا}}",
        "سويسرا": "{{رمز علم|سويسرا}}",
        "باريس-نايس": "{{رمز علم|فرنسا}}",
    }
    # ---
    race = str(race)
    # ---
    for ff in flage:
        te = re.sub(str(ff), "", race)
        # ---
        if te != race:
            flag = flage[ff]
    # ---
    return flag


def fix_label(label):
    label = label.strip()

    label = re.sub(r"بطولة العالم لسباق الدراجات على الطريق (\d+) – سباق الطريق الفردي للرجال", r"سباق الطريق في بطولة العالم \g<1>", label)

    label = re.sub(r"ركوب الدراجات في الألعاب الأولمبية الصيفية (\d+) – سيدات فردي سباق الطريق", r"سباق الطريق للسيدات في ركوب الدراجات الأولمبية الصيفية \g<1>", label)

    label = re.sub(r"ركوب الدراجات في الألعاب الأولمبية الصيفية (\d+) – فريق رجال سباق الطريق", r"سباق الطريق لفرق الرجال في ركوب الدراجات الأولمبية الصيفية \g<1>", label)

    # بطولة العالم لسباق الدراجات على الطريق 1966 – سباق الطريق الفردي للرجال
    label = re.sub(r"بطولة العالم لسباق الدراجات على الطريق (\d+) – سباق الطريق الفردي للرجال", r"سباق الطريق للرجال في بطولة العالم \g<1>", label)

    label = re.sub(r"سباق الطريق المداري ", "سباق الطريق ", label)
    label = re.sub(r"(بطولة [\s\w]+) الوطنية ", r"\g<1> ", label)
    label = re.sub(r"^(سباق\s*.*? في بطولة العالم)\s*(لسباق الدراجات على الطريق|للدراجات) (.*?)$", r"\g<1> \g<3>", label)
    label = re.sub(r"^(سباق\s*.*? في بطولة [\s\w]+)\s*(لسباق الدراجات على الطريق|للدراجات) (.*?)$", r"\g<1> \g<3>", label)

    # سباق الطريق للسيدات في ركوب الدراجات في الألعاب الأولمبية الصيفية 2016
    label = re.sub(r"في ركوب الدراجات في الألعاب الأولمبية ", "في ركوب الدراجات الأولمبية ", label)

    # في ركوب الدراجات في دورة ألعاب الكومنولث
    label = re.sub(r"ركوب الدراجات في دورة ألعاب الكومنولث", "ركوب الدراجات في دورة الكومنولث", label)
    label = re.sub(r"\s+", " ", label)
    return label


def make_temp_lines(table, title, with_stages):
    # ---
    for rr in HeadVars:
        if rr not in table:
            table[rr] = ""
    # ---
    image = table["imagejersey"]
    image = re.sub(r"JOJOJO", JOJOJO, image)
    image = image.replace("%20", "_")
    # ---
    date = table["Date"]
    flag = table["p17lab"]
    # ---
    qid = table["item"]
    table2 = {"race": "", "p17": "", "poss": "", "qid": qid}
    # ---
    if qid in Skip_items:
        return "", table2
    # ---
    link = table.get("title", "")
    label = table.get("itemlab", "")
    if link:
        race = f"[[{link}]]"
        label = link.split(" (")[0]
    # ---
    label = fix_label(label)
    # ---
    if link:
        race = f"[[{link}|{label}]]" if label != link else f"[[{link}]]"
    else:
        race = label
    # ---
    sss = table["p642label"]
    # الفائز وفقاً لترتيب النقاط للشباب
    sss = re.sub(r"الفائز وفقاً لترتيب", "الفائز في ترتيب", sss)
    sss = re.sub(r"الفائز حسب التصنيف العام", "الفائز في التصنيف العام", sss)
    # ---
    ranke = table.get("rank", "")
    # ---
    ranke_tab = {
        "المرتبة 1 في": "الأول في",
        "المرتبة 2 في": "الثاني في",
        "المرتبة 3 في": "الثالث في",
        "المرتبة 4 في": "الرابع في",
        "المرتبة 5 في": "الخامس في",
        "المرتبة 6 في": "السادس في",
        "المرتبة 7 في": "السابع في",
        "المرتبة 8 في": "الثامن في",
        "المرتبة 9 في": "التاسع في",
        "المرتبة 10 في": "العاشر في",
        # "المرتبة 11 في" : "الحادي عشر في",
        # "المرتبة 12 في" : "الثاني عشر في",
    }
    for kk in ranke_tab:
        if ranke.find(kk) >= 0:
            ranke = re.sub(kk, ranke_tab[kk], ranke)
    # ---
    newflag = findflag(race, flag)
    # ---
    table2["race"] = race
    table2["p17"] = newflag
    table2["poss"] = sss
    # ---
    so = "{{نتيجة سباق الدراجات/سطر4"
    so = so + "\n|qid = " + qid
    so = so + "\n|السباق = " + race
    so = so + "\n|البلد = " + newflag
    so = so + "\n|التاريخ = " + date
    so = so + "\n|المركز = " + sss
    so = so + "\n|المرتبة = " + ranke
    so = so + "\n|جيرسي = " + image
    so += "\n}}"
    # ---
    if race and race.lower().strip().startswith("q"):
        printt(" *** remove line startswith q.")
        return "", table2
    # ---
    if ranke and sss.strip() == "":
        if not with_stages and Len_of_valid_results.get(title, 0) > 10:
            if re.sub(r"المرتبة 1 في", "", ranke) == ranke and re.sub(r"الأول في", "", ranke) == ranke:
                printt(" *** remove line with rank < 1.")
                return "", table2
    # ---
    if flag != newflag:
        printt(f' *** race:"{race}", flag:"{flag}", newflag:"{newflag}"')
    # ---
    if title not in Len_of_valid_results:
        Len_of_valid_results[title] = 0
    Len_of_valid_results[title] += 1
    # ---
    return so, table2


def fix_results(table):
    results2 = {}
    # ---
    tata = {
        "head": {"vars": ["item", "p17lab", "itemlab", "jersey_1", "jersey_2", "jersey_3", "jersey_4", "p642label", "p585", "p582", "p580", "rankP4323", "rankP2321", "rankP4320", "rankP3494", "title"]},
        "results": {
            "bindings": [
                {
                    "item": {"type": "uri", "value": "http://www.wikidata.org/entity/Q53557910"},
                    "title": {"xml:lang": "ar", "type": "literal", "value": "طواف أستونيا 2018"},
                    "p580": {"datatype": "http://www.w3.org/2001/XMLSchema#dateTime", "type": "literal", "value": "2018-05-25T00:00:00Z"},
                    "p582": {"datatype": "http://www.w3.org/2001/XMLSchema#dateTime", "type": "literal", "value": "2018-05-26T00:00:00Z"},
                    "p17lab": {"xml:lang": "ar", "type": "literal", "value": "إستونيا"},
                    "itemlab": {"xml:lang": "ar", "type": "literal", "value": "طواف أستونيا 2018"},
                    "rankP2321": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "2"},
                    "rankP4323": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "1"},
                    "rankP3494": {"datatype": "http://www.w3.org/2001/XMLSchema#decimal", "type": "literal", "value": "1"},
                    "p642label": {"xml:lang": "ar", "type": "literal", "value": "الفائز وفقاً لترتيب النقاط"},
                    "jersey_1": {"type": "literal", "value": "{{JOJOJO|Jersey%20white.svg|قميص أبيض، أفضل شاب}}"},
                    "jersey_2": {"type": "literal", "value": "{{JOJOJO|Jersey%20white.svg|قميص أبيض، أفضل شاب}}"},
                    "jersey_4": {"type": "literal", "value": "{{JOJOJO|Jersey%20red.svg|قميص أحمر، تصنيف النقاط}}"},
                }
            ]
        },
    }
    # ---
    printt(f"* Lenth fix_results: '{len(table)}' .")
    for params in table:
        # ---
        if params.get("itemlab", {}).get("value", "").lower().strip().startswith("q"):
            printt(" *** remove line startswith q---.")
            continue
        # ---
        q = "item" in params and params["item"]["value"].split("/entity/")[1]
        # ---
        if q not in results2:
            results2[q] = {"Date": [], "imagejersey": [], "item": [], "rank": []}
        # ---
        date = params.get("p585") or params.get("p582") or params.get("p585") or {}
        date = date.get("value") or ""
        # ---
        if date not in results2[q]["Date"]:
            results2[q]["Date"].append(date)
        # ---
        for param in params:
            # ---
            value = params[param]["value"]
            # ---
            param2 = param
            if param.startswith("rank"):
                param2 = "rank"
                value2 = param.replace("rank", "")
                if value2 in ranks_label:
                    value = ranks_label[value2] % value
            # ---
            if param.startswith("jersey_"):
                param2 = "imagejersey"
            # ---
            if param == "p17lab":
                value = "{{رمز علم|" + value + "}}"
            elif param == "item":
                value = value.split("/entity/")[1]
            # ---
            # if param == "p642label":
            # value = re.sub(r'الفائز وفقاً ', 'الفائز في ', value )
            # value = re.sub(r'الفائز حسب التصنيف العام ', 'الفائز في التصنيف العام', value )
            # ---
            if param2 not in NoAppend:
                if param2 not in results2[q]:
                    results2[q][param2] = []
                # ---
                if value not in results2[q][param2]:
                    results2[q][param2].append(value)
            # ---
    return results2


def fix_date(data, title):
    data2 = {}
    # ---
    p642label = 0
    # ---
    for ta in data:
        # ---
        datn = data[ta].get("Date", [])
        # ---
        if isinstance(datn, list) and len(datn) > 0:
            ddds = [x.strip() for x in datn if x.strip() != ""]
            # ---
            # print(date)
            # ---
            fanco = title
            if fanco not in remove_date:
                remove_date[fanco] = 0
            # ---
            if fanco in Work_with_Year:
                date = ""
                if ddds != []:
                    date = ddds[0]
                if not date:
                    remove_date[fanco] += 1
                    # return ""
                    continue
                else:
                    if hhh := re.match(r"(\d\d\d\d)\-\d\d\-\d\dT\d\d\:\d\d\:\d\dZ", date):
                        if int(hhh.group(1)) < Work_with_Year[fanco]:
                            remove_date[fanco] += 1
                            continue
        # ---
        data2[ta] = data[ta]
        if data2[ta].get("p642label", False):
            p642label += 1
        # ---
        if remove_date[fanco] != 0:
            print_test2("remove_date[fanco] += 1 (%d)" % remove_date[fanco])
    # ---
    Len_of_results[title] = p642label
    # ---
    return data2


def make_new_section(qid, title):
    Date_List2 = []
    # ---
    with_stages= Work_with_Stage.get(title, False)
    # ---
    new_lines[title] = {}
    # ---
    json1 = GetSparql(qid, title)
    # ---
    if not json1:
        return False
    # ---
    bindings = json1.get("results", {}).get("bindings", [])
    # ---
    for rr in json1.get("head", {}).get("vars", []):
        HeadVars.append(rr)
    # ---
    if len(bindings) < 1:
        return False
    # ---
    results = fix_results(bindings)
    # ---
    Len_results = len(results)
    printt("* Lenth results: '%d' ." % Len_results)
    # ---
    # Len_of_results[title] = Len_results
    # ---
    qidso = {}
    for num, qq in enumerate(results):
        # ---
        if qq not in qidso:
            qidso[qq] = {}
        # ---
        date = results[qq]["Date"][0]
        if not date:
            if qq not in Date_List2:
                Date_List2.append(qq)
        elif date not in Date_List2:
            Date_List2.append(date)
        # ---
        qidso[qq] = results[qq]
    # ---
    qids_2 = fix_date(qidso, title)
    # ---
    Date_List2.sort()
    printt("**Date_List2: ")
    # ---
    texxt = ""
    for dd in Date_List2:
        for qoo, tao in qids_2.items():
            # ---
            if qoo in Skip_items:
                continue
            # ---
            date = tao["Date"][0]
            # ---
            if dd == date:
                table = {}
                # ---
                for ss in tao:
                    space = "، "
                    if ss in ["imagejersey", "p17lab"]:
                        space = ""
                    # ---
                    faso = sorted(tao[ss])
                    # ---
                    if len(faso) > 0:
                        if len(faso) == 1 or ss == "p17lab":
                            k = faso[0]
                        elif len(faso) > 1:
                            k = space.join(faso)
                        # ---
                        if ss == "Date":
                            k = faso[0]
                        # ---
                        table[ss] = k
                # ---
                v, tab = make_temp_lines(table, title, with_stages)
                # ---
                if v:
                    # vvv = re.sub(r"\n", "", v)
                    new_lines[title][qoo] = tab
                    new_lines[title][qoo]["qid"] = qoo
                    new_lines[title][qoo]["race"] = tab.get("race", "")
                    new_lines[title][qoo]["p17"] = tab.get("p17", "")
                    new_lines[title][qoo]["poss"] = tab.get("poss", "")
                    # ---
                    texxt = texxt + v + "\n"
                # ---
    note = "<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->\n"
    texxt = note + texxt
    # ---
    t24 = Len_of_valid_results.get(title, 0)
    t23 = Len_of_results.get(title, 0)
    # ---
    printt(f"Len_of_valid_results : {t24}, Len_of_results : {t23}")
    # ---
    printt(f"Len_of_valid_results : {t24}, Len_of_results : {t23}")
    # ---
    return texxt


def work_tano(text, MainTitle):
    # ---
    lines[MainTitle] = make_data(text)
    # ---
    new_line = 0
    same_line = 0
    removed_line = 0
    # ---
    if MainTitle in new_lines:
        for line in new_lines[MainTitle].keys():
            # ---
            if line == "Q49164584" and TEST[1]:
                print(new_lines[MainTitle][line])
            # ---
            same = 0
            new = 0
            if line in lines[MainTitle].keys():
                for x in ["poss", "race", "p17"]:
                    if new_lines[MainTitle][line][x] == lines[MainTitle][line][x]:
                        same = 1
                    else:
                        new = 1
            else:
                new = 1
            # ---
            if same == 1:
                same_line += 1
            elif new == 1:
                new_line += 1
            # ---
        # ---
        for liner in lines[MainTitle].keys():
            if liner not in new_lines[MainTitle].keys():
                removed_line += 1
    # ---
    states[MainTitle] = {"new_line": new_line, "same_line": same_line, "removed_line": removed_line}
    # ---
    liner = "new_line:%d,same_line:%d,removed_line:%d" % (new_line, same_line, removed_line)
    # ---
    if MainTitle in remove_date and remove_date[MainTitle] != 0:
        liner += ",removed_line_date:%d" % remove_date[MainTitle]
        states[MainTitle]["removed_line_date"] = remove_date[MainTitle]
    # ---
    return liner


def make_new_text(item, title, text):
    # ---
    Newsect = make_new_section(item, title)
    # ---
    if not Newsect:
        ur = f'<a href="https://www.wikidata.org/wiki/{item}">{item}</a>.'
        print_test2("no new section")
        printo(f"لا توجد نتائج لهذه الصفحة تأكد من صحة معرف ويكي بيانات: {ur}.")
        return False
    # ---
    sect, Frist = GetSectionNew3(text)
    # ---
    work_tano(sect, title)
    # ---
    Newsect = Frist + "\n" + Newsect + "{{نتيجة سباق الدراجات/نهاية}}"
    Newsect = re.sub(r"\n\n{{نتيجة سباق الدراجات/نهاية}}", "\n{{نتيجة سباق الدراجات/نهاية}}", Newsect)
    # ---
    NewText = text.replace(sect, Newsect)
    # ---
    printt(f"showDiff of page: {title}<br>")
    # ---
    if title not in states:
        return False
    # ---
    if states[title]["new_line"] != 0 or states[title]["removed_line"] != 0 and text != NewText:
        return NewText
    else:
        printo("nodiff")
    # ---
    return "nodiff"


def do_One_Page(title, text, item=""):
    # ---
    Check = CheckTempalteInPageText(text)
    # ---
    if not Check:
        printt("no Check: pass....<br>")
        return
    # ---
    printt("**Isre: ")
    # ---
    Qid, QidinTemplate = template_params(text, title)
    # ---
    if QidinTemplate:
        item = Qid
    # ---
    if not item:
        hte = "<!-- Can't find item in page :\"" + title + '" --> '
        # ---
        if QidinTemplate:
            hte = "<!-- Can't find item by item :\"" + item + '" --> '
        # ---
        printt(f"**{hte}")
    # ---
    if not item:
        return
    # ---
    printt(f"**item: {item}")
    # ---
    NewText = make_new_text(item, title, text)
    # ---
    if not NewText:
        ur = f'<a href="https://www.wikidata.org/wiki/{item}">{item}</a>.'
        printo(f"لا توجد نتائج لهذه الصفحة تأكد من صحة معرف ويكي بيانات: {ur}.")
        return
    # ---
    if NewText == "nodiff":
        printo("nodiff")
        return
    # ---
    return NewText

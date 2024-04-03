#!/usr/bin/env python3
"""
toolforge jobs run arw2 --mem 1Gi --image python3.9 --command "$HOME/local/bin/python3 $HOME/core8/pwb.py dump/arw/arw2"

python3 wd_core/dump/arw/arw2.py test
python3 core8/pwb.py dump/arw/arw2
python3 core8/pwb.py dump/arw/arw2 test ask
python3 core8/pwb.py dump/arw/arw2 test ask p31
python3 core8/pwb.py dump/arw/arw2 test ask printline
python3 core8/pwb.py dump/arw/arw2 test ask limit:5000
"""
import sys
import os
import bz2
import json
import time

# ---
from dump.arw.p31_table import make_text_p31, create_p31_table_no, ns_stats
from dump.memory import print_memory

# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r"I:\core\dumps"):
    Dump_Dir = r"I:\core\dumps"
# ---
print(f"Dump_Dir:{Dump_Dir}")
Offset = {1: 0}
# ---
Limit = {1: 9000000000} if "test" not in sys.argv else {1: 15000}
# ---
for arg in sys.argv:
    arg, _, value = arg.partition(":")
    if arg.startswith("-"):
        arg = arg[1:]
    if arg in ["offset", "off"]:
        Offset[1] = int(value)
    if arg == "limit":
        Limit[1] = int(value)
# ---
priffixeso = [
    "مقالة",
    "نقاش:",
    "مستخدم:",
    "نقاش المستخدم:",
    "ويكيبيديا:",
    "نقاش ويكيبيديا:",
    "ملف:",
    "نقاش الملف:",
    "ميدياويكي:",
    "نقاش ميدياويكي:",
    "قالب:",
    "نقاش القالب:",
    "مساعدة:",
    "نقاش المساعدة:",
    "تصنيف:",
    "نقاش التصنيف:",
    "بوابة:",
    "نقاش البوابة:",
    "وحدة:",
    "نقاش الوحدة:",
    "إضافة:",
    "نقاش الإضافة:",
    "تعريف الإضافة:",
    "نقاش تعريف الإضافة:",
    "موضوع:",
]
priffixes = {
    x: {
        "count": 0,
        "labels": {"yes": 0, "no": 0, "yesar": 0, "noar": 0},
        "descriptions": {"yes": 0, "no": 0, "yesar": 0, "noar": 0},
        "aliases": {"yes": 0, "no": 0, "yesar": 0, "noar": 0},
    }
    for x in priffixeso
}
# ---
stats_tab = {
    "all_items": 0,
    "all_ar_sitelinks": 0,
    "sitelinks_no_ar": 0,
    "no_p31": 0,
    "no_claims": 0,
    "other_claims_no_p31": 0,
    "Table_no_ar_lab": {},
    "p31_main_tab": {},
    "delta": 0,
}
# ---


def save_to_wp(text):
    if text == "":
        print("text is empty")
        return
    # ---
    print(text)
    # ---
    if "nosave" in sys.argv:
        print("nosave")
        return
    # ---
    title = "ويكيبيديا:مشروع_ويكي_بيانات/تقرير_P31"
    # ---
    if "test" in sys.argv:
        title += "/ملعب"
    # ---
    print(f"title:{title}")
    # ---
    from API import arAPI

    arAPI.page_put(oldtext="", newtext=text, summary="Bot - Updating stats", title=title)
    # ---
    del text
    del arAPI


def read_data():
    filename = "/mnt/nfs/dumps-clouddumps1002.wikimedia.org/other/wikibase/wikidatawiki/latest-all.json.bz2"
    # ---
    if not os.path.isfile(filename):
        print(f"file {filename} <<lightred>> not found")
        return
    # ---
    t1 = time.time()
    # ---
    c = 0
    # ---
    with bz2.open(filename, "rt", encoding="utf-8") as f:
        for line in f:
            line = line.strip("\n").strip(",")
            if line.startswith("{") and line.endswith("}"):
                c += 1
                # ---
                if c > Limit[1]:
                    print(f"c:{c}>Limit[1]:{Limit[1]}")
                    break
                # ---
                if c < Offset[1]:
                    if c % 1000 == 0:
                        dii = time.time() - t1
                        print("Offset c:%d, time:%d" % (c, dii))
                    continue
                # ---
                if (c % 1000 == 0 and c < 100000) or c % 100000 == 0:
                    dii = time.time() - t1
                    print(f"c:{c}, time:{dii}")
                    t1 = time.time()
                    print_memory()
                # ---
                if "printline" in sys.argv and (c % 1000 == 0 or c == 1):
                    print(line)
                # ---
                # جميع عناصر ويكي بيانات المفحوصة
                stats_tab["all_items"] += 1
                # ---
                # p31_no_ar_lab = []
                json1 = json.loads(line)
                # ---
                # q = json1['id']
                sitelinks = json1.get("sitelinks", {})
                if not sitelinks or sitelinks == {}:
                    del json1
                    continue
                # ---
                arlink = sitelinks.get("arwiki", {}).get("title", "")
                if not arlink:
                    # عناصر بوصلات لغات بدون وصلة عربية
                    stats_tab["sitelinks_no_ar"] += 1
                    del json1, sitelinks
                    continue
                # ---
                # عناصر ويكي بيانات بها وصلة عربية
                stats_tab["all_ar_sitelinks"] += 1
                arlink_type = "مقالة"
                # ---
                for pri, _ in priffixes.items():
                    if arlink.startswith(pri):
                        priffixes[pri]["count"] += 1
                        arlink_type = pri
                        break
                # ---
                if arlink_type not in stats_tab["p31_main_tab"]:
                    stats_tab["p31_main_tab"][arlink_type] = {}
                # ---
                if arlink_type == "مقالة":
                    priffixes["مقالة"]["count"] += 1
                # ---
                p31x = "no"
                # ---
                claims = json1.get("claims", {})
                # ---
                if claims == {}:
                    # صفحات دون أية خواص
                    stats_tab["no_claims"] += 1
                # ---
                P31 = claims.get("P31", {})
                # ---
                if P31 == {}:
                    # صفحة بدون خاصية P31
                    stats_tab["no_p31"] += 1
                    # ---
                    if len(claims) > 0:
                        # خواص أخرى بدون خاصية P31
                        stats_tab["other_claims_no_p31"] += 1
                # ---
                for x in P31:
                    p31x = x.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id")
                    if not p31x:
                        continue
                    # ---
                    # if p31x not in p31_no_ar_lab:
                    #     p31_no_ar_lab.append(p31x)
                    # ---
                    if p31x in stats_tab["p31_main_tab"][arlink_type]:
                        stats_tab["p31_main_tab"][arlink_type][p31x] += 1
                    else:
                        stats_tab["p31_main_tab"][arlink_type][p31x] = 1
                # ---
                tat = ["labels", "descriptions", "aliases"]
                # ---
                for x in tat:
                    if x not in json1:
                        # دون عربي
                        priffixes[arlink_type][x]["no"] += 1
                        continue
                    # ---
                    priffixes[arlink_type][x]["yes"] += 1
                    # ---
                    # تسمية عربي
                    if "ar" in json1[x]:
                        priffixes[arlink_type][x]["yesar"] += 1
                    else:
                        priffixes[arlink_type][x]["noar"] += 1
                # ---
                ar_desc = json1.get("descriptions", {}).get("ar", False)
                # ---
                if not ar_desc:
                    # استخدام خاصية 31 بدون وصف عربي
                    for x in json1.get("claims", {}).get("P31", []):
                        if p31d := x.get("mainsnak", {}).get("datavalue", {}).get("value", {}).get("id"):
                            if p31d not in stats_tab["Table_no_ar_lab"]:
                                stats_tab["Table_no_ar_lab"][p31d] = 0
                            stats_tab["Table_no_ar_lab"][p31d] += 1


def mainar():
    start = time.time()
    # ---
    read_data()
    # ---
    final = time.time()
    # ---
    stats_tab["delta"] = int(final - start)
    text = "* تقرير تاريخ: latest تاريخ التعديل ~~~~~.\n" + "* جميع عناصر ويكي بيانات المفحوصة: {all_items:,} \n"
    text += "* عناصر ويكي بيانات بها وصلة عربية: {all_ar_sitelinks:,} \n"
    text += "* عناصر بوصلات لغات بدون وصلة عربية: {sitelinks_no_ar:,} \n"
    text += "<!-- bots work done in {delta} secounds --> \n"
    text += "__TOC__\n"
    # ---
    text = text.format_map(stats_tab)
    # ---
    NS_table = ns_stats(priffixes)
    # ---
    P31_secs = "== استخدام خاصية P31 ==\n" + "* {no_claims:,} صفحة دون أية خواص.\n"
    P31_secs += "* {no_p31:,} صفحة بدون خاصية P31.\n"
    P31_secs += "* {other_claims_no_p31:,} صفحة بها خواص أخرى دون خاصية P31.\n"
    # ---
    P31_secs = P31_secs.format_map(stats_tab)
    # ---
    textP31 = make_text_p31(stats_tab["p31_main_tab"], priffixes)
    # ---
    P31_table_no = create_p31_table_no(stats_tab["Table_no_ar_lab"])
    # ---
    text += f"\n{NS_table}"
    text += f"\n{P31_secs}"
    text += f"\n{textP31}"
    text += f"\n{P31_table_no}"
    # ---
    print(text)
    # ---
    if stats_tab["all_items"] == 0:
        print("nothing to update")
        return
    # ---
    save_to_wp(text)
    # ---
    if "test" not in sys.argv and "nodump" not in sys.argv:
        with open(f"{Dump_Dir}/texts/arw2.txt", "w", encoding="utf-8") as f:
            f.write(text)


if __name__ == "__main__":
    mainar()

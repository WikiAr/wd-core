#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Wikidata Properties Arabic Labels/Descriptions Filler
----------------------------------------------------
- يجلب خصائص بلا وسم عربي من WDQS
- يجلب الوسم/الوصف بالإنجليزية
- يترجم للّغة العربية بالذكاء الاصطناعي
- يرفع الوسوم/الأوصاف العربية عبر wbsetlabel / wbsetdescription

الاستخدام:
    python I:/core/bots/wd_core/prop_labs/fill_ar_props.py --limit 200 --dry-run
    python I:/core/bots/wd_core/prop_labs/fill_ar_props.py --limit 1000 --offset 0 --only labels
    python I:/core/bots/wd_core/prop_labs/fill_ar_props.py --limit 500 --only descriptions

بيئة التشغيل (متغيرات البيئة):
    WD_USERNAME          اسم مستخدم ويكي بيانات
    WD_PASSWORD          كلمة مرور البوت (أو Bot Password)

ملاحظات:
- احرص على استخدام حساب بوت/صلاحيات مناسبة.
- يحترم السكربت maxlag لتجنّب ضغط السيرفر.
"""

import os
import sys
import time
import json
import argparse
import requests

from tqdm import tqdm
from pathlib import Path

from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Dict, List, Optional, Tuple

sys.path.append(str(Path(__file__).parent))
sys.path.append("I:/core/bots/new/newapi_bot")

from wd_Session import WikidataSession
from newapi import printe
from newapi.accounts.useraccount import User_tables_ibrahem

from translate_bot import translate_en_to_ar

WDQS_ENDPOINT = "https://query.wikidata.org/sparql"
MW_API = "https://www.wikidata.org/w/api.php"

HEADERS_API = {
    "User-Agent": "WD-Ar-Props-Filler/1.0 (contact: your-email@example.com)"
}

username = User_tables_ibrahem["username"]
password = User_tables_ibrahem["password"]


# =========================
# ترجمات: اختر مزوّدك
# =========================

# =========================
# WDQS: جلب خصائص بلا وسم عربي
# =========================
def fetch_props_missing_ar(limit: int, offset: int = 0) -> List[dict]:
    # ---
    query = f"""
        SELECT ?p ?pLabel ?pDescription WHERE {{
            values ?P31 {{
                wd:Q54254515
                wd:Q54275221
                wd:Q54275340
                wd:Q116547761
                wd:Q56216056
            }}
            ?p a wikibase:Property .
            ?p wdt:P31 ?P31 .
            # ?p wdt:P31/wdt:P279* wd:Q54076056 .

            FILTER(NOT EXISTS {{ ?p wdt:P1630 ?P1630. }})

            FILTER(NOT EXISTS {{ ?p rdfs:label ?l . FILTER(LANG(?l) = "ar") }})
            SERVICE wikibase:label {{
                bd:serviceParam wikibase:language "en" .
            }}
        }}
        LIMIT {limit}
        OFFSET {offset}
    """
    # ---
    print(query)
    # ---
    sparql = SPARQLWrapper(WDQS_ENDPOINT)
    sparql.setQuery(query)
    # ---
    results = []
    # ---
    sparql.setReturnFormat(JSON)
    # ---
    sparql_results = sparql.query().convert()
    # ---
    for b in sparql_results["results"]["bindings"]:
        uri = b["p"]["value"]
        pid = uri.rsplit("/", 1)[-1]
        en_label = b.get("pLabel", {}).get("value", "")
        en_desc = b.get("pDescription", {}).get("value", "")
        results.append({"id": pid, "en_label": en_label, "en_desc": en_desc})
    # ---
    return results

# =========================
# منطق التنفيذ
# =========================


cache_file_labels = Path(__file__).parent / "cache_data_labels.json"

cache_data_labels = {}
if cache_file_labels.exists():
    with cache_file_labels.open("r", encoding="utf-8") as f:
        cache_data_labels = json.load(f)


cache_file = Path(__file__).parent / "cache_data.json"
cache_data = {}
results_cache = []

already_translated = {}

if cache_file.exists():
    with cache_file.open("r", encoding="utf-8") as f:
        cache_data = json.load(f)
    # ---
    for pid, pid_data in cache_data.items():
        results_cache.append({"id": pid, "en_label": pid_data["label"]["en"], "en_desc": pid_data["description"]["en"]})
        # ---
        if pid_data["label"]["ar"]:
            already_translated[pid_data["label"]["en"]] = pid_data["label"]["ar"]
        # ---
        if pid_data["description"]["ar"]:
            already_translated[pid_data["description"]["en"]] = pid_data["description"]["ar"]


def translate_en_to_ar_wrap(text):
    if already_translated.get(text):
        return already_translated[text]
    return translate_en_to_ar(text)


def dump_all():
    printe.output("<<green>> dump_all():")

    with cache_file.open("w", encoding="utf-8") as f:
        json.dump(cache_data, f, ensure_ascii=False, indent=4)

    with cache_file_labels.open("w", encoding="utf-8") as f:
        json.dump(cache_data_labels, f, ensure_ascii=False, indent=4)


def start(args):
    if not args.dry_run and (not username or not password):
        raise SystemExit("الرجاء ضبط WD_USERNAME و WD_PASSWORD في متغيرات البيئة أو استخدم --dry-run.")

    print(f"[*] fetching property props with missing Arabic label (limit={args.limit}, offset={args.offset}) ...")
    # ---
    if args.cache:
        props = results_cache
        props = props[:args.limit]
    else:
        props = fetch_props_missing_ar(limit=args.limit, offset=args.offset)
    # ---

    print(f"[*] found {len(props)} properties.")

    # تسجيل الدخول
    wd = None
    if not args.dry_run and not args.dumpen:
        print("[*] logging in to Wikidata...")
        wd = WikidataSession(username, password)
        wd.login()
        print("[*] logged in.")

    # ^ حيلة لاستدعاء wbgetentities_en حتى في dry-run دون تسجيل دخول (لأنه GET عام).
    # ننسخ الجلسة المؤقتة:
    if args.dry_run:
        wd = WikidataSession("", "")
        wd.s.headers.update(HEADERS_API)

    done_labels = 0
    done_descs = 0

    for n, p in enumerate(tqdm(props), 1):
        # ---
        if n % 100 == 0 :
            dump_all()
        # ---
        pid, en_label, en_desc = p["id"], p["en_label"], p["en_desc"]
        # ---
        cache_data.setdefault(pid, {
            "label" : {
                "en": en_label,
                "ar": ""
            },
            "description" : {
                "en": en_desc,
                "ar": ""
            },
        })
        # ---
        cache_data[pid].setdefault("saved", {"label": False, "description": False})
        # ---
        cache_data_labels.setdefault(en_label, cache_data[pid].get("label", {}).get("ar", ""))
        # ---
        if args.dumpen:
            print(f"en_label: {en_label}, en_desc: {en_desc}")
            continue
        # ---
        # لا نعمل على خصائص بلا نص إنجليزي
        # (يمكنك تعديل السياسة إن أردت الترجمة من مصدر آخر)
        target_label = None
        target_desc = None

        if args.only in ("labels", "both") and en_label:
            target_label = translate_en_to_ar(en_label)

        if args.only in ("descriptions", "both") and en_desc:
            target_desc = translate_en_to_ar(en_desc)

        if target_label is None and target_desc is None:
            continue

        if target_label is not None:
            cache_data[pid]["label"]["ar"] = target_label

        if target_desc is not None:
            cache_data[pid]["description"]["ar"] = target_desc

        # عرض ما سنفعله (dry-run)
        if args.dry_run:
            if target_label is not None:
                print(f"[dry-run][{pid}] set AR label: '{target_label}'  (from EN: '{en_label}')")

            if target_desc is not None:
                print(f"[dry-run][{pid}] set AR description: '{target_desc}'  (from EN: '{en_desc}')")
            continue

        if cache_data[pid]["saved"]["label"]:
            print("label already saved..")
        else:
            if target_label is not None:
                # summary = "Add Arabic label via AI translation from English"
                summary = ""
                # ---
                print(f"en_label: {en_label}, target_label: {target_label}")
                # ---
                resp = wd.set_label_ar(pid, target_label, summary=summary, assert_bot=False)
                if "error" in resp:
                    print(f"[err][{pid}] label: {resp['error']}")
                else:
                    cache_data[pid]["saved"]["label"] = True
                    # ---
                    dump_all()
                    # ---
                    done_labels += 1
                    printe.output(f"<<green>> [ok][{pid}] label set.")

                print(f"time.sleep({args.sleep})")
                time.sleep(args.sleep)

        if cache_data[pid]["saved"]["description"]:
            print("description already saved..")
        else:
            if target_desc is not None:
                # summary = "Add Arabic description via AI translation from English"
                summary = ""
                # ---
                print(f"en_desc: {en_desc}, target_desc: {target_desc}")
                # ---
                resp = wd.set_description_ar(pid, target_desc, summary=summary, assert_bot=False)
                if "error" in resp:
                    print(f"[err][{pid}] desc: {resp['error']}")
                else:
                    cache_data[pid]["saved"]["description"] = True
                    # ---
                    dump_all()
                    # ---
                    done_descs += 1
                    printe.output(f"<<green>> [ok][{pid}] description set.")

                print(f"time.sleep({args.sleep})")
                time.sleep(args.sleep)

    print(f"[*] finished. labels added: {done_labels}, descriptions added: {done_descs}")


def main():
    ap = argparse.ArgumentParser(description="Fill Arabic labels/descriptions for Wikidata properties.")
    ap.add_argument("--limit", type=int, default=200, help="عدد الخصائص المطلوب جلبها من WDQS")
    ap.add_argument("--offset", type=int, default=0, help="إزاحة في نتائج WDQS")
    ap.add_argument("--only", choices=["labels", "descriptions", "both"], default="both",
                    help="حدّد ما الذي ستعمل عليه")

    ap.add_argument("--dry-run", action="store_true", help="لا يرسل أي تعديلات، فقط يعرض ما سيفعله")

    ap.add_argument("--sleep", type=float, default=0.1, help="زمن انتظار (ثوانٍ) بين الطلبات للاحترام")

    ap.add_argument("--dumpen", action="store_true", help="just dump en")
    ap.add_argument("--cache", action="store_true", help="use cache not sparql")

    args = ap.parse_args()

    start(args)
    dump_all()


if __name__ == "__main__":
    main()

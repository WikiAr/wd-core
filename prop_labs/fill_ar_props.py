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

from pathlib import Path

from SPARQLWrapper import SPARQLWrapper, JSON
from typing import Dict, List, Optional, Tuple

sys.path.append(str(Path(__file__).parent))
sys.path.append("I:/core/bots/new/newapi_bot")

from newapi import printe
from newapi.accounts.useraccount import User_tables_ibrahem

from gemini_bot import send_ai
from translate_bot import translate_en_to_ar

WDQS_ENDPOINT = "https://query.wikidata.org/sparql"
MW_API = "https://www.wikidata.org/w/api.php"

HEADERS_API = {
    "User-Agent": "WD-Ar-Props-Filler/1.0 (contact: your-email@example.com)"
}

username = User_tables_ibrahem["username"]
password = User_tables_ibrahem["password"]

# =========================
# MediaWiki: جلسة وتوكينات
# =========================
ask_user = {1: False}
if "ask" in sys.argv:
    ask_user[1] = True
    sys.argv.remove("ask")


class WikidataSession:
    def __init__(self, username: str, password: str):
        self.s = requests.Session()
        self.s.headers.update(HEADERS_API)
        self.username = username
        self.password = password
        self.csrf_token = None
        self.save_all = False

    def _get_login_token(self) -> str:
        r = self.s.get(
            MW_API, params={"action": "query", "meta": "tokens", "type": "login", "format": "json"}, timeout=60
        )
        r.raise_for_status()
        return r.json()["query"]["tokens"]["logintoken"]

    def login(self):
        token = self._get_login_token()
        r = self.s.post(
            MW_API,
            data={
                "action": "login",
                "lgname": self.username,
                "lgpassword": self.password,
                "lgtoken": token,
                "format": "json",
            },
            timeout=60,
        )
        r.raise_for_status()
        data = r.json()
        if data.get("login", {}).get("result") != "Success":
            raise RuntimeError(f"Login failed: {data}")

        # CSRF token
        r2 = self.s.get(
            MW_API, params={"action": "query", "meta": "tokens", "type": "csrf", "format": "json"}, timeout=60
        )
        r2.raise_for_status()
        self.csrf_token = r2.json()["query"]["tokens"]["csrftoken"]

    def wbgetentities_en(self, ids: List[str]) -> Dict[str, dict]:
        """
        يجلب labels/descriptions الإنجليزية لمجموعة معرّفات (خصائص).
        """
        results = {}
        # تجزئة على دفعات حتى لا يزيد طول الرابط
        CHUNK = 50
        for i in range(0, len(ids), CHUNK):
            chunk = ids[i : i + CHUNK]
            r = self.s.get(
                MW_API,
                params={
                    "action": "wbgetentities",
                    "ids": "|".join(chunk),
                    "props": "labels|descriptions",
                    "languages": "en|ar",
                    "format": "json",
                },
                timeout=60,
            )
            r.raise_for_status()
            data = r.json()
            results.update(data.get("entities", {}))
        return results

    def confirm_if_ask(self, pid: str, field: str, value: str) -> bool:
        """
        إذا كان "ask" موجود في sys.argv -> يسأل المستخدم للتأكيد.
        - pid: رقم الخاصية (مثلاً P123)
        - field: 'label' أو 'description'
        - value: النص العربي المقترح

        يرجع True إذا وافق المستخدم أو إذا لم يوجد "ask".
        يرجع False إذا رفض المستخدم.
        """
        # ---
        if not ask_user[1] or self.save_all:
            return True
        # ---
        printe.output(f"<<yellow>> [ask][{pid}] Add AR {field}: '{value}'")
        ans = input("(y/n)?").strip().lower()
        # ---
        answers = ["y", "yes", "", "a"]
        # ---
        if ans == "a":
            self.save_all = True
            printe.output("<<green>> SAVE ALL Without Asking\n" * 3)
            return True
        # ---
        return ans in answers

    def set_label_ar(self, pid: str, value: str, summary: str, assert_bot: bool = True) -> dict:
        data = {
            "action": "wbsetlabel",
            "id": pid,
            "language": "ar",
            "value": value,
            "token": self.csrf_token,
            "format": "json",
            "summary": summary,
            "maxlag": "5",
        }
        if assert_bot:
            data["assert"] = "bot"
        # ---
        if not self.confirm_if_ask(pid, "label", value):
            print(f"[skip][{pid}] label skipped.")
            return {"skipped": True}
        # ---
        r = self.s.post(MW_API, data=data, timeout=60)
        # ---
        return r.json()

    def set_description_ar(self, pid: str, value: str, summary: str, assert_bot: bool = True) -> dict:
        data = {
            "action": "wbsetdescription",
            "id": pid,
            "language": "ar",
            "value": value,
            "token": self.csrf_token,
            "format": "json",
            "summary": summary,
            "maxlag": "5",
        }
        if assert_bot:
            data["assert"] = "bot"
        # ---
        if not self.confirm_if_ask(pid, "description", value):
            print(f"[skip][{pid}] description skipped.")
            return {"skipped": True}
        # ---
        r = self.s.post(MW_API, data=data, timeout=60)
        # ---
        return r.json()


# =========================
# ترجمات: اختر مزوّدك
# =========================

# =========================
# WDQS: جلب خصائص بلا وسم عربي
# =========================
def fetch_props_missing_ar(limit: int, offset: int = 0) -> List[str]:
    # ---
    query = f"""
        SELECT ?p ?pLabel ?pDescription WHERE {{

            ?p a wikibase:Property .
            # ?p wdt:P31 wd:Q54254515 .

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


def start(args):
    if not args.dry_run and (not username or not password):
        raise SystemExit("الرجاء ضبط WD_USERNAME و WD_PASSWORD في متغيرات البيئة أو استخدم --dry-run.")

    print(f"[*] fetching property props with missing Arabic label (limit={args.limit}, offset={args.offset}) ...")
    props = fetch_props_missing_ar(limit=args.limit, offset=args.offset)
    print(f"[*] found {len(props)} properties.")

    # تسجيل الدخول
    wd = None
    if not args.dry_run:
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

    for p in props:
        pid, en_label, en_desc = p["id"], p["en_label"], p["en_desc"]

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

        # عرض ما سنفعله (dry-run)
        if args.dry_run:
            if target_label is not None:
                print(f"[dry-run][{pid}] set AR label: '{target_label}'  (from EN: '{en_label}')")
            if target_desc is not None:
                print(f"[dry-run][{pid}] set AR description: '{target_desc}'  (from EN: '{en_desc}')")
            continue

        # إرسال فعلي
        # ملاحظة: نستخدم ملخص تحرير واضح
        if target_label is not None:
            # summary = "Add Arabic label via AI translation from English"
            summary = ""
            # ---
            print(f"en_label: {en_label}")
            # ---
            resp = wd.set_label_ar(pid, target_label, summary=summary, assert_bot=False)
            if "error" in resp:
                print(f"[err][{pid}] label: {resp['error']}")
            else:
                done_labels += 1
                printe.output(f"<<green>> [ok][{pid}] label set.")
            time.sleep(args.sleep)

        if target_desc is not None:
            # summary = "Add Arabic description via AI translation from English"
            summary = ""
            # ---
            print(f"en_desc: {en_desc}")
            # ---
            resp = wd.set_description_ar(pid, target_desc, summary=summary, assert_bot=False)
            if "error" in resp:
                print(f"[err][{pid}] desc: {resp['error']}")
            else:
                done_descs += 1
                printe.output(f"<<green>> [ok][{pid}] description set.")
            time.sleep(args.sleep)

    print(f"[*] finished. labels added: {done_labels}, descriptions added: {done_descs}")


def main():
    ap = argparse.ArgumentParser(description="Fill Arabic labels/descriptions for Wikidata properties.")
    ap.add_argument("--limit", type=int, default=200, help="عدد الخصائص المطلوب جلبها من WDQS")
    ap.add_argument("--offset", type=int, default=0, help="إزاحة في نتائج WDQS")
    ap.add_argument("--only", choices=["labels", "descriptions", "both"], default="both",
                    help="حدّد ما الذي ستعمل عليه")
    ap.add_argument("--dry-run", action="store_true", help="لا يرسل أي تعديلات، فقط يعرض ما سيفعله")
    ap.add_argument("--sleep", type=float, default=0.5, help="زمن انتظار (ثوانٍ) بين الطلبات للاحترام")
    args = ap.parse_args()

    start(args)


if __name__ == "__main__":
    main()

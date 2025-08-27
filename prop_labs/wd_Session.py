#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

from wd_Session import WikidataSession

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

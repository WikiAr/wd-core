#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""

"""

import os
import sys
import time
import jsonlines
import json
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.append(str(Path(__file__).parent))

from gemini_bot import send_ai

dump_file = Path(__file__).parent / "dump.jsonl"

cache_data = {}
if dump_file.exists():
    with jsonlines.open(dump_file) as reader:
        for obj in reader.iter(skip_empty=True):
            cache_data[obj["en"]] = obj["ar"]


def save_cache(en, ar):
    with jsonlines.open(dump_file, mode="a") as writer:
        writer.write({"en": en, "ar": ar})


def translate_en_to_ar(en: str) -> str:
    # ---
    en = (en or "").strip()
    # ---
    if not en:
        return ""
    # ---
    in_cache = cache_data.get(en)
    # ---
    if in_cache:
        return in_cache
    # ---
    prompt = (
        "ترجم النص التالي ترجمة عربية طبيعية موجزة ومناسبة لوصف/وسم ويكي بيانات:\n\n"
        f"النص:\n{en}\n\n"
        "تعليمات:\n- إن كان النص اسمًا علميًا/تقنيًا شائع التعريب فعرّبه، وإن كان اسمًا ذاتيًا (اسم شخص/مكان/مؤسسة) فحافظ عليه كما هو إن لم يكن له تعريب راسخ.\n"
        "- لا تضف تعليقات أو أقواس.\n"
    )
    # ---
    text = send_ai(prompt)
    # ---
    if text:
        save_cache(en, text)
    # ---
    return text

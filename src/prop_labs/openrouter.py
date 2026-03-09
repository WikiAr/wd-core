import json
import requests
import os

from tqdm import tqdm
from pathlib import Path

env_path = Path(__file__).parent / ".env2"

with open(env_path, "r", encoding="utf-8") as f:
    API_KEY = f.read().strip()

# إعدادات OpenRouter API
API_URL = "https://openrouter.ai/api/v1/chat/completions"

MODEL = "openai/gpt-3.5-turbo"  # يمكنك تغيير النموذج حسب الحاجة

# MODEL = "openai/gpt-oss-20b:free"  # يمكنك تغيير النموذج حسب الحاجة
MODEL = "z-ai/glm-4.5-air:free"  # يمكنك تغيير النموذج حسب الحاجة


def dump_all(cache_file, data):
    print("<<green>> dump_all():")

    # حفظ ملف JSON المحدث
    with open(cache_file, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

    print(" Dump saved to: data_translated.json")


def translate_text(text):
    """ترجمة النص من الإنجليزية إلى العربية باستخدام OpenRouter API"""
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = (
        "ترجم النص التالي ترجمة عربية طبيعية موجزة ومناسبة لوصف/وسم ويكي بيانات:\n\n"
        f"النص:\n{text}\n\n"
        "تعليمات:\n- إن كان النص اسمًا علميًا/تقنيًا شائع التعريب فعرّبه، وإن كان اسمًا ذاتيًا (اسم شخص/مكان/مؤسسة) فحافظ عليه كما هو إن لم يكن له تعريب راسخ.\n"
        "- لا تضف تعليقات.\n"
    )
    # ---
    prompt2 = f"Translate to Arabic: {text}"
    # ---
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "system", "content": "You are a professional translator. Translate the following English text to Arabic accurately and naturally."},
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = requests.post(API_URL, headers=headers, json=payload, timeout=5)
        response.raise_for_status()
        result = response.json()
        translation = result['choices'][0]['message']['content'].strip()
        return translation
    except Exception as e:
        print(f" error: {e}")
        return None


cache_file = Path(__file__).parent / "cache_data_new.json"

# تحميل ملف JSON
with open(cache_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

n = 0

data_to_translate = {x: v for x, v in data.items() if not v.get("label", {}).get("ar") or not v.get("description", {}).get("ar")}


for prop_id, prop_data in tqdm(data_to_translate.items()):
    # ---
    n += 1
    # ---
    ar_label = prop_data.get('label', {}).get('ar', '')
    ar_desc = prop_data.get('description', {}).get('ar', '')
    # ---
    if ar_label and ar_desc:
        continue
    # ---
    if n % 10 == 0:
        dump_all(cache_file, data)
    # ---
    en_label = prop_data.get('label', {}).get('en', '')
    en_desc = prop_data.get('description', {}).get('en', '')
    # ---
    # ترجمة التسمية إذا كان الحقل العربي فارغًا
    if en_label and not ar_label:
        # ---
        print(f"translate label {prop_id}: ({en_label})")
        # ---
        translation = translate_text(en_label)
        # ---
        if translation:
            data[prop_id]['label']['ar'] = translation
            # ---
            print(f"-> result: ({translation})")

    # ترجمة الوصف إذا كان الحقل العربي فارغًا
    if en_desc and not ar_desc:
        # ---
        print(f"translate description {prop_id}: ({en_desc})")
        # ---
        translation = translate_text(en_desc)
        # ---
        if translation:
            data[prop_id]['description']['ar'] = translation
            # ---
            print(f"-> result: ({translation})")


dump_all(cache_file, data)

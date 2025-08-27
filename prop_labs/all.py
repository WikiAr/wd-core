#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

!pip install SPARQLWrapper

https://colab.research.google.com/drive/1EKsGjGkFa8csw4qwT0kQmASrYJrwAGVb#scrollTo=mHKQes0100lT

"""
import os
import sys
import time
import json
from typing import Dict, List, Optional, Tuple
import tqdm
import argparse
import requests
import google.generativeai as genai
from google.colab import userdata
from collections import namedtuple

from SPARQLWrapper import SPARQLWrapper, JSON

WDQS_ENDPOINT = "https://query.wikidata.org/sparql"
MW_API = "https://www.wikidata.org/w/api.php"

HEADERS_API = {
    "User-Agent": "WD-Ar-Props-Filler/1.0 (contact: your-email@example.com)"
}

username = userdata.get('hiacc')
password = userdata.get('hipass')
api_key = userdata.get('GOOGLE_API_KEY')

# =========================
# MediaWiki: جلسة وتوكينات
# =========================
ask_user = {1: False}

if "ask" in sys.argv:
    ask_user[1] = True
    sys.argv.remove("ask")

genai.configure(api_key=api_key)

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_NONE",
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_NONE",
    },
]

instractions = """أنت مترجم محترف من اللغة الإنجليزية إلى اللغة العربية، أحرص على الترجمة بلغة سليمة لغويًا ونحويًا وإملائيًا، واتبع قواعد الإملاء والنحو التالية للحصول على ترجمة سليمة:
* عند الترجمة من الانجليزية إلي العربية, ابحث عن الفعل و أبدأ به الحملة العربية.
* الصفة تسبق الموصوف في الانجليزية و لا تجمع بينما تأتي بعد الموصوف في العربية.
* الجملة المبنية للمجهول في الانجليزية تترجم كجملة مبنية للمعلوم في العربية، مثال \"A new hospital is being built by the government in our village\" تُترجم إلى \"تبني الحكومة مستشفى جديدة في قريتنا\".
* الجملة الاسمية في العربية تترجم إلي جملة فعلية في الانجليزية باستخدام (to be)، مثال \"Egypt is rich in its natural resources\" تُترجم إلى \"إن مصر غنية بثرواتها الطبيعية\".
* يجب مراعاة ترجمة (to be / to have) للعربية لما لهما من تراجم عديدة حسب السياق.
* استخدم اسماء الشهور الإنجليزية مثل (يناير، فبراير، مارس، أبريل) لا داعي لاستخدام (كانون الثاني، شباط، آذار، نيسان)
* الضمير المضاف إلى اسم يترجم إلى صفة ملكية (my – his – her – its – our – your – their ) .
* الضمير المضاف إلى فعل يترجم ضمير مفعول ( me – him – her – it – us – you – them)
* راعي ربط الجمل مع بعضها عند الترجمة إلي العربية بكلمات مثل (حيث / من ثم / كذلك / هكذا).

* لا تستخدم تم في ترجمة الأفعال، وبدلا من ذلك انسبها للمجهول:
** بدلًا من: (تم بناء) أكتب: (بُني).
** بدلًا من: (تم إطلاق) أكتب: (أطلق).
** بدلًا من: (تم إطلاقها) أكتب: (أطلقت).
** بدلًا من: (تم الإعلان) أكتب: (أُعلن).
** بدلًا من: (تم السماح) أكتب: (سُمح).
** بدلًا من: (تم الكشف) أكتب: (كُشف).
** بدلًا من: (تم بيعها) أكتب: (بيعت).
** بدلًا من: (تم تعديله) أكتب: (عُدل).
** بدلًا من: (تم تنزيله) أكتب: (نُزل).
** بدلًا من: (تمت كتابة الورقة البحثية الأصلية بواسطة الباحث وزملائه) أكتب: (كتب الباحث وزملائه الورقة البحثية الأصلية).

ملاحظة أخيرة: قلل من استخدام الحركات التشكيلية، وأحرص على ترجمة أسماء الشركات والمؤسسات والأشخاص وأي اسم إنجليزي إلى العربية

في حالة وجود أرقام المصادر في النص، حافظ عليها في أماكنها

"""


data_parts = [
    {
        "en": """A mass grave with 283 bodies was uncovered in April 2024 at Khan Younis's Nasser medical complex in Gaza City. Further mass graves with several hundreds of bodies were found in the courtyard of Al-Shifa Hospital.[144][145] Reports indicated that some of the bodies were found with their hands and feet tied.[146][147] Following the discovery of the mass graves, UN human rights chief Volker Türk called for an independent investigation on the intentional killing of civilians by the Israeli Defense Forces. He stated the "intentional killing of civilians, detainees, and others who are hors de combat is a war crime."[148][149] A spokesperson for the U.N. High Commissioner for Human Rights described the discoveries, stating, "Some of them had their hands tied, which of course indicates serious violations of international human rights law and international humanitarian law, and these need to be subjected to further investigations".[150] William Schabas, a Canadian expert on international human rights law, stated mass graves have "always been an indication that war crimes have been committed".[151]""",
        "ar": """كُشف عن مقبرة جماعية تضم 283 جثة في أبريل/نيسان 2024 في مجمع ناصر الطبي بخان يونس في مدينة غزة. كذلك عُثر على مقابر جماعية أخرى تضم عدة مئات من الجثث في فناء مستشفى الشفاء.[144][145] أشارت تقارير إلى أن بعض الجثث عُثر عليها وقد رُبطت أيديها وأرجلها.[146][147] في أعقاب اكتشاف المقابر الجماعية، دعا مفوض الأمم المتحدة السامي لحقوق الإنسان فولكر تورك إلى إجراء تحقيق مستقل في القتل العمد للمدنيين على يد قوات الدفاع الإسرائيلية. صرح بأن "القتل العمد للمدنيين والمعتقلين وغيرهم ممن هم خارج نطاق القتال هو جريمة حرب".[148][149] ووصف متحدث باسم المفوض السامي للأمم المتحدة لحقوق الإنسان هذه الاكتشافات، قائلاً: "كانت أيدي بعضهم مقيدة، مما يشير بالطبع إلى انتهاكات خطيرة للقانون الدولي لحقوق الإنسان والقانون الإنساني الدولي، ويجب إخضاعها لمزيد من التحقيقات".[150] وصرح ويليام شاباس، الخبير الكندي في القانون الدولي لحقوق الإنسان، بأن المقابر الجماعية "لطالما كانت دليلاً على ارتكاب جرائم حرب".[151]"""
    },
    {
        "en": 'As of February and March, similar protests and calls for divestment had already been occurring at Goldsmiths, University of London, the University of Leeds, and the University of Bristol. After a campaign from students, the University of York announced on 27 April it "no longer holds investments in companies that primarily make or sell weapons and defence-related products or services".',
        "ar": 'كانت احتجاجاتٌ مماثلة ودعواتٌ لسحبِ الاستثمارات قد اندلعت بالفعل في جامعات جولدسميث، ولندن، وليدز، وبريستول، وذلك بدءًا من فبراير ومارس. وبعد حملةٍ من الطلاب، أعلنتْ جامعة يورك في 27 أبريل أنها "لم تعدْ تُبقي على استثماراتٍ في الشركات التي تَصنع أو تبيعُ في المقام الأول الأسلحة والمنتجات أو الخدمات المتعلقة بالدفاع". '
    },
    {
        "en": "On the evening of April 19, students from the University of Warwick occupied the campus piazza. On April 22, students from the University of Leicester Palestine Society held a protest. On April 26, a rally was held by students of University College London (UCL) on campus, though they had been campaigning for months. UCL Action for Palestine won a meeting with senior members of university's management, also on 26 April, to discuss divestment and propose aiding Palestinian students whose universities had been destroyed.\n\nOn May 1, encampments were established at the University of Bristol, the University of Leeds, the University of Manchester, and Newcastle University, as well as a joint one between the University of Sheffield and Sheffield Hallam University. On May 3, protesters set up an encampment at University College, London. Protesters also occupied the library at Goldsmiths, University of London. Goldsmiths agreed to the protester's demands, naming a building after Palestinian journalist Shireen Abu Akleh, review the University's policy regarding the IHRA working definition of antisemitism, and to erect an installation on campus memorializing the protest.",
        "ar": 'في مساء يوم 19 أبريل، احتلَّ طلابٌ من جامعة وارويك ساحة الحرم الجامعي. وفي 22 أبريل، نظَّم طلابٌ من جمعية فلسطين بجامعة ليستر احتجاجًا. وفي 26 أبريل، نظَّم طلابٌ من كلية لندن الجامعية (UCL) مسيرةً في الحرم الجامعي، على الرغم من أنهم كانوا يُنظمون حملاتٍ منذ شهور. وقد فازَتْ مجموعة "عمل لندن من أجل فلسطين" بلقاءٍ مع أعضاءٍ بارزين في إدارة الجامعة، أيضًا في 26 أبريل، لمناقشة سحب الاستثمارات واقتراحِ مساعدةِ الطلاب الفلسطينيين الذين دُمِّرت جامعاتُهم.\n\nوفي الأول من مايو، أُقيمتْ اعتصاماتٌ في جامعة بريستول، وجامعة ليدز، وجامعة مانشستر، وجامعة نيوكاسل، بالإضافة إلى اعتصامٍ مُشتركٍ بين جامعة شيفيلد وجامعة هالام شيفيلد. وفي 3 مايو، أقامَ المُحتجُّون اعتصامًا في كلية لندن الجامعية. واحتلَّ المُحتجُّون أيضًا المكتبة في جامعة جولدسميث في لندن. وقد وافقتْ جولدسميث على مطالب المُحتجِّين، فأطلقتْ اسمَ الصحفية الفلسطينية شيرين أبو عاقلة على أحدِ المباني، ومراجعة سياسة الجامعة فيما يتعلق بتعريف IHRA العامل لمعاداة السامية، وإقامةِ نصبٍ تذكاريٍّ للاحتجاج في الحرم الجامعي. '
    },
    {
        "en": """""",
        "ar": """"""
    },
    {
        "en": """""",
        "ar": """"""
    }
]

contents = []

for x in data_parts:
    ar = x["ar"]
    en = x["en"]
    # ---
    if ar and en:
        contents.append({
            "role": "user",
            "parts": [
                en,
            ],
        })
        contents.append({
            "role": "model",
            "parts": [
                ar,
            ],
        })


def send_ai(text):
    time_start = time.time()

    model = genai.GenerativeModel(
        # model_name="gemini-2.0-flash-lite",
        model_name="gemini-2.5-flash-preview-05-20",
        safety_settings=safety_settings,
        generation_config=generation_config,

        system_instruction=instractions,
    )

    contents.append({
        "role": "user",
        "parts": [
            text,
        ],
    })

    chat_session = model.start_chat(
        history=contents
    )

    response = chat_session.send_message(text)

    delta = time.time() - time_start
    # ---
    print(f"delta: {delta}")
    # ---
    contents.append({
        "role": "model",
        "parts": [
            response.text,
        ],
    })
    # ---
    return response.text


def translate_en_to_ar(en: str) -> str:
    # ---
    en = (en or "").strip()
    # ---
    if not en:
        return ""
    # ---
    prompt = (
        "ترجم النص التالي ترجمة عربية طبيعية موجزة ومناسبة لوصف/وسم ويكي بيانات:\n\n"
        f"النص:\n{en}\n\n"
        "تعليمات:\n- إن كان النص اسمًا علميًا/تقنيًا شائع التعريب فعرّبه، وإن كان اسمًا ذاتيًا (اسم شخص/مكان/مؤسسة) فحافظ عليه كما هو إن لم يكن له تعريب راسخ.\n"
        "- لا تضف تعليقات أو أقواس.\n"
    )
    # ---
    print(f"start translate: {en}")
    # ---
    text = send_ai(prompt)
    # ---
    return text


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
        print(f"<<yellow>> [ask][{pid}] Add AR {field}: '{value}'")
        ans = input("(y/n)?").strip().lower()
        # ---
        answers = ["y", "yes", "", "a"]
        # ---
        if ans == "a":
            self.save_all = True
            print("<<green>> SAVE ALL Without Asking\n" * 3)
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
                print(f"<<green>> [ok][{pid}] label set.")

            print(f"time.sleep({args.sleep})")
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
                print(f"<<green>> [ok][{pid}] description set.")

            print(f"time.sleep({args.sleep})")
            time.sleep(args.sleep)

    print(f"[*] finished. labels added: {done_labels}, descriptions added: {done_descs}")


args = namedtuple("args", ["limit", "offset", "sleep", "only", "dry_run"])

args.limit = 200
args.offset = 0
args.sleep = 0.1
args.only = "both"
args.dry_run = ""

start(args)

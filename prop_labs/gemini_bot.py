"""

python3 core8/pwb.py I:/core/bots/wd_core/prop_labs/gemini_bot.py


"""

import tqdm
from pathlib import Path
import google.generativeai as genai
import time

env_path = Path(__file__).parent / ".env"

with open(env_path, "r", encoding="utf-8") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)

Dir = Path(__file__).resolve().parent

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

"""

contents = []


def send_ai(text):
    time_start = time.time()

    model = genai.GenerativeModel(
        model_name="gemini-2.0-flash-lite",
        # model_name="gemini-2.5-flash-preview-05-20",
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


def start():
    file = Dir / "old.txt"
    file2 = Dir / "new.txt"
    # ---
    text = file.read_text("utf-8")
    # ---
    new_text = text
    # ---
    ssplits = [x.strip() for x in text.splitlines() if x.strip()]
    # ---
    time_start = time.time()
    # ---
    for n, x in enumerate(tqdm.tqdm(ssplits), 1):
        print("____")
        # ---
        if not x.strip():
            continue
        # ---
        print(x)
        # ---
        new_x = send_ai(x)
        new_x = f"# part:{n} \n {new_x}"
        # ---
        print(new_x)
        # ---
        new_text = new_text.replace(x, new_x)
    # ---
    file2.write_text(new_text, "utf-8")
    # ---
    end = time.time() - time_start
    # ---
    print(f"end at: {end}")


if __name__ == "__main__":
    start()

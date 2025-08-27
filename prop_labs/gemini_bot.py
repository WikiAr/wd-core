"""

python3 core8/pwb.py I:/core/bots/wd_core/prop_labs/gemini_bot.py


"""

import tqdm
from pathlib import Path
import google.generativeai as genai
import time

env_path = Path(__file__).parent / ".env"

with open(env_path, "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)

Dir = Path(__file__).resolve().parent
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

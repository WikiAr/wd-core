"""

from .cy_regs import make_data_new

python3 I:/core/bots/wd_core/cy/cy_bot/cy_regs.py

"""
import wikitextparser as wtp

from .cy_helps import get_temp_arg


def make_data_new(text):
    # ---
    tab = {}
    # ---
    temp_name = "نتيجة سباق الدراجات/سطر4"
    # ---
    parser = wtp.parse(text)
    # ---
    for template in parser.templates:
        # ---
        temp_str = template.string
        # ---
        if not temp_str or temp_str.strip() == "":
            continue
        # ---
        name = str(template.normal_name()).strip()
        # ---
        if name == temp_name:
            q_id = get_temp_arg(template, "qid")
            # ---
            if not q_id:
                continue
            # ---
            tab[q_id] = {}
            tab[q_id]["qid"] = q_id
            tab[q_id]["poss"] = get_temp_arg(template, "المركز")
            tab[q_id]["rank"] = get_temp_arg(template, "المرتبة")
            # ---
            if not tab[q_id]["rank"]:
                tab[q_id]["rank"] = get_temp_arg(template, "rank")
            # ---
            tab[q_id]["race"] = get_temp_arg(template, "السباق")
            tab[q_id]["p17"] = get_temp_arg(template, "البلد")
            tab[q_id]["jersey"] = get_temp_arg(template, "جيرسي")
    # ---
    return tab


def test():
    text = """{{نتيجة سباق الدراجات/سطر4
|qid = Q110775370
|السباق = 2022 Tour de Romandie Féminin
|البلد = {{رمز علم|سويسرا}}
|التاريخ = 2022-10-09T00:00:00Z
|المركز = الفائز في التصنيف العام
|المرتبة = الأول في التصنيف العام، الثالث في تصنيف الجبال، السادس في تصنيف النقاط
|جيرسي = {{نتيجة سباق الدراجات/جيرسي|Jersey_green.svg|قميص أخضر لمتصدر الترتيب العام}}
}}"""
    # ---
    tab2 = make_data_new(text)
    # ---
    print(tab2)


if __name__ == "__main__":
    test()

"""

from .cy_regs import regline

"""
import re

regline = r"\{\{نتيجة سباق الدراجات/سطر4"
regline += r"\|\s*qid\s*\=(?P<qid>Q\d+)"
regline += r"\|\s*السباق\s*\=(?P<race>.*)"
regline += r"\|\s*البلد\s*\=(?P<p17>.*)"
regline += r"\|\s*التاريخ\s*\=(?P<date>.*)"
regline += r"\|\s*المركز\s*\=(?P<poss>.*)"
regline += r"\|\s*(?:rank|المرتبة)\s*\=(?P<rank>.*)"
regline += r"\|\s*جيرسي\s*\=(?P<jersey>.*)"
regline += r"\s*\|\}\}"


def make_data(text):
    # ---
    # reg_line = r"\{\{نتيجة سباق الدراجات\/سطر4([^{]|\{[^{]|\{\{[^{}]+\}\})+\}\}"
    # re.compile(reg_line)
    # ---
    comont = "<!-- هذه القائمة يقوم بوت: [[مستخدم:Mr._Ibrahembot]] بتحديثها من ويكي بيانات بشكل دوري. -->"
    # ---
    if text.startswith("{{نتيجة سباق الدراجات/بداية}}\n" + comont):
        text = text.replace("{{نتيجة سباق الدراجات/بداية}}\n" + comont, "")
    # ---
    text = text.replace("{{نتيجة سباق الدراجات/نهاية}}", "")
    text = text.strip()
    # ---
    tab = {}
    # ---
    vf = text.split("{{نتيجة سباق الدراجات/سطر4")
    # ---
    if vf:
        # ---
        for pp in vf:
            if not pp:
                continue
            # ---
            if not pp.startswith("{{نتيجة سباق الدراجات/سطر4"):
                pp = "{{نتيجة سباق الدراجات/سطر4" + pp
            # ---
            q_id = ""
            ppr = re.sub(r"\n", "", pp)
            # ---
            q_id = re.sub(r"\{\{نتيجة سباق الدراجات\/سطر4\|qid\s*\=\s*(Q\d+)\|.*\}\}", r"\g<1>", ppr)
            # ---
            if hhh := re.match(r".*(Q\d+).*", ppr):
                if q_id != hhh.group(1):
                    q_id = hhh.group(1)
            # ---
            tab[q_id] = {}
            tab[q_id]["qid"] = q_id
            tab[q_id]["poss"] = re.sub(regline, r"\g<poss>", ppr)
            tab[q_id]["rank"] = re.sub(regline, r"\g<rank>", ppr)
            tab[q_id]["race"] = re.sub(regline, r"\g<race>", ppr)
            tab[q_id]["p17"] = re.sub(regline, r"\g<p17>", ppr)
    # ---
    return tab

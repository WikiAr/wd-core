#!/usr/bin/python3
"""
tfj run jsubx --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/jsub -ns:10 -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات/قوالب"

python3 core8/pwb.py cy/jsub -page:جيروين_بلايلفينس ask
python3 core8/pwb.py cy/jsub -page:إديتا_بوتشينسكايتي
python3 core8/pwb.py cy/jsub -page:
python3 core8/pwb.py cy/jsub -page:قالب:نتيجة_سباق_الدراجات/ميغيل_إندوراين
python3 core8/pwb.py cy/jsub -page:قالب:نتيجة_سباق_الدراجات/ألبيرتو_كونتادور
python3 core8/pwb.py cy/jsub -page:
python3 core8/pwb.py cy/jsub -page:
python3 core8/pwb.py cy/jsub -page:كريس_فروم

python3 core8/pwb.py cy/jsub -ref:قالب:نتيجة_سباق_الدراجات/بداية
python3 core8/pwb.py cy/jsub -cat:
python3 core8/pwb.py cy/jsub -ns:10 -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات/قوالب
python3 core8/pwb.py cy/jsub -cat:
python3 core8/pwb.py cy/jsub -cat:
python3 core8/pwb.py cy/jsub -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات

https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Gathering_data_from_Arabic-Wikipedia

"""
# ---
from newapi.page import MainPage

from cy_bot.do_text import do_One_Page
import gent

skip_titles = [
    "قالب:نتيجة سباق الدراجات",
    "قالب:نتيجة سباق الدراجات/بداية",
]


def onep(title):
    # ---
    if title in skip_titles:
        return
    # ---
    page = MainPage(title, "ar", family="wikipedia")
    # ---
    if not page.exists():
        return
    # ---
    if not page.can_edit():
        return
    # ---
    if page.isDisambiguation():
        return
    # ---
    if page.isRedirect():
        return
    # ---
    text = page.get_text()
    # ---
    item = page.get_qid()
    # ---
    new_text = do_One_Page(title, text, item)
    # ---
    if not new_text:
        print(f"لا توجد نتائج لهذه الصفحة تأكد من صحة معرف ويكي بيانات: {item}.")
        return
    # ---
    if new_text == text:
        print("no changes")
        return
    # ---
    if new_text:
        page.save(newtext=new_text, summary="بوت:تجربة تحديث بيانات اللاعب")


def main2(*args):
    generator = gent.get_gent(listonly=True, *args)
    # ---
    for numb, pagetitle in enumerate(generator, start=1):
        print(f"page: {numb} : {pagetitle}")
        onep(pagetitle)


if __name__ == "__main__":
    main2()

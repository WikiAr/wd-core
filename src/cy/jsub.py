#!/usr/bin/python3
"""

https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Gathering_data_from_Arabic-Wikipedia

"""

from shared.api_page import load_main_api
from wd_core import wd_gent
from wd_core.cy.cy_bot.do_text import do_One_Page

skip_titles = [
    "قالب:نتيجة سباق الدراجات",
    "قالب:نتيجة سباق الدراجات/بداية",
]


def onep(title) -> None:
    # ---
    if title in skip_titles:
        return
    # ---
    ar_api = load_main_api("ar", "wikipedia")
    # ---
    page = ar_api.MainPage(title)
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


def main2() -> None:
    generator = wd_gent.get_gent_list()
    # ---
    for numb, pagetitle in enumerate(generator, start=1):
        print(f"page: {numb} : {pagetitle}")
        onep(pagetitle)


if __name__ == "__main__":
    main2()

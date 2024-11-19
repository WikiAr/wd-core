#!/usr/bin/python3
"""
python pwb.py cy/cy5 -page:باتريك_كونراد
python pwb.py cy/cy5 -page:جويل_سوتير
python pwb.py cy/cy5 -page:كريس_فروم

python pwb.py cy/cy5  ask -title:إديتا_بوتشينسكايتي
python pwb.py cy/cy5 workibrahem test2 -title:خوان_سباستيان_مولانو
python pwb.py cy/cy5 workibrahem test2 -title:إليسا_ونغو_بورغيني ask
python pwb.py cy/cy5 workibrahem test2 -title:كوين_سيمونز

"""

import sys

# ---
try:
    from .cy_api import page_put, GetPageText
    from .do_text import do_One_Page
    from .cy_helps import printt, printo, TEST
except Exception:
    from cy.cy_api import page_put, GetPageText
    from cy.do_text import do_One_Page
    from cy.cy_helps import printt, printo, TEST
# ---
workibrahem = "workibrahem" in sys.argv
# ---
br = "</br>"


def StartOnePage(title):
    printt("**StartOnePage: <br>")
    # ---
    title = title.replace("_", " ")
    # ---
    text, item = GetPageText(title)
    # ---
    if not text:
        printo("الصفحة المطلوبة غير موجودة أو أن محتواها فارغ.")
        return
    # ---
    NewText = do_One_Page(title, text, item)
    # ---
    if not NewText:
        ur = f'<a href="https://www.wikidata.org/wiki/{item}">{item}</a>.'
        printo(f"لا توجد نتائج لهذه الصفحة تأكد من صحة معرف ويكي بيانات: {ur}.")
        return
    # ---
    page_put(NewText, title)


def main():
    # ---
    title = ""
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        # ---
        if arg in ["-title", "-page"]:
            title = value
    # ---
    if TEST[1]:
        printt("TestMain:<br>")
        # python pwb.py cy5 test
        StartOnePage("%D8%B1%D9%8A%D8%AA%D8%B4%D9%8A_%D8%A8%D9%88%D8%B1%D8%AA")
    # make_new_text('Q286183')#
    # ---
    if title:
        StartOnePage(title)
    else:
        printo('title==""')


if __name__ == "__main__":
    main()

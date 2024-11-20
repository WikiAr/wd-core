#!/usr/bin/python3
"""
python3 /data/project/himo/bots/wd_core/cy/cy6.py -title:إديتا_بوتشينسكايتي
python3 /data/project/himo/bots/wd_core/cy/cy6.py -title:جيروين_بلايلفينس

python3 core8/pwb.py cy/cy6 -title:جيروين_بلايلفينس
python3 core8/pwb.py cy/cy6 -title:إديتا_بوتشينسكايتي
python3 core8/pwb.py cy/cy6 -title:
python3 core8/pwb.py cy/cy6 -title:
python3 core8/pwb.py cy/cy6 -title:


python3 core8/pwb.py cy/cy6 -title:باتريك_كونراد
python3 core8/pwb.py cy/cy6 -title:جويل_سوتير
python3 core8/pwb.py cy/cy6 -title:كريس_فروم

python3 core8/pwb.py cy/cy6 -title:إديتا_بوتشينسكايتي
python3 core8/pwb.py cy/cy6 workibrahem test2 -title:خوان_سباستيان_مولانو
python3 core8/pwb.py cy/cy6 workibrahem test2 -title:إليسا_ونغو_بورغيني ask
python3 core8/pwb.py cy/cy6 workibrahem test2 -title:كوين_سيمونز

"""

import sys

# ---
from cy_bot.cy_api import page_put, GetPageText
from cy_bot.do_text import do_One_Page
from cy_bot.cy_helps import printt, printo, TEST

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
        # python3 core8/pwb.py cy6 test
        StartOnePage("%D8%B1%D9%8A%D8%AA%D8%B4%D9%8A_%D8%A8%D9%88%D8%B1%D8%AA")
    # make_new_text('Q286183')#
    # ---
    if title:
        StartOnePage(title)
    else:
        printo('title==""')


if __name__ == "__main__":
    main()

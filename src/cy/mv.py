#!/usr/bin/python3
"""

python3 core8/pwb.py cy/mv -ns:0 -ref:قالب:نتيجة_سباق_الدراجات/بداية ask nodiff
python3 core8/pwb.py cy/mv -ns:0 -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات nofa

https://www.wikidata.org/wiki/Wikidata:Pywikibot_-_Python_3_Tutorial/Gathering_data_from_Arabic-Wikipedia

tfj run jsuw1 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/mv -ns:0 -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات p1 nofa"
tfj run jsuw2 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/mv -ns:0 -cat:تصنيف:سجل_فوز_دراج_من_ويكي_بيانات p2 nofa"
tfj run jsubp2 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/mv -ns:0 -ref:قالب:نتيجة_سباق_الدراجات/بداية p2"
tfj run jsubp3 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/mv -ns:0 -ref:قالب:نتيجة_سباق_الدراجات/بداية p3"
tfj run jsubp4 --image python3.9 --command "$HOME/local/bin/python3 core8/pwb.py cy/mv -ns:0 -ref:قالب:نتيجة_سباق_الدراجات/بداية p4"

"""
# ---
import wikitextparser as wtp
from newapi.page import MainPage

import logging
logger = logging.getLogger(__name__)

import tqdm
import sys
import gent

def add_id_to_text(item, text):
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
        if name == "نتيجة سباق الدراجات/بداية":
            template.set_arg("id", item)
            template.set_arg("قالب", "t")
            break
    # ---
    text = parser.string
    # ---
    return text

def move_it_to_temp(title, item, text):
    # ---
    if not text:
        return
    # ---
    temp_title = f"قالب:نتيجة سباق الدراجات/{title}"
    # ---
    text = add_id_to_text(item, text)
    # ---
    temp_page = MainPage(temp_title, "ar", family="wikipedia")
    # ---
    if temp_page.exists():
        do = temp_page.save(text, summary="بوت:تجربة تحديث بيانات اللاعب")
    else:
        do = temp_page.Create(text, summary="بوت:تجربة تحديث بيانات اللاعب")
    # ---
    return do

def find_cy_temp(text):
    start = "{{نتيجة سباق الدراجات/بداية"
    end = "{{نتيجة سباق الدراجات/نهاية}}"
    # ---
    start_pos = text.find(start)
    if start_pos < 0:
        return
    # ---
    end_pos = text.find(end)
    if end_pos < 0:
        return
    # ---
    if end_pos < start_pos:
        return
    # ---
    end_pos += len(end)
    # ---
    return text[start_pos:end_pos]

def one_page_work(title, text, item):
    # ---
    cy_temp = find_cy_temp(text)
    # ---
    if not cy_temp:
        logger.info(f"no cy temp on {title}")
        return text
    # ---
    temp = move_it_to_temp(title, item, cy_temp)
    # ---
    if not temp:
        return text
    # ---
    new_temp = f"{{{{نتيجة سباق الدراجات/{title}}}}}"
    # ---
    if text.find(cy_temp) != -1:
        text = text.replace(cy_temp, new_temp)
    # ---
    return text

def onep(title):
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
    ns = page.namespace()
    # ---
    if ns != 0:
        logger.info(f"<<red>> page:{title} {ns=} not in main namespace.")
        return
    # ---
    text = page.get_text()
    # ---
    item = page.get_qid()
    # ---
    # new_text = make_new_text(item, title, text)
    new_text = one_page_work(title, text, item)
    # ---
    if not new_text:
        logger.info("no new text!!")
        return
    # ---
    if new_text.find("{{نتيجة سباق الدراجات/بداية") != -1 or new_text.find("{{نتيجة سباق الدراجات/نهاية}}") != -1:
        logger.info("error when replacing templates")
        return
    # ---
    if new_text == text:
        logger.info("no changes")
        return
    # ---
    if new_text:
        page.save(newtext=new_text, summary="بوت:تجربة تحديث بيانات اللاعب")

def split_pages(pages, parts=4):
    length = len(pages)
    part_size = length // parts
    remaining = length % parts

    # Create a dictionary to store the split parts
    parts_dict = {}
    start_index = 0
    for i in range(parts):
        end_index = start_index + part_size + (1 if i < remaining else 0)
        parts_dict[f"p{i+1}"] = pages[start_index:end_index]
        start_index = end_index

    # Return the specified part or the original list
    for part_name, part_pages in parts_dict.items():
        if part_name in sys.argv:
            logger.info(f"<<yellow>> part: {part_name}: {len(part_pages):,}")
            return part_pages

    return pages

def main2(*args):
    generator = gent.get_gent(listonly=True, *args)
    # ---
    list_of_pages = [x for x in tqdm.tqdm(generator)]
    # ---
    list_of_pages = split_pages(list_of_pages)
    # ---
    for numb, pagetitle in enumerate(list_of_pages, start=1):
        logger.info(f"<<yellow>> page: {numb}/{len(list_of_pages)} : {pagetitle}")
        onep(pagetitle)

if __name__ == "__main__":
    main2()

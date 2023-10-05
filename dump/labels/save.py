"""
python3 core8/pwb.py dump/labels/save
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os
# ---
from wd_API import himoAPI
# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r'I:\core\dumps'):
    Dump_Dir = r'I:\core\dumps'
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
file_to_title = {
    'labels.txt': 'User:Mr. Ibrahem/Language statistics for items',
    'template.txt': 'Template:Tr langcodes counts',
}
# ---
if 'test' in sys.argv:
    file_to_title['labels_test.txt'] = 'User:Mr. Ibrahem/Language statistics for items/sandbox'
    file_to_title['template_test.txt'] = 'Template:Tr langcodes counts/sandbox'
# ---
for file, title in file_to_title.items():
    if os.path.exists(f"{Dump_Dir}/texts/{file}"):
        text = open(f"{Dump_Dir}/texts/{file}", encoding="utf-8").read()
        # ---
        if text.strip() == "":
            print(f'file {file} <<lightred>> empty.')
            continue
        # ---
        if file == 'labels.txt' and len(text) < 50000:
            print(f'file {file} <<lightred>> too small.')
            continue
        # ---
        if file == 'template.txt' and len(text) < 5000:
            print(f'file {file} <<lightred>> too small.')
            continue
        # ---
        himoAPI.page_putWithAsk("", text, "Bot - Updating stats", title, False)

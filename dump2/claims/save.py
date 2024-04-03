"""
python3 core8/pwb.py dump/claims/save
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os

# ---
from wd_api import himoAPI

# ---
Dump_Dir = "/data/project/himo/dumps"
# ---
if os.path.exists(r'I:\core\dumps'):
    Dump_Dir = r'I:\core\dumps'
# ---
print(f'Dump_Dir:{Dump_Dir}')
# ---
file_to_title = {
    'claims_new.txt': 'User:Mr. Ibrahem/claims',
    'claims_p31.txt': 'User:Mr. Ibrahem/p31',
}
# ---
if 'test' in sys.argv:
    file_to_title = {
        'claims_new_test.txt': 'User:Mr. Ibrahem/claims/sandbox',
        'claims_p31_test.txt': 'User:Mr. Ibrahem/p31/sandbox',
    }
# ---
for file, title in file_to_title.items():
    if os.path.exists(f"{Dump_Dir}/texts/{file}"):
        text = open(f"{Dump_Dir}/texts/{file}", encoding="utf-8").read()
        # ---
        if text.strip() == "":
            print(f'file {file} <<lightred>> empty.')
            continue
        # ---
        if file == 'claims_new.txt' and len(text) < 100000:
            print(f'file {file} <<lightred>> too small.')
            continue
        # ---
        if file == 'claims_p31.txt' and len(text) < 10000:
            print(f'file {file} <<lightred>> too small.')
            continue
        # ---
        himoAPI.page_putWithAsk("", text, "Bot - Updating stats", title, False)

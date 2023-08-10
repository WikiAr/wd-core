"""
python3 wd_core/dump/save.py
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import sys
import os
from pathlib import Path
import json
import time
# ---
from wd_API import himoAPI
# ---
Dump_Dir = Path(__file__).parent
# ---
file_to_title = {
    'lables.txt': 'User:Mr. Ibrahem/Language statistics for items',
    'template.txt': 'Template:Tr langcodes counts',
}
# ---
for file, title in file_to_title.items():
    text = open(f"{Dump_Dir}/{file}", "r", encoding="utf-8").read()
    # ---
    if text.strip() == "":
        print(f'file {file} <<lightred>> empty.')
        continue
    # ---
    himoAPI.page_putWithAsk("", text, "Bot - Updating stats", title, False)

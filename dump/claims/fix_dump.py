"""

python3 wd_core/dump/fix_dumps.py

"""
import os
from pathlib import Path
import sys
import json
import tqdm


def start():
    try:
        # ---
        # Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
        Himo_Dir = Path(__file__).parent.parent.parent.parent  # Dump_Dir:/data/project/himo
        # ---
        Dump_Dir = "/data/project/himo/dumps"
        Dump_Dir = f"{Himo_Dir}/dumps"
        # ---
        print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
        # ---
    except Exception as e:
        Dump_Dir = '/content'

    data = json.load(open(f'{Dump_Dir}/claims.json'))
    data2 = {}
    for x, y in data.items():
        if x != 'Main_Table':
            data2[x] = y

    data2['Main_Table'] = {}
    len_props = 0
    for p, pap in tqdm.tqdm(data['Main_Table'].items()):
        # "props": {},"lenth_of_usage": 0,"lenth_of_claims_for_property": 0,
        len_props += 1
        tab = {}
        tab['lenth_of_usage'] = pap['lenth_of_usage']
        tab['lenth_of_claims_for_property'] = pap['lenth_of_claims_for_property']

        tab['len_of_qids'] = len(pap['props'])

        tab['props'] = {}
        others = 0
        # ---
        # sort by usage
        props = pap['props']
        props = {k: v for k, v in sorted(props.items(), key=lambda item: item[1], reverse=True)}
        # ---
        maxx = 500 if p == 'P31' else 100
        # ---
        # add first 500 properties to dict and other to others
        n = 0
        for k, v in props.items():
            n += 1
            if n <= maxx:
                tab['props'][k] = v
            else:
                others += v
        # print(f'len_props:{len_props}')
        if others > 0:
            tab['props']['others'] = others
        if len(tab['props']) > 0:
            data2['Main_Table'][p] = tab

    P31_tab = data2['Main_Table']['P31']

    data2['Main_Table'] = {k: v for k, v in sorted(data2['Main_Table'].items(), key=lambda item: item[1]['lenth_of_usage'], reverse=True)}

    if '100' in sys.argv:
        # get only first 100 properties
        first_100 = data2['Main_Table'][:100]
        if 'P31' not in first_100:
            first_100['P31'] = P31_tab

        # first_100['other'] = data2['Main_Table'][-100:]

        data2['Main_Table'] = first_100

    json.dump(data2, open(f'{Dump_Dir}/claims2.json', 'w'))


if __name__ == '__main__':
    start()

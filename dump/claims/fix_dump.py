"""

python3 wd_core/dump/fix_dumps.py

"""
import os
from pathlib import Path
import sys
import json
import tqdm
# ---
# Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
Himo_Dir = Path(__file__).parent.parent.parent.parent  # Dump_Dir:/data/project/himo
# ---
Dump_Dir = "/data/project/himo/dumps"
# Dump_Dir = f"{Himo_Dir}/dumps"
# ---
print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
# ---
filename = f'{Dump_Dir}/claims.json'
# ---
if 'test' in sys.argv:
    filename = f'{Dump_Dir}/claims_test.json'

def start():
    data = json.load(open(filename))
    data2 = {}
    for x, y in data.items():
        if x != 'properties':
            data2[x] = y

    data2['properties'] = {}
    len_props = 0
    # ---
    for p, pap in tqdm.tqdm(data['properties'].items()):
        # "qids": {},"lenth_of_usage": 0,"len_prop_claims": 0,
        len_props += 1
        tab = {}
        tab['lenth_of_usage'] = pap['lenth_of_usage']
        tab['len_prop_claims'] = pap['len_prop_claims']

        tab['len_of_qids'] = len(pap['qids'])

        tab['qids'] = {}
        others = 0
        # ---
        # sort by usage
        qids = pap['qids']
        qids = {k: v for k, v in sorted(qids.items(), key=lambda item: item[1], reverse=True)}
        # ---
        maxx = 500 if p == 'P31' else 100
        # ---
        # add first 500 properties to dict and other to others
        n = 0
        for k, v in qids.items():
            n += 1
            if n <= maxx:
                tab['qids'][k] = v
            else:
                others += v
        # print(f'len_props:{len_props}')
        # ---
        if others > 0:
            tab['qids']['others'] = others
        # ---
        if len(tab['qids']) > 0:
            data2['properties'][p] = tab
        # ---
        del tab
        del qids
        del others
    # ---
    P31_tab = data2['properties'].get('P31', {})
    # ---
    data2['properties'] = {k: v for k, v in sorted(data2['properties'].items(), key=lambda item: item[1]['lenth_of_usage'], reverse=True)}

    if '100' in sys.argv:
        # get only first 100 properties
        first_100 = data2['properties'][:100]
        if 'P31' not in first_100:
            first_100['P31'] = P31_tab

        # first_100['other'] = data2['properties'][-100:]

        data2['properties'] = first_100
    # ---
    json.dump(data2, open(f'{Dump_Dir}/claims2.json', 'w'))


if __name__ == '__main__':
    start()

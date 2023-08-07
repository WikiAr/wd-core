"""

python3 wd_core/dump/fix_dumps.py

"""
import os
import sys
import json


def start():
    try:
        Dump_Dir = os.path.dirname(os.path.realpath(__file__))
    except Exception as e:
        Dump_Dir = '/content'

    data = json.load(open(f'{Dump_Dir}/dumps/claims.json'))
    data2 = {}
    for x, y in data.items():
        if x != 'Main_Table':
            data2[x] = y

    data2['Main_Table'] = {}
    len_props = 0
    for p, pap in data['Main_Table'].items():
        # "props": {},"lenth_of_usage": 0,"lenth_of_claims_for_property": 0,
        len_props += 1
        tab = {}
        tab['lenth_of_usage'] = pap['lenth_of_usage']
        tab['lenth_of_claims_for_property'] = pap['lenth_of_claims_for_property']

        tab['props'] = {}
        tab['props']['others'] = 0
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
                tab['props']['others'] += v
        print(f'len_props:{len_props}')

        data2['Main_Table'][p] = tab

    json.dump(data2, open(f'{Dump_Dir}/dumps/claims2.json', 'w'))


if __name__ == '__main__':
    start()

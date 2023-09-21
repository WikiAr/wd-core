"""
python3 wd_core/dump/do_text.py claims2
"""
#
# (C) Ibrahem Qasim, 2023
#
#
import os
from pathlib import Path
import sys
import time
import codecs
import json
# ---
time_start = time.time()
print(f"time_start:{str(time_start)}")
# ---
try:
    # ---
    # Dump_Dir = Path(__file__).parent                      # /data/project/himo/wd_core/dump/labels
    Himo_Dir = Path(__file__).parent.parent.parent.parent  # Dump_Dir:/data/project/himo
    # ---
    Dump_Dir = "/data/project/himo/dumps"
    # Dump_Dir = f"{Himo_Dir}/dumps"
    # ---
    print(f'Himo_Dir:{Himo_Dir}, Dump_Dir:{Dump_Dir}')
    # ---
except Exception as e:
    Dump_Dir = '/content'
# ---
sections_done = {1: 0, 'max': 100}
sections_false = {1: 0}


def make_section(P, table, max_n=51):
    """
    Creates a section for a given property in a table.

    Args:
        P (str): The property value.
        table (dict): The table data.

    Returns:
        str: The section text.

    """
    # ---
    # if sections_done[1] >= sections_done['max']:    return ""
    # ---
    Len = table['lenth_of_usage']
    # ---
    texts = "== {{P|%s}} ==" % P
    # ---
    print(f"make_section for property:{P}")
    texts += f"\n* Total items use these property:{Len:,}"
    # ---
    lnnn = table.get("lenth_of_claims_for_property")
    if lnnn:
        texts += f"\n* Total number of claims with these property:{lnnn:,}"
    # ---
    len_of_qids = table.get("len_of_qids")
    if len_of_qids:
        texts += f"\n* Number of unique qids:{len_of_qids:,}"
    # ---
    texts += "\n"
    print(texts)
    if table["props"] == {}:
        print(f'{P} table["props"] == empty.')
        return ""
    # ---
    if len(table["props"]) == 1 and table["props"].get("others"):
        print(f'{P} table["props"] == empty.')
        return ""
    # ---
    Chart = '{| class="floatright sortable"\n|-\n|\n'
    Chart += "{{Graph:Chart|width=140|height=140|xAxisTitle=value|yAxisTitle=Number\n"
    Chart += "|type=pie|showValues1=offset:8,angle:45\n|x=%s\n|y1=%s\n|legend=value\n}}\n|-\n|}"
    # ---
    tables = """{| class="wikitable sortable plainrowheaders"\n|-\n! class="sortable" | #\n! class="sortable" | value\n! class="sortable" | Numbers\n|-\n"""
    # ---
    lists = {k: v for k, v in sorted(table["props"].items(), key=lambda item: item[1], reverse=True)}
    # ---
    xline = ""
    yline = ""
    # ---
    num = 0
    other = 0
    # ---
    for x, ye in lists.items():
        # ---
        if x == "others":
            other += ye
            continue
        # ---
        num += 1
        if num < max_n:
            Q = x
            if x.startswith("Q"):
                Q = "{{Q|%s}}" % x
            # ---
            tables += f"\n! {num} \n| {Q} \n| {ye:,} \n|-"
            # ---
            xline += f",{x}"
            yline += f",{ye:,}"
        else:
            other += ye
    # ---
    num += 1
    # ---
    Chart = Chart % (xline, yline)
    # ---
    tables += f"\n! {num} \n! others \n! {other:,} \n|-"
    # ---
    tables += "\n|}\n{{clear}}\n"
    # ---
    # texts += Chart.replace("=,", "=") + "\n\n"
    # ---
    texts += tables
    # ---
    sections_done[1] += 1
    # ---
    return texts


# ---
def make_numbers_section(p31list):
    xline = ""
    yline = ""
    # ---
    rows = []
    # ---
    property_other = 0
    # ---
    n = 0
    # ---
    for Len, P in p31list:
        n += 1
        if n < 27:
            xline += f",{P}"
            yline += f",{Len}"
        # ---
        if len(rows) < 101:
            Len = f"{Len:,}"
            P = "{{P|%s}}" % P
            lune = f"| {n} || {P} || {Len} "
            rows.append(lune)
        else:
            property_other += int(Len)
    # ---
    Chart2 = "{| class='floatright sortable' \n|-\n|"
    Chart2 += "{{Graph:Chart|width=900|height=100|xAxisTitle=property|yAxisTitle=usage|type=rect\n"
    Chart2 += f"|x={xline}\n|y1={yline}"
    Chart2 += "\n}}"
    Chart2 += "\n|-\n|}"
    # ---
    Chart2 = Chart2.replace("=,", "=")
    # ---
    rows.append(f"! {n} \n! others \n! {property_other:,}")
    rows = "\n|-\n".join(rows)
    table = (
        "\n{| "
        + f'class="wikitable sortable"\n|-\n! #\n! property\n! usage\n|-\n{rows}\n'
        + "|}"
    )
    # ---
    text = "== Numbers ==\n" f"\n{Chart2}\n{table}"
    # ---
    return text


def make_text(tab, ty=''):
    p31list = [[y["lenth_of_usage"], x] for x, y in tab["Main_Table"].items() if y["lenth_of_usage"] != 0]
    p31list.sort(reverse=True)
    # ---
    final = time.time()
    delta = int(final - time_start)
    # ---
    tab['len_of_all_properties'] = len(tab["Main_Table"])
    # ---
    if not tab.get('file_date'):
        tab['file_date'] = 'latest'
    # ---
    text = (
        "<onlyinclude>;dump date {file_date}</onlyinclude>.\n"
        "* Total items: {All_items:,}\n"
        "* Items without P31: {items_no_P31:,} \n"
        "* Items without claims: {items_0_claims:,}\n"
        "* Items with 1 claim only: {items_1_claims:,}\n"
        "* Total number of claims: {all_claims_2020:,}\n"
        "* Number of properties of the report: {len_of_all_properties:,}\n"
    ).format_map(tab)
    # ---
    text += f"<!-- bots work done in {delta} secounds --> \n--~~~~~\n"
    chart = make_numbers_section(p31list)
    # ---
    text_p31 = ''
    # ---
    if tab["Main_Table"].get('P31'):
        text_p31 = text + make_section('P31', tab["Main_Table"]['P31'], max_n=501)
        # ---
    # ---
    if 'onlyp31' in sys.argv or ty == "onlyp31":
        return text, text_p31
    # ---
    sections = ""
    for Len, P in p31list:
        if sections_done[1] >= sections_done['max']:
            break
        # ---
        sections += make_section(P, tab["Main_Table"][P], max_n=51)
    # ---
    text += f"{chart}\n{sections}"
    # ---
    # text = text.replace("0 (0000)", "0")
    # text = text.replace("0 (0)", "0")
    # ---
    return text, text_p31


if __name__ == "__main__":
    filename = f"{Dump_Dir}/claims.json"

    if 'claims2' in sys.argv:
        filename = f"{Dump_Dir}/claims2.json"

    if 'test' in sys.argv:
        filename = f"{Dump_Dir}/claims_test.json"

    data = json.load(open(filename))

    tab = {
        "done": 0,
        "len_of_all_properties": 0,
        "items_0_claims": 0,
        "items_1_claims": 0,
        "items_no_P31": 0,
        "All_items": 0,
        "all_claims_2020": 0,
        "Main_Table": {},
    }
    # ---
    for x, g in tab.items():
        if not x in data:
            data[x] = g
    # ---
    text, text_p31 = make_text(data, ty='')
    codecs.open(f'{Dump_Dir}/claims_new.txt', 'w', 'utf-8').write(text)
    codecs.open(f'{Dump_Dir}/claims_p31.txt', 'w', 'utf-8').write(text_p31)
    print(text_p31)
    print("log_dump done")

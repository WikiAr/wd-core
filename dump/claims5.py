#!/usr/bin/env python3
"""
python3 pwb.py dump/claims5 jsonnew
python3 pwb.py dump/claims5 makereport
python3 core8/pwb.py dump/claims5 makereport ask
python3 pwb.py dump/claims5 test nosave
"""
#
# (C) Ibrahem Qasim, 2022
#
#
import sys
import os
import json
import time
# ---
from dump.read_dump import read_file
# ---
Dump_Dir = os.path.dirname(os.path.realpath(__file__))
# ---
Limit = {1: 900000000}
saveto = {1: ""}
sections_done = {1: 0, 'max': 100}
sections_false = {1: 0}
dump_done = {1: 0}
# ---
jsonname = ""
# ---
if "test" in sys.argv:
    Limit[1] = 30010
# ---
for arg in sys.argv:
    arg, sep, value = arg.partition(":")
    if arg.startswith("-"):
        arg = arg[1:]
    if arg == "limit":
        Limit[1] = int(value)
    if arg == "saveto":
        saveto[1] = value
# ---
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
tab2 = tab.copy()
# ---


def load_tab(ty):
    """
    Loads the tab from a json file.
    """
    # ---
    global tab, tab2, jsonname
    # ---
    ta = "claims" if ty == "all" else ty.lower()
    # ---
    jsonname = f"{Dump_Dir}/dumps/{ta}.json"
    # ---
    if "jsonnew" in sys.argv:
        # dump tab to json
        json.dump(tab, open(jsonname, "w"), indent=4)
        print(f"clear jsonname:{jsonname}")
    elif "test" not in sys.argv:
        if 'read' in sys.argv:
            # read json
            print(f'read file: {jsonname}')
            tab = json.loads(open(jsonname).read())
            for k, v in tab2.items():
                if not k in tab:
                    tab[k] = v
            print("tab['done'] == %d" % tab.get('done', 0))
        else:
            try:
                # read json
                print(f'read file: {jsonname}')
                tab = json.loads(open(jsonname).read())
                for k, v in tab2.items():
                    if not k in tab:
                        tab[k] = v
                print("tab['done'] == %d" % tab.get('done', 0))
            except Exception as e:
                print(f"cant read {jsonname} ")
                print(f"error: {e}")
    # ---
    return tab


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
    texts += "\n"
    print(texts)
    if table["props"] == {}:
        print(f'{P} table["props"] == empty.')
        return ""
    # ---
    Chart = '{| class="floatright sortable"\n|-\n|\n'
    Chart += "{{Graph:Chart|width=140|height=140|xAxisTitle=value|yAxisTitle=Number\n"
    Chart += "|type=pie|showValues1=offset:8,angle:45\n|x=%s\n|y1=%s\n|legend=value\n}}\n|-\n|}"
    # ---
    tables = """{| class="wikitable sortable plainrowheaders"\n|-\n! class="sortable" | #\n! class="sortable" | value\n! class="sortable" | Numbers\n|-\n"""
    # ---
    lists = [[y, xff] for xff, y in table["props"].items()]
    lists.sort(reverse=True)
    # ---
    xline = ""
    yline = ""
    # ---
    num = 0
    other = 0
    # ---
    for ye, x in lists:
        if ye == 0 and sections_false[1] < 100:
            print(f"p({P}), x({x}) ye == 0 or ye == 1 ")
            sections_false[1] += 1
            return ""
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
    tables += f"\n! {num} \n| others \n| {other:,} \n|-"
    # ---
    tables += "\n|}\n{{clear}}\n"
    # ---
    texts += Chart.replace("=,", "=")
    texts += "\n\n"
    texts += tables
    # ---
    sections_done[1] += 1
    # ---
    return texts


def log_dump():
    """
    Logs the dump of the current process.
    """
    global jsonname
    if "test" not in sys.argv:
        with open(jsonname, "w") as outfile:
            json.dump(tab, outfile)
        dump_done[1] += 1
        print("log_dump %d done " % dump_done[1])


def workondata(props_tos="all"):
    global tab
    tab = read_file()
    log_dump()


def save_to_wd(text, ta):
    if "nosave" in sys.argv:
        return
    # ---
    ta = ta.lower()
    # ---
    title = f"User:Mr. Ibrahem/{ta}"
    # ---
    if "test" in sys.argv:
        title = f"User:Mr. Ibrahem/{ta}_test"
    # ---
    from wd_API import himoAPI

    himoAPI.page_putWithAsk("", text, "Bot - Updating stats", title, False)


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
    rows.append(f"! {n} \n| others \n| {property_other:,}")
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


def mainar(ty="all"):
    time_start = time.time()
    print(f"time_start:{str(time_start)}")
    # ---
    global tab
    # ---
    tab = load_tab(ty)
    # ---
    if "makereport" not in sys.argv:
        workondata(props_tos=ty)
    # ---
    p31list = [[y["lenth_of_usage"], x] for x, y in tab["Main_Table"].items() if y["lenth_of_usage"] != 0]
    p31list.sort(reverse=True)
    # ---
    mxn = 51 if ty == "all" else 501
    # ---
    sections = ""
    for Len, P in p31list:
        if sections_done[1] >= sections_done['max']:
            break
        # ---
        sections += make_section(P, tab["Main_Table"][P], max_n=mxn)
    # ---
    final = time.time()
    delta = int(final - time_start)
    # ---
    tab['len_of_all_properties'] = len(tab["Main_Table"])
    # ---
    text = (
        "<onlyinclude>latest</onlyinclude>.\n"
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
    if tab["Main_Table"].get('P31'):
        text_p31 = text + make_section('P31', tab["Main_Table"]['P31'], max_n=501)
        # ---
        with open(f"{Dump_Dir}/dumps/p31_new.txt", "w", encoding="utf-8") as f:
            f.write(text_p31)
        # ---
        save_to_wd(text_p31, 'p31')
    # ---
    text += f"{chart}\n{sections}"
    # ---
    # text = text.replace("0 (0000)", "0")
    # text = text.replace("0 (0)", "0")
    # ---
    # python3 pwb.py dump/claims2 test nosave saveto:ye
    if saveto[1] != "":
        with open(f"{Dump_Dir}/dumps/{saveto[1]}.txt", "w", encoding="utf-8") as f:
            f.write(text)
    # ---
    if text == "":
        print("no data")
        return ""
    # ---
    if "test" in sys.argv and "noprint" not in sys.argv:
        print(text)
    # ---
    if tab["All_items"] == 0:
        print("no data")
        return
    # ---
    ta = "claims" if ty == "all" else ty
    # ---
    save_to_wd(text, ta)
    # ---
    to_log = f"{Dump_Dir}/dumps/{ta}.txt"
    if "test" in sys.argv:
        to_log = f"{Dump_Dir}/dumps/{ta}_test.txt"
    # ---
    with open(to_log, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    # print(make_cou( 70900911 , 84601659 ))
    mainar(ty="all")

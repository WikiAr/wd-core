"""

"""
import sys
from pathlib import Path
import pywikibot

# ---
from nep import si3

# ---
Dir = Path(__file__).parent
# ---
# 32500000   اكتمل حتى
# 32897048  متبقي حتى


def WorkNew():
    start = 32700000
    ATend = 32500000
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew list1
    if "list1" in sys.argv:
        start = 77196790
        ATend = 77038417
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew  list2
    if "list2" in sys.argv:
        start = 80999999
        ATend = 80000000
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew  list3
    if "list3" in sys.argv:
        start = 79788588
        ATend = 79000000
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew  list4
    if "list4" in sys.argv:
        start = 78411675
        ATend = 78000000
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew  list5
    if "list5" in sys.argv:
        start = 78823351
        ATend = 78412057
    # ---
    for arg in sys.argv:
        # ---
        arg, _, value = arg.partition(":")
        # ---
        value = value.replace(", ", "")
        # ---
        # python3 core8/pwb.py nep/si3 WorkNew start:95682306 to:100000
        # python3 core8/pwb.py nep/si3 WorkNew start:95000000 to:100000
        # python3 core8/pwb.py nep/si3 WorkNew start:95630660 to:100000
        # python3 core8/pwb.py nep/si3 WorkNew start:85000000 to:100000
        # python3 core8/pwb.py nep/si3 WorkNew start:75000000 to:100000
        # jsub -N ff python3 core8/pwb.py nep/si3 WorkNew start:75000000 to:100000

        # python3 core8/pwb.py nep/si3 WorkNew start:25000000 to:100000
        # python3 core8/pwb.py nep/si3 WorkNew start:25130000 to:100000
        if arg == "start":
            start = int(value)
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        value = value.replace(", ", "")
        if arg == "to":
            ATend = int(start) + int(value)
        # ---
        # python3 core8/pwb.py nep/si3 WorkNew start:95, 682, 306 end:95, 582, 306
        if arg == "end":
            ATend = int(value)
    # ---
    # python3 core8/pwb.py nep/si3 WorkNew
    # ---
    start = int(start)
    end = int(ATend)
    # ---
    list = range(end, start) if end < start else range(start, end)
    # ---
    lenth = len(list)
    pywikibot.output(f"** <<lightyellow>> WorkNew in {int(lenth)} items (start:{int(start)}, end:{int(end)})")
    # ---
    for num, q in enumerate(list, start=1):
        qitem = f"Q{int(q)}"
        si3.ISRE(qitem, num, lenth)


# ---
# python3 core8/pwb.py nep/work_new
# ---
if __name__ == "__main__":
    WorkNew()

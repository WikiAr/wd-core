"""

"""
import sys
import json
import os
from pathlib import Path
import codecs
import pywikibot
import re
# ---
Dir = Path(__file__).parent
# ---
from np import si3
# ---
#32500000   اكتمل حتى
#32897048  متبقي حتى
# ---
def WorkNew():
    start = 32700000
    ATend = 32500000
    # ---
    # python3 pwb.py np/si3 WorkNew list1
    if "list1" in sys.argv:
        start = 77196790
        ATend = 77038417 
    # ---
    # python3 pwb.py np/si3 WorkNew  list2
    if "list2" in sys.argv:
        start = 80999999 
        ATend = 80000000 
    # ---
    # python3 pwb.py np/si3 WorkNew  list3
    if "list3" in sys.argv:
        start = 79788588 
        ATend = 79000000 
    # ---
    # python3 pwb.py np/si3 WorkNew  list4
    if "list4" in sys.argv:
        start = 78411675 
        ATend = 78000000 
    # ---
    # python3 pwb.py np/si3 WorkNew  list5
    if "list5" in sys.argv:
        start = 78823351 
        ATend = 78412057
    # ---
    for arg in sys.argv:
        # ---
        arg, sep, value = arg.partition(':')
        # ---
        value = value.replace(", ", "")
        # ---
        # python3 pwb.py np/si3 WorkNew start:95682306 to:100000
        # python3 pwb.py np/si3 WorkNew start:95000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:95630660 to:100000
        # python3 pwb.py np/si3 WorkNew start:85000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:75000000 to:100000
        # jsub -N ff python3 ./core/pwb.py ./core/np/si3 WorkNew start:75000000 to:100000

        # python3 pwb.py np/si3 WorkNew start:25000000 to:100000
        # python3 pwb.py np/si3 WorkNew start:25130000 to:100000
        if arg == 'start':
            start = int(value)
    # ---      
    for arg in sys.argv:

        arg, sep, value = arg.partition(':')
        value = value.replace(", ", "")
        if arg == 'to':
            ATend = int(start) + int(value)
        # ---
        # python3 pwb.py np/si3 WorkNew start:95, 682, 306 end:95, 582, 306 
        if arg == 'end':
            ATend = int(value)
    # ---
    # ---
    # python3 pwb.py np/si3 WorkNew 
    # ---
    #if len(sys.argv) > 1:
        #start = sys.argv[1]
    # ---
    #if len(sys.argv) > 2:
        #ATend = sys.argv[2]
    # ---
    num   = 0
    # ---
    start = int(start)
    end = int(ATend)
    # ---
    if end < start:
        list  = range( end, start )
    else:
        list  = range( start, end )
    # ---
    lenth = len(list)
    pywikibot.output( '** <<lightyellow>> WorkNew in %d items (start:%d, end:%d)'  % (lenth, start, end) )
    # ---
    for q in list:
        qitem  = 'Q%d' % q
        num += 1
        si3.ISRE( qitem, num, lenth )
# ---
# python3 pwb.py np/work_new
# ---
if __name__ == "__main__":
    WorkNew()
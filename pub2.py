#!/usr/bin/python
"""

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pub
import time
import sys
# ---
def main():
    print('main:')
    numb = 0
    type = "MED"
    start = 0
    ATend = 10
    # ---
    if len(sys.argv) > 1:
        start = sys.argv[1]
    # ---
    if len(sys.argv) > 2:
        ATend = sys.argv[2]
    # ---
    #list  = range(62700,62710)
    start = int(start)
    end = start + int(ATend)
    list = range(start, end)
    for id in list:
        numb += 1
        id = str(id)
        print('%d : id: %s' % (numb, id))
        pub.add(id, type)
        time.sleep(2)
# ---
if __name__ == "__main__":
    main()
# ---
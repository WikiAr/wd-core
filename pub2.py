#!/usr/bin/python3
"""

"""
import pub
import time
import sys


def main():
    print("main:")
    type = "MED"
    start = sys.argv[1] if len(sys.argv) > 1 else 0
    ATend = sys.argv[2] if len(sys.argv) > 2 else 10
    # ---
    # list  = range(62700,62710)
    start = int(start)
    end = start + int(ATend)
    list = range(start, end)
    for numb, id in enumerate(list, start=1):
        id = str(id)
        print(f"{numb} : id: {id}")
        pub.add(id, type)
        time.sleep(2)


if __name__ == "__main__":
    main()

"""

"""
import sys
from nep import si3

si3.MainTestTable[1] = True


def Main_Test():
    # python core8/pwb.py nep/test_si3 -page:Q122652815
    # python core8/pwb.py nep/test_si3
    print("<<lightyellow>> Main_Test :")
    num = 0
    # for qq in ['Q21146082', 'Q21563434', 'Q21563625', 'Q22061800', 'Q22065466']:#, 'Q38822009', 'Q38822019', 'Q38822020']:
    # ---
    q = "Q95690374"
    # ---
    for arg in sys.argv:
        # ---
        arg, _, value = arg.partition(":")
        # ---
        if arg == "-page":
            q = value
    # ---
    # si3.ISRE( "Q4116394", num, 0)   # scientific article published in 2018
    # si3.ISRE( "Q20420158", num, 0)   # scientific article published in 2018
    # si3.ISRE( "Q92203555", num, 0)
    # si3.ISRE( "Q95629862", num, 0)
    # si3.ISRE( "Q92313024", num, 0)
    # ---
    # si3.ISRE( "Q90006515", num, 0)
    # ---
    # si3.ISRE( "Q75729", num, 0)
    si3.ISRE(q, num, 0)
    # ---
    # si3.ISRE( "Q92313521", num, 0)
    # si3.ISRE( "Q92313027", num, 0)
    # ---
    # ---
    # si3.ISRE( "Q92283597", num, 0)
    # si3.ISRE( "Q77038516", num, 0)
    # ---
    # si3.ISRE( "Q42997227", num, 0)   # scientific article published in 1988
    # si3.ISRE( "Q63681354", num, 0)   # scientific article published in 2018
    # si3.ISRE( "Q63957216", num, 0)   # scientific article published in January 1990
    # si3.ISRE( "Q36565264", num, 0)   # scientific article published on 5 September 2006
    # si3.ISRE( "Q31056229", num, 0)   # scientific article published in May 1999
    # ---
    """
    item = FindItem(qq, no_donelist = True)
    num += 1
    # ---python pwb.py nep/d2 33200000
    if item:
        q = item["q"]
        sa = Get_P_API_time(item, 'P577')
        print(sa)
        #make_scientific_art(item, 'Q13442814', num)
    """


# ---
# python3 core8/pwb.py nep/test_si3
# ---
if __name__ == "__main__":
    Main_Test()

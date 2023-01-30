#!/usr/bin/python
#--
#!/usr/bin/python
# -*- coding: utf-8 -*-
#---
"""
python pwb.py cy/cy4 -page:كريس_فروم

"""
#---
#
# (C) Ibrahem Qasim, 2022
#
#---
import urllib
import re
import urllib.request
import urllib.parse
#---
import sys
#---
br = '''
'''
#---
def ec_de_code(tt , type):
    fao = tt
    if type == 'encode' :
        fao = urllib.parse.quote(tt)
    elif type == 'decode' :
        fao = urllib.parse.unquote(tt)
    return fao
#---
def printo(po):
    #print( ec_de_code(po , 'encode') + br)
    print( po + br)
#---
def main():
    #printo( 'TestMain:' + br)
    #StartOnePage('%D9%88%D8%A8:%D9%85%D9%84%D8%B9%D8%A8')
    #GetTempaltes('Q286183')
    if sys.argv:
        printo(str(sys.argv) + br)
        title = sys.argv[1]
        #title = ec_de_code(title , 'encode')
        #StartOnePage(title)
#---
def findflag(race , flag):
    flage = { 
         'إيطاليا' : '{{flag|إيطاليا}}' 
        ,'جيرو ديل ترينتينو' : '{{flag|إيطاليا}}' 
        ,'the Alps' : '{{flag|إيطاليا}}' 
        ,'France' : '{{flag|فرنسا}}' 
        ,'فرنسا' : '{{flag|فرنسا}}' 
        ,'إسبانيا' : '{{flag|إسبانيا}}' 
        ,'دونكيرك' : '{{flag|بلجيكا}}' 
        ,'غنت-وفلجم' : '{{flag|بلجيكا}}' 
        ,'Gent–Wevelgem' : '{{flag|بلجيكا}}' 
        ,'Norway' : '{{flag|النرويج}}' 
        ,'النرويج' : '{{flag|النرويج}}' 
        ,'كريثيديا دو دوفين' : '{{flag|سويسرا}}' 
        ,'du Dauphiné' : '{{flag|سويسرا}}' 
        ,'سويسرا' : '{{flag|سويسرا}}' 
    }
    #---
    for ff in flage.keys():
        te = re.sub( ff , '' , str(race))
        if te != str(race):
            return flage[ff]
    #---
    return flag
#---
def main2():
    s = findflag('طواف إيطاليا للنساء 2004' , 'dfdf' )
    print(s)
#---
test = True#False#True
#---
if __name__ == "__main__":
    main2()
#---
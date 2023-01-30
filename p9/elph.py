#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إضافة بيانات خاصية موضوعان أو أكثر للتصنيفات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import time
import pywikibot
#import Nationalities as aa
import codecs
from API.maindir import main_dir
#---
import sys
#---
# start of himoBOT.py file
from API import himoBOT
#---
HEAD = '''#!/usr/bin/python
# -*- coding: utf-8 -*-
"""


"""
#
# (C) Ibrahem Qasim, 2022
#
#
'''

foter = '''    ]
#---'''
#---
def log22(t , file):
    form = t + '\n'
    #pywikibot.output(t)
    with codecs.open('make/' + file + '.py', "a", encoding="utf-8") as logfile:
      try:
            logfile.write(form)
      except :
            pywikibot.output("Error writing")
#---
def work(file , name , list):
    #oo = '"%s" ,\n'
    rows = ''
    log22(HEAD, file )
    log22(name +' = [' , file )
    num = 0 
    #---
    if len(list) > 5000:
        kkkkk  = 1000
    elif len(list) < 2000:
        kkkkk  = 500
    elif len(list) < 1000:
        kkkkk  = 250
    #---
    for li in list:
        num += 1
        tot = '"%s" ,\n' % li
        #---
        litest = re.sub('"' , '' , li)
        if li != litest:
            li = re.sub("\'" , "\'" , li)
            tot = "'%s' ,\n" % li
        #---
        if li != litest and litest != re.sub("'" , "" , li):
            pywikibot.output('<<lightyellow>> %s' % tot )
        else:
            rows = rows + tot
        sss = '%d/%d: %s' % (num , len(list) , tot )
        #---
        if num == 1:
            pywikibot.output( sss )
        #---
        for y in range(1,50):
            if num == y * kkkkk:
                pywikibot.output( sss )
        #---
    log22(rows , file )
    log22(foter, file )
#---
{"n":"result"
,"a":{"querytime_sec":0.035883,"query":""}
,"*":[{"n":"combination"
    ,"a":{"type":"subset"
    ,"*":["فؤاد_راتب","محمد_رياض_(ممثل)","روجر_شانك","جون_ستاب","المخصص","المختار_بن_الشیخ","عبير_فاروق","فتحي_سعد","سلمان_بن_سعد_بن_عبد_الله_بن_تركي_آل_سعود","صهيب_الراوي","محمد_الصدیق_حمادوش","عدنان_بالعيس","إبراهيم_السويلم","محمد_محمد_المفتي","الصدیق_حمادوش","محمد_بن_عمر_بقاق","الطیب_حمادوش","محمد_الجلواح","علي_بن_عبدالله_باراس","حيدر_منصور_هادي_العذاري","عبد_الرحمن_حمادوش","سياف_أباالخيل","كوسوكي_سايتو","غنوة_محمود","رشا_بلال","مسعود_بن_محمد_المعدري","علي_سالم_(رجل_أعمال)","ظهير_الدين_المباركفوري","ميمون_الخالدي","جلال_الحمداوي","شيرين_بوتلة","فريدريك_من_لوكسمبورغ","الطاهر_بن_محمد_حمادوش","نوميديا_لزول","صالح_بن_عبد_الله_الإلغي","ماريا_رحماني","رنا_العظم","عبادة_بن_الخشخاش_الفراني_البلوي","سيف_عامر","سعيد_العوامي","محمد_ابن_المجراد_السلاوي","صالح_بن_سعيد_الزهراني","سعيد_الغانمي","كاميلا_كابيلو","فالح_شبيب_العجمي","نادر_محمد_علي","سعدي_الحديثي"
    ]}}]}
#---
def main2():
    file = 'rupages'
    name = 'rupage'
    cat = 'Yemen_paghimo_ni_bot'
    url = 'https://' + 'petscan.wmflabs.org/?language=ceb&project=wikipedia&depth=0&categories=' + cat + '&combination=subset'
    url = url +  '&negcats=&ns%5B0%5D=1&show_redirects=no&edits%5Bbots%5D=both&edits%5Banons%5D=both&edits%5Bflagged%5D=both'
    url = url +  '&subpage_filter=either&common_wiki=auto&wikidata_item=without&wpiu=any&cb_labels_yes_l=1&&cb_labels_any_l=1'
    url = url +  '&cb_labels_no_l=1&format=json&output_compatability=catscan&sparse=on&min_redlink_count=1&doit=Do%20it%21'
    print(url)

    #list = [x for x in jso["*"][0]["a"]["*"] ]
    #work(file , name , list)
#---
def main1():
    #quarrr = '198879'
    quarrr = '205887'#199712#201191#205887
    file = 'FilmCat'
    name = 'FilmCat_list'
    url = 'https://quarry.wmflabs.org/run/' + quarrr + '/output/0/json'
    sparql = himoBOT.getURL(url=url)
    jso = himoBOT.load_SPARQL_New(sparql=sparql)
    list = [x[0] for x in jso['rows'] ]
    work(file , name , list)
#---
if __name__ == "__main__":
    main2()
    #main1()
#---
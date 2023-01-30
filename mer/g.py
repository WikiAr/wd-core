#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

إيجاد تسمية عربية من خلال قوالب 
geobox

"""
#
# (C) Ibrahem Qasim, 2022
#
import urllib
import pywikibot
import re
import string
import codecs
from datetime import datetime
#---
import sys
#---
import urllib
import urllib
import urllib.request
import urllib.parse

#---
from pywikibot.bot import (SingleSiteBot, ExistingPageBot, NoRedirectPageBot, AutomaticTWSummaryBot)
# This is required for the text that is shown when you run this script
# with the parameter -help.


#---
# start of himoAPI.py 
#from API import himoAPI
from API import himoAPI_test as himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#---
# start of himoBOT.py file
from API import himoBOT
#---
categories = {
    "Kategoriya:Mga subdibisyon sa Al Mahrah (lalawigan)" : "تصنيف:عزل محافظة المهرة" , 
    "Kategoriya:Mga subdibisyon sa Al Maḩwīt (lalawigan)" : "تصنيف:عزل محافظة المحويت" , 
    "Kategoriya:Mga subdibisyon sa Amanat Al Asimah" : "تصنيف:عزل صنعاء" , #########
    "Kategoriya:Mga subdibisyon sa Ibb (lalawigan)" : "تصنيف:عزل محافظة إب" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Abyan" : "تصنيف:عزل محافظة أبين" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Bayḑā'" : "تصنيف:عزل محافظة البيضاء (اليمن)" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Jawf" : "تصنيف:عزل محافظة الجوف (اليمن)" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at al Ḩudaydah" : "تصنيف:عزل محافظة الحديدة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at aḑ Ḑāli‘" : "تصنيف:عزل محافظة الضالع" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Dhamār" : "تصنيف:عزل محافظة ذمار" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Laḩij" : "تصنيف:عزل محافظة لحج" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ma'rib" : "تصنيف:عزل محافظة مأرب" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Raymah" : "تصنيف:عزل محافظة ريمة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ta‘izz" : "تصنيف:عزل محافظة تعز" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Şa‘dah" : "تصنيف:عزل محافظة صعدة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ḩajjah" : "تصنيف:عزل محافظة حجة" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at Ḩaḑramawt" : "تصنيف:عزل محافظة حضرموت" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at ‘Adan" : "تصنيف:عزل محافظة عدن" , 
    "Kategoriya:Mga subdibisyon sa Muḩāfaz̧at ‘Amrān" : "تصنيف:عزل محافظة عمران" , 
    "Kategoriya:Mga subdibisyon sa Sanaa (lalawigan)" : "تصنيف:عزل محافظة صنعاء" , 
    "Kategoriya:Mga subdibisyon sa Shabwah" : "تصنيف:عزل محافظة شبوة" , 
    "Kategoriya:Mga subdibisyon sa Socotra (lalawigan)" : "تصنيف:عزل محافظة أرخبيل سقطرى" 
    }
#---
def main(categories):
    #---
    qua = """SELECT (concat(strafter(str(?ss),"/entity/"))  as ?item)
    ?page 
    WHERE {
    SERVICE wikibase:mwapi {
    bd:serviceParam wikibase:api "Generator" .
    bd:serviceParam wikibase:endpoint "ceb.wikipedia.org" .
    bd:serviceParam mwapi:gcmtitle "YYY" .
    bd:serviceParam mwapi:generator "categorymembers" .
    bd:serviceParam mwapi:gcmprop "ids|title|type" .
    bd:serviceParam mwapi:gcmlimit "max" .
    ?page wikibase:apiOutput mwapi:title  .
    ?ns wikibase:apiOutput "@ns" .
    ?ss wikibase:apiOutputItem mwapi:item .
    }
    #OPTIONAL {} .
    FILTER NOT EXISTS {?ss rdfs:label ?itemabel filter (lang(?itemabel) = "ar")} .
    FILTER (?ns = "0")
    }"""
    number = 0
    catelenth = len(categories.keys())
    cebwiki = pywikibot.Site("ceb", "wikipedia") 
    #---
    for category in categories.keys():
        number +=1
        pywikibot.output('<<lightred>> %d/%d start with cat: %s'  % (number ,catelenth , category ) )
        #CategoryID = categories[category]['id']
        #quarry = re.sub( 'Q4117509' , CategoryID , quarry)
        #---
        quarry2 = re.sub( 'YYY' , category, qua)
        pagelist2 = himoBOT.sparql_generator_url2(quarry2) 
        lenth = len(pagelist2)
        num = 0
        for pp in pagelist2:         
            num +=1
            pywikibot.output('<<lightyellow>> %d/%d page:"%s" , item:"%s".' % ( num , lenth , pp['page'] , pp['item']) )
            page = pywikibot.Page(cebwiki, pp['page'])
            if page:
                item = himoBOT.GetItemFromQid(pp['item'])
                #item = pywikibot.ItemPage.fromPage(page)
                text = page.text
                #pat =  'native_name\s*=\s*(\w+)\n'
                pat =  'native_name\s*=\s*(.*)\n'
                OtherName =  re.compile( pat )
                na = OtherName.findall(text)
                if na:
                    if item:
                        pywikibot.output('find name : %s' % na[0])
                        if na[0] != re.sub( '[ابتثجحخدذرزسشصضطظعغفقكلمنهوي]' , '' , na[0]):
                            himoAPI.Labels_API( pp['item'], na[0] , 'ar' , False)
                    else:
                        pywikibot.output('no item for: %s' % pp['item'])
#---   
if __name__ == '__main__':
     main(categories)
#---
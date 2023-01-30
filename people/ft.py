#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

تعديل وصف لاعب كرة قدم للإناث في ويكي بيانات

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import pywikibot
import re
#---
# start of himoAPI.py file
from API import himoAPI
#himoAPI.Claim_API2( item_numeric , property, id)
#himoAPI.Claim_API_With_Quall(q , pro ,numeric, quall_prop , quall_id)
#himoAPI.New_API(data2, summary)
#himoAPI.New_Mult_Des( q, data2, summary , ret )
#himoAPI.Des_API( Qid, desc , lang )
#himoAPI.Labels_API( Qid, desc , lang , False)
#---
#import Nationalities as aa
#---
# start of himoBOT.py file
from API import himoBOT
#---
def main():
    pywikibot.output( '<<lightpurple>>------------\n main :' )
    #---
    translations = {}
    #---
    qua = '''PREFIX schema: <http://schema.org/>
        SELECT DISTINCT 

          #(concat(strafter(str(?item),"/entity/"))  as ?ss) 
          ?item
          #(CONCAT("Dar") as ?en)
          #(CONCAT('"لاعبة كرة قدم"') as ?aa)
         #?year2 
        WHERE {
          VALUES ?yea2r2 { "لاعب كرة سلة"@ar
                          "لاعب كرة تنس"@ar
                          "لاعب كرة قدم"@ar }
         # ?item wdt:P21 wd:Q6581097.  #ذكر
         ?item wdt:P21 wd:Q6581072. #انثى
        #  BIND("لاعبة كرة قدم"@ar AS ?year)
          ?item schema:description "لاعب كرة قدم"@ar.  
        #  FILTER(!BOUND(?itemabel))
        }

        #LIMIT 5000'''
    #---
    json1 = himoBOT.wd_sparql_generator_url(qua)
    c = 0
    if json1:
        #out = '<<lightgreen>>  *== (Quary: %d/%d; %s:%s:%s;) =='
        #pywikibot.output(out % (Queries, totalqueries, targetlang, genderlabel, translation ))
        #---
        for item in json1:    # عنصر ويكي بيانات
            q = item.title(as_link=False)
            c += 1
            item.get()
            pywikibot.output( '  * action %d/%d "%s"' % ( c , 0 , q) )
            #work_2(item , translations , translation , genderlabel )
            #---
                #OOutPut( '<<lightyellow>>* work 2:' )
            #---
            descriptions = item.descriptions
            NewDesc = '{"descriptions":{"ar":{"language":"ar","value":"لاعبة كرة قدم"}}}'
            addedlangs = []
            q = item.title(as_link=False)
            #---
            if 'ar' in descriptions.keys():
                if descriptions['ar'] == 'لاعب كرة قدم':
                    pywikibot.output( '  * %s: change "%s"  to "%s"' % (q, 'لاعب كرة قدم' ,'لاعبة كرة قدم' ) )
                    summary = ('Bot: fix ar description')
                    #---
                    himoAPI.New_Mult_Des_2(q, NewDesc, summary , False)
#---
if __name__ == "__main__":
    main()

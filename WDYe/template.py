
from wd_API import newdesc
# site = pywikibot.Site('wikidata', 'wikidata')
# repo = site.data_repository()
from desc_dicts.descraptions import DescraptionsTable

translations = {}
translations['Wikimedia template'] = DescraptionsTable['Wikimedia template']

# import pywikibot

# item = pywikibot.ItemPage(repo, 'Q20509009')
# item.get()
list = [
    "Q15671253",  # Wikimedia template for chess diagram
    "Q19887878",  # قالب معلومات ويكيميديا
    "Q20769160",  # Wikimedia userbox template
    "Q24731821",  # Commons Creator page
    "Q26267864",  # ملف ويكيميديا كيه إم إل
]
topic = 'Wikimedia template'

quarry2 = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:Q11266439.}'
# newdesc.mainfromQuarry( topic , quarry2, translations)

for ll in list:
    quarry = 'SELECT ?item  WHERE {  ?item wdt:P31 wd:%s.}' % ll
    newdesc.mainfromQuarry2(topic, quarry, translations)

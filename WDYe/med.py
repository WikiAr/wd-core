#!/usr/bin/python3
#!/usr/bin/python3
"""

إضافة تسميات مواضيع طبية

"""
#
# (C) Ibrahem Qasim, 2022
#
#

import re
import pywikibot
from wd_api import wd_bot
import logging
logger = logging.getLogger(__name__)

# ---

import sys

# ---
import urllib
import urllib.request
import urllib.parse
from API import open_url
# ---
from himo_api import New_Himo_API
WD_API_Bot = New_Himo_API.NewHimoAPIBot(Mr_or_bot="mr", www="www")
# ---
from newapi.page import MainPage

def dec(xx):
    xx = xx.replace(" ", "_")
    fao = xx
    try:
        fao = urllib.parse.quote(xx)
    except BaseException:
        logger.info(f'<<lightred>> except when urllib.parse.quote({xx})')
    return fao

def fixrow(row):
    en, ar = False, False
    # logger.info( "===============================" )
    row = re.sub(r"\n+", "", row)
    row = re.sub(r"\t+", "", row)
    row = re.sub(r"\s+", " ", row)
    row = re.sub(r"</strong><strong>", " ", row)
    row = re.sub(r"<strong>", "", row)
    row = re.sub(r"</strong>", "", row)
    row = re.sub(r'<td class="views-field views-field-field-hadaf-value views-align-center" >', "<tdss>", row)
    # logger.info( row )
    # ---
    if row.find('<td class="views-field views-field-title views-align-center" >') != -1:
        row = row.split('<td class="views-field views-field-title views-align-center" >')[1]
        row = row.split('</p>')[0]
        # if row.find('<tdss>') != -1:
        row = re.sub(r'</td><tdss><p>', "<ssss>", row)
        # logger.info( row )
    # ---
    if row.find("<ssss>") != -1:
        en = row.split('<ssss>')[0].strip()
        ar = row.split('<ssss>')[1].strip()
        if en and ar:
            return en, ar
    # ---
    return en, ar

# ---
Labels = {}
SaveR = {1: False}

def fixo(stro):
    stro = stro.strip()
    stro = stro.split("(")[0]
    stro = stro.split("[")[0]
    stro = stro.split(":")[0]
    return stro

def Fix_List(List):
    New_List = []
    # ---
    for y in List:
        yy = y
        yy = re.sub(r";", "،", yy)
        yy = re.sub(r"؛", "،", yy)
        yy = re.sub(r"\‚", "،", yy)
        yy = re.sub(r",", "،", yy)
        yy = re.sub(r"-->", "", yy)
        New_List.append(yy)
    # ---
    New_List2 = []
    # if ar.find(" (الجمع:") != -1 :
    # ---
    FFA = r"(الجمع|ج|جمعها|)(\=|\:)(.*)"
    mattes = [r"^(.*)\(" + FFA + r"\)$", r"^(.*)\[" + FFA + r"\]$", r"^(.*)\[" + FFA + r"\]$"]
    # ---
    comas = ["،", ";", "؛"]
    # comas = ["، ", "; " , "؛ "]
    # ---
    for ar in New_List:
        Conn = True
        # ---
        for coma in comas:
            if ar.find(coma) != -1:
                Conn = False
                logger.info(f'ca "{ar}" , .find("{coma}") != -1')
                # New_List.remove(ar)
                ars = ar.split(coma)
                # ---
                logger.info(f"ars:\"{'|'.join(ars)}\"")
                for aa in ars:
                    if aa.strip() not in New_List2:
                        New_List2.append(fixo(aa))
                        # New_List.append( aa.strip() )
        # ---
        # elif re.match( mat , ar) or re.match( mat1 , ar) or re.match( mat2 , ar):
        if Conn:
            Dodo = True
            for mate in mattes:
                if re.match(mate, ar.strip()) and Dodo:
                    # New_List.remove(ar)
                    Dodo = False
                    Conn = False
                    # ---
                    ar1 = re.sub(mate, r'\g<4>', ar)
                    ar2 = re.sub(mate, r'\g<1>', ar)
                    logger.info(f'ar2:"{ar2}",ar1:"{ar1}" ')
                    # ---
                    if ar1.strip() not in New_List2:
                        New_List2.append(fixo(ar1))
                    # ---
                    if ar2.strip() not in New_List2:
                        New_List2.append(fixo(ar2))
                    # ---
        # ---
        if Conn:
            if ar.strip() not in New_List2:
                New_List2.append(fixo(ar))
        # ---
    New_List = [fixo(x) for x in New_List2]
    logger.info("New_List: " + "|".join(New_List))
    return New_List

def fixrow2(row):
    en, ar = False, False
    row = re.sub(r" <", "<", row)
    row = re.sub(r"> ", ">", row)
    row = re.sub(r"\n+", "", row)
    row = re.sub(r"\t+", "", row)
    row = re.sub(r"\s+", " ", row)
    row = re.sub(r'\<tr bgcolor\=\"\#\w+\"\>', "", row)
    # logger.info( "===============================" )
    rowss = row.split("</td>")
    # logger.info( rowss )
    # logger.info( "===============================" )
    # ---
    # en = re.sub(r'\<td class\=\"tden\"\>(.*)\<\/td\>' , '\g<1>', row )
    # ar = re.sub(r'\<td class\=\"tdar\"\>(.*)\<\/td\>' , '\g<1>', row )
    # ---
    for x in rowss:
        # logger.info( x )
        if x.startswith('<td class="tdar">'):
            ar = x.split('<td class="tdar">')[1]
        elif x.startswith('<td class="tden">'):
            en = x.split('<td class="tden">')[1]
    # ---
    return en, ar

def Get_item_table(enlab):
    Item_tab = []
    so = enlab
    so = so.replace(" ", "+")
    url = f"http://tbeeb.net/med/search.php?q={so}"
    logger.info(url)
    # ---
    if url == "http://tbeeb.net/med/search.php?q=":
        return Item_tab
    # ---
    html = open_url.open_the_url(url=url)
    if html.find('<table class="table">') == -1:
        return Item_tab
    # ---
    html = html.split('<table class="table">')[1]
    html = html.split("</table>")[0]
    html = re.sub(r"\n+", "", html)
    html = re.sub(r"\t+", "", html)
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r"> <", "><", html)
    # logger.info( html )
    # ---
    if enlab in Labels:
        for eee in Labels[enlab]:
            if eee not in Item_tab:
                Item_tab.append(eee)
    # ---
    rows = html.split("</tr>")
    for row in rows:
        en, ar = fixrow2(row)
        if en and ar:
            if en not in Labels:
                Labels[en] = []
            Labels[en].append(ar)
            # ---
            if en == enlab:
                # ---
                if ar not in Item_tab:
                    Item_tab.append(ar)
    return Fix_List(Item_tab)

def Get_item_table2(enlab):
    Item_tab = []
    # url = "http://www.alqamoos.org/?search_fulltext={}&field_magal=Medical".format( dec(enlab) )
    url = f"http://www.alqamoos.org/?search_fulltext={dec(enlab)}&field_magal=All"
    logger.info(url)
    # ---
    # if url == "http://www.alqamoos.org/?search_fulltext=&field_magal=Medical" :
    if url == "http://www.alqamoos.org/?search_fulltext=&field_magal=All":
        return Item_tab
    # ---
    html = open_url.open_the_url(url=url)
    if html.find("No results matched your search") != -1:
        return Item_tab
    # ---
    html = html.split("<tbody>")[1]
    html = html.split("</tbody>")[0]
    html = re.sub(r"\n+", "", html)
    html = re.sub(r"\t+", "", html)
    html = re.sub(r"\s+", " ", html)
    html = re.sub(r"> <", "><", html)
    # logger.info( html )
    # ---
    if enlab in Labels:
        for eee in Labels[enlab]:
            if eee not in Item_tab:
                Item_tab.append(eee)
    # ---
    rows = html.split("</tr>")
    for row in rows:
        en, ar = fixrow(row)
        if en and ar:
            if en not in Labels:
                Labels[en] = []
            Labels[en].append(ar)
            # ---
            if en == enlab:
                # ---
                if ar not in Item_tab:
                    Item_tab.append(ar)
    return Fix_List(Item_tab)

# ---
Looogs = {}

def looog():
    log2 = {x: Looogs[x] for x in Looogs if Looogs[x] != []}
    # ---
    text2 = ""
    # ---
    for x, value in log2.items():
        q = '{{Q| ' + x + '}}'
        text2 += "\n|-\n| %s || {{" % q
        text2 += f"Label | {x} | en"
        text2 += "}} ||"
        text2 += ",".join(value) + "\n"
    # ---
    if text2:
        text2 = '''\n=={{subst:date}}==\n{| class="wikitable sortable"\n|-\n! item\n! en \n! ar\n|-''' + text2
        text2 = text2 + "|-\n|}"
        # ---
        title = "user:Mr._Ibrahem/medstat"
        # ---
        EngPage = MainPage(title, "wikidata", family="wikidata")
        # ---
        main_text = EngPage.get_text()
        newtext = main_text + text2
        # ---
        # WD_API_Bot.page_put(text3, "update.", title)
        EngPage.save(newtext=newtext, summary="update.", nocreate=1)

def WORK(item, table):
    # logger.info( item )
    logger.info(table)
    # ---
    if item not in Looogs:
        Looogs[item] = []
    # ---
    # logger.info( '<<lightgreen>> item:"%s" ' % item )
    # ---
    arlab = table["ar"]
    enlab = table["en"]
    enlab = re.sub(r"_", " ", enlab.lower())
    # ---
    Item_tab = Get_item_table2(enlab)
    if not Item_tab:
        Item_tab = Get_item_table(enlab)
    # ---
    Item_tab2 = Item_tab
    # logger.info( ",".join(Item_tab) )
    for alia in Item_tab:
        if alia in table["alias"]:
            Item_tab.remove(alia)
            logger.info(f'alia : "{alia}" in alias')
        # ---
        elif alia == table["ar"]:
            Item_tab.remove(alia)
            logger.info(f'alia : "{alia}" == ar label')
    # ---
    if Item_tab != Item_tab2:
        logger.info(",".join(Item_tab))
    # ---
    NewALLi_to_add = []
    for ali in Item_tab:
        if not arlab:
            arlab = ali
            if SaveR[1]:
                WD_API_Bot.Labels_API(item, ali, "ar", False)
                Looogs[item].append(ali)
            else:
                sa = pywikibot.input(f'<<lightyellow>>add ali : "{ali}" as label to item :{item}? ')
                if sa in ['y', "a", '']:
                    WD_API_Bot.Labels_API(item, ali, "ar", False)
                    Looogs[item].append(ali)
                else:
                    print(' bot: wrong answer')
        else:
            NewALLi_to_add.append(ali)
    # ---
    if arlab in NewALLi_to_add:
        NewALLi_to_add.remove(arlab)
    # ---
    for uu in NewALLi_to_add:
        if uu in table["alias"]:
            NewALLi_to_add.remove(uu)
            logger.info(f'uu : "{uu}" in table["alias"]')
        elif SaveR[1] and uu.find("(") != -1:
            NewALLi_to_add.remove(uu)
            logger.info(f'uu : "{uu}" in table["alias"]')
    # ---
    if NewALLi_to_add != []:
        logger.info("|".join(NewALLi_to_add))
        # logger.info( 'NewALLi_to_add: "%s"'  % str("|".join(NewALLi_to_add)) )
        if SaveR[1]:
            WD_API_Bot.Alias_API(item, NewALLi_to_add, "ar", False)
            Looogs[item].append(",".join(NewALLi_to_add))
        else:
            sa = pywikibot.input(f'<<lightyellow>>bot: Add Alias ([y]es, [N]o, [a]ll): for item {item}')
            if sa in ['y', "a", '']:
                WD_API_Bot.Alias_API(item, NewALLi_to_add, "ar", False)
                Looogs[item].append(",".join(NewALLi_to_add))
            else:
                print(' bot: wrong answer')

    # ---

Limit = {1: "500"}

def main():
    # python3 core8/pwb.py WDYe/med
    # python3 core8/pwb.py WDYe/med short
    # python3 core8/pwb.py WDYe/med  ta:horror
    # python3 core8/pwb.py WDYe/med qs:Q12136
    # python3 core8/pwb.py WDYe/med qs:Q39546
    # python3 core8/pwb.py WDYe/med qs:Q24017414
    # python3 core8/pwb.py WDYe/med qs:Q27043950
    # ---
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # sat = "{?item wdt:%s  wd:%s. }" % (pp , qq)
    # pp , qq = "P105" , "Q35409"
    pp, qq = "P31", "Q27043950"
    sat = "?item wdt:%s  wd:%s. "
    for arg in sys.argv:
        arg, _, value = arg.partition(':')
        # ---#Depth[1]
        if arg == "p":
            pp = value
        # ---#
        if arg == "qs":
            qq = value
            pp = "P31/wdt:P279*"
        # ---#
        if arg == "q":
            qq = value
        # ---#
        if arg == 'always':
            SaveR[1] = True
            logger.info('<<lightred>> SaveR = True.')
        # ---#limit[1]
        if arg in ['-limit', 'limit']:
            Limit[1] = value
            logger.info(f'<<lightred>> Limit = {value}.')
            # ---#
    sat %= (pp, qq)
    # ?item wdt:P1343 ?P1343.
    # {?P1343 wdt:P629 wd:Q200306.} UNION {?item wdt:P1343 wd:Q19558994. }
    # sat = "{?item wdt:P31/wdt:P279* wd:Q27043950. }"#Q4936952.}
    # SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    Quaa = ''' SELECT ?item ?en ?ar ?alias WHERE { '''

    Quaa += (
        sat
        + '''
    ?item rdfs:label ?en. FILTER(LANG(?en) = "en").
    FILTER NOT EXISTS { ?item rdfs:label ?ar. FILTER(LANG(?ar) = "ar"). }
    FILTER NOT EXISTS  { ?item skos:altLabel ?alias FILTER (LANG (?alias) = "ar") }
    }
    LIMIT '''
    )

    Quaa += Limit[1]

    logger.info(Quaa)
    sparql = wd_bot.sparql_generator_url(Quaa)
    # ---
    Table = {}
    for item in sparql:
        q = item['item'].split("/entity/")[1]
        if q not in Table:
            Table[q] = {}
        for tab in item:
            if tab not in Table[q]:
                Table[q][tab] = []
            # if item[tab] :
            Table[q][tab].append(item[tab])
    Tab_l = {
        it_em: {
            'ar': Table[it_em]["ar"][0],
            'alias': Table[it_em]["alias"],
            'en': Table[it_em]["en"][0],
        }
        for it_em in Table
    }
    for num, (item, value_) in enumerate(Tab_l.items(), start=1):
        # if num < 2:
        logger.info('<<lightgreen>> %d/%d item:"%s" ' % (num, len(Tab_l.keys()), item))
        # item['item'] = item['item'].split("/entity/")[1]
        WORK(item, value_)
    # ---
    looog()

    # ---

if __name__ == "__main__":
    main()
    # logger.info(Get_item_table("ships")  )
    # t = fixrow2('<tr bgcolor="#FCFCFC"><td class="tden"> ship | ships | </td><td class="tdar"> فلك سفينة, سفينة, قارب, زورق بخاري, نوتية المركب</td>')
    # logger.info( t )
    # Fix_List(["الفروة","الشواة (فروة الرأس)","الشواة","الفروة، الشواة، فروة الرأس","فروة"])
    # Fix_List(['صدر', 'صدر [:صدور]', 'كلاب [ج=كب]'])
    # Fix_List(["الترقوة","الناحرة","الترقوة (الجمع: التراقي)","عظم الترقوة"])
    # Fix_List(['كلاب [ج=كب]'])
    # Fix_List(['صدر', 'صدر [ج:صدور]', 'الصدر'])
    # Fix_List(['الطبلة (=غشاء الطبل)'])
    # Fix_List(["برتقالية" , "برتقال [نبات]" , "برتقالي" , "برتقالي - برتقال" , "برتقال (نبات)" , "برتقالية (مادة ملونة)"])
    # Fix_List(["لؤلوة (ج: لآلئ)", "لآلىء"])
    # Fix_List(["توت الأرض؛فراولة ;فريز"])
    # Fix_List(['الطبلة (ج=غشاء الطبل)'])
    # WORK("Q4115189" , {'en': 'orbitofrontal cortex','ar': 'يمو', "alias" :[] })
    # WORK("Q4115189" , {'en': 'orbitofrontal cortex','ar': 'يمو', "alias" :[] })
# ---

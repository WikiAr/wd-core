#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
python pwb.py cy/cy3 -page:كريس_فروم

"""
#
# (C) Ibrahem Qasim, 2022
#
#
import re
import pywikibot
from pywikibot import pagegenerators
#---
import sys
#---
import urllib
import urllib.request
import urllib.parse
#---
def ec_de(tt):
    fao = tt
    try:
        fao = urllib.parse.quote(tt)
    except:
        fao = urllib.parse.quote(tt)#.decode('utf8')

    return fao
#---
def list_template_usage():
    arsite = pywikibot.Site("ar", "wikipedia")
    tmpl_name = 'نتيجة_سباق_الدراجات/بداية'
    name = "{}:{}".format(arsite.namespace(10), tmpl_name)
    tmpl_page = pywikibot.Page(arsite, name)
    ref_gen = pagegenerators.ReferringPageGenerator(tmpl_page, onlyTemplateInclusion=True)
    filter_gen = pagegenerators.NamespaceFilterPageGenerator(ref_gen, namespaces=[0])
    generator = arsite.preloadpages(filter_gen, pageprops=True)
    return generator
#---
import cy4
#---
def main(*args):
    generator = list_template_usage()
    num = 0
    #---
    for page in generator:
        num = num + 1
        MainTitle = page.title(as_link=False)
        pywikibot.output( '<<lightyellow>>\n----------\n>> %d >> %s << <<' % ( num , MainTitle) )
        rr = ec_de(MainTitle)
        cy4.StartOnePage(rr)
#---
if __name__ == "__main__":
    main()
#---
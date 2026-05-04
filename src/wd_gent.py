#!/usr/bin/python3
""" """
import logging
import sys
from typing import Iterable

import pywikibot
from pywikibot import pagegenerators

from api_page import load_main_api

logger = logging.getLogger(__name__)


def fetch_user_new_pages(limit="max", namespace="0", user=""):
    api = load_main_api("www", "wikidata")
    new_api = api.NewApi()
    generator = new_api.Get_Newpages(limit=limit, namespace=namespace, user=user)
    return generator


def getusernewpages():
    # python3 core8/pwb.py wd_gent -mynewpages:10 -ns:0
    usernewpages = ""
    ns = ""
    limit = 100
    # ---
    for arg in sys.argv:
        arg, _, value = arg.partition(":")
        arg = arg.removeprefix("-")
        if arg == "usernewpages":
            usernewpages = value
        if arg == "mynewpages":
            usernewpages = "Mr. Ibrahem"
            # ns = "0"
            if value:
                limit = int(value)
        if arg == "limit":
            limit = int(value)
        elif arg == "ns":
            ns = value
    # ---
    if usernewpages and ns == "":
        ns = "0"
    # ---
    lista = []
    # ---
    if usernewpages:
        lista = fetch_user_new_pages(limit=limit, namespace=ns, user=usernewpages)
    # ---
    return lista


def do_title(generator):
    # [page.title(as_link=False) for page in generator]
    for page in generator:
        yield page.title(as_link=False)


def fetch_new_pages(value):
    api = load_main_api("www", "wikidata")
    new_api = api.NewApi()
    generator = new_api.Get_Newpages(limit=value, namespace="0", three_houers=True)
    return generator


def get_gent(listonly=True, *args):
    # ---
    options = {}
    # ---
    genFactory = pagegenerators.GeneratorFactory()
    # ---
    for arge in pywikibot.handle_args(args):
        arg, sep, value = arge.partition(":")
        # ---
        option = arg[1:]
        # ---
        if option in ("summary", "text"):
            if not value:
                input(f"Please enter a value for {arg}")
            options[option] = value
        else:
            options[option] = True
            # ---
            genFactory.handle_arg(arge)
    # ---
    generator = genFactory.getCombinedGenerator()
    # ---
    if generator and listonly:
        # return [page.title(as_link=False) for page in generator]
        return do_title(generator)
    # ---
    if not generator:
        # ---
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            # ---
            if arg == "-newpages2":
                generator = fetch_new_pages(value)
    # ---
    if not generator:
        logger.info("<<lightred>> No pages to work on")
        generator = getusernewpages()
    # ---
    return generator


def get_gent_list(args: Iterable[str] | None = None):
    # ---
    options = {}
    # ---
    genFactory = pagegenerators.GeneratorFactory()
    # ---
    for arge in pywikibot.handle_args(args):
        arg, sep, value = arge.partition(":")
        # ---
        option = arg[1:]
        # ---
        if option in ("summary", "text"):
            if not value:
                input(f"Please enter a value for {arg}")
            options[option] = value
        else:
            options[option] = True
            # ---
            genFactory.handle_arg(arge)
    # ---
    generator = genFactory.getCombinedGenerator()
    # ---
    if generator:
        # return [page.title(as_link=False) for page in generator]
        return do_title(generator)
    # ---
    if not generator:
        # ---
        for arg in sys.argv:
            arg, _, value = arg.partition(":")
            # ---
            if arg == "-newpages2":
                generator = fetch_new_pages(value)
    # ---
    if not generator:
        logger.info("<<lightred>> No pages to work on")
        generator = getusernewpages()
    # ---
    return generator

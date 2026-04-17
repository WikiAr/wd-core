#!/usr/bin/python3
""" """

import os
import sys
from urllib.parse import urlencode

import requests

from .cy_helps import TEST, ec_de_code, make_dada, printo, printt

username = os.getenv("WIKIPEDIA_BOT_USERNAME", "")
password = os.getenv("WIKIPEDIA_BOT_PASSWORD", "")

hiacc = os.getenv("WIKIPEDIA_HIMO_USERNAME", "")
hipass = os.getenv("WIKIPEDIA_HIMO_PASSWORD", "")

api_url = "https://" + "ar.wikipedia.org/w/api.php"

workibrahem = False

if "workibrahem" in sys.argv:
    username = hiacc
    password = hipass
    workibrahem = True
    print("workibrahem active")

headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}

session = {1: requests.session(), "csrftoken": ""}
session[1].headers.update(headers)

returntext = {1: True}

if "text" in sys.argv:
    returntext[1] = False

br = "<br>"


def login():
    # get login token
    r1 = session[1].get(
        api_url,
        params={
            "format": "json",
            "action": "query",
            "meta": "tokens",
            "type": "login",
        },
        timeout=10,
    )
    r1.raise_for_status()
    # ---
    # headers=headers,
    headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
    # ---
    # log in
    r2 = session[1].post(
        api_url,
        data={
            "format": "json",
            "action": "login",
            "lgname": username,
            "lgpassword": password,
            "lgtoken": r1.json()["query"]["tokens"]["logintoken"],
        },
        timeout=10,
        headers=headers,
    )

    # print( str( r2.json() ) )

    if r2.json()["login"]["result"] != "Success":
        raise RuntimeError(r2.json()["login"]["reason"])

    # get edit token
    r3 = session[1].get(
        api_url,
        params={
            "format": "json",
            "action": "query",
            "meta": "tokens",
        },
        timeout=10,
    )
    session["csrftoken"] = r3.json()["query"]["tokens"]["csrftoken"]


login()


def page_put(newtext, maintitle):
    printt(" page_put: <br>")
    # try:
    title = ec_de_code(maintitle, "decode")
    # ---
    summ = "" if "workibrahem" in sys.argv else "بوت:تجربة تحديث بيانات اللاعب"
    # ---
    printt(f" page_put {maintitle}:<br>")
    # print_test2( NewText )
    # ---
    # headers=headers,
    headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
    # ---
    if (not TEST[1] and not TEST[2]) or workibrahem:
        r4 = session[1].post(
            api_url,
            headers=headers,
            data={
                "action": "edit",
                "format": "json",
                "title": title,
                "text": newtext,
                "summary": summ,
                "bot": 1,
                "nocreate": 1,
                "token": session["csrftoken"],
            },
        )
        if workibrahem:
            print(r4.text)
        if "nochange" in r4.text:
            printo("nodiff")
        elif "Success" in r4.text:
            # print('** true .. ' + '[[' + title + ']]' )
            # print('* true . ')
            printo("true")
            # printo( r4.text )
        elif "abusefilter-disallowed" in r4.text and returntext[1]:
            texts = "</br>خطأ عند تعديل الصفحة، قم بنسخ المحتوى أدناه إلى الصفحة:</br>"
            texts += make_dada(newtext, maintitle)
            printo(texts)
        else:
            printo(r4.text)


def GetPageText(title):
    text, item = "", False
    # ---
    printt("**GetPageText: <br>")
    # ---
    url = "https://" + "ar.wikipedia.org/w/api.php"
    # ---
    if title.find("%") != -1:
        title = ec_de_code(title, "decode")
    # ---
    params = {
        "action": "parse",
        "prop": "wikitext|properties",
        "utf8": "1",
        "format": "json",
        "page": title,
    }
    # ---
    printt(f"url:{url}?" + urlencode(params) + "<br>")
    # ---
    json1 = {}
    try:
        json1 = session[1].get(url, params=params, timeout=10).json()

    except requests.exceptions.ReadTimeout:
        print(f"ReadTimeout: {url}")

    except Exception as e:
        print("<<lightred>> Traceback (most recent call last):")
        print(f"<<lightred>> Exception:{e}.")
        print("CRITICAL:")
    # ---
    if not json1:
        return text, item
    # ---
    printt("find json1:<br>")
    # ---
    parse = json1.get("parse", {})
    if parse != {}:
        printt("find parse in json1:<br>")
        # ---
        text = parse.get("wikitext", {}).get("*", "")
        if text:
            printt("find wikitext in parse:<br>")
            printt("find * in parse.wikitext :<br>")
        # ---
        properties = parse.get("properties", [])
        # ---
        if properties != []:
            printt("find properties in parse:<br>")
            for prop in properties:
                if "name" in prop:
                    if prop["name"] == "wikibase_item":
                        item = prop["*"]
                        printt("find item in parse.wikitext :{item}<br>")
                        break
    elif "error" in json1:
        text = False
        if "info" in json1["error"]:
            printt(json1["error"]["info"])
        else:
            printt(json1)
    else:
        printt("no parse in json1:<br>")
        printt(json1)
    # ---
    return text, item

#!/usr/bin/python3
"""
Output JSON handling

This module provides functions for handling JSON output from API calls.
"""

import logging
import os
import time

logger = logging.getLogger(__name__)
file_name = os.path.basename(__file__)


def outbot_json_bot(err):
    # ---
    text = str(err)
    # ---
    err_code = err.get("code", "")
    err_info = err.get("info", "")
    # ---
    extradata = err.get("extradata", [""])
    messages = err.get("messages", [{}])[0]
    msg_name = messages.get("name", "")
    # ---
    msg_html = ""
    if isinstance(messages.get("html", {}), dict):
        msg_html = messages.get("html", {}).get("*", "")
    # ---
    err_wait = "احترازًا من الإساء، يُحظر إجراء هذا الفعل مرات كثيرة في فترةٍ زمنية قصيرة، ولقد تجاوزت هذا الحد"
    # ---
    if err_code == "origin-not-empty":
        _err_ = {
            "error": {
                "code": "origin-not-empty",
                "info": "Can't create redirect on non empty item Q65686922",
                "messages": [
                    {
                        "name": "wikibase-api-origin-not-empty",
                        "parameters": ["Can't create redirect on non empty item Q65686922"],
                        "html": {"*": "Can't create redirect on non empty item Q65686922"},
                    }
                ],
                "*": "",
            },
            "servedby": "mw2356",
        }
        logger.info(f"<<lightred>> msg_html: {msg_html} ")
        logger.info(f"<<lightred>> err_info: {err_info} ")
        return err_code
    # ---
    if err_code == "missingparam":
        # {"error":{"code":"missingparam","info":"The \"token\" parameter must be set.","*":""},"servedby":"mw2350"}
        # if err_info in [r'The \"token\" parameter must be set.', 'The "token" parameter must be set.']:
        logger.info(f"<<lightred>> err_info: {err_info} ")
        return "warn"
    # ---
    elif err_code in ["modification-failed", "failed-modify"]:
        # ---
        logger.info(f"<<lightred>> err_info: {err_info} ")
        # ---
        if msg_name == "wikibase-api-failed-modify":
            # ---
            _merge_err_ = {
                "error": {
                    "code": "failed-modify",
                    "info": "Attempted modification of the Item failed.",
                    "extradata": ["Conflicting sitelinks for arwiki"],
                    "messages": [
                        {
                            "name": "wikibase-api-failed-modify",
                            "parameters": [],
                            "html": {"*": "Attempted modification of the Item failed."},
                        }
                    ],
                    "*": ".",
                },
                "servedby": "mw2404",
            }
            # ---
            logger.info(f"<<lightred>>err msg_name: {msg_name}")
            logger.info(f"<<lightred>>\t: {extradata}")
            return msg_name
        # ---
        if msg_name == "wikibase-validator-label-equals-description":
            z = {
                "code": "modification-failed",
                "info": "Label and description for language code ar can not have the same value.",
                "messages": [
                    {
                        "name": "wikibase-validator-label-equals-description",
                        "parameters": ["ar"],
                        "html": {"*": "لا يمكن أن تكون للتسمية والوصف لرمز اللغة ar نفس القيمة."},
                    }
                ],
                "*": "",
            }
            logger.info(f"<<lightred>>err msg_name: {msg_name}")
            logger.info(f"<<lightred>>\t: {msg_html}")
            return msg_name
        # ---
        if msg_name == "wikibase-validator-label-with-description-conflict":
            _zox = {
                "error": {
                    "code": "modification-failed",
                    "info": 'Item [[Q116681602|Q116681602]] already has label "منحوتة1" associated with language code ar, using the same description text.',
                    "messages": [
                        {
                            "name": "wikibase-validator-label-with-description-conflict",
                            "parameters": [
                                "منحوتة1",
                                "ar",
                                "[[Q116681602|Q116681602]]",
                            ],
                            "html": {
                                "*": 'العنصر <a href="/wiki/Q116681602" title="Q116681602">Q116681602</a> له وسم «منحوتة1» يرتبط برمز اللغة ar باستخدام نفس نص الوصف.'
                            },
                        }
                    ],
                    "*": "",
                },
                "servedby": "",
            }
            # ---
            # logger.info(f'<<lightred>>err msg_name: {msg_name}')
            logger.info("<<lightred>>same description:")
            # ---
            lab, code, q = messages.get("parameters", [])
            # ---
            logger.info(f"<<lightred>>\t: lab:{lab}, code:{code}, q:{q}")
            # ---
            return "same description"
        return "warn"
    elif err_code == "unresolved-redirect":
        # ---
        # {'code': 'unresolved-redirect', 'info': 'The given entity ID refers to a redirect, which is not supported in this context.', 'messages': [{'name': 'wikibase-api-unresolved-redirect', 'parameters': [], 'html': {'*': 'يشير معرِّف الكائن المحدد إلى تحويلة، وهذا غير مدعوم في السياق الحالي.'}}], '*': 'See https://www.wikidata.org/w/api.php for API usage. Subscribe to the mediawiki-api-announce mailing list at &lt;https://lists.wikimedia.org/postorius/lists/mediawiki-api-announce.lists.wikimedia.org/&gt; for notice of API deprecations and breaking changes.'}
        logger.info("<<lightred>>    - unresolved-redirect")
        return "unresolved-redirect"
        # ---
    elif err_code == "failed-save":
        # {'code': 'failed-save', 'info': 'The save has failed.', 'messages': [{'name': 'wikibase-api-failed-save', 'parameters': [], 'html': {'*': 'لم ينجح الحفظ.'}}, {'name': 'actionthrottledtext', 'parameters': [], 'html': {'*': 'احترازًا من الإساء، يُحظر إجراء هذا الفعل مرات كثيرة في فترةٍ زمنية قصيرة، ولقد تجاوزت هذا الحد.\nمن فضلك حاول مجددًا بعد عدة دقائق.'}}], '*': ''}
        if err_wait in text:
            logger.info(f'<<lightred>> {file_name} - "{err_wait} time.sleep(5) " ')
            time.sleep(5)
            return "reagain"
        # ---
        logger.info(f'<<lightred>>    - "{err_code}" ')
        logger.info(text)
        return False
    elif err_code == "no-external-page":
        # ---
        _a_ = {
            "error": {
                "code": "no-external-page",
                "info": 'The external client site "enwiki" did not provide page information for page "Category:Romanian male songwriters".',
                "messages": [
                    {
                        "name": "wikibase-api-no-external-page",
                        "parameters": ["enwiki", "Category:Romanian male songwriters"],
                        "html": {
                            "*": 'لم يوفر موقع العميل الخارجي "enwiki" معلومات الصفحة لصفحة "Category:Romanian male songwriters".'
                        },
                    }
                ],
                "*": "",
            },
            "servedby": "mw2289",
        }
        # ---
        logger.info(f'<<lightred>>    - "{err_code}" ')
        logger.info(text)
        return False
        # ---
    else:
        # ---
        if "wikibase-api-invalid-json" in text:
            logger.info('<<lightred>>    - "wikibase-api-invalid-json" ')
            logger.info(text)
            return "wikibase-api-invalid-json"
        # ---
        elif "Could not find an Item containing a sitelink to the provided site and page name" in text:
            logger.info(
                "<<lightred>> ** error. : Could not find an Item containing a sitelink to the provided site and page name "
            )
            return "Could not find an Item containing a sitelink to the provided site and page name"
        else:
            return err_code


def outbot_json(js_text, fi="", line="", timesleeps=0, NoWait=False):
    # ---
    success = js_text.get("success", 0)
    # ---
    if success == 1:
        # ---
        # {"entity":{"sitelinks":{"arwiki":{"site":"arwiki","title":"قالب:Db-attack-deleted","badges":[],"url":"https://ar.wikipedia.org/wiki/%D9%82%D8%A7%D9%84%D8%A8:Db-attack-deleted"}},"id":"Q97928551","type":"item","lastrevid":1242627521,"nochange":""},"success":1}
        # ---
        logger.info(f"<<lightgreen>> ** true. {fi}")
        # ---
        return True
    # ---
    err = js_text.get("error", {})
    # ---
    if not err:
        return "warn"
    # ---
    if fi:
        logger.info(f"<<lightred>> ** error. : {fi} ")
    # ---
    if line:
        logger.info(f"<<lightpurple>> ** line. : {line} ")
    # ---
    return outbot_json_bot(err)

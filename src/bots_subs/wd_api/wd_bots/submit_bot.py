
"""

from .wd_bots.submit_bot import submitAPI

"""
import logging

import pywikibot.data.api as apit
import requests

logger = logging.getLogger(__name__)

Session_t = {1: requests.Session()}


def submitAPI(params):
    # ---
    # global Session_t
    # ---
    Code = "www"
    family = "wikidata"
    # ---
    params["formatversion"] = 1
    params["utf8"] = 1
    params["format"] = "json"
    # ---
    if params.get("titles"):
        titles = params["titles"]
        if isinstance(titles, list):
            params["titles"] = "|".join(titles)
    # ---
    # himo API
    if family == "commons":
        family = "wikimedia"
    # ---
    mainurl = f"https://{Code}.{family}.org/w/api.php"
    # ---
    encode_params = apit.encode_url(params)
    url = f"https://{Code}.{family}.org/w/api.php?{encode_params}"
    url2 = url.replace("&format=json", "").replace("?format=json", "?")
    # ---
    r22 = False
    # ---
    headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
    # ---
    try:
        r22 = Session_t[1].post(mainurl, data=params, timeout=10, headers=headers)

    except requests.exceptions.ReadTimeout:
        logger.info(f"ReadTimeout: {mainurl}")

    except Exception as e:
        logger.exception("Exception:", exc_info=True)
        _known_exceptions = [
            "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))",
            """('Connection aborted.', OSError("(104, "ECONNRESET")"))""",
            """""",
        ]

    # ---
    json1 = {}
    # ---
    if r22:
        try:
            json1 = r22.json()
        except Exception as e:
            logger.warning(f"{e} - {url2}")
            json1 = {}
    # ---
    return json1

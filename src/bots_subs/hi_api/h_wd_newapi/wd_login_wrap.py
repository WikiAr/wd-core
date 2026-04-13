"""

"""

import os
import sys

try:
    from newapi import ALL_APIS
except ImportError:
    sys.path.append("I:/core/bots/new/newapi_bot")
    from newapi import ALL_APIS

from newapi import Login


def _load_credentials(mr_or_bot) -> dict[str, str]:

    username = os.getenv("WIKIPEDIA_BOT_USERNAME", "")
    password = os.getenv("WIKIPEDIA_BOT_PASSWORD", "")

    hiacc = os.getenv("WIKIPEDIA_HIMO_USERNAME", "")
    hipass = os.getenv("WIKIPEDIA_HIMO_PASSWORD", "")

    if "workibrahem" in sys.argv:
        username = hiacc
        password = hipass

    User_tables_bot = {
        "username": username,
        "password": password,
    }

    User_tables_ibrahem = {
        "username": hiacc,
        "password": hipass,
    }

    return User_tables_bot if mr_or_bot == "bot" else User_tables_ibrahem


def log_in_wikidata(mr_or_bot="bot", www="www") -> Login:
    # ---
    users_data = _load_credentials(mr_or_bot)
    # ---
    www2 = "test" if "wikidata_test" in sys.argv else "www"
    # ---
    if www != "www":
        www2 = www
    # ---
    api = ALL_APIS(
        lang=www2,
        family="wikidata",
        username=users_data["username"],
        password=users_data["password"],
    )
    # ---
    login_bot = api.login_bot
    # ---
    return login_bot

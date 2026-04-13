"""
from api_page import load_main_api
api = load_main_api("en", "wikipedia")
page = api.MainPage('Main Page Title')
"""

import functools
import os
import sys

from newapi import ALL_APIS


@functools.lru_cache(maxsize=1)
def _load_credentials() -> tuple[str, str]:
    username = os.getenv("WIKIPEDIA_BOT_USERNAME", "")
    password = os.getenv("WIKIPEDIA_BOT_PASSWORD", "")

    if "workibrahem" in sys.argv:
        username = os.getenv("WIKIPEDIA_HIMO_USERNAME", "")
        password = os.getenv("WIKIPEDIA_HIMO_PASSWORD", "")

    return username, password


@functools.lru_cache(maxsize=1)
def load_main_api(lang, family="wikipedia") -> ALL_APIS:
    """
    Loads and returns an instance of ALL_APIS for the specified language and family, using cached credentials.
    Args:
        lang (str): The language code for the API (e.g., 'en', 'fr').
        family (str, optional): The family of the API (default is 'wikipedia').

    Returns:
        ALL_APIS: An instance of the ALL_APIS class initialized with the provided language, family, and user credentials.

    Notes:
        - The result of this function is cached with an LRU cache of size 1.
        - Credentials are loaded internally via the _load_credentials() function.
    """
    username, password = _load_credentials()
    return ALL_APIS(
        lang=lang,
        family=family,
        username=username,
        password=password,
    )

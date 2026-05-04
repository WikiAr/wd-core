"""
from api_page import load_main_api
api = load_main_api("en", "wikipedia")
page = api.MainPage('Main Page Title')
cat_members = api.CatDepth('Category Title')
new_api = api.NewApi()
"""

import functools
import os
import sys

from newapi import AllAPIS


@functools.lru_cache(maxsize=1)
def _load_credentials() -> tuple[str, str]:
    username = os.getenv("WIKIPEDIA_BOT_USERNAME", "")
    password = os.getenv("WIKIPEDIA_BOT_PASSWORD", "")

    if "workibrahem" in sys.argv:
        username = os.getenv("WIKIPEDIA_HIMO_USERNAME", "")
        password = os.getenv("WIKIPEDIA_HIMO_PASSWORD", "")

    return username, password


@functools.lru_cache(maxsize=1)
def load_main_api(lang, family="wikipedia") -> AllAPIS:
    """
    Loads and returns an instance of AllAPIS for the specified language and family, using cached credentials.
    Args:
        lang (str): The language code for the API (e.g., 'en', 'fr').
        family (str, optional): The family of the API (default is 'wikipedia').

    Returns:
        AllAPIS: An instance of the AllAPIS class initialized with the provided language, family, and user credentials.

    Notes:
        - The result of this function is cached with an LRU cache of size 1.
        - Credentials are loaded internally via the _load_credentials() function.
    """
    username, password = _load_credentials()
    return AllAPIS(
        lang=lang,
        family=family,
        username=username,
        password=password,
    )

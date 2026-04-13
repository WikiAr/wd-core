# -*- coding: utf-8 -*-
"""
Himo Wikidata bots package

This package contains Wikidata-specific bots.
"""

# Expose the main modules
from . import bot_wd, bot_wp

__all__ = [
    "bot_wd",
    "bot_wp",
]

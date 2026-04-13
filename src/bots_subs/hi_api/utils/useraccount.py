"""
from .utils.useraccount import qs_token, qs_tokenbot
"""

import os

qs_token = os.getenv("QS_TOKEN", "")
qs_tokenbot = os.getenv("QS_TOKEN_BOT", "")

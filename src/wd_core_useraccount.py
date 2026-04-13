""" """

import os

qs_token = os.getenv("QS_TOKEN", "")
qs_tokenbot = os.getenv("QS_TOKEN_BOT", "")

username = os.getenv("WIKIPEDIA_BOT_USERNAME", "")
password = os.getenv("WIKIPEDIA_BOT_PASSWORD", "")

hiacc = os.getenv("WIKIPEDIA_HIMO_USERNAME", "")
hipass = os.getenv("WIKIPEDIA_HIMO_PASSWORD", "")

User_tables_ibrahem = {
    "username": hiacc,
    "password": hipass,
}

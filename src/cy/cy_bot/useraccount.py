import sys
import os

from dotenv import load_dotenv
load_dotenv()

qs_token = os.getenv("QS_TOKEN")
qs_tokenbot = os.getenv("QS_TOKEN_BOT")



username = os.getenv("WIKIPEDIA_BOT_USERNAME")
password = os.getenv("WIKIPEDIA_BOT_PASSWORD")

hiacc = os.getenv("WIKIPEDIA_HIMO_USERNAME")
hipass = os.getenv("WIKIPEDIA_HIMO_PASSWORD")

if "workibrahem" in sys.argv:
    username = hiacc
    password = hipass

#!/usr/bin/python3
""" """
import logging
import sys
import time

import requests

logger = logging.getLogger(__name__)


class ClassGetURL:
    def __init__(self, url):
        self.start = time.time()
        self.url = url
        self.html = ""
        self.session = requests.session()
        self.session.headers.update(
            {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
        )

    def open_it(self):
        if not self.url:
            logger.info('open_url.py: self.url == ""')
            return ""
        if "printurl" in sys.argv:
            logger.info(f"getURL: {self.url}")

        try:
            req = self.session.get(self.url, timeout=10)
            # ---
            if 500 <= req.status_code < 600:
                logger.info(f"received {req.status_code} status from {req.url}")
                self.html = ""
            else:
                # ---
                self.html = req.text

        except requests.exceptions.ReadTimeout:
            logger.info(f"ReadTimeout: {self.url}")

        except Exception:
            logger.exception("Exception:", exc_info=True)
            _except_ions = [
                "Too long GET request",
                "HTTPSConnectionPool(host='en.wikipedia.org', port=443): Read timed out. (read timeout=45)",
                "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))",
                """('Connection aborted.', OSError("(104, 'ECONNRESET')"))""",
                """HTTP Error 414: URI Too Long""",
                "HTTP Error 500: Internal Server Error",
            ]
        # ---
        return self.html


def open_the_url(url):
    bot = ClassGetURL(url)
    return bot.open_it()

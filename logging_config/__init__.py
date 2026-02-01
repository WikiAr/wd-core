# -*- coding: utf-8 -*-
"""
from pathlib import Path
from logging_config import setup_logging
setup_logging(Path(__file__).parent.name)
"""
import logging
import sys
from pathlib import Path

name = Path(__file__).parent.name


def setup_logging(name):
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(name)
    # Check if handler already exists to avoid duplicates
    if not logger.handlers:
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler(sys.stdout)
        handler.setFormatter(logging.Formatter("%(filename)s:%(lineno)d %(funcName)s() - %(levelname)s - %(message)s"))
        logger.addHandler(handler)


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
python3 pwb.py dump/p31 jsonnew
python3 pwb.py dump/p31 makereport
python3 pwb.py dump/p31
python3 pwb.py dump/p31 test nosave
"""
#
# (C) Ibrahem Qasim, 2022
#
#
import sys
import os
import bz2
import json
import time
#---
from dump.claims5 import mainar
#---
mainar(ty='P31')
#---
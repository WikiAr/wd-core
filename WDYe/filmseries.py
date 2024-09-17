#!/usr/bin/env python3
#  python pwb.py wd/wikinews
#
#

# ---

from wd_api import newdesc

#   newdesc.mainfromQuarry2( topic , Quarry, translations)
# ---
from desc_dicts.descraptions import DescraptionsTable

translations = {'film series': DescraptionsTable['film series']}
# ---
quarry = 'SELECT ?item  WHERE { ?item wdt:P31 wd:Q24856 \nFILTER NOT EXISTS { ?item schema:description ?des. filter (lang(?des) = "ar")} .}'
topic = 'film series'
# ---
newdesc.mainfromQuarry2(topic, quarry, translations)
# ---

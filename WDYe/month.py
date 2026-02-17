#!/usr/bin/env python3
#
# ---
import sys

import logging
logger = logging.getLogger(__name__)

# ---
from wd_api import newdesc

# ---
quuu = {
    'month': '''
SELECT DISTINCT ?item
WHERE {
?item schema:description "%s"@en  .
FILTER NOT EXISTS {?item schema:description ?ar.
             FILTER((LANG(?ar)) = "ar" ) }
}
limit 3000
'''
}
# ---
# newdesc.work22(q , topic, translations)

# newdesc.mainfromQuarry2( topic , Quarry, translations)
# --- ----------------------
translations = {
    'month': {'ar': 'شهر'},
    "island in Indonesia": {"ar": "جزيرة في إندونيسيا"},
}


def main_from_quarry(topic):
    logger.info('*<<lightyellow>> main_from_quarry:')
    Quarry = quuu["month"] % topic
    if sys.argv and "OFFSET" in sys.argv:
        Quarry = f"{Quarry} OFFSET 100000"
    newdesc.mainfromQuarry2(topic, Quarry, translations)


# ---
if __name__ == "__main__":
    main_from_quarry("island in Indonesia")
    main_from_quarry('month')
# ---

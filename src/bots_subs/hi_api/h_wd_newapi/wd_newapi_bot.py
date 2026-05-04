""" """

import logging
import sys
import time

from newapi import Login

from ..utils import lag_bot
from ..utils.handle_wd_errors import WD_ERRORS_HANDLER

logger = logging.getLogger(__name__)


class WdAPI(WD_ERRORS_HANDLER):
    def __init__(self, login_bot, mr_or_bot="bot"):
        # ---
        self.login_bot: Login = login_bot
        # ---
        self.lang = "test" if "testwikidata" in sys.argv else "www"
        self.family = "wikidata"
        # ---
        self.usernamex = self.login_bot.user_login
        # ---
        WD_ERRORS_HANDLER.__init__(self)
        # ---
        logger.info(f"<<lightgreen>> WdAPI: {mr_or_bot}, {self.usernamex=} \n")

    def post_to_newapi(self, params={}, data={}, tage="", editgroups="", max_retry=0, **kwargs):
        # ---
        if not params and data:
            params = data
        # ---
        params = self.filter_data(params, tage=tage, editgroups=editgroups)
        # ---
        results = self.login_bot.post_params(params, request_type="get", get_csrf=True, do_error=False, max_retry=max_retry)
        # ---
        if results.get("servedby"):
            results["servedby"] = ""
        # ---
        error = results.get("error", {})
        error_code = error.get("code", "")
        # ---
        if error_code == "maxlag" and max_retry < 4:
            self.lag_work(error)
            # ---
            logger.info(f"<<purple>>post_to_newapi: <<red>> lag_work: {max_retry=}")
            # ---
            return self.post_to_newapi(params=params, tage=tage, editgroups=editgroups, max_retry=max_retry + 1)
        # ---
        if error:
            # ---
            er = self.handle_err_wd(error, function="", params=params)
            # ---
            logger.info(f"<<purple>>post_to_newapi: <<red>> handle_err_wd: {er}")
            # return er
        # ---
        success = results.get("success", 0)
        # ---
        if success == 1:
            # ---
            # {"entity":{"sitelinks":{"arwiki":{}},"id":"Q97928551","type":"item","lastrevid":1242627521,"nochange":""},"success":1}
            # ---
            if lag_bot.newsleep[1] != 0:
                logger.info(f"<<lightgreen>> ** true. sleep({lag_bot.newsleep[1]})")
                time.sleep(lag_bot.newsleep[1])
            else:
                logger.info("<<lightgreen>> ** true.")
            # return True
        # ---
        return results

    def filter_data(self, data, editgroups, tage):
        # ---
        lag_bot.do_lag()
        # ---
        if "maxlag" not in data:
            data["maxlag"] = lag_bot.FFa_lag[1] + 1
        # ---
        data["format"] = "json"
        data["utf8"] = 1
        # ---
        if "summary" in data:
            if self.usernamex.find("bot") == -1:
                del data["summary"]
        # ---
        data.setdefault("formatversion", 1)
        # ---
        return data

    def lag_work(self, err):
        # ---
        _ixix = {
            "error": {
                "code": "maxlag",
                "info": "Waiting for wdqs1006: 3.2333333333333 seconds lagged.",
                "host": "wdqs1006",
                "lag": 3.333333333333334,
                "type": "wikibase-queryservice",
                "queryserviceLag": 194,
            },
            "servedby": "",
        }
        # ---
        lag_bot.find_lag(err)
        # ---
        return "reagain"

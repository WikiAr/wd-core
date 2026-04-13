""" """

import logging
import sys
import time

from newapi import Login

from ..utils import lag_bot
from ..utils.handle_wd_errors import WD_ERRORS_HANDLER

logger = logging.getLogger(__name__)


class WD_API(WD_ERRORS_HANDLER):
    def __init__(self, login_bot, mr_or_bot="bot"):
        # ---
        self.login_bot: Login = login_bot
        # ---
        self.lang = "test" if "testwikidata" in sys.argv else "www"
        self.family = "wikidata"
        # ---
        self.usernamex = self.login_bot.user_login
        # ---
        # super().__init__(self.post_continue)
        # ---
        WD_ERRORS_HANDLER.__init__(self)
        # ---
        logger.info(f"<<lightgreen>> WD_API: {mr_or_bot}, {self.usernamex=} \n")

    def get_rest_result(self, url) -> dict:
        # ---
        return self.login_bot.get_rest_result(url)

    def post_params(self, params, Type="get", addtoken=False, GET_CSRF=True, files=None, do_error=False, max_retry=0):
        # ---
        return self.login_bot.post_params(
            params, Type=Type, addtoken=addtoken, GET_CSRF=GET_CSRF, files=files, do_error=do_error, max_retry=max_retry
        )

    def post_continue(
        self, params, action, _p_="pages", p_empty=None, Max=500000, first=False, _p_2="", _p_2_empty=None
    ):
        return self.login_bot.post_continue(
            params, action, _p_=_p_, p_empty=p_empty, Max=Max, first=first, _p_2=_p_2, _p_2_empty=_p_2_empty
        )

    def post_to_newapi(self, params={}, data={}, tage="", editgroups="", max_retry=0, **kwargs):
        # ---
        if not params and data:
            params = data
        # ---
        params = self.filter_data(params, tage=tage, editgroups=editgroups)
        # ---
        results = self.post_params(params, do_error=False)
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

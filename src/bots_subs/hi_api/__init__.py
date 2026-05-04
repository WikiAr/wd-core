#!/usr/bin/python3
""" """
from newapi import Login

from .h_wd_newapi.wd_login_wrap import log_in_wikidata
from .h_wd_newapi.wd_newapi_bot import WdAPI
from .req_bots_new import claims_wd, descriptions_wd, labels_wd


class HimoAPIBot:
    def __init__(self, mr_or_bot="bot", www="www"):
        # ---
        self.login_bot: Login = log_in_wikidata(mr_or_bot=mr_or_bot, www=www)
        # ---
        self.wdapi_new = WdAPI(self.login_bot, mr_or_bot=mr_or_bot)
        # ---
        self.session_post = self.wdapi_new.post_to_newapi

        # =======================
        claims_wd_bot = claims_wd.WD_Claims(self.wdapi_new)
        descriptions_wd_bot = descriptions_wd.WD_Descriptions(self.wdapi_new)
        labels_wd_bot = labels_wd.WD_Labels(self.wdapi_new, descriptions_wd_bot.Des_API)
        # ---

        # =======================

        # ---
        self.add_quall = claims_wd_bot.add_quall
        self.Claim_API2 = claims_wd_bot.Claim_API2
        self.Claim_API_time = claims_wd_bot.Claim_API_time

        # =======================

        # ---
        self.New_Mult_Des = descriptions_wd_bot.New_Mult_Des
        self.New_Mult_Des_2 = descriptions_wd_bot.New_Mult_Des_2
        self.Des_API = descriptions_wd_bot.Des_API
        # ---
        # =======================

        # ---
        self.Labels_API = labels_wd_bot.Labels_API
        self.Add_Labels_if_not_there = labels_wd_bot.Add_Labels_if_not_there
        self.Alias_API = labels_wd_bot.Alias_API
        # =======================


__all__ = [
    "HimoAPIBot",
]

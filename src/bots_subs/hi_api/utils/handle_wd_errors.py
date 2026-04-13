"""


"""

import logging
import sys

logger = logging.getLogger(__name__)


class WD_ERRORS_HANDLER:
    def __init__(self):
        logger.info("class WD_ERRORS_HANDLER:")

    def handle_err_wd(self, error: dict, function: str = "", params: dict = None):
        """Handle errors related to the specified function.

        This method processes an error dictionary returned from an API call,
        extracting relevant error codes and information. It outputs error
        messages based on the error code and may modify the provided parameters.
        The function handles specific error codes such as 'abusefilter-
        disallowed', 'no-such-entity', 'protectedpage', 'articleexists', and
        'maxlag', providing appropriate responses for each case.

        Args:
            error (dict): A dictionary containing error information from the API.
            function (str?): The name of the function that encountered the error.
                Defaults to an empty string.
            params (dict?): A dictionary of parameters that may be modified
                based on the error. Defaults to None.

        Returns:
            Union[str, bool]: Returns a string indicating the error type for specific
                errors or False for others.

        Raises:
            Exception: If the 'raise' argument is present in the command line arguments,
                an exception is raised with the error information.
        """

        # ---
        # {'error': {'code': 'articleexists', 'info': 'The article you tried to create has been created already.', '*': 'See https://ar.wikipedia.org/w/api.php for API usage. Subscribe to the mediawiki-api-announce mailing list at &lt;https://lists.wikimedia.org/postorius/lists/mediawiki-api-announce.lists.wikimedia.org/&gt; for notice of API deprecations and breaking changes.'}, 'servedby': 'mw1425'}
        # ---
        err_code = error.get("code", "")
        err_info = error.get("info", "")
        # ---
        tt = f"<<lightred>>{function} ERROR: <<defaut>>code:{err_code}."
        logger.info(tt)
        # ---["protectedpage", 'تأخير البوتات 3 ساعات', False]
        if err_code == "abusefilter-disallowed":
            # ---
            # oioioi = {'error': {'code': 'abusefilter-disallowed', 'info': 'This', 'abusefilter': {'id': '169', 'description': 'تأخير البوتات 3 ساعات', 'actions': ['disallow']}, '*': 'See https'}, 'servedby': 'mw1374'}
            # ---
            abusefilter = error.get("abusefilter", "")
            description = abusefilter.get("description", "")
            logger.info(f"<<lightred>> ** abusefilter-disallowed: {description} ")
            if description in [
                "تأخير البوتات 3 ساعات",
                "تأخير البوتات 3 ساعات- 3 من 3",
                "تأخير البوتات 3 ساعات- 1 من 3",
                "تأخير البوتات 3 ساعات- 2 من 3",
            ]:
                return False
            return description
        # ---
        if err_code == "no-such-entity":
            logger.info("<<lightred>> ** no-such-entity. ")
            return False
        # ---
        if err_code == "protectedpage":
            logger.info("<<lightred>> ** protectedpage. ")
            # return "protectedpage"
            return False
        # ---
        if err_code == "articleexists":
            logger.info("<<lightred>> ** article already created. ")
            return "articleexists"
        # ---
        if err_code == "maxlag":
            logger.info("<<lightred>> ** maxlag. ")
            return False
        # ---
        params["data"] = {}
        logger.info(f"<<lightred>>{function} ERROR: <<defaut>>info: {err_info}, {params=}")
        # ---
        if "raise" in sys.argv:
            raise Exception(error)

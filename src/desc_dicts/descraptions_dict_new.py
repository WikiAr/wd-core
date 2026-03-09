"""
# https://www.wikidata.org/wiki/User:Mr._Ibrahem/descraptions.json?action=raw
"""
import functools
import logging
from pathlib import Path
from desc_dicts.descraptions_dict import many_lang_qid_desc, replace_desc
from wd_utils.utils import load_data_from_url, open_file_json_check_time, save_json_data

logger = logging.getLogger(__name__)

back_up_data = {
    "descraptions": many_lang_qid_desc,
    "replace_descraptions": replace_desc,
}


@functools.lru_cache(maxsize=1)
def get_data(file_name: str) -> dict[str, dict[str, str]]:
    """
    Fetch data from file, URL, or backup. Returns data and file path.
    file_name one of ("descraptions", "replace_descraptions")
    """
    file_path = Path(__file__).parent / f"{file_name}.json"

    data = open_file_json_check_time(file_path)

    if not data:
        data = load_data_from_url(page_name=file_name)
        if data:
            save_json_data(file_path, data)
    if not data:
        data = back_up_data.get(file_name, {})

    return data

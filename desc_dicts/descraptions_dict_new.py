# https://www.wikidata.org/wiki/User:Mr._Ibrahem/descraptions.json?action=raw
import json
import logging
import requests
from pathlib import Path
from desc_dicts.descraptions_dict import many_lang_qid_desc as backup_data

many_lang_qid_desc = {}
logger = logging.getLogger(__name__)


def load_data_from_url(page_name="descraptions.json"):
    url = f"https://www.wikidata.org/wiki/User:Mr._Ibrahem/{page_name}?action=raw"

    headers = {"User-Agent": "Himo bot/1.0 (https://himo.toolforge.org/; tools.himo@toolforge.org)"}
    try:
        session = requests.Session()
        request = session.get(url, headers=headers)
        if request.status_code == 200:
            data = json.loads(request.text)
            return data
        else:
            print(f"Error: {request.status_code}")
            return {}
    except Exception:
        logger.exception(f"Error occurred while loading data from URL, {page_name}")
    return {}


def open_file_json(file_path: Path):
    if not file_path.exists():
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except Exception:
        logger.exception(f"Error occurred while loading data from file, {file_path}")

    return {}


def get_data(file_name: str) -> dict[str, dict[str, str]]:
    """
    file_name one of ("descraptions", "replace_descraptions")
    """
    file_path = Path(__file__).parent / f"{file_name}.json"
    data = open_file_json(file_path)

    if not data:
        data = load_data_from_url(page_name=file_name)

    if not data and file_name == "descraptions":
        data = backup_data

    return data

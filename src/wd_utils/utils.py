"""
"""
import datetime
import json
import logging
import os
import requests
from pathlib import Path

logger = logging.getLogger(__name__)


def load_data_from_url(page_name="descraptions.json"):
    if not page_name.endswith(".json"):
        page_name = f"{page_name}.json"

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


def get_file_date(file_path: Path) -> str:
    """Get file modification date as YYYY-MM-DD string, or empty string if file doesn't exist."""
    if not file_path.exists():
        return ""
    mtime = os.path.getmtime(file_path)
    return datetime.datetime.fromtimestamp(mtime).strftime("%Y-%m-%d")


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


def are_dates_same(today, file_date) -> bool:
    return file_date == today


def open_file_json_check_time(file_path: Path):
    """
    file_name one of ("descraptions", "replace_descraptions")
    """
    data = {}

    if file_path.exists():
        today = datetime.datetime.now().strftime("%Y-%m-%d")
        file_date = get_file_date(file_path)

        # Check if file date matches today's date
        if are_dates_same(today, file_date):
            data = open_file_json(file_path)

    return data


def save_json_data(file_path, data):
    try:
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
    except Exception:
        logger.exception(f"Error occurred while saving data to file, {file_path}")

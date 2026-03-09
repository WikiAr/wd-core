import pytest

from src.wd_utils.utils import (
    get_file_date,
    open_file_json,
    open_file_json_check_time,
    are_dates_same,
)


def test_load_data_from_url():
    """
    no need to test requests
    """


class TestCheckDate:
    def test_check_date(self):
        # Test with a valid date string
        today = "2023-01-01"
        assert are_dates_same(today, "2023-01-01") is True

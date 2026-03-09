import datetime
import json
import os

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


class TestGetFileDate:
    def test_get_file_date_existing_file(self, tmp_path):
        """Test get_file_date with an existing file."""
        test_file = tmp_path / "test.json"
        test_file.write_text('{"key": "value"}')

        result = get_file_date(test_file)

        # Should return a valid date string in YYYY-MM-DD format
        assert len(result) == 10
        assert result[4] == "-"
        assert result[7] == "-"
        # Verify it's a reasonable year
        assert int(result[:4]) >= 2020

    def test_get_file_date_nonexistent_file(self, tmp_path):
        """Test get_file_date with a non-existent file."""
        nonexistent_file = tmp_path / "nonexistent.json"

        result = get_file_date(nonexistent_file)

        assert result == ""

    def test_get_file_date_directory(self, tmp_path):
        """Test get_file_date with a directory (edge case)."""
        test_dir = tmp_path / "test_dir"
        test_dir.mkdir()

        result = get_file_date(test_dir)

        # Should return a valid date string since directories have mtime
        assert len(result) == 10


class TestOpenFileJson:
    def test_open_file_json_existing_valid_file(self, tmp_path):
        """Test open_file_json with an existing valid JSON file."""
        test_file = tmp_path / "test.json"
        expected_data = {"key": "value", "number": 42}
        test_file.write_text(json.dumps(expected_data))

        result = open_file_json(test_file)

        assert result == expected_data

    def test_open_file_json_nonexistent_file(self, tmp_path):
        """Test open_file_json with a non-existent file."""
        nonexistent_file = tmp_path / "nonexistent.json"

        result = open_file_json(nonexistent_file)

        assert result == {}

    def test_open_file_json_invalid_json(self, tmp_path):
        """Test open_file_json with an invalid JSON file."""
        test_file = tmp_path / "invalid.json"
        test_file.write_text("not valid json {")

        result = open_file_json(test_file)

        assert result == {}

    def test_open_file_json_empty_file(self, tmp_path):
        """Test open_file_json with an empty file."""
        test_file = tmp_path / "empty.json"
        test_file.write_text("")

        result = open_file_json(test_file)

        assert result == {}

    def test_open_file_json_empty_json_object(self, tmp_path):
        """Test open_file_json with an empty JSON object."""
        test_file = tmp_path / "empty_obj.json"
        test_file.write_text("{}")

        result = open_file_json(test_file)

        assert result == {}

    def test_open_file_json_array(self, tmp_path):
        """Test open_file_json with a JSON array."""
        test_file = tmp_path / "array.json"
        expected_data = [1, 2, 3]
        test_file.write_text(json.dumps(expected_data))

        result = open_file_json(test_file)

        assert result == expected_data


class TestOpenFileJsonCheckTime:
    def test_open_file_json_check_time_same_day(self, tmp_path):
        """Test open_file_json_check_time when file was modified today."""
        import time

        test_file = tmp_path / "test.json"
        expected_data = {"key": "value"}
        test_file.write_text(json.dumps(expected_data))

        # Touch the file to ensure it has today's date
        current_time = time.time()
        os.utime(test_file, (current_time, current_time))

        result = open_file_json_check_time(test_file)

        assert result == expected_data

    def test_open_file_json_check_time_nonexistent_file(self, tmp_path):
        """Test open_file_json_check_time with a non-existent file."""
        nonexistent_file = tmp_path / "nonexistent.json"

        result = open_file_json_check_time(nonexistent_file)

        assert result == {}

    def test_open_file_json_check_time_old_file(self, tmp_path, mocker):
        """Test open_file_json_check_time when file has an old modification date."""
        test_file = tmp_path / "old.json"
        test_file.write_text(json.dumps({"key": "value"}))

        # Mock get_file_date to return an old date (different from today)
        # This simulates a file that was modified on a different day
        mocker.patch("src.wd_utils.utils.get_file_date", return_value="2020-01-01")

        result = open_file_json_check_time(test_file)

        # Should return empty dict because file date doesn't match today
        assert result == {}

    def test_open_file_json_check_time_invalid_json(self, tmp_path):
        """Test open_file_json_check_time with invalid JSON content."""
        import time

        test_file = tmp_path / "invalid.json"
        test_file.write_text("not valid json")

        # Touch the file to ensure it has today's date
        current_time = time.time()
        os.utime(test_file, (current_time, current_time))

        result = open_file_json_check_time(test_file)

        assert result == {}

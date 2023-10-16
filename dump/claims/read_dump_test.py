import sys
from pathlib import Path
core_dir = Path(__file__).parent.parent
sys.path.append(core_dir)
# ---
import unittest
from unittest.mock import patch
from dump.claims.read_dump import log_dump, get_file_info, check_file_date, read_file

class TestReadDump(unittest.TestCase):

    @patch('builtins.open', new_callable=unittest.mock.mock_open)
    @patch('json.dump')
    def test_log_dump(self, mock_json_dump, mock_open):
        tab = {"key": "value"}
        _claims = "claims"
        log_dump(tab, _claims)
        mock_open.assert_called_once_with("/data/project/himo/dumps/claims.json", "w", encoding='utf-8')
        mock_json_dump.assert_called_once_with(tab, mock_open())

    def test_get_file_info(self):
        file_path = "dump/claims/read_dump.py"
        self.assertEqual(get_file_info(file_path), "2022-01-01")

    @patch('sys.exit')
    def test_check_file_date(self, mock_sys_exit):
        file_date = "2022-01-01"
        check_file_date(file_date)
        mock_sys_exit.assert_called_once_with(0)

    @patch('dump.claims.read_dump.get_file_info')
    @patch('dump.claims.read_dump.check_file_date')
    @patch('os.path.isfile')
    def test_read_file(self, mock_isfile, mock_check_file_date, mock_get_file_info):
        mock_isfile.return_value = True
        mock_get_file_info.return_value = "2022-01-01"
        try:
            read_file()
        except Exception as e:
            self.fail(f"read_file() raised exception {e}")

if __name__ == '__main__':
    unittest.main()

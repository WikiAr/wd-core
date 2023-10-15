# wd-core
wikidata core

## Test Files

### cy5_test.py
This test file contains unit tests for the functions in the cy5.py file. It tests functions such as encode_arabic, ec_de_code, findflag, fix_label, and make_temp_lines.

To run these tests, use the following command:
```bash
python -m unittest cy/cy5_test.py
```

### si3g_test.py
This test file contains a unit test for the mainwithcat2 function in the si3g.py file.

To run this test, use the following command:
```bash
python -m unittest np/si3g_test.py
```

### read_dump_test.py
This test file contains unit tests for the functions in the read_dump.py file. It tests functions such as log_dump, get_file_info, check_file_date, and read_file.

To run these tests, use the following command:
```bash
python -m unittest dump/claims/read_dump_test.py
```

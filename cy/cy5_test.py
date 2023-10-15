import unittest
from cy5 import login, encode_arabic, ec_de_code, print_test2, printt, printo, findflag, fix_label, make_temp_lines, mainwithcat2

class TestCy5(unittest.TestCase):

    def test_encode_arabic(self):
        self.assertEqual(encode_arabic("مرحبا"), "%D9%85%D8%B1%D8%AD%D8%A8%D8%A7")

    def test_ec_de_code(self):
        self.assertEqual(ec_de_code("%D9%85%D8%B1%D8%AD%D8%A8%D8%A7", 'decode'), "مرحبا")
        self.assertEqual(ec_de_code("مرحبا", 'encode'), "%D9%85%D8%B1%D8%AD%D8%A8%D8%A7")

    def test_findflag(self):
        self.assertEqual(findflag("جيرو ديل ترينتينو", ""), "{{رمز علم|إيطاليا}}")

    def test_fix_label(self):
        self.assertEqual(fix_label("بطولة العالم لسباق الدراجات على الطريق 1966 – سباق الطريق الفردي للرجال"), "سباق الطريق للرجال في بطولة العالم 1966")

    def test_make_temp_lines(self):
        table = {"qid": "Q1", "race": "race1", "p17": "p17_1", "poss": "poss1", "Date": ["2022-01-01T00:00:00Z"], "imagejersey": ["image1"], "item": ["Q1"], "rank": ["rank1"]}
        title = "title1"
        expected_output = "{{نتيجة سباق الدراجات/سطر4\n|qid = Q1\n|السباق = race1\n|البلد = p17_1\n|التاريخ = 2022-01-01T00:00:00Z\n|المركز = poss1\n|المرتبة = rank1\n|جيرسي = image1\n}}"
        self.assertEqual(make_temp_lines(table, title), (expected_output, {"qid": "Q1", "race": "race1", "p17": "p17_1", "poss": "poss1"}))

if __name__ == '__main__':
    unittest.main()

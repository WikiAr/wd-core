import unittest
from cy.cy5 import encode_arabic, ec_de_code, findflag, fix_label, make_temp_lines

class TestCy5(unittest.TestCase):

    def test_encode_arabic(self):
        self.assertEqual(encode_arabic('ب'), '%D8%A8')

    def test_ec_de_code(self):
        self.assertEqual(ec_de_code('%D8%A8', 'decode'), 'ب')
        self.assertEqual(ec_de_code('ب', 'encode'), '%D8%A8')

    def test_findflag(self):
        self.assertEqual(findflag('جيرو ديل ترينتينو', ''), '{{رمز علم|إيطاليا}}')

    def test_fix_label(self):
        self.assertEqual(fix_label('بطولة العالم لسباق الدراجات على الطريق 1966 – سباق الطريق الفردي للرجال'), 'سباق الطريق للرجال في بطولة العالم 1966')

    def test_make_temp_lines(self):
        table = {'imagejersey': 'test'}
        title = 'test_title'
        self.assertEqual(make_temp_lines(table, title), ('', {'qid': '', 'race': '', 'p17': '', 'poss': ''}))

if __name__ == '__main__':
    unittest.main()

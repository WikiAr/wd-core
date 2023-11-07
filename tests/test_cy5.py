import unittest
from unittest.mock import patch
from cy import cy5

class TestCy5(unittest.TestCase):

    def test_extract_first_part_with_pattern(self):
        text = "{{نتيجة سباق الدراجات/بداية some text}}"
        expected_text2 = "{{نتيجة سباق الدراجات/بداية some text}}"
        expected_firs_part = "{{نتيجة سباق الدراجات/بداية some text}}"
        self.assertEqual(cy5.extract_first_part(text), (expected_text2, expected_firs_part))

    def test_extract_first_part_without_pattern(self):
        text = "some text without pattern"
        expected_text2 = "some text without pattern"
        expected_firs_part = ""
        self.assertEqual(cy5.extract_first_part(text), (expected_text2, expected_firs_part))

    def test_create_form(self):
        new_text = "new text"
        main_title = "main title"
        expected_form = "<form id='editform' name='editform' method='POST' action='https://ar.wikipedia.org/w/index.php?title=main%20title&action=submit'><textarea id='wikitext-new' class='form-control' name='wpTextbox1'>new text</textarea><input type='hidden' name='wpSummary' value='تحديث نتائج اللاعب'/><input id='btn-saveandreturn' type='submit' class='btn' name='wpDiff' value='Save &amp; Return' title='Open the edit interface in a new tab/window, then quietly return to the main page.'/><input id='wpPreview' type='submit' class='btn-lg' tabindex='5' title='[p]' accesskey='p' name='wpPreview' value='Preview changes'/><input id='wpDiff' type='submit' class='btn-lg' tabindex='7' name='wpDiff' value='show changes' accesskey='v' title='show changes.'/></form>"
        self.assertEqual(cy5.create_form(new_text, main_title), expected_form)

    @patch('requests.Session.post')
    def test_update_page(self, mock_post):
        new_text = "new text"
        summ = "summary"
        main_title = "main title"
        cy5.update_page(new_text, summ, main_title)
        mock_post.assert_called_once_with(
            'https://ar.wikipedia.org/w/api.php',
            data={
                "action": "edit",
                "format": "json",
                "title": "main title",
                "text": "new text",
                "summary": "summary",
                "bot": 1,
                "nocreate": 1,
                "token": cy5.session["csrftoken"],
            },
        )

if __name__ == '__main__':
    unittest.main()

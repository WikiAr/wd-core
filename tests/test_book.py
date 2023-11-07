import unittest
from unittest.mock import MagicMock
from des import book

class TestBook(unittest.TestCase):

    def test_create_query(self):
        keys = ['en', 'fr', 'de']
        lang = 'en'
        expected_query = 'SELECT ?item (GROUP_CONCAT(DISTINCT(?authen); separator=", ") as ?en) \n(GROUP_CONCAT(DISTINCT(?authfr); separator=" et ") as ?fr) \n(GROUP_CONCAT(DISTINCT(?authde); separator=" und ") as ?de) WHERE {?item wdt:P50 ?auths .\n?item wdt:P31 wd:Qid .\nOPTIONAL {?auths rdfs:label ?authfr filter (lang(?authfr) = "fr")} .\nOPTIONAL {?auths rdfs:label ?authde filter (lang(?authde) = "de")} .\n ?auths rdfs:label ?authen filter (lang(?authen) = "en") .\nOPTIONAL {?item schema:description ?itemDes filter(lang(?itemDes) = "en")}FILTER(!BOUND(?itemDes))  }\n GROUP BY ?item '
        self.assertEqual(book.create_query(keys, lang), expected_query)

    def test_process_results(self):
        json_results = {
            'results': {
                'bindings': [
                    {
                        'item': {'value': 'http://www.wikidata.org/entity/Q1'},
                        'en': {'value': 'Universe'},
                        'fr': {'value': 'Univers'},
                        'de': {'value': 'Universum'}
                    },
                    {
                        'item': {'value': 'http://www.wikidata.org/entity/Q2'},
                        'en': {'value': 'Earth'},
                        'fr': {'value': 'Terre'},
                        'de': {'value': 'Erde'}
                    }
                ]
            }
        }
        expected_table = {
            'Q1': {'item': 'Q1', 'en': 'Universe', 'fr': 'Univers', 'de': 'Universum'},
            'Q2': {'item': 'Q2', 'en': 'Earth', 'fr': 'Terre', 'de': 'Erde'}
        }
        self.assertEqual(book.process_results(json_results), expected_table)

if __name__ == '__main__':
    unittest.main()

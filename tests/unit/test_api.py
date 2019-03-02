from pyleo.api import LeoApi
from urllib import parse
import unittest
import json


class TestApi(unittest.TestCase):
    fake_email = 'test@email.test'
    fake_password = 'change_me'

    _test_instance = LeoApi(fake_email, fake_password)

    def test_construct_url(self):
        word = parse.quote_plus('Touch me')
        query_string = 'getTranslations?word_value='

        expected = 'https://lingualeo.com/userdict3/getTranslations?word_value=Touch+me'
        result = self._test_instance.construct_url(query_string, word)
        self.assertEqual(expected, result)

    def test_construct_url_with_none_word(self):
        word = None
        query_string = 'getTranslations'

        expected = 'https://lingualeo.com/userdict3/getTranslations'
        result = self._test_instance.construct_url(query_string, word)
        self.assertEqual(expected, result)

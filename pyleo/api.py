from http.cookiejar import CookieJar
from pyleo.abstractions import leoapi
from urllib import parse
import urllib
import json


class LeoApi(leoapi.LA):
    base_url = 'https://lingualeo.com/userdict3/'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cj = CookieJar()

    @classmethod
    def construct_url(cls, url, query):
        try:
            return cls.base_url + url + query
        except TypeError as e:
            return cls.base_url + url

    def auth(self):
        query_string = 'login'
        process_url = LeoApi.construct_url(query_string, '')
        values = {
            'email': self.email,
            'password': self.password
        }

        return self.get_data(process_url, values)

    def add_word(self, word, word_translation):
        pass

    def get_translations(self, word):
        word_to_translate = parse.quote_plus(word)
        query_string = 'getTranslations?word_value='
        process_url = LeoApi.construct_url(query_string, word_to_translate)

        try:
            ...
        except Exception as e:
            return e

    def get_data(self, url, values):
        ...


if __name__ == '__main__':
    fake_email = 'test@email.test'
    fake_password = 'change_me'

    _instance = LeoApi(fake_email, fake_password)

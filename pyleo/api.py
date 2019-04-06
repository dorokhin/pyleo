from pyleo.abstractions import leoapi
from pyleo.exceptions.arg_error import LocaleError
from pyleo.utils import get_or_create_node
from http.cookiejar import MozillaCookieJar
from http.cookiejar import LoadError
from urllib import request, error
from urllib import parse
import logging
import time
import json


class LeoApi(leoapi.LA):
    base_url = 'https://lingualeo.com/'

    def __init__(self, email, password, locale='ru'):
        """
        :param email:
        :param password:
        :param locale: (Portuguese: pt | Russian: ru | Turkish: tr | Spanish: es | Spanish Latin America: es_LA)
        """
        self.logger = logging.getLogger('leoapi')
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(get_or_create_node('pyleo.log'))
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        self.logger.addHandler(fh)
        self.logger.debug('Creating an instance of LeoApi class')

        self.email = email
        self.password = password
        if locale in ['pt', 'ru', 'tr', 'es', 'es_LA']:
            self.locale = locale
        else:
            raise LocaleError
        self.cj = MozillaCookieJar()
        self.cookie_file_name = get_or_create_node()
        self.need_auth = 1
        try:
            self.cj.load(self.cookie_file_name)
            self.need_auth = 0
            self.logger.debug('Auth: no auth needed')
        except LoadError as e:
            pass
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36'
                          '(KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }

    @classmethod
    def construct_url(cls, url, query):
        try:
            return cls.base_url + url + query
        except TypeError as e:
            return cls.base_url + url

    def auth(self):
        query_string = 'ru/uauth/dispatch'
        process_url = LeoApi.construct_url(query_string, '')
        referer = 'https://lingualeo.com/ru'
        values = {
            'email': self.email,
            'password': self.password,
            'type': 'login',
            'source': 'landing',
        }
        self.logger.debug('Auth user: {0}'.format(self.email))
        return self.get_data(process_url, values, referer)

    def get_word_(self, word_value):
        """
        Method: GET
        :param word_value:
        :return:
        """
        payload = {
            'word_value': word_value,
            'groupId': 'dictionary',
            '_': int(time.time() * 1000),

        }

        try:
            query_string = parse.urlencode(payload, quote_via=parse.quote_plus)
        except TypeError:
            """
            Python 3.4.9 
            https://docs.python.org/3.4/library/urllib.parse.html#urllib.parse.urlencode
            In this version quote_via keyword argument is absent.
            
            The resulting string is a series of key=value pairs separated by '&' characters, 
            where both key and value are quoted using quote_plus() above.
            """
            query_string = parse.urlencode(payload)

        url_string = 'userdict3/getWord?'
        process_url = LeoApi.construct_url(url_string, query_string)
        referer = 'https://lingualeo.com/{locale}/glossary/learn/dictionary'.format(locale=self.locale)
        self.logger.debug('Get word from LinguaLeo: {0}'.format(word_value))
        return self.get_data(process_url, referer=referer)

    def add_word(self, user_word_value, translate_value):
        """
        Method: POST
        :param user_word_value:
        :param translate_value:
        :return:
        """
        word_id = json.loads(self.get_word_(user_word_value).decode('utf-8'))['userdict3']['word_id']
        values = {
            'word_id': word_id,
            'speech_part_id': '0',
            'groupId': 'dictionary',
            'translate_id': '',
            'translate_value': translate_value,
            'user_word_value': user_word_value,
            'from_syntrans_id': '',
            'to_syntrans_id': '',
        }
        url_string = 'userdict3/addWord'
        process_url = LeoApi.construct_url(url_string, '')
        referer = 'https://lingualeo.com/{locale}/glossary/learn/dictionary'.format(locale=self.locale)
        self.logger.debug('Add word to user dictionary: {0}'.format(user_word_value))
        return self.get_data(process_url, values, referer)

    def get_translations(self, word):
        word_to_translate = parse.quote_plus(word)
        query_string = 'userdict3/getTranslations?word_value='
        process_url = LeoApi.construct_url(query_string, word_to_translate)
        referer = 'https://lingualeo.com/ru/glossary/learn/dictionary'
        self.logger.debug('Get translation: {0}'.format(word))
        return self.get_data(process_url, referer=referer)

    def get_data(self, url, values=None, referer=None, proxy=None, retry_count=3):
        if url is None:
            return None
        if values:
            data = parse.urlencode(values).encode("utf-8")
        else:
            data = None

        try:
            self.logger.debug('Request URL: {0}'.format(url))
            req = request.Request(url, headers=self.headers, data=data)
            if referer:
                req.add_header('Referer', referer)
            cookie = self.cj
            cookie_process = request.HTTPCookieProcessor(cookie)
            opener = request.build_opener(cookie_process)
            if proxy:
                proxies = {parse.urlparse(url).scheme: proxy}
                opener.add_handler(request.ProxyHandler(proxies))
            content = opener.open(req).read()
            self.cj.save(self.cookie_file_name, ignore_discard=True, ignore_expires=True)
        except error.URLError as e:
            self.logger.debug('Error: {0}'.format(e))
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    return self.get_data(url, data, referer, proxy, retry_count-1,)
        self.logger.debug('Request URL success: {0}'.format(url))
        return content

from pyleo.abstractions import leoapi
from pyleo.exceptions.arg_error import LocaleError
from pyleo.utils import create_node
from http.cookiejar import MozillaCookieJar
from http.cookiejar import LoadError
from urllib import request, error
from urllib import parse
import logging


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
        fh = logging.FileHandler(create_node('pyleo.log'))
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
        self.cookie_file_name = create_node()
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

    def add_word(self, word, word_translation):
        pass

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

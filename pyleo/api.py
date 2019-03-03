from pyleo.abstractions import leoapi
from pyleo.utils import create_node
from http.cookiejar import MozillaCookieJar
from http.cookiejar import LoadError
from urllib import request, error
from urllib import parse


class LeoApi(leoapi.LA):
    base_url = 'https://lingualeo.com/'

    def __init__(self, email, password):
        self.email = email
        self.password = password
        self.cj = MozillaCookieJar()
        self.cookie_file_name = create_node()
        self.need_auth = 1
        try:
            self.cj.load(self.cookie_file_name)
            self.need_auth = 0
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

        return self.get_data(process_url, values, referer)

    def add_word(self, word, word_translation):
        pass

    def get_translations(self, word):
        word_to_translate = parse.quote_plus(word)
        query_string = 'userdict3/getTranslations?word_value='
        process_url = LeoApi.construct_url(query_string, word_to_translate)
        referer = 'https://lingualeo.com/ru/glossary/learn/dictionary'

        return self.get_data(process_url, referer=referer)

    def get_data(self, url, values=None, referer=None, proxy=None, retry_count=3):
        if url is None:
            return None
        if values:
            data = parse.urlencode(values).encode("utf-8")
        else:
            data = None

        try:
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
            print('error:', e.reason)
            content = None
            if retry_count > 0:
                if hasattr(e, 'code') and 500 <= e.code < 600:
                    return self.get_data(url, data, referer, proxy, retry_count-1,)
        return content

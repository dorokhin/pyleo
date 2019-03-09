from abc import ABC, abstractmethod


class LA(ABC):
    @classmethod
    @abstractmethod
    def construct_url(cls, url, query):
        raise NotImplementedError

    @abstractmethod
    def auth(self):
        raise NotImplementedError

    @abstractmethod
    def add_word(self, user_word_value, translate_value):
        raise NotImplementedError

    @abstractmethod
    def get_translations(self, word):
        raise NotImplementedError

    @abstractmethod
    def get_data(self, url, values):
        raise NotImplementedError

from pyleo.exceptions import PyLeoError


class LocaleError(PyLeoError):
    def __str__(self):
        return 'Wrong locale, allowed locale are: pt, ru, tr, es, es_LA'

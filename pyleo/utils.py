import os
from time import time, sleep


def get_or_create_node(_file_name='cookies.txt', _path='.pyleo'):
    _file_path = os.path.join(os.path.expanduser("~"), _path)

    if not os.path.exists(os.path.join(_file_path, _file_name)):
        try:
            os.makedirs(_file_path)
        except FileExistsError as e:
            pass
        os.mknod(os.path.join(_file_path, _file_name))
    return os.path.join(_file_path, _file_name)


class TokenBucket(object):
    def __init__(self, tokens, fill_rate):
        self.capacity = float(tokens)
        self._tokens = float(tokens)
        self.fill_rate = float(fill_rate)
        self.timestamp = time()

    def consume(self, tokens):
        if tokens > self.tokens:
            deficit = tokens - self._tokens
            delay = deficit / self.fill_rate
            sleep(delay)

        else:
            self._tokens -= tokens
            return True

    def get_tokens(self):
        now = time()
        if self._tokens < self.capacity:
            delta = self.fill_rate * (now - self.timestamp)
            self._tokens = min(self.capacity, self._tokens + delta)
        self.timestamp = now
        return int(self._tokens)

    tokens = property(get_tokens)

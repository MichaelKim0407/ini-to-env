__version__ = '1.0dev0'

import os as _os
from configparser import (
    ConfigParser as _ConfigParser,
)


class Loader(object):
    def __init__(self):
        self.conf = _ConfigParser()
        self.conf.optionxform = str  # preserve case

    def add_file(self, filename):
        with open(filename):  # raise FileNotFoundError
            pass
        self.conf.read(filename)

    def __iter__(self):
        for section in self.conf:
            yield from self.conf[section].items()

    def load(self, target=None):
        if target is None:
            target = _os.environ
        for k, v in self:
            target.setdefault(k, v)


def load(filename):
    loader = Loader()
    loader.add_file(filename)
    loader.load()

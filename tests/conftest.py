import os

import pytest


@pytest.fixture
def patch_env(monkeypatch):
    monkeypatch.setattr(os, 'environ', {})


@pytest.fixture
def ini_file_name():
    dirname = os.path.dirname(__file__)

    def result(name=None):
        if name is None:
            name = 'conf.ini'
        return os.path.join(dirname, name)

    return result

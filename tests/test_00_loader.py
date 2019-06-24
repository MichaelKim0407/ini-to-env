import os

import pytest

from ini2env import Loader


def test_iter(ini_file_name):
    loader = Loader()
    loader.add_files(ini_file_name())
    assert dict(loader) == {
        'HELLO': 'WORLD',
        'HOST': 'localhost',
        'PORT': '8000',
    }


def test_file_not_found(ini_file_name):
    loader = Loader()
    with pytest.raises(FileNotFoundError):
        loader.add_files(ini_file_name('xyz'))


def test_load(ini_file_name, patch_env):
    loader = Loader()
    loader.add_files(ini_file_name())
    loader.load()
    assert os.environ['HELLO'] == 'WORLD'
    assert os.environ['HOST'] == 'localhost'
    assert os.environ['PORT'] == '8000'


def test_target(ini_file_name, patch_env):
    envs = {}
    loader = Loader()
    loader.add_files(ini_file_name())
    loader.load(target=envs)
    assert envs['HELLO'] == 'WORLD'
    assert envs['HOST'] == 'localhost'
    assert envs['PORT'] == '8000'
    assert 'HELLO' not in os.environ


def test_multiple_files(ini_file_name):
    loader = Loader()
    loader.add_files(
        ini_file_name(),
        ini_file_name('conf2.ini'),
    )
    assert dict(loader) == {
        'HELLO': 'WORLD',
        'HOST': 'localhost',
        'PORT': '8000',
        'DB_HOST': 'localhost',
        'DB_PORT': '5432',
        'DB_NAME': 'test',
        'DB_USER': 'testuser',
        'DB_PASSWORD': 'testtesttest',
    }

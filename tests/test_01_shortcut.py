import os

from ini2env import load


def test_load_func(ini_file_name, patch_env):
    load(ini_file_name())
    assert os.environ['HELLO'] == 'WORLD'
    assert os.environ['HOST'] == 'localhost'
    assert os.environ['PORT'] == '8000'

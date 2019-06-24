import sys

from ini2env import cmd


def test_cmd_direct(ini_file_name, capsys, monkeypatch):
    monkeypatch.setattr(sys.stdout, 'isatty', lambda: True)
    cmd([ini_file_name()])
    captured = capsys.readouterr()
    assert captured.err == '''\
# source this output to export environment variables
'''
    assert captured.out.splitlines() == [
        'export HELLO=WORLD',
        'export HOST=localhost',
        'export PORT=8000',
    ]


def test_cmd_source(ini_file_name, capsys):
    cmd([ini_file_name()])
    captured = capsys.readouterr()
    assert captured.err == ''
    assert captured.out.splitlines() == [
        'export HELLO=WORLD',
        'export HOST=localhost',
        'export PORT=8000',
    ]

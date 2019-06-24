from setuptools import setup

from ini2env import __version__

extra_test = [
    'pytest>=4',
    'pytest-cov>=2',
]
extra_dev = [
    *extra_test,
]

setup(
    name='ini-to-env',
    version=__version__,
    description='Load environment variables from ini file.',

    url='https://github.com/MichaelKim0407/ini-to-env',
    author='Michael Kim',
    author_email='mkim0407@gmail.com',

    py_modules=['ini2env'],

    extras_require={
        'test': extra_test,
        'dev': extra_dev,
    },

    entry_points={
        'console_scripts': [
            'ini2env=ini2env:cmd',
        ],
    },

    classifiers=[
        'Intended Audience :: Developers',

        'Development Status :: 5 - Production/Stable',

        'Programming Language :: Python',
        'Programming Language :: Python :: 3',

        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)

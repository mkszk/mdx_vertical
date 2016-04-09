#!/usr/bin/env python

from setuptools import setup
import doctest

MODULE = 'mdx_vertical'

tests = lambda: doctest.DocTestSuite(MODULE)

setup(
    name=MODULE,
    version='1.0',
    author='MKSZK',
    author_email='mks@ulthar.com',
    description='Vertical Text extension for Python-Markdown.',
    long_description_markdown_filename='README.md',
    url='https://github.com/mkszk/' + MODULE,
    py_modules=[MODULE],
    test_suite='setup.tests',
    install_requires=['Markdown'],
    license='The BSD 2-Clause License',
    keywords='markdown vertical',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: The BSD 2-Clause License (BSD)',
        'Environment :: Web Environment',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup :: HTML'
    ]
)

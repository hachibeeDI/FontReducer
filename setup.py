# -*- coding: utf-8 -*-
from __future__ import (print_function, division, absolute_import, unicode_literals, )

import os
from setuptools import setup


LICENSE = open(
    os.path.join(os.path.dirname(__file__), 'LICENSE')).read().strip()

DESCRIPTION = open(
    os.path.join(os.path.dirname(__file__), 'README.md')).read().strip()

classifiers = [
    "Development Status :: 4 - Beta",
    "License :: OSI Approved :: Apache Software License",
    "Programming Language :: Python",
    "Topic :: Utilities",
]

setup(
    name='FontReducer',
    version='0.0.1',
    description='Generate font subsets',
    author='OGURA_Daiki',
    author_email='8hachibee125@gmail.com',
    url='https://github.com/hachibeeDI/FontReducer',
    py_modules=['fontreducer', ],
    scripts=["bin/fontreduce", ],
    keywords=['fontforge', ],
    classifiers=classifiers,
    install_requires=['', ],
    license=LICENSE,
    long_description=DESCRIPTION,
    test_suite='')

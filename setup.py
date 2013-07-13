#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#------
# Used http://www.python.org/dev/peps/pep-0314/ and
# http://getpython3.com/diveintopython3/packaging.html
#
# to wrote this script
#------------------------

"""
    Duty: Make random duty in LaTeX
    Copyright (C) 2013 Julien Freyermuth
    All Rights Reserved
    This file is part of Duty.

    See the file LICENSE for copying permission.
"""

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

import Duty

###########
# À refaire
###########

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Console',
    'Intended Audience :: Education',
    'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    'Natural Language :: English',
    'Operating System :: POSIX',
    'Operating System :: POSIX :: Linux',
    'Programming Language :: Python :: 3.3',
    'Topic :: Office :: LaTeX',
]

SCRIPTS = ['duty', ]

setup(
        name             = Duty.__name__,
        version          = Duty.__version__,
        description      = Duty.__description__,
        long_description = Duty.__long_description__,
        author           = Duty.__author__,
        author_email     = Duty.__author_email__,
        url              = Duty.__url__,
        license          = Duty.__license__,
        platforms        = Duty.__platforms__,
        packages         = find_packages(),
        include_package_data = True,
        scripts          = SCRIPTS,
        requires         = ['python (>=3.3)'],
        classifiers      = CLASSIFIERS,
)

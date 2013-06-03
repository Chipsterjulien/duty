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

import sys
try:
	from setuptools import setup, Command
except ImportError:
	from distutils.core import setup, Command

from duty import *

CLASSIFIERS = [
								'License :: OSI Approved :: GNU General Public License (GPLv3)',
								'Programming Language :: Python',
								'Programming Language :: Python :: 3'
								'Intended Audience :: End Users/Desktop',
								'Operating System :: GNU/Linux',
								'Development Status :: 5 - Production/Stable',
								'Topic :: Office :: LaTeX',
								'Natural Language :: English',
							]

PACKAGES      = [ 'duty', ]

SCRIPTS       = ['duty/duty',]

setup(
	name             = NAME,
	version          = VERSION,
	description      = DESCRIPTION,
	long_description = LONG_DESCRIPTION,
	author           = AUTHOR,
	author_email     = AUTHOR_EMAIL,
	url              = URL,
	license          = LICENSE,
	platforms        = PLATFORMS,
	packages         = PACKAGES,
	scripts          = SCRIPTS,
	requires         = ['TexLive', 'python (>=3.3)'],
	classifiers      = CLASSIFIERS
)

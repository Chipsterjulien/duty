# -*- coding: utf-8 -*-


######################################################################
# Copyright (C) 2013 Julien Freyermuth
# All Rights Reserved
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
######################################################################


__author__           = "Julien Freyermuth"
__author_email__     = "julien [dote] chipster [hate] gmail [dote] com"
__copyright__        = "Copyright (c) 2013, Julien Freyermuth"
__description__      = "Make random duty in LaTeX"
__long_description__ = "It is a program that allows you to generate questions / homework LaTeX randomly. You can choose either a period or a number of exercises"
__license__          = "GPLv3"
__name__             = "duty"
__platforms__        = "GNU/Linux"
__url__              = "https://github.com/Chipsterjulien/duty"
__version__          = '0.2.1'
__version_info__     = (0, 2, 1, '', 0)


from .begin import beginning
from .duty_with_number import duty_number
from .duty_with_time import duty_time
from .is_a_number import is_int, is_float
from .mylog import *

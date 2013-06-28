# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Duty.

See the file LICENSE for copying permission.
"""

def is_int(n):
    """
    Return True if parameter is an integer otherwise it return False
    """

    try:
        int(n)
        return True

    except ValueError:
        return False


def is_float(n):
    """
    Return True if parameter is a float otherwise it return False
    """

    try:
        float(n)
        return True

    except ValueError:
        return False

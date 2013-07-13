# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Duty.

See the file LICENSE for copying permission.
"""

import os
import datetime
import glob
import sys
import random

from Duty.is_a_number import is_float
from Duty.mylog import logger


def duty_time(t, hash_file):
    """
    This function create a PDF file with a number of exercises that depend of
    the time to solve them
    """

    # Verify that the total time is greater than t
    timer_sum = 0
    for f in hash_file.keys():
        with open(f, 'r') as r:
            var = r.readline().split(' ')
            if len(var) < 2:
                logger.warning("In the \"{0}\" file is not formated  \
                correctly ! You should have at the first line a time as  \
                \"% 10\" where 10 represents the number of minutes".format(f))
                sys.exit(1)

            var = var[1].strip()
            print(var)
            if not is_float(var):
                logger.warning("In the \"{0}\" file, {1} is not a number  \
                    !".format(f, var))
                sys.exit(1)

            timer_sum += float(var)

    if t > timer_sum:
        logger.warning("You want {0} minute{1} but you have only {2} with  \
            all exercises!".format(t, "s" if t > 1 else "", timer_sum))
        sys.exit(0)

    # Check rights access to write
    if not os.access(os.getcwd(), os.W_OK):
        logger.warning("You have not the right to create directory !")
        sys.exit(1)

    os.makedirs("PDF", exist_ok=True)
    timer = 0
    now = datetime.datetime.now()
    name_d = "PDF/" + now.strftime("%d-%m-%Y_%H:%M.tex")
    name_r = "PDF/" + now.strftime("%d-%m-%Y_%H:%M_reply.tex")
    target_d = open(name_d, 'w')
    target_r = open(name_r, 'w')

    # Copy headers in exercises and answer files
    with open('header.tex', 'r') as d:
        target_d.write(d.read())

    with open('header_reply.tex', 'r') as r:
        target_r.write(r.read())

    keys = list(hash_file.keys())

    while timer < t:
        i = random.randint(0, len(keys) - 1)

        # Write exercise
        with open(keys[i], 'r') as d:
            # On ajoute le temps au temps total en récupérant la première ligne
            timer += float(d.readline().split('%')[1].strip())
            target_d.write(d.read())

        # Write answer
        with open(hash_file[keys[i]], 'r') as r:
            target_r.write(r.read())

        # Delete the file from the list
        del(keys[i])

    # Copy end of file in the exercises files
    with open('end.tex', 'r') as d:
        target_d.write(d.read())

    # Copy end of file in the answer files
    with open('end_reply.tex', 'r') as r:
        target_r.write(r.read())

    target_d.close()
    target_r.close()

    os.chdir('PDF')

    # Compile 2 times the .tex file
    for i in range(2):
        os.system("pdflatex {0}".format(name_d.split('/')[1]))
        os.system("pdflatex {0}".format(name_r.split('/')[1]))

    # Delete unnecessary files related of compiling
    list_files = glob.glob('*')
    for f in list_files:
        name, ext = os.path.splitext(f)
        if ext == '.aux' or ext == '.log' or ext == '.toc':
            os.remove(f)

# -*- coding: utf-8 -*-

"""
Copyright (C) 2013 Julien Freyermuth
All Rights Reserved
This file is part of Duty.

See the file LICENSE for copying permission.
"""

import datetime
import os
import glob
import random
import sys


def duty_number(n, hash_file):
    """
    This function cover the choise -n where n is the number of exercises.
    It create .pdf file with n exercise(s)
    """

    # Verify that they are enough exercises relative of demand
    if len(hash_file) < n:
        print("You want {0} exercice{1} but there are only {2} file{3} \
            !".format(n, "s" if n > 1 else "", len(hash_file),
            "s" if len(hash_file) > 1 else ""))
        sys.exit(2)

    # Test right of current directory
    if not os.access(os.getcwd(), os.W_OK):
        print("You have not the right to create directory !")
        sys.exit(2)

    os.makedirs("PDF", exist_ok=True)
    counter = 0
    now = datetime.datetime.now()
    name_d = "PDF/" + now.strftime("%d-%m-%Y_%H:%M.tex")
    name_r = "PDF/" + now.strftime("%d-%m-%Y_%H:%M_reply.tex")
    target_d = open(name_d, 'w')
    target_r = open(name_r, 'w')

    # Copy the headers in exercise and answer files
    with open('header.tex', 'r') as d:
        target_d.write(d.read())

    with open('header_reply.tex', 'r') as r:
        target_r.write(r.read())

    keys = list(hash_file.keys())

    while counter < n:
        i = random.randint(0, len(keys) - 1)

        # Write exercise
        with open(keys[i], 'r') as d:
            target_d.write(d.read())

        # Write answer
        with open(hash_file[keys[i]], 'r') as r:
            target_r.write(r.read())

        # Delete file from the list
        del(keys[i])

        counter += 1

    # Copy the end in the exercise file
    with open('end.tex', 'r') as d:
        target_d.write(d.read())

    # Copy the end in the answer file
    with open('end_reply.tex', 'r') as r:
        target_r.write(r.read())

    # Close files
    target_d.close()
    target_r.close()

    os.chdir('PDF')

    # Compile 2 times exercise file
    for i in range(2):
        os.system("pdflatex %s" % (name_d.split('/')[1]))

    # Compile 2 times answer file
    for i in range(2):
        os.system("pdflatex %s" % (name_r.split('/')[1]))

    # Delete inutils files related to the LaTeX compilation
    list_files = glob.glob('*')
    for f in list_files:
        name, ext = os.path.splitext(f)
        if ext == '.aux' or ext == '.log' or ext == '.toc':
            os.remove(f)

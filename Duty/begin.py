# -*- coding: utf-8 -*-

import glob
import os
import sys

from Duty.mylog import logging


def beginning():
    """
    Function was called at the begining of script.
    It get all file ".tex" in the current directory, test if file header.tex,
    header_reply.tex, end.tex and end_reply.tex exist.
    Finaly it return an hash of exercice / reply
    """

    # Get all files .tex
    list_of_files = glob.glob("*.tex")

    # Verify that file exists header.tex
    if not "header.tex" in list_of_files:
        logging.warning("File \"header.tex\" not found !")
        sys.exit(2)

    # Verify that file exists header_reply.tex
    if not "header_reply.tex" in list_of_files:
        logging.warning("File \"header_reply.tex\" not found !")
        sys.exit(2)

    # Verify that file exists end.tex
    if not "end.tex" in list_of_files:
        logging.warning("File \"end.tex\" not found !")
        sys.exit(2)

    # Verify that file exists end_reply.tex
    if not "end_reply.tex" in list_of_files:
        logging.warning("File \"end_reply.tex\" not found !")
        sys.exit(2)

    # Delete theses 4 files in list_of_files
    del_list = ['header.tex', 'header_reply.tex', 'end.tex', 'end_reply.tex']
    for f in del_list:
        list_of_files.remove(f)

    # Create 2 lists: 1 for exercises and 1 for answers
    list_of_exercise = []
    list_of_reply = []
    for f in list_of_files:
        if "reply" in f:
            list_of_reply.append(f)
        else:
            list_of_exercise.append(f)

    # Merge the 2 lists in a dictionnary
    hash_file = {}
    for i in range(len(list_of_exercise)):
        name, ext = os.path.splitext(list_of_exercise[i])
        reply = name + "_reply" + ext
        if reply in list_of_reply:
            hash_file[list_of_exercise[i]] = reply
            list_of_reply.remove(reply)
        else:
            logging.warning("\"{0}\" not found !".format(reply))
            sys.exit(2)

    if len(list_of_reply) != 0:
        for f in list_of_reply:
            name, ext = os.path.splitext(f)
            name = name.split("_")[0]
            logging.warning("\"{0}\" not found !".format(name + ext))
        sys.exit(2)

    return hash_file

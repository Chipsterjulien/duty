# -*- coding: utf-8 -*-

import glob, os, sys


def beginning():
	"""
		Function was called at the begining of script.
		It get all file ".tex" in the current directory, test if file header.tex,
		header_reply.tex, end.tex and end_reply.tex exist.
		Finaly it return an hash of exercice / reply
	"""

	# Récupérer la liste de tous les fichiers .tex
	list_of_files = glob.glob("*.tex")

	# On vérifie que le fichier header.tex existe
	if not "header.tex" in list_of_files:
		print("File \"header.tex\" not found !")
		sys.exit(2)

	# On vérifie que le fichier header_reply.tex existe
	if not "header_reply.tex" in list_of_files:
		print("File \"header_reply.tex\" not found !")
		sys.exit(2)

	# On vérifie que le fichier end.tex existe
	if not "end.tex" in list_of_files:
		print("File \"end.tex\" not found !")
		sys.exit(2)

	# On vérifie que le fichier end_reply.tex existe
	if not "end_reply.tex" in list_of_files:
		print("File \"end_reply.tex\" not found !")
		sys.exit(2)

	# On supprime les 4 fichiers de la listes
	list_of_files.remove("header.tex")
	list_of_files.remove("header_reply.tex")
	list_of_files.remove("end.tex")
	list_of_files.remove("end_reply.tex")

	# On fait 2 listes: 1 pour les exercices, l'autres pour les réponses
	list_of_exercise = []
	list_of_reply     = []
	for f in list_of_files:
		if "reply" in f:
			list_of_reply.append(f)
		else:
			list_of_exercise.append(f)

	hash_file = {}
	for i in range(len(list_of_exercise)):
		name, ext = os.path.splitext(list_of_exercise[i])
		reply = name + "_reply" + ext
		if reply in list_of_reply:
			hash_file[list_of_exercise[i]] = reply
			list_of_reply.remove(reply)
		else:
			print("\"%s\" not found !" %(reply))
			sys.exit(2)

	if len(list_of_reply) != 0:
		for f in list_of_reply:
			name, ext = os.path.splitext(f)
			name = name.split("_")[0]
			print("\"%s\" not found !" %(name + ext))
		sys.exit(2)

	return hash_file


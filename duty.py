#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys, glob, time

# Le programme prend le temps de l'interrogation (par défaut 1h / 60 minutes)
# Dans l'entête des questions, il devra y avoir le temps passé pour la question
# Prévoir l'entête de fichier (header)
# Prévoir la fin de fichier (end of file)
# Prévoir la correction
# Prévoir des tranches de temps pour prendre en premier les exercices les plus long
# Une fois le devoir prêt, faire un random pour obtenir l'ordre des exercices
# Générer le fichier avec une date
# Mettre un barème pour chaque exercice



if __name__ == "__main__":
	if len(sys.argv) < 2:
		print("You must give time in argument : %s 60\n - 60 is the time in minutes" %(sys.argv[0]))
		sys.exit(0)

	# Je récupère le temps de l'interrogation
	all_time = sys.argv[1]

# On récupère la liste des fichiers
	file_list = glob.glob('*.tex')

	# On vérifie qu'un fichier header.tex existe
	if not ("header.tex" in file_list):
		print("File header.tex not found !")
		sys.exit(2)

	# Pareil pour end_of_file.tex
	if not ("end_of_file.tex" in file_list):
		print("File end_of_file.tex not found !")
		sys.exit(2)

#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys, glob, datetime, os, getopt, shutil




VERSION = "0.1"




def beginning():
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




def duty_number(n, hash_file):
	# Vérifier qu'il y a assez d'exercices par rapport à la demande
	if len(hash_file) < n:
		print("You want %i exercice%s but there are only %i file%s !" %(n, "s" if n > 1 else "", len(hash_file), "s" if len(hash_file) > 1 else ""))
		sys.exit(2)

	if not os.access(os.getcwd(), os.W_OK):
		print("You have not the right to create directory !")
		sys.exit(2)

	os.makedirs("PDF", exist_ok=True)
	counter  = 0
	now      = datetime.datetime.now()
	name_d   = now.strftime("%d-%m-%Y_%H:%M.tex")
	name_r   = now.strftime("%d-%m-%Y_%H:%M_reply.tex")
	target_d = open(name_d, 'w')
	target_r = open(name_r, 'w')

	# On copie l'entête dans les exercices et les réponses
	with open('header.tex', 'r') as d:
		target_d.write(d.read())

	with open('header_reply.tex', 'r') as r:
		target_r.write(r.read())

	keys = list(hash_file.keys())

	while counter < n:
		i = random.randint(0, len(keys) - 1)

		# Écrire l'exercice
		with open(keys[i], 'r') as d:
			target_d.write(d.read())

		# Écrire la correction
		with open(hash_file[keys[i]], 'r') as r:
			target_r.write(r.read())

		# Supprimer le fichierde la liste
		del(keys[i])

		# Ajouter 1 au compteur
		counter += 1

	# Copier la fin de fichier dans les exercices
	with open('end.tex', 'r') as d:
		target_d.write(d.read())

	# Copier la fin de fichier dans les réponses
	with open('end_reply.tex', 'r') as r:
		target_r.write(r.read())

	# On ferme les fichiers
	target_d.close()
	target_r.close()

	# Compiler 2x les fichiers .tex
	for i in range(2):
		os.system("pdflatex %s" %(name_d))
		os.system("pdflatex %s" %(name_r))

	# Supprimer les fichiers inutiles liés à la compilation LaTeX
	list_files = glob.glob(*)
	for f in list_files:
		name, ext = os.path.splitext()
		if ext == '.aux' or ext == '.log' or ext == '.toc':
			os.remove(f)

	# Déplacer les fichiers .pdf dans le répertoire PDF
	name_d = os.path.splitext()[0] + '.pdf'
	name_r = os.path.splitext()[0] + '.pdf'
	shutil.move(name_d, 'PDF/')
	shutil.move(name_r, 'PDF/')


def help():
	print("%s %s" %(sys.argv[0], VERSION))
	print("Usage: %s [Options]" %(sys.argv[0]))
	print("  -t <number in minute(s)>: make a duty thats last in x minute(s)")
	print("  -n <number of exercise(s): make a duty with x exercise(s)")
	print("EXAMPLE:")
	print("  %s -t 60" %(sys.argv[0]))




def is_number(n):
	try:
		int(a)
		return True

	except ValueError:
		return False




if __name__ == "__main__":
	if len(sys.argv) < 2:
		help()
		sys.exit(2)

	try:
		opts, args = getopt.getopt(sys.argv[1:], "hn:t:v")
	except getopt.GetoptError as err:
		print(err)
		sys.exit(2)

	for o, a in opts:
		if o == '-h':
			help()

		# NOMBRE
		elif o == '-n':
			if not is_number(a):
				print("\"%s\"  is not a number !" %(a))
				sys.exit(2)

			a = int(a)
			hash_file = beginning()
			duty_number(a, hash_file)

		# TEMPS
		elif o == '-t':
			if not is_number(a):
				print("\"%s\"  is not a number !" %(a))
				sys.exit(2)

			a = int(a)
			hash_file = beginning()

		elif o == '-v':
			print("%s %s" %(sys.argv[0], VERSION))






#import random, sys, glob, time, os

# Le programme prend le temps de l'interrogation (par défaut 1h / 60 minutes)
# Dans l'entête des questions, il devra y avoir le temps passé pour la question
# Prévoir l'entête de fichier (header)
# Prévoir la fin de fichier (end of file)
# Prévoir la correction
# Prévoir des tranches de temps pour prendre en premier les exercices les plus long
# Une fois le devoir prêt, faire un random pour obtenir l'ordre des exercices
# Générer le fichier avec une date
# Mettre un barème pour chaque exercice


#class Exercise:
#	def __init__(self, name):
#		self.filename = name
#		self.duration = int()


#if __name__ == "__main__":
#	if len(sys.argv) < 2:
#		print("You must give time in argument : %s 60\n - 60 is the time in minutes" %(sys.argv[0]))
#		sys.exit(0)
#
#	# Je récupère le temps de l'interrogation
#	all_time = sys.argv[1]
#
# On récupère la liste des fichiers
#	list_of_exercise = glob.glob('*.tex')
#
#	# On vérifie qu'un fichier header.tex existe
#	if "header.tex" in list_of_exercise:
#		list_of_exercise.remove("header.tex")
#
#	else:
#		print("File header.tex not found !")
#		sys.exit(2)
#
#	# Pareil pour end_of_file.tex
#	if "end_of_file.tex" in list_of_exercise:
#		list_of_exercise.remove("end_of_file.tex")
#
#	else:
#		print("File end_of_file.tex not found !")
#		sys.exit(2)
#
#	# On récupère les fichiers qui servent à la correction
#	list_of_reply = []
#	for f in list_of_exercise:
#		if "_reply" in f:
#			list_of_reply.append(f)
#
#	# On supprime les fichiers inutiles
#	for f in list_of_reply:
#		list_of_exercise.remove(f)
#
#	# On récupère le temps pour chaque exercice sur la première ligne
#	for exercise in list_of_exercise:
#		e = Exercise(exercise)
#		with open(exercise, 'r') as f:
#			line = f.readline()
#			if line == '':
#				print("Exercise \"%s\" don't have the duration at the first line" %(exercise))
#				sys.exit(2)
#
#			else:
#				e.duration = int(line.split(' ')[1])

#	# Création du fichier exercice avec sa correction

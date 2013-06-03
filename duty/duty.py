#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random, sys, glob, datetime, os, getopt
from duty.version import VERSION


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
	name_d   = "PDF/" + now.strftime("%d-%m-%Y_%H:%M.tex")
	name_r   = "PDF/" + now.strftime("%d-%m-%Y_%H:%M_reply.tex")
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

	os.chdir('PDF')

	# Compiler 2x les fichiers .tex
	for i in range(2):
		os.system("pdflatex %s" %(name_d.split('/')[1]))

	for i in range(2):
		os.system("pdflatex %s" %(name_r.split('/')[1]))

	# Supprimer les fichiers inutiles liés à la compilation LaTeX
	list_files = glob.glob('*')
	for f in list_files:
		name, ext = os.path.splitext(f)
		if ext == '.aux' or ext == '.log' or ext == '.toc':
			os.remove(f)




def duty_time(t, hash_file):
	# Vérifier que le temps total est supérieur à t
	timer_sum = 0
	for f in hash_file.keys():
		with open(f, 'r') as r:
			var = r.readline().split(' ')
			if len(var) < 2:
				print("In the \"{0}\" file is not formated correctly ! You should have at the first line a time as \"% 10\" where 10 represents the number of minutes".format(f))
				sys.exit(2)

			var = var[1].strip()
			print(var)
			if not is_float(var):
				print("In the \"%s\" file, %s is not a number !" %(f, var))
				sys.exit(2)

			timer_sum += float(var)

	if t > timer_sum:
		print("You want %d minute%s but you have only %f with all exercises!" %(t, "s" if t > 1 else "", timer_sum))
		sys.exit(0)
		
	# Vérifier qu'on a les droits d'écriture
	if not os.access(os.getcwd(), os.W_OK):
		print("You have not the right to create directory !")
		sys.exit(2)

	os.makedirs("PDF", exist_ok=True)
	timer    = 0
	now      = datetime.datetime.now()
	name_d   = "PDF/" + now.strftime("%d-%m-%Y_%H:%M.tex")
	name_r   = "PDF/" + now.strftime("%d-%m-%Y_%H:%M_reply.tex")
	target_d = open(name_d, 'w')
	target_r = open(name_r, 'w')


	# On copie l'entête dans les exercices et les réponses
	with open('header.tex', 'r') as d:
		target_d.write(d.read())

	with open('header_reply.tex', 'r') as r:
		target_r.write(r.read())

	keys = list(hash_file.keys())

	while timer < t:
		i = random.randint(0, len(keys) - 1)

		# Écrire l'exercice
		with open(keys[i], 'r') as d:
			# On ajoute le temps au temps total en récupérant la première ligne
			timer += float(d.readline().split('%')[1].strip())
			target_d.write(d.read())

		# Écrire la correction
		with open(hash_file[keys[i]], 'r') as r:
			target_r.write(r.read())

		# Supprimer le fichierde la liste
		del(keys[i])

	# Copier la fin de fichier dans les exercices
	with open('end.tex', 'r') as d:
		target_d.write(d.read())

	# Copier la fin de fichier dans les réponses
	with open('end_reply.tex', 'r') as r:
		target_r.write(r.read())

	target_d.close()
	target_r.close()

	os.chdir('PDF')

	# Compiler 2x les fichiers .tex
	for i in range(2):
		os.system("pdflatex %s" %(name_d.split('/')[1]))
		os.system("pdflatex %s" %(name_r.split('/')[1]))

	# Supprimer les fichiers inutiles liés à la compilation LaTeX
	list_files = glob.glob('*')
	for f in list_files:
		name, ext = os.path.splitext(f)
		if ext == '.aux' or ext == '.log' or ext == '.toc':
			os.remove(f)




def help():
	print("%s %s" %(sys.argv[0], VERSION))
	print("Usage: %s [Options]" %(sys.argv[0]))
	print("  -t <number in minute(s)>: make a duty thats last in x minute(s)")
	print("  -n <number of exercise(s): make a duty with x exercise(s)")
	print("EXAMPLE:")
	print("  %s -t 60" %(sys.argv[0]))
	print("ATTENTION:")
	print("You must have \"% a_number\" at the first line of your all files of exercises if you use the \"-t\" option")




def is_int(n):
	try:
		int(n)
		return True

	except ValueError:
		return False




def is_float(n):
	try:
		float(n)
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
			if not is_int(a):
				print("\"%s\"  is not a number !" %(a))
				sys.exit(2)

			a = int(a)
			hash_file = beginning()
			duty_number(a, hash_file)

		# TEMPS
		elif o == '-t':
			if not is_int(a):
				print("\"%s\"  is not a number !" %(a))
				sys.exit(2)

			a = int(a)
			hash_file = beginning()
			duty_time(a, hash_file)

		elif o == '-v':
			print("%s %s" %(sys.argv[0], VERSION))

# -*- coding: utf-8 -*-

import os, datetime, glob


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


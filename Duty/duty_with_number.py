# -*- coding: utf-8 -*-

import datetime, os, glob




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


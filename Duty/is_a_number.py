# -*- coding: utf-8 -*-

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

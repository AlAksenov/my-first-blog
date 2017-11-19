#!/usr/bin/python3
# -*- coding: utf-8 -*-

# casual print (печатает переданные аргументы по 1 в строке)
def cprint(*args):
	for arg in args:
		print(arg)

# dash print (работает как cprint и печатает разделитель с пробелами)
def dprint(*args):
	cprint(*args)
	print( '\n--------------------------------------\n')


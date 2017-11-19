#!/usr/bin/python3
# -*- coding: utf-8 -*-

class Program_info:
	"""Класс содержит основную информацию о программе"""
	def __init__ (  self, name = "Program", 
					version = None, 
					base_aims = [], 
					extra_aims = [], 
					base_rules = [], 
					extra_rules = []):
		self.name = name
		self.version = version
		self.base_aims = base_aims
		self.extra_aims = extra_aims
		self.base_rules = base_rules
		self.extra_rules = extra_rules


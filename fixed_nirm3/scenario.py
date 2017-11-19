#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import xlrd
import uuid


from k_map import Map

class Scenario:
	"""Сценарий содержит множество итераций"""

	"Список сценариев"
	full_list = []

	def __init__(self, k_map, description = None):
		self.uid = uuid.uuid4().hex
		self.k_map = k_map
		self.description = description
		self.full_list.append(self)
		# список итераций
		self.data_list = [] 
		
	"Изменение отображения класса при принте"
	def __str__(self):
		return "Scenario № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Scenario № {}".format(self.uid)

	"Метод добавления итерации в сценарий"
	def add_iteration(self, iteration):
		self.data_list.append(iteration)
		return iteration

	"Метод очистки списка итераций"
	def clear(self):
		self.data_list = []
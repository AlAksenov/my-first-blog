#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import uuid


class Change:
	"""Изменение (веса или значения)"""

	"Полный список изменений"
	full_list = []

	def __init__(self, iteration, description = None):
		self.uid = uuid.uuid4().hex
		self.iteration = iteration
		self.description = description
		self.full_list.append(self)
		
		self.data_dict = {}

	"Изменение отображения класса при принте"
	def __str__(self):
		return "Change № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Change № {}".format(self.uid)

	"Создание изменения вершины"
	def set_node_change(self, name = '', value = None, order = None,  duration = 0):
		self.data_dict = {'node': name, 'value': value, 'order': order, 'duration': duration}
		return self.data_dict

	"Создание изменения ребра"
	def set_link_change(self, source = '', target = '', value = None, order = None,  duration = 0):
		self.data_dict = {'source': source, 'target': target,'value': value, 'order': order, 'duration': duration}
		return self.data_dict

	
#!/usr/bin/python3
# -*- coding: utf-8 -*-
import xlrd
import uuid
from change import Change
from iteration import Iteration

class Reaction(Change):
	"""Реакция на изменение (унаследован от изменения)"""

	"Полный список реакций"
	full_list = []

	"Хранит словарь сущностей" 
	def __init__(self, iteration, description = None):
		super().__init__(iteration, description = None)
		iteration.reactions_list.append(self)
		iteration.set_iteration()
	
	"Изменение отображения класса при принте"
	def __str__(self):
		return "Reaction № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Reaction № {}".format(self.uid)


	
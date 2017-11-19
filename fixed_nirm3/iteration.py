#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import xlrd
import uuid

from k_map import Map
from scenario import Scenario
from change import Change

class Iteration:
	"""Итерация = несколько изменений (Список)"""

	"Полный список итераций"
	full_list = []

	def __init__(   self,  
					scenario = None, 
					description=None, 
					changes_list=[],
					reactions_list = [],  
					data_dict = {}):

		self.uid = uuid.uuid4().hex
		self.scenario = scenario
		self.description = description
		self.full_list.append(self)
		self.scenario.add_iteration(self)

		self.changes_list = changes_list
		self.reactions_list = reactions_list

		# словарь изменений и реакций в итерации
		self.data_dict = data_dict


	"Изменение отображения класса при принте"
	def __str__(self):
		return "Iteration № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Iteration № {}".format(self.uid)


	"Метод создания словаря изменений итерации из excel файла"
	def create_change_pack(self, location, sheet_num, row_start, row_end, column):
		location = xlrd.open_workbook(location,formatting_info=True)
		sheet_num = location.sheet_by_index(sheet_num)
		for rownum in range(row_start,row_end):
			full_cell = str(sheet_num.cell_value(rownum,column))
			if full_cell != '':
				splited_cells = full_cell.strip().lower().split(' ')
				description = 'No description'
				change_type = None
				order = None
				cell = []
				value = 0
				duration = 0	
				for splited_cell in splited_cells:
					if splited_cell.isdigit():
						cell.append(splited_cell)
					elif splited_cell.startswith('w'):
						change_type = splited_cell
					elif splited_cell.startswith('e'):
						change_type = splited_cell
					elif splited_cell.startswith('+') or splited_cell.startswith('-'):
						if splited_cell.endswith('%'):
							value = float(splited_cell.split('%')[0])
							#print('ЗНАЧЕНИЕ = ',splited_cell.split('%'))
						else:
							try:
								value = float(splited_cell)
							except ValueError:
								pass

						# print('value', value)
					elif splited_cell.startswith('d'):
						duration = splited_cell.split('d')[1]
						# print('duration', duration)
					elif splited_cell.startswith('or'):
						order = splited_cell.split('or')[1]
						# print('order', order)						
					else:
						try:
							value = float(splited_cell)
							# print('value without sign', value)
						except ValueError:
							#print('Excel файл содержит неправильный формат данных или пустые ячейки', ValueError)
							pass
				new_change = Change(iteration = self)
				if change_type == 'e':
					try:
						new_change.set_node_change(name = self.scenario.k_map.node_name_list[int(cell[0])], 
							 							value = value,
							 							order = order, 
							 							duration = duration)
					except:
						print('Ошибка создания изменения вершины')

				elif change_type == 'w':
					try:
						new_change.set_link_change(	source = self.scenario.k_map.node_name_list[int(cell[0])], 
															target = self.scenario.k_map.node_name_list[int(cell[1])],
															value = value, 
															order = order,  
															duration = duration)
					except:
						print('Ошибка создания изменения ребра')
				else:
					pass
				self.changes_list.append(new_change)

			else:
				pass
		self.set_iteration()


	def set_iteration(self):
		ch_list = []
		reac_list = []
		for change in self.changes_list:
			ch_list.append(change.data_dict)
		for reaction in self.reactions_list:
			reac_list.append(reaction.data_dict)
		self.data_dict = {  'changes': ch_list,
							'reactions': reac_list} 
		return self.data_dict

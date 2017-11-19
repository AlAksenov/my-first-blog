#!/usr/bin/python3.5
# -*- coding: utf-8 -*-
import xlrd
import uuid
import math

class Map():
	"Список всех карт"
	map_list = []

	def __init__(self, name = 'No name', node_data = [], link_data = []):
		self.uid = uuid.uuid4().hex
		self.name = name
		# словарь всей карты
		self.map_dict = {}
		# атрибуты вершин
		self.node_data = node_data
		self.node_dict = {}
		self.node_name_list = []
		# шкалы вершин
		self.node_scale_list = []
		# атрибуты ребер
		self.link_data = link_data
		self.link_dict = {}
		self.weight_matrix = []
		# список всех созданных карт
		self.map_list.append(self)
		# список повторений (исключает циклы)
		self.__cycle_list = []	

		# self.set_data()

	"Изменение отображения класса при принте"
	def __str__(self):
		return "Map № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Map № {}".format(self.uid)

	"Создание словаря вершин из excel"
	def set_node_dict(   self,  
						 location,
						 sheet_num, 
						 row_start, 
						 row_end, 
						 column_scales, 
						 column_values,
						 column_names):
		location = xlrd.open_workbook(location,formatting_info=True)
		sheet_num = location.sheet_by_index(sheet_num)
		for rownum in range(row_start,row_end):
			cella_scales = float(sheet_num.cell_value(rownum,column_scales))
			cella_values = float(sheet_num.cell_value(rownum,column_values))
			cella_names = str(sheet_num.cell_value(rownum,column_names))
			self.node_scale_list.append(cella_scales)
			self.node_name_list.append(cella_names)
			self.node_data.append({'node': cella_names, 'value': cella_values, 'scale': cella_scales})
		self.node_dict = {'nodes': self.node_data}
		self.set_map()
		return self.node_dict	

	"Создание словаря ребер из excel"
	def set_link_dict(self, location, sheet_num, row_start, row_end, column_start, column_end):
		location = xlrd.open_workbook(location,formatting_info=True)
		sheet_num = location.sheet_by_index(sheet_num)
		line = []
		for rownum in range(row_start,row_end):
			for column in range(column_start,column_end):
				# пустые ячейки в xls считаются текстом, поэтому они заполняются нулями
				try:
					cella = float(sheet_num.cell_value(rownum,column))
				except ValueError:
					cella = 0.0
				line.append(cella)
		self.weight_matrix = [line[x:x+int(len(line)**0.5)] for x in range(0, len(line), int(len(line)**0.5))]

		for row in range(len(self.weight_matrix)):
			for col in range(len(self.weight_matrix)):
				if self.weight_matrix[row][col] != 0:
					self.link_data.append({ "source": self.node_name_list[row], 
											"target": self.node_name_list[col], 
											"weight": self.weight_matrix[row][col]})
		self.link_dict = {"links": self.link_data}
		self.set_map()
		return self.link_dict

	"Создание карты"
	def set_map(self):
		self.map_dict = {"nodes": self.node_data, "links": self.link_data}
		return self.map_dict

	"Метод изменения значения вершины"
	def node_change(self, change = None):
		name = change.get('node')
		new_value = change.get('value')
		for change_item in self.node_data:
			if change_item.setdefault('node','') == name:
				change_item.update({'node': name, 'value': new_value})
		return name


	"Метод пересчета карты по одному изменению"
	def recount_change(self, change = None):
		# изменение начального значения
		self.node_change(change)
		# деление вершин на шкалы
		self.node_value_divider()
		# внутренний пересчет всей карты на основе изменения
		self.__inner_recount(change)
		# очистка списка циклов
		self.__cycle_list.clear()
		# умножение вершин на шкалы
		self.node_value_multiplier()
		return self.set_map()

	"Метод пересчета карты по итерации"
	def recount_iteration(self, iteration = None):
		for change in iteration:
			self.recount_change(change)	
		return self.set_map()


	"Внут метод пересчета карты по одному изменению"
	# из-за json получается тройное вложение циклов мм... здорово
	# мб есть способ сделать лучше?
	def __inner_recount(self, change = None):
		# цикл перебора ребер влияния исходной вершины
		for link_item in self.link_data:
			# список ребер, влияющих на таргет
			a_list = []
			# сумма прозведений ребер на вершины
			summ_c_w = 0
			# имя искходной вершины
			source_name = change.get('node') 
			# отбор всех ребер влияния исходной вершины
			if link_item.setdefault('source','') == source_name:
				# создание таргета
				target_name = link_item.setdefault('target','')
				# фильтр циклов
				if [source_name, target_name] not in self.__cycle_list:
					#print('текущая комбинация',[source_name, target_name])

					# поиск всех ребер влияющих на этот таргет
					for link in self.link_data:
						if link.setdefault('target','') == target_name:
							# добавление этих ребер в список
							a_list.append(link)
					# перебор ребер, влияющих на таргет
					for a_link in a_list:
						# поиск значения вершины
						for i in self.node_data:
							if i.get('node') == a_link.get('source') and target_name == a_link.get('target'):
								c_value = i.get('value')
						# создание суммы произведений ребер на вершины
						summ_c_w += a_link.get('weight')*c_value

					# поиск старого значения таргет-вершины 
					for i in self.node_data:
						if i.get('node') == target_name:
							old_target_value = i.get('value')
					new_target_value = self.sigmoid(summ_c_w + old_target_value)
					new_change = {'node': target_name, 'value': new_target_value}
					self.node_change(new_change)
					# добавление комбинации сущностей в список циклов
					self.__cycle_list.append([source_name, target_name])
					# запуск рекурсии
					self.__inner_recount(new_change)
				else: 
					#print('Нашел цикл')
					pass
		#print('Список циклов',len(self.__cycle_list),self.__cycle_list)
		return self.set_map()


	"Функция активации (сигмоида)"
	def sigmoid(self,x=0):
		return (1/(1 + math.exp(-0.5*(x))))

	"Метод расчетного значения вершины на шкалу"
	def node_value_multiplier(self):
		for node in self.node_data:
			node.update({'value': node.get('value')*node.get('scale')})

	"Метод деления реального значения вершины на шкалу"
	def node_value_divider(self):
		for node in self.node_data:
			node.update({'value': node.get('value')/node.get('scale')})		


#!/usr/bin/python3
# -*- coding: utf-8 -*-

import uuid
from entity import Entity
from matrix import Matrix
import copy

class United(Entity, Matrix):
	def __init__ (self, entity, matrix):
		self.uid = uuid.uuid4().hex
		self.entity = entity
		self.matrix = matrix
		# список повторений (исключает циклы)
		self.cycle_list = []	

	"Изменение отображения класса при принте"
	def __str__(self):
		return "Объект United № {}".format(self.uid)

	"Изменения внутреннего представления класса"
	def __repr__(self):
		return  "Объект United № {}".format(self.uid)

	"Рекурсивный метод пересчета сущностей и матрицы"
	def recount(self, key = None, key_index = None, new_value = 0, recount_type = None):
		# Пересчет по ключу
		if key_index == None and key != None:
			# изменение значения сущности по ключу
			self.entity.fixed_change(key = key, new_value = new_value)
			print('ВЫПОЛНЕНО НАЧАЛЬНОЕ ИЗМЕНЕНИЕ ПО КЛЮЧУ', key, self.entity.data_dict[key])
			# вызов внутренней функции пересчета
			self.__inner_recount(key = key, new_value = new_value, recount_type = recount_type)
			# очистка списка повторений
			self.cycle_list.clear()

		# Пересчет по индексу ключа
		elif key_index != None and key == None:
			# изменение значения сущности индексу 
			self.entity.fixed_change(index = key_index, new_value = new_value)
			print('ВЫПОЛНЕНО НАЧАЛЬНОЕ ИЗМЕНЕНИЕ ПО ИНДЕКСУ', key_index, self.entity.data_list[key_index])
			key = self.entity.ordered_name_list[key_index]
			# вызов внутренней функции пересчета
			self.__inner_recount(key = key, new_value = new_value, recount_type = recount_type)
			# очистка списка повторений
			self.cycle_list.clear()
		else: 
			print('Ошибка пересчета')
		
	"Внутренняя функция пересчета сущности (рекурсия)"	
	def __inner_recount(self, key, new_value, recount_type = None):
		# получение индекса строки влияния
		base_row_index = self.entity.ordered_name_list.index(key)
		# список новых ключей ряда, порождаемых пересчетом
		new_key_list = []
		# вектор изменений сущности
		p_vector = []
		# перебор по столбцам	
		for col in range(len(self.matrix.weight_matrix)):
			# копия старого значения сущности
			old_entity_value = copy.deepcopy(self.entity.data_list[col])			
			# фильтр циклов
			if [base_row_index, col] not in self.cycle_list:
				# фильтр пустых клеток
				if self.matrix.weight_matrix[base_row_index][col] != '':
					# Изменение 
					self.entity.data_list[col] = self.__formula_reader(self.matrix.weight_matrix[base_row_index][col])
					# пополнение списка новыми ключами
					new_key_list.append(self.entity.ordered_name_list[col])
					# добавление комбинации сущностей в список циклов
					self.cycle_list.append([base_row_index, col])
				else:
					pass
				# добавление изменения в вектор изменений
				p_vector.append(self.entity.data_list[col]-old_entity_value)
			else: 
				print('Нашел цикл')
				pass
		# print('ВЕКТОР ИЗМЕНЕНИЙ = ',p_vector)
		# print('Список новых ключей = ',new_key_list)
		# print('Список циклов = ', self.cycle_list)
		# проверка наличия новых ключей в списке
		if new_key_list != []:
			# перебор новых ключей
			for new_key in new_key_list:
				# запуск функции с новыми аргументами (рекурсия)
				self.__inner_recount(key = new_key, 
									 new_value = self.entity.data_list[self.entity.ordered_name_list.index(new_key)])	
		else:
			# print('Новые ключи закончились')
			pass

	"Метод пересчета сущности по формуле из матрицы"
	def __formula_reader(self, string):
		# отформатированная строка
		base_string = string.lower().strip()
		# список иксов
		x_list = []
		# словарь X-значение
		x_dict = {}
		for i in range(len(self.entity.data_list)):
			x_list.append('x' + str(i))
			x_dict.update({x_list[i]: self.entity.data_list[i]})
		# eval() перобразует строку в формулу и исполняет
		result = eval(base_string, x_dict)
		return result

		



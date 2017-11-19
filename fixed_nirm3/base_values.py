#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import os

from k_map import Map
from smart_print import dprint
from json_file import File
from iteration import Iteration
from scenario import Scenario
from change import Change
from reaction import Reaction
from recount import recount

def main():
	# путь до excel
	excel_path = os.getcwd() + '/static/json/base_info.xls'

	# создание карты
	map_sber = Map("Карта сбербанка")
	map_sber.set_node_dict(excel_path, 1, 1, 17, 1 , 2, 3)
	map_sber.set_link_dict(excel_path, 1, 1, 17, 5, 21)

	# dprint(map_sber.map_dict)
	# dprint(len(map_sber.map_dict.get('links')))
	# dprint(len(map_sber.map_dict.get('nodes')))

	# создание сценария
	sc = Scenario(k_map=map_sber)
	
	# создание итераций
	it_1 = Iteration(scenario=sc, description='Итерация 1')
	it_2 = Iteration(scenario=sc, description='Итерация 2')
	it_3 = Iteration(scenario=sc, description='Итерация 3')

	dprint('Список итераций в сценарии', sc.data_list)
	
	# блок реакций (по 2 реакции на 1 итерацию)
	reac_1 = Reaction(it_1)
	reac_2 = Reaction(it_1)
	reac_1.set_node_change(name = 'Число сотрудников банка', value = 315000,)
	reac_2.set_node_change(name = 'Средняя ставка по кредитам', value = 12,)

	reac_3 = Reaction(it_2)
	reac_4 = Reaction(it_2)
	reac_3.set_node_change(name = 'Число отделений банка', value = 13000,)
	reac_4.set_node_change(name = 'Количество клиентов', value = 130000000,)

	reac_5 = Reaction(it_3)
	reac_6 = Reaction(it_3)
	reac_5.set_node_change(name = 'Степень автоматизации процессов', value = 75,)
	reac_6.set_node_change(name = 'Средняя ставка по депозитам', value = 9,)


	# добавление изменений в итерации
	it_1.create_change_pack(excel_path, 2, 3, 9, column = 1)
	it_2.create_change_pack(excel_path, 2, 3, 9, column = 2)
	it_3.create_change_pack(excel_path, 2, 3, 9, column = 3)

	dprint('Содержание итерации 1',it_1.data_dict)
	dprint('Содержание итерации 2',it_2.data_dict)
	dprint('Содержание итерации 3',it_3.data_dict)

	# создание json-файлов и запись в них информации
	# описание путей до json
	file_path_0 = os.getcwd() +'/static/json/json_files/k_map.txt'

	file_path_1 = os.getcwd() +'/static/json/json_files/iteration_1.txt'
	file_path_2 = os.getcwd() +'/static/json/json_files/iteration_2.txt'
	file_path_3 = os.getcwd() +'/static/json/json_files/iteration_3.txt'

	# пути до изменений итерации 1
	file_path_11 = os.getcwd() +'/static/json/json_files/change_11.txt'
	file_path_12 = os.getcwd() +'/static/json/json_files/change_12.txt'

	# пути до изменений итерации 2
	file_path_21 = os.getcwd() +'/static/json/json_files/change_21.txt'
	file_path_22 = os.getcwd() +'/static/json/json_files/change_22.txt'

	# пути до изменений итерации 3
	file_path_31 = os.getcwd() +'/static/json/json_files/change_31.txt'
	file_path_32 = os.getcwd() +'/static/json/json_files/change_32.txt'

	# создание json-карты (1)
	file_0 = File(file_path_0)
	file_0.write(map_sber.map_dict)

	# создание json-итераций (3)
	file_1 = File(file_path_1)
	file_1.write(it_1.data_dict)

	file_2 = File(file_path_2)
	file_2.write(it_2.data_dict)

	file_3 = File(file_path_3)
	file_3.write(it_3.data_dict)

	# создание json-реакций (6)
	file_11 = File(file_path_11)
	file_11.write(reac_to_iter(reac_1.data_dict))

	file_12 = File(file_path_12)
	file_12.write(reac_to_iter(reac_2.data_dict))

	file_21 = File(file_path_21)
	file_21.write(reac_to_iter(reac_3.data_dict))

	file_22 = File(file_path_22)
	file_22.write(reac_to_iter(reac_4.data_dict))

	file_31 = File(file_path_31)
	file_31.write(reac_to_iter(reac_5.data_dict))

	file_32 = File(file_path_32)
	file_32.write(reac_to_iter(reac_6.data_dict))
	

	# # функция пересчета
	# dprint('Пересчитанная карта',recount(file_path_0, file_path_11))


# функция переводит реакцию в формат итерации
def reac_to_iter(reac):
	return {'changes':[reac]}


if __name__ == '__main__':
	main()

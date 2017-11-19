#!/usr/bin/python3.5
# -*- coding: utf-8 -*-

import os

from k_map import Map
from iteration import Iteration
from json_file import File
from scenario import Scenario
from smart_print import dprint

# принимает путь до файла карты и путь до файла изменения
def recount(json_map_path, json_change_path):
	# try:
	json_map_file = File(json_map_path)
	json_change_file = File(json_change_path)
	if json_map_file.read() != {} or json_change_file.read() != {}:
		node_data = json_map_file.read().get('nodes')
		link_data = json_map_file.read().get('links')

		json_map = Map(node_data=node_data, link_data=link_data)
		scenario = Scenario(json_map)
		json_change = Iteration(scenario = scenario, data_dict = json_change_file.read())
		# новая карта
		new_map = json_map.recount_iteration(json_change.data_dict.get('changes'))
		# перезапись файла
		json_map_file.write(new_map)
		return new_map
	else:
		return 'Необходимо создать исходные файлы'
	# except:
	# 	print('Чечьня круто')


def main():
	# путь до карты
	file_path_0 = os.getcwd() +'/static/json/json_files/k_map.txt'
	# путь до итерации или изменения
	file_path_1 = os.getcwd() +'/static/json/json_files/iteration_1.txt'
	# функция пересчета
	dprint('Пересчитанная карта',recount(file_path_0, file_path_1))

def main1():
	# путь до карты
	file_path_0 = os.getcwd() +'/static/json/json_files/k_map.txt'
	# путь до итерации или изменения
	file_path_1 = os.getcwd() +'/static/json/json_files/change_11.txt'
	# функция пересчета
	dprint('Пересчитанная карта',recount(file_path_0, file_path_1))

def main2():
	# путь до карты
	file_path_0 = os.getcwd() +'/static/json/json_files/k_map.txt'
	# путь до итерации или изменения
	file_path_1 = os.getcwd() +'/static/json/json_files/change_12.txt'
	# функция пересчета
	dprint('Пересчитанная карта',recount(file_path_0, file_path_1))

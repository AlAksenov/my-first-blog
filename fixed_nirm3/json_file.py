#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import os

class File:
	def __init__(self, file_path):
		# в file_path записывается путь
		self.file_path = os.path.abspath(file_path)
		if not os.path.exists(file_path):
			# open создает файл
			try:
				with open(self.file_path, 'w') as f:
					pass
			except:
				print('Проблема создания файла', ' (Измени путь создания файла)')
		else:
			pass

	def __str__(self):
		return self.file_path

	# запись json
	def write(self, data):
		# try:
		with open(self.file_path, 'w') as f:
			f.write(json.dumps(data, ensure_ascii=False, sort_keys=True, indent=2 ))
			#print('Успешная запись')
		# except:
		# 	print('Проблема записи данных в файл')

	# чтение json
	def read(self):
		try:
			with open(self.file_path, 'r') as f:
				raw_data = f.read()
				if raw_data:
					return json.loads(raw_data, encoding='utf-8')
				return {}
		except IOError:
			return ""

	# удаление файла
	def delete(self):
		os.remove(self.file_path)



def main():
	# прописать подходящий путь для создания файла
	data_file = File("/home/yuriy/Desktop/your_json.txt")
	# запись данных
	asd = 'more_data'
	data_file.write('some data')
	data_file.write(asd)

	print('\n')
	print('Содержание файла =',data_file.read())


if __name__ == '__main__':
	main()


	dprint('количество вершин', len(sc.data_list[0].full_change_dict.get('node_changes')))
	dprint('количество ребер', len(sc.data_list[0].full_change_dict.get('link_changes')))

	dprint('количество вершин', len(sc.data_list[1].full_change_dict.get('node_changes')))
	dprint('количество ребер', len(sc.data_list[1].full_change_dict.get('link_changes')))
	dprint('Проверка равенства', sc.data_list[1].full_change_dict.get('link_changes') \
		== sc.data_list[0].full_change_dict.get('link_changes'))

	

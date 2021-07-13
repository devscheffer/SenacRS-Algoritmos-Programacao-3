def fn_get_item( dictionary: dict) -> tuple:
	lst_key_sorted = sorted(dictionary.keys())
	item = dictionary[lst_key_sorted[0]].pop(0)
	if dictionary[lst_key_sorted[0]] == []:
		dictionary.pop(lst_key_sorted[0])
		lst_key_sorted.pop(0)
	return dictionary, item

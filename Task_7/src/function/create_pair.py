from Task_7.src.function.get_element_value import fn_get_element_value
from Task_7.src.function.get_item_from_dict_list import fn_get_item


def fn_create_pair(dictionary: dict) -> tuple:
	pair = []
	total = 0
	while len(pair) < 2 and dictionary != {}:
		dictionary, item = fn_get_item(dictionary)
		pair.append(item)
		total += fn_get_element_value(item)
	return dictionary, pair, total

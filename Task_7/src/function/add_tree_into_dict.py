
from Task_7.src.create_node import cls_node


def fn_add_tree_into_dict( binary_tree: cls_node, dictionary: dict) -> dict:
	tree_data = binary_tree.data
	if tree_data in dictionary:
		dictionary[tree_data].append(binary_tree)
	else:
		dictionary[tree_data] = [binary_tree]
	return dictionary

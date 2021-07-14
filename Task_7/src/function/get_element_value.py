from Task_7.src.create_node import cls_node


def fn_get_element_value(element):
	if isinstance(element, dict):
		return element['frequency']
	if isinstance(element, cls_node):
		return element.data
	else:
		raise Exception('The element is not a dictionary or a node.')


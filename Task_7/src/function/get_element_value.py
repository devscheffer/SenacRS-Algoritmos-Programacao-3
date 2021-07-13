def fn_get_element_value(element) -> int:
	if isinstance(element, dict):
		element_value = element['frequency']
	else:
		element_value = element.data
	return element_value


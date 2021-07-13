def fn_create_dict_binary_to_string(string):
	dict_translate = {}
	string_set=''.join(list(set(string)))
	string_set_binary=list(map(bin,bytearray(string_set,'utf-8')))
	for j in range(len(string_set)):
		dict_translate[string_set_binary[j]] = string_set[j]
	return dict_translate

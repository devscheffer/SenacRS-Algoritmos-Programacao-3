from Task_7.src.function.create_dict_binary_to_string import fn_create_dict_binary_to_string
from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.src.create_node import cls_node
from Task_7.src.function.add_tree_into_dict import fn_add_tree_into_dict
from Task_7.src.function.create_pair import fn_create_pair
from Task_7.src.function.create_binary_tree_huffman import fn_create_binary_subtree


class cls_huffman_algorithm:
	def __init__(self, input_string: str):
		self._string = input_string

	@property
	def string(self):
		return self._string

	@string.setter
	def string(self, value: str):
		self._string = value

	def mtd_create_table_frequency(self) -> dict:
		dict_frequency = {}
		for char in self.string:
			if char in dict_frequency:
				dict_frequency[char] += 1
			else:
				dict_frequency[char] = 1
		return dict_frequency

	def mtd_create_table_frequency_list(self)->dict:
		dict_frequency_list = {}
		dict_frequency = list(
			self
			.mtd_create_table_frequency()
			.items()
			)
		for k, v in dict_frequency:
			dict_element = {"char": k, "frequency": v}
			if v in dict_frequency_list:
				dict_frequency_list[v].append(dict_element)
			else:
				dict_frequency_list[v] = [dict_element]
		return dict_frequency_list

	def mtd_create_binary_tree_huffman(self) -> cls_node:
		dict_list_frequency = self.mtd_create_table_frequency_list()
		while dict_list_frequency != {}:
			dict_list_frequency, pair, total = fn_create_pair(dict_list_frequency)
			binary_tree = fn_create_binary_subtree(pair, total)
			dict_list_frequency = fn_add_tree_into_dict(binary_tree, dict_list_frequency)
			list_key = list(dict_list_frequency.keys())
			key = dict_list_frequency[list_key[0]]
			if len(list_key) == 1 and len(key) == 1:
				return key[0]

	def mtd_create_binary_table(self) -> dict:
		root_node = self.mtd_create_binary_tree_huffman()
		dictionary = root_node.mtd_dct_leaf_path_Preorder()
		return dictionary

	def mtd_string_to_binary_normal(self) -> dict:
		string = self.string
		string_binary = list(map(bin,bytearray(string,'utf8')))
		binary = ' '.join(string_binary)
		binary_size = len(str(binary))
		dict_binary_to_string=fn_create_dict_binary_to_string(string)
		dict_normal = {
			"binary": binary
			, "size": binary_size
			,"dict_binary_to_string":dict_binary_to_string}
		return dict_normal



	def mtd_string_to_binary_huffman(self) -> dict:
		dct_aux = self.mtd_create_binary_table()
		dict_binary_to_string = {}
		lst_binary = []
		for i in self.string:
			element = dct_aux[i]["path_binary"]
			lst_binary.append(element)
			dict_binary_to_string[element] = i
		binary = ' '.join(lst_binary)
		binary_size = len(str(binary))
		dict_huffman = {
			"binary": binary
			, "size": binary_size
			,"dict_binary_to_string":dict_binary_to_string}
		return dict_huffman

	def mtd_compression(self) -> str:
		normal = self.mtd_string_to_binary_normal()["size"]
		huffman = self.mtd_string_to_binary_huffman()["size"]
		ratio = huffman / normal
		return f"{ratio*100:.1f} %"

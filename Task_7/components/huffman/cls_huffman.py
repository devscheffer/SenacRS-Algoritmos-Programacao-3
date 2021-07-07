from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.binary_tree.cls_node import cls_node


class cls_huffman:
	def __init__(self, inpt_text: str) -> None:
		self._text = inpt_text

	@property
	def text(self) -> str:
		return self._text

	@text.setter
	def text(self, text: str) -> None:
		self._text = text

	def fn_frequency_table(self) -> dict[str, int]:
		frequency: dict[str, int] = {}
		for letter in self.text:
			if letter in frequency:
				frequency[letter] += 1
			else:
				frequency[letter] = 1
		return frequency

	def fn_frequency_list(self) -> dict[int, list[tuple[str, int]]]:
		dct_frequency: dict[int, list[tuple[str, int]]] = {}
		for k, v in self.fn_frequency_table().items():
			if v in dct_frequency:
				dct_frequency[v].append((k, v))
			else:
				dct_frequency[v] = [(k, v)]
		return dct_frequency

	def __get_element_value(self, element) -> int:
		if isinstance(element, cls_node):
			element_value = element.data
		else:
			element_value = element[1]
		return element_value

	def __get_item(self, dct_aux):
		lst_key: list[int] = list(dct_aux.keys())
		lst_key_sorted: list[int] = sorted(lst_key)
		item = dct_aux[lst_key_sorted[0]].pop(0)
		if dct_aux[lst_key_sorted[0]] == []:
			dct_aux.pop(lst_key_sorted[0])
			lst_key_sorted.pop(0)
		return dct_aux, item

	def __create_binary_tree(self, pair, total):
		binary_tree = cls_node(total)
		for i in range(len(pair)):
			element = pair.pop(0)
			binary_tree.insert(element)
		return binary_tree

	def __create_pair(self, dct_aux):
		pair = []
		total = 0
		while len(pair) < 2:
			dct_aux, item = self.__get_item(dct_aux)
			pair.append(item)
			total += self.__get_element_value(item)
		return dct_aux, pair, total


	def __insert_tree_in_dict(self, binary_tree, dct_aux):
		dct_aux_v2 = dct_aux
		if binary_tree.data in dct_aux:
			dct_aux_v2[binary_tree.data].append(binary_tree)
		else:
			dct_aux_v2[binary_tree.data] = [binary_tree]
		return dct_aux_v2

	def fn_create_huffman_binary_tree(self):
		dct_aux = self.fn_frequency_list()
		while dct_aux != {}:
			dct_aux, pair, total = self.__create_pair(dct_aux)
			binary_tree = self.__create_binary_tree(pair, total)
			dct_aux=self.__insert_tree_in_dict(binary_tree, dct_aux)
			if len(dct_aux.keys()) == 1 and len(dct_aux[list(dct_aux.keys())[0]]) == 1:
				return dct_aux[list(dct_aux.keys())[0]][0]

	def fn_binary_table(self):
		root_node = self.fn_create_huffman_binary_tree()
		dct_aux=root_node.dct_leaf_path_Preorder()
		dct_aux_v2= {}
		for i in dct_aux:
			lst_binary = list(map(str,(dct_aux[i])))
			new_binary=''.join(lst_binary)
			dct_aux_v2[i]=new_binary
		return dct_aux_v2





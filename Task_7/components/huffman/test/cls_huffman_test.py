from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_7.components.huffman.cls_huffman import cls_huffman

class Test_frequency:
	def test_dictionary(self):
		res = cls_huffman("hello world")
		assert res.fn_frequency_table()== {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
	def test_dictionary_key(self):
		res = cls_huffman("hello world")
		assert res.fn_frequency_list()== {1: [('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)], 3: [('l', 3)], 2: [('o', 2)]}

	def test_list_item(self):

		res = cls_huffman("aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst")
		assert res.fn_frequency_list() == {10: [('a', 10)], 15: [('e', 15)], 12: [('i', 12)], 3: [('o', 3)], 4: [('u', 4)], 13: [('s', 13)], 1: [('t', 1)]}
	def test_leaf_path(self):

		res = cls_huffman("aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst")
		root_node = res.fn_create_huffman_binary_tree()
		bt= root_node
		assert bt.dct_leaf_path_Preorder() == {('i', 12): [0, 0], ('s', 13): [0, 1], ('e', 15): [1, 0], ('u', 4): [1, 1, 0, 0], ('t', 1): [1, 1, 0, 1, 0], ('o', 3): [1, 1, 0, 1, 1], ('a', 10): [1, 1, 1]}
	def test_binary_table(self):

		res = cls_huffman("aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst")
		assert res.fn_binary_table() == {('i', 12): '00', ('s', 13): '01', ('e', 15): '10', ('u', 4): '1100', ('t', 1): '11010', ('o', 3): '11011', ('a', 10): '111'}







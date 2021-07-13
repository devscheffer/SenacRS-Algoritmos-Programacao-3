from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.src.create_huffman_algorithm import cls_huffman_algorithm


class Test_1_item:
	def test_binary_table_1_item(self):
		t5 = cls_huffman_algorithm("a")
		binary_table = t5.mtd_create_binary_table()
		assert binary_table == {"a": {"path_binary": "0", "frequency": 1}}


class Test_init:
	def test_init_get(self):
		string = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
		res = cls_huffman_algorithm(string)
		assert res.string == string

	def test_init_set(self):
		string = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
		res = cls_huffman_algorithm(string)
		res.text = "ab"
		assert res.text == "ab"


class Test_dict_frequency:
	def test_dictionary(self):
		t1 = cls_huffman_algorithm("hello world")
		assert t1.mtd_create_table_frequency() == {
			"h": 1,
			"e": 1,
			"l": 3,
			"o": 2,
			" ": 1,
			"w": 1,
			"r": 1,
			"d": 1,
		}

	def test_dictionary_key(self):
		t2 = cls_huffman_algorithm("hello world")
		res = t2.mtd_create_table_frequency_list()
		assert (res) == {1: [{'char': 'h', 'frequency': 1}, {'char': 'e', 'frequency': 1}, {'char': ' ', 'frequency': 1}, {'char': 'w', 'frequency': 1}, {'char': 'r', 'frequency': 1}, {'char': 'd', 'frequency': 1}], 3: [{'char': 'l', 'frequency': 3}], 2: [{'char': 'o', 'frequency': 2}]}

	def test_leaf_path(self):
		t3 = cls_huffman_algorithm(
			"aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
		)
		root_node = t3.mtd_create_binary_tree_huffman()
		res = root_node.mtd_dct_leaf_path_Preorder()
		assert res == {'i': {'frequency': 12, 'path_binary': '00'}, 's': {'frequency': 13, 'path_binary': '01'}, 'e': {'frequency': 15, 'path_binary': '10'}, 'u': {'frequency': 4, 'path_binary': '1100'}, 't': {'frequency': 1, 'path_binary': '11010'}, 'o': {'frequency': 3, 'path_binary': '11011'}, 'a': {'frequency': 10, 'path_binary': '111'}}

	def test_binary_table(self):
		t4 = cls_huffman_algorithm(
			"aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
		)
		res=t4.mtd_create_binary_table()
		assert res == {'i': {'frequency': 12, 'path_binary': '00'}, 's': {'frequency': 13, 'path_binary': '01'}, 'e': {'frequency': 15, 'path_binary': '10'}, 'u': {'frequency': 4, 'path_binary': '1100'}, 't': {'frequency': 1, 'path_binary': '11010'}, 'o': {'frequency': 3, 'path_binary': '11011'}, 'a': {'frequency': 10, 'path_binary': '111'}}


class Test_binary_table:
	def test_binary_table(self):
		res = cls_huffman_algorithm("hello world")
		answer = {
			" ": {"path_binary": "000", "frequency": 1},
			"w": {"path_binary": "001", "frequency": 1},
			"r": {"path_binary": "010", "frequency": 1},
			"d": {"path_binary": "011", "frequency": 1},
			"l": {"path_binary": "10", "frequency": 3},
			"o": {"path_binary": "110", "frequency": 2},
			"h": {"path_binary": "1110", "frequency": 1},
			"e": {"path_binary": "1111", "frequency": 1},
		}
		for k, v in res.mtd_create_binary_table().items():
			assert v == answer[k]

	def test_string_to_binary(self):
		res = cls_huffman_algorithm("a")
		assert res.mtd_string_to_binary_normal()["binary"] == "0b1100001"

	def test_string_huffman_binary(self):
		res = cls_huffman_algorithm("abb")
		assert (res.mtd_string_to_binary_huffman())["binary"] == "0 1 1"

	def test_compression(self):
		res = cls_huffman_algorithm("abb")
		assert (res.mtd_string_to_binary_normal())['size'] == 29
		assert (res.mtd_compression()) == "17.2 %"

from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_7.components.huffman.cls_huffman import cls_huffman

class Test_frequency:
	def test_dictionary(self):
		res = cls_huffman("hello world")
		assert res.fn_frequency()== {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}
	def test_dictionary_key(self):
		res = cls_huffman("hello world")
		assert res.fn_frequency_key()== {1: [('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)], 3: [('l', 3)], 2: [('o', 2)]}


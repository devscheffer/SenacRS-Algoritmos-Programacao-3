from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.huffman.cls_huffman import cls_huffman

string = "aaaaaaaaaaeeeeeeeeeeeeeeeiiiiiiiiiiiiooouuuussssssssssssst"
res = cls_huffman(string)
table_freq = res.fn_frequency_table()
print(table_freq)
table_binary = res.fn_binary_table()
print(table_binary)

from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.file_read import cls_read_file
from Task_7.components.huffman_algorithm import cls_huffman_algorithm


file_name = 'entrada.txt'

print('read file')
file_text=cls_read_file(file_name)
string = file_text.read_file()
print(string)

res = cls_huffman_algorithm(string)

print('frequencia:')
table_freq = res.mtd_create_frequency_table()
print(table_freq)
print()

print('Binary path:')
table_binary = res.mtd_create_binary_table()
print(table_binary)
print()

print('Compressao:')
comprassion = res.mtd_compression()
print(res.mtd_string_to_binary_normal())
print(res.mtd_string_to_binary_huffman())
print(comprassion)
print()

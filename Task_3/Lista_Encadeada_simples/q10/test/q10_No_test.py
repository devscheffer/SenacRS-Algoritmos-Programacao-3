from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.q10.No import Node

class Test_node:
	def test_node(self):
		n1= Node('2021-01-01')
		assert n1.label.data == '2021-01-01'
		assert n1.next == None

from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.ListasSimplesmenteEncadeadas.v2.No import Node

class Test_node:
	def test_node(self):
		n1= Node('teste')
		assert n1.label == 'teste'
		assert n1.next == None

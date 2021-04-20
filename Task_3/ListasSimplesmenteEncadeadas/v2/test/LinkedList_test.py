from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.ListasSimplesmenteEncadeadas.v2.LinkedList import LinkedList
import pytest
class Test_linkedList:

	def test_creation(self):
		lista = LinkedList()
		lista.Node_add('Eduarda', 0)
		assert lista.viewList() == ['Eduarda']

	def test_index_lt_0(self):
		lista = LinkedList()
		with pytest.raises(ValueError):
			lista.Node_add('Eduarda', -1)

	def test_many(self):
		lista = LinkedList()
		lista.Node_add('p1', 0)
		lista.Node_add('p2', 1)
		lista.Node_add('p3', 2)
		lista.Node_add('p4', 5)
		assert lista.viewList() == ['p1','p2','p3','p4']

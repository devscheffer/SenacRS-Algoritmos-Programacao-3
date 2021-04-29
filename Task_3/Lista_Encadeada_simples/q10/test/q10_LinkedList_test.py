from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.q10.LinkedList import LinkedList
import pytest
class Test_linkedList:

	def test_creation(self):
		lista = LinkedList()
		lista.Node_add('2021-02-05', 0)
		assert lista.viewList() == ['2021-02-05']

	def test_index_lt_0(self):
		lista = LinkedList()
		with pytest.raises(ValueError):
			lista.Node_add('Eduarda', -1)

	def test_add(self):
		lista = LinkedList()
		lista.Node_add('2021-02-05', 0)
		lista.Node_add('2021-03-05', 1)
		lista.Node_add('2021-04-05', 2)
		lista.Node_add('2021-05-05', 5)
		assert lista.viewList() == ['2021-02-05','2021-03-05','2021-04-05','2021-05-05']

	def test_sub(self):
		lista = LinkedList()
		lista.Node_add('2021-02-05', 0)
		lista.Node_add('2021-03-05', 1)
		lista.Node_add('2021-04-05', 2)
		lista.Node_add('2021-05-05', 5)
		lista.Node_remove_by_index(0)
		assert lista.viewList() == ['2021-03-05','2021-04-05','2021-05-05']

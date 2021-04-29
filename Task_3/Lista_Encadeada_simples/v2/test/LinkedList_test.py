from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.v2.LinkedList import LinkedList
import pytest
class Test_linkedList:

	def test_creation(self):
		lista = LinkedList()
		lista.Node_add('Eduarda', 0)
		assert lista.viewList() == ['Eduarda']
		assert lista.len_list == 1

	def test_index_lt_0(self):
		lista = LinkedList()
		with pytest.raises(ValueError):
			lista.Node_add('Eduarda', -1)

	def test_add(self):
		lista = LinkedList()
		lista.Node_add('p1', 0)
		lista.Node_add('p2', 1)
		lista.Node_add('p3', 2)
		lista.Node_add('p4', 5)
		assert lista.viewList() == ['p1','p2','p3','p4']
		assert lista.len_list == 4

	def test_sub_by_index(self):
		lista = LinkedList()
		lista.Node_add('p1', 0)
		lista.Node_add('p2', 1)
		lista.Node_add('p3', 2)
		lista.Node_add('p4', 5)
		lista.Node_remove_by_index(0)
		assert lista.viewList() == ['p2','p3','p4']
		assert lista.len_list == 3

	def test_sub_by_value(self):
		lista = LinkedList()
		lista.Node_add('p1', 0)
		lista.Node_add('p2', 1)
		lista.Node_add('p3', 2)
		lista.Node_add('p4', 5)
		lista.Node_remove_by_label('p1')
		assert lista.viewList() == ['p2','p3','p4']
		assert lista.len_list == 3

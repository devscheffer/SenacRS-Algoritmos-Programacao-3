from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

# TAD data
from Task_2.Class.controller import cls_Controller as tad_data

class Node:
	def __init__(self, data:str):
		label = tad_data()
		label.data = data
		self.__label = label  #nome Nodo
		self.__next = None    #ao inicializar o no nao tem ref para o proximo

	@property
	def label(self):
		return self.__label

	@label.setter
	def label(self, label):
		self.__label = label

	@property
	def next(self):
		return self.__next

	@next.setter
	def next(self, next):
		self.__next = next



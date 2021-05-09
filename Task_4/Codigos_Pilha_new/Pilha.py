from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.v2.LinkedList import LinkedList

class Pilha:

	def __init__(self):
		self.__pilha = LinkedList()

	@property
	def pilha(self):
		return self.__pilha
	@property
	def tamanho_pilha(self):
		return self.pilha.len_list


	def push(self, elemento):  # entrada desse método que a gente quer inserir
		self.pilha.Node_add(elemento,0)


	def pop(self):  # nao precisa do elemento como parâmetro que a remoção será sempre do início
		if not self.verificaPilhaVazia():  # so posso remover se tiver, pelo menos um elemento na pilha
			# porque eu ja sei que o tamnho da pilha está apontando p início dela
			self.pilha.Node_remove_by_index(0)


	def verificaPilhaVazia(self):
		if (self.tamanho_pilha == 0):  # tamanho da pilha for igual a zero - pilha vazia
			return True  # pilha vazia
		return False

	def mostraPilha_format_list(self):
		return self.pilha.viewList()

	def mostraPilha_format_stack(self):
		for i in self.mostraPilha_format_list():
			print(i)



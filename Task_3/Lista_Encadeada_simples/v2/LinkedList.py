from Task_3.Lista_Encadeada_simples.v2.No import Node
from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)


class LinkedList:
	def __init__(self):
		self.__first = None  # precisamos da ref para o primeiro nodo
		self.__last = None  # precisamos da ref para o ultimo nodo
		self.__len_list = 0  # variavel para retornar o tamanho da lista

# ========== getter and setter ==========
	@property
	def first(self):
		return self.__first

	@first.setter
	def first(self, first):
		self.__first = first

	@property
	def last(self):
		return self.__last

	@last.setter
	def last(self, last):
		self.__last = last

	@property
	def len_list(self):
		return self.__len_list

# ========== private methods ==========

	def __check_index(self, index):
		if index >= 0:
			return index
		else:
			raise ValueError('Valor invalido para index')

	def __index_first(self, node):
		"""Cria um node no inicio da fila.

		Args:
		node ([obj]): node que será colocado na fila
		"""
		node.next = self.first  # next_node será o antigo primeiro node
		self.first = node

	def __index_last(self, node):
		"""Cria um node no fim da fila.

		Args:
		node ([obj]): node que será colocado na fila
		"""
		self.last.next = node
		self.last = node

	def __index_middle(self, node, index):
		"""Cria um node na posição dada pelo index

		Args:
		node (obj): node que será colocado na fila
		index (int): posição na fila
		"""
		# seta o nodo corrente, como o proximo do no que estamos inserindo
		currentNode, previousNode = self.__find_node_by_index(index)
		node.next = currentNode
		# seta o node como proximo do anterior - ligando a lista novamente
		previousNode.next = node

	def __find_node_by_index(self, index):
		"""Encontra o node com o index dado

		Args:
		index (int): posição do node na fila

		Returns:
		[tuple]: currentNode,previousNode
		"""
		previousNode = self.first  # no anterior
		currentNode = self.first.next  # no atual
		currentIndex = 1  # indice auxiliar
		# informacoes guardadas, agora eu tenho o no anterior e o no atual
		# agora posso percorrer para inserir sem quebrar o encadeamento
		while(currentNode != None):
			# se estamos no lugar procurado, se o indice que estamos eh o indice onde queremos inserir
			if (currentIndex == index):  # encontramos o indice, o lugar onde queremos inserir
				return (currentNode, previousNode)
			# continuar percorrendo ate achar, andando na lista
			previousNode = currentNode
			currentNode = currentNode.next
			currentIndex += 1

	def __find_node_by_label(self, label):
		"""Encontra o node com o label dado

		Args:
		label (str): label unico do node

		Returns:
		[tuple]: currentNode,previousNode
		"""
		previousNode = self.first  # no anterior
		currentNode = self.first.next  # no atual
		# informacoes guardadas, agora eu tenho o no anterior e o no atual
		# agora posso percorrer para inserir sem quebrar o encadeamento
		while(currentNode != None):
			# se estamos no lugar procurado, se o indice que estamos eh o indice onde queremos inserir
			if (currentNode.label == label):  # encontramos o indice, o lugar onde queremos inserir
				return (currentNode, previousNode)
			# continuar percorrendo ate achar, andando na lista
			previousNode = currentNode
			currentNode = currentNode.next

	def __Node_remove_len_lt_2(self):
		if self.len_list == 0:
			raise IndexError('Lista não possui node para remover')
		elif self.len_list == 1:
			self.first == None
			self.last == None
			self.len_list == 0

# ========== public method ==========

	def Node_add(self, label, index):
		"""metodo para inserir nodos / informacoes da lista

		index = 0: insercao no INICIO
		index >= len_list: insercao no FINAL
		index between 1 and len_list: insercao na posicao do index

		Args:
		label (str): nome do no
		index (int): posição na fila

		Raises:
		ValueError: valor incorreto do indice
		"""
		try:
			index = self.__check_index(index)
			node = Node(label)  # node eh o no que eu estou criando
			if self.len_list == 0:
				# verifica se lista esta vazia
				# se estiver vazio, o no que esta sendo inserido será o 1 o ult
				self.first = node
				self.last = node
			else:
				if (index == 0):
					# 1 - se nao esta vazia, entao insercao no INICIO
					self.__index_first(node)
				elif (index >= self.len_list):
					# 2- insercao no FINAL
					self.__index_last(node)
				else:
					# 3 - insercao no MEIO , necessidade de:
					# percorrer e guardar o no atual e o anterior
					# um indice auxiliar
					self.__index_middle(node, index)
			# atualiza o tamanho da lista
			self.__len_list += 1
		except:
			raise ValueError()

	def Node_remove_by_index(self, index):
		index = self.__check_index(index)
		if self.len_list < 2:
			self.__Node_remove_len_lt_2()
		else:
			currentNode, previousNode = self.__find_node_by_index(index)
			previousNode.next = currentNode.next
			del currentNode

	def Node_remove_by_label(self, label):
		if self.len_list < 2:
			self.__Node_remove_len_lt_2()
		else:
			currentNode, previousNode = self.__find_node_by_label(label)
			previousNode.next = currentNode.next
			del currentNode

	def viewList(self):
		res = []
		currentNode = self.first
		while (currentNode != None):
			res.append(currentNode)
			print(currentNode.label, end="->")
			currentNode = currentNode.next
		return list(map(lambda x: x.label, res))



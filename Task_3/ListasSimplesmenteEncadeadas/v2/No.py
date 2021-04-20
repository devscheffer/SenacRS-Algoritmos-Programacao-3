class Node:
	def __init__(self, label:str):
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



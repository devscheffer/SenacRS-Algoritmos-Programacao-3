from os import getcwd
from sys import path

cwd = getcwd()
path.append(cwd)
from Task_7.components.binary_tree.cls_node import cls_node

# binary tree from node component


class cls_binary_tree:
	def __init__(self, data: int):
		self.__root: cls_node = cls_node(data)

	@property
	def root(self) -> cls_node:
		return self.__root

	@root.setter
	def root(self, data:int) -> None:
		self.__root = cls_node(data)

	def insert(self, data: int):
		self.root.insert(data)

	def print_tree_preorder(self) -> list[int] or str:
		if self.root is None:
			return "arvore vazia"
		current = self.root
		queue = [current]
		lst_tree: list[int] = []
		while len(queue) > 0:
			current = queue.pop(0)
			if current is None:
				continue
			if current.left is not None:
				queue.append(current.left)
			if current.right is not None:
				queue.append(current.right)
			lst_tree.append(current.data)
		return lst_tree

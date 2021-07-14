class cls_node:
	def __init__(self, data: int):
		self.data = data
		self.left = None
		self.right = None

	def __get_node(self, element):
		if isinstance(element, cls_node):
			return element
		if isinstance(element, dict):
			return cls_node(element)
		else:
			raise Exception('element is not cls_node or dict')

	def mtd_insert(self, data)-> None:
		new_node = self.__get_node(data)
		if self.left is None:
			self.left = new_node
		else:
			self.right = new_node

	def mtd_dct_leaf_path_Preorder(self, path:list=[], dct_res:dict={})->dict:
		if self.left is None and self.right is None:
			lst_binary = list(map(str, (path.copy())))
			path_binary = "".join(lst_binary)
			dct_res[self.data['char']] = {
				"frequency": self.data['frequency'],
				"path_binary":path_binary
				}
			return dct_res
		else:
			if self.left is not None:
				path.append(0)
				self.left.mtd_dct_leaf_path_Preorder(path, dct_res)
				path.pop()
			if self.right is not None:
				path.append(1)
				self.right.mtd_dct_leaf_path_Preorder(path, dct_res)
				path.pop()
		return dct_res

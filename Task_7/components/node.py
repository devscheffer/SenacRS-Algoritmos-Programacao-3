class cls_node:
	def __init__(self, data: int):
		self.data = data
		self.left = None
		self.right = None

	def __get_element_value(self, element) -> int:
		if isinstance(element, cls_node):
			element_value = element
		else:
			element_value = cls_node(element)
		return element_value

	def insert(self, data: int):
		new_node=self.__get_element_value(data)
		if self.left is None:
			self.left = new_node
		else:
			self.right = new_node


	def mtd_dct_leaf_path_Preorder(self,path=[],dct_res={}):
		if self.left is None and self.right is None:
			dct_res[self.data]=path.copy()
			return dct_res
		else:
			if self.left is not None:
				path.append(0)
				self.left.mtd_dct_leaf_path_Preorder(path,dct_res)
				path.pop()
			if self.right is not None:
				path.append(1)
				self.right.mtd_dct_leaf_path_Preorder(path,dct_res)
				path.pop()
		return dct_res



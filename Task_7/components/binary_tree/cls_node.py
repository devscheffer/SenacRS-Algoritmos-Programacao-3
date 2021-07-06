# Create node for a binary tree
class cls_node:
	def __init__(self, data: int):
		self.data = data
		self.left = None
		self.right = None

	def insert(self, data: int):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = cls_node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = cls_node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data



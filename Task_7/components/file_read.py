from os import getcwd



class cls_read_file:
	def __init__(self,file_name,path_rel = 'Task_7/data/input'):
		self.file_name = file_name
		self.path_rel = path_rel
		self.file_path = f'{getcwd()}/{path_rel}/{file_name}'

	def read_file(self):
		try:
			with open(f'{self.file_path}',mode='r') as file:
				f = file.readlines()
				return ''.join(f)
		except FileNotFoundError:
			return 'File not found'

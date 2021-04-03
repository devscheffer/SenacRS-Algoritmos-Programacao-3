from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.cls.Date_Struct import cls_Date_Struct
class cls_Controller:
	def __init__(self):
		self.obj_data=cls_Date_Struct()

	def mtd_Ler_Data(self,yyyy_mm_dd:str):
		lst_data=yyyy_mm_dd.split(sep='-')
		lst_data=list(map(int,lst_data))
		self.obj_data.ano=lst_data[0]
		self.obj_data.mes=lst_data[1]
		self.obj_data.dia=lst_data[2]

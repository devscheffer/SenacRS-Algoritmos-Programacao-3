import os,sys
cwd=os.getcwd()
sys.path.append(cwd)

from task_2.fn.fn_aux import fn_check_ano,fn_check_mes,fn_check_dia

class cls_Date_Struct:
	def __init__(self,dia:int,mes:int,ano:int):
		self.dia=dia
		self.mes=mes
		self.ano=ano

	@property
	def dia(self):
		return self.__dia

	@dia.setter
	def dia(self,value):
		dia_new=fn_check_dia(value)
		self.__dia=dia_new

	@property
	def mes(self):
		return self.__mes

	@mes.setter
	def mes(self,value):
		mes_new=fn_check_mes(value)
		self.__mes=mes_new

	@property
	def ano(self):
		return self.__ano

	@ano.setter
	def ano(self,value):
		ano_new=fn_check_ano(value)
		self.__ano=ano_new


import os,sys
cwd = os.getcwd()
sys.path.append(cwd)
from task_2.fn.fn_aux import fn_check_ano, fn_check_mes, fn_check_dia


class cls_Date_Struct:
	def __init__(self, dia: int, mes: int, ano: int):
		self.dia = dia
		self.mes = mes
		self.ano = ano

	@property
	def dia(self):
		return self.__dia

	@dia.setter
	def dia(self, value: int) -> int:
		dia_new = fn_check_dia(value)
		self.__dia = dia_new

	@property
	def mes(self):
		return self.__mes

	@mes.setter
	def mes(self, value: int) -> int:
		mes_new = fn_check_mes(value)
		self.__mes = mes_new

	@property
	def ano(self):
		return self.__ano

	@ano.setter
	def ano(self, value: int) -> int:
		ano_new = fn_check_ano(value)
		self.__ano = ano_new

	def mtd_Inicializar_Data(self) -> int:
		print(f'Ano: {self.ano}')
		print(f'Mes: {self.mes}')
		print(f'Dia: {self.dia}')
		data = f'{self.ano:04d}{self.mes:02d}{self.dia:02d}'
		data = int(data)
		print(data)
		return data

	def mtd_Acrescentar_Dias(self, value:int):
		"""Adiciona quantidade de dias a data

		Args:
			value (int): [description]
		"""
		ano_dias = 31*12
		dia = (value % ano_dias) % 31
		mes = (value % ano_dias)//31
		ano = value//ano_dias
		self.dia = self.dia+dia
		self.mes = self.mes+mes
		self.ano = self.ano+ano

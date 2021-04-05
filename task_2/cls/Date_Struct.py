from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.fn.Auxiliar import fn_check_day, fn_check_month, fn_check_year

class cls_Date_Struct:
	def __init__(self
	, year: int = -999
	, month: int = -999
	, day: int = -999
	):
		self.year = year
		self.month = month
		self.day = day

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, year: int) -> int:
		self.__year = fn_check_year(year)

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, month: int) -> int:
		self.__month = fn_check_month(month)


	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, day: int) -> int:
		self.__day = fn_check_day(year=self.year,month=self.month,day=day)

'''
	@property
	def data(self):
		return self.mtd_Inicializar_Data()

	@property
	def data_extenso(self):
		return self.mtd_Escrever_Extenso()

'''

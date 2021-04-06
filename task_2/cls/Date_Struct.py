from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from task_2.fn.auxiliar import fn_check_day, fn_check_month, fn_check_year, fn_Inicializar_Data


class cls_Date_Struct:
	def __init__(self, year: int = -999, month: int = -999, day: int = -999
				 ):
		self.year = year
		self.month = month
		self.day = day

	@property
	def year(self):
		return self.__year

	@year.setter
	def year(self, year: int) -> None:
		self.__year = fn_check_year(year)

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, month: int) -> None:
		self.__month = fn_check_month(month)

	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, day: int) -> None:
		self.__day = fn_check_day(year=self.year, month=self.month, day=day)

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self):
		self.__data = fn_Inicializar_Data(
			year=self.year, month=self.month, day=self.day)

	def mtd_Inicializar_Data(self, year: int, month: int, day: int) -> int:
		self.year = year
		self.month = month
		self.day = day
		res = fn_Inicializar_Data(year=year, month=month, day=day)
		return res

from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)


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
		if len(str(year)) == 4 or year == -999:
			print(f"year {year}")
			self.__year = year
		else:
			raise ValueError('Valor {year} incorreto para o ano')

	@property
	def month(self):
		return self.__month

	@month.setter
	def month(self, month: int) -> int:
		if int(month) in range(1, 13) or month == -999:
			print(f"month {month}")
			self.__month = month
		else:
			raise ValueError('Valor {month} incorreto para o mes')

	@property
	def day(self):
		return self.__day

	@day.setter
	def day(self, day: int) -> int:
		if int(day) in range(1, 32) or day == -999:
			print(f"day {day}")
			self.__day = day
		else:
			raise ValueError('Valor {day} incorreto para o dia')
'''
	@property
	def data(self):
		return self.mtd_Inicializar_Data()

	@property
	def data_extenso(self):
		return self.mtd_Escrever_Extenso()

'''

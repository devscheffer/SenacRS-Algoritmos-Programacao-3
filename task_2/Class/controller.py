from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_2.Function.auxiliar import fn_check_year, fn_days_to_add, fn_lst_Data, fn_leap, fn_Escrever_Extenso, fn_check_month, fn_check_day
from Task_2.Class.date_struct import cls_Date_Struct


class cls_Controller:
	def __init__(self, year: int = -999, month: int = -999, day: int = -999, data: str = '9999-01-01'):
		self.obj_data = cls_Date_Struct(year, month, day)
		self.data = data

	def mtd_Pascoa(self, year: int) -> str:
		year = str(year).split('-')[0]
		year = int(year)
		year = fn_check_year(year)
		g = year % 19
		e = 0
		c = year//100
		h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
		i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
		j = (year + year//4 + i + 2 - c + c//4) % 7
		p = i - j + e
		d = 1 + (p + 27 + (p + 6)//40) % 31
		m = 3 + (p + 26)//30
		return (f'{int(year)}-{int(m):02d}-{int(d):02d}')

	@property
	def data(self):
		return self.__data

	@data.setter
	def data(self, data: str) -> None:
		dict_data = fn_lst_Data(data)
		self.obj_data.year = dict_data['year']
		self.obj_data.month = dict_data['month']
		self.obj_data.day = dict_data['day']

	def mtd_Ler_Data(self, data: str) -> None:
		try:
			self.data = data
		except:
			raise ValueError('Data incorreta \nUtilizar o padrão yyyy-mm-dd')

	def __mtd_data_input(self, data: str) -> dict:
		dict_data = fn_lst_Data(data)
		year = dict_data['year']
		month = dict_data['month']
		day = dict_data['day']
		fn_check_year(year=year)
		fn_check_month(month=month)
		fn_check_day(year=year, month=month, day=day)
		return dict_data

	def mtd_Validar_Data(self, data: str) -> int:
		try:
			self.__mtd_data_input(data=data)
			return int(True)
		except:
			return int(False)

	def mtd_Verificar_Bissexto(self) -> bool:
		return fn_leap(self.obj_data.year)

	def mtd_Escrever_Extenso(self, data: str) -> bool:
		try:
			dict_data = self.__mtd_data_input(data=data)
			year = dict_data['year']
			month = dict_data['month']
			day = dict_data['day']
			fn_Escrever_Extenso(year=year, month=month, day=day)
			return int(True)
		except:
			return int(False)

	def mtd_Days_to_Add(self, days_to_add: int) -> bool:
		try:
			year = self.obj_data.year
			month = self.obj_data.month
			day = self.obj_data.day
			y, m, d = fn_days_to_add(days_to_add=days_to_add, year=year, month=month, day=day)
			self.data = f'{y}-{m}-{d}'
			print(self.data)
			return int(True)
		except:
			return int(False)

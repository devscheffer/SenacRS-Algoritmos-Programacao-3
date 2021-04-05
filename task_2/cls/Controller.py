from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.cls.Date_Struct import cls_Date_Struct
from task_2.fn.Auxiliar import fn_check_year
class cls_Controller:
	def __init__(self
	, year: int = -999
	, month: int = -999
	, day: int = -999
	):
		self.obj_data=cls_Date_Struct(year,month,day)

	def mtd_Pascoa(self,year:int)->str:
		year=str(year).split('-')[0]
		year=int(year)
		year=fn_check_year(year)
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

	def mtd_Ler_Data(self,yyyy_mm_dd:str)->None:
		lst_data=yyyy_mm_dd.split(sep='-')
		lst_data=list(map(int,lst_data))
		self.obj_data.year=lst_data[0]
		self.obj_data.month=lst_data[1]
		self.obj_data.day=lst_data[2]

	def mtd_Verificar_Bissexto(self)->int:
		return fn_leap(self.year)


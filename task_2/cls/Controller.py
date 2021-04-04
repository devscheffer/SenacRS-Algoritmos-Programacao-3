from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.cls.Date_Struct import cls_Date_Struct
from task_2.fn.fn_aux import fn_check_ano, fn_leap
class cls_Controller:
	def __init__(self):
		self.obj_data=cls_Date_Struct()

	def mtd_Ler_Data(self,yyyy_mm_dd:str)->None:
		lst_data=yyyy_mm_dd.split(sep='-')
		lst_data=list(map(int,lst_data))
		self.obj_data.ano=lst_data[0]
		self.obj_data.mes=lst_data[1]
		self.obj_data.dia=lst_data[2]

	def mtd_Verificar_Bissexto(self)->int:
		return fn_leap(self.ano)

	def mtd_Pascoa(self,ano)->str:
		ano=str(ano).split('-')[0]
		ano=int(ano)
		ano=fn_check_ano(ano)
		g = ano % 19
		e = 0
		c = ano//100
		h = (c - c//4 - (8*c + 13)//25 + 19*g + 15) % 30
		i = h - (h//28)*(1 - (h//28)*(29//(h + 1))*((21 - g)//11))
		j = (ano + ano//4 + i + 2 - c + c//4) % 7
		p = i - j + e
		d = 1 + (p + 27 + (p + 6)//40) % 31
		m = 3 + (p + 26)//30
		return (f'{int(ano)}-{int(m):02d}-{int(d):02d}')

from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
# from task_2.fn.fn_aux import fn_date_add


class cls_Date_Struct:
	def __init__(self, dia: int = -999, mes: int = -999, ano: int = -999):
		self.ano = ano
		self.mes = mes
		self.dia = dia

	@property
	def ano(self):
		return self.__ano

	@ano.setter
	def ano(self, ano: int) -> int:
		if len(str(ano)) == 4 or ano == -999:
			print(f"Ano {ano}")
			self.__ano = ano
		else:
			raise ValueError('Valor {ano} incorreto para o ano')

	@property
	def mes(self):
		return self.__mes

	@mes.setter
	def mes(self, mes: int) -> int:
		if int(mes) in range(1, 13) or mes == -999:
			print(f"Mes {mes}")
			self.__mes = mes
		else:
			raise ValueError('Valor {mes} incorreto para o mes')

	@property
	def dia(self):
		return self.__dia

	@dia.setter
	def dia(self, dia: int) -> int:
		if int(dia) in range(1, 32) or dia == -999:
			print(f"Dia {dia}")
			self.__dia = dia
		else:
			raise ValueError('Valor incorreto para o dia')

	@property
	def data(self):
		return self.mtd_Inicializar_Data()

	@property
	def data_extenso(self):
		return self.mtd_Escrever_Extenso()

	def mtd_Inicializar_Data(self) -> int:
		print(f'Ano: {self.ano}')
		print(f'Mes: {self.mes}')
		print(f'Dia: {self.dia}')
		data = f'{self.ano:04d}{self.mes:02d}{self.dia:02d}'
		data = int(data)
		print(data)
		return data

	def mtd_Acrescentar_Dias(self, value: int):
		add_mes_dia = fn_date_add(value, self.ano)
		mes = add_mes_dia[0]
		dia = add_mes_dia[1]
		ano = add_mes_dia[2]
		self.dia = dia
		self.mes = mes
		self.ano = ano

	def mtd_Escrever_Extenso(self):
		mes_name = fn_mes_int_to_str(self.mes)
		data_extenso = f'{self.dia} de {mes_name.capitalize()} de {self.ano}'
		return data_extenso

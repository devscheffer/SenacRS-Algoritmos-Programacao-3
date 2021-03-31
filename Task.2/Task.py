class cls_data:
	def __init__(self,dia,mes,ano):
		self.dia=dia
		self.mes=mes
		self.ano=ano

	def fn_check_ano(self):
		if len(self.ano)!=4:
			return self.ano
		else:
			self.ano=input('Tente novamente o ano')
			return fn_check_ano(self)

	def fn_check_mes(self):
		if int(self.mes) in range(1,13):
			return self.mes
		else:
			self.mes=input('Tente novamente o mes')
			return fn_check_mes(self)

	def fn_check_dia(self):
		if int(self.dia) in range(1,31):
			return self.dia
		else:
			self.dia=input('Tente novamente o dia')
			return fn_check_dia(self)



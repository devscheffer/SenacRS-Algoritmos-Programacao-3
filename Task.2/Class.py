from Task.2.Check import fn_check_ano,fn_check_mes,fn_check_dia

class cls_data:
	def __init__(self,dia,mes,ano):
		self.ano=fn_check_ano(ano)
		self.mes=fn_check_mes(mes)
		self.dia=fn_check_dia(dia)

	def fn_(self):
		print(self.dia,self.mes,self.ano)


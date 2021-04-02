def fn_check_ano(ano):
	if len(str(ano)) == 4:
		print(f"Ano {ano}")
		return ano
	else:
		raise ValueError('Valor incorreto')

def fn_check_mes(mes):
	if int(mes) in range(1, 13):
		print(f"Mes {mes}")
		return mes
	else:
		raise ValueError('Valor incorreto')

def fn_check_dia(dia):
	if int(dia) in range(1, 32):
		print(f"Dia {dia}")
		return dia
	else:
		raise ValueError('Valor incorreto')


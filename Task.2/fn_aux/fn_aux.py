def fn_check_ano(ano):
		if len(ano)!=4:
			return ano
		else:
			ano=input('Tente novamente o ano')
			return fn_check_ano()

def fn_check_mes(mes):
	if int(mes) in range(1,13):
		return mes
	else:
		mes=input('Tente novamente o mes')
		return fn_check_mes()

def fn_check_dia(dia):
	if int(dia) in range(1,31):
		return dia
	else:
		dia=input('Tente novamente o dia')
		return fn_check_dia()

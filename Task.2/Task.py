def fn_check_ano(ano):
	if len(ano)!=4:
		return ano
	else:
		new_input=input('Tente novamente o ano')
		return fn_check_ano(new_input)


def fn_check_mes(mes):
	if int(mes) in range(1,13):
		return mes
	else:
		new_input=input('Tente novamente o mes')
		return fn_check_mes(new_input)

def fn_check_dia(dia):
	if int(dia) in range(1,31):
		return dia
	else:
		new_input=input('Tente novamente o dia')
		return fn_check_dia(new_input)

ano=fn_check_ano(input('ano'))
mes=fn_check_mes(input('mes'))
dia=fn_check_dia(input('dia'))

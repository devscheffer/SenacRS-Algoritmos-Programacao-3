def fn_check_ano(ano):
	if len(str(ano)) == 4 or ano==0:
		print(f"Ano {ano}")
		return ano
	else:
		raise ValueError('Valor incorreto ano')

def fn_check_mes(mes):
	if int(mes) in range(1, 13) or mes==0:
		print(f"Mes {mes}")
		return mes
	else:
		raise ValueError('Valor incorreto mes')

def fn_check_dia(dia):
	if int(dia) in range(1, 32) or dia==0:
		print(f"Dia {dia}")
		return dia
	else:
		raise ValueError('Valor incorreto dia')

def fn_mes_int_to_str(value):
	dct_mes = {
	1:'janeiro'
	,2:'fevereiro'
	,3:'março'
	,4:'abril'
	,5:'maio'
	,6:'junho'
	,7:'julho'
	,8:'agosto'
	,9:'outubro'
	,10:'novembro'
	,11:'setembro'
	,12:'dezembro'
}
	return dct_mes[value]



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

def fn_mes_int_to_str(value:int)->str:
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

def fn_leap(ano)->int:
	ano=ano
	res = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
	return int(res)

def fn_dias_mes(mes:int, ano:int)->int:
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if mes == 2:
        if fn_leap(ano):
            return 29
        return 28
    return 30

def fn_dias_ano(ano:int)->int:
	total=0
	for i in range(1,13):
		total=total+fn_dias_mes(i,ano)
	return total
def fn_dias_passado_ano(ano,mes,dia):
	total=0
	for i in range(1,mes+1):
		total += fn_dias_mes(i,ano)
	total=total-fn_dias_mes(mes,ano)+dia
	return total

def fn_date_add(dias:int,ano:int,mes:int)->list:
	# ano=2020
	# mes=2
	# dia=1
	# dias=366
	ano=ano
	mes=mes
	dia=1
	dias=dias
	add_dia = dias
	add_ano=0


	dias_ano=fn_dias_ano(ano+add_ano)
	while add_dia+fn_dias_passado_ano(ano,mes,dia) > dias_ano:
		dias_ano=fn_dias_ano(ano+add_ano)
		if add_dia+fn_dias_passado_ano(ano,mes,dia) > dias_ano:
			add_dia = add_dia-dias_ano+fn_dias_passado_ano(ano,mes,dia)
			add_ano+=1
	add_mes=0
	dias_mes=fn_dias_mes(mes+add_mes,ano+add_ano)
	while add_dia > dias_mes:
		dias_mes=fn_dias_mes(mes+add_mes,ano+add_ano)
		if add_dia > dias_mes:
			add_dia = add_dia-dias_mes
			add_mes+=1
	return [ano+add_ano,mes+add_mes,dia+add_dia]
# fn_date_add(1,1,1)

def fn_date_sub(ano:int,mes:int,dia:int,dias:int)->list:
	ano=ano
	mes=mes
	dia=dia
	dias=dias
	# ano=2020
	# mes=1
	# dia=1
	# dias=-1
	sub_ano=0
	dias_passados=fn_dias_passado_ano(ano,mes,dia)
	while abs(dias) >= dias_passados:
		if abs(dias) >= dias_passados:
			dias=dias + dias_passados
			sub_ano+=1
	dias_total=fn_dias_ano(ano-sub_ano)+dias

	lista=fn_date_add(dias_total,ano,mes)
	a=lista[0]
	sub_mes=lista[1]
	sub_dia=lista[2]
	return [ano-sub_ano,sub_mes,sub_dia]

print(fn_date_sub(1,1,1,1))

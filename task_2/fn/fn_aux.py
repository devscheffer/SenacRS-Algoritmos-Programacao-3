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

def fn_mes_int_to_str(value: int) -> str:
    dct_mes = {
          1: 'janeiro'
		, 2: 'fevereiro'
		, 3: 'março'
		, 4: 'abril'
		, 5: 'maio'
		, 6: 'junho'
		, 7: 'julho'
		, 8: 'agosto'
		, 9: 'outubro'
		, 10: 'novembro'
		, 11: 'setembro'
		, 12: 'dezembro'
    }
    return dct_mes[value]


def fn_leap(ano) -> int:
    ano = ano
    res = ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0)
    return int(res)


def fn_days_in_year(ano: int) -> int:
    return 365+fn_leap(ano)


def fn_days_in_month(mes: int, ano: int) -> int:
    if mes in {1, 3, 5, 7, 8, 10, 12}:
        return 31
    if mes == 2:
        return 28+fn_leap(ano)
    return 30


def fn_days_passed_in_year(ano, mes, dia):
    days_passed = 0
    for i in range(1, mes):
        days_passed += fn_days_in_month(i, ano)
    days_passed += dia
    return days_passed


'''
[todo]: Corrigir adiconar data
Usar dias passado + dias > 0
se negativo
se positivo
'''


def fn_days_to_add(days_to_add: int, year: int, month: int, day: int) -> list:
    days_rest = fn_days_passed_in_year(year, month, day)+days_to_add
    add_year = 0
    if days_rest > fn_days_in_year(year+add_year) and days_rest > 0:
        days_rest -= fn_days_in_year(year)
        add_year += 1
    if abs(days_rest) > fn_days_in_year(year+add_year) and days_rest <= 0:
        days_rest += fn_days_in_year(year)
        add_year -= 1

    add_month = 0
    days_rest = days_rest
    if days_rest > fn_days_in_month(month+add_month, year+add_year) and days_rest > 0:
        days_rest -= fn_days_in_month(month+add_month, year+add_year)
        add_month += 1
    if abs(days_rest) > fn_days_in_month(month+add_month, year+add_year) and days_rest <= 0:
        days_rest += fn_days_in_month(month+add_month, year+add_year)
        add_month -= 1

    add_day = days_rest-fn_days_passed_in_year(year, month, day)
    return [year+add_year, month+add_month, day+add_day]


print(fn_days_to_add(5, 2020, 1, 1))

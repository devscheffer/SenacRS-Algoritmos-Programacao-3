def fn_leap(year) -> int:
	year = year
	res = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	return int(res)

def fn_days_in_month(month: int, year: int) -> int:
	if month in {1, 3, 5, 7, 8, 10, 12}:
		return 31
	if month == 2:
		return 28+fn_leap(year)
	return 30

def fn_check_year( year: int) -> int:
	if len(str(year)) == 4 or year == -999:
		print(f"year: {year}")
		return year
	else:
		raise ValueError('Valor [{year}] incorreto para o year')

def fn_check_month( month: int) -> int:
	if int(month) in range(1, 13) or month == -999:
		print(f"month: {month}")
		return month
	else:
		raise ValueError('Valor [{month}] incorreto para o month')

def fn_check_day( year:int,month:int,day: int) -> int:
	if int(day) in range(1, fn_days_in_month(month,year)+1) or day == -999:
		print(f"Dia: {day}")
		return day
	else:
		raise ValueError('Valor [{day}] incorreto para o dia')
'''
def mtd_Inicializar_Data(self) -> int:
	print(f'year: {self.year}')
	print(f'month: {self.month}')
	print(f'Dia: {self.dia}')
	data = f'{self.year:04d}{self.month:02d}{self.dia:02d}'
	data = int(data)
	print(data)
	return data

def mtd_Acrescentar_Dias(self, value: int):
	add_month_dia = fn_date_add(value, self.year)
	month = add_month_dia[0]
	dia = add_month_dia[1]
	year = add_month_dia[2]
	self.dia = dia
	self.month = month
	self.year = year

def mtd_Escrever_Extenso(self):
	month_name = fn_month_int_to_str(self.month)
	data_extenso = f'{self.dia} de {month_name.capitalize()} de {self.year}'
	return data_extenso

def fn_month_int_to_str(value: int) -> str:
	dct_month = {
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
	return dct_month[value]





def fn_days_in_year(year: int) -> int:
	return 365+fn_leap(year)





def fn_days_passed_in_year(year, month, dia):
	days_passed = 0
	for i in range(1, month):
		days_passed += fn_days_in_month(i, year)
	days_passed += dia
	return days_passed
'''

'''
[todo]: Corrigir adiconar data
Usar dias passado + dias > 0
se negativo
se positivo
'''
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
'''

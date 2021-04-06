def fn_leap(year) -> int:
	year = year
	res = year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)
	return int(res)


def fn_days_in_year(year: int) -> int:
	return 365+fn_leap(year)


def fn_days_in_month(month: int, year: int) -> int:
	if month in {1, 3, 5, 7, 8, 10, 12}:
		return 31
	if month == 2:
		return 28+fn_leap(year)
	return 30


def fn_check_year(year: int) -> int:
	if len(str(year)) == 4 or year == -999:
		print(f"year: {year}")
		return year
	else:
		raise ValueError('Valor [{year}] incorreto para o year')


def fn_check_month(month: int) -> int:
	if int(month) in range(1, 13) or month == -999:
		print(f"month: {month}")
		return month
	else:
		raise ValueError('Valor [{month}] incorreto para o month')


def fn_check_day(year: int, month: int, day: int) -> int:
	if int(day) in range(1, fn_days_in_month(month, year)+1) or day == -999:
		print(f"Dia: {day}")
		return day
	else:
		raise ValueError('Valor [{day}] incorreto para o dia')


def fn_Inicializar_Data(year: int, month: int, day: int) -> int:
	print(f'year: {year}')
	print(f'month: {month}')
	print(f'Dia: {day}')
	data = f'{year:04d}{month:02d}{day:02d}'
	data = int(data)
	print(data)
	return data


def fn_lst_Data(data: str) -> dict:
	lst_key = ['year', 'month', 'day']
	lst_data = data.split(sep='-')
	lst_data = list(map(int, lst_data))
	dict_data = dict(zip(lst_key, lst_data))
	return dict_data


def fn_month_int_to_str(month_number: int) -> str:
	dct_month = {
		1: 'janeiro', 2: 'fevereiro', 3: 'março', 4: 'abril', 5: 'maio', 6: 'junho', 7: 'julho', 8: 'agosto', 9: 'outubro', 10: 'novembro', 11: 'setembro', 12: 'dezembro'
	}
	return dct_month[month_number]


def fn_Escrever_Extenso(year, month, day):
	month_name = fn_month_int_to_str(month)
	data_extenso = f'{day} de {month_name.capitalize()} de {year}'
	return data_extenso


def fn_days_passed_in_year(year, month, day):
	days_passed = 0
	for i in range(1, month):
		days_passed += fn_days_in_month(i, year)
	days_passed += day
	return days_passed


def fn_add_year(days: int, year: int) -> list:
	add_year = 0
	while days > fn_days_in_year(year+add_year) or days <= 0:
		if days > 0:
			add_year += 1
			days -= fn_days_in_year(year+add_year-1)
		if days <= 0:
			add_year -= 1
			days += fn_days_in_year(year+add_year)
	return [days, add_year]


def fn_add_month(days, year):
	add_month = 0
	while days > fn_days_in_month(1+add_month, year) or days <= 0:
		if days > 0:
			days -= fn_days_in_month(1+add_month, year)
			add_month += 1
		if days <= 0:
			days += fn_days_in_month(1+add_month, year)
			add_month -= 1
	else:
		add_month += 1
	return [days, add_month]


def fn_days_to_add(days_to_add: int, year: int, month: int, day: int) -> list:
	days = days_to_add+fn_days_passed_in_year(year, month, day)
	days, add_year = fn_add_year(days, year)
	days, add_month = fn_add_month(days, year+add_year)
	add_day = days
	return [year+add_year, add_month, add_day]


'''
def mtd_Acrescentar_Dias(self, value: int):
	add_month_dia = fn_date_add(value, self.year)
	month = add_month_dia[0]
	dia = add_month_dia[1]
	year = add_month_dia[2]
	self.dia = dia
	self.month = month
	self.year = year


'''

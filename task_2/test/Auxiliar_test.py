from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from task_2.fn.auxiliar import fn_days_passed_in_year, fn_days_to_add, fn_leap, fn_days_in_month, fn_Inicializar_Data, fn_Escrever_Extenso, fn_days_in_year


class Test_fn_leap:
	def test_leap_true(self):
		assert fn_leap(2020) == True

	def test_leap_false(self):
		assert fn_leap(2021) == False


class Test_fn_days_in_month:
	def test_month_fev(self):
		assert fn_days_in_month(month=2, year=2021) == 28

	def test_month_fev_leap(self):
		assert fn_days_in_month(month=2, year=2020) == 29


class Test_fn_Inicializar_Data:
	def test_data(self):
		assert fn_Inicializar_Data(year=2020, month=1, day=2) == 20200102


class Test_fn_Escrever_Extenso:
	def test_1(self):
		assert fn_Escrever_Extenso(
			year=2020, month=1, day=1) == '1 de Janeiro de 2020'


class Test_fn_Acrescentar_Dias:
	def test_fn_days_in_year(self):
		assert fn_days_in_year(2020) == 366
		assert fn_days_in_year(2021) == 365

	def test_fn_days_passed_in_year(self):
		res1 = fn_days_passed_in_year(year=2021, month=1, day=1)
		assert res1 == 1
		res2 = fn_days_passed_in_year(year=2021, month=3, day=1)
		assert res2 == 60

	def test_fn_days_to_add(self):
		assert fn_days_to_add(1, 2021, 1, 1) == [2021, 1, 2]
		assert fn_days_to_add(5, 2021, 1, 1) == [2021, 1, 6]
		assert fn_days_to_add(37, 2021, 1, 1) == [2021, 2, 7]
		assert fn_days_to_add(500, 2020, 5, 3) == [2021, 9, 15]

	def test_fn_days_to_sub(self):
		assert fn_days_to_add(-1, 2021, 1, 1) == [2020, 12, 31]
		assert fn_days_to_add(-366, 2021, 1, 1) == [2020, 1, 1]
		assert fn_days_to_add(-759, 2021, 1, 1) == [2018, 12, 4]
		assert fn_days_to_add(-500, 2020, 5, 3) == [2018, 12, 20]

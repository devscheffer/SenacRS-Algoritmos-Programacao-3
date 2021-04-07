from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_2.Class.controller import cls_Controller
import pytest


class Test_mtd_Pascoa:
	def test_pascoa_1(self):
		obj = cls_Controller()
		assert obj.mtd_Pascoa(2021) == '2021-04-04'

	def test_pascoa_2(self):
		obj = cls_Controller()
		assert obj.mtd_Pascoa(2020) == '2020-04-12'


class Test_mtd_Ler_Data:
	def test_happy(self):
		res = cls_Controller()
		res.mtd_Ler_Data('2021-01-03')
		assert res.obj_data.year == 2021
		assert res.obj_data.month == 1
		assert res.obj_data.day == 3

	def test_wrong_year(self):
		res = cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('91-01-03')

	def test_wrong_month(self):
		res = cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('2021-15-03')

	def test_wrong_day(self):
		res = cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('2021-01-33')

	def test_wrong_data(self):
		res = cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('20210101')


class Test_mtd_Verificar_Bissexto:

	def test_leap_f(self):
		res = cls_Controller()
		res.mtd_Ler_Data('2021-01-03')
		assert res.mtd_Verificar_Bissexto() == 0

	def test_leap_t(self):
		res = cls_Controller()
		res.mtd_Ler_Data('2012-01-03')
		assert res.mtd_Verificar_Bissexto() == 1


class Test_mtd_Escrever_Extenso:
	def test_data_extenso(self):
		res = cls_Controller()
		assert res.mtd_Escrever_Extenso('2020-03-10') == 1

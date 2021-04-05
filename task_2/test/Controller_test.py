from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

import pytest
from task_2.cls.Controller import cls_Controller

class Test_Pascoa:
	def test_pascoa_1(self):
		obj=cls_Controller()
		assert obj.mtd_Pascoa(2021) == '2021-04-04'
	def test_pascoa_2(self):
		obj=cls_Controller()
		assert obj.mtd_Pascoa(2020) == '2020-04-12'

'''
class Test_mtd_Ler_Data:
	def test_happy(self):
		res=cls_Controller()
		res.mtd_Ler_Data('2021-01-03')
		assert res.obj_data.ano == 2021
		assert res.obj_data.mes == 1
		assert res.obj_data.dia == 3
	def test_wrong_ano(self):
		res=cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('91-01-03')
	def test_wrong_mes(self):
		res=cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('2021-15-03')
	def test_wrong_dia(self):
		res=cls_Controller()
		with pytest.raises(ValueError):
			res.mtd_Ler_Data('2021-01-33')

class Test_mtd_Verificar_Bissexto:

	def test_leap_f(self):
		res=cls_Controller()
		res.mtd_Ler_Data('2021-01-03')
		assert res.mtd_Verificar_Bissexto() == 0

	def test_leap_t(self):
		res=cls_Controller()
		res.mtd_Ler_Data('2012-01-03')
		assert res.mtd_Verificar_Bissexto() == 1

class Test_mtd_Pascoa:
	def test_(self):
		res=cls_Controller()
		assert res.mtd_Pascoa(2021)=='2021-04-04'
	def test_(self):
		res=cls_Controller()
		assert res.mtd_Pascoa('2021-1-1')=='2021-04-04'
'''

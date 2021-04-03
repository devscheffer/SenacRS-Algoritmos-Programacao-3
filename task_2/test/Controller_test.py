from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

import pytest
from task_2.cls.Controller import cls_Controller

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



from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.cls.Date_Struct import cls_Date_Struct
import pytest

class Test_cls_init:
	def test_init_value(self):
		obj = cls_Date_Struct(year= 2020,month=2,day=1)
		assert obj.year == 2020
		assert obj.month == 2
		assert obj.day == 1

	def test_init_none(self):
		obj = cls_Date_Struct()
		assert obj.year == -999
		assert obj.month == -999
		assert obj.day == -999

	def test_input_year(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(1, 2, 1)

	def test_input_month(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(1, 22, 2020)

	def test_input_day(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(-1, 2, 2020)


'''
class Test_mtd_Inicializar_Data:
	def test_return(self):
		res = cls_Date_Struct(1, 1, 1111)
		assert res.mtd_Inicializar_Data() == 11110101


class Test_mtd_Acrescentar_days:

	def test_add_day_lt_31(self):
		res = cls_Date_Struct(1, 1, 1111)
		res.mtd_Acrescentar_days(5)
		assert res.day == 6

	def test_add_day_gt_31(self):
		res = cls_Date_Struct(1, 1, 1111)
		res.mtd_Acrescentar_days(400)
		assert res.year == 1112
		assert res.month == 2
		assert res.day == 5

	def test_add_negative(self):
		res = cls_Date_Struct(1, 1, 2020)
		res.mtd_Acrescentar_days(-1)
		assert res.year == 1110
		assert res.month == 11
		assert res.day == 22
		assert res.data == 11101122

class Test_mtd_Escrever_Extenso:
	def test_data_extenso(self):
		res=cls_Date_Struct(10,3,2020)
		assert res.data_extenso == '10 de Março de 2020'

'''

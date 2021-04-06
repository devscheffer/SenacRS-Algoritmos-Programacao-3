from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
import pytest
from task_2.cls.date_struct import cls_Date_Struct


class Test_cls_init:
	def test_init_value(self):
		obj = cls_Date_Struct(year=2020, month=2, day=1)
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


class Test_mtd_Inicializar_Data:
	def test_return(self):
		res = cls_Date_Struct()
		assert res.mtd_Inicializar_Data(year=1111, month=1, day=1) == 11110101

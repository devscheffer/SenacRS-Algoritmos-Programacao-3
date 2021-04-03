from task_2.cls.Date_Struct import cls_Date_Struct
import pytest
import os
import sys
cwd = os.getcwd()
sys.path.append(cwd)


class Test_cls_init:
	def test_class_ini(self):
		res = cls_Date_Struct(1, 2, 1111)
		assert res.ano == 1111
		assert res.mes == 2
		assert res.dia == 1

	def test_ano(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(1, 2, 1)

	def test_mes(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(1, 22, 2020)

	def test_dia(self):
		with pytest.raises(ValueError):
			cls_Date_Struct(-1, 2, 2020)


class Test_mtd_Inicializar_Data:
	def test_return(self):
		res = cls_Date_Struct(1, 1, 1111)
		assert res.mtd_Inicializar_Data() == 11110101


class Test_mtd_Acrescentar_Dias:

	def test_add_dia_lt_31(self):
		res = cls_Date_Struct(1, 1, 1111)
		res.mtd_Acrescentar_Dias(5)
		assert res.dia == 6

	def test_add_dia_gt_31(self):
		res = cls_Date_Struct(1, 1, 1111)
		res.mtd_Acrescentar_Dias(400)
		assert res.ano == 1112
		assert res.mes == 1
		assert res.dia == 29

	def test_add_negative(self):
		res = cls_Date_Struct(1, 1, 1111)
		res.mtd_Acrescentar_Dias(-40)
		assert res.ano == 1110
		assert res.mes == 11
		assert res.dia == 23

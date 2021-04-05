from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from task_2.cls.Date_Struct import cls_Date_Struct
import pytest

class Test_cls_init:
	def test_class_ini(self):
		obj = cls_Date_Struct(1, 2, 2020)
		assert obj.ano == 2020
		assert obj.mes == 2
		assert obj.dia == 1

	def test_init_none(self):
		obj = cls_Date_Struct()
		assert obj.ano == -999
		assert obj.mes == -999
		assert obj.dia == -999

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
		assert res.mes == 2
		assert res.dia == 5

	def test_add_negative(self):
		res = cls_Date_Struct(1, 1, 2020)
		res.mtd_Acrescentar_Dias(-1)
		assert res.ano == 1110
		assert res.mes == 11
		assert res.dia == 22
		assert res.data == 11101122

class Test_mtd_Escrever_Extenso:
	def test_data_extenso(self):
		res=cls_Date_Struct(10,3,2020)
		assert res.data_extenso == '10 de Março de 2020'


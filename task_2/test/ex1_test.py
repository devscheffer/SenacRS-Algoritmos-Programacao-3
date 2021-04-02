import pytest
from task_2.cls.Date_Struct import cls_Date_Struct

def test_ano():
    with pytest.raises(ValueError):
        cls_Date_Struct(1, 2, 1)


def test_mes():
    with pytest.raises(ValueError):
        cls_Date_Struct(1, 22, 2020)


def test_dia():
    with pytest.raises(ValueError):
        cls_Date_Struct(-1, 2, 2020)

def test_class_ini():
	res=cls_Date_Struct(1,2,1111)
	assert res.ano == 1111
	assert res.mes == 2
	assert res.dia == 1
def test_mtd_1():
	res=cls_Date_Struct(1,1,1111)
	assert res.mtd_Inicializar_Data() == 11110101

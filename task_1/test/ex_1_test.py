from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_1.main.ex_1 import cls_Lampada, cls_Testa_Lampada

def test_cls():
    res = cls_Testa_Lampada(cls_Lampada("teste", "big"))

    assert res.status == "desligado"


def test_on():
    res = cls_Testa_Lampada(cls_Lampada("teste", "big"))
    res.mtd_switch()
    assert res.status == "ligado"

def test_off():
    res = cls_Testa_Lampada(cls_Lampada("teste", "big"))
    res.mtd_switch()
    res.mtd_switch()
    assert res.status == "desligado"

print('ok')

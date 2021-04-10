from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_1.main.ex_3 import cls_Aluno


def test_reprovado():
	res = cls_Aluno("gerson", 1, "ads", 5)
	res.mtd_check_is_approved()
	assert res.status == 'reprovado'

def test_aprovado():
	res = cls_Aluno("gerson", 1, "ads", 7)
	res.mtd_check_is_approved()
	assert res.status == 'aprovado'


from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
import pytest
from Task_1.main.ex_6 import cls_CD

@pytest.fixture
def obj():
	a=15
	res = cls_CD(a)
	return res

def test_start(obj):
	res = obj
	assert res.status == 'parado'

def test_play(obj):
	res = obj
	res.mtd_play()
	assert res.status == 'tocando'

def test_pause(obj):
	res = obj
	res.status = 'tocando'
	res.mtd_pause()
	assert res.status == 'parado'
	assert res.n_musica == 1

def test_stop(obj):
	res = obj
	res.mtd_stop()
	assert res.status == 'parado'
	assert res.n_musica == 1

def test_next(obj):
	res = obj
	res.mtd_next()
	assert res.n_musica == 2
	res.n_musica = res.qtd_musica
	res.mtd_next()
	assert res.n_musica == 1


def test_previous(obj):
	res = obj
	res.mtd_previous()
	assert res.n_musica == res.qtd_musica
	res.n_musica = 2
	res.mtd_previous()
	assert res.n_musica == 1

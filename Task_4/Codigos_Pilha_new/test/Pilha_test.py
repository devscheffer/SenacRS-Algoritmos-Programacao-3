from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_4.Codigos_Pilha_new.Pilha import Pilha

class Test_1:
	def test_prof(self):
		p = Pilha()
		p.push("Eduarda")
		p.mostraPilha_format_list()
		print("--------------")
		p.push("Senac")
		p.mostraPilha_format_list()
		print("--------------")
		p.push("FSPOA")
		p.mostraPilha_format_list()
		print("--------------")
		p.pop()
		p.mostraPilha_format_list()

class Test_basic:
	def test_create(self):
		p=Pilha()
		assert p.tamanho_pilha==0
		assert p.pilha.first==None
		assert p.pilha.last==None
		assert p.pilha.len_list==0

	def test_insert_1(self):
		p=Pilha()
		p.push('Senac')
		assert p.mostraPilha_format_list()==['Senac']
	def test_insert_3(self):
		p=Pilha()
		p.push('Eduarda')
		p.push('Senac')
		p.push('FSPOA')
		assert p.mostraPilha_format_list()==['FSPOA','Senac','Eduarda']
		assert p.tamanho_pilha==3
	def test_remove_1(self):
		p=Pilha()
		p.push('Eduarda')
		p.push('Senac')
		p.push('FSPOA')
		p.pop()
		assert p.mostraPilha_format_list()==['Senac','Eduarda']
		assert p.tamanho_pilha==2
	def test_remove_2(self):
		p=Pilha()
		p.push('Eduarda')
		p.push('Senac')
		p.push('FSPOA')
		p.pop()
		p.pop()
		assert p.mostraPilha_format_list()==['Eduarda']
		assert p.tamanho_pilha==1
	def test_remove_all(self):
		p=Pilha()
		p.push('Eduarda')
		p.push('Senac')
		p.push('FSPOA')
		p.pop()
		p.pop()
		p.pop()
		assert p.mostraPilha_format_list()==[]
		assert p.tamanho_pilha==0

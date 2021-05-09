from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_4.Codigos_Pilha.Pilha import Pilha

p = Pilha()

p.push("Eduarda")
p.mostraPilha()
print("--------------")
p.push("Senac")
p.mostraPilha()
print("--------------")
p.push("FSPOA")
p.mostraPilha()
print("--------------")
p.pop()
p.mostraPilha()

from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.v1.LinkedList import LinkedList

lista = LinkedList()
#print(lista)
lista.addNode('Eduarda', 0)
lista.viewList()

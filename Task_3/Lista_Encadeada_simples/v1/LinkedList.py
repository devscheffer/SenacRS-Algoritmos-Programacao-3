from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)
from Task_3.Lista_Encadeada_simples.v1.No import Node

class LinkedList:
    def __init__(self):
        self.first = None       #precisamos da ref para o primeiro nodo
        self.last = None        #precisamos da ref para o ultimo nodo
        self.len_list = 0      #variavel para retornar o tamanho da lista

    #metodo para inserir nodos / informacoes da lista
    def addNode(self, label, index):
        #precisamos criar um novo no
        if (index >= 0 ):  #nao pode ter indice negativo
            #criando novo no
            node = Node(label)  # node eh o no que eu estou criando
            print(node.getLabel())
        #verifica se lista esta vazia
        if self.empty(): #se estiver vazio, o no que esta sendo inserido será o 1 o ult
            self.first = node
            self.last = node
        else:
            # 1 - se nao esta vazia, entao insercao no INICIO
            if (index == 0):
                #inserindo no inicio
                node.setNext(self.first) # o prox do no que esta sendo criado e o primeiro
                #pronto, no criado -- precisamos dizer que ele é o primeiro
                self.first = node
                print(node.getLabel())
            #2- insercao no FINAL
            elif (index >= self.len_list):
                self.last.setNext(node)
                self.last = node
            #3 - insercao no MEIO , necessidade de:
                # percorrer e guardar o no atual e o anterior
                # um indice auxiliar
            else:
                previousNode = self.first                   #no anterior
                currentNode = self.first.getNext()          #no atual
                currentIndex = 1                            #indice auxiliar
                #informacoes guardadas, agora eu tenho o no anterior e o no atual
                #agora posso percorrer para inserir sem quebrar o encadeamento
                while(currentNode != None):

                    #se estamos no lugar procurado, se o indice que estamos eh o indice onde queremos inserir
                    if (currentIndex == index): #encontramos o indice, o lugar onde queremos inserir
                        #seta o nodo corrente, como o proximo do no que estamos inserindo
                        node.setNext(currentNode)
                        #seta o node como proximo do anterior - ligando a lista novamente
                        previousNode.setNext(node)


                    #continuar percorrendo ate achar, andando na lista
                    previousNode = currentNode
                    currentNode = currentNode.getNext()
                    currentIndex += 1

        #atualiza o tamanho da lista
        self.len_list += 1


    def viewList(self):
        currentNode = self.first
        while (currentNode != None):
            print(currentNode.getLabel(), end=" ")
            currentNode = currentNode.getNext()
        print(' ')

    def empty(self): #verifica se a lista esta vazia
        if (self.first == None):
            return True
        return False








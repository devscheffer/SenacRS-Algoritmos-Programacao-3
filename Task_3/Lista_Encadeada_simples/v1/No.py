class Node:
    def __init__(self, label):
        self.label = label  #nome Nodo
        self.next = None    #ao inicializar o no nao tem ref para o proximo
    
    def getLabel(self):
        return self.label
    
    def setLabel(self, label):
        self.label = label

    def getNext(self):
        return self.next
    
    def setNext(self, next):
        self.next = next

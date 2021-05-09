class Pilha:

    def __init__(self):
        self.pilha = []  # pilha
        self.tamanho_pilha = 0

    def push(self, elemento):  # entrada desse método que a gente quer inserir
        self.pilha.append(elemento)
        self.tamanho_pilha += 1

    def pop(self):  # nao precisa do elemento como parâmetro que a remoção será sempre do início
        if not self.verificaPilhaVazia():  # so posso remover se tiver, pelo menos um elemento na pilha
            # porque eu ja sei que o tamnho da pilha está apontando p início dela
            self.pilha.pop(self.tamanho_pilha - 1)
            self.tamanho_pilha -= 1

    def verificaPilhaVazia(self):
        if (self.tamanho_pilha == 0):  # tamanho da pilha for igual a zero - pilha vazia
            return True  # pilha vazia
        return False

    def mostraPilha(self):
        for e in reversed(self.pilha):
            print(e)


'''
Escreva uma classe “Lampada” as quais suas características referem-se à
- um modelo
- um supermercado.
'''

class Lampada:
    def __init__(self, modelo, mercado):
        self.modelo=modelo
        self.mercado=mercado
        self.status='desligado'

    def list_att(self):
        return [self.modelo,self.mercado]
'''
Após, crie uma classe “TestaLampada”
- onde os atributos são inicializados e mostrados na tela.
- desenvolva os métodos para ligar e desligar a lâmpada
'''

class Testa_Lampada:
    def __init__(self, Lampada):
        self.atributos=Lampada.list_att()
        self.status=Lampada.status
        print(self.atributos)

    def ligar(self):
        if self.status == 'desligado':
            self.status='ligado'
        else:
            self.status='desligado'
        print(self.status)

res=Testa_Lampada(Lampada('teste','big'))
res.ligar()

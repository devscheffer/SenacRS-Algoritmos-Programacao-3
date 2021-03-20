"""
Escreva uma classe “Lampada” as quais suas características referem-se à
- um modelo
- um supermercado.
"""
"""
Após, crie uma classe “TestaLampada”
- onde os atributos são inicializados e mostrados na tela.
- desenvolva os métodos para ligar e desligar a lâmpada
"""


class cls_Lampada:
    def __init__(self, modelo, mercado):
        self.modelo = modelo
        self.mercado = mercado
        self.status = "desligado"


class cls_Testa_Lampada:
    def __init__(self, Lampada):
        self.atributos = Lampada.__dict__
        self.status = Lampada.status
        print(self.atributos)

    def mtd_switch(self):
        if self.status == "desligado":
            self.status = "ligado"
        else:
            self.status = "desligado"
        print(self.status)

"""
Faça um programa em Python que contenha duas classes:
	b. Circulo:
		A área de cada um deles deve ser calculada e exibida na tela conforme descrição da classe Circulo definida abaixo.
		i. Atributo principal: raio.
		ii. Método: CalcularAreaCirculo, através da fórmula: raio * raio * PI
"""

"""
	a. TestaCirculo:
		- Três objetos da classe Circulo devem ser instanciados.
			- o primeiro objeto (c1) deve ter o raio igual a 1
			- o segundo (c2) igual a 0,25
			- o terceiro (c3) 125.
"""


class cls_circulo:
    def __init__(self, raio):
        self.raio = raio

    def mtd_Calcular_Area_Circulo(self):
        from math import pi

        area = (self.raio) ** 2 * pi
        print(f"Raio:{self.raio:.2f}")
        print(f"Area:{area:.2f}")


class cls_Testa_Circulo:
    def __init__(self, lst_Circulo):
        self.lst_Circulo = lst_Circulo
        self.dict_circulo = {}

    def mtd_test_circulo(self):
        for i in range(len(self.lst_Circulo)):
            self.dict_circulo[f"c{i}"] = cls_circulo(self.lst_Circulo[i])
            print(f"Circulo: C{i}")
            self.dict_circulo[f"c{i}"].mtd_Calcular_Area_Circulo()

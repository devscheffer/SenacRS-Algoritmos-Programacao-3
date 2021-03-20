"""
Crie uma classe chamada Quadrado, que será um modelo para construção de objetos que
armazenem dados de quadrados.
- Esta classe conterá um único atributo, que armazenará o
tamanho do lado do quadrado em centímetros.
- Além deste atributo, a classe conterá três métodos:
	- calcule e devolva a área do quadrado (dado por LADO²)
	- calcule e devolva o perímetro do quadrado (4 * LADO)
	- calcule e devolva o valor da diagonal do quadrado (LADO * √2).
Escreva um programa que recebe o valor do lado de um quadrado, crie um objeto da classe Quadrado com
este valor de lado e mostre a
- área
- perímetro
- diagonal deste quadrado
usando os métodos do objeto criado
"""


class cls_Quadrado:
	def __init__(self, size_lado):
		self.size_lado = size_lado

	def mtd_area(self):
		print(f"Area: {self.size_lado**2:.2f}")

	def mtd_perimetro(self):
		print(f"Perimetro: {self.size_lado*4:.2f}")

	def mtd_diagonal(self):
		from math import sqrt

		print(f"Diagonal: {self.size_lado*sqrt(2):.2f}")

	def mtd_info(self):
		print(f"Lado: {self.size_lado:.2f}")
		self.mtd_area()
		self.mtd_perimetro()
		self.mtd_diagonal()

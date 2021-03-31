from main.Ex_4 import cls_Testa_Circulo,cls_circulo



def test_cls_circulo():
	c = 1
	res = cls_circulo(c)
	res.mtd_Calcular_Area_Circulo()
	assert round(res.area,2) == 3.14


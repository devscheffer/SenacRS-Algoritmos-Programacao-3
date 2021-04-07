from Task_1.main.ex_5 import cls_Quadrado

def test_area():
	a=1
	res = cls_Quadrado(a)
	assert res.mtd_area() == 1
def test_perimetro():
	a=1
	res = cls_Quadrado(a)
	assert res.mtd_perimetro() == 4
def test_diagonal():
	a=1
	res = cls_Quadrado(a)
	assert round(res.mtd_diagonal(),2) == 1.41

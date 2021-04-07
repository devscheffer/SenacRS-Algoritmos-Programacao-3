from Task_1.main.ex_2 import cls_Conta_Corrente, cls_Testa_Conta_Corrente

def test_cls():
	res = cls_Testa_Conta_Corrente(cls_Conta_Corrente(1, 10, "especial", 200))
	assert res.conta.get_saldo() == 10

def test_saque():
	res = cls_Testa_Conta_Corrente(cls_Conta_Corrente(1, 10, "especial", 200))
	res.mtd_saque(5)
	assert res.conta.get_saldo() == 5

def test_deposito():
	res = cls_Testa_Conta_Corrente(cls_Conta_Corrente(1, 10, "especial", 200))
	res.mtd_depositar(70)
	assert res.conta.get_saldo() == 80

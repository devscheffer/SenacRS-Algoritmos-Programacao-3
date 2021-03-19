from Ex_2 import cls_Conta_Corrente,cls_Testa_Conta_Corrente

a = cls_Testa_Conta_Corrente(cls_Conta_Corrente(1, 10, "especial", 200))
a.mtd_saque(5)
a.mtd_depositar(70)
a.mtd_saldo()

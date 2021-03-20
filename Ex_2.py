"""
Crie uma classe “ContaCorrente” que possui:
- um número,
- um saldo,
- um status (informa se é especial ou comum)
- um limite.
"""

"""
Após, crie uma classe “TestaContaCorrente” onde:
- Os atributos são inicializados e mostrados na tela.
- Desenvolva métodos para realizar:
	- saque (verificando se o cliente possui as condições necessárias)
	- depositar
	- consultar saldo
[warning] não foi definida a regra
	- verificar o uso do cheque especial (ou não)
"""


def fn_check_status(status):
    dict_status = {"especial": 1, "comum": 1}
    if dict_status.get(status, 0) == 1:
        return status
    else:
        raise ValueError(f"[{status}] Não é um status valido")


def fn_check_gte_0(number):
    if number >= 0:
        return number
    else:
        raise ValueError(f"[{number}] Não é permitido um valor menor que zero")


class cls_Conta_Corrente:
    def __init__(self, numero, saldo, status, limite):
        self.numero = fn_check_gte_0(numero)
        self.saldo = saldo
        self.status = fn_check_status(status)
        self.limite = fn_check_gte_0(limite)


class cls_Testa_Conta_Corrente:
    def __init__(self, Conta_Corrente):
        self.atributos = Conta_Corrente.__dict__
        self.conta = Conta_Corrente
        print(self.atributos)

    def mtd_saque(self, vlr_saque):
        fn_check_gte_0(vlr_saque)
        if self.conta.saldo > vlr_saque:
            self.conta.saldo -= vlr_saque
        else:
            print(f"[Error]Valor maior que o saldo.")
        print(f"Saque: {vlr_saque}")
        print(f"Saldo atual: {self.conta.saldo}")

    def mtd_depositar(self, vlr_deposito):
        fn_check_gte_0(vlr_deposito)
        self.conta.saldo += vlr_deposito
        print(f"Deposito: {vlr_deposito}")
        print(f"Saldo atual: {self.conta.saldo}")

    def mtd_saldo(self):
        print(f"Saldo atual: {self.conta.saldo}")

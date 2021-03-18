def check_status(status):
	dict_status = {'especial':1,'comum':1}
	if dict_status.get(status,0) == 1:
		return status
	else:
		raise ValueError(f'[{status}] Não é um status valido')

def check_gte_0(number):
	if number>=0:
		return number
	else:
		raise ValueError(f'[{number}] Não é permitido um valor menor que zero')

'''
# [todo]#1
Crie uma classe “ContaCorrente” que possui:
- um número,
- um saldo,
- um status (informa se é especial ou comum)
- um limite.
'''
class Conta_Corrente:
	def __init__(self,numero,saldo,status,limite):
		self.numero =check_gte_0(numero)
		self.saldo  =saldo
		self.status =check_status(status)
		self.limite =check_gte_0(limite)

#[todo]#2
'''
Após, crie uma classe “TestaContaCorrente” onde:
- Os atributos são inicializados e mostrados na tela.
- Desenvolva métodos para realizar:
	- saque (verificando se o cliente possui as condições necessárias),
	- depositar,
	- consultar saldo
	- verificar o uso do cheque especial (ou não).
'''
class Testa_Conta_Corrente:
	def __init__(self,Conta_Corrente):



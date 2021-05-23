from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from Task_5.Fib_Iterativo import fib_iterativo
from Task_5.Fib_Recursivo import fib_recursivo

def fn_iterativo(num):
	import csv
	with open(f'Task_5/output/fib_iterativo-{num}.txt',mode='a',newline='') as file:
		write = csv.writer(file)
		header = ['num','execution','time','res']
		write.writerow(header)
		for i in range(10):
			res=fib_iterativo(num)
			print(f'fib_iterativo {res[0]} - Execucao {i+1}/10')
			res.insert(1,i+1)
			write.writerow(res)

def fn_recursivo(num):
	import csv
	with open(f'Task_5/output/fib_recursivo-{num}.txt',mode='a',newline='') as file:
		write = csv.writer(file)
		header = ['num','execution','time','res']
		write.writerow(header)
		for i in range(2):
			res=fib_recursivo(num)
			print(f'fib_recursivo {res[0]} - Execucao {i+1}/10')
			res.insert(1,i+1)
			write.writerow(res)

for i in range(60,101,10):
	# fn_iterativo(i)
	fn_recursivo(i)

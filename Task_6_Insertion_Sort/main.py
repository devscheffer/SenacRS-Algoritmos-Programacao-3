from os import getcwd
from sys import path
cwd = getcwd()
path.append(cwd)

from Task_6_Insertion_Sort.Sorts.bubble import bubble_sort
from Task_6_Insertion_Sort.Sorts.insertion import insertion_sort
from Task_6_Insertion_Sort.Sorts.merge import merge_sort
from Task_6_Insertion_Sort.Sorts.quick import quicksort
from Task_6_Insertion_Sort.Sorts.selection import selection_sort

from Task_6_Insertion_Sort.Sorts.time import run_sorting_algorithm

lst_sample = ['sample_5000','sample_10000','sample_50000','sample_100000','sample_500000']
lst_sorts = ['bubble_sort','insertion_sort','merge_sort','quicksort','selection_sort']

def sample_array(file_name):
	with open(file=f'Task_6_Insertion_Sort\Sample\{file_name}.txt',mode='r') as f:
		f1=f.read().splitlines()
		array=list(map(int,f1))
	return array

def algorithm_test(sort_type,sample):
	print('Gerando array')
	array = sample_array(sample)
	print('array gerado')
	print('Testando algoritmo')
	min_times=run_sorting_algorithm(sort_type,array)
	res = f'{sort_type},{sample},{min_times}'
	print('Teste finalizado')
	print(res)
	print('Comecando escrita')
	with open(file='./Task_6_Insertion_Sort/output.txt',mode='a') as output:
		output.write(f'{res}\n')
	print('Escrita finalizada')

for i in lst_sample:
	for j in lst_sorts:
		print(f'Start: {j} - {i}')
		algorithm_test(sort_type=j,sample=i)

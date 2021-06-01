import random

def sample(step):
	randomlist = random.sample(range(0, step), step)
	with open(file=f'./sample_{step}.txt',mode='w') as f:
		for i in randomlist:
			f.write(f'{i}\n')

lst_sample = [5_000,10_000,50_000,100_000,500_000]
for i in lst_sample:
	sample(i)



import timeit

def fib_iterativo(num):
    start_time = timeit.default_timer()
    ultimo = 1
    penultimo = 1
    if num == 1:
        fib = penultimo
    elif num == 2:
        fib = ultimo
    else:
        atual = 0
        for i in range(2, num):
            atual = ultimo + penultimo
            penultimo = ultimo
            ultimo = atual
        fib = atual
    final_time = timeit.default_timer() - start_time
    return [num, final_time, fib]

'''
num = int(input('Digite um numero para encontrar o seu fib: '))
num,final_time,fib_i = fib_iterativo(num)
print("Fibonacci Iterativo de %d: %d" % (num,fib_i))
print('Tempo: ' + str(final_time) + ' segundos')
'''

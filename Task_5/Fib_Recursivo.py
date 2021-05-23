import timeit


def fib_recursivo(num):
    def fib(number):
        if number == 0 or number == 1:
            return number
        else:

            return fib(number-1) + fib(number-2)

    start_time = timeit.default_timer()
    fib = fib(num)
    final_time = timeit.default_timer() - start_time

    return [num, final_time, fib]

'''
num = int(input('Digite um numero para encontrar o seu fib: '))
num, final_time, fib_r = fib_recursivo(num)
print("Fibonacci Recursivo de %d: %d" % (num, fib_r))
print('Tempo: ' + str(final_time) + ' segundos')
'''

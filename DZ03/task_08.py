#task08
"""
6*. Решить рекурсивно задачу нахождения n-го числа фиббоначи (см. https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
Пример
>>fib(4)
>>3
"""

import time
n1 = int(input('Введите номер числа Фибоначчи\n>'))
n = n1
l = n1
def fib(n):
    if n < 3:
        return 2
    return fib(n - 1) + fib(n - 2)
start1 = time.time()
print('Число Фиббоначи с номером ', n, ':', fib(n))
print(time.time() - start1)

start2 = time.time()
def fib2(l):
    a, b = 1, 1
    for i in range(l):
        a, b = b, a + b
    return b
print('Число Фиббоначи с номером ', l, ':', fib2(l))
print(time.time() - start2)

print(time.time() - start1)
#task08
"""
6*. Решить рекурсивно задачу нахождения n-го числа фиббоначи (см. https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
Пример
>>fib(4)
>>3
"""
# n = input('Введите номер числа Фибоначчи\n>')
n = 6

def fib(n):
    for i in range(n):
        fibn = [1, 1]
        z = fibn[0] + fibn[1]
        fibn.append(z)
        return fibn[n]
fib(n)
print('Число Фиббоначи с номером ', n, '=', fib(n))
#task08
"""
6*. Решить рекурсивно задачу нахождения n-го числа фиббоначи (см. https://ru.wikipedia.org/wiki/Числа_Фибоначчи)
Пример
>>fib(4)
>>3
"""
# n = int(input('Введите номер числа Фибоначчи\n>'))
# def fib(n):
#     if n < 3:
#         return 2
#     return fib(n - 1) + fib(n -2)
#
# print('Число Фиббоначи с номером ', n, ':', fib(n))

n = int(input('Введите номер числа Фибоначчи\n>'))
def fib(n):
    a, b = 1, 1
    for i in range(n):
        a, b = b, a + b
    return b
print('Число Фиббоначи с номером ', n, ':', fib(n))

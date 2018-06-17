#task02
"""
Написать функцию которая находит факториал числа.
(https://ru.wikipedia.org/wiki/Факториал)
"""
a = int(input('Введите число\n>'))
def fact(b):
    value = 1
    for i in range(1, b + 1):
        value *= i
    return value
print(fact(a))
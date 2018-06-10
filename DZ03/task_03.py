#task03
"""
Написать функцию is_prime(a), Которая принимает число и возвращает True или False в зависимости от того, 
простое это число или нет (см. https://ru.wikipedia.org/wiki/Простое_число)
Пример:
>>is_prime(3)
>>True
>>is_prime(4)
>>False
"""
a = int(input('Введите число\n>'))
def is_prime(b):
    for i in range (2, b):
        if b % i is not 0:
            i += 1
        else: return b
    return 0
if is_prime(a) == 0:
    print(a, '- простое')
else:
    print(a, ' - не простое')
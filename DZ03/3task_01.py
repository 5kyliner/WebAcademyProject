#task01
"""
Написать аналог функции len:
Пример:
>>my_len([1,2,3]
3
>>my_len(«hello»)
5
"""
a = input('Введите строку\n>')
def my_len(a):
    count = 0
    for n in a:
        count += 1
    return count
print(my_len(a))

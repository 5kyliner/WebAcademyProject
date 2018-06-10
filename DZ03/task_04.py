#task04
"""
Вывести на экран 10 первых простых чисел используя функцию задания 1
Подсказка:
>>if is_prime(num):
      print(num)
"""
a = int(input('Введите кол-во простых\n>'))
list = [2]
j = 3
def is_prime(b):
    for i in range (2, b):
        if b % i is not 0:
            i += 1
        else: return b
    return 0

while int(len(list)) < a:
    if is_prime(j) == 0:
        list.append(j)
        j += 1
    else:
        j += 1

print(list)
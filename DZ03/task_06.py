﻿>>2, 4, 6
"""
a = int(input('Введите кол-во четных\n>'))
list = [2]
j = 3
while int(len(list)) < a:
    if j % 2 == 0:
        list.append(j)
        j += 1
    else:
        j += 1

print(list)
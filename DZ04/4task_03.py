﻿#task03
"""
Заменить каждый элемент на следующий, последний на первый
	[1, 2, 3, 4] -> [4, 1, 2, 3]
"""
a = [1, 2, -3, 5, -6, 7, -9]
def f(a):
    z = a[0]
    for i in range(len(a) - 1):
        a[i] = a[i + 1]
    a[-1] = z
    return a
print(f(a))
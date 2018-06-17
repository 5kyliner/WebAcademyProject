#task06
"""
Посчитать сумму первых двух четных чисел в списке
	[5, 7, 8, 3, 4, 6, 8] -> 12
"""
a = [1, 2, -3, 5, -6, 7, -9]
def f(a):
    twoeven = 0
    for i in range(len(a)):
        if a[i] % 2 == 0:
            twoeven += a[i]
    return twoeven
print(f(a))
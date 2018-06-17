#task01
"""
0. Дан список чисел, заменить каждое число на квадрат этого числа.
	[1, 2, 3, 4] -> [1, 4, 9, 16]
"""
spis_OK = [1, 2, 3, 4]

def f(spis_OK):
    for i in range(len(spis_OK)):
        spis_OK[i] = spis_OK[i] ** 2
    return spis_OK
print(f(spis_OK))
#task04
"""
Перевернуть список
	[1, 2, 3, 4] -> [4, 3, 2, 1]
"""
a = [1, 2, -3, 5, -6, 7, -9]
def f(a):
    b = []
    for i in range(len(a)):
        b.append(a[-i])
    b.append(a[0])
    del b[0]
    return b
print(f(a))
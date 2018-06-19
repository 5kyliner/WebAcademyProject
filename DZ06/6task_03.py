# Task03
"""
Дан список, содержащий положительные и отрицательные числа.
Заменить все элементы списка на противоположные по знаку.
Например, задан список [1, -5, 0, 3, -4].
После преобразования должно получиться [-1, 5, 0, -3, 4]."""
# a = [-4, -2, -3, 4, -6, 4, 343]
def reverse_values(a):
    for i in range(len(a)):
        a[i] *= -1
    return a


if __name__ == '__main__':
    assert reverse_values([-1, -2, -3]) == [1, 2, 3]
    assert reverse_values([1, 1, 1]) == [-1, -1, -1]
    assert reverse_values([]) == []
    assert reverse_values([1, -1, 0]) == [-1, 1, 0]
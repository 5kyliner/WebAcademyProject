# Task06
"""
Дан список чисел. Выведите все элементы списка, которые больше предыдущего элемента.
"""
# a = [-4, -2, -3, 4, -6, 4, 343]

def get_largest(a):
    b = []
    for i in range(len(a)):
        if a[i] > a[i - 1]:
            b.append(a[i])
    return b

if __name__ == '__main__':
    assert get_largest([1, 2, 3, 4]) == [2, 3, 4]
    assert get_largest([2, 3, 100, 4]) == [3, 100]
    assert get_largest([-10, -2, 0, 4]) == [-2, 0, 4]

# Task01
"""
1. Найти номер и значение первого положительного элемента списка.
"""
def find_first_positive(a):
    for i in range(len(a)):
        if a[i] > 0:
            # print('Номер элемента списке:', i)
            # print('Значение:', a[i])
            return (i, a[i])
        elif a[i] < 0:
            pass
        else:
            print('Положительных элементов нет')

if __name__ == '__main__':
    # some tests
    assert find_first_positive([-1, 2, 5]) == (1, 2)
    assert find_first_positive([1, 2, 5]) == (0, 1)
    assert find_first_positive([-1, -2, 5]) == (2, 5)
    assert find_first_positive([-1, -2, -5]) is None

"""
1. Найти сумму положительных элементов списка.
# """
# a = [-4, -2, -3, 4, -6, 4, 343]

def sum_of_positives(a):
    z = 0
    for i in range(len(a)):
        if a[i] > 0:
            z += a[i]
        # elif a[i] < 0:
        #     pass
        # else:
        #     print('Положительных элементов нет')
    # print('Сумма положительных элементов:', z)
    return z


if __name__ == '__main__':
    assert sum_of_positives([1, 2, -4, 0]) == 3
    assert sum_of_positives([-1, -2, -3]) == 0
    assert sum_of_positives([1, 1, 1]) == 2, "Ошибка пилота"

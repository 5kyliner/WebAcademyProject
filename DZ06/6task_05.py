# Task05
"""
Найти сумму и произведение элементов одномерного числового списка.
"""
# a = [-4, -2, -3, 4, -6, 4, 343]

def get_sum(a):
    sssum = 0
    for i in range(len(a)):
        sssum += a[i]
    return sssum
# print('Сумма:', sssum, '\nПроизведение:', mult)

def get_production(a):
    mult = 1
    for i in range(len(a)):
        mult *= a[i]
    return mult


if __name__ == '__main__':
    assert get_sum([1, 2]) == 3
    assert get_sum([0, -3]) == -3

    assert get_production([1, 1]) == 1
    assert get_production([2, 3]) == 6
    assert get_production([0, 1]) == 0

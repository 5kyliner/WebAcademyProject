# Task09
"""
Из одномерного списка удалить все повторяющиеся элементы (дубликаты) так,
чтобы каждое значение встречалось в списке только один раз.
"""
# a = [-4, 2, -3, 4, -6, 4, 343]

def uniq_list(a):
    b = []
    b.append(a[0])
    for i in range(len(a)):
        if a[i] in b:
            pass
        else:
            b.append(a[i])
    return b


if __name__ == '__main__':
    assert uniq_list([1, 1, 2]) == [1, 2]

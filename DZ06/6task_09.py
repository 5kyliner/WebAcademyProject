# Task09
"""
Из одномерного списка удалить все повторяющиеся элементы (дубликаты) так,
чтобы каждое значение встречалось в списке только один раз.
"""
# a = [-4, 2, -3, 4, -6, 4, 343]
a = [1, 1, 2]

def uniq_list(a):
    b = a[0]
    for i in range(len(a) - 1):
        if a[i + 1] in b:
            pass
        else:
            b.append(a[i + 1])
    return b
print(uniq_list(a))


# if __name__ == '__main__':
#     assert uniq_list([1, 1, 2]) == [1, 2]

# Task10
"""
В одномерном списке удалить все четные элементы и оставить
только нечетные.
"""
# a = [-4, 2, -3, 4, -6, 4, 343]

def odd(a):
    b = []
    for i in range(len(a)):
        if a[i] % 2 != 0:
            b.append(a[i])
    return b
    # print(b)




if __name__ == '__main__':
    assert odd([1, 2, 3, 4]) == [1, 3]
    assert odd([0, 1, 1]) == [1, 1]

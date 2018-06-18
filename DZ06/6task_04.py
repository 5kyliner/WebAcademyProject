# Task04
"""
В списке найти минимальный и максимальный элементы, поменять их местами.
"""
a = [-4, -2, -3, 4, -6, 4, 343]

def change_max_min(a):
    x = a[0]
    y = a[0]
    k = l = 0
    for i in range(len(a)):
        if a[i] > x:
            x = a[i]
            k = i
        elif a[i] < y:
            y = a[i]
            l = i
        else:
            pass
    a[k] = y
    a[l] = x
    return a
    # return print('Минимальный:', y, '\nМаксимальный:', x)

if __name__ == '__main__':
    assert change_max_min([1, 2, 3]) == [3, 2, 1]
    assert change_max_min([1, 1, 1]) == [1, 1, 1]
    assert change_max_min([2, 2, 1]) == [1, 2, 2]
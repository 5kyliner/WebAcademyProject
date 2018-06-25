# Task07
"""
Дан список чисел. Если в нем есть два соседних элемента одного знака, выведите эти числа.
Если соседних элементов одного знака нет — не выводите ничего.
Если таких пар соседей несколько — выведите первую пару.
"""
# a = [-4, 2, -3, 4, -6, 4, 343]

def find_pairs(a):
    b = []
    for i in range(len(a) - 1):
        if a[i + 1] < 0 and a[i] < 0:
            b.append(tuple((a[i], a[i + 1])))
            i += 1
            if a[i] < 0 and a[i - 1] < 0:
                break
        elif a[i + 1] > 0 and a[i] > 0:
            b.append(tuple((a[i], a[i + 1])))
            i += 1
            if a[i + 1] > 0 and a[i] > 0:
                break
    return b

if __name__ == '__main__':
    assert find_pairs([1, 2, -1, -1]) == [(1, 2), (-1, -1)]
    assert find_pairs([1, 2, 3, 4]) == [(1, 2)]
    assert find_pairs([1, -1, 2, -4]) == []
#Task 13
"""Дано два списка значений, вывести значения которые есть в
обоих списках.
[1,2,3,4] [3, 5, 7, 1] -> [1, 3]"""

# a = [1, 2, 3, 4]
# b = [3, 5, 7, 1]
#
# c = []


def intersection_ordered(a, b):
    c = []
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                c.append(a[i])
    return c

if __name__ == '__main__':
    assert intersection_ordered([1, 2, 3], [3, 5, 4]) == [3]
    assert intersection_ordered([1, 2], [2, 1]) == [1, 2]
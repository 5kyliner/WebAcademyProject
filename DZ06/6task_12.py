#Task 12
"""Дан список значений. Превратить список в словарь
поочередно превращая елменты в ключи и значения. [1, 2, 3, 4, 5, 6]
-> {1: 2, 3: 4, 5: 6}"""

# a = [1, 2, 3, 4, 5, 6]
#
# # b = {key: key + 1 for key in a}
# # b.pop(2)
# # b.pop(4)
# # b.pop(6)
# # print(b)


# def list_to_dict(a):
#     b = {}
#     for i in range(len(a)):
#         try:
#             if i % 2 == 0:
#                 b[a[i]] = a[i + 1]
#         except IndexError:
#             pass
#     return b
    # print(b)

def list_to_dict(a):
    b = {}
    for i in range(0, len(a), 2):
        try:
            b[a[i]] = a[i + 1]
        except IndexError:
            pass
    return b


if __name__ == '__main__':
    assert list_to_dict([1, 2, 3, 4, 5]) == {1: 2, 3: 4}
    assert list_to_dict(['k', 'v', 'k2', 'v2']) == {'k': 'v', 'k2': 'v2'}
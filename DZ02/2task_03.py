#task 03
"""
Вывести таблицу умножения на экран.
"""

for i in range(8):
    for j in range(8):
        print(i+2, 'x', j+2, '=' , (i+2) * (j+2), end='\t')
    print('\n')
# Task01
"""
Переписать информацию с одного файла в другой
"""

with open('xczxc.txt', 'w') as f:
    f.write(input('Input data:\n>'))

with open('xczxc.txt', 'r') as f:
    with open('xczxc2.txt', 'w+') as f1:
        f1.write(f.read())
        f1.seek(0)
        a = f1.read()

print(a)

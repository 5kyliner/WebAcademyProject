#task 04
"""
Вывести на экран фигуры со звездочек (
Ромб, Елочка, Треугольник, Квадрат, ступеньки
)
"""

a = int(input('Введите высоту ромба\n>'))
b = int(input('Введите ширину ромба\n>'))
for i in range(a // 2):
        print(' ' * (b // 2 - i + 40),'*' * i * 2)
for j in range(a // 2, 0, -1):
        print(' ' * (b // 2 - j + 40),'*' * j * 2)

a = int(input('Введите высоту молнии\n>'))
b = int(input('Введите ширину молнии\n>'))
for i in range(a // 2):
        print(' ' * (b // 2 - i + 40),'*' * i)
for j in range(a // 2, 0, -1):
        print(' ' * (b // 2 + 40),'*' * j)

a = int(input('Введите высоту елки\n>'))
b = int(input('Введите среднюю ширину елки\n>'))
c = int(input('Введите количество ярусов\n>'))
d = a // c
for i in range(d):
    print(' ' * (b // 2 - i + 40),'*' * i * 2)	# не придумал как загнать макушку в один for
for count in range(c - 1):
    l = d + count * 5
    for j in range(l - 3, l + 6):
            print(' ' * (b // 2 - j + 40),'*' * j * 2)

a = int(input('Введите высоту ступеньки\n>'))
b = int(input('Введите количество ступенек\n>'))
for i in range(b):
    for j in range(a):
        print(' '*(a*(b-1)-i*a),'*'*a*i)

# task07
"""
5. Написать функцию принимающую имя фигуры (квадрат, треугольник, ромб), ее размерность и рисует эту фигуру на экран
Пример:
>> print_figure(‘треугольник’, 3)
*
**
***
"""

def rhombus():
    a = int(input('Введите высоту ромба\n>'))
    b = int(input('Введите ширину ромба\n>'))
    for i in range(a // 2):
            print(' ' * (b // 2 - i + 40),'*' * i * 2)
    for j in range(a // 2, 0, -1):
            print(' ' * (b // 2 - j + 40),'*' * j * 2)

def lightning():
    a = int(input('Введите высоту молнии\n>'))
    b = int(input('Введите ширину молнии\n>'))
    for i in range(a // 2):
            print(' ' * (b // 2 - i + 40),'*' * i)
    for j in range(a // 2, 0, -1):
            print(' ' * (b // 2 + 40),'*' * j)

def pinetree():
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

def stairs():
    a = int(input('Введите высоту ступеньки\n>'))
    b = int(input('Введите количество ступенек\n>'))
    for i in range(b):
        for j in range(a):
            print(' '*(a*(b-1)-i*a),'*'*a*i)

fig = input('Введите фигуру: Ромб, Молния, Ёлка, Ступеньки\n>')
if fig == 'Ромб':
    rhombus()
elif fig == 'Молния':
    lightning()
elif fig == 'Ёлка':
    pinetree()
elif fig == 'Ступеньки':
    stairs()
# elif fig == 'Треугольник':
#     triangle()
else:
    print('Такая фигура ещё не запрограммирована')
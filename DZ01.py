# # # Задача 01
# a = int(input('Введите a: '))
# b = int(input('Введите b: '))
# f = int(input('Введите f: '))
# # c =  2 * b - f / a + f * a**2
# print ('Результат:',2 * b - f / a + f * a**2)

# # # Задача 02
# import datetime
# now = datetime.datetime.now()
# a = int(input('Год рождения: '))
# b = int(input('Номер месяца: '))
# с = int(input('День месяца: '))
# print ()
# print ('Ваш возраст:', now.year - a)
# print ('Вы прожили:', (now.year - a - 1)*12 + now.month, 'месяцев')
# print ('Вы продышали(приблизительно):', (now.year - a - 1)*365 -
#        (now.year - a)//4 + now.month*30 + now.month//2 + now.day, 'дней')

# # # Задача 03
# a = int(input('Введите длину (м): '))
# print ('Длина (км):', a / 1000)

# # # Задача 04
# name = input('name: ')
# c =  len (name)
# x = c
# while True:
#     x = abs (x - 2)
#     if x == 1:
#         # print("Нечет!")
#         break
#     if x == 0:
#         # print("Чет!")
#         break
# # print (x)
# space = int((20 - 6 - c) / 2)
# print ('*' * 20)
# print ('*',(' ' * space)+(' ' * x),name,(' ' * space),'*')
# print ('*' * 20)

# # Задача 04'
# name = input('name: ')
# c =  len (name)
# x = c % 2
# # print (x)
# space = int((20 - 6 - c) / 2)
# print ('*' * 20)
# print ('*',(' ' * space)+(' ' * x),name,(' ' * space),'*')
# print ('*' * 20)

# # # Задача 05*
# n = int(input('Введите N: '))
# print ('Часов', n // 60, 'Минут', n % 60)
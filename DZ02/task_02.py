#task 02
a = int(input('Введите первое число\n>'))
b = int(input('Введите второе число\n>'))
c = int(input('Введите третье число\n>'))
list = [a, b, c]
for z in list:
    if list.count(z) >= 2:
        list2 = [list[0] + 5, list[1] + 5, list[2] + 5] # Есть ли альтернатива проще?
        print(list2)
        break
    else:
        print('Равных нет')
        break
# Task 15
"""
15. Программа переводчик на соленый язык. 
Правило: после каждой гласной вставляем с + сама гласная. 
Привет -> Приcивеcет 
Сальса -> саcальсаcа
"""
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']

a = [i for i in input('Введите фразу по-русски:')]
b = []
s = 'с'
c = ''
for i in range(len(a)):
    if str(a[i]) in vowels:
        b.append(a[i])
        b.append(s)
        b.append(a[i])
    else:
        b.append(a[i])
c = c.join(b)
print(c)
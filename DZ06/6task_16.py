#Task 16
"""
Программа переводчик из соленого языка.
Посокесемосон -> Покемон
Посокемн
"""
vowels = ['а', 'о', 'и', 'е', 'ё', 'э', 'ы', 'у', 'ю', 'я']

a = [i for i in input('Введите фразу по-русски:')]
b = []
c = ''
for i in range(len(a)):
    try:
        if str(a[i]) in vowels:
            b.append(a[i])
            del a[(i + 1):(i + 3)]
        else:
            b.append(a[i])
        print(b)
    except:
        IndexError
c = c.join(b)
print(c)
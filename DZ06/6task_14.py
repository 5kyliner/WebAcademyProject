# Task 14
"""
14. Программа конвертер валют (для валют: евро, доллар, гривна, рубль, фунт)
должна переводить из любой валюты в любую. Курсы хардкодим.
Пример:
——————————————
Введите валюту: UAH
Введите сумму: 2600
В какой валюте получить результат? USD
2600 UAH = 100 USD
———————————————
"""

course = {
    'usd' : [26, 0.038],
    'uah' : [1, 1],
    'rub' : [0.4, 2.416],
    'gbp' : [34, 1.333],
    'eur' : [31, 0.0325]
             }

into = input('Введите валюту: USD, UAH, RUB, GBP, EUR\n>')
out = input('Куда выводим: USD, UAH, RUB, GBP, EUR\n>')

try:
    val = int(input('Введите сумму:\n>'))
except ValueError:
    print('Необходимо ввести цифры')

try:
    k1 = course[into.lower()][0]
    k2 = course[out.lower()][1]
except KeyError:
    print('Валюта не найдена')
else:
    print(into, val, '=', out, k1 * val * k2)
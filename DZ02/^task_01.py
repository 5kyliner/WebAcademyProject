﻿#task01
"""
Сумма покупки составляет а гривен. Если а больше 1000 гривен, то предоставляется скидка 15%.
Вывести на экран сумму покупки с учетом скидки либо сообщение о том, что скидка не предоставляется.
"""

a = int(input('Введите сумму покупки\n>'))

if a > 1000:
    a -= a * 0.15
    print('Сумма со скидкой:', int(a))
else:
    print('Скидка не предоставляется')

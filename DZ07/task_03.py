# #Task 01
# """
# Создать класс Автомобиль содержащий информацию: модель, цвет, год_выпуска, стоимость. Описать метод __str__.
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >>print(car1)
# name: Audi
# color: Red
# year: 1999
# price: $12000
# """
#
# class Car:
#
#     def __init__(self, model, color, year, price):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#
#     def __str__(self):
#         string = f'model: {self.model}\ncolor: {self.color}' \
#                  f'\nyear: {self.year}\nprice: {self.price}'
#         return string
#
#     """
#     model: Audi
#     color: Red
#     year: 1999
#     price: $12000
#     """
#
# car1 = Car('Audi', 'Red', '1999', '$12000')
# print(car1)
#
#
# #Task 02
# """
# Создать класс Автосалон содержащий информацию: адрес, имя, список доступных машин.
# Реализовать методы для отображения всех доступных машин, добавления новых машин, покупки машин (после покупки машина удаляется из списка) + проверки на наличие такой машины в салоне
# Пример
# >> car1 = Car(‘Audi’, ‘Red’, ‘1999’, ‘$12000’)
# >> car2 = Car(‘BMW’, ‘Black’, ‘2009’, ‘$18000’)
# >>
# >>showroom = ShowRoom(‘Borshagovska 17’, ‘Volkswagen showroom’)
# >>showroom.add_car(car1)
# >>showroom.add_car(car2)
# >>
# >>showroom.show_all()
# 1
# ————————-
# name: Audi
# color: Red
# year: 1999
# price: $12000
#
# 2
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
# >>showroom.sell_car(Car(‘Volvo’, ‘Red’, ’1993’, ‘$20000’))
# ‘No such car!’
# >>showroom.sell_car(car1)
# ‘Car has been sold!’
# >>showroom.show_all()
# 1
# —————————
# name: BMW
# color: Black
# year: 2009
# price: $18000
# """
#
# class ShowRoom:
#
#     def __init__(self, name_init, address_init):
#         self.name = name_init
#         self.address = address_init
#         self._cars = []
#
#     def add_car(self, car):
#         self._cars.append(car)
#
#     def show_all(self ):
#         string = ''
#         for car in self._cars:
#             if car.status == 'In stock':
#                 string = string + str(car) + '\n'
#         # print('\n\n'.join(map(str, self._cars)))
#         print('Автосалон', self.name, 'на', self.address, ':\n', string)
#
#
#     def reserve_car(self, car):
#         car.status = 'Reserved'
#         print('Reserved\n')
#
#     def sell_car(self, car):
#         if car in self._cars:
#             car.status = 'Sold'
#             print('Sold\n')
#
#     def is_car(self, car):
#         if car.status == 'In stock':
#             print('In stock\n')
#         elif car.status == 'Sold' or 'Reserved':
#             print('This car has been sold or reserved')
#         else:
#             print('Unavailable\n')
#
# class Car:
#
#     def __eq__(self, other):
#         return [self.model, self.year, self.color, self.price, self.status] == \
#                [other.model, other.year, other.color, other.price, other.status]
#
#     def __init__(self, model, color, year, price, status):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.price = price
#         self.status = status
#
#     def __str__(self):
#         string = f'status: {self.status}\nmodel: {self.model}\ncolor:' \
#                  f'{self.color}\nyear: {self.year}\nprice: {self.price}\n'
#         return string
#
# car1 = Car('Audi', 'Red', '1999', '$12000', 'In stock')
# car2 = Car('BMW', 'Black', '2009', '$18000', 'In stock')
#
# showroom  = ShowRoom('VW showroom', 'Borshagovska 17')
# showroom2  = ShowRoom('BMW', 'Khreshatyk 17')
#
#
# showroom.add_car(car1)
# showroom.add_car(car2)
#
# showroom.show_all()
#
# showroom2.add_car(car1)
# showroom2.add_car(car2)
#
# showroom2.show_all()
#
# showroom.sell_car(car1)
#
# showroom.show_all()
#
# showroom2.reserve_car(car2)
#
# showroom2.show_all()
#
#
# showroom2.is_car(car2)
# # showroom2.is_car(car2)

#Task 03
"""
Описать класс Книга. (год, название, автор) Описать метод __eq__  для сравнения
>> book1 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
>> book2 = Book(‘Nineteen Eighty-Four’, 1949, ‘George Orwell’)
>> book3 = Book(‘Над пропастью во ржи’, 1951, ‘Jerome David Salinger’)
>>book1 == book2
True
>>book1 == book3
False
Добавить поле с отзывами и методы добавить отзыв, посмотреть все отзывы.
>>book1.add_review(‘Cool!!’)
>>book1.add_review(‘Not bad’)
>>book1.show_reviews()
1.
Cool!!

2.
Not bad
"""

class Kniga:

    def __init__(self, name, year, author):
        self.year = year
        self.name = name
        self.author = author
        self.review = []

    def __eq__(self, other):
        return [self.year, self.name, self.author] == [other.year, other.name, other.author]

    def __str__(self):
        string = f'author: {self.author}\nname: {self.name}\nyear: {self.year}\n'
        return string

    def add_review(self):
        a = input('Оставьте Ваш отзыв:\n>')
        self.review.append(a)

    def show_reviews(self):
        print(self)
        print('Reviews:')
        for i in range(len(self.review)):

            print("{}{} {}".format(i + 1, ')', self.review[i]))


book1 = Kniga('Nineteen Eighty-Four', 1949, 'George Orwell')
book2 = Kniga('Nineteen Eighty-Four', 1949, 'George Orwell')
book3 = Kniga('Над пропастью во ржи', 1951, 'Jerome David Salinger')

book1.add_review()
book1.add_review()
# book3.add_review()

book1.show_reviews()


print(book1 == book2)
print(book3 == book2)
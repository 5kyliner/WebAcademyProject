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

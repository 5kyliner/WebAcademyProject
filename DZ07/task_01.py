#Task 01
"""
—оздать класс јвтомобиль содержащий информацию: модель, цвет, год_выпуска, стоимость. ќписать метод __str__.
ѕример
>> car1 = Car(СAudiТ, СRedТ, С1999Т, С$12000Т)
>>print(car1)
name: Audi
color: Red
year: 1999
price: $12000
"""

class Car:

    def __init__(self, model, color, year, price):
        self.model = model
        self.color = color
        self.year = year
        self.price = price

    def __str__(self):
        string = f'model: {self.model}\ncolor: {self.color}' \
                 f'\nyear: {self.year}\nprice: {self.price}'
        return string

    """
    model: Audi
    color: Red
    year: 1999
    price: $12000
    """

car1 = Car('Audi', 'Red', '1999', '$12000')
print(car1)
import csv


class Item:
    """Класс товаров"""
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        """Инициализация"""
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def calculate_total_price(self):
        """Получит общую стоимость конкретного товара в магазине"""
        return self.price * self.quantity

    def apply_discount(self):
        """Применить установленную скидку для конкретного товара"""
        new_price = self.price * self.pay_rate
        self.price = new_price

    @property
    def name(self):
        """Проверка на длину названия"""
        if len(self.__name) < 10:
            return self.__name
        else:
            return 'Exception: Длина наименования товара превышает 10 символов.'

    @name.setter
    def name(self, value: str) -> None:
        """Устанавливает название"""
        self.__name = value

    '''@name.getter
    def name(self):
        return self.name'''

    @staticmethod
    def is_integer(num) -> bool:
        """Проверка на целое число"""
        if num % 2 == 0 or (num + 1) % 2 == 0:
            return True
        return False

    @classmethod
    def instantiate_from_csv(cls):
        """Загрузка экземпляров из csv"""
        with open('items.csv', 'r') as File:
            reader = csv.DictReader(File)
            for line in reader:
                item = cls(line['name'], int(line['price']), int(line['quantity']))
                Item.all.append(item)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.__name}, {self.price}, {self.quantity})'

    def __str__(self):
        return f'{self.__name}'

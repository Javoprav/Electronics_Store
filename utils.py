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


class Phone(Item):
    """Класс телефоны"""
    def __init__(self, name, price, quantity, number_of_sim):
        """Инициализация"""
        super().__init__(name, price, quantity)
        self.__number_of_sim = number_of_sim

    def __add__(self, other):
        """Сложение экземпляров по кол-ву"""
        if isinstance(other, Item):
            return self.quantity + self.quantity
        else:
            raise ValueError('Только объекты Item')

    @property
    def number_of_sim(self):
        """Возврат кол-ва сим-карт"""
        if self.__number_of_sim > 0 and self.__number_of_sim == int(self.__number_of_sim):
            return self.__number_of_sim
        else:
            raise ValueError('Количество физических SIM-карт должно быть целым числом больше нуля.')

    @number_of_sim.setter
    def number_of_sim(self, value):
        """Назначение кол-ва сим-карт"""
        self.__number_of_sim = value


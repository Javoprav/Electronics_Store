class Item:
    """Класс товаров"""
    pay_rate = 0.85
    all = []

    def __init__(self, name, price, quantity):
        """Инициализация"""
        self.name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def calculate_total_price(self):
        """Получит общую стоимость конкретного товара в магазине"""
        return self.price * self.quantity

    def apply_discount(self):
        """Применить установленную скидку для конкретного товара"""
        new_price = self.price * self.pay_rate
        self.price = new_price
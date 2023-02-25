from utils import *

if __name__ == "__main__":
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)

    print(item1.calculate_total_price())
    print(item2.calculate_total_price())

    Item.pay_rate = 0.8  # устанавливаем новый уровень цен
    item1.apply_discount()
    print(item1.price)
    print(item2.price)
    print(Item.all)
    item_3 = Item('Samsung', 100, 10)
    item_3.pay_rate = 0.7
    item_3.apply_discount()
    print(item_3.price)
    # print(item2.__name)

    item = Item('Телефон', 10000, 5)
    item.name = 'Смартфон'
    print(item.name)
    item.name = 'СуперСмартфон'
    print(item.name)
    print(len(Item.all))
    Item.instantiate_from_csv()  # создание объектов из данных файла
    print(len(Item.all))  # в файле 5 записей с данными по товарам
    # 5
    item1 = Item.all[0]
    print(item1.name)
    # Смартфон

    print(Item.is_integer(5))
    print(Item.is_integer(5.0))
    print(Item.is_integer(5.5))
    # True
    # True
    # False
    item1 = Item("Смартфон", 10000, 20)
    print(item1.__repr__())
    # Item('Смартфон', 10000, 20)
    print(item1)
    # Смартфон
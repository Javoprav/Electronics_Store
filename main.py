from utils import Item

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
from utils import *


def test_calculate_total_price():
    item_3 = Item('Samsung', 3, 10)
    assert item_3.calculate_total_price() == 30


def test_apply_discount():
    item_4 = Item('Samsung', 100, 10)
    item_4.pay_rate = 0.7  # устанавливаем новый уровень цен
    item_4.apply_discount()
    assert item_4.price == 70


def test_name():
    item_5 = Item('Samsung', 100, 10)
    item_5.name = 'sams'
    assert item_5.name == 'sams'
    assert print(item_5.name) is None
    item_5.name = 'SamsungSamsung'
    assert item_5.name == 'Exception: Длина наименования товара превышает 10 символов.'

def test_is_integer():
    assert Item.is_integer(5) is True
    assert Item.is_integer(5.5) is False


def test_instantiate_from_csv():
    assert print(Item.instantiate_from_csv()) == None
import pytest

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
    item_6 = Item('Samsung', 100, 10)
    assert print(item_6.instantiate_from_csv()) is None


def test___repr__():
    item_7 = Item('Samsung', 100, 10)
    assert item_7.__repr__() == 'Item(Samsung, 100, 10)'


def test___str__():
    item_8 = Item('Samsung', 100, 10)
    assert item_8.__str__() == 'Samsung'


def test___add__():
    phone4 = Phone("iPhone 14", 120_000, 5, 2)
    phone5 = Phone("iPhone 14", 120_000, 9, 2)
    assert phone4 + phone5 == 14
    # assert phone4 + 5 is ValueError('Только объекты Item')


def test_number_of_sim():
    phone6 = Phone("iPhone 14", 120_000, 9, 2)
    phone6.number_of_sim = 6
    assert phone6.number_of_sim == 6
    '''with pytest.raises(ValueError):
        phone6.number_of_sim = 0'''


def test_language():
    kb1 = Keyboard('Dark Project KD87A', 9600, 5)
    assert kb1.language == 'EN'
    kb1.change_lang
    assert kb1.language == 'RU'
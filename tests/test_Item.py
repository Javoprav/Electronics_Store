import pytest
from utils import *


def test_calculate_total_price():
    """Получит общую стоимость конкретного товара в магазине"""
    item_3 = Item('Samsung', 3, 10)
    assert item_3.calculate_total_price() == 30


def test_apply_discount():
    """Получит общую стоимость конкретного товара в магазине"""
    item_4 = Item('Samsung', 100, 10)
    item_4.pay_rate = 0.7  # устанавливаем новый уровень цен
    item_4.apply_discount()
    assert item_4.price == 70
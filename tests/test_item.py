"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item


def test_item_creation():
    """Тест для проверки создания экземпляра класса Item"""

    item = Item("Смартфон", 500, 10)
    assert isinstance(item, Item)
    assert item.name == "Смартфон"
    assert item.price == 500
    assert item.quantity == 10


def test_calculate_total_price():
    """Тест для проверки расчета общей стоимости товара"""

    item = Item("Смартфон", 20000, 5)
    assert item.calculate_total_price() == 100000


def test_apply_discount():
    """Тест для проверки применения скидки"""

    item = Item("Ноутбук", 10000, 2)
    item.apply_discount()
    assert item.price == 10000 * Item.pay_rate

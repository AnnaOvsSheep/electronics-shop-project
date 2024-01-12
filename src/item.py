import csv
import os


class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        self.all.append(self)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value[0:10]

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.quantity * self.price
        return total_price

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls, f_path):
        path = "../src/items.csv"
        f_path = os.path.abspath(path)
        cls.all.clear()
        with open(f_path, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                name = row['name']
                price = float(row['price'])
                quantity = int(row['quantity'])
                cls(name, price, quantity)

    @staticmethod
    def string_to_number(s: str) -> int:
        """
        Преобразует строку в число, если это возможно.

        :param s: Строка.
        :return: Число.
        """
        return int(float(s))

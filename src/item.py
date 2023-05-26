import os.path

import src.item
import csv


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
        Item.all.append(self)


    # Геттер для name
    @property
    def name(self):
        """Возвращает имя сотрудника. К атрибуту можно обращаться без ()."""
        return self.__name

    # Чтобы иметь возможность присваивать атрибуту name значения,
    # надо определить его сеттер. Это работает только для атрибутов с @property
    '''В этом сеттере `name` проверяем, что длина наименования товара не больше 10 символов'''

    @name.setter
    def name(self, name):
        if len(self.__name) <= 10:
            self.__name = name
        else:
            raise Exception('Длина товара более 10 символов')

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self):
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate


    '''класс-метод, инициализирующий экземпляры класса `Item` данными из файла'''
    @classmethod
    def instantiate_from_csv(cls):
        dir_path=os.path.dirname(os.path.realpath(__file__))
        with open(dir_path + '\items.csv') as csv.file:
            reader = csv.DictReader(csv.file)

            for row in reader:
                cls(row['name'], row['price'], row['quantity'])



    '''статический метод, возвращающий число из числа-строки'''

    @staticmethod
    def string_to_number(string_number):
        return float(string_number.replace(',', '.'))




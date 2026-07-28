""" 
    Модуль, который реализует практическое применение полиморфизма и композиции через задачу создания системы заказа для интернет-магазина. В системе есть следующие компоненты:

    Item (Товар):

    Имеет свойства: название, цена, количество.
    Метод subtotal для определения общей стоимости товара в зависимости от его количества.
    Order (Заказ):

    Содержит список товаров.
    Метод total для подсчета общей стоимости заказа без учета скидок.
    Метод total with discount для расчета общей стоимости с учетом скидки.
    Метод set policy для изменения политики скидок.
    Discount Policies (Политики скидок):

    NoDiscount: не применяет скидку.
    PercentageDiscount: предоставляет скидку в процентах от общей суммы.
    Класс Order использует композицию для внедрения политики скидок, что позволяет динамически изменять поведение скидок в заказе. Заказ сначала подсчитывают без скидки с помощью NoDiscount, а затем политику меняют на процентную скидку через метод set policy, чтобы применить 10% скидку и проверить работу системы.

    В результате, используя этот подход можно легко расширять систему, добавляя новые политики скидок без изменения существующего кода.
"""

from dataclasses import dataclass
from typing import Protocol


@dataclass
class Item:
    """ Единица товара """
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        """ Расчет суммы """
        return self.price * self.qty


class DiscountPolicy(Protocol):
    """ Протокол политики скидок """

    def discount(self, total: float) -> float: ...


class NoDiscount:
    """ Политика без скидки """

    def discount(self, total: float) -> float:
        return 0


@dataclass
class PercentageDiscount:
    """ Политика с % скидки"""
    percent: float

    def discount(self, total: float) -> float:
        return total * (self.percent / 100)


class Order:
    """ Заказ """

    def __init__(self, items: list[Item], policy: DiscountPolicy):
        self.items = items
        self.policy = policy

    def total(self) -> float:
        return sum(i.subtotal() for i in self.items)

    def total_with_discount(self) -> float:
        return self.total() - self.policy.discount(self.total())

    def set_policy(self, policy: DiscountPolicy):
        pass


item = Item(name="Apple", price=1.5, qty=3)
print(item)              # Item(name='Apple', price=1.5, qty=3)
print(item.subtotal())   # 4.5
print(item == Item(name="Apple", price=1.5, qty=3))  # True

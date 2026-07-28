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


@dataclass
class Item:
    """ Единица товара """
    name: str
    price: float
    qty: int = 1

    def subtotal(self) -> float:
        """ Расчет суммы """
        return self.price * self.qty


class NoDiscount:
    """ Политика без скидки """

    def discount(self, total: float) -> float:
        return 0


class PercentageDiscount:
    pass


@dataclass
class Order:
    """ Заказ """
    items: list[Item]


item = Item(name="Apple", price=1.5, qty=3)
print(item)              # Item(name='Apple', price=1.5, qty=3)
print(item.subtotal())   # 4.5
print(item == Item(name="Apple", price=1.5, qty=3))  # True

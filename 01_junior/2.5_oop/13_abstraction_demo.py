# -*- coding: utf-8 -*-
"""
Блок 2.5.7: Демо — абстракция (abc.ABC, @abstractmethod)
════════════════════════════════════════════════════════════════════════
Темы:
  1. Проблема без abc: базовый класс можно создать напрямую по ошибке
  2. abc.ABC + @abstractmethod — запрет на уровне создания объекта
  3. Наследник обязан реализовать ВСЕ абстрактные методы
  4. Абстрактный метод + обычный (шаблонный) метод в одном базовом классе
  5. @property + @abstractmethod — абстрактное свойство
  6. Практическая польза: полиморфизм через общий интерфейс
"""

from abc import ABC, abstractmethod


# ════════════════════════════════════════════════════════════════════════
# 1. Проблема без abc: базовый класс можно создать напрямую по ошибке
# ════════════════════════════════════════════════════════════════════════

class ShapePlain:
    def area(self) -> float:
        raise NotImplementedError("наследник должен переопределить area()")


plain = ShapePlain()  # создался без ошибок — хотя area() ещё не работает
try:
    plain.area()
except NotImplementedError as e:
    print(f"Ошибка: {e}")
# Ошибка ловится только в РАНТАЙМЕ, при вызове area() — ничего не
# мешало создать бесполезный объект ShapePlain() без переопределения


# ════════════════════════════════════════════════════════════════════════
# 2. abc.ABC + @abstractmethod — запрет на уровне создания объекта
# ════════════════════════════════════════════════════════════════════════

class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


try:
    shape = Shape()  # type: ignore[misc] # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")
# Ошибка: Can't instantiate abstract class Shape without an implementation
# for abstract method 'area' — Python не дал даже СОЗДАТЬ объект


# ════════════════════════════════════════════════════════════════════════
# 3. Наследник обязан реализовать ВСЕ абстрактные методы
# ════════════════════════════════════════════════════════════════════════

class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


circle = Circle(2)
print(circle.area())   # 12.56636 — теперь можно создать и посчитать


class Square(Shape):
    def __init__(self, side: float) -> None:
        self.side = side
    # area() не переопределён — Square по факту остаётся абстрактным


try:
    square = Square(3)  # type: ignore[misc] # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")
# Ошибка: Can't instantiate abstract class Square without an implementation
# for abstract method 'area' — не важно, что Square НАСЛЕДУЕТ Shape,
# сам он всё ещё не выполнил контракт


# ════════════════════════════════════════════════════════════════════════
# 4. Абстрактный метод + обычный метод (шаблон) в одном базовом классе
# ════════════════════════════════════════════════════════════════════════

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        ...

    def checkout(self, amount: float) -> None:
        # обычный метод — готовая реализация доступна ВСЕМ наследникам
        # без переопределения; сам вызывает абстрактный pay()
        print(f"Оформление заказа на {amount}")
        self.pay(amount)


class CardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Списано с карты: {amount}")


CardPayment().checkout(500)
# Оформление заказа на 500
# Списано с карты: 500


# ════════════════════════════════════════════════════════════════════════
# 5. @property + @abstractmethod — абстрактное свойство
# ════════════════════════════════════════════════════════════════════════

class Vehicle(ABC):
    @property
    @abstractmethod
    def wheels(self) -> int:
        ...


class Car(Vehicle):
    @property
    def wheels(self) -> int:
        return 4


class Motorcycle(Vehicle):
    @property
    def wheels(self) -> int:
        return 2


print(Car().wheels)          # 4
print(Motorcycle().wheels)   # 2
# Car/Motorcycle обязаны реализовать wheels именно как @property — ABC
# проверяет только ИМЯ метода, но не то, обёрнут ли он в @property


# ════════════════════════════════════════════════════════════════════════
# 6. Практическая польза: полиморфизм через общий интерфейс
# ════════════════════════════════════════════════════════════════════════

shapes: list[Shape] = [Circle(1), Circle(2)]
total_area = sum(shape.area() for shape in shapes)
print(total_area)   # 3.14159 + 12.56636 = 15.70795
# Код, который считает total_area, ВООБЩЕ не знает, что такое Circle —
# он знает только, что у любого Shape есть area(). ABC гарантирует,
# что это верно для любого наследника Shape.

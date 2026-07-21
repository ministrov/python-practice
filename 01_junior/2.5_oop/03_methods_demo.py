# -*- coding: utf-8 -*-
"""
Блок 2.5.2: Демо — методы: обычные, @classmethod, @staticmethod, @property
════════════════════════════════════════════════════════════════════════
Темы:
  1. Обычный метод — всегда первым параметром self, работает с
     конкретным экземпляром
  2. @staticmethod — не получает ни self, ни cls; просто функция,
     логически связанная с классом (утилита)
  3. @classmethod — первым параметром cls (сам класс, не экземпляр);
     типичное применение — альтернативные конструкторы
  4. @property — метод, который вызывается БЕЗ скобок, как обычный
     атрибут; вычисляемое значение вместо хранимого
  5. @x.setter — разрешает присваивание в property, с проверкой
     (валидацией) значения перед сохранением
"""


# ════════════════════════════════════════════════════════════════════════
# 1. Обычный метод — уже знаком по теме 1, self обязателен
# ════════════════════════════════════════════════════════════════════════

class Rectangle:
    """Прямоугольник со сторонами width и height."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        # self нужен, чтобы добраться до width/height ИМЕННО этого экземпляра
        return self.width * self.height


rect = Rectangle(3, 4)
print(rect.area())            # 12


# ════════════════════════════════════════════════════════════════════════
# 2. @staticmethod — функция внутри класса, но БЕЗ доступа к self/cls
# ════════════════════════════════════════════════════════════════════════

class MathUtils:
    """Набор независимых от состояния утилит — логически про математику."""

    @staticmethod
    def is_even(number: int) -> bool:
        # никакого self — не нужен доступ ни к экземпляру, ни к классу
        return number % 2 == 0

    @staticmethod
    def clamp(value: float, low: float, high: float) -> float:
        return max(low, min(value, high))


# staticmethod можно вызвать и через класс, и через экземпляр — одинаково
print(MathUtils.is_even(4))       # True
print(MathUtils.is_even(7))       # False
print(MathUtils.clamp(15, 0, 10))  # 10

utils = MathUtils()
print(utils.is_even(2))           # True — через экземпляр тоже работает

# Когда использовать: логика не зависит ни от self, ни от cls, но
# тематически принадлежит классу (иначе была бы просто функцией снаружи)


# ════════════════════════════════════════════════════════════════════════
# 3. @classmethod — первый параметр cls (класс, а не экземпляр)
# ════════════════════════════════════════════════════════════════════════

class Pizza:
    def __init__(self, toppings: list[str]) -> None:
        self.toppings = toppings

    @classmethod
    def margherita(cls) -> "Pizza":
        # cls() — то же самое, что Pizza(), но работает и для наследников
        return cls(["сыр", "томаты", "базилик"])

    @classmethod
    def pepperoni(cls) -> "Pizza":
        return cls(["сыр", "пепперони"])

    def describe(self) -> str:
        return f"Пицца с: {', '.join(self.toppings)}"


# classmethod как АЛЬТЕРНАТИВНЫЙ КОНСТРУКТОР — способ создать объект
# по-другому, без явного перечисления всех параметров каждый раз
pizza_one = Pizza.margherita()
pizza_two = Pizza.pepperoni()
print(pizza_one.describe())   # Пицца с: сыр, томаты, базилик
print(pizza_two.describe())   # Пицца с: сыр, пепперони


# ════════════════════════════════════════════════════════════════════════
# 4. @property — метод, который выглядит как атрибут (без скобок)
# ════════════════════════════════════════════════════════════════════════

class Circle:
    def __init__(self, radius: float) -> None:
        self.radius = radius

    @property
    def diameter(self) -> float:
        # вычисляется КАЖДЫЙ раз при обращении — не хранится отдельно
        return self.radius * 2

    @property
    def area(self) -> float:
        return 3.14159 * self.radius ** 2


circle = Circle(5)
print(circle.diameter)        # 10 — без скобок! как обычный атрибут
print(circle.area)            # 78.53975

# Если радиус меняется — diameter и area пересчитываются автоматически,
# не нужно вручную синхронизировать несколько атрибутов
circle.radius = 10
print(circle.diameter)        # 20


# ════════════════════════════════════════════════════════════════════════
# 5. @x.setter — присваивание в property С ПРОВЕРКОЙ значения
# ════════════════════════════════════════════════════════════════════════

class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self._balance = balance   # "_balance" — приватное имя по конвенции

    @property
    def balance(self) -> float:
        # геттер — читается как account.balance, без скобок
        return self._balance

    @balance.setter
    def balance(self, value: float) -> None:
        # сеттер — вызывается при account.balance = ...
        if value < 0:
            raise ValueError("Баланс не может быть отрицательным")
        self._balance = value


account = BankAccount("Anton", 100)
print(account.balance)        # 100

account.balance = 250         # вызывает setter, проверка проходит
print(account.balance)        # 250

try:
    account.balance = -50     # setter бросает ValueError
except ValueError as e:
    print(f"Ошибка: {e}")     # Ошибка: Баланс не может быть отрицательным

print(account.balance)        # 250 — значение не изменилось после ошибки

# Без property пришлось бы либо разрешать account.balance = -50 напрямую
# (без проверки), либо переименовывать в метод set_balance(value) — тогда
# теряется удобный синтаксис "как у атрибута"


# ════════════════════════════════════════════════════════════════════════
# 6. property БЕЗ setter — доступно только для чтения
# ════════════════════════════════════════════════════════════════════════

class Employee:
    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name}"
        # setter для full_name не объявлен — присвоить нельзя


employee = Employee("Ivan", "Petrov")
print(employee.full_name)     # Ivan Petrov

try:
    employee.full_name = "Ivan Sidorov"  # type: ignore[misc] # намеренно
except AttributeError as e:
    print(f"Ошибка: {e}")

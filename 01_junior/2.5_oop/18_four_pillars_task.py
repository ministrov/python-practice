# -*- coding: utf-8 -*-
"""
Блок 2.5.9: Практика — 4 столпа ООП (итог блока)
════════════════════════════════════════════════════════════════════════
5 ЗАДАНИЙ для самостоятельного решения. Новый синтаксис не нужен — все
инструменты уже знакомы из тем 2-8. Задание 1 — назвать столп словами,
задания 2-5 — по одному короткому упражнению на каждый столп.
Совет: посмотри 17_four_pillars_demo.py, если застрял.
"""

from abc import ABC, abstractmethod


print("=" * 60)
print("ЗАДАНИЕ 1: назови столп")
print("=" * 60)
print("""
Для каждого фрагмента ниже напечатай ОДНО слово — какой из 4 столпов
ООП (Инкапсуляция / Абстракция / Наследование / Полиморфизм) он
иллюстрирует. Объяснять не нужно, только назвать.

1.1 class Shape(ABC):
        @abstractmethod
        def area(self) -> float: ...

1.2 class Manager(Employee):
        def __init__(self, name, salary, team_size):
            super().__init__(name, salary)
            self.team_size = team_size

1.3 class Temperature:
        @property
        def celsius(self) -> float:
            return self._celsius
        @celsius.setter
        def celsius(self, value: float) -> None:
            if value < -273.15:
                raise ValueError("Ниже абсолютного нуля")
            self._celsius = value

1.4 for shape in shapes:   # shapes: list[Shape]
        print(shape.area())   # Circle и Square считают по-разному,
                               # вызывающий код это не знает
""")

# ТВОЙ КОД ЗДЕСЬ:
# 1.1
print("Абстракция")
# 1.2
print("Наследование")
# 1.3
print("Инкапсуляция")
# 1.4
print("Полиморфизм")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: инкапсуляция")
print("=" * 60)
print("""
2.1 Создай класс Product с приватным атрибутом _price и property price
    (геттер + сеттер).
2.2 В сеттере price запрети отрицательные значения (raise ValueError).
2.3 Создай Product с начальной ценой 10, попробуй присвоить price = -5,
    оберни в try/except ValueError as e, напечатай f"Ошибка: {e}".
2.4 Напечатай product.price — убедись, что значение не изменилось.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Product:
    def __init__(self, price: int) -> None:
        self._price = price

    @property
    def price(self) -> int:
        return self._price

    @price.setter
    def price(self, value: int) -> None:
        if value < 0:
            raise ValueError("Цена не может быть отрицательным числом")
        self._price = value


product_a = Product(10)

try:
    product_a.price = -5
except ValueError as e:
    print(f"Ошибка: {e}")

print(product_a.price)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: абстракция")
print("=" * 60)
print("""
3.1 Создай абстрактный класс Shape(ABC) с абстрактным методом
    area(self) -> float.
3.2 Создай Circle(Shape), реализующий area() (используй radius,
    3.14159 * radius ** 2).
3.3 Попробуй создать Shape() напрямую, оберни в try/except TypeError
    as e, напечатай f"Ошибка: {e}".
""")

# ТВОЙ КОД ЗДЕСЬ:


class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        ...


class Circle(Shape):
    def __init__(self, radius: float) -> None:
        self.radius = radius

    def area(self) -> float:
        return 3.14159 * self.radius ** 2


try:
    shape = Shape()  # type: ignore # намеренно
except TypeError as e:
    print(f"Ошибка: {e}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: наследование")
print("=" * 60)
print("""
4.1 Создай класс Person с __init__(self, name: str, age: int).
4.2 Создай класс Student(Person) с __init__(self, name, age,
    university: str), который вызывает super().__init__(name, age)
    вместо повторного присваивания self.name/self.age.
4.3 Создай Student(...), напечатай его name, age и university.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


class Student(Person):
    def __init__(self, name: str, age: int, university: str) -> None:
        super().__init__(name, age)
        self.university = university


student_anna = Student("Anna", 19, "Бауманка")
print(student_anna.name)
print(student_anna.age)
print(student_anna.university)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: полиморфизм")
print("=" * 60)
print("""
5.1 Используя Shape/Circle из задания 3, создай ещё Square(Shape)
    с area() -> side ** 2.
5.2 Собери список shapes: list[Shape] из Circle(...) и Square(...).
5.3 Пройдись циклом for, напечатай shape.area() для каждого — код не
    должен знать заранее, какой это конкретный тип.
""")

# ТВОЙ КОД ЗДЕСЬ:


class Square(Shape):
    def __init__(self, side: float) -> None:
        super().__init__()
        self.side = side

    def area(self) -> float:
        return self.side ** 2


shapes: list[Shape] = [Circle(3), Square(2.3)]
for shape in shapes:
    print(shape.area())

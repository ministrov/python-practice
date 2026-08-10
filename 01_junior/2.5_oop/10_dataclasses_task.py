# -*- coding: utf-8 -*-
"""
Блок 2.5.5: Практика — dataclasses
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 09_dataclasses_demo.py, если застрял с синтаксисом.
"""

# from dataclasses import dataclass, field

from dataclasses import dataclass, field


print("=" * 60)
print("ЗАДАНИЕ 1: базовый dataclass — Point")
print("=" * 60)
print("""
1.1 Создай @dataclass Point с полями x: float, y: float (без ручного
    __init__/__repr__ — dataclass сгенерирует их сам).
1.2 Создай Point(1, 2) и Point(1, 2) в двух разных переменных,
    напечатай оба объекта (проверь автогенерированный __repr__) и
    результат их сравнения через == (должно быть True — сравнение по
    значениям полей).
""")

# ТВОЙ КОД ЗДЕСЬ:


@dataclass
class Point:
    x: float
    y: float


p1 = Point(1, 2)
p2 = Point(1, 2)
print(p1)
print(p2)
print(p1 == p2)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: значения по умолчанию — User")
print("=" * 60)
print("""
2.1 Создай @dataclass User с полями name: str и is_active: bool = True
    (дефолт только у второго поля).
2.2 Создай User("Игорь") без второго аргумента, напечатай — is_active
    должен быть True.
2.3 Создай User("Олег", False), напечатай — is_active должен быть
    False.
""")

# ТВОЙ КОД ЗДЕСЬ:


@dataclass
class User:
    name: str
    is_active: bool = True


user_a = User("Игорь")
print(user_a.is_active)
user_b = User("Олег", False)
print(user_b.is_active)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: ловушка изменяемого дефолта — Cart")
print("=" * 60)
print("""
3.1 Создай @dataclass Cart с полем items: list[str], используя
    field(default_factory=list[str]) как значение по умолчанию (НЕ
    просто "= []" — dataclass бросит ValueError).
3.2 Создай cart_a = Cart() и cart_b = Cart(), добавь cart_a.items.
    append("книга"), напечатай items у ОБОИХ — у cart_b список должен
    остаться пустым (независимые списки, не общий на оба объекта).
""")

# ТВОЙ КОД ЗДЕСЬ:


@dataclass
class Cart:
    items: list[str] = field(default_factory=list[str])


cart_a = Cart()
cart_b = Cart()
cart_a.items.append("Книга")
print(cart_a.items)
print(cart_b.items)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: frozen=True — неизменяемые координаты")
print("=" * 60)
print("""
4.1 Создай @dataclass(frozen=True) Coordinates с полями lat: float,
    lon: float.
4.2 Создай coords = Coordinates(55.75, 37.62), напечатай его.
4.3 В try/except попробуй присвоить coords.lat = 0, поймай исключение
    (какой класс исключения бросается?) и напечатай
    f"Ошибка: {type(e).__name__}".
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: order=True — сравнение и сортировка версий")
print("=" * 60)
print("""
5.1 Создай @dataclass(order=True) Version с полями major: int,
    minor: int, patch: int.
5.2 Создай Version(1, 2, 0) и Version(1, 10, 0), напечатай результат
    v1 < v2 (сравнение идёт по кортежу полей в порядке объявления).
5.3 Создай список из трёх произвольных Version, напечатай
    sorted(список) — объекты должны выстроиться по возрастанию.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: field(repr=..., compare=...) — Account")
print("=" * 60)
print("""
6.1 Создай @dataclass Account с полями username: str, password: str =
    field(repr=False) (пароль не должен попадать в вывод print) и
    login_count: int = field(default=0, compare=False) (это поле не
    должно участвовать в сравнении ==).
6.2 Создай acc1 = Account("admin", "secret123") и acc2 = Account(
    "admin", "secret123", login_count=5), напечатай acc1 (пароль не
    должен быть виден) и результат acc1 == acc2 (должно быть True,
    несмотря на разный login_count).
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: __post_init__ — валидация и вычисляемое поле")
print("=" * 60)
print("""
7.1 Создай @dataclass Rectangle с полями width: float, height: float
    и area: float = field(init=False) (не принимается в __init__
    снаружи, вычисляется внутри).
7.2 Добавь __post_init__(self) -> None, который бросает ValueError,
    если width <= 0 или height <= 0, иначе вычисляет self.area =
    self.width * self.height.
7.3 Создай Rectangle(3, 4), напечатай его (area должен быть 12).
7.4 В try/except создай Rectangle(-1, 5), поймай ValueError и
    напечатай текст сообщения.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: комплексное — dataclass + композиция (Invoice)")
print("=" * 60)
print("""
8.1 Создай @dataclass LineItem с полями name: str, price: float,
    quantity: int, и методом subtotal(self) -> float, возвращающим
    price * quantity.
8.2 Создай @dataclass Customer с полями name: str, email: str.
8.3 Создай @dataclass Invoice с полями customer: Customer, items:
    list[LineItem] = field(default_factory=list[LineItem]) — Invoice
    ИМЕЕТ customer и items внутри (композиция, как в задании 5 темы
    "композиция vs наследование"), а не наследуется от них.
8.4 Добавь Invoice метод total(self) -> float, возвращающий
    sum(item.subtotal() for item in self.items).
8.5 Создай Invoice с Customer("Аня", "a@mail.com") и двумя LineItem
    внутри items (через append после создания Invoice), напечатай
    invoice.total().
""")

# ТВОЙ КОД ЗДЕСЬ:

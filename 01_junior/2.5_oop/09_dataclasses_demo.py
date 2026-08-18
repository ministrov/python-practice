# -*- coding: utf-8 -*-
"""
Блок 2.5.5: Демо — dataclasses
════════════════════════════════════════════════════════════════════════
Темы:
  1. От обычного класса к @dataclass — автогенерация __init__/__repr__/
     __eq__
  2. Значения по умолчанию и ловушка изменяемых дефолтов
  3. frozen=True — неизменяемые объекты
  4. order=True — автоматическое сравнение и сортировка
  5. field(repr=..., compare=...) — тонкая настройка полей
  6. __post_init__ — вычисляемые поля и валидация
"""

from dataclasses import dataclass, field


# ════════════════════════════════════════════════════════════════════════
# 1. Обычный класс-данные — сколько boilerplate нужно писать руками
# ════════════════════════════════════════════════════════════════════════


class PointPlain:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"PointPlain(x={self.x!r}, y={self.y!r})"

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, PointPlain):
            return NotImplemented
        return self.x == other.x and self.y == other.y


p1 = PointPlain(1, 2)
p2 = PointPlain(1, 2)
print(p1)  # PointPlain(x=1, y=2)
print(p1 == p2)  # True — но только потому что __eq__ написан руками


# То же самое через @dataclass — __init__, __repr__ и __eq__ генерируются
# автоматически из аннотированных полей класса
@dataclass
class Point:
    x: float
    y: float


q1 = Point(1, 2)
q2 = Point(1, 2)
print(q1)  # Point(x=1, y=2)
print(q1 == q2)  # True — сравнение по значениям полей, не по id()
print(q1 is q2)  # False — это разные объекты в памяти


# ════════════════════════════════════════════════════════════════════════
# 2. Значения по умолчанию и ловушка изменяемых дефолтов
# ════════════════════════════════════════════════════════════════════════


@dataclass
class User:
    name: str
    is_active: bool = True  # обычный дефолт для неизменяемого типа — ок


user_a = User("Аня")
print(user_a)  # User(name='Аня', is_active=True)


# С изменяемыми типами (list/dict/set) в поле по умолчанию так писать
# НЕЛЬЗЯ — dataclass бросит ValueError на этапе объявления класса:
#
#     @dataclass
#     class Cart:
#         items: list[str] = []   # -> ValueError: mutable default...
#
# Причина та же, что и с дефолтными аргументами функций: один и тот же
# list был бы общим для ВСЕХ экземпляров Cart. Правильно — через
# field(default_factory=...), которая создаёт НОВЫЙ list на каждый
# экземпляр:


@dataclass
class Cart:
    items: list[str] = field(default_factory=list[str])


cart_a = Cart()
cart_b = Cart()
cart_a.items.append("книга")
print(cart_a.items)  # ['книга']
print(cart_b.items)  # [] — независимый список, не расшарен с cart_a


# ════════════════════════════════════════════════════════════════════════
# 3. frozen=True — неизменяемые объекты (как tuple, но с именами полей)
# ════════════════════════════════════════════════════════════════════════


@dataclass(frozen=True)
class Coordinates:
    lat: float
    lon: float


moscow = Coordinates(55.75, 37.62)
print(moscow)  # Coordinates(lat=55.75, lon=37.62)

try:
    moscow.lat = 0  # type: ignore[misc]
except Exception as e:
    print(f"Ошибка: {type(e).__name__}: {e}")
    # Ошибка: FrozenInstanceError: cannot assign to field 'lat'

# frozen-объекты удобны как value object — координата, деньги, версия:
# их нельзя случайно испортить после создания, и они хешируемы (можно
# класть в set или использовать как ключ dict), в отличие от обычного
# @dataclass без frozen.


# ════════════════════════════════════════════════════════════════════════
# 4. order=True — автоматическое сравнение (<, <=, >, >=) и сортировка
# ════════════════════════════════════════════════════════════════════════


@dataclass(order=True)
class Version:
    major: int
    minor: int
    patch: int


v1 = Version(1, 2, 0)
v2 = Version(1, 10, 0)
print(v1 < v2)  # True — сравнение идёт по кортежу полей
# (1, 2, 0) < (1, 10, 0), по порядку объявления

versions = [Version(2, 0, 0), Version(1, 0, 0), Version(1, 5, 0)]
print(sorted(versions))
# [Version(major=1, minor=0, patch=0), Version(major=1, minor=5, patch=0),
#  Version(major=2, minor=0, patch=0)]


# ════════════════════════════════════════════════════════════════════════
# 5. field(repr=..., compare=...) — тонкая настройка отдельных полей
# ════════════════════════════════════════════════════════════════════════


@dataclass
class Account:
    username: str
    password: str = field(repr=False)  # не попадает в __repr__
    login_count: int = field(default=0, compare=False)  # не участвует в __eq__


acc1 = Account("admin", "secret123")
acc2 = Account("admin", "secret123", login_count=5)
print(acc1)  # Account(username='admin') — пароль скрыт
print(acc1 == acc2)  # True — login_count разный, но не участвует
# в сравнении благодаря compare=False


# ════════════════════════════════════════════════════════════════════════
# 6. __post_init__ — вычисляемые поля и валидация после генерации __init__
# ════════════════════════════════════════════════════════════════════════


@dataclass
class Rectangle:
    width: float
    height: float
    area: float = field(init=False)  # не принимается в __init__ снаружи

    def __post_init__(self) -> None:
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Стороны прямоугольника должны быть > 0")
        self.area = self.width * self.height


rect = Rectangle(3, 4)
print(rect)  # Rectangle(width=3, height=4, area=12)

try:
    Rectangle(-1, 5)
except ValueError as e:
    print(f"Ошибка: {e}")
    # Ошибка: Стороны прямоугольника должны быть > 0

# __post_init__ вызывается автоматически СРАЗУ после автогенерированного
# __init__ — удобное место для валидации входных данных и для вычисления
# полей, которые зависят от других полей (area зависит от width/height).

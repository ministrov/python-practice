# -*- coding: utf-8 -*-
"""
Блок 2.2.2: Кортеж (tuple) — неизменяемая последовательность
════════════════════════════════════════════════════════════════════════

Кортеж — это упорядоченная, НЕИЗМЕНЯЕМАЯ коллекция элементов.
Элементы могут быть разных типов. Доступ по индексу как в списке.
Главное отличие от списка: нельзя изменять содержимое (immutable).
"""

# ===== СОЗДАНИЕ КОРТЕЖЕЙ =====
from collections import namedtuple
from typing import Any
print("=== СОЗДАНИЕ КОРТЕЖЕЙ ===\n")

# Пустой кортеж
empty: tuple[Any, ...] = ()
print(f"Пустой кортеж: {empty}")  # ()

# Кортеж с элементами
numbers: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
print(f"Числа: {numbers}")  # (1, 2, 3, 4, 5)

# Кортеж с разными типами
mixed: tuple[int, str, float, bool, None] = (1, "hello", 3.14, True, None)
print(f"Смешанные типы: {mixed}")  # (1, 'hello', 3.14, True, None)

# Кортеж из одного элемента (важна запятая!)
single: tuple[int] = (42,)
print(f"Кортеж из одного элемента: {single}")  # (42,)

# БЕЗ запятой это просто скобки, не кортеж
not_tuple: int = (42)
# 42, <class 'int'>
print(f"Без запятой (это просто число): {not_tuple}, тип: {type(not_tuple)}")

# Кортеж можно создать без скобок
implicit: tuple[int, int, int] = 1, 2, 3
print(f"Кортеж без скобок: {implicit}")  # (1, 2, 3)

# Кортеж из списка
from_list: tuple[int, int, int] = tuple([10, 20, 30])
print(f"Кортеж из списка: {from_list}")  # (10, 20, 30)

print()

# ===== ИНДЕКСИРОВАНИЕ И СРЕЗЫ =====
print("=== ИНДЕКСИРОВАНИЕ И СРЕЗЫ ===\n")

students: tuple[str, str, str, str, str] = ("Alice", "Bob", "Charlie", "Diana", "Eve")
print(f"Список студентов: {students}")

# Индекс начинается с 0
print(f"students[0] = {students[0]}")  # Alice
print(f"students[-1] = {students[-1]}")  # Eve (последний)

# Срезы работают как в списках
print(f"students[1:4] = {students[1:4]}")  # ('Bob', 'Charlie', 'Diana')
print(f"students[:3] = {students[:3]}")  # ('Alice', 'Bob', 'Charlie')
print(f"students[::2] = {students[::2]}")  # ('Alice', 'Charlie', 'Eve')

print()

# ===== ОСНОВНЫЕ ОПЕРАЦИИ =====
print("=== ОСНОВНЫЕ ОПЕРАЦИИ ===\n")

# len() — длина кортежа
print(f"len((1, 2, 3)) = {len((1, 2, 3))}")  # 3

# count() — подсчитать вхождения элемента
numbers_dup: tuple[int, int, int, int, int, int] = (1, 2, 2, 3, 2, 4)
print(f"(1, 2, 2, 3, 2, 4).count(2) = {numbers_dup.count(2)}")  # 3

# index() — найти индекс первого вхождения
print(f"(1, 2, 2, 3, 2, 4).index(2) = {numbers_dup.index(2)}")  # 1

# in — проверка принадлежности
colors: tuple[str, str, str] = ("red", "green", "blue")
print(f"'red' in {colors} = {'red' in colors}")  # True
print(f"'yellow' in {colors} = {'yellow' in colors}")  # False

print()

# ===== НЕИЗМЕНЯЕМОСТЬ (IMMUTABLE) =====
print("=== НЕИЗМЕНЯЕМОСТЬ (IMMUTABLE) ===\n")

my_tuple: tuple[int, int, int] = (1, 2, 3)
print(f"Исходный кортеж: {my_tuple}")

# НЕЛЬЗЯ изменять элементы кортежа
try:
    my_tuple[0] = 10  # type: ignore
except TypeError as e:
    print(f"Ошибка при попытке изменить: {e}")
    # 'tuple' object does not support item assignment

# НЕЛЬЗЯ добавлять элементы
try:
    my_tuple.append(4)  # type: ignore
except AttributeError as e:
    print(f"Ошибка при попытке добавить: {e}")
    # 'tuple' object has no attribute 'append'

print("Кортеж защищен от случайных изменений!")

print()

# ===== КОНКАТЕНАЦИЯ И ПОВТОРЕНИЕ =====
print("=== КОНКАТЕНАЦИЯ И ПОВТОРЕНИЕ ===\n")

tuple1: tuple[int, int, int] = (1, 2, 3)
tuple2: tuple[int, int] = (4, 5)

# Конкатенация
combined: tuple[int, int, int, int, int] = tuple1 + tuple2
print(f"{tuple1} + {tuple2} = {combined}")  # (1, 2, 3, 4, 5)

# Повторение
repeated: tuple[int, int, int, int, int, int] = (1, 2) * 3
print(f"(1, 2) * 3 = {repeated}")  # (1, 2, 1, 2, 1, 2)

print()

# ===== РАСПАКОВКА (UNPACKING) =====
print("=== РАСПАКОВКА (UNPACKING) ===\n")

# Распаковка кортежа в переменные
coordinates: tuple[int, int] = (10, 20)
x: int
y: int
x, y = coordinates
print(f"Координаты: x={x}, y={y}")  # x=10, y=20

# Распаковка с несколькими элементами
data: tuple[int, int, int, int, int] = (1, 2, 3, 4, 5)
first: int
middle: list[int]
last: int
first, *middle, last = data
print(f"Первый: {first}, середина: {middle}, последний: {last}")
# Первый: 1, середина: [2, 3, 4], последний: 5

# Обмен переменных через распаковку
a: int
b: int
a, b = 5, 10
a, b = b, a
print(f"После обмена: a={a}, b={b}")  # a=10, b=5

print()

# ===== ИСПОЛЬЗОВАНИЕ КАК КЛЮЧ СЛОВАРЯ =====
print("=== КОРТЕЖ КАК КЛЮЧ СЛОВАРЯ ===\n")

# Кортежи можно использовать как ключи словаря (списки нельзя!)
locations = {
    (40.7128, 74.0060): "New York",
    (51.5074, 0.1278): "London",
    (48.8566, 2.3522): "Paris"
}

print(f"Координаты: {locations}")
print(f"Город на (40.7128, 74.0060): {locations[(40.7128, 74.0060)]}")

print()

# ===== ИТЕРАЦИЯ =====
print("=== ИТЕРАЦИЯ ===\n")

fruits: tuple[str, str, str] = ("apple", "banana", "cherry")
for fruit in fruits:
    print(f"  {fruit}")

# С индексом
print("\nС индексом (enumerate):")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")

print()

# ===== ПРЕОБРАЗОВАНИЕ =====
print("=== ПРЕОБРАЗОВАНИЕ ===\n")

# Список в кортеж
list_to_tuple: tuple[int, ...] = tuple([1, 2, 3])
print(f"Список [1, 2, 3] в кортеж: {list_to_tuple}")  # (1, 2, 3)

# Кортеж в список
tuple_to_list: list[int] = list((4, 5, 6))
print(f"Кортеж (4, 5, 6) в список: {tuple_to_list}")  # [4, 5, 6]

# Строка в кортеж (каждый символ отдельно)
string_to_tuple: tuple[str, ...] = tuple("hello")
# ('h', 'e', 'l', 'l', 'o')
print(f"Строка 'hello' в кортеж: {string_to_tuple}")

print()

# ===== NAMED TUPLES (ИМЕНОВАННЫЕ КОРТЕЖИ) =====
print("=== NAMED TUPLES (ИМЕНОВАННЫЕ КОРТЕЖИ) ===\n")


# Создаем именованный кортеж
Point: type[Any] = namedtuple('Point', ['x', 'y'])
p: Any = Point(3, 4)

print(f"Point: {p}")
print(f"x={p.x}, y={p.y}")  # Доступ по имени вместо индекса

# Это все еще кортеж
print(f"Это кортеж: {isinstance(p, tuple)}")  # True
print(f"Длина: {len(p)}")  # 2

# -*- coding: utf-8 -*-
"""
Блок 2.2.3: Словарь (dict) — коллекция ключ-значение
════════════════════════════════════════════════════════════════════════

Словарь — это НЕУПОРЯДОЧЕННАЯ (в Python 3.7+ сохраняет порядок),
ИЗМЕНЯЕМАЯ коллекция пар ключ-значение.
Доступ по ключу (не по индексу).
"""
from typing import Any

# ===== СОЗДАНИЕ СЛОВАРЕЙ =====
print("=== СОЗДАНИЕ СЛОВАРЕЙ ===\n")

# Пустой словарь
empty: dict[str, Any] = {}
print(f"Пустой словарь: {empty}")  # {}

# Словарь с элементами
person: dict[str, str | int] = {"name": "Alice", "age": 30, "city": "London"}
print(f"Словарь: {person}")
# {'name': 'Alice', 'age': 30, 'city': 'London'}

# Словарь с разными типами значений
mixed: dict[str, str | int | float | list[int]] = {"string": "hello", "number": 42, "float": 3.14, "list": [1, 2, 3]}
print(f"Смешанные значения: {mixed}")

# Создание словаря через dict()
from_dict: dict[str, int] = dict(a=1, b=2, c=3)
print(f"Через dict(): {from_dict}")  # {'a': 1, 'b': 2, 'c': 3}

# Создание из списка кортежей
from_list: dict[str, int] = dict([("x", 10), ("y", 20)])
print(f"Из списка кортежей: {from_list}")  # {'x': 10, 'y': 20}

print()

# ===== ДОСТУП К ЭЛЕМЕНТАМ =====
print("=== ДОСТУП К ЭЛЕМЕНТАМ ===\n")

student: dict[str, str | int] = {"name": "Bob", "age": 25, "grade": "A"}

# Доступ по ключу
print(f"student['name'] = {student['name']}")  # Bob
print(f"student['age'] = {student['age']}")  # 25

# get() — безопасный доступ (не вызывает ошибку если ключа нет)
print(f"student.get('name') = {student.get('name')}")  # Bob
print(f"student.get('email') = {student.get('email')}")  # None
print(f"student.get('email', 'no email') = {student.get('email', 'no email')}")  # no email

# KeyError при обращении к несуществующему ключу
try:
    print(student["email"])
except KeyError as e:
    print(f"Ошибка: ключ {e} не найден")

print()

# ===== ИЗМЕНЕНИЕ И ДОБАВЛЕНИЕ =====
print("=== ИЗМЕНЕНИЕ И ДОБАВЛЕНИЕ ===\n")

book: dict[str, str | int] = {"title": "Python 101", "pages": 300}
print(f"Исходный словарь: {book}")

# Изменить значение
book["pages"] = 350
print(f"После изменения pages: {book}")

# Добавить новый элемент
book["author"] = "John Smith"
print(f"После добавления author: {book}")

# update() — добавить несколько элементов
book.update({"year": 2023, "language": "Python"})
print(f"После update(): {book}")

print()

# ===== УДАЛЕНИЕ ЭЛЕМЕНТОВ =====
print("=== УДАЛЕНИЕ ЭЛЕМЕНТОВ ===\n")

colors: dict[str, str] = {"red": "#FF0000", "green": "#00FF00", "blue": "#0000FF"}
print(f"Исходный: {colors}")

# del — удалить по ключу
del colors["green"]
print(f"После del colors['green']: {colors}")

# pop() — удалить и вернуть значение
value: str = colors.pop("red")
print(f"pop('red') вернул: {value}, осталось: {colors}")

# pop() с значением по умолчанию
missing: str = colors.pop("yellow", "not found")
print(f"pop('yellow', 'not found') вернул: {missing}")

# clear() — удалить все элементы
temp: dict[str, int] = {"a": 1, "b": 2}
temp.clear()
print(f"После clear(): {temp}")

print()

# ===== ПРОВЕРКА КЛЮЧЕЙ =====
print("=== ПРОВЕРКА КЛЮЧЕЙ ===\n")

country: dict[str, str | int] = {"name": "France", "capital": "Paris", "population": 67000000}

# in — проверить наличие ключа
print(f"'name' in {country} = {'name' in country}")  # True
print(f"'Paris' in {country} = {'Paris' in country}")  # False (проверяет ключи, не значения)

# keys(), values(), items()
print(f"\nКлючи: {country.keys()}")
# dict_keys(['name', 'capital', 'population'])

print(f"Значения: {country.values()}")
# dict_values(['France', 'Paris', 67000000])

print(f"Пары: {country.items()}")
# dict_items([('name', 'France'), ('capital', 'Paris'), ('population', 67000000)])

print()

# ===== ИТЕРАЦИЯ =====
print("=== ИТЕРАЦИЯ ===\n")

scores: dict[str, int] = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Итерация по ключам (по умолчанию)
print("Итерация по ключам:")
for key in scores:
    print(f"  {key}")

# Итерация по значениям
print("\nИтерация по значениям:")
for value: int in scores.values():
    print(f"  {value}")

# Итерация по парам ключ-значение
print("\nИтерация по парам:")
for key: str in scores:
    value: int = scores[key]
    print(f"  {key}: {value}")

print()

# ===== ВЛОЖЕННЫЕ СЛОВАРИ =====
print("=== ВЛОЖЕННЫЕ СЛОВАРИ ===\n")

company: dict[str, str | dict[str, dict[str, str | int]]] = {
    "name": "TechCorp",
    "employees": {
        "alice": {"position": "Manager", "salary": 50000},
        "bob": {"position": "Developer", "salary": 40000}
    }
}

print(f"Компания: {company['name']}")
employees: dict[str, dict[str, str | int]] = company["employees"]  # type: ignore
print(f"Должность Alice: {employees['alice']['position']}")
print(f"Зарплата Bob: {employees['bob']['salary']}")

print()

# ===== МЕТОДЫ СЛОВАРЯ =====
print("=== МЕТОДЫ СЛОВАРЯ ===\n")

data: dict[str, int] = {"a": 1, "b": 2, "c": 3}

# len() — количество элементов
print(f"len({data}) = {len(data)}")  # 3

# copy() — поверхностная копия
copy_data: dict[str, int] = data.copy()
copy_data["d"] = 4
print(f"Исходный: {data}")
print(f"Копия после изменения: {copy_data}")

# setdefault() — получить значение или установить по умолчанию
result: int = data.setdefault("a", 10)
print(f"setdefault('a', 10) = {result}")  # 1 (уже существует)

result = data.setdefault("d", 10)
print(f"setdefault('d', 10) = {result}")  # 10 (добавили)
print(f"Словарь после: {data}")

print()

# ===== СЛОВАРИ КАК ПАРАМЕТРЫ =====
print("=== СЛОВАРИ КАК ПАРАМЕТРЫ ===\n")

def print_person(person_dict: dict[str, str | int]) -> None:
    for key, value in person_dict.items():
        print(f"  {key}: {value}")

info: dict[str, str | int] = {"name": "David", "age": 28, "job": "Engineer"}
print("Информация о человеке:")
print_person(info)

print()

# ===== COMPREHENSION СЛОВАРЕЙ =====
print("=== COMPREHENSION СЛОВАРЕЙ ===\n")

# Создать словарь из списка чисел
squares: dict[int, int] = {x: x**2 for x in range(1, 6)}
print(f"Квадраты: {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# С условием
even_squares: dict[int, int] = {x: x**2 for x in range(1, 6) if x % 2 == 0}
print(f"Квадраты четных: {even_squares}")  # {2: 4, 4: 16}

# Инвертировать ключи и значения
original: dict[str, int] = {"a": 1, "b": 2, "c": 3}
inverted: dict[int, str] = {v: k for k, v in original.items()}
print(f"Инвертированный: {inverted}")  # {1: 'a', 2: 'b', 3: 'c'}

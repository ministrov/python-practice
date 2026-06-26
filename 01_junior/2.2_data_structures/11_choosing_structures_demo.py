# -*- coding: utf-8 -*-
"""
Блок 2.2.6: Выбор структуры данных под задачу
════════════════════════════════════════════════════════════════════════

Четыре основные структуры Python и когда каждую выбирать:

  list   — упорядоченная изменяемая последовательность
  tuple  — упорядоченная НЕИЗМЕНЯЕМАЯ последовательность
  dict   — пары ключ:значение, быстрый поиск по ключу
  set    — уникальные элементы, быстрая проверка принадлежности
"""

print("=== ШПАРГАЛКА: КОГДА ЧТО ИСПОЛЬЗОВАТЬ ===\n")
print("""
  list   -> порядок важен, нужно менять / добавлять элементы
  tuple  -> фиксированный набор данных (координаты, RGB, запись БД)
  dict   -> нужно искать по имени/ключу
  set    -> нужно убрать дубли или проверить пересечение

Общая скорость O(1): dict.get(), x in set, list[i], tuple[i]
Медленно O(n):        x in list, x in tuple (перебор всех элементов)
""")

# ===== list: порядок + изменяемость =====
print("=== list: ОЧЕРЕДЬ ЗАДАЧ ===\n")

tasks: list[str] = ["купить молоко", "позвонить врачу", "сдать отчёт"]
tasks.append("забрать посылку")
tasks.remove("позвонить врачу")
print(f"Задачи: {tasks}")
print(f"Первая: {tasks[0]}")

print()

# ===== tuple: фиксированная запись =====
print("=== tuple: ФИКСИРОВАННЫЕ ДАННЫЕ ===\n")

# Координаты, цвета, строки таблицы — не должны меняться
point: tuple[float, float] = (55.7558, 37.6173)   # Москва (lat, lon)
color: tuple[int, int, int] = (255, 128, 0)        # RGB оранжевый
user_row: tuple[int, str, str] = (1, "Alice", "alice@example.com")

print(f"Точка: {point}")
print(f"Цвет:  {color}")
print(f"Строка БД: {user_row}")

# tuple как ключ словаря (list нельзя!)
cache: dict[tuple[int, int], str] = {
    (0, 0): "origin",
    (1, 0): "right",
}
print(f"Кэш координат: {cache}")

print()

# ===== dict: поиск по ключу =====
print("=== dict: ПОИСК ПО КЛЮЧУ ===\n")

# Инвентарь: O(1) поиск по названию
inventory: dict[str, int] = {"яблоки": 50, "груши": 30, "бананы": 0}
print(f"Яблок: {inventory['яблоки']}")
print(f"Манго (нет): {inventory.get('манго', 0)}")

# Подсчёт частоты — классический dict use-case
text: str = "banana"
freq: dict[str, int] = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(f"Частота букв в '{text}': {freq}")

print()

# ===== set: уникальность + пересечения =====
print("=== set: УНИКАЛЬНОСТЬ И ПЕРЕСЕЧЕНИЕ ===\n")

# Дедупликация
visits: list[str] = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
unique_visitors: set[str] = set(visits)
print(f"Уникальных посетителей: {len(unique_visitors)} — {unique_visitors}")

# Быстрая проверка принадлежности
banned: set[str] = {"spam@mail.ru", "bad@mail.ru"}
email: str = "spam@mail.ru"
print(f"'{email}' заблокирован: {email in banned}")  # O(1)

# Общие элементы
python_devs: set[str] = {"Alice", "Bob", "Charlie"}
js_devs: set[str] = {"Bob", "Diana", "Charlie"}
fullstack: set[str] = python_devs & js_devs
print(f"Знают оба языка: {fullstack}")

print()

# ===== СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ =====
print("=== ПРОВЕРКА ПРИНАДЛЕЖНОСТИ: list vs set ===\n")

# На больших данных set в разы быстрее list для 'in'
big_list: list[int] = list(range(10_000))
big_set: set[int] = set(range(10_000))

# Оба дают True, но set ищет за O(1), list за O(n)
print(f"9999 in list: {9999 in big_list}")
print(f"9999 in set:  {9999 in big_set}")
print("(set значительно быстрее на больших данных)")

print()

# ===== ПРАКТИЧЕСКИЙ ПРИМЕР: выбор структуры =====
print("=== ПРИМЕР: СИСТЕМА ТЕГОВ ===\n")

# Плохо: list для тегов (дубли, медленный поиск)
tags_bad: list[str] = ["python", "backend", "python", "api"]

# Хорошо: set для тегов (уникальность + быстрая проверка)
tags: set[str] = {"python", "backend", "api"}
tags.add("python")   # дубль игнорируется
print(f"Теги: {tags}")
print(f"Есть 'python': {'python' in tags}")

# Статья с метаданными — dict
article: dict[str, object] = {
    "title": "FastAPI за 5 минут",
    "author": "Alice",
    "tags": tags,
    "views": 1200,
}
print(f"Статья: {article['title']} by {article['author']}, просмотров: {article['views']}")

print()
print("=== ИТОГО: ПРАВИЛО ВЫБОРА ===")
print("""
  Нужны дубли + порядок?             -> list
  Данные фиксированы / ключ словаря? -> tuple
  Поиск по имени / подсчёт?          -> dict
  Уникальность / пересечение?        -> set
""")

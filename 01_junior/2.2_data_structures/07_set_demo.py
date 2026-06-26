# -*- coding: utf-8 -*-
"""
Блок 2.2.4: Множество (set) — коллекция уникальных элементов
════════════════════════════════════════════════════════════════════════

Множество — это НЕУПОРЯДОЧЕННАЯ, ИЗМЕНЯЕМАЯ коллекция УНИКАЛЬНЫХ элементов.
Нет дублей, нет индексов, можно использовать для удаления дубликатов.
"""
from typing import Any

# ===== СОЗДАНИЕ МНОЖЕСТВ =====
print("=== СОЗДАНИЕ МНОЖЕСТВ ===\n")

# Пустое множество (не {}, это пустой словарь!)
empty: set[Any] = set()
print(f"Пустое множество: {empty}")  # set()

# Множество с элементами
numbers = {1, 2, 3, 4, 5}
print(f"Множество чисел: {numbers}")  # {1, 2, 3, 4, 5}

# Множество со строками
colors = {"red", "green", "blue", "yellow"}
print(f"Цвета: {colors}")

# Множество с дублями (дубли удаляются автоматически)
with_duplicates = {1, 2, 2, 3, 3, 3, 4}
print(f"С дублями (они удалены): {with_duplicates}")  # {1, 2, 3, 4}

# Создание из списка (удаляет дубли)
from_list = set([1, 2, 2, 3, 3, 4, 4])
print(f"Из списка: {from_list}")  # {1, 2, 3, 4}

# Создание из строки (каждый символ — элемент)
from_string = set("hello")
print(f"Из строки 'hello': {from_string}")  # {'h', 'e', 'l', 'o'}

print()

# ===== ДОБАВЛЕНИЕ И УДАЛЕНИЕ =====
print("=== ДОБАВЛЕНИЕ И УДАЛЕНИЕ ===\n")

fruits = {"apple", "banana", "cherry"}
print(f"Исходное: {fruits}")

# add() — добавить один элемент
fruits.add("orange")
print(f"После add('orange'): {fruits}")

# add() не вызывает ошибку для дубликата, просто игнорирует его
fruits.add("apple")
print(f"После add('apple') (дубликат): {fruits}")

# remove() — удалить элемент (вызывает ошибку если его нет)
fruits.remove("banana")
print(f"После remove('banana'): {fruits}")

# discard() — удалить элемент (не вызывает ошибку если его нет)
fruits.discard("grape")  # Нет ошибки, хотя grape нет
print(f"После discard('grape'): {fruits}")

# pop() — удалить случайный элемент
random_fruit = fruits.pop()
print(f"pop() удалил: {random_fruit}, осталось: {fruits}")

# clear() — удалить все элементы
temp = {1, 2, 3}
temp.clear()
print(f"После clear(): {temp}")

print()

# ===== ПРОВЕРКА ПРИНАДЛЕЖНОСТИ =====
print("=== ПРОВЕРКА ПРИНАДЛЕЖНОСТИ ===\n")

animals = {"dog", "cat", "bird", "fish"}

# in — проверить наличие элемента
print(f"'dog' in {animals} = {'dog' in animals}")  # True
print(f"'horse' in {animals} = {'horse' in animals}")  # False

# not in
print(f"'snake' not in {animals} = {'snake' not in animals}")  # True

print()

# ===== ОПЕРАЦИИ С МНОЖЕСТВАМИ =====
print("=== ОПЕРАЦИИ С МНОЖЕСТВАМИ ===\n")

set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

# Объединение (union) — все элементы из обоих
union = set_a | set_b
print(f"{set_a} | {set_b} = {union}")  # {1, 2, 3, 4, 5, 6}

union_method = set_a.union(set_b)
print(f"set_a.union(set_b) = {union_method}")

# Пересечение (intersection) — только общие элементы
intersection = set_a & set_b
print(f"{set_a} & {set_b} = {intersection}")  # {3, 4}

intersection_method = set_a.intersection(set_b)
print(f"set_a.intersection(set_b) = {intersection_method}")

# Разность (difference) — элементы из первого, которых нет во втором
difference = set_a - set_b
print(f"{set_a} - {set_b} = {difference}")  # {1, 2}

difference_method = set_a.difference(set_b)
print(f"set_a.difference(set_b) = {difference_method}")

# Симметричная разность (symmetric difference) — элементы, которые есть в одном из множеств
sym_diff = set_a ^ set_b
print(f"{set_a} ^ {set_b} = {sym_diff}")  # {1, 2, 5, 6}

sym_diff_method = set_a.symmetric_difference(set_b)
print(f"set_a.symmetric_difference(set_b) = {sym_diff_method}")

print()

# ===== СРАВНЕНИЕ МНОЖЕСТВ =====
print("=== СРАВНЕНИЕ МНОЖЕСТВ ===\n")

set1 = {1, 2, 3}
set2 = {1, 2, 3}
set3 = {1, 2, 3, 4}

# Равенство
print(f"{set1} == {set2} = {set1 == set2}")  # True
print(f"{set1} == {set3} = {set1 == set3}")  # False

# Подмножество (subset) — все элементы set1 в set3?
print(f"{set1}.issubset({set3}) = {set1.issubset(set3)}")  # True
print(f"set1 <= set3 = {set1 <= set3}")  # True

# Надмножество (superset) — все элементы set3 в set1?
print(f"{set3}.issuperset({set1}) = {set3.issuperset(set1)}")  # True
print(f"set3 >= set1 = {set3 >= set1}")  # True

# Непересекающиеся (disjoint) — нет общих элементов?
set4 = {5, 6, 7}
print(f"{set1}.isdisjoint({set4}) = {set1.isdisjoint(set4)}")  # True

print()

# ===== ИТЕРАЦИЯ =====
print("=== ИТЕРАЦИЯ ===\n")

languages = {"Python", "JavaScript", "Go", "Rust"}
print("Элементы множества:")
for lang in languages:
    print(f"  {lang}")

print()

# ===== МЕТОДЫ МНОЖЕСТВА =====
print("=== МЕТОДЫ МНОЖЕСТВА ===\n")

data = {1, 2, 3, 4, 5}

# len() — количество элементов
print(f"len({data}) = {len(data)}")  # 5

# copy() — копия множества
copy_data = data.copy()
copy_data.add(6)
print(f"Исходное: {data}")
print(f"Копия после добавления 6: {copy_data}")

# max() и min()
print(f"max({data}) = {max(data)}")  # 5
print(f"min({data}) = {min(data)}")  # 1

# sum() — сумма всех элементов
print(f"sum({data}) = {sum(data)}")  # 15

print()

# ===== SET COMPREHENSION =====
print("=== SET COMPREHENSION ===\n")

# Создать множество четных чисел
even_numbers = {x for x in range(1, 11) if x % 2 == 0}
print(f"Четные числа от 1 до 10: {even_numbers}")  # {2, 4, 6, 8, 10}

# Множество квадратов
squares = {x**2 for x in range(1, 6)}
print(f"Квадраты 1-5: {squares}")  # {1, 4, 9, 16, 25}

# Удалить дубли из списка с comprehension
numbers_list = [1, 2, 2, 3, 3, 3, 4, 4]
unique = {x for x in numbers_list}
print(f"Уникальные числа из {numbers_list}: {unique}")  # {1, 2, 3, 4}

print()

# ===== ПРАКТИЧЕСКИЙ ПРИМЕР =====
print("=== ПРАКТИЧЕСКИЙ ПРИМЕР ===\n")

# Найти общие навыки двух разработчиков
dev1_skills = {"Python", "JavaScript", "SQL", "Docker"}
dev2_skills = {"Python", "Go", "Kubernetes", "SQL"}

common = dev1_skills & dev2_skills
print(f"Общие навыки: {common}")  # {'Python', 'SQL'}

only_dev1 = dev1_skills - dev2_skills
print(f"Только у разработчика 1: {only_dev1}")  # {'JavaScript', 'Docker'}

all_skills = dev1_skills | dev2_skills
print(f"Все навыки: {all_skills}")  # {'Python', 'JavaScript', 'SQL', 'Docker', 'Go', 'Kubernetes'}

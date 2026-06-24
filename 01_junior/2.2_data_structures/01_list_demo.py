# -*- coding: utf-8 -*-
"""
Блок 2.2.1: Список (list) — базовые операции
════════════════════════════════════════════════════════════════════════

Список — это упорядоченная, изменяемая коллекция элементов.
Элементы могут быть разных типов. Доступ по индексу (0, 1, 2, ...).
"""

# ===== СОЗДАНИЕ СПИСКОВ =====
print("=== СОЗДАНИЕ СПИСКОВ ===\n")

# Пустой список
empty = []
print(f"Пустой список: {empty}")  # []

# Список с элементами
numbers = [1, 2, 3, 4, 5]
print(f"Числа: {numbers}")  # [1, 2, 3, 4, 5]

# Список с разными типами
mixed: list[object] = [1, "hello", 3.14, True, None]
print(f"Смешанные типы: {mixed}")  # [1, 'hello', 3.14, True, None]

# Список из другого списка (копия поверхностная)
copy_list = list(numbers)
print(f"Копия списка: {copy_list}")  # [1, 2, 3, 4, 5]

print()

# ===== ИНДЕКСИРОВАНИЕ (доступ по индексу) =====
print("=== ИНДЕКСИРОВАНИЕ (доступ по индексу) ===\n")

students = ["Alice", "Bob", "Charlie", "Diana", "Eve"]
print(f"Список студентов: {students}")

# Индекс начинается с 0
print(f"students[0] = {students[0]}")  # Alice
print(f"students[1] = {students[1]}")  # Bob
print(f"students[-1] = {students[-1]}")  # Eve (последний)
print(f"students[-2] = {students[-2]}")  # Diana (предпоследний)

print()

# ===== СРЕЗЫ (SLICING) =====
print("=== СРЕЗЫ (list[start:stop:step]) ===\n")

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"Исходный список: {numbers}")

# list[start:stop] — от start до stop-1 (stop исключительно)
print(f"numbers[2:5] = {numbers[2:5]}")  # [2, 3, 4]
print(f"numbers[:3] = {numbers[:3]}")    # [0, 1, 2] (с начала)
print(f"numbers[5:] = {numbers[5:]}")    # [5, 6, 7, 8, 9] (до конца)
print(f"numbers[::2] = {numbers[::2]}")  # [0, 2, 4, 6, 8] (каждый второй)
print(f"numbers[::-1] = {numbers[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0] (развернуть)

print()

# ===== ОСНОВНЫЕ МЕТОДЫ СПИСКА =====
print("=== ОСНОВНЫЕ МЕТОДЫ СПИСКА ===\n")

# append() — добавить элемент в конец
fruits = ["apple", "banana"]
fruits.append("cherry")
print(f"После append('cherry'): {fruits}")  # ['apple', 'banana', 'cherry']

# insert(index, element) — вставить на позицию
fruits.insert(1, "orange")
print(f"После insert(1, 'orange'): {fruits}")  # ['apple', 'orange', 'banana', 'cherry']

# remove(element) — удалить первый элемент со значением
fruits.remove("orange")
print(f"После remove('orange'): {fruits}")  # ['apple', 'banana', 'cherry']

# pop(index) — удалить элемент по индексу и вернуть его
last = fruits.pop()  # удалит последний
print(f"pop() удалил: {last}, остаток: {fruits}")  # cherry, ['apple', 'banana']

# pop(1) — удалить элемент по индексу
fruits.pop(0)  # удалит первый
print(f"pop(0) удалил первый, остаток: {fruits}")  # ['banana']

# extend() — добавить все элементы из другого списка
nums = [1, 2, 3]
nums.extend([4, 5])
print(f"После extend([4, 5]): {nums}")  # [1, 2, 3, 4, 5]

# len() — длина списка
print(f"len([1, 2, 3]) = {len([1, 2, 3])}")  # 3

# count() — подсчитать вхождения элемента
duplicates = [1, 2, 2, 3, 2, 4]
print(f"duplicates.count(2) = {duplicates.count(2)}")  # 3

# index() — найти индекс первого вхождения
print(f"duplicates.index(2) = {duplicates.index(2)}")  # 1

# clear() — удалить все элементы
temp = [1, 2, 3]
temp.clear()
print(f"После clear(): {temp}")  # []

print()

# ===== СОРТИРОВКА =====
print("=== СОРТИРОВКА ===\n")

# sort() — сортирует список на месте
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(f"После sort(): {numbers}")  # [1, 1, 2, 3, 4, 5, 6, 9]

# sort(reverse=True) — сортировка в обратном порядке
numbers.sort(reverse=True)
print(f"После sort(reverse=True): {numbers}")  # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() — функция, возвращает новый отсортированный список
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(f"sorted({original}) = {sorted_list}")  # [1, 1, 3, 4, 5]
print(f"Исходный не изменился: {original}")  # [3, 1, 4, 1, 5]

print()

# ===== ПРОВЕРКА ПРИНАДЛЕЖНОСТИ (in) =====
print("=== ПРОВЕРКА ПРИНАДЛЕЖНОСТИ (in) ===\n")

colors = ["red", "green", "blue"]
print(f"'red' in {colors} = {'red' in colors}")  # True
print(f"'yellow' in {colors} = {'yellow' in colors}")  # False

print()

# ===== ИТЕРАЦИЯ (цикл) =====
print("=== ИТЕРАЦИЯ (цикл for) ===\n")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"  {fruit}")

# С индексом (enumerate)
print("\nС индексом (enumerate):")
for i, fruit in enumerate(fruits):
    print(f"  [{i}] {fruit}")

print()

# ===== ИЗМЕНЯЕМОСТЬ (MUTABLE) =====
print("=== ИЗМЕНЯЕМОСТЬ ===\n")

list1 = [1, 2, 3]
list2 = list1  # Ссылка на тот же список, не копия!

list1.append(4)
print(f"Добавили 4 в list1")
print(f"list1 = {list1}")  # [1, 2, 3, 4]
print(f"list2 = {list2}")  # [1, 2, 3, 4] — изменилась тоже!

print("\nЕсли нужна копия, используй list() или [:]:")
list3 = [1, 2, 3]
list4 = list(list3)  # или list4 = list3[:] — настоящая копия
list3.append(4)
print(f"list3 = {list3}")  # [1, 2, 3, 4]
print(f"list4 = {list4}")  # [1, 2, 3] — не изменилась

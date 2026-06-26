# -*- coding: utf-8 -*-
"""
Блок 2.2.5: Comprehensions — списковые, словарные, множественные выражения
════════════════════════════════════════════════════════════════════════════

Comprehension — это компактный способ создать коллекцию из другой коллекции.
Вместо цикла + append() — одно выражение в одну строку.

Синтаксис:
  [выражение for элемент in итерируемое]
  [выражение for элемент in итерируемое if условие]
"""

# ===== LIST COMPREHENSION — БАЗОВЫЙ СИНТАКСИС =====
print("=== LIST COMPREHENSION: БАЗОВЫЙ СИНТАКСИС ===\n")

# Без comprehension:
squares_loop: list[int] = []
for x in range(1, 6):
    squares_loop.append(x ** 2)
print(f"Через цикл:         {squares_loop}")

# С comprehension — то же самое, одной строкой:
squares: list[int] = [x ** 2 for x in range(1, 6)]
print(f"Через comprehension: {squares}")
# [1, 4, 9, 16, 25]

print()

# Любое выражение — не только x**2
doubled: list[int] = [x * 2 for x in range(1, 6)]
print(f"Удвоенные: {doubled}")  # [2, 4, 6, 8, 10]

upper_words: list[str] = [word.upper() for word in ["hello", "world", "python"]]
print(f"Заглавные: {upper_words}")  # ['HELLO', 'WORLD', 'PYTHON']

lengths: list[int] = [len(word) for word in ["cat", "elephant", "fox"]]
print(f"Длины слов: {lengths}")  # [3, 8, 3]

print()

# ===== LIST COMPREHENSION С УСЛОВИЕМ (ФИЛЬТРАЦИЯ) =====
print("=== LIST COMPREHENSION С УСЛОВИЕМ ===\n")

# Только чётные числа
evens: list[int] = [x for x in range(1, 11) if x % 2 == 0]
print(f"Чётные от 1 до 10: {evens}")  # [2, 4, 6, 8, 10]

# Только положительные
numbers: list[int] = [-3, -1, 0, 2, 4, -2, 7]
positives: list[int] = [x for x in numbers if x > 0]
print(f"Положительные из {numbers}: {positives}")  # [2, 4, 7]

# Фильтрация строк
words: list[str] = ["apple", "banana", "avocado", "cherry", "apricot"]
a_words: list[str] = [w for w in words if w.startswith("a")]
print(f"Слова на 'a': {a_words}")  # ['apple', 'avocado', 'apricot']

# Длинные слова
long_words: list[str] = [w for w in words if len(w) > 6]
print(f"Длиннее 6 букв: {long_words}")  # ['banana', 'avocado', 'apricot']

print()

# ===== ВЫРАЖЕНИЕ + УСЛОВИЕ =====
print("=== ВЫРАЖЕНИЕ И УСЛОВИЕ ВМЕСТЕ ===\n")

# Квадраты только чётных
even_squares: list[int] = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(f"Квадраты чётных: {even_squares}")  # [4, 16, 36, 64, 100]

# Верхний регистр только длинных слов
big_upper: list[str] = [w.upper() for w in words if len(w) >= 6]
print(f"Длинные в верхнем: {big_upper}")

print()

# ===== ВЛОЖЕННЫЕ LIST COMPREHENSIONS =====
print("=== ВЛОЖЕННЫЕ COMPREHENSIONS ===\n")

# Таблица умножения 3x3 — список кортежей
pairs: list[tuple[int, int]] = [(x, y) for x in range(1, 4) for y in range(1, 4)]
print(f"Все пары (1-3) x (1-3): {pairs}")

# Эквивалент двойного цикла:
# for x in range(1, 4):
#     for y in range(1, 4):
#         pairs.append((x, y))

# Сглаживание (flatten) вложенного списка
matrix: list[list[int]] = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat: list[int] = [num for row in matrix for num in row]
print(f"Матрица сглажена: {flat}")  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

print()

# ===== ТЕРНАРНОЕ ВЫРАЖЕНИЕ В COMPREHENSION =====
print("=== ТЕРНАРНОЕ ВЫРАЖЕНИЕ ===\n")

# «если чётное — 'even', иначе — 'odd'»
labels: list[str] = ["even" if x % 2 == 0 else "odd" for x in range(1, 7)]
print(f"Метки: {labels}")  # ['odd', 'even', 'odd', 'even', 'odd', 'even']

# Заменить отрицательные на 0
data: list[int] = [-2, 5, -1, 8, -4, 3]
clamped: list[int] = [x if x > 0 else 0 for x in data]
print(f"Без отрицательных: {clamped}")  # [0, 5, 0, 8, 0, 3]

print()

# ===== DICT COMPREHENSION =====
print("=== DICT COMPREHENSION ===\n")

# Базовый синтаксис: {ключ: значение for элемент in итерируемое}
squares_dict: dict[int, int] = {x: x ** 2 for x in range(1, 6)}
print(f"Квадраты (dict): {squares_dict}")
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Из двух списков через zip
keys: list[str] = ["name", "age", "city"]
values: list[str | int] = ["Alice", 30, "Moscow"]
person: dict[str, str | int] = {k: v for k, v in zip(keys, values)}
print(f"Из zip: {person}")
# {'name': 'Alice', 'age': 30, 'city': 'Moscow'}

# Инвертировать словарь (ключи ↔ значения)
original: dict[str, int] = {"a": 1, "b": 2, "c": 3}
inverted: dict[int, str] = {v: k for k, v in original.items()}
print(f"Инвертированный: {inverted}")  # {1: 'a', 2: 'b', 3: 'c'}

# Отфильтровать словарь
scores: dict[str, int] = {"Alice": 85, "Bob": 42, "Charlie": 91, "Diana": 67}
passing: dict[str, int] = {name: score for name, score in scores.items() if score >= 70}
print(f"Сдавшие (>=70): {passing}")
# {'Alice': 85, 'Charlie': 91}

print()

# ===== SET COMPREHENSION =====
print("=== SET COMPREHENSION ===\n")

# Базовый синтаксис: {выражение for элемент in итерируемое}
even_set: set[int] = {x for x in range(1, 11) if x % 2 == 0}
print(f"Чётные (set): {even_set}")  # {2, 4, 6, 8, 10}

# Уникальные длины слов
word_list: list[str] = ["cat", "dog", "elephant", "fox", "bee", "ant"]
unique_lengths: set[int] = {len(w) for w in word_list}
print(f"Уникальные длины: {unique_lengths}")  # {3, 8} (порядок не гарантирован)

# Уникальные первые буквы
first_letters: set[str] = {w[0] for w in word_list}
print(f"Первые буквы: {first_letters}")

print()

# ===== GENERATOR EXPRESSION =====
print("=== GENERATOR EXPRESSION ===\n")

# Похож на list comprehension, но в круглых скобках.
# НЕ создаёт весь список в памяти — вычисляет элементы по одному (лениво).
gen = (x ** 2 for x in range(1, 6))
print(f"Тип: {type(gen)}")  # <class 'generator'>

# Использовать в sum/max/min напрямую — экономия памяти
total: int = sum(x ** 2 for x in range(1, 101))
print(f"Сумма квадратов 1-100: {total}")  # 338350

# Когда нужен список — list comprehension.
# Когда нужно только пройтись или посчитать — generator expression.

print()

# ===== КОГДА ИСПОЛЬЗОВАТЬ COMPREHENSION =====
print("=== КОГДА ИСПОЛЬЗОВАТЬ ===\n")

print("""
[OK] Используй comprehension когда:
   - Одна операция над каждым элементом
   - Простое условие фильтрации (if)
   - Результат -- список / словарь / множество

[NO] НЕ используй comprehension когда:
   - Внутри несколько операций (лучше обычный цикл)
   - Глубокая вложенность (>2 уровня) -- трудно читать
   - Нужны side-эффекты (print, запись в файл)

Правило: если comprehension не читается с первого взгляда -- пиши цикл.
""")

# ПРИМЕР: вложенность > 2 уровней — лучше цикл
# Плохо (трудно читать):
# result = [cell for row in matrix for cell in row if cell > 0]
# Лучше:
result: list[int] = []
for row in matrix:
    for cell in row:
        if cell > 0:
            result.append(cell)
print(f"Положительные из матрицы: {result}")

print()
print("=== ИТОГО ===")
print("""
list comprehension  : [expr for x in iter if cond]
dict comprehension  : {k: v for x in iter if cond}
set comprehension   : {expr for x in iter if cond}
generator expr      : (expr for x in iter if cond)
""")

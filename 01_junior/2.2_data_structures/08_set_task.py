# -*- coding: utf-8 -*-
"""
Блок 2.2.4: Практика с множествами (set)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Напиши свой код и выведи результаты.

Совет: Если застрял — посмотри 07_set_demo.py, но старайся решить сам.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Создание множеств и удаление дубликатов")
print("=" * 60)
print("""
1.1 Создай множество из списка [1, 2, 2, 3, 3, 3, 4]
    Выведи множество (дубли должны исчезнуть)

1.2 Создай множество из строки "hello"
    Выведи, сколько уникальных букв в строке (len)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:

list_to_set = set([1, 2, 2, 3, 3, 3, 4])
print(list_to_set)
hello_set = set("hello")
print(hello_set)

for char in hello_set:
    if char not in hello_set:
        print(char)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Добавление и удаление элементов")
print("=" * 60)
print("""
2.1 Создай множество {"apple", "banana", "cherry"}
    Добавь "orange" через add()
    Напечатай результат

2.2 Удали "banana" через remove()
    Напечатай результат

2.3 Используй discard() для удаления элемента, которого нет
    Напечатай результат (ошибки быть не должно)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

fruits.discard("pineapple")
print(fruits)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Проверка принадлежности и размер")
print("=" * 60)
print("""
3.1 Создай множество {"Python", "JavaScript", "Go"}
    Проверь через 'in' есть ли "Python" и "Rust"
    Напечатай результаты

3.2 Напечатай количество элементов через len()

3.3 Найди максимальный и минимальный элемент (в алфавитном порядке)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
languages = {"Python", "JavaScript", "Go"}
has_python_and_rust = "Python" and "Rust" in languages
print(has_python_and_rust)
print(len(languages))

# min_lang = min(len(languages["Python"]))
# 3.3 Найди максимальный и минимальный элемент (в алфавитном порядке) Не понял что нужно? Как можно найти мин и мах у строки?

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Операции с множествами (объединение, пересечение)")
print("=" * 60)
print("""
4.1 Создай два множества:
    A = {1, 2, 3, 4}
    B = {3, 4, 5, 6}
    Найди объединение (все элементы из обоих)
    Напечатай результат

4.2 Найди пересечение (только общие элементы)
    Напечатай результат

4.3 Найди разность (элементы из A, которых нет в B)
    Напечатай результат
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
union = A.union(B)
print(union)

C = A.intersection(B)
print(C)

D = A.difference(B)
print(D)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Симметричная разность и сравнение")
print("=" * 60)
print("""
5.1 Используя множества A и B из задания 4:
    Найди симметричную разность (элементы, которые есть в одном из них)
    Напечатай результат

5.2 Проверь, является ли A подмножеством B (все ли элементы A в B?)
    Напечатай результат

5.3 Проверь, имеют ли множества {1, 2} и {3, 4} общие элементы
    Используй isdisjoint()
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
A_2 = {1, 2, 3, 4}
B_2 = {3, 4, 5, 6}

sym_diff = A_2.symmetric_difference(B_2)
print(sym_diff)

result_is_subset = A_2.issubset(B_2)
print(result_is_subset)

is_disjoint = A.isdisjoint(B_2)
print(is_disjoint)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Итерация и копирование")
print("=" * 60)
print("""
6.1 Создай множество {"a", "b", "c", "d"}
    Пройди по каждому элементу через for и напечатай его

6.2 Создай копию этого множества
    Добавь "e" в копию
    Напечатай оба множества (исходное не должно измениться)

6.3 Напечатай сумму элементов множества {1, 2, 3, 4, 5}
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
letters = {"a", "b", "c", "d"}
for letter in letters:
    print(letter)

letters_copy = letters.copy()
letters_copy.add("e")

print(letters)
print(letters_copy)

print(sum({1, 2, 3, 4, 5}))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Set Comprehension")
print("=" * 60)
print("""
7.1 Создай множество четных чисел от 1 до 10 через comprehension
    {2, 4, 6, 8, 10}

7.2 Создай множество кубов чисел от 1 до 5 через comprehension
    {1, 8, 27, 64, 125}

7.3 Создай множество длин слов из списка:
    ["hello", "world", "python", "code"]
    (какие разные длины слов?)
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
evens = {x for x in range(1, 11) if x % 2 == 0}
print(evens)

squares = {x**3 for x in range(1, 6)}
print(squares)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Практическое применение")
print("=" * 60)
print("""
8.1 У тебя есть два списка покупок:
    lista = ["яблоко", "банан", "апельсин", "яблоко", "банан"]
    listb = ["банан", "груша", "апельсин", "груша", "груша"]

    Найди продукты, которые есть в ОБОИХ списках
    Найди продукты ТОЛЬКО в первом списке
    Найди ВСЕ уникальные продукты

8.2 Дан текст: "the quick brown fox jumps over the lazy dog"
    Найди ВСЕ уникальные буквы (без пробелов)
    Напечатай их количество
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
list_a = ["яблоко", "банан", "апельсин", "яблоко", "банан"]
list_b = ["банан", "груша", "апельсин", "груша", "груша"]

list_to_set_a = set(list_a)
list_to_set_b = set(list_b)

both_product = list_to_set_a.intersection(list_to_set_b)
only_one_list = list_to_set_a.difference(list_to_set_b)
unique_list = list_to_set_a.union(list_to_set_b)

text = "the quick brown fox jumps over the lazy dog"
letters = set(text) - {""}
print(len(letters))

print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

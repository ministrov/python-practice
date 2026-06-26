# -*- coding: utf-8 -*-
"""
Блок 2.2.5: Практика — Comprehensions
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Напиши свой код и выведи результаты.

Совет: Если застрял — посмотри 09_list_comprehensions_demo.py.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Базовый list comprehension")
print("=" * 60)
print("""
1.1 Создай список кубов чисел от 1 до 5 через comprehension
    Ожидаемый результат: [1, 8, 27, 64, 125]

1.2 Создай список из заглавных версий слов:
    ["python", "java", "go", "rust"]
    Ожидаемый результат: ['PYTHON', 'JAVA', 'GO', 'RUST']

1.3 Создай список длин слов из того же списка
    Ожидаемый результат: [6, 4, 2, 4]
""")

# ТВОЙ КОД ЗДЕСЬ:
cubed = [x ** 3 for x in range(1, 6)]
print(cubed)

words = ["python", "java", "go", "rust"]
upper_case_words = [word.upper() for word in words]

print(upper_case_words)

lengths = [len(word) for word in words]
print(lengths)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Comprehension с фильтрацией (if)")
print("=" * 60)
print("""
2.1 Из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    получи только нечётные числа
    Ожидаемый результат: [1, 3, 5, 7, 9]

2.2 Из списка слов ["cat", "dog", "elephant", "ox", "bear"]
    получи только слова длиннее 3 букв
    Ожидаемый результат: ['elephant', 'bear']

2.3 Из списка чисел [-5, -3, 0, 2, -1, 8, 4]
    получи только отрицательные
    Ожидаемый результат: [-5, -3, -1]
""")

# ТВОЙ КОД ЗДЕСЬ:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds = [num for num in numbers if num % 2 == 1]
print(odds)

animals = ["cat", "dog", "elephant", "ox", "bear"]
words_more_than_three = [word for word in animals if len(word) > 3]
print(words_more_than_three)

numbers_2 = [-5, -3, 0, 2, -1, 8, 4]
negative_numbers = [num for num in numbers_2 if num < 0]
print(negative_numbers)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Выражение + условие")
print("=" * 60)
print("""
3.1 Создай список квадратов чётных чисел от 1 до 10
    Ожидаемый результат: [4, 16, 36, 64, 100]

3.2 Из списка ["hello", "world", "hi", "python", "ok"]
    получи заглавные версии слов длиннее 3 букв
    Ожидаемый результат: ['HELLO', 'WORLD', 'PYTHON']

3.3 Из списка чисел [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    создай список: если число чётное - умножь на 2, если нечётное - умножь на 3
    (тернарное выражение в comprehension)
    Ожидаемый результат: [3, 4, 9, 8, 15, 12, 21, 16, 27, 20]
""")

# ТВОЙ КОД ЗДЕСЬ:
squares = [x ** 2 for x in range(1, 11) if x % 2 == 0]
print(squares)

words = ["hello", "world", "hi", "python", "ok"]
upper_words = [word.upper() for word in words if len(word) > 3]
print(upper_words)

numbers_3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_and_odds = [num * 2 if num % 2 == 0 else num * 3 for num in numbers_3]
print(evens_and_odds)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Dict comprehension")
print("=" * 60)
print("""
4.1 Создай словарь {число: квадрат} для чисел от 1 до 5
    Ожидаемый результат: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

4.2 Из словаря {"Alice": 55, "Bob": 80, "Charlie": 45, "Diana": 90}
    оставь только тех, у кого оценка >= 60
    Ожидаемый результат: {'Bob': 80, 'Diana': 90}

4.3 Создай словарь {слово: длина} для списка ["cat", "dog", "python"]
    Ожидаемый результат: {'cat': 3, 'dog': 3, 'python': 6}
""")

# ТВОЙ КОД ЗДЕСЬ:
dict_squares = {x: x ** 2 for x in range(1, 6)}
print(dict_squares)

some_dict: dict[str, int] = {"Alice": 55,
                             "Bob": 80, "Charlie": 45, "Diana": 90}
new_dict: dict[str, int] = {name: score for name,
                            score in some_dict.items() if score >= 60}
print(new_dict)

any_words = ["cat", "dog", "python"]
new_words = {w: len(w) for w in any_words}
print(new_words)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Set comprehension")
print("=" * 60)
print("""
5.1 Создай множество квадратов чисел от 1 до 5
    Ожидаемый результат: {1, 4, 9, 16, 25}

5.2 Из списка ["Hello", "WORLD", "Python", "hello", "world"]
    создай множество уникальных слов в нижнем регистре
    Ожидаемый результат: {'hello', 'world', 'python'}

5.3 Из списка [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    создай множество остатков от деления на 3
    Ожидаемый результат: {0, 1, 2}
""")

# ТВОЙ КОД ЗДЕСЬ:
set_of_squares = {x ** 2 for x in range(1, 6)}
print(set_of_squares)

any_words_2 = ["Hello", "WORLD", "Python", "hello", "world"]
new_any_words = {word.lower() for word in any_words_2}
print(new_any_words)

numbers_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
set_of_numbers_4 = {num % 3 for num in numbers_4}
print(set_of_numbers_4)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Работа со строками")
print("=" * 60)
print("""
6.1 Из строки "Hello World Python"
    создай список отдельных слов в нижнем регистре
    Подсказка: используй split()
    Ожидаемый результат: ['hello', 'world', 'python']

6.2 Из той же строки создай список длин каждого слова
    Ожидаемый результат: [5, 5, 6]

6.3 Из списка строк ["  hello  ", "  world  ", "  python  "]
    убери пробелы у каждой строки через strip()
    Ожидаемый результат: ['hello', 'world', 'python']
""")

# ТВОЙ КОД ЗДЕСЬ:
text_str = "Hello World Python"
splitted_text = text_str.split()
new_words_2 = [word.lower() for word in splitted_text]
print(new_words_2)

lengths_text_str = [len(word) for word in splitted_text]
print(lengths_text_str)

trim_words = ["  hello  ", "  world  ", "  python  "]
trimmed_words = [word.strip().lower() for word in splitted_text]
print(trimmed_words)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Вложенный comprehension")
print("=" * 60)
print("""
7.1 Создай список всех пар (x, y), где x из [1, 2, 3], y из [10, 20]
    Ожидаемый результат: [(1, 10), (1, 20), (2, 10), (2, 20), (3, 10), (3, 20)]

7.2 Сгладь (flatten) вложенный список [[1, 2], [3, 4], [5, 6]]
    в один плоский список
    Ожидаемый результат: [1, 2, 3, 4, 5, 6]

7.3 Создай список только положительных чисел из матрицы:
    matrix = [[-1, 2, -3], [4, -5, 6], [-7, 8, 9]]
    Ожидаемый результат: [2, 4, 6, 8, 9]
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Практическое применение")
print("=" * 60)
print("""
8.1 Дан список температур в Цельсиях: [0, 20, 37, 100, -10, 15]
    Переведи каждую в Фаренгейты по формуле: F = C * 9/5 + 32
    Округли до 1 знака (round(x, 1))
    Ожидаемый результат: [32.0, 68.0, 98.6, 212.0, 14.0, 59.0]

8.2 Дан список слов: ["banana", "apple", "cherry", "date", "elderberry"]
    Создай словарь {слово: количество_гласных} для слов длиннее 4 букв
    Гласные: a, e, i, o, u
    Ожидаемый результат: {'banana': 3, 'apple': 2, 'cherry': 1, 'elderberry': 4}

8.3 Дан текст: "the quick brown fox"
    Найди все уникальные буквы, которые встречаются более 1 раза
    (set comprehension + условие)
    Ожидаемый результат: {'h', 'o', 'e', 'k', 'r', 'u', 'n', ...}
    (точный набор зависит от текста — проверь логику)
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

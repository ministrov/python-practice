# -*- coding: utf-8 -*-
"""
Блок 2.2.3: Практика со словарями (dict)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Напиши свой код и выведи результаты.

Совет: Если застрял — посмотри 05_dict_demo.py, но старайся решить сам.
"""
from collections.abc import ValuesView

print("=" * 60)
print("ЗАДАНИЕ 1: Создание словарей и доступ к элементам")
print("=" * 60)
print("""
1.1 Создай словарь с информацией о фильме:
    - название (название)
    - год (год)
    - рейтинг (рейтинг)
    Напечатай каждый элемент по ключу

1.2 Используй get() для доступа к элементу "режиссер" (которого нет)
    Выведи значение по умолчанию
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
film_info: dict[str, str | int | float] = {
    "name": "Agent 007",
    "year": 1967,
    "rating": 4.7
}

print(film_info["name"])
print(film_info["rating"])
print(film_info["year"])
print(film_info.get("director"))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Изменение и добавление элементов")
print("=" * 60)
print("""
2.1 Создай словарь автомобиля:
    {"brand": "Toyota", "model": "Camry", "year": 2020}
    Измени год на 2023
    Добавь новый ключ "color": "blue"
    Напечатай финальный словарь

2.2 Используй update() для добавления нескольких ключей:
    {"engine": "V6", "fuel": "gasoline"}
    Напечатай словарь после update
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
car_info: dict[str, str | int] = {
    "brand": "Toyota", "model": "Camry", "year": 2020}
car_info["year"] = 2023
car_info["color"] = "blue"
print(car_info)
car_info.update({"engine": "V6", "fuel": "gasoline"})
print(car_info)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Удаление элементов")
print("=" * 60)
print("""
3.1 Создай словарь {"a": 1, "b": 2, "c": 3, "d": 4}
    Удали "b" через del
    Напечатай результат

3.2 Используй pop() для удаления "c" и сохранения значения
    Напечатай, что было удалено и что осталось

3.3 Попробуй pop() на несуществующий ключ с значением по умолчанию
    Напечатай результат
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
letter_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4}
del letter_dict["b"]
print(letter_dict)
deleted_c_value = letter_dict.pop("c")
print(deleted_c_value)
print(letter_dict)

print(letter_dict.pop("z", "default value"))
print(letter_dict)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Проверка и итерация")
print("=" * 60)
print("""
4.1 Создай словарь {"x": 10, "y": 20, "z": 30}
    Проверь наличие ключа "x" (in)
    Проверь наличие ключа "w"

4.2 Напечатай все КЛЮЧИ словаря

4.3 Напечатай все ЗНАЧЕНИЯ словаря

4.4 Напечатай все ПАРЫ ключ-значение
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
coordinate: dict[str, int] = {"x": 10, "y": 20, "z": 30}
print("x" in coordinate)
print("w" in coordinate)
for key in coordinate:
    print(f"Key: {key}")

for value in coordinate.values():
    print(f"Value: {value}")

for key, value in coordinate.items():
    print(f"Key: {key}, Value: {value}")

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Итерация по словарю")
print("=" * 60)
print("""
5.1 Создай словарь оценок: {"Alice": 95, "Bob": 87, "Charlie": 92}
    Напечатай все пары через цикл for

5.2 Умножь каждую оценку на 1.1 и напечатай результаты
    (используй keys() или items())

5.3 Найди среднюю оценку (используй values())
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
grades: dict[str, float] = {"Alice": 95, "Bob": 87, "Charlie": 92}
for key, value in grades.items():
    print(f"KEY: {key}, VALUE: {value}")

for key in grades:
    grades[key] *= 1.1
    print(grades[key])

grades_values: ValuesView[float] = grades.values()
sum_grades: float = 0
for i in grades_values:
    sum_grades += i

average = sum_grades / len(grades_values)
print(average)
print(grades_values)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Вложенные словари")
print("=" * 60)
print("""
6.1 Создай словарь с информацией о студентах:
    {
        "alice": {"age": 20, "grade": "A"},
        "bob": {"age": 21, "grade": "B"}
    }
    Напечатай возраст Alice
    Напечатай оценку Bob

6.2 Добавь нового студента "charlie": {"age": 19, "grade": "A+"}

6.3 Измени оценку Bob на "A"

6.4 Напечатай весь словарь
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
students_info: dict[str, dict[str, int | str]] = {
    "alice": {"age": 20, "grade": "A"},
    "bob": {"age": 21, "grade": "B"}
}

print(students_info["alice"]["age"])
print(students_info["bob"]["grade"])
students_info["charlie"] = {"age": 19, "grade": "A+"}
print(students_info)
students_info["bob"]["grade"] = "A"
print(students_info)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Методы и копирование")
print("=" * 60)
print("""
7.1 Создай словарь {"a": 1, "b": 2}
    Сделай копию через copy()
    Измени копию: добавь "c": 3
    Напечатай оба словаря (исходный не должен измениться)

7.2 Используй setdefault():
    - Получи значение "a" (существует)
    - Получи значение "d" со значением по умолчанию 4
    Напечатай словарь после setdefault()

7.3 Найди количество элементов через len()
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
some_dict: dict[str, int] = {"a": 1, "b": 2}
new_some_dict = some_dict.copy()
print(some_dict)
print(new_some_dict)
new_some_dict["c"] = 3
print(some_dict)
print(new_some_dict)
some_dict.setdefault("a", 10)
some_dict.setdefault("d", 4)
print(some_dict)
print(len(some_dict))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Dictionary Comprehension")
print("=" * 60)
print("""
8.1 Создай словарь квадратов чисел от 1 до 5 через comprehension
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

8.2 Создай словарь с comprehension, где только четные числа:
    {2: 4, 4: 16}

8.3 Инвертируй словарь (ключи <-> значения) через comprehension:
    Исходный: {"a": 1, "b": 2, "c": 3}
    Результат: {1: "a", 2: "b", 3: "c"}
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:
some_squares: dict[int, int] = {x: x**2 for x in range(1, 6)}
print(some_squares)
even_squares: dict[int, int] = {x: x**2 for x in range(1, 5) if x % 2 == 0}
print(even_squares)
main_squares: dict[str, int] = {"a": 1, "b": 2, "c": 3}
result_squares = {v: k for k, v in main_squares.items()}
print(result_squares)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 9: Подсчёт частот")
print("=" * 60)
print("""
9.1 Подсчитай, сколько раз каждая буква встречается в строке:
    text = "hello world"
    Ожидаемый результат: {"h": 1, "e": 1, "l": 3, ...}
    (пробел тоже считается)

9.2 Подсчитай, сколько раз каждое слово встречается в тексте:
    text = "the cat sat on the mat the cat"
    Ожидаемый результат: {"the": 3, "cat": 2, ...}

9.3 Найди самое частое слово из 9.2
""")

# ТВОЙ КОД ЗДЕСЬ:
text = "hello world"
count_chars = {}

for char in text:
    if char in count_chars:
        count_chars[char] += 1
    else:
        count_chars[char] = 1

print(count_chars)

text_2 = "the cat sat on the mat the cat"
count_sub_text = {}
words_from_text_2 = text_2.split()

for word in words_from_text_2:
    if word in count_sub_text:
        count_sub_text[word] += 1
    else:
        count_sub_text[word] = 1

print(count_sub_text)

most_common_word = None
max_count = 0

for word_2 in count_sub_text:
    if count_sub_text[word_2] > max_count:
        max_count = count_sub_text[word_2]
        most_common_word = word_2

print(most_common_word, max_count)


print("\n" + "=" * 60)
print("ЗАДАНИЕ 10: Слияние словарей")
print("=" * 60)
print("""
10.1 Объедини два словаря через распаковку **:
    dict1 = {"a": 1, "b": 2}
    dict2 = {"c": 3, "d": 4}
    Ожидаемый результат: {"a": 1, "b": 2, "c": 3, "d": 4}

10.2 Объедини словари так, чтобы значения из dict2 перезаписали dict1:
    dict1 = {"a": 1, "b": 2, "x": 99}
    dict2 = {"b": 20, "c": 3}
    Ожидаемый результат: {"a": 1, "b": 20, "x": 99, "c": 3}

10.3 Используй оператор | (Python 3.9+) для слияния dict1 и dict2 из 10.2
    Напечатай результат
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 11: Сортировка словаря")
print("=" * 60)
print("""
11.1 Отсортируй словарь по КЛЮЧАМ (по алфавиту):
    scores = {"charlie": 85, "alice": 92, "bob": 78}
    Ожидаемый результат: {"alice": 92, "bob": 78, "charlie": 85}

11.2 Отсортируй тот же словарь по ЗНАЧЕНИЯМ (по возрастанию):
    Ожидаемый результат: {"bob": 78, "charlie": 85, "alice": 92}

11.3 Отсортируй по значениям в УБЫВАЮЩЕМ порядке (reverse=True):
    Ожидаемый результат: {"alice": 92, "charlie": 85, "bob": 78}
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 12: Создание словаря из двух списков")
print("=" * 60)
print("""
12.1 Создай словарь из двух списков через zip():
    keys = ["name", "age", "city"]
    values = ["Anna", 25, "Moscow"]
    Ожидаемый результат: {"name": "Anna", "age": 25, "city": "Moscow"}

12.2 Создай словарь через dict comprehension + zip():
    products = ["apple", "banana", "cherry"]
    prices = [1.5, 0.75, 2.0]
    Ожидаемый результат: {"apple": 1.5, "banana": 0.75, "cherry": 2.0}

12.3 Что будет если списки разной длины? Проверь с zip() и напечатай результат:
    keys2 = ["a", "b", "c", "d"]
    values2 = [1, 2]
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 13: Группировка данных")
print("=" * 60)
print("""
13.1 Сгруппируй список студентов по их оценке:
    students = [
        {"name": "Alice", "grade": "A"},
        {"name": "Bob", "grade": "B"},
        {"name": "Charlie", "grade": "A"},
        {"name": "Diana", "grade": "B"},
        {"name": "Eve", "grade": "C"},
    ]
    Ожидаемый результат:
    {"A": ["Alice", "Charlie"], "B": ["Bob", "Diana"], "C": ["Eve"]}

    Подсказка: используй setdefault() или проверяй наличие ключа
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 14: Фильтрация словаря")
print("=" * 60)
print("""
14.1 Оставь только пары, где значение > 50 (через comprehension):
    data = {"a": 30, "b": 70, "c": 10, "d": 90, "e": 50}
    Ожидаемый результат: {"b": 70, "d": 90}

14.2 Оставь только пары, где ключ начинается на гласную (a, e, i, o, u):
    words = {"apple": 1, "banana": 2, "orange": 3, "grape": 4, "ice": 5}
    Ожидаемый результат: {"apple": 1, "orange": 3, "ice": 5}

14.3 Создай новый словарь, где все значения умножены на 2,
    но только для ключей с нечётными значениями:
    nums = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
    Ожидаемый результат: {"a": 2, "c": 6, "e": 10}
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 15: Глубокие вложенные структуры")
print("=" * 60)
print("""
15.1 Работа с вложенным словарём компании:
    company = {
        "name": "TechCorp",
        "departments": {
            "engineering": {
                "head": "Alice",
                "employees": ["Bob", "Charlie", "Diana"],
                "budget": 500000
            },
            "marketing": {
                "head": "Eve",
                "employees": ["Frank"],
                "budget": 200000
            }
        }
    }

    a) Напечатай имя главы engineering
    b) Напечатай список сотрудников marketing
    c) Добавь "Grace" в список сотрудников engineering
    d) Увеличь бюджет marketing на 50000
    e) Напечатай суммарный бюджет всех отделов
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 16: Паттерн накопления и подсчёта")
print("=" * 60)
print("""
16.1 Дан список транзакций. Посчитай баланс каждого пользователя:
    transactions = [
        ("Alice", 100),
        ("Bob", 200),
        ("Alice", -50),
        ("Charlie", 300),
        ("Bob", -75),
        ("Alice", 25),
    ]
    Ожидаемый результат: {"Alice": 75, "Bob": 125, "Charlie": 300}

16.2 Найди пользователя с наибольшим балансом из 16.1

16.3 Найди пользователей с отрицательным балансом (если есть).
    Если нет — напечатай "Все балансы положительные"
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

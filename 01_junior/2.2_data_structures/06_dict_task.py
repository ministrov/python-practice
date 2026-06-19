# -*- coding: utf-8 -*-
"""
Блок 2.2.3: Практика со словарями (dict)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Напиши свой код и выведи результаты.

Совет: Если застрял — посмотри 05_dict_demo.py, но старайся решить сам.
"""

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
film_info = {
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
car_info = {"brand": "Toyota", "model": "Camry", "year": 2020}
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
letter_dict = {"a": 1, "b": 2, "c": 3, "d": 4}
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
coordinate = {"x": 10, "y": 20, "z": 30}
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

grades_values = grades.values()
for i in grades_values:
    sum = 0
    sum += i
    average = sum / len(grades_values)
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


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Dictionary Comprehension")
print("=" * 60)
print("""
8.1 Создай словарь квадратов чисел от 1 до 5 через comprehension
    {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

8.2 Создай словарь с comprehension, где только четные числа:
    {2: 4, 4: 16}

8.3 Инвертируй словарь (ключи ↔ значения) через comprehension:
    Исходный: {"a": 1, "b": 2, "c": 3}
    Результат: {1: "a", 2: "b", 3: "c"}
""")

# ТВ ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

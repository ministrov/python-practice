# -*- coding: utf-8 -*-
"""
Блок 2.3.1: Практика — Основы функций
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 01_functions_basics_demo.py если застрял.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Определение и вызов функции")
print("=" * 60)
print("""
1.1 Напиши функцию square(n), которая возвращает квадрат числа n
    Вызови её с аргументами 4, 7, 10
    Ожидаемый результат: 16, 49, 100

1.2 Напиши функцию is_even(n), которая возвращает True если n чётное
    Проверь: is_even(4) -> True, is_even(7) -> False

1.3 Напиши функцию greet(name), которая выводит (print) "Hello, {name}!"
    Проверь что возвращает None
""")

# ТВОЙ КОД ЗДЕСЬ:


def square(n: int) -> int:
    return n ** 2


print(square(4))
print(square(7))
print(square(10))


def is_even(n: int) -> bool:
    return n % 2 == 0


print(is_even(4))
print(is_even(7))


def greet(name: str) -> None:
    print(f"Hello, {name}!")


print(greet("Anton"))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Позиционные и именованные аргументы")
print("=" * 60)
print("""
2.1 Напиши функцию make_email(username, domain), которая
    возвращает строку вида "username@domain"
    Вызови позиционно: make_email("alice", "gmail.com")
    Вызови именованно: make_email(domain="yandex.ru", username="bob")

2.2 Напиши функцию rectangle_area(width, height), которая
    возвращает площадь прямоугольника
    Вызови оба способа (позиционно и именованно)
""")

# ТВОЙ КОД ЗДЕСЬ:


def make_email(username: str, domain: str) -> str:
    return f"{username}@{domain}"


print(make_email("alice", "gmail.com"))
print(make_email(domain="yandex.ru", username="bob"))


def rectangle_area(width: int, height: int) -> int:
    return width * height


print(rectangle_area(12, 34))
print(rectangle_area(width=23, height=23))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Значения по умолчанию")
print("=" * 60)
print("""
3.1 Напиши функцию repeat(text, times=3), которая
    возвращает строку text, повторённую times раз через пробел
    repeat("ha") -> "ha ha ha"
    repeat("go", 2) -> "go go"

3.2 Напиши функцию introduce(name, role="студент", lang="Python"), которая
    возвращает "Я {name}, {role}, изучаю {lang}"
    Проверь с разными комбинациями аргументов (минимум 3 вызова)
""")

# ТВОЙ КОД ЗДЕСЬ:


def repeat(text: str, times: int = 3) -> str:
    return " ".join([text] * times)


print(repeat("dfdf"))
print(repeat("mey", 4))


def introduce(name: str, role: str = "студент", lang: str = "Python") -> str:
    return f"Я {name}, {role}, изучаю {lang}"


print(introduce("Anton", "Professor", "Go"))
print(introduce("Gilbert"))
print(introduce(name="Dave", role="Student", lang="JavaScript"))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Ловушка mutable default")
print("=" * 60)
print("""
4.1 Напиши функцию append_to(item, target=None), где target — список.
    Если target is None — создай новый список внутри функции.
    Добавь item в список и верни его.

    Проверь что каждый вызов без аргумента target даёт НОВЫЙ список:
    append_to(1)    -> [1]
    append_to(2)    -> [2]   (не [1, 2]!)
    append_to(3, [10, 20]) -> [10, 20, 3]
""")

# ТВОЙ КОД ЗДЕСЬ:


def append_to(item: int, target: list[int] | None = None) -> list[int]:
    if target is None:
        target = []
    target.append(item)
    return target


print(append_to(1))
print(append_to(2))
print(append_to(3, [10, 30]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: Возврат нескольких значений")
print("=" * 60)
print("""
5.1 Напиши функцию stats(numbers), которая принимает список чисел
    и возвращает кортеж (минимум, максимум, среднее)
    Среднее округли до 2 знаков через round()

    stats([1, 2, 3, 4, 5]) -> (1, 5, 3.0)
    stats([10, 20, 30])     -> (10, 30, 20.0)

5.2 Распакуй результат в три переменные и выведи каждую отдельно
""")

# ТВОЙ КОД ЗДЕСЬ:


def stats(numbers: list[int]) -> tuple[int, int, float]:
    average: float = round(sum(numbers) / len(numbers), 2)
    return (min(numbers), max(numbers), average)


print(stats([1, 2, 3, 4, 5]))
print(stats([10, 20, 30]))

result = stats([1, 2, 3, 5])
min_value, max_value, average_value = result

print(min_value, max_value, average_value)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Ранний return (guard clause)")
print("=" * 60)
print("""
6.1 Напиши функцию safe_divide(a, b), которая:
    - Если b == 0: выводит сообщение и возвращает None
    - Иначе: возвращает a / b (float)
    Проверь: safe_divide(10, 2) -> 5.0
             safe_divide(5, 0)  -> None (с сообщением)

6.2 Напиши функцию get_first(items), которая:
    - Если список пустой: возвращает None
    - Иначе: возвращает первый элемент
    Проверь с пустым и непустым списком
""")

# ТВОЙ КОД ЗДЕСЬ:


def safe_divide(a: int, b: int) -> float | None:
    if b == 0:
        print("Ошибка: деление на ноль")
        return None
    return a / b


print(safe_divide(10, 2))
print(safe_divide(5, 0))


def get_first(items: list[int]) -> int | None:
    if len(items) == 0:
        return None
    return items[0]


print(get_first([21, 3, 45]))
print(get_first([]))


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Аннотации типов и docstring")
print("=" * 60)
print("""
7.1 Напиши функцию celsius_to_fahrenheit(c) с:
    - Аннотацией параметра (float) и возврата (float)
    - Docstring (одна строка что делает)
    - Формула: F = C * 9/5 + 32
    Проверь: celsius_to_fahrenheit(0) -> 32.0
             celsius_to_fahrenheit(100) -> 212.0

7.2 Напиши функцию count_vowels(text) с аннотациями:
    - Принимает str, возвращает int
    - Считает гласные (a, e, i, o, u) без учёта регистра
    Проверь: count_vowels("Hello") -> 2
             count_vowels("Python") -> 1
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное задание")
print("=" * 60)
print("""
Напиши функцию summarize_grades(grades, passing=60), где:
  - grades: dict[str, int] — словарь {имя: оценка}
  - passing: int — порог прохождения (по умолчанию 60)

Функция должна возвращать dict со структурой:
  {
    "total": количество студентов,
    "passed": количество сдавших (оценка >= passing),
    "failed": количество не сдавших,
    "average": средняя оценка (round до 1 знака),
    "best": имя студента с наивысшей оценкой
  }

Проверь с данными:
  grades = {"Alice": 85, "Bob": 42, "Charlie": 91, "Diana": 67, "Eve": 55}
  результат при passing=60:
    total=5, passed=3, failed=2, average=68.0, best="Charlie"
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

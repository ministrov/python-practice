# -*- coding: utf-8 -*-
"""
Блок 2.6.1: Практика — аннотации типов
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 01_type_annotations_demo.py если застрял.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: list[float]")
print("=" * 60)
print("""
1.1 Напиши average(numbers: list[float]) -> float, которая
    возвращает среднее арифметическое.
1.2 Проверь: average([2.0, 4.0, 6.0]) -> 4.0
""")

# ТВОЙ КОД ЗДЕСЬ:


def average(numbers: list[float]) -> float:
    return sum(numbers) / len(numbers)


print(average([2.0, 4.0, 6.0]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: dict[str, int]")
print("=" * 60)
print("""
2.1 Напиши merge_counts(a: dict[str, int], b: dict[str, int])
    -> dict[str, int], которая складывает счётчики по одинаковым
    ключам (если ключ есть только в одном словаре — берёт как есть).
2.2 Проверь: merge_counts({"a": 1, "b": 2}, {"b": 3, "c": 4})
    -> {"a": 1, "b": 5, "c": 4}
""")

# ТВОЙ КОД ЗДЕСЬ:


def merge_counts(a: dict[str, int], b: dict[str, int]) -> dict[str, int]:
    result = dict(a)

    for key, value in b.items():
        result[key] = result.get(key, 0) + value
    return result


print(merge_counts({"a": 1, "b": 2}, {"b": 3, "c": 4}))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: tuple[int, int] — фиксированная длина")
print("=" * 60)
print("""
3.1 Напиши swap(pair: tuple[int, int]) -> tuple[int, int], которая
    возвращает пару элементов в обратном порядке.
3.2 Проверь: swap((1, 2)) -> (2, 1)
""")

# ТВОЙ КОД ЗДЕСЬ:


def swap(pair: tuple[int, int]) -> tuple[int, int]:
    num_1, num_2 = pair

    return (num_2, num_1)


print(swap((1, 2)))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: X | None (Optional)")
print("=" * 60)
print("""
4.1 Напиши find_age(users: dict[str, int], name: str) -> int | None,
    которая возвращает возраст по имени, или None, если такого
    имени в словаре нет.
4.2 Проверь на users = {"Ann": 25, "Bob": 30}: find_age(users, "Ann")
    -> 25, find_age(users, "Nobody") -> None
""")

# ТВОЙ КОД ЗДЕСЬ:


users = {"Ann": 25, "Bob": 30}


def find_age(users: dict[str, int], name: str) -> int | None:
    if name not in users:
        return None

    return users[name]


print(find_age(users, "Ann"))
print(find_age(users, "Nobody"))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: X | Y (Union)")
print("=" * 60)
print("""
5.1 Напиши to_number(raw: str) -> int | float, которая возвращает
    int, если строка похожа на целое число, иначе float.
5.2 Проверь: to_number("10") -> 10 (int), to_number("2.5") -> 2.5
    (float)
""")

# ТВОЙ КОД ЗДЕСЬ:


def to_number(raw: str) -> int | float:
    try:
        return int(raw)
    except ValueError:
        return float(raw)


print(to_number("10"), type(to_number("10")))
print(to_number("2.5"), type(to_number("2.5")))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Вложенные generic-типы")
print("=" * 60)
print("""
6.1 Напиши words_by_length(words: list[str]) -> dict[int, list[str]],
    которая группирует слова по их длине.
6.2 Проверь: words_by_length(["a", "bb", "cc", "ddd"])
    -> {1: ["a"], 2: ["bb", "cc"], 3: ["ddd"]}
""")

# ТВОЙ КОД ЗДЕСЬ:


def words_by_length(words: list[str]) -> dict[int, list[str]]:
    grouped: dict[int, list[str]] = {}

    for word in words:
        grouped.setdefault(len(word), []).append(word)
    return grouped


print(words_by_length(["a", "bb", "cc", "ddd"]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: X | None как значение по умолчанию параметра")
print("=" * 60)
print("""
7.1 Напиши greet(name: str | None = None) -> str. Если name — None,
    используй "Гость" вместо имени.
7.2 Проверь: greet("Антон") -> "Привет, Антон!",
    greet() -> "Привет, Гость!"
""")

# ТВОЙ КОД ЗДЕСЬ:


print(greet("Антон"))
print(greet())

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное")
print("=" * 60)
print("""
8.1 Напиши split_by_status(
        items: list[tuple[str, bool]],
    ) -> dict[str, list[str]]
    Вход — список пар (имя, готов_ли). Раздели имена на два списка
    в словаре с ключами "ready" и "not_ready".
8.2 Проверь: split_by_status(
        [("Alice", True), ("Bob", False), ("Cara", True)]
    ) -> {"ready": ["Alice", "Cara"], "not_ready": ["Bob"]}
""")

# ТВОЙ КОД ЗДЕСЬ:


print(split_by_status([("Alice", True), ("Bob", False), ("Cara", True)]))

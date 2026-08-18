# -*- coding: utf-8 -*-
"""
Блок 2.6.2: Практика — модуль typing (Any, Callable, Iterable, Sequence,
TypedDict)
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 03_typing_module_demo.py если застрял.
"""

from typing import Any, Callable, Iterable, Sequence, TypedDict

print("=" * 60)
print("ЗАДАНИЕ 1: Callable — функция как параметр")
print("=" * 60)
print("""
1.1 Напиши apply_to_all(func: Callable[[int], int], numbers: list[int])
    -> list[int], которая применяет func к каждому числу.
1.2 Проверь: apply_to_all(lambda x: x * 2, [1, 2, 3]) -> [2, 4, 6]
""")

# ТВОЙ КОД ЗДЕСЬ:


def apply_to_all(func: Callable[[int], int], numbers: list[int]) -> list[int]:
    results: list[int] = []

    for num in numbers:
        doubled = func(num)
        results.append(doubled)

    return results


print(apply_to_all(lambda x: x * 2, [1, 2, 3]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Callable — функция как результат")
print("=" * 60)
print("""
2.1 Напиши make_multiplier(factor: int) -> Callable[[int], int],
    которая возвращает функцию, умножающую свой аргумент на factor.
2.2 Проверь: triple = make_multiplier(3); triple(5) -> 15
""")

# ТВОЙ КОД ЗДЕСЬ:


def make_multiplier(factor: int) -> Callable[[int], int]:
    def multiplier(x: int):
        return x * factor
    return multiplier


triple = make_multiplier(3)
print(triple(5))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Iterable — принимай абстрактно")
print("=" * 60)
print("""
3.1 Напиши count_positive(numbers: Iterable[int]) -> int, которая
    считает, сколько чисел больше нуля. Функция должна работать и на
    list, и на генераторе (то есть проходить numbers только ОДИН раз
    циклом for, без len() и без обращения по индексу).
3.2 Проверь: count_positive([1, -2, 3, -4, 5]) -> 3
    count_positive(x for x in [1, -2, 3]) -> 2
""")

# ТВОЙ КОД ЗДЕСЬ:


def count_positive(numbers: Iterable[int]) -> int:
    count: int = 0

    for num in numbers:
        if num > 0:
            count += 1

    return count


print(count_positive([1, -2, 3, -4, 5]))
print(count_positive(x for x in [1, -2, 3]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Sequence — нужна индексация")
print("=" * 60)
print("""
4.1 Напиши middle_element(items: Sequence[str]) -> str, которая
    возвращает средний элемент (для нечётной длины). Используй
    индексацию items[i], а не list(items).
4.2 Проверь: middle_element(["a", "b", "c"]) -> "b"
    middle_element(("x", "y", "z", "w", "v")) -> "z"
""")

# ТВОЙ КОД ЗДЕСЬ:


print(middle_element(["a", "b", "c"]))
print(middle_element(("x", "y", "z", "w", "v")))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: TypedDict — фиксированная схема")
print("=" * 60)
print("""
5.1 Объяви TypedDict с именем Product с полями:
    name: str, price: float, in_stock: bool
5.2 Напиши format_product(product: Product) -> str, которая
    возвращает строку вида "Ноутбук: 999.99 (в наличии)" или
    "Ноутбук: 999.99 (нет в наличии)".
5.3 Проверь на {"name": "Ноутбук", "price": 999.99, "in_stock": True}
""")

# ТВОЙ КОД ЗДЕСЬ:


laptop: Product = {"name": "Ноутбук", "price": 999.99, "in_stock": True}
print(format_product(laptop))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Any — граница с нетипизированными данными")
print("=" * 60)
print("""
6.1 Напиши extract_names(records: list[dict[str, Any]]) -> list[str],
    которая достаёт значение по ключу "name" из каждого словаря
    (предполагай, что ключ "name" есть всегда).
6.2 Проверь: extract_names(
        [{"name": "Ann", "age": 25}, {"name": "Bob", "score": 4.5}]
    ) -> ["Ann", "Bob"]
""")

# ТВОЙ КОД ЗДЕСЬ:


print(extract_names(
    [{"name": "Ann", "age": 25}, {"name": "Bob", "score": 4.5}]))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Callable[..., Any] — универсальный колбэк")
print("=" * 60)
print("""
7.1 Напиши call_and_double_time(func: Callable[..., int]) -> int,
    которая вызывает func() без аргументов и возвращает результат,
    умноженный на 2.
7.2 Проверь: call_and_double_time(lambda: 21) -> 42
""")

# ТВОЙ КОД ЗДЕСЬ:


print(call_and_double_time(lambda: 21))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное — Sequence + TypedDict")
print("=" * 60)
print("""
8.1 Объяви TypedDict с именем Task с полями: title: str, done: bool
8.2 Напиши count_done(tasks: Sequence[Task]) -> int, которая
    считает количество задач с done=True.
8.3 Проверь: count_done([
        {"title": "A", "done": True},
        {"title": "B", "done": False},
        {"title": "C", "done": True},
    ]) -> 2
""")

# ТВОЙ КОД ЗДЕСЬ:


tasks: list[Task] = [
    {"title": "A", "done": True},
    {"title": "B", "done": False},
    {"title": "C", "done": True},
]
print(count_done(tasks))

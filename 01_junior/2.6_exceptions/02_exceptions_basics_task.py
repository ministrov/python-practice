# -*- coding: utf-8 -*-
"""
Блок 2.6.1: Практика — основы обработки ошибок
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 01_exceptions_basics_demo.py если застрял.
"""

from typing import Any

print("=" * 60)
print("ЗАДАНИЕ 1: Базовый try/except")
print("=" * 60)
print("""
1.1 Напиши safe_divide(a, b), которая делит a на b.
1.2 Если b == 0 — поймай ZeroDivisionError, напечатай понятное
    сообщение и верни None.
1.3 Проверь: safe_divide(10, 2) -> 5.0, safe_divide(10, 0) -> None
    (с сообщением об ошибке).
""")

# ТВОЙ КОД ЗДЕСЬ:


def safe_divide(a: int, b: int) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Делить на ноль запрещено")


print(safe_divide(10, 2))
print(safe_divide(10, 0))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Несколько except подряд")
print("=" * 60)
print("""
2.1 Напиши parse_int(value: str), которая пытается вернуть int(value).
2.2 Отдельно поймай ValueError (не число) и отдельно TypeError
    (например, если передали не строку, а None) — с РАЗНЫМИ
    сообщениями для каждого случая. В обоих случаях верни None.
2.3 Проверь на: "42", "abc", None.
""")

# ТВОЙ КОД ЗДЕСЬ:


def parse_int(value: Any) -> int | None:
    try:
        return int(value)
    except ValueError:
        print(f"Ошибка: '{value}' — это не число (ValueError)")
        return None
    except TypeError:
        print(
            f"Ошибка: передан не подходящий тип {type(value).__name__} вместо строки/числа (TypeError)")
        return None


print(parse_int("42"))
print(parse_int("abc"))
print(parse_int(None))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: Один except на несколько типов + as e")
print("=" * 60)
print("""
3.1 Напиши get_item(items: list, index), которая возвращает
    items[index].
3.2 Одним except поймай СРАЗУ IndexError и TypeError (кортежем типов),
    через `as e` напечатай f"Ошибка: {type(e).__name__}: {e}",
    верни None.
3.3 Проверь: get_item([1,2,3], 1), get_item([1,2,3], 99),
    get_item([1,2,3], "x").
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: else и finally")
print("=" * 60)
print("""
4.1 Напиши convert_to_positive(n: float), которая:
    - если n < 0, поднимает ValueError("число отрицательное")
    - в except ловит ValueError, печатает сообщение, возвращает None
    - в else (только если ошибки не было) печатает "OK" и возвращает n
    - в finally печатает "Проверка завершена" (всегда, при любом исходе)
4.2 Проверь на 5 и на -3, посмотри порядок печати в обоих случаях.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 5: raise вручную")
print("=" * 60)
print("""
5.1 Напиши validate_age(age: int) -> int:
    - если age < 0 или age > 150 — raise ValueError с понятным
      сообщением, включающим само значение age
    - иначе верни age
5.2 Вызови validate_age(200) внутри try/except, поймай ValueError,
    напечатай текст ошибки.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 6: Иерархия исключений")
print("=" * 60)
print("""
6.1 Дан код:
    try:
        {"a": 1}["b"]
    except Exception as e:
        ...
    Прогноз ДО запуска: какой именно тип исключения попадёт в `e`
    (не Exception — какой РЕАЛЬНЫЙ тип, KeyError или что-то другое)?
    Впиши прогноз в комментарий, потом проверь код и сверь.
6.2 Своими словами объясни (в комментарии): почему except Exception
    поймал ошибку, хотя явно указан не тот тип, что реально произошёл?
""")

# ТВОЙ ПРОГНОЗ 6.1:

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 7: Своё исключение")
print("=" * 60)
print("""
7.1 Создай класс NegativeBalanceError(Exception), который в __init__
    принимает amount: float и формирует сообщение вида
    f"Баланс не может стать отрицательным: {amount}".
7.2 Напиши withdraw(balance: float, amount: float) -> float:
    - если amount > balance — raise NegativeBalanceError(amount - balance)
    - иначе верни balance - amount
7.3 Вызови withdraw(100, 150) внутри try/except NegativeBalanceError,
    напечатай текст ошибки.
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("ЗАДАНИЕ 8: Комплексное — обработка списка операций")
print("=" * 60)
print("""
8.1 Дан список операций (каждая — кортеж (a, b), нужно поделить a / b):
    operations = [(10, 2), (5, 0), (9, 3), ("x", 2)]
8.2 Напиши process_operations(operations), которая в цикле для каждой
    пары пытается посчитать a / b и печатает результат в формате
    f"{a} / {b} = {результат}". Если деление невозможно (ZeroDivisionError
    или TypeError) — печатает f"{a} / {b} -> ошибка: {тип_ошибки}" и
    продолжает со следующей операцией (одна ошибка не должна прерывать
    обработку всего списка).
8.3 В конце (после всех операций, через finally или просто после цикла)
    напечатай "Обработка завершена".
""")

# ТВОЙ КОД ЗДЕСЬ:


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)

# -*- coding: utf-8 -*-
"""
Блок 2.3.4: Демо — функции как объекты первого класса
════════════════════════════════════════════════════════════════════════
Темы:
  1. Функция — обычный объект: присваивание переменной
  2. Передача функции как аргумента (функция высшего порядка)
  3. Возврат функции из функции (без замыкания — просто ссылка)
  4. Хранение функций в структурах данных (dispatch table)
  5. Атрибуты функции: __name__, __doc__
  6. lambda — анонимные функции
  7. Встроенные функции высшего порядка: map(), filter(), sorted(key=...),
     reduce()
"""

from collections.abc import Callable
from functools import reduce

# ════════════════════════════════════════════════════════════════════════
# 1. Функция — обычный объект
# ════════════════════════════════════════════════════════════════════════
# Имя функции — это просто переменная, ссылающаяся на объект-функцию.
# Её можно присвоить другому имени, как любое другое значение.


def square(x: int) -> int:
    """Возвращает квадрат числа."""
    return x * x


my_func = square       # НЕ square() — без скобок, это ссылка на сам объект
print(my_func(5))      # 25
print(my_func is square)  # True — это один и тот же объект


# ════════════════════════════════════════════════════════════════════════
# 2. Функция как аргумент (функция высшего порядка)
# ════════════════════════════════════════════════════════════════════════
# Функция, которая принимает другую функцию как аргумент (или возвращает
# функцию), называется функцией высшего порядка (higher-order function).

def apply_twice(func: Callable[[int], int], value: int) -> int:
    """Применяет func к value дважды подряд."""
    return func(func(value))


def increment(x: int) -> int:
    return x + 1


print(apply_twice(square, 3))     # square(square(3)) = square(9) = 81
print(apply_twice(increment, 3))  # increment(increment(3)) = 5


# ════════════════════════════════════════════════════════════════════════
# 3. Функция как возвращаемое значение (без замыкания)
# ════════════════════════════════════════════════════════════════════════
# В отличие от фабрик из темы 3 (LEGB), здесь функция просто выбирает
# и возвращает уже существующую функцию — не создаёт новую с состоянием.

def double(x: int) -> int:
    return x * 2


def negate(x: int) -> int:
    return -x


def choose_operation(name: str):
    """Возвращает нужную функцию по имени операции."""
    if name == "double":
        return double
    if name == "negate":
        return negate
    raise ValueError(f"Неизвестная операция: {name}")


operation = choose_operation("double")
print(operation(7))  # 14


# ════════════════════════════════════════════════════════════════════════
# 4. Функции в структурах данных (dispatch table)
# ════════════════════════════════════════════════════════════════════════
# Словарь "имя операции -> функция" — частая замена длинной цепочке
# if/elif/else. Называется dispatch table (таблица диспетчеризации).

operations = {
    "square": square,
    "double": double,
    "negate": negate,
}

print(operations["square"](6))  # 36

for op_name, func in operations.items():
    print(f"{op_name}(4) = {func(4)}")


# ════════════════════════════════════════════════════════════════════════
# 5. У функций есть атрибуты
# ════════════════════════════════════════════════════════════════════════

print(square.__name__)  # "square"
print(square.__doc__)   # "Возвращает квадрат числа."


# ════════════════════════════════════════════════════════════════════════
# 6. lambda — анонимная функция "на один раз"
# ════════════════════════════════════════════════════════════════════════
# lambda аргументы: выражение
# Может содержать только ОДНО выражение (не блок кода), возвращает его
# результат неявно (без слова return). Используется, когда функция
# нужна один раз и не заслуживает отдельного def с именем.

square_lambda: Callable[[int], int] = lambda x: x * x
print(square_lambda(5))  # 25

add: Callable[[int, int], int] = lambda a, b: a + b
print(add(2, 3))  # 5


# ════════════════════════════════════════════════════════════════════════
# 7. Встроенные функции высшего порядка: map, filter, sorted, reduce
# ════════════════════════════════════════════════════════════════════════

numbers = [1, 2, 3, 4, 5, 6]

# map(func, iterable) — применяет func к каждому элементу, возвращает
# ленивый итератор (нужно обернуть в list(), чтобы увидеть все значения)
squared = list(map(lambda x: x * x, numbers))
print(squared)  # [1, 4, 9, 16, 25, 36]

# filter(func, iterable) — оставляет только элементы, где func(x) истинно
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6]

# sorted(iterable, key=func) — func вычисляет "ключ сортировки" для
# каждого элемента, сама сортировка идёт по этим ключам
words = ["banana", "kiwi", "apple", "fig"]
by_length = sorted(words, key=lambda w: len(w))
print(by_length)  # ['fig', 'kiwi', 'apple', 'banana']

people = [("Anna", 25), ("Boris", 19), ("Vera", 32)]
by_age = sorted(people, key=lambda person: person[1])
print(by_age)  # [('Boris', 19), ('Anna', 25), ('Vera', 32)]

# На практике list/dict/set comprehensions (тема 2.2) чаще предпочтительнее
# map/filter — они читаются линейнее. Но map/filter/sorted(key=...) —
# стандартный инструмент, который встретится в чужом коде повсеместно.

# reduce(func, iterable, initial) — сворачивает итерируемое в одно
# значение: последовательно применяет func(accumulator, item), передавая
# результат каждого шага в следующий. initial задаёт стартовое значение
# accumulator (и то, что вернётся, если iterable пуст).
total = reduce(lambda acc, x: acc + x, numbers, 0)
print(total)  # 21 — (((((0+1)+2)+3)+4)+5)+6

product = reduce(lambda acc, x: acc * x, numbers, 1)
print(product)  # 720 — 1*2*3*4*5*6

maximum = reduce(lambda acc, x: acc if acc > x else x, numbers)
print(maximum)  # 6 — initial не задан, стартует с numbers[0]

joined = reduce(lambda acc, w: acc + "-" + w, words)
print(joined)  # banana-kiwi-apple-fig

# Без initial reduce падает с TypeError на пустом iterable — initial
# делает функцию безопасной для этого случая.
empty: list[int] = []
print(reduce(lambda acc, x: acc + x, empty, 0))  # 0

# sum()/max()/min() — частные случаи reduce для чисел; используйте их
# вместо reduce, когда задача укладывается в готовую встроенную функцию.

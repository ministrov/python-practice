# -*- coding: utf-8 -*-
"""
Блок 2.3.3: Практика — области видимости (LEGB), global, nonlocal
════════════════════════════════════════════════════════════════════════
8 ЗАДАНИЙ для самостоятельного решения.
Совет: посмотри 05_legb_demo.py если застрял.
"""

print("=" * 60)
print("ЗАДАНИЕ 1: Глобальная область видимости")
print("=" * 60)
print("""
1.1 Дана глобальная переменная counter = 0.
    Напиши функцию show_counter(), которая печатает текущее
    значение counter (просто читает, без global).

1.2 Напиши функцию increment_counter(), которая увеличивает
    глобальный counter на 1 (используй global).
    Вызови её 3 раза и покажи, что counter стал равен 3.
""")

counter = 0

# ТВОЙ КОД ЗДЕСЬ:


def show_counter():
    print(f"{counter}")


def increment_counter():
    global counter
    counter += 1
    return counter


counter_a = increment_counter()
counter_b = increment_counter()
counter_c = increment_counter()

show_counter()
print(counter_a)
print(counter_b)
print(counter_c)

print("\n" + "=" * 60)
print("ЗАДАНИЕ 2: Замыкания (closures) и nonlocal")
print("=" * 60)
print("""
2.1 Напиши функцию-фабрику make_counter(), которая возвращает
    функцию increment(), увеличивающую счётчик при каждом вызове.
    counter_a = make_counter()
    counter_a() -> 1
    counter_a() -> 2
    counter_a() -> 3

2.2 Напиши make_multiplier(factor), возвращающую функцию,
    которая умножает переданное число на factor.
    double = make_multiplier(2)
    double(5)  -> 10
    triple = make_multiplier(3)
    triple(5)  -> 15
""")

# ТВОЙ КОД ЗДЕСЬ:


def make_counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count
    return increment


counter_1 = make_counter()

print(counter_1())
print(counter_1())
print(counter_1())


def make_multiplier(factor: int):
    def multiply(value: int):
        return value * factor
    return multiply


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))

print("\n" + "=" * 60)
print("ЗАДАНИЕ 3: LEGB и затенение (shadowing)")
print("=" * 60)
print("""
3.1 Дана глобальная переменная name = "Global".
    Напиши функцию local_shadow(), которая создаёт локальную
    переменную name = "Local" и печатает её.
    После вызова функции распечатай глобальный name снаружи —
    покажи, что он не изменился.

3.2 Напиши функцию broken_counter(), которая пытается сделать
    total += 1 БЕЗ global/nonlocal (используй уже существующую
    глобальную total = 100). Оберни вызов в try/except
    UnboundLocalError и выведи текст ошибки.
    Затем напиши исправленную версию fixed_counter() с global,
    которая корректно увеличивает total.
""")

name = "Global"
total = 100

# ТВОЙ КОД ЗДЕСЬ:


def local_shadow():
    name = "Local"
    print(name)


local_shadow()
print(name)


def broken_counter():
    total += 1  # type: ignore[reportUnboundVariable]  # намеренно: демонстрация UnboundLocalError


try:
    broken_counter()
except UnboundLocalError as e:
    print(f"UnboundLocalError: {e}")


def fixed_counter():
    global total
    total += 1
    return total


print(fixed_counter())
print(fixed_counter())


print("\n" + "=" * 60)
print("ЗАДАНИЕ 4: Практическое применение замыканий")
print("=" * 60)
print("""
4.1 Напиши make_accumulator(), возвращающую функцию add(value),
    которая хранит бегущую сумму (nonlocal) и возвращает её
    после каждого добавления.
    acc = make_accumulator()
    acc(10) -> 10
    acc(5)  -> 15
    acc(20) -> 35

4.2 Напиши make_greeter(greeting), возвращающую функцию
    greet(name) -> f"{greeting}, {name}!".
    Создай hello = make_greeter("Привет") и hi = make_greeter("Hi").
    Покажи, что они независимы друг от друга (разные greeting).
""")

# ТВОЙ КОД ЗДЕСЬ:


def make_accumulator():
    total = 0

    def add(value: int):
        nonlocal total
        total += value
        return total
    return add


acc = make_accumulator()

print(acc(4))
print(acc(6))
print(acc(7))


def make_greeter(greeting: str):
    def greet(name: str):
        return f"{greeting}, {name}!"
    return greet


hello = make_greeter("Привет")
hi = make_greeter("Hi")

print(hello("Аня"))  # Привет, Аня!
print(hi("Anna"))


print("\n" + "=" * 60)
print("КОНЕЦ ЗАДАНИЙ, ПРОВЕРЬ ЧТО ВСЕ ЗАДАНИЯ РАБОТАЮТ!")
print("=" * 60)
